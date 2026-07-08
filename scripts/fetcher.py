#!/usr/bin/env python3
"""
Fetch Anthropic documentation from all known sources.

Sources (see sources.json for the complete registry):
  - platform.claude.com     -> API/platform docs (sitemap + .md suffix)
  - code.claude.com         -> Claude Code + Agent SDK (llms.txt + .md suffix)
  - modelcontextprotocol.io -> MCP spec (sitemap + .md suffix)
  - support.claude.com      -> Help articles (sitemap + .md suffix)
  - anthropic.com blog      -> FROZEN 2026-07 (HTML-only, no .md variant;
                               the jina.ai proxy path was removed)
  - github.com/anthropics/* -> Repos (raw.githubusercontent.com)

Usage:
  uv run scripts/fetcher.py                       # Fetch all
  uv run scripts/fetcher.py --tree                 # Show source structure
  uv run scripts/fetcher.py --discover             # Probe domains for new sources
  uv run scripts/fetcher.py --section claude-code  # Single section
  uv run scripts/fetcher.py --section mcp          # MCP spec docs
  uv run scripts/fetcher.py --section github       # GitHub repos
"""
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "aiohttp",
#   "aiofiles",
#   "tqdm",
# ]
# ///

import asyncio
import hashlib
import json
import os
import re
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import aiofiles
import aiohttp
from tqdm.asyncio import tqdm_asyncio


GITHUB_REPOS = [
    ("anthropics/claude-cookbooks",        "main",   [".md", ".ipynb"]),
    ("anthropics/skills",                  "main",   [".md"]),
    ("anthropics/claude-plugins-official",  "main",   [".md", ".json"]),
    ("anthropics/courses",                 "master", [".md", ".ipynb"]),
    ("anthropics/claude-quickstarts",      "main",   [".md"]),
    ("anthropics/claude-code-action",      "main",   [".md"]),
    ("anthropics/cwc-workshops",           "main",   [".md", ".ipynb"]),
    ("anthropics/cwc-long-running-agents", "main",   [".md"]),
    ("anthropics/anthropic-sdk-python",    "main",   [".md"]),
    ("anthropics/anthropic-sdk-typescript","main",   [".md"]),
]

DISCOVER_DOMAINS = [
    ("anthropic.com",           "Main site"),
    ("platform.claude.com",     "API platform docs"),
    ("code.claude.com",         "Claude Code docs"),
    ("support.claude.com",      "Support articles"),
    ("modelcontextprotocol.io", "MCP protocol spec"),
    ("claude.ai",               "Claude app"),
    ("claude.com",              "Product landing"),
]


class Fetcher:
    def __init__(
        self,
        output_dir: str = "content",
        jobs: int = 50,
        incremental: bool = False,
        section: Optional[str] = None,
    ):
        self.output_dir = Path(output_dir)
        self.jobs = jobs
        self.incremental = incremental
        self.section = section

        self.platform_sitemap_url = "https://platform.claude.com/sitemap.xml"
        self.claude_code_llms_url = "https://code.claude.com/docs/llms.txt"
        self.mcp_sitemap_url = "https://modelcontextprotocol.io/sitemap.xml"
        self.support_sitemap_url = "https://support.claude.com/sitemap.xml"

        self.stats = {"total": 0, "downloaded": 0, "skipped": 0, "failed": 0}

    def want(self, *sections: str) -> bool:
        if not self.section or self.section == "all":
            return True
        return self.section in sections

    # -- URL extraction ---------------------------------------------------

    async def fetch_text(self, session: aiohttp.ClientSession, url: str) -> str:
        async with session.get(url) as r:
            r.raise_for_status()
            return await r.text()

    async def fetch_bytes(self, session: aiohttp.ClientSession, url: str) -> bytes:
        async with session.get(url) as r:
            r.raise_for_status()
            return await r.read()

    def extract_sitemap_urls(self, xml: str, must_contain: str = "") -> List[str]:
        urls = []
        for line in xml.split("\n"):
            if "<loc>" not in line:
                continue
            url = line.split("<loc>")[1].split("</loc>")[0]
            if must_contain and must_contain not in url:
                continue
            urls.append(url)
        return urls

    async def fetch_claude_code_urls(self, session: aiohttp.ClientSession) -> List[str]:
        content = await self.fetch_text(session, self.claude_code_llms_url)
        urls = []
        for match in re.findall(r'\(https://code\.claude\.com/docs/en/[^)]+\.md\)', content):
            urls.append(match[1:-4])  # strip parens and .md
        return urls

    def extract_support_urls(self, sitemap_xml: str) -> List[str]:
        # Articles serve a .md variant directly (since ~2026-07), so plain
        # download_doc applies; sitemap covers more articles than llms.txt.
        return [
            url for url in self.extract_sitemap_urls(sitemap_xml)
            if "/en/articles/" in url
        ]

    # -- Output path mapping ----------------------------------------------

    def get_output_path(self, url: str) -> Path:
        if "code.claude.com" in url:
            path = url.replace("https://code.claude.com/docs/", "")
            parts = path.split("/", 1)
            if len(parts) == 2:
                return self.output_dir / parts[0] / "docs" / "claude-code" / f"{parts[1]}.md"
            return self.output_dir / f"{path}.md"
        elif "platform.claude.com" in url:
            path = url.replace("https://platform.claude.com/docs/", "")
            return self.output_dir / f"{path}.md"
        elif "modelcontextprotocol.io" in url:
            path = url.replace("https://modelcontextprotocol.io/", "")
            return self.output_dir / "mcp" / f"{path}.md"
        elif "support.claude.com" in url:
            path = url.replace("https://support.claude.com/en/articles/", "")
            return self.output_dir / "support" / f"{path}.md"
        else:
            path = url.replace("https://", "").split("/", 1)[-1]
            return self.output_dir / f"{path}.md"

    # -- Downloaders -------------------------------------------------------

    async def download_doc(self, session, url, semaphore) -> Dict:
        async with semaphore:
            output_path = self.get_output_path(url)
            if self.incremental and output_path.exists():
                self.stats["skipped"] += 1
                return {"url": url, "status": "skipped"}
            try:
                content = await self.fetch_bytes(session, f"{url}.md")
                output_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)
                self.stats["downloaded"] += 1
                return {
                    "url": url, "status": "success",
                    "path": str(output_path.relative_to(self.output_dir)),
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                }
            except Exception as e:
                self.stats["failed"] += 1
                return {"url": url, "status": "failed", "error": str(e)}

    async def download_github_file(self, session, repo, branch, filepath, semaphore) -> Dict:
        async with semaphore:
            repo_short = repo.split("/")[1]
            output_path = self.output_dir / "github" / repo_short / filepath
            url = f"https://raw.githubusercontent.com/{repo}/{branch}/{filepath}"
            if self.incremental and output_path.exists():
                self.stats["skipped"] += 1
                return {"url": url, "status": "skipped"}
            try:
                content = await self.fetch_bytes(session, url)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)
                self.stats["downloaded"] += 1
                return {
                    "url": url, "status": "success",
                    "path": str(output_path.relative_to(self.output_dir)),
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                }
            except Exception as e:
                self.stats["failed"] += 1
                return {"url": url, "status": "failed", "error": str(e)}

    # -- GitHub repo listing -----------------------------------------------

    def _github_headers(self) -> Dict:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            return {"Authorization": f"token {token}"}
        return {}

    async def list_github_files(self, session, repo, branch, extensions) -> List[str]:
        url = f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1"
        headers = self._github_headers()
        try:
            async with session.get(url, headers=headers) as r:
                if r.status == 403:
                    print(f"  WARN: GitHub rate limit for {repo}", file=sys.stderr)
                    return []
                r.raise_for_status()
                data = await r.json()
        except Exception as e:
            print(f"  WARN: Failed to list {repo}: {e}", file=sys.stderr)
            return []
        files = []
        for item in data.get("tree", []):
            if item["type"] != "blob":
                continue
            if any(item["path"].endswith(ext) for ext in extensions):
                files.append(item["path"])
        return files

    # -- Meta fetchers -----------------------------------------------------

    async def fetch_npm_manifest(self, session) -> Dict:
        url = "https://registry.npmjs.org/@anthropic-ai/claude-code/latest"
        async with session.get(url) as r:
            r.raise_for_status()
            return await r.json()

    async def fetch_github_changelog(self, session) -> bytes:
        url = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
        return await self.fetch_bytes(session, url)

    # -- Orchestration -----------------------------------------------------

    async def fetch_all(self):
        print(f"Fetching to {self.output_dir}")
        print(f"Jobs: {self.jobs}")
        if self.incremental:
            print("Mode: incremental (skip existing)")
        if self.section:
            print(f"Section: {self.section}")
        print()

        timeout = aiohttp.ClientTimeout(total=600)
        connector = aiohttp.TCPConnector(limit=self.jobs)

        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            # -- Meta (always fetch) --
            if self.want("meta", "claude-code"):
                await self._fetch_meta(session)

            tasks = []
            semaphore = asyncio.Semaphore(self.jobs)
            counts = {}

            # -- Platform docs --
            if self.want("api", "platform"):
                print("Source: platform.claude.com/sitemap.xml")
                xml = await self.fetch_text(session, self.platform_sitemap_url)
                urls = self.extract_sitemap_urls(xml, "/docs/en/")
                # Terraform provider reference serves no .md variant (404s)
                terraform = [u for u in urls if "/api/terraform/" in u]
                urls = [u for u in urls if "/api/terraform/" not in u]
                counts["platform"] = len(urls)
                print(f"  {len(urls)} docs"
                      + (f" ({len(terraform)} terraform pages skipped, no .md)"
                         if terraform else ""))
                for url in urls:
                    tasks.append(self.download_doc(session, url, semaphore))

            # -- Claude Code docs --
            if self.want("claude-code"):
                print("Source: code.claude.com/docs/llms.txt")
                urls = await self.fetch_claude_code_urls(session)
                counts["claude-code"] = len(urls)
                print(f"  {len(urls)} docs")
                for url in urls:
                    tasks.append(self.download_doc(session, url, semaphore))

            # -- MCP docs --
            if self.want("mcp"):
                print("Source: modelcontextprotocol.io/sitemap.xml")
                xml = await self.fetch_text(session, self.mcp_sitemap_url)
                urls = self.extract_sitemap_urls(xml)
                counts["mcp"] = len(urls)
                print(f"  {len(urls)} docs")
                for url in urls:
                    tasks.append(self.download_doc(session, url, semaphore))

            # -- Blog (anthropic.com): FROZEN 2026-07 --
            # HTML-only upstream (no llms.txt / .md variant); the jina.ai
            # proxy path was removed. content/blog/ stays as a static archive.

            # -- Support articles --
            if self.want("support"):
                print("Source: support.claude.com/sitemap.xml")
                xml = await self.fetch_text(session, self.support_sitemap_url)
                urls = self.extract_support_urls(xml)
                counts["support"] = len(urls)
                print(f"  {len(urls)} articles")
                for url in urls:
                    tasks.append(self.download_doc(session, url, semaphore))

            # -- GitHub repos --
            if self.want("github"):
                print("Source: github.com/anthropics/*")
                for repo, branch, exts in GITHUB_REPOS:
                    files = await self.list_github_files(session, repo, branch, exts)
                    repo_short = repo.split("/")[1]
                    counts[f"github/{repo_short}"] = len(files)
                    print(f"  {repo_short}: {len(files)} files")
                    for filepath in files:
                        tasks.append(self.download_github_file(
                            session, repo, branch, filepath, semaphore))

            # -- Execute --
            self.stats["total"] = len(tasks)
            total_parts = " + ".join(f"{v} {k}" for k, v in counts.items())
            print(f"\nTotal: {len(tasks)} ({total_parts})")
            print()

            if tasks:
                results = await tqdm_asyncio.gather(*tasks, desc="Fetching", unit="file")
                await self._save_metadata(results)
                self._print_failures(results)

        self._print_summary()

    def _print_failures(self, results: List[Dict]):
        failed = [r for r in results if r.get("status") == "failed"]
        if not failed:
            return
        by_host = defaultdict(int)
        for r in failed:
            by_host[r["url"].split("/")[2]] += 1
        print("\nFailed by host:")
        for host, n in sorted(by_host.items(), key=lambda kv: -kv[1]):
            print(f"  {host}: {n}")
        print("Sample errors:")
        for r in failed[:3]:
            print(f"  {r['url']}: {str(r.get('error', ''))[:120]}")

    async def _fetch_meta(self, session):
        print("Meta: NPM manifest + CHANGELOG")
        try:
            manifest = await self.fetch_npm_manifest(session)
            path = self.output_dir / "claude-code-manifest.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            async with aiofiles.open(path, "w") as f:
                await f.write(json.dumps(manifest, indent=2))
            print(f"  claude-code v{manifest.get('version', '?')}")
        except Exception as e:
            print(f"  WARN: NPM manifest: {e}", file=sys.stderr)

        try:
            changelog = await self.fetch_github_changelog(session)
            path = self.output_dir / "CHANGELOG.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            async with aiofiles.open(path, "wb") as f:
                await f.write(changelog)
            print(f"  CHANGELOG: {len(changelog):,} bytes")
        except Exception as e:
            print(f"  WARN: CHANGELOG: {e}", file=sys.stderr)

    async def _save_metadata(self, results: List[Dict]):
        metadata = {
            "metadata": {
                "version": "2.0",
                "fetch_date": datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z",
                "section": self.section or "all",
            },
            "items": [r for r in results if r.get("status") == "success"],
            "failures": [
                {"url": r["url"], "error": str(r.get("error", ""))[:200]}
                for r in results if r.get("status") == "failed"
            ],
            "summary": {
                "total": self.stats["total"],
                "downloaded": self.stats["downloaded"],
                "skipped": self.stats["skipped"],
                "failed": self.stats["failed"],
                "success_rate": (
                    round(self.stats["downloaded"] / self.stats["total"] * 100, 1)
                    if self.stats["total"] > 0 else 0
                ),
            },
        }
        path = self.output_dir / ".metadata.json"
        async with aiofiles.open(path, "w") as f:
            await f.write(json.dumps(metadata, indent=2))

    def _print_summary(self):
        print()
        print(f"Total:      {self.stats['total']}")
        print(f"Downloaded: {self.stats['downloaded']}")
        print(f"Skipped:    {self.stats['skipped']}")
        print(f"Failed:     {self.stats['failed']}")
        if self.stats["total"] > 0:
            rate = (self.stats["downloaded"] / self.stats["total"]) * 100
            print(f"Success:    {rate:.1f}%")

    # -- Single-URL fetch --------------------------------------------------

    def validate_url(self, url: str) -> bool:
        allowed = ["platform.claude.com", "code.claude.com", "modelcontextprotocol.io"]
        return any(f"https://{d}" in url for d in allowed)

    async def fetch_urls(self, urls: List[str]):
        invalid = [u for u in urls if not self.validate_url(u)]
        if invalid:
            print("ERROR: Invalid URLs:", file=sys.stderr)
            for u in invalid:
                print(f"  {u}", file=sys.stderr)
            print("Allowed: platform.claude.com, code.claude.com, modelcontextprotocol.io", file=sys.stderr)
            sys.exit(1)

        normalized = [u[:-3] if u.endswith(".md") else u for u in urls]
        print(f"Fetching {len(normalized)} URL(s)")

        timeout = aiohttp.ClientTimeout(total=300)
        connector = aiohttp.TCPConnector(limit=self.jobs)
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            self.stats["total"] = len(normalized)
            sem = asyncio.Semaphore(self.jobs)
            results = await tqdm_asyncio.gather(
                *(self.download_doc(session, u, sem) for u in normalized),
                desc="Fetching", unit="file",
            )
            await self._save_metadata(results)

        for r in results:
            s = r.get("status")
            if s == "success":
                print(f"  OK: {r.get('path')}")
            elif s == "skipped":
                print(f"SKIP: {r.get('url')}")
            else:
                print(f"FAIL: {r.get('url')} - {r.get('error')}", file=sys.stderr)
        self._print_summary()
        if self.stats["failed"] > 0:
            sys.exit(1)

    # -- Tree view ---------------------------------------------------------

    async def show_tree(self):
        print("Fetching source indexes...\n")
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            platform_urls = self.extract_sitemap_urls(
                await self.fetch_text(session, self.platform_sitemap_url), "/docs/en/")
            cc_urls = await self.fetch_claude_code_urls(session)
            mcp_urls = self.extract_sitemap_urls(
                await self.fetch_text(session, self.mcp_sitemap_url))
            support_urls = self.extract_support_urls(
                await self.fetch_text(session, self.support_sitemap_url))

        def show_grouped(title, urls, strip_prefix):
            print(f"{title} ({len(urls)})")
            print("-" * 50)
            groups = defaultdict(list)
            for url in urls:
                path = url.replace(strip_prefix, "")
                top = path.split("/")[0] if "/" in path else "(root)"
                groups[top].append(path)
            for sec in sorted(groups, key=lambda x: -len(groups[x])):
                print(f"  {sec}/ ({len(groups[sec])})")
            print()

        show_grouped("code.claude.com", cc_urls, "https://code.claude.com/docs/en/")
        show_grouped("platform.claude.com", platform_urls, "https://platform.claude.com/docs/en/")
        show_grouped("modelcontextprotocol.io", mcp_urls, "https://modelcontextprotocol.io/")

        print(f"support.claude.com: {len(support_urls)} articles")
        print("anthropic.com blog: frozen archive (not fetched)")
        print(f"GitHub repos: {len(GITHUB_REPOS)} repos configured")
        print()

        total = len(cc_urls) + len(platform_urls) + len(mcp_urls) + len(support_urls)
        print(f"Total fetchable: {total}+ (excludes GitHub repos)")

    # -- Discovery ---------------------------------------------------------

    async def discover(self):
        print("Probing Anthropic domains for content sources...")
        print("=" * 60)

        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            for domain, desc in DISCOVER_DOMAINS:
                print(f"\n{domain} ({desc})")
                print("-" * 40)

                # robots.txt
                try:
                    text = await self.fetch_text(session, f"https://{domain}/robots.txt")
                    sitemaps = [
                        l.split("Sitemap:", 1)[1].strip()
                        for l in text.split("\n")
                        if l.strip().startswith("Sitemap:")
                    ]
                    if sitemaps:
                        for s in sitemaps:
                            print(f"  Sitemap: {s}")
                    signals = [l for l in text.split("\n") if "Content-Signal" in l]
                    for s in signals:
                        print(f"  {s.strip()}")
                except Exception:
                    print("  robots.txt: unreachable")

                # llms.txt
                for path in ["/llms.txt", "/docs/llms.txt"]:
                    try:
                        async with session.get(f"https://{domain}{path}") as r:
                            ct = r.headers.get("content-type", "")
                            if r.status == 200 and "text/" in ct and "html" not in ct:
                                body = await r.text()
                                lines = body.strip().split("\n")
                                print(f"  {path}: {len(lines)} lines")
                    except Exception:
                        pass

                # llms-full.txt
                try:
                    async with session.get(f"https://{domain}/llms-full.txt") as r:
                        ct = r.headers.get("content-type", "")
                        if r.status == 200 and "text/" in ct and "html" not in ct:
                            size = int(r.headers.get("content-length", 0))
                            if size == 0:
                                body = await r.read()
                                size = len(body)
                            print(f"  /llms-full.txt: {size:,} bytes")
                except Exception:
                    pass

                # sitemap.xml
                for path in ["/sitemap.xml", "/docs/sitemap.xml"]:
                    try:
                        async with session.get(f"https://{domain}{path}") as r:
                            ct = r.headers.get("content-type", "")
                            if r.status == 200 and ("xml" in ct or "text/" in ct):
                                text = await r.text()
                                if "<loc>" in text:
                                    url_count = text.count("<loc>")
                                    has_lastmod = "<lastmod>" in text
                                    extra = " (has lastmod)" if has_lastmod else ""
                                    print(f"  {path}: {url_count} URLs{extra}")
                    except Exception:
                        pass

            # GitHub org
            print(f"\ngithub.com/anthropics")
            print("-" * 40)
            try:
                page = 1
                all_repos = []
                while True:
                    url = f"https://api.github.com/orgs/anthropics/repos?per_page=100&page={page}&type=public"
                    async with session.get(url) as r:
                        if r.status != 200:
                            break
                        repos = await r.json()
                        if not repos:
                            break
                        all_repos.extend(repos)
                        page += 1

                all_repos.sort(key=lambda r: r.get("stargazers_count", 0), reverse=True)
                print(f"  {len(all_repos)} public repos")
                for r in all_repos[:15]:
                    stars = r.get("stargazers_count", 0)
                    updated = r.get("pushed_at", "")[:10]
                    desc = (r.get("description") or "")[:50]
                    print(f"  {stars:>7}* {r['name']:<35} {updated}  {desc}")
                if len(all_repos) > 15:
                    print(f"  ... +{len(all_repos)-15} more")
            except Exception as e:
                print(f"  Error: {e}")

        print(f"\n{'=' * 60}")
        print("Compare against sources.json to find gaps.")


async def main():
    parser = ArgumentParser(
        description="Fetch Anthropic documentation from all known sources",
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""
Sections:
  claude-code   Claude Code + Agent SDK docs (code.claude.com)
  api/platform  API and platform docs (platform.claude.com)
  mcp           MCP protocol spec (modelcontextprotocol.io)
  github        All configured GitHub repos
  support       Support articles (support.claude.com, sitemap + .md)
  all           Everything (default)

Note: content/blog/ (anthropic.com engineering/research/news) is a
frozen archive as of 2026-07 — the site is HTML-only and the jina.ai
proxy path was removed.

Examples:
  fetcher.py                               Fetch everything
  fetcher.py --section mcp                 MCP spec only
  fetcher.py --section github              GitHub repos only
  fetcher.py --tree                         Show all sources
  fetcher.py --discover                     Probe domains for new sources
  fetcher.py --incremental                  Skip existing files
  fetcher.py URL [URL ...]                  Fetch specific URLs
        """,
    )
    parser.add_argument("urls", nargs="*", metavar="URL")
    parser.add_argument("--out", default="content", help="Output directory")
    parser.add_argument("--jobs", "-j", type=int, default=50)
    parser.add_argument(
        "--section", "-s",
        choices=[
            "claude-code", "api", "platform", "mcp",
            "github", "support", "all",
        ],
    )
    parser.add_argument("--incremental", action="store_true", help="Skip existing files")
    parser.add_argument("--tree", action="store_true", help="Show source structure")
    parser.add_argument("--discover", action="store_true", help="Probe domains for new sources")

    args = parser.parse_args()
    fetcher = Fetcher(
        output_dir=args.out, jobs=args.jobs,
        incremental=args.incremental, section=args.section,
    )

    if args.discover:
        await fetcher.discover()
    elif args.tree:
        await fetcher.show_tree()
    elif args.urls:
        await fetcher.fetch_urls(args.urls)
    else:
        await fetcher.fetch_all()


if __name__ == "__main__":
    asyncio.run(main())
