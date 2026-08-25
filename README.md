# Claude Code Docs

> Comprehensive, auto-updating archive of everything Anthropic publishes
> for building with Claude. 3,900+ docs from 12 sources.

[![fetch](https://github.com/thevibeworks/claude-code-docs/actions/workflows/fetch-claude-docs.yml/badge.svg)](https://github.com/thevibeworks/claude-code-docs/actions/workflows/fetch-claude-docs.yml)
[![review](https://github.com/thevibeworks/claude-code-docs/actions/workflows/claude-review.yml/badge.svg)](https://github.com/thevibeworks/claude-code-docs/actions/workflows/claude-review.yml)
[![license](https://img.shields.io/github/license/thevibeworks/claude-code-docs)](LICENSE)
[![docs](https://img.shields.io/badge/docs-3900%2B-blue)](#content)

Clone this repo and point Claude Code at it. Every doc, tutorial, cookbook,
skill, and engineering post Anthropic has published -- searchable, version-
controlled, and offline.

## Install

```bash
git clone https://github.com/thevibeworks/claude-code-docs
cd claude-code-docs
```

Then ask Claude Code anything:

```bash
claude "how does the agent loop work?"
claude "show me the MCP spec for tool annotations"
claude "what did the 'Building Effective Agents' post recommend?"
claude "how do I set up hooks in the Agent SDK?"
```

## Content

| Source | Section | Files | What |
|--------|---------|------:|------|
| code.claude.com | `--section claude-code` | 198 | Claude Code + Agent SDK docs |
| platform.claude.com | `--section api` | 1,993 | API reference, build guides |
| claude.com/docs | `--section products` | 215 | Claude Tag, Cowork, office agents, connectors |
| modelcontextprotocol.io | `--section mcp` | 373 | MCP spec, SDKs, governance |
| anthropic.com | `--section engineering` | 25 | "Building Effective Agents", context engineering, tool use |
| anthropic.com | `--section research` | 118 | Research papers |
| anthropic.com | `--section news` | ~76 | Model releases, announcements |
| github.com/anthropics | `--section github` | 718 | Cookbooks, skills, plugins, courses, SDK docs |
| support.claude.com | `--section support` | 365 | Help articles |

```
content/
  en/docs/claude-code/   Claude Code + Agent SDK
  en/api/                API reference (1,500+ endpoints)
  en/build-with-claude/  Platform features
  en/agents-and-tools/   Tool use, agent skills
  en/manage-claude/      Admin, billing, managed agents
  claude/                Product docs (Claude Tag, Cowork, office agents)
  mcp/                   MCP protocol spec + community
  blog/
    engineering/         Building Effective Agents, context engineering, ...
    research/            Research papers
    news/                Model releases
  github/
    cookbooks/           164 recipes + notebooks
    skills/              90 official Agent Skills
    plugins-official/    266 plugin docs
    courses/             80 prompt engineering notebooks
    quickstarts/         Deployable app starters
    code-action/         GitHub Actions for Claude Code
    sdk-python/          Python SDK reference
    sdk-typescript/      TypeScript SDK reference
  support/               365 help articles
```

## Fetching

Auto-updates every 6 hours via GitHub Actions. To fetch manually:

```bash
# Requires: uv (https://docs.astral.sh/uv/)
uv run scripts/fetcher.py                    # Fetch everything (~3 min)
uv run scripts/fetcher.py --section mcp      # MCP spec only
uv run scripts/fetcher.py --section github   # GitHub repos only
uv run scripts/fetcher.py --incremental      # Skip existing files
uv run scripts/fetcher.py --tree             # Show all sources + counts
uv run scripts/fetcher.py --discover         # Probe domains for new sources
```

GitHub repo fetching needs `GITHUB_TOKEN` or `GH_TOKEN` in the environment.
Blog, research, and support articles use [jina.ai](https://jina.ai) for
HTML-to-markdown conversion (rate-limited at ~10 req/s).

See [`sources.json`](sources.json) for the complete machine-readable source
registry.

## Source Discovery

The fetcher doesn't just download from hardcoded URLs. `--discover` probes
every known Anthropic domain for `robots.txt`, `sitemap.xml`, `llms.txt`,
and `llms-full.txt`, then compares against what we already archive.

Known domains: `anthropic.com`, `platform.claude.com`, `code.claude.com`,
`support.claude.com`, `modelcontextprotocol.io`, `claude.ai`, `claude.com`

Run `--discover` periodically to catch new sources before they go stale.

**Sitemaps are treated as incomplete, not authoritative.** Upstream de-indexes
pages it still serves: in July 2026 platform.claude.com dropped every
per-language SDK reference page from both its sitemap and its `llms.txt` while
continuing to edit them, and the archive quietly stopped refreshing 1,560 files
for seven weeks. So every full run also refetches what is already on disk, and
pages that really died are removed by the reaper below rather than by absence
from an index.

### Reaping

A page removed upstream used to live here forever — the fetcher only ever added
or overwrote. Full runs now delete archived files whose URL returns 404/410 or
the site's HTML shell, with two guardrails:

- **Only markup is deleted automatically.** A file holding real markdown whose
  URL has died is content Anthropic removed and we may hold the only copy; it is
  reported for a human instead of destroyed by a job that merges its own PRs.
- **A mass-deletion circuit breaker.** More than 200 pages vanishing at once
  means an upstream outage, not 200 real deletions — nothing is deleted and the
  run fails loudly.

`--no-reap` reports what would go without touching anything.

### Tombstones

`tombstones.json` records every URL confirmed gone upstream, with the date and
reason. It exists so that a page which died once does not report as a fresh
failure on every subsequent run — 123 standing failures would pin the success
rate at 96.9% and bury the one new breakage that matters. Later runs count
known deaths quietly and print only what changed: pages newly gone, and pages
that came *back* (whose tombstone is then removed automatically). The success
rate is computed over live docs, so it means something.

## Automation

Two GitHub Actions workflows power this repo:

**[fetch-claude-docs.yml](.github/workflows/fetch-claude-docs.yml)** --
Scheduled every 6 hours. Runs the fetcher, then hands the diff to
Claude Code (via [claude-code-action](https://github.com/anthropics/claude-code-action))
which decides: ignore noise, commit minor fixes directly, or create a PR
for meaningful changes. Sends push notifications via
[barkme](https://github.com/nickchou/barkme-mcp-server) for PRs.

**[claude-review.yml](.github/workflows/claude-review.yml)** --
Triggered on PRs and `@claude` mentions. Reviews changes, merges routine
updates, creates tracking issues for version bumps, and alerts humans only
for breaking changes.

## Contributing

PRs welcome. The fetcher is a single Python file (`scripts/fetcher.py`)
with no framework dependencies beyond `aiohttp` and `aiofiles`.

To add a new source:
1. Add the source definition to `sources.json`
2. Add the fetch logic to `scripts/fetcher.py`
3. Run `uv run scripts/fetcher.py --section <name>` to test
4. Update `--section` choices in the CLI

## Disclaimer

Unofficial mirror for educational and development purposes. Documentation
content is sourced from Anthropic's public sites. For official docs, visit
[code.claude.com](https://code.claude.com) and
[platform.claude.com](https://platform.claude.com). Repository code from
[anthropics/claude-code](https://github.com/anthropics/claude-code).
Redistribution should comply with Anthropic's
[terms](https://www.anthropic.com/legal/commercial-terms).

## License

[MIT](LICENSE)
