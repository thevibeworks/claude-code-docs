#!/usr/bin/env python3
"""
Fetch Claude Code documentation from docs.claude.com

Usage:
  uv run scripts/fetcher.py
  uv run scripts/fetcher.py --tree
  uv run scripts/fetcher.py --section en/docs/claude-code
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
        self.sitemap_url = "https://docs.claude.com/sitemap.xml"
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

    def extract_urls(self, sitemap_xml: str) -> List[str]:
        urls = []
        for line in sitemap_xml.split("\n"):
            if "<loc>" in line and "</loc>" in line:
                url = line.split("<loc>")[1].split("</loc>")[0]
                if "/en/" in url and "docs.claude.com" in url:
                    urls.append(url)
        return urls

    def get_output_path(self, url: str) -> Path:
        path = url.replace("https://docs.claude.com/", "")
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

            # Fetch sitemaps
            print("Fetching sitemaps...")
            sitemap_xml = await self.fetch_sitemap(session, self.sitemap_url)
            anthropic_xml = await self.fetch_sitemap(
                session, self.anthropic_sitemap_url
            )

            # Extract docs URLs
            urls = self.extract_urls(sitemap_xml)

            # Extract blog URLs
            blog_urls = []
            for line in anthropic_xml.split("\n"):
                if "<loc>" in line and "claude-code" in line:
                    url = line.split("<loc>")[1].split("</loc>")[0]
                    blog_urls.append(url)

            # Filter by section if specified
            if self.section:
                section_prefix = f"https://docs.claude.com/{self.section}"
                urls = [u for u in urls if u.startswith(section_prefix)]
                if not self.section.startswith("blog"):
                    blog_urls = []

            self.stats["total"] = len(urls) + len(blog_urls)
            print(f"Total: {self.stats['total']} ({len(urls)} docs, {len(blog_urls)} blog)")
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
        print("Fetching sitemap...")
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            sitemap_xml = await self.fetch_sitemap(session, self.sitemap_url)
            urls = self.extract_urls(sitemap_xml)

        print(f"\ndocs.claude.com ({len(urls)} URLs)\n")

        # Group by language/top-level
        lang_groups = defaultdict(list)
        for url in urls:
            path = url.replace("https://docs.claude.com/", "")
            parts = path.split("/")
            if len(parts) >= 1:
                lang_groups[parts[0]].append(path)

        for lang in sorted(lang_groups.keys()):
            paths = lang_groups[lang]
            print(f"{lang}/ ({len(paths)})")

            # Group by second level (docs, api, resources, etc.)
            second_level = defaultdict(list)
            for path in paths:
                parts = path.split("/")
                if len(parts) >= 2:
                    second_level[parts[1]].append(path)

            for section in sorted(second_level.keys(), key=lambda x: -len(second_level[x])):
                section_paths = second_level[section]
                print(f"  {section}/ ({len(section_paths)})")

                # Group by third level
                third_level = defaultdict(int)
                for path in section_paths:
                    parts = path.split("/")
                    if len(parts) >= 3:
                        third_level[parts[2]] += 1

                shown = 0
                for subsection, count in sorted(
                    third_level.items(), key=lambda x: -x[1]
                ):
                    if shown < 8:
                        print(f"    {subsection}/ ({count})")
                        shown += 1
                    else:
                        remaining = len(third_level) - shown
                        if remaining > 0:
                            print(f"    [+{remaining} more]")
                        break

            print()

        print("Usage:")
        print("  fetcher.py --section en/docs/claude-code")
        print("  fetcher.py --section en/api/agent-sdk")
        print("  fetcher.py --section en/docs")


async def main():
    parser = ArgumentParser(
        description="Fetch Claude Code documentation",
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fetcher.py                                 Fetch all docs
  fetcher.py --tree                          Show sitemap structure
  fetcher.py --section en/docs/claude-code   Fetch specific section
  fetcher.py --incremental                   Skip existing files
  fetcher.py --jobs 100                      Use 100 parallel jobs
        """,
    )
    parser.add_argument("--out", default="content", help="Output directory")
    parser.add_argument(
        "--jobs", "-j", type=int, default=50, help="Parallel jobs (default: 50)"
    )
    parser.add_argument(
        "--section", "-s", help="Filter to specific section (e.g., en/docs/claude-code)"
    )
    parser.add_argument(
        "--incremental", action="store_true", help="Skip existing files"
    )
    parser.add_argument("--tree", action="store_true", help="Show sitemap structure")

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
