# Source Registry & Architecture

This project archives everything Anthropic publishes that helps people
build with Claude: docs, engineering posts, research, SDK references,
cookbooks, skills, plugins, and support articles.

## Sources (2,900+ files, 11 sources)

| Source | Section | Pages | Method |
|--------|---------|-------|--------|
| code.claude.com | `claude-code` | 141 | llms.txt -> .md suffix |
| platform.claude.com | `api` | 1,541 | sitemap -> .md suffix |
| modelcontextprotocol.io | `mcp` | 203 | sitemap -> .md suffix |
| anthropic.com/engineering | `engineering` | 26 | jina.ai proxy |
| anthropic.com/research | `research` | 118 | jina.ai proxy |
| anthropic.com/news (filtered) | `news` | ~76 | jina.ai proxy |
| anthropic.com/product | `blog` | 4 | jina.ai proxy |
| support.claude.com | `support` | 343 | jina.ai proxy |
| github.com/anthropics/* | `github` | 718 | raw.githubusercontent.com |
| NPM manifest | `meta` | 1 | registry.npmjs.org |
| GitHub CHANGELOG | `meta` | 1 | raw.githubusercontent.com |

## Discovery

`fetcher.py --discover` probes all known Anthropic domains via
robots.txt, sitemap.xml, llms.txt, and llms-full.txt. Run
periodically to find new sources.

Known domains: anthropic.com, platform.claude.com, code.claude.com,
support.claude.com, modelcontextprotocol.io, claude.ai, claude.com

## Content Layout

```
content/
  en/docs/claude-code/   Claude Code + Agent SDK (code.claude.com)
  en/api/                API reference (platform.claude.com)
  en/build-with-claude/  Platform features
  en/agents-and-tools/   Tool use, agent skills
  en/manage-claude/      Admin, billing
  en/managed-agents/     Managed agents API
  mcp/                   MCP protocol spec + community
  blog/
    engineering/         Technical deep-dives
    research/            Research papers
    news/                Model releases, announcements
    product/             Product pages
  support/               Help articles (support.claude.com)
  github/
    cookbooks/           claude-cookbooks (recipes, notebooks)
    skills/              Official Agent Skills
    plugins-official/    Plugin directory
    courses/             Prompt engineering curriculum
    quickstarts/         Deployable app starters
    code-action/         GitHub Actions for Claude Code
    workshops/           CWC workshops
    long-running-agents/ Long-running agent patterns
    sdk-python/          Python SDK docs
    sdk-typescript/      TypeScript SDK docs
```

## Commands

```bash
uv run scripts/fetcher.py                         # Fetch everything
uv run scripts/fetcher.py --section mcp            # MCP spec only
uv run scripts/fetcher.py --section github         # GitHub repos only
uv run scripts/fetcher.py --section engineering    # Engineering blog
uv run scripts/fetcher.py --incremental            # Skip existing
uv run scripts/fetcher.py --tree                   # Show all sources
uv run scripts/fetcher.py --discover               # Probe for new sources
uv run scripts/fetcher.py URL [URL ...]            # Fetch specific URLs
```

GitHub repo fetching needs `GITHUB_TOKEN` or `GH_TOKEN` env var.
Blog/research/support use jina.ai which rate-limits at ~10 req/s.

## Source Registry

`sources.json` contains the complete machine-readable registry of all
discovered Anthropic content sources, including domains, aliases, and
per-source metadata.
