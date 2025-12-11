# Documentation Fetch Script

## fetcher.py

Async Python 3.14 fetcher for Claude documentation.

**Sources** (Dec 2025):
- `platform.claude.com/sitemap.xml` - API docs, Agent SDK, prompt engineering (528 docs)
- `code.claude.com/docs/llms.txt` - Claude Code docs (47 docs)
- `anthropic.com/sitemap.xml` - Blog posts

### Usage

```bash
uv run scripts/fetcher.py                       # Fetch all (575+ docs)
uv run scripts/fetcher.py --section claude-code # Claude Code only
uv run scripts/fetcher.py --section api         # API docs only
uv run scripts/fetcher.py --section blog        # Blog posts only
uv run scripts/fetcher.py --tree                # Show structure
uv run scripts/fetcher.py --incremental         # Skip existing
uv run scripts/fetcher.py --jobs 100            # More parallelism
```

### Performance

| Section | Docs | Time |
|---------|------|------|
| All | 575+ | ~40 sec |
| claude-code | 47 | ~5 sec |
| api | 528 | ~35 sec |

### Output Structure

```
content/
├── en/docs/claude-code/   # Claude Code (from code.claude.com)
├── en/build-with-claude/  # Platform docs (from platform.claude.com)
├── en/agent-sdk/
├── en/api/
├── blog/
├── CHANGELOG.md
└── claude-code-manifest.json
```

### Requirements

- Python 3.14+ (free-threaded)
- `uv` package manager
- Dependencies auto-installed via inline script metadata
