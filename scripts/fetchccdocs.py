#!/usr/bin/env python3
"""
Fetch Claude Code documentation from docs.claude.com
Fast async implementation with concurrent downloads using Python 3.14 free-threaded

Usage:
  uv run scripts/fetchccdocs.py
  uv run scripts/fetchccdocs.py --jobs 100
  uv run scripts/fetchccdocs.py --incremental
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
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional

import aiohttp
import aiofiles
from tqdm.asyncio import tqdm


class DocFetcher:
    def __init__(
        self,
        output_dir: str = "content",
        format: str = "md",
        parallel_jobs: int = 50,
        incremental: bool = False,
        sections: Optional[List[str]] = None,
    ):
        self.output_dir = Path(output_dir)
        self.format = format
        self.parallel_jobs = parallel_jobs
        self.incremental = incremental
        self.sections = sections
        self.sitemap_url = "https://docs.claude.com/sitemap.xml"
        self.anthropic_sitemap_url = "https://www.anthropic.com/sitemap.xml"
        self.metadata_file = self.output_dir / ".metadata.json"
        self.previous_checksums: Dict[str, str] = {}

        self.stats = {
            "total": 0,
            "downloaded": 0,
            "skipped": 0,
            "failed": 0,
        }
        
    async def load_previous_metadata(self):
        """Load previous checksums for incremental updates"""
        if not self.metadata_file.exists():
            return
        
        try:
            async with aiofiles.open(self.metadata_file, 'r') as f:
                content = await f.read()
                metadata = json.loads(content)
                for item in metadata.get("items", []):
                    self.previous_checksums[item["url"]] = item.get("sha256", "")
        except Exception as e:
            print(f"[WARN] Could not load previous metadata: {e}")
    
    async def fetch_sitemap(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch sitemap XML"""
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    
    async def extract_urls(self, session: aiohttp.ClientSession) -> Dict[str, List[str]]:
        """Extract all documentation URLs from sitemaps"""
        print("[INFO] Fetching sitemaps...")

        sitemap_xml = await self.fetch_sitemap(session, self.sitemap_url)
        anthropic_xml = await self.fetch_sitemap(session, self.anthropic_sitemap_url)

        patterns = {
            "build": r"https://docs\.claude\.com/en/docs/build-with-claude",
            "agents": r"https://docs\.claude\.com/en/docs/agents-and-tools",
            "claude-code": r"https://docs\.claude\.com/en/docs/claude-code",
            "agent-sdk": r"https://docs\.claude\.com/en/api/agent-sdk",
            "api-skills": r"https://docs\.claude\.com/en/api/skills",
            "admin-api": r"https://docs\.claude\.com/en/api/admin-api",
            "api-reference": r"https://docs\.claude\.com/en/api/(messages|models|files-|errors|rate-limits|versioning)",
            "about-claude": r"https://docs\.claude\.com/en/docs/about-claude",
            "test-eval": r"https://docs\.claude\.com/en/docs/test-and-evaluate",
            "get-started": r"https://docs\.claude\.com/en/docs/(get-started|intro|overview)",
            "release-notes": r"https://docs\.claude\.com/en/release-notes",
            "resources": r"https://docs\.claude\.com/en/resources",
            "blog": r"https://www\.anthropic\.com/.*claude-code",
        }

        urls_by_section = {}

        for section, pattern in patterns.items():
            if section == "blog":
                continue
            urls = []
            for line in sitemap_xml.split('\n'):
                if '<loc>' in line and '</loc>' in line:
                    url = line.split('<loc>')[1].split('</loc>')[0]
                    if self._matches_pattern(url, section):
                        urls.append(url)
            if urls:
                urls_by_section[section] = urls

        blog_urls = []
        for line in anthropic_xml.split('\n'):
            if '<loc>' in line and 'claude-code' in line:
                url = line.split('<loc>')[1].split('</loc>')[0]
                blog_urls.append(url)
        if blog_urls:
            urls_by_section["blog"] = blog_urls
        
        return urls_by_section
    
    def _matches_pattern(self, url: str, section: str) -> bool:
        """Simple pattern matching for URL categorization"""
        if not "/en/" in url:
            return False
            
        if section == "build":
            return "/docs/build-with-claude" in url
        elif section == "agents":
            return "/docs/agents-and-tools" in url
        elif section == "claude-code":
            return "/docs/claude-code" in url
        elif section == "agent-sdk":
            return "/api/agent-sdk" in url
        elif section == "api-skills":
            return "/api/skills" in url
        elif section == "admin-api":
            return "/api/admin-api" in url
        elif section == "api-reference":
            return "/api/" in url and any(x in url for x in ["messages", "models", "files-", "errors", "rate-limits", "versioning", "batch"])
        elif section == "about-claude":
            return "/docs/about-claude" in url
        elif section == "test-eval":
            return "/docs/test-and-evaluate" in url
        elif section == "get-started":
            return any(x in url for x in ["/docs/get-started", "/docs/intro", "/docs/overview"])
        elif section == "release-notes":
            return "/release-notes" in url
        elif section == "resources":
            return "/resources" in url
        return False
    
    def get_output_path(self, url: str, section: str) -> Path:
        """Determine output file path for a URL"""
        if "docs.claude.com" in url:
            rel_path = url.split("/en/", 1)[1]
        elif "anthropic.com" in url:
            rel_path = url.split("anthropic.com/", 1)[1]
        else:
            rel_path = url.split("/")[-1]

        if section in ["build", "agents"]:
            base_dir = section.replace("agents", "agents-and-tools")
            if f"/docs/{base_dir.split('-')[0]}" in url:
                rel_path = rel_path.split("/", 2)[2]  # Remove docs/section-name/
        elif section == "claude-code":
            base_dir = "claude-code-docs"
            if "/docs/claude-code/" in url:
                rel_path = rel_path.split("docs/claude-code/", 1)[1]
        elif section.startswith("api") or section == "agent-sdk":
            base_dir = "claude-code-docs/api"
            if "/api/" in url:
                rel_path = rel_path.split("api/", 1)[1]
        elif section == "blog":
            base_dir = "anthropic-blog"
        elif section == "resources":
            base_dir = "resources"
        elif section == "release-notes":
            base_dir = "release-notes"
        elif section in ["about-claude", "test-eval", "get-started"]:
            base_dir = section.replace("test-eval", "test-and-evaluate")
            if "/docs/" in rel_path:
                rel_path = rel_path.split("/", 2)[2]
        else:
            base_dir = section
        
        output_path = self.output_dir / base_dir / f"{rel_path}.{self.format}"
        return output_path
    
    async def download_doc(
        self,
        session: aiohttp.ClientSession,
        url: str,
        section: str,
        semaphore: asyncio.Semaphore,
    ) -> Dict:
        """Download a single document"""
        async with semaphore:
            output_path = self.get_output_path(url, section)

            if self.incremental and output_path.exists():
                self.stats["skipped"] += 1
                return {"url": url, "status": "skipped", "path": str(output_path)}

            try:
                if section == "blog":
                    fetch_url = f"https://r.jina.ai/{url}"
                else:
                    fetch_url = f"{url}.{self.format}"

                async with session.get(fetch_url) as response:
                    response.raise_for_status()
                    content = await response.read()

                output_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(output_path, 'wb') as f:
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
                return {
                    "url": url,
                    "status": "failed",
                    "error": str(e),
                }
    
    async def fetch_all(self):
        """Main fetch logic"""
        print(f"[INFO] Starting fetch to {self.output_dir}")
        print(f"[INFO] Parallel jobs: {self.parallel_jobs}")
        print(f"[INFO] Incremental mode: {self.incremental}")

        if self.incremental:
            await self.load_previous_metadata()

        timeout = aiohttp.ClientTimeout(total=300)
        connector = aiohttp.TCPConnector(limit=self.parallel_jobs)

        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            urls_by_section = await self.extract_urls(session)

            if self.sections:
                print(f"[INFO] Filtering to sections: {', '.join(self.sections)}")
                urls_by_section = {
                    section: urls
                    for section, urls in urls_by_section.items()
                    if section in self.sections or any(s in section for s in self.sections)
                }

            all_tasks = []
            for section, urls in urls_by_section.items():
                self.stats["total"] += len(urls)
                print(f"[INFO] {section}: {len(urls)} docs")

            print(f"\n[INFO] Total: {self.stats['total']} documents")
            print("[INFO] Starting downloads...\n")

            semaphore = asyncio.Semaphore(self.parallel_jobs)

            for section, urls in urls_by_section.items():
                for url in urls:
                    task = self.download_doc(session, url, section, semaphore)
                    all_tasks.append(task)

            results = []
            for coro in tqdm.as_completed(all_tasks, total=len(all_tasks), desc="Downloading"):
                result = await coro
                results.append(result)

            await self.save_metadata(results)
            self.print_summary()
    
    async def save_metadata(self, results: List[Dict]):
        """Save fetch metadata"""
        metadata = {
            "metadata": {
                "version": "1.0",
                "fetch_date": datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z",
                "format": self.format,
            },
            "items": [r for r in results if r.get("status") == "success"],
            "summary": {
                "total": self.stats["total"],
                "downloaded": self.stats["downloaded"],
                "skipped": self.stats["skipped"],
                "failed": self.stats["failed"],
                "success_rate": round(self.stats["downloaded"] / self.stats["total"] * 100, 1) if self.stats["total"] > 0 else 0,
            }
        }
        
        async with aiofiles.open(self.metadata_file, 'w') as f:
            await f.write(json.dumps(metadata, indent=2))
    
    def print_summary(self):
        """Print fetch summary"""
        print("\n" + "="*50)
        print("FETCH SUMMARY")
        print("="*50)
        print(f"Total:      {self.stats['total']}")
        print(f"Downloaded: {self.stats['downloaded']}")
        print(f"Skipped:    {self.stats['skipped']}")
        print(f"Failed:     {self.stats['failed']}")
        if self.stats["total"] > 0:
            success_rate = (self.stats["downloaded"] / self.stats["total"]) * 100
            print(f"Success:    {success_rate:.1f}%")
        print("="*50)


async def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch Claude Code documentation",
        epilog="""
Examples:
  uv run fetchccdocs.py                               # Fetch all docs (fresh)
  uv run fetchccdocs.py --section agent-sdk           # Only SDK docs
  uv run fetchccdocs.py --section agent-sdk,api-reference  # SDK + API reference
  uv run fetchccdocs.py --incremental                 # Skip existing files

Available sections:
  build, agents, claude-code, agent-sdk, api-skills, admin-api,
  api-reference, about-claude, test-eval, get-started, release-notes,
  resources, blog
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--out", default="content", help="Output directory")
    parser.add_argument("--format", default="md", help="Output format")
    parser.add_argument("--jobs", "-j", type=int, default=50, help="Parallel jobs (default: 50)")
    parser.add_argument("--section", "-s", help="Comma-separated list of sections to fetch (e.g., agent-sdk,api-reference)")
    parser.add_argument("--incremental", action="store_true", help="Enable incremental updates (skip existing files)")

    args = parser.parse_args()

    sections = None
    if args.section:
        sections = [s.strip() for s in args.section.split(",")]

    fetcher = DocFetcher(
        output_dir=args.out,
        format=args.format,
        parallel_jobs=args.jobs,
        incremental=args.incremental,
        sections=sections,
    )

    await fetcher.fetch_all()


if __name__ == "__main__":
    asyncio.run(main())
