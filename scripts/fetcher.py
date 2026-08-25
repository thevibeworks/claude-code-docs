#!/usr/bin/env python3
"""
Fetch Anthropic documentation from all known sources.

Sources (see sources.json for the complete registry):
  - platform.claude.com     -> API/platform docs (sitemap + .md suffix)
  - code.claude.com         -> Claude Code + Agent SDK (llms.txt + .md suffix)
  - modelcontextprotocol.io -> MCP spec (sitemap + .md suffix)
  - support.claude.com      -> Help articles (sitemap + .md suffix)
  - claude.com/docs         -> Product docs (sitemap + .md suffix)
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
from urllib.parse import urlsplit
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
    ("claude.com",              "Product docs"),
    ("academy.claude.com",      "Courses/tutorials (HTML-only, not fetched)"),
]

# Which of the above the fetcher actually archives. Kept next to
# DISCOVER_DOMAINS so "we probe it" and "we fetch it" can never drift apart
# silently — that gap is the whole reason academy.claude.com went unnoticed.
FETCHED_DOMAINS = {
    "platform.claude.com", "code.claude.com", "modelcontextprotocol.io",
    "support.claude.com", "claude.com",
}
# Archived, deliberately not refreshed: anthropic.com is HTML-only and the
# jina.ai proxy path was removed in 2026-07.
FROZEN_DOMAINS = {"anthropic.com"}


def normalize_url(url: str) -> str:
    """Drop the #fragment and any trailing slash from a sitemap URL.

    A fragment addresses a heading inside a page, not a page. Kept, it became
    part of the output filename and the fetch path: 16 files landed as
    `.../delete#delete.md` and `.../federation_rules#admin.federation_rules.md`,
    and every one of them held an HTML soft-404 rather than docs, because
    platform.claude.com has no such page to serve. The clean twin was always
    fetched alongside, so the fragment copy was pure garbage.
    """
    return url.split("#", 1)[0].rstrip("/").strip()


def looks_like_html(content: bytes) -> bool:
    """True if the body is an HTML page rather than the markdown we asked for.

    platform.claude.com answers unknown doc paths with its Next.js app shell at
    HTTP 200 — a soft 404. raise_for_status() sees nothing wrong, so without
    this check the shell gets written straight into a .md file. That is how 53
    files, 44 of them under content/en/api/kotlin/, ended up holding
    "<!DOCTYPE html><html class=..." instead of documentation, across three
    separate bug reports (#669, #768, #941) while the scheduled run stayed
    green.
    """
    head = content[:512].lstrip().lower()
    return head.startswith(b"<!doctype html") or head.startswith(b"<html")


class Fetcher:
    def __init__(
        self,
        output_dir: str = "content",
        jobs: int = 50,
        incremental: bool = False,
        section: Optional[str] = None,
        no_reap: bool = False,
    ):
        self.output_dir = Path(output_dir)
        self.jobs = jobs
        self.incremental = incremental
        self.section = section
        self.no_reap = no_reap

        self.platform_sitemap_url = "https://platform.claude.com/sitemap.xml"
        self.claude_code_llms_url = "https://code.claude.com/docs/llms.txt"
        self.mcp_sitemap_url = "https://modelcontextprotocol.io/sitemap.xml"
        self.support_sitemap_url = "https://support.claude.com/sitemap.xml"
        # claude.com stopped being a marketing redirect: since ~2026-08 it hosts
        # the product docs (Claude Tag, Cowork, office agents, connectors,
        # government, claude-science) and serves .md variants like the other
        # docs sites. Found by following the redirects on 8 support articles
        # that had gone soft-404 — upstream had been pointing here for weeks.
        self.claude_com_sitemap_url = "https://claude.com/docs/sitemap.xml"

        self.stats = {"total": 0, "downloaded": 0, "skipped": 0,
                      "failed": 0, "dead": 0, "reaped": 0}
        self._stats_finalized = False

        # Paths whose upstream answered 200-with-HTML (a soft 404). Refusing the
        # write is not enough on its own: any copy fetched before the guard
        # existed stays on disk forever, since every later run refuses again and
        # never touches the stale file. 159 such files accumulated by 2026-08 —
        # all 135 of content/en/api/terraform/ among them — and re-probing every
        # one upstream found 145 hard 404s, 14 still-soft 404s, 0 recoverable.
        # Collected here and reaped after the run, not deleted inline, so the
        # circuit breaker below can see the whole batch at once.
        self.soft_404_paths: List[Path] = []

        # URLs already confirmed gone upstream, with the date we confirmed it.
        # Without this every dead page fails on every run forever: 123 permanent
        # failures pinning the success rate at 96.9% and burying the one new
        # failure that actually matters. Known deaths are counted, not shouted.
        self.tombstones_path = Path("tombstones.json")
        self.tombstones: Dict[str, dict] = {}
        if self.tombstones_path.exists():
            try:
                self.tombstones = json.loads(self.tombstones_path.read_text())["urls"]
            except (OSError, ValueError, KeyError):
                self.tombstones = {}
        self.dead_now: Dict[str, str] = {}     # url -> reason, this run
        self.resurrected: List[str] = []

        # "<from-host> -> <to-host>" : the URLs we asked for that landed there.
        # Off-site redirects are how a docs site announces it moved; this is the
        # discovery signal --discover cannot see, because it only probes domains
        # we already know to ask about.
        self.redirects_offsite: Dict[str, set] = defaultdict(set)

        # What the last full run could see of the world outside sources.json.
        # Printing it was not enough: the run that found academy.claude.com had
        # already printed "support.claude.com -> academy.claude.com" for weeks,
        # into an Actions log with no reader. The decision agent downstream sees
        # `git status`, so a discovery only reaches a human once it is a file
        # that changes. Sets and capability booleans only — no counts, or every
        # run rewrites it and the diff stops meaning anything.
        self.discovery_path = Path("discovery.json")

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
        # A sitemap is one long line as often as not, so scan the whole text
        # rather than assuming one <loc> per line.
        urls = []
        seen = set()
        for url in re.findall(r"<loc>([^<]+)</loc>", xml):
            url = normalize_url(url)
            if not url or url in seen:
                continue
            if must_contain and must_contain not in url:
                continue
            seen.add(url)
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

    # -- Reverse mapping: what we already archived -------------------------

    # Sections of content/ whose files came from a URL we can re-derive.
    # github/ is fetched by repo tree walk, blog/ is a frozen archive.
    _REFETCHABLE = ("en", "mcp", "support", "claude")

    def existing_urls(self) -> List[str]:
        """URLs for docs already on disk — the inverse of get_output_path.

        Discovery surfaces are not a complete index of what exists. In July 2026
        platform.claude.com dropped every per-language SDK reference page from
        both its sitemap and its llms.txt while leaving the pages live and
        actively edited. The fetcher followed the sitemap, so 1,560 files simply
        stopped being refreshed — no error, no missing file, nothing for the
        pipeline to report, just a slow drift into staleness that went unnoticed
        for seven weeks (content/en/api/python/messages/create.md sat 35%
        smaller than upstream).

        Refetching what we already hold makes the archive self-healing: pages
        keep updating after they are de-indexed, and any that truly died get
        removed by reap() on a hard 404 rather than lingering.
        """
        urls = []
        for section in self._REFETCHABLE:
            base = self.output_dir / section
            if not base.is_dir():
                continue
            for path in base.rglob("*.md"):
                rel = path.relative_to(self.output_dir).with_suffix("")
                parts = rel.parts
                if parts[0] == "en":
                    if parts[1:3] == ("docs", "claude-code"):
                        tail = "/".join(parts[3:])
                        urls.append(f"https://code.claude.com/docs/en/{tail}")
                    else:
                        tail = "/".join(parts)
                        urls.append(f"https://platform.claude.com/docs/{tail}")
                elif parts[0] == "mcp":
                    tail = "/".join(parts[1:])
                    urls.append(f"https://modelcontextprotocol.io/{tail}")
                elif parts[0] == "support":
                    tail = "/".join(parts[1:])
                    urls.append(f"https://support.claude.com/en/articles/{tail}")
                elif parts[0] == "claude":
                    tail = "/".join(parts[1:])
                    urls.append(f"https://claude.com/docs/{tail}")
        return urls

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
        elif "claude.com/docs" in url:
            path = url.replace("https://claude.com/docs/", "")
            return self.output_dir / "claude" / f"{path}.md"
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
                async with session.get(f"{url}.md") as r:
                    r.raise_for_status()
                    content = await r.read()
                    if r.history:
                        # Where a dead page points is the best new-source signal
                        # we get. claude.com/docs — 215 pages of product
                        # documentation — was found exactly this way: 8 support
                        # articles had been 301-ing there for weeks and nothing
                        # was reading the Location header.
                        landed_host = r.url.host or ""
                        asked_host = urlsplit(url).hostname or ""
                        if landed_host and landed_host != asked_host:
                            self.redirects_offsite[
                                f"{asked_host} -> {landed_host}"].add(url)

                        # A redirect to a different path means this page moved,
                        # and the body now in hand belongs to the TARGET. Writing
                        # it back to the old path silently misattributes it: when
                        # release-notes/system-prompts split into per-model pages,
                        # the 471KB history was replaced by the 3.7KB overview it
                        # redirects to. The target has its own entry in the fetch
                        # set, so drop this one and record the move.
                        landed = normalize_url(str(r.url))
                        if landed.removesuffix(".md") != url:
                            self.dead_now[url] = f"moved -> {landed.removesuffix('.md')}"
                            if output_path.exists():
                                self.soft_404_paths.append(output_path)
                            self.stats["failed"] += 1
                            return {
                                "url": url,
                                "status": "dead" if url in self.tombstones else "failed",
                                "error": f"moved to {landed}",
                            }
                if looks_like_html(content):
                    # Soft 404: HTTP 200 with the site's HTML shell. Writing it
                    # would replace docs with markup, and because incremental
                    # mode skips paths that already exist, a bad file is never
                    # re-fetched — it just stays wrong. Queue any existing copy
                    # for reaping so a page deleted upstream also leaves us.
                    if output_path.exists():
                        self.soft_404_paths.append(output_path)
                    self.dead_now[url] = "soft-404 (HTML shell)"
                    self.stats["failed"] += 1
                    return {
                        "url": url, "status": "dead" if url in self.tombstones else "failed",
                        "error": "upstream returned HTML, not markdown (soft 404)",
                    }
                output_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)
                self.stats["downloaded"] += 1
                if url in self.tombstones:
                    self.resurrected.append(url)
                return {
                    "url": url, "status": "success",
                    "path": str(output_path.relative_to(self.output_dir)),
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                }
            except aiohttp.ClientResponseError as e:
                # 404/410 is upstream stating the page is gone — reap our copy.
                # Every other status (429, 5xx) is noise that must never delete
                # anything, or one bad afternoon upstream empties the archive.
                if e.status in (404, 410):
                    if output_path.exists():
                        self.soft_404_paths.append(output_path)
                    self.dead_now[url] = f"HTTP {e.status}"
                    self.stats["failed"] += 1
                    return {
                        "url": url,
                        "status": "dead" if url in self.tombstones else "failed",
                        "error": f"HTTP {e.status}",
                    }
                self.stats["failed"] += 1
                return {"url": url, "status": "failed", "error": f"HTTP {e.status}"}
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
                if filepath.endswith(".md") and looks_like_html(content):
                    self.stats["failed"] += 1
                    return {
                        "url": url, "status": "failed",
                        "error": "upstream returned HTML, not markdown",
                    }
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
            queued = set()

            def queue(url: str):
                if url in queued:
                    return
                queued.add(url)
                tasks.append(self.download_doc(session, url, semaphore))

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
                    queue(url)

            # -- Claude Code docs --
            if self.want("claude-code"):
                print("Source: code.claude.com/docs/llms.txt")
                urls = await self.fetch_claude_code_urls(session)
                counts["claude-code"] = len(urls)
                print(f"  {len(urls)} docs")
                for url in urls:
                    queue(url)

            # -- MCP docs --
            if self.want("mcp"):
                print("Source: modelcontextprotocol.io/sitemap.xml")
                xml = await self.fetch_text(session, self.mcp_sitemap_url)
                urls = self.extract_sitemap_urls(xml)
                counts["mcp"] = len(urls)
                print(f"  {len(urls)} docs")
                for url in urls:
                    queue(url)

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
                    queue(url)

            # -- claude.com product docs --
            if self.want("products"):
                print("Source: claude.com/docs/sitemap.xml")
                xml = await self.fetch_text(session, self.claude_com_sitemap_url)
                urls = [
                    u for u in self.extract_sitemap_urls(xml, "/docs/")
                    if u.startswith("https://claude.com/docs/")
                ]
                counts["products"] = len(urls)
                print(f"  {len(urls)} docs")
                for url in urls:
                    queue(url)

            # -- Refresh what we already hold --
            # Catches pages upstream de-indexed but still serves; reap() removes
            # the ones that really died. Full runs only: a --section run has no
            # business refreshing sections it was not asked to fetch.
            if self.want("all") and not self.incremental:
                stragglers = [u for u in self.existing_urls() if u not in queued]
                if stragglers:
                    counts["refresh"] = len(stragglers)
                    print("Source: on-disk archive (de-indexed upstream)")
                    print(f"  {len(stragglers)} docs")
                    for url in stragglers:
                        queue(url)

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

            # Same rule as tombstones below: only a full run has seen every
            # redirect, so only a full run may rewrite the snapshot. A --section
            # run would drop the other sections' redirect targets by omission
            # and report the loss as news.
            if self.want("all") and not self.incremental:
                await self.snapshot_discovery(session)

        # Only a full run sees every URL, so only a full run may conclude that a
        # missing page is really gone. A --section run has no opinion about the
        # sections it did not fetch, and --incremental never re-probes what it
        # skipped, so neither is allowed to delete.
        # Only a full run may rewrite tombstones.json: a --section run has not
        # probed the other sections and would resurrect their tombstoned URLs by
        # omission. (The dead/failed split itself happens in _print_summary, so
        # every entry point reports it.)
        if self.want("all") and not self.incremental:
            self._sync_tombstones(datetime.now(timezone.utc).strftime("%Y-%m-%d"))
            self.reap(dry_run=self.no_reap)
        self._report_offsite_redirects()

        self._print_summary()

    def _sync_tombstones(self, today: str):
        """Fold this run's deaths into tombstones.json and report only the news.

        A page that died months ago is not news; a page that died today is. And
        a tombstoned page that starts answering again is the most interesting
        case of all, because it means we were wrong to write it off.
        """
        new_deaths = {u: r for u, r in self.dead_now.items() if u not in self.tombstones}

        for url in self.resurrected:
            self.tombstones.pop(url, None)
        for url, reason in new_deaths.items():
            self.tombstones[url] = {"since": today, "reason": reason}

        if self.resurrected:
            print(f"\nBack from the dead ({len(self.resurrected)}) — "
                  f"tombstone removed, content refetched:")
            for u in sorted(self.resurrected)[:10]:
                print(f"  {u}")

        if new_deaths:
            print(f"\nNewly gone upstream ({len(new_deaths)}):")
            for u, reason in sorted(new_deaths.items())[:20]:
                # Print the URL we asked for first. Putting the reason first put
                # a "moved -> <target>" ahead of the source URL, and the two read
                # as a pair in the wrong order.
                if reason.startswith("moved -> "):
                    print(f"  {u}\n      moved to {reason.removeprefix('moved -> ')}")
                else:
                    print(f"  {u}\n      {reason}")
            if len(new_deaths) > 20:
                print(f"  ... +{len(new_deaths) - 20} more (full list in tombstones.json)")

        known = len(self.dead_now) - len(new_deaths)
        if known:
            print(f"\nAlready-known dead pages re-probed: {known} "
                  f"(see tombstones.json)")

        self.tombstones_path.write_text(json.dumps(
            {"version": 1,
             "note": ("URLs confirmed gone upstream. Kept so a page that died "
                      "once does not report as a fresh failure on every later "
                      "run, which would bury the failure that is actually new. "
                      "An entry clears itself if the URL answers again -- but "
                      "only while something still probes it. Entries whose local "
                      "file was removed are no longer fetched, so they stay as a "
                      "record of the restructure rather than a live check."),
             "updated": today,
             "urls": dict(sorted(self.tombstones.items()))},
            indent=2) + "\n")

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
        live = self._finalize_stats()
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
            # Known deaths appeared in neither list before: "items" keeps only
            # successes and "failures" only status == "failed", so all 94
            # tombstoned pages fell through the artifact entirely while the
            # summary still counted them. Recorded here so the file explains its
            # own numbers.
            "dead": [
                {"url": r["url"], "reason": self.dead_now.get(r["url"], "")}
                for r in results if r.get("status") == "dead"
            ],
            "summary": {
                "total": self.stats["total"],
                "downloaded": self.stats["downloaded"],
                "skipped": self.stats["skipped"],
                "failed": self.stats["failed"],
                "dead": self.stats["dead"],
                "success_rate": (
                    round(self.stats["downloaded"] / live * 100, 1)
                    if live > 0 else 0
                ),
            },
        }
        path = self.output_dir / ".metadata.json"
        async with aiofiles.open(path, "w") as f:
            await f.write(json.dumps(metadata, indent=2))

    def _finalize_stats(self) -> int:
        """Split confirmed-dead pages out of the failure count. Returns live docs.

        A page upstream deleted is not a fetch failure. This used to happen only
        in _print_summary, so the console told the truth while
        content/.metadata.json — the machine-readable artifact, the one a
        consumer would actually parse — kept reporting `failed: 95` and
        `success_rate: 97.6` for a run whose real numbers were 1 and 100.0%.
        That is rule 12's camouflage surviving in the file after being removed
        from the terminal: a rate pinned by 94 standing deaths cannot show the
        95th failure that is new. Instrumentation is code; it has bugs too.

        Idempotent, because both writers call it.
        """
        if not self._stats_finalized:
            self._stats_finalized = True
            self.stats["dead"] = len(self.dead_now)
            self.stats["failed"] -= len(self.dead_now)
        return self.stats["total"] - self.stats["dead"]

    def _print_summary(self):
        live = self._finalize_stats()

        print()
        print(f"Total:      {self.stats['total']}")
        print(f"Downloaded: {self.stats['downloaded']}")
        print(f"Skipped:    {self.stats['skipped']}")
        print(f"Failed:     {self.stats['failed']}")
        print(f"Gone:       {self.stats['dead']}  (confirmed removed upstream)")
        print(f"Reaped:     {self.stats['reaped']}")
        # Pages upstream deleted are not our failures, so they are excluded from
        # the rate. Leaving them in pinned it at 96.9% forever and made a real
        # new breakage indistinguishable from the standing background.
        if live > 0:
            rate = (self.stats["downloaded"] / live) * 100
            print(f"Success:    {rate:.1f}% of {live} live docs")

    # -- Reaping -----------------------------------------------------------

    # A page removed upstream used to live in the archive forever: the fetcher
    # only ever added or overwrote, so nothing could ever shrink. Reaping closes
    # that loop. The cap exists because this runs unattended four times a day
    # and merges its own "minor" PRs — an upstream outage that soft-404s
    # everything would otherwise delete the archive and self-merge the result.
    REAP_LIMIT = 200

    @staticmethod
    def _holds_markup(path: Path) -> bool:
        try:
            with open(path, "rb") as f:
                return looks_like_html(f.read(512))
        except OSError:
            return False

    def reap(self, dry_run: bool = False) -> int:
        """Delete archived files whose upstream is gone — but only the markup.

        "Gone upstream" and "should be deleted" are different questions for an
        archive. A file holding an HTML shell is markup we failed to recognise
        as an error; deleting it loses nothing. A file holding real markdown
        whose URL now 404s is the opposite: Anthropic removed the page and our
        copy may be the only one left. content/en/resources/prompt-library/ is
        exactly that — 19 pages, ~20KB each, redirected away to a generic
        best-practices page in 2026-08. An unattended job that merges its own
        PRs has no business destroying those, so they are reported for a human
        instead.
        """
        candidates = sorted(set(self.soft_404_paths))
        paths = [p for p in candidates if self._holds_markup(p)]
        keep = [p for p in candidates if p not in set(paths)]

        if keep:
            print(f"\nGone upstream but holding real content — kept for review "
                  f"({len(keep)}):")
            for p in keep:
                print(f"  kept: {p}")
            print("  (delete by hand if the archive should not keep them)")

        if not paths:
            return 0

        if len(paths) > self.REAP_LIMIT:
            print(
                f"\n::error::Refusing to reap {len(paths)} files "
                f"(limit {self.REAP_LIMIT}). This many pages vanishing at once "
                f"means an upstream outage, not {len(paths)} real deletions. "
                f"Nothing was deleted; re-run when upstream is healthy.",
                file=sys.stderr,
            )
            for p in paths[:20]:
                print(f"  would reap: {p}", file=sys.stderr)
            print(f"  ... +{len(paths) - 20} more", file=sys.stderr)
            return 0

        verb = "would reap" if dry_run else "reaped"
        print(f"\nReaping {len(paths)} file(s) gone upstream (HTML markup, no loss):")
        for p in paths:
            print(f"  {verb}: {p}")
            if not dry_run:
                p.unlink(missing_ok=True)
        if not dry_run:
            self._prune_empty_dirs()
        self.stats["reaped"] = len(paths)
        return len(paths)

    # -- Discovery state ---------------------------------------------------

    async def _probe_domain(self, session, domain: str) -> dict:
        """What this domain offers a fetcher, as stable facts.

        Deliberately no counts. "sitemap has 1,541 URLs" changes on almost every
        run and would make discovery.json churn like the content it is supposed
        to be a signal *about*; a file that always changes says nothing when it
        changes. Capability booleans flip once, on the day the answer is news.

        `serves_markdown` is the one that decides everything: it is the exact
        test for whether this fetcher could archive the domain at all. It is why
        academy.claude.com sits recorded-but-unfetched (725 pages, every path a
        404 to an HTML shell) rather than being silently forgotten, and the day
        upstream adds .md variants that `false` becomes a `true` in a diff.
        """
        out = {"serves_llms_txt": False, "serves_sitemap": False,
               "serves_markdown": False}
        locs: List[str] = []

        for path in ("/llms.txt", "/docs/llms.txt"):
            try:
                async with session.get(f"https://{domain}{path}") as r:
                    ct = r.headers.get("content-type", "")
                    if r.status == 200 and "text/" in ct and "html" not in ct:
                        out["serves_llms_txt"] = True
                        break
            except Exception:
                pass

        for path in ("/docs/sitemap.xml", "/sitemap.xml"):
            try:
                async with session.get(f"https://{domain}{path}") as r:
                    if r.status != 200:
                        continue
                    text = await r.text()
                    if "<loc>" not in text:
                        continue
                    out["serves_sitemap"] = True
                    locs = [normalize_url(c.split("</loc>", 1)[0])
                            for c in text.split("<loc>")[1:]]
                    break
            except Exception:
                # Cloudflare answers claude.ai's sitemap with a challenge. That
                # is a fact about the domain, not an error to swallow silently.
                out["serves_sitemap"] = "blocked"

        # Sample doc pages, not the first <loc>. The first entry is the site
        # root on platform.claude.com and a localised marketing page on
        # claude.com — neither has a .md twin, so a one-sample probe called both
        # domains markdown-incapable while the fetcher was busy pulling 829 .md
        # files off them. Spread the sample so one dead page cannot decide it.
        docs = [u for u in locs if "/docs/" in u] or locs
        step = max(1, len(docs) // 5)
        for sample in docs[::step][:5]:
            try:
                async with session.get(f"{sample}.md") as r:
                    body = await r.read()
                    if r.status == 200 and not looks_like_html(body):
                        out["serves_markdown"] = True
                        break
            except Exception:
                pass
        return out

    async def snapshot_discovery(self, session) -> dict:
        """Write discovery.json: what exists upstream that sources.json does not.

        The pipeline could already see new sources and threw the sight away.
        `_report_offsite_redirects` prints "<-- UNKNOWN DOMAIN" to stdout, and
        stdout in CI is an Actions log nobody opens; the agent that decides
        whether a run is newsworthy reads `git status`, not the log above it.
        So academy.claude.com — 725 pages that support.claude.com had been
        redirecting to for weeks — was found by a human chasing a dead article,
        not by the automation that had been printing the hop all along.

        Making it a tracked file needs no new plumbing: a new domain, a new
        anthropics repo, or a domain that starts serving markdown all become a
        line in a diff, which is exactly the signal the existing publish path
        already turns into a PR.
        """
        known = {d for d, _ in DISCOVER_DOMAINS}
        domains = {}
        for domain, _desc in DISCOVER_DOMAINS:
            probe = await self._probe_domain(session, domain)
            if domain in FETCHED_DOMAINS:
                status = "fetched"
            elif domain in FROZEN_DOMAINS:
                status = "frozen"
            else:
                status = "not-fetched"
            domains[domain] = {"status": status, **probe}

        # Redirect targets are observed by *fetching*, so a --discover run sees
        # none. Overwriting from one would wipe the field the pipeline fills and
        # report academy.claude.com's disappearance as good news. Keep the last
        # full run's answer unless this run actually fetched something.
        targets = sorted({hop.split(" -> ")[1] for hop in self.redirects_offsite})
        if not targets:
            try:
                targets = json.loads(
                    self.discovery_path.read_text()).get("redirect_targets", [])
            except (OSError, ValueError):
                targets = []
        for target in targets:
            if target not in domains:
                # A domain upstream points at that we have never probed. This is
                # the branch that would have caught academy.claude.com.
                domains[target] = {
                    "status": "UNKNOWN — seen only as a redirect target",
                    **await self._probe_domain(session, target),
                }

        fetched_repos = {r for r, _, _ in GITHUB_REPOS}
        org = sorted(await self._list_org_repos(session))
        review = sorted(
            f"{d}: reachable and serves .md, but not fetched"
            for d, v in domains.items()
            if v.get("serves_markdown") and v["status"] not in ("fetched", "frozen")
        )

        snapshot = {
            "version": 1,
            "note": (
                "What the last full run could see outside sources.json. Written "
                "by the fetcher so a new source arrives as a diff a human "
                "reviews, not as a line in an Actions log nobody reads. Stable "
                "facts only: a change here is always news. `review` is the "
                "actionable list — domains we could archive today and do not."
            ),
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "domains": domains,
            "redirect_targets": targets,
            "github_org_anthropics": {
                "fetched": sorted(fetched_repos),
                "not_fetched": [r for r in org if r not in fetched_repos],
            },
            "review": review,
        }

        if org:
            self.discovery_path.write_text(json.dumps(snapshot, indent=2) + "\n")
        else:
            # A rate-limited or unauthenticated GitHub API returns nothing, and
            # writing that would delete every repo from the file and report it
            # as "Anthropic archived its whole org". Skip instead.
            print("\n::warning::GitHub org enumeration returned no repos "
                  "(rate limit?) — discovery.json left untouched")

        unknown = [d for d, v in domains.items() if v["status"].startswith("UNKNOWN")]
        if unknown or review:
            print("\nDiscovery — needs a decision (see discovery.json):")
            for d in unknown:
                print(f"  UNKNOWN domain seen upstream: {d}")
            for line in review:
                print(f"  {line}")
        return snapshot

    async def _list_org_repos(self, session) -> List[str]:
        repos, page = [], 1
        headers = {}
        if os.environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
        while True:
            url = (f"https://api.github.com/orgs/anthropics/repos"
                   f"?per_page=100&page={page}&type=public")
            try:
                async with session.get(url, headers=headers) as r:
                    if r.status != 200:
                        break
                    batch = await r.json()
            except Exception:
                break
            if not batch:
                break
            repos.extend(f"anthropics/{x['name']}" for x in batch
                         if not x.get("archived"))
            page += 1
        return repos

    def _report_offsite_redirects(self):
        known = {d for d, _ in DISCOVER_DOMAINS} | {"www.anthropic.com"}
        news = {
            hop: urls for hop, urls in self.redirects_offsite.items()
            if hop.split(" -> ")[1] not in known
        }
        if not self.redirects_offsite:
            return
        print(f"\nOff-site redirects seen ({len(self.redirects_offsite)} route(s)):")
        for hop, urls in sorted(self.redirects_offsite.items()):
            flag = "  <-- UNKNOWN DOMAIN, consider adding a source" if hop in news else ""
            print(f"  {hop}  ({len(urls)} page(s)){flag}")
            for u in sorted(urls)[:3]:
                print(f"      {u}")

    def _prune_empty_dirs(self):
        for d in sorted(self.output_dir.rglob("*"), key=lambda p: -len(p.parts)):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()

    # -- Single-URL fetch --------------------------------------------------

    def validate_url(self, url: str) -> bool:
        allowed = [
            "platform.claude.com", "code.claude.com",
            "modelcontextprotocol.io", "claude.com/docs",
        ]
        return any(f"https://{d}" in url for d in allowed)

    async def fetch_urls(self, urls: List[str]):
        invalid = [u for u in urls if not self.validate_url(u)]
        if invalid:
            print("ERROR: Invalid URLs:", file=sys.stderr)
            for u in invalid:
                print(f"  {u}", file=sys.stderr)
            print("Allowed: platform.claude.com, code.claude.com, "
              "modelcontextprotocol.io, claude.com/docs", file=sys.stderr)
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
        # The human report above is for reading; the snapshot is for diffing.
        # Writing it here too means `--discover` and the scheduled run leave the
        # same artifact, so a manual probe cannot disagree with the pipeline.
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            await self.snapshot_discovery(session)
        print(f"Snapshot written to {self.discovery_path} — "
              f"diff it against the committed copy to find gaps.")


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
  products      Product docs (claude.com/docs: Claude Tag, Cowork, connectors)
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
  fetcher.py --no-reap                      Report pages gone upstream, delete nothing
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
            "github", "support", "products", "all",
        ],
    )
    parser.add_argument("--incremental", action="store_true", help="Skip existing files")
    parser.add_argument("--tree", action="store_true", help="Show source structure")
    parser.add_argument("--discover", action="store_true", help="Probe domains for new sources")
    parser.add_argument(
        "--no-reap", action="store_true",
        help="List files gone upstream without deleting them (full runs only)",
    )

    args = parser.parse_args()
    fetcher = Fetcher(
        output_dir=args.out, jobs=args.jobs,
        incremental=args.incremental, section=args.section,
        no_reap=args.no_reap,
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
