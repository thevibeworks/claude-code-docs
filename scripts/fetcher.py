#!/usr/bin/env python3
"""
Fetch Claude documentation from platform.claude.com and code.claude.com

Sources:
  - platform.claude.com/sitemap.xml  → API docs
  - code.claude.com/docs/llms.txt    → Claude Code docs

Usage:
  uv run scripts/fetcher.py
  uv run scripts/fetcher.py --tree
  uv run scripts/fetcher.py --section claude-code
  uv run scripts/fetcher.py --section api
  uv run scripts/fetcher.py --incremental --jobs 100
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

        # New URL structure (Dec 2025)
        self.platform_sitemap_url = "https://platform.claude.com/sitemap.xml"
        self.claude_code_llms_url = "https://code.claude.com/docs/llms.txt"
        self.anthropic_sitemap_url = "https://www.anthropic.com/sitemap.xml"

        self.stats = {"total": 0, "downloaded": 0, "skipped": 0, "failed": 0}

    async def fetch_sitemap(self, session: aiohttp.ClientSession, url: str) -> str:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

    async def fetch_npm_manifest(self, session: aiohttp.ClientSession) -> Dict:
        url = "https://registry.npmjs.org/@anthropic-ai/claude-code/latest"
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def fetch_github_changelog(self, session: aiohttp.ClientSession) -> bytes:
        url = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.read()

    async def fetch_claude_code_urls(self, session: aiohttp.ClientSession) -> List[str]:
        """Fetch Claude Code doc URLs from llms.txt (markdown link format)"""
        async with session.get(self.claude_code_llms_url) as response:
            response.raise_for_status()
            content = await response.text()

        urls = []
        # llms.txt uses markdown links: [Title](https://code.claude.com/docs/en/foo.md)
        pattern = r'\(https://code\.claude\.com/docs/en/[^)]+\.md\)'
        for match in re.findall(pattern, content):
            url = match[1:-1]  # Remove parens
            # Store without .md suffix (we add it back when fetching)
            urls.append(url[:-3])
        return urls

    def extract_platform_urls(self, sitemap_xml: str) -> List[str]:
        """Extract English doc URLs from platform.claude.com sitemap"""
        urls = []
        for line in sitemap_xml.split("\n"):
            if "<loc>" in line and "</loc>" in line:
                url = line.split("<loc>")[1].split("</loc>")[0]
                # Only English docs from platform
                if "/docs/en/" in url and "platform.claude.com" in url:
                    urls.append(url)
        return urls

    def extract_urls(self, sitemap_xml: str) -> List[str]:
        """Legacy method - kept for compatibility"""
        return self.extract_platform_urls(sitemap_xml)

    def get_output_path(self, url: str) -> Path:
        """Map URL to local file path"""
        if "code.claude.com" in url:
            # code.claude.com/docs/en/foo -> en/docs/claude-code/foo.md
            path = url.replace("https://code.claude.com/docs/", "")
            parts = path.split("/", 1)  # ['en', 'foo']
            if len(parts) == 2:
                return self.output_dir / parts[0] / "docs" / "claude-code" / f"{parts[1]}.md"
            return self.output_dir / f"{path}.md"
        elif "platform.claude.com" in url:
            # platform.claude.com/docs/en/foo -> en/foo.md
            path = url.replace("https://platform.claude.com/docs/", "")
            return self.output_dir / f"{path}.md"
        else:
            # Fallback
            path = url.replace("https://", "").split("/", 1)[-1]
            return self.output_dir / f"{path}.md"

    async def download_doc(
        self,
        session: aiohttp.ClientSession,
        url: str,
        semaphore: asyncio.Semaphore,
    ) -> Dict:
        async with semaphore:
            output_path = self.get_output_path(url)

            if self.incremental and output_path.exists():
                self.stats["skipped"] += 1
                return {"url": url, "status": "skipped"}

            try:
                fetch_url = f"{url}.md"
                async with session.get(fetch_url) as response:
                    response.raise_for_status()
                    content = await response.read()

                output_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)

                checksum = hashlib.sha256(content).hexdigest()
                self.stats["downloaded"] += 1

                return {
                    "url": url,
                    "status": "success",
                    "path": str(output_path.relative_to(self.output_dir)),
                    "sha256": checksum,
                    "size": len(content),
                }

            except Exception as e:
                self.stats["failed"] += 1
                return {"url": url, "status": "failed", "error": str(e)}

    async def download_blog(
        self,
        session: aiohttp.ClientSession,
        url: str,
        semaphore: asyncio.Semaphore,
    ) -> Dict:
        async with semaphore:
            slug = url.split("anthropic.com/")[1]
            output_path = self.output_dir / "blog" / f"{slug}.md"

            if self.incremental and output_path.exists():
                self.stats["skipped"] += 1
                return {"url": url, "status": "skipped"}

            try:
                fetch_url = f"https://r.jina.ai/{url}"
                async with session.get(fetch_url) as response:
                    response.raise_for_status()
                    content = await response.read()

                output_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)

                checksum = hashlib.sha256(content).hexdigest()
                self.stats["downloaded"] += 1

                return {
                    "url": url,
                    "status": "success",
                    "path": str(output_path.relative_to(self.output_dir)),
                    "sha256": checksum,
                    "size": len(content),
                }

            except Exception as e:
                self.stats["failed"] += 1
                return {"url": url, "status": "failed", "error": str(e)}

    async def fetch_all(self):
        print(f"Fetching to {self.output_dir}")
        print(f"Jobs: {self.jobs}")
        if self.incremental:
            print("Incremental: skip existing")
        if self.section:
            print(f"Section: {self.section}")

        timeout = aiohttp.ClientTimeout(total=300)
        connector = aiohttp.TCPConnector(limit=self.jobs)

        async with aiohttp.ClientSession(
            timeout=timeout, connector=connector
        ) as session:
            # Fetch NPM manifest
            print("Fetching NPM manifest...")
            try:
                manifest = await self.fetch_npm_manifest(session)
                manifest_path = self.output_dir / "claude-code-manifest.json"
                manifest_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(manifest_path, "w") as f:
                    await f.write(json.dumps(manifest, indent=2))
                print(f"NPM manifest: v{manifest.get('version', 'unknown')}")
            except Exception as e:
                print(f"Failed to fetch NPM manifest: {e}", file=sys.stderr)

            # Fetch GitHub CHANGELOG
            print("Fetching GitHub CHANGELOG...")
            try:
                changelog = await self.fetch_github_changelog(session)
                changelog_path = self.output_dir / "CHANGELOG.md"
                changelog_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(changelog_path, "wb") as f:
                    await f.write(changelog)
                print(f"CHANGELOG: {len(changelog)} bytes")
            except Exception as e:
                print(f"Failed to fetch CHANGELOG: {e}", file=sys.stderr)

            # Fetch from both sources
            print("Fetching sources...")

            # Platform docs (API, build-with-claude, etc.)
            platform_urls = []
            if not self.section or self.section in ("api", "platform", "all"):
                print("  platform.claude.com/sitemap.xml...")
                sitemap_xml = await self.fetch_sitemap(session, self.platform_sitemap_url)
                platform_urls = self.extract_platform_urls(sitemap_xml)
                print(f"    Found {len(platform_urls)} platform docs")

            # Claude Code docs
            claude_code_urls = []
            if not self.section or self.section in ("claude-code", "all"):
                print("  code.claude.com/docs/llms.txt...")
                claude_code_urls = await self.fetch_claude_code_urls(session)
                print(f"    Found {len(claude_code_urls)} Claude Code docs")

            # Blog posts
            blog_urls = []
            if not self.section or self.section in ("blog", "all"):
                print("  anthropic.com/sitemap.xml...")
                anthropic_xml = await self.fetch_sitemap(session, self.anthropic_sitemap_url)
                for line in anthropic_xml.split("\n"):
                    if "<loc>" in line and "claude-code" in line:
                        url = line.split("<loc>")[1].split("</loc>")[0]
                        blog_urls.append(url)
                print(f"    Found {len(blog_urls)} blog posts")

            # Combine all URLs
            urls = platform_urls + claude_code_urls

            self.stats["total"] = len(urls) + len(blog_urls)
            print(f"\nTotal: {self.stats['total']} ({len(platform_urls)} platform, {len(claude_code_urls)} claude-code, {len(blog_urls)} blog)")
            print()

            # Download concurrently
            semaphore = asyncio.Semaphore(self.jobs)
            tasks = []

            for url in urls:
                tasks.append(self.download_doc(session, url, semaphore))

            for url in blog_urls:
                tasks.append(self.download_blog(session, url, semaphore))

            results = await tqdm_asyncio.gather(
                *tasks, desc="Downloading", unit="file"
            )

            # Save metadata
            await self.save_metadata(results)

        # Print summary
        print()
        print(f"Total:      {self.stats['total']}")
        print(f"Downloaded: {self.stats['downloaded']}")
        print(f"Skipped:    {self.stats['skipped']}")
        print(f"Failed:     {self.stats['failed']}")
        if self.stats["total"] > 0:
            rate = (self.stats["downloaded"] / self.stats["total"]) * 100
            print(f"Success:    {rate:.1f}%")

    async def save_metadata(self, results: List[Dict]):
        metadata = {
            "metadata": {
                "version": "1.0",
                "fetch_date": datetime.now(timezone.utc)
                .replace(tzinfo=None)
                .isoformat()
                + "Z",
            },
            "items": [r for r in results if r.get("status") == "success"],
            "summary": {
                "total": self.stats["total"],
                "downloaded": self.stats["downloaded"],
                "skipped": self.stats["skipped"],
                "failed": self.stats["failed"],
                "success_rate": (
                    round(self.stats["downloaded"] / self.stats["total"] * 100, 1)
                    if self.stats["total"] > 0
                    else 0
                ),
            },
        }

        metadata_file = self.output_dir / ".metadata.json"
        async with aiofiles.open(metadata_file, "w") as f:
            await f.write(json.dumps(metadata, indent=2))

    async def show_tree(self):
        print("Fetching sources...")
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            # Platform docs
            sitemap_xml = await self.fetch_sitemap(session, self.platform_sitemap_url)
            platform_urls = self.extract_platform_urls(sitemap_xml)

            # Claude Code docs
            claude_code_urls = await self.fetch_claude_code_urls(session)

        # Show Claude Code docs
        print(f"\ncode.claude.com ({len(claude_code_urls)} docs)")
        print("-" * 40)
        for url in sorted(claude_code_urls):
            path = url.replace("https://code.claude.com/docs/en/", "")
            print(f"  {path}")

        # Show Platform docs grouped
        print(f"\nplatform.claude.com ({len(platform_urls)} docs)")
        print("-" * 40)

        # Group by path structure
        groups = defaultdict(list)
        for url in platform_urls:
            path = url.replace("https://platform.claude.com/docs/en/", "")
            parts = path.split("/")
            if len(parts) >= 1:
                groups[parts[0]].append(path)

        for section in sorted(groups.keys(), key=lambda x: -len(groups[x])):
            paths = groups[section]
            print(f"  {section}/ ({len(paths)})")

            # Show subsections
            subs = defaultdict(int)
            for path in paths:
                parts = path.split("/")
                if len(parts) >= 2:
                    subs[parts[1]] += 1

            shown = 0
            for sub, count in sorted(subs.items(), key=lambda x: -x[1]):
                if shown < 5:
                    print(f"    {sub}/ ({count})")
                    shown += 1
                elif shown == 5:
                    remaining = len(subs) - shown
                    if remaining > 0:
                        print(f"    [+{remaining} more]")
                    break

        print("\nUsage:")
        print("  fetcher.py                     # Fetch all")
        print("  fetcher.py --section claude-code")
        print("  fetcher.py --section api")
        print("  fetcher.py --section blog")


async def main():
    parser = ArgumentParser(
        description="Fetch Claude documentation from platform.claude.com and code.claude.com",
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fetcher.py                       Fetch all docs (platform + claude-code + blog)
  fetcher.py --tree                Show available documentation structure
  fetcher.py --section claude-code Fetch only Claude Code docs
  fetcher.py --section api         Fetch only API/platform docs
  fetcher.py --section blog        Fetch only blog posts
  fetcher.py --incremental         Skip existing files
  fetcher.py --jobs 100            Use 100 parallel jobs
        """,
    )
    parser.add_argument("--out", default="content", help="Output directory")
    parser.add_argument(
        "--jobs", "-j", type=int, default=50, help="Parallel jobs (default: 50)"
    )
    parser.add_argument(
        "--section", "-s",
        choices=["claude-code", "api", "platform", "blog", "all"],
        help="Section to fetch (default: all)",
    )
    parser.add_argument(
        "--incremental", action="store_true", help="Skip existing files"
    )
    parser.add_argument("--tree", action="store_true", help="Show documentation structure")

    args = parser.parse_args()

    fetcher = Fetcher(
        output_dir=args.out,
        jobs=args.jobs,
        incremental=args.incremental,
        section=args.section,
    )

    if args.tree:
        await fetcher.show_tree()
    else:
        await fetcher.fetch_all()


if __name__ == "__main__":
    asyncio.run(main())
