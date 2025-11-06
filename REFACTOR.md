# Refactor: Documentation Fetcher

## What

Rewrite `scripts/fetchccdocs.py` → `scripts/fetcher.py`

Clean 1:1 mirror of sitemap. Auto-discover sections. Zero hardcoding.

## Why

Current problems:
- Hardcoded patterns (fragile, needs updates for new sections)
- Convoluted mapping (api/agent-sdk → claude-code-docs/api/api/agent-sdk)
- 50+ lines of path logic
- Missing 6 API endpoints
- Adding sections requires code changes

Goals:
- 100% coverage (all 269 sitemap URLs)
- Zero hardcoding (auto-discover from sitemap)
- Simple mapping (3 lines vs 50 lines)
- Future-proof (new languages/sections auto-work)
- Fast (~5 sec, async concurrent fetching)

## How

### Target Structure

True 1:1 mirror:

```
content/
├── en/
│   ├── docs/
│   ├── api/
│   ├── resources/
│   └── release-notes/
├── zh/                      # Future
├── blog/                    # anthropic.com posts
├── claude-code-manifest.json
└── .metadata.json
```

Mapping: `https://docs.claude.com/{path}` → `content/{path}.md`

### Core Changes

**1. Auto-discover sections**
```python
def extract_urls(session):
    sitemap = await fetch_sitemap(session)
    urls = defaultdict(list)

    for url in parse_sitemap_urls(sitemap):
        if '/en/' not in url:
            continue
        urls[url].append(url)

    return urls
```

**2. Simple path mapping**
```python
def get_output_path(url):
    path = url.replace('https://docs.claude.com/', '')
    return output_dir / f"{path}.md"
```

**3. Special files (outside /en/)**
```python
# NPM manifest
await fetch_npm_manifest()
→ content/claude-code-manifest.json

# GitHub CHANGELOG
await fetch_github_changelog()
→ content/CHANGELOG.md

# Blog posts (anthropic.com)
await fetch_blog_posts()
→ content/blog/{slug}.md
```

### New Features

**--tree**: Browse sitemap structure
```
$ fetcher.py --tree

en/ (269)
  docs/ (116)
    claude-code/ (44)
    build-with-claude/ (30)
    ...
  api/ (84)
    agent-sdk/ (16)
    admin-api/ (25)
    ...
```

**--section**: Filter by path
```
$ fetcher.py --section en/docs/claude-code
$ fetcher.py --section en/api/agent-sdk
$ fetcher.py --section en/docs
```

### CLI

```
fetcher.py                          Fetch all
fetcher.py --tree                   Show structure
fetcher.py --section en/docs        Filter by path
fetcher.py --incremental            Skip existing
fetcher.py --jobs 100               Parallel jobs
```

### Implementation

Single-file script following @repo/sbin/AGENTS.md:
- Minimal comments; --help is docs
- Clean output (no emojis, minimal logging)
- Fail fast
- Type hints
- PEP 723 inline deps

Core logic:
```python
class Fetcher:
    async def fetch_all(self):
        # Fetch special files first
        await self.fetch_npm_manifest()
        await self.fetch_github_changelog()

        # Auto-discover and fetch sitemap URLs
        urls = await self.extract_urls()

        # Filter if --section specified
        if self.section:
            urls = [u for u in urls if u.startswith(self.section)]

        # Concurrent download
        semaphore = asyncio.Semaphore(self.jobs)
        tasks = [self.download(url, semaphore) for url in urls]
        await asyncio.gather(*tasks)

    def get_output_path(self, url):
        path = url.replace('https://docs.claude.com/', '')
        return self.output_dir / f"{path}.md"
```

Efficiency:
- Async/await with aiohttp
- Concurrent downloads (default 50 jobs)
- Single sitemap fetch
- Incremental mode (skip existing)
- Python 3.14t free-threaded

### Update CLAUDE.md

Replace all doc references:
```
@./content/claude-code-docs/          → @./content/en/docs/claude-code/
@./content/build-with-claude/         → @./content/en/docs/build-with-claude/
@./content/agents-and-tools/          → @./content/en/docs/agents-and-tools/
@./content/about-claude/              → @./content/en/docs/about-claude/
@./content/test-and-evaluate/         → @./content/en/docs/test-and-evaluate/
@./content/resources/                 → @./content/en/resources/
@./content/release-notes/             → @./content/en/release-notes/
```

Keep:
```
@./content/claude-code-manifest.json  (unchanged)
@./content/CHANGELOG.md               (new location)
```

### Workflow Updates

`.github/workflows/fetch-claude-docs.yml`:
```yaml
- name: Fetch docs
  run: uv run scripts/fetcher.py
```

No other changes needed.

## Verification

After implementation:
1. Run `fetcher.py` - verify all 269 URLs fetched
2. Check `content/en/` structure mirrors sitemap
3. Verify special files (manifest.json, CHANGELOG.md, blog/)
4. Test `--tree` output
5. Test `--section` filtering
6. Update and test CLAUDE.md references
7. Remove old content/ directories
8. Delete `scripts/fetchccdocs.py` and `scripts/fetchccdocs.sh`

Done when:
- 100% coverage (269/269 URLs + manifest + changelog + blog)
- Clean 1:1 structure
- CLAUDE.md references work
- Workflow runs successfully
