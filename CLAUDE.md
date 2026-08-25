# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Comprehensive archive of everything Anthropic publishes for building with
Claude. 3,900+ docs from 12 sources; active sources auto-updated four
times daily (blog archive frozen, see Fetcher).

## Fetcher

`scripts/fetcher.py` -- single-file multi-source fetcher.

Sources: code.claude.com, platform.claude.com, claude.com/docs,
modelcontextprotocol.io, support.claude.com (sitemap + .md),
github.com/anthropics/* (10 repos). anthropic.com blog
(engineering/research/news) is a FROZEN archive as of 2026-07: the site is
HTML-only and the jina.ai proxy path was removed.

Two rules keep the archive honest, both learned the hard way:

- **Discovery surfaces are incomplete.** Sitemaps and llms.txt undercount what
  a site serves, so every full run also refetches what is already on disk.
  Without this, 1,560 de-indexed-but-live API pages sat stale for seven weeks.
- **The archive must be able to shrink.** Full runs reap files whose URL is
  gone (404/410 or HTML shell). Only markup is deleted automatically; real
  markdown that died upstream is reported for a human. A >200-file reap is
  refused outright as an upstream outage.

```bash
uv run scripts/fetcher.py                    # Fetch everything
uv run scripts/fetcher.py --section mcp      # Single section
uv run scripts/fetcher.py --tree             # Show sources
uv run scripts/fetcher.py --discover         # Probe for new sources
uv run scripts/fetcher.py --no-reap          # Report dead pages, delete none
```

Sections: `claude-code`, `api`, `platform`, `mcp`, `github`, `support`,
`products`, `all`

Source registry: `sources.json`
Architecture: `REFACTOR.md`

When adding new sections:
1. Add source to `sources.json`
2. Add fetch logic + output path mapping to `fetcher.py`
3. Test: `uv run scripts/fetcher.py --section <name>`
4. Update this file's doc references below

Reference documentation files in this repository when providing guidance.


### Documentation Resources

Use these paths to reference documentation when helping users:

#### Claude Code Documentation (from code.claude.com)
- `@./content/en/docs/claude-code/overview.md` - Claude Code overview and capabilities
- `@./content/en/docs/claude-code/quickstart.md` - Getting started guide
- `@./content/en/docs/claude-code/setup.md` - Installation and setup
- `@./content/en/docs/claude-code/settings.md` - Configuration and permissions setup
- `@./content/en/docs/claude-code/common-workflows.md` - Common usage patterns
- `@./content/en/docs/claude-code/memory.md` - Memory management and CLAUDE.md
- `@./content/en/docs/claude-code/interactive-mode.md` - Keyboard shortcuts and interactive features
- `@./content/en/docs/claude-code/slash-commands.md` - Available slash commands
- `@./content/en/docs/claude-code/hooks.md` - Hooks reference
- `@./content/en/docs/claude-code/hooks-guide.md` - Hooks guide
- `@./content/en/docs/claude-code/troubleshooting.md` - Problem solving
- `@./content/en/docs/claude-code/cli-reference.md` - Command line interface reference
- `@./content/en/docs/claude-code/jetbrains.md` - JetBrains IDE integration
- `@./content/en/docs/claude-code/vs-code.md` - VS Code integration
- `@./content/en/docs/claude-code/desktop.md` - Claude Code desktop app
- `@./content/en/docs/claude-code/claude-code-on-the-web.md` - Claude Code on the web
- `@./content/en/docs/claude-code/slack.md` - Claude Code in Slack
- `@./content/en/docs/claude-code/mcp.md` - Model Context Protocol
- `@./content/en/docs/claude-code/github-actions.md` - GitHub Actions integration
- `@./content/en/docs/claude-code/gitlab-ci-cd.md` - GitLab CI/CD integration
- `@./content/en/docs/claude-code/sdk/migration-guide.md` - SDK migration guide
- `@./content/en/docs/claude-code/third-party-integrations.md` - Third-party integrations
- `@./content/en/docs/claude-code/devcontainer.md` - Development containers
- `@./content/en/docs/claude-code/security.md` - Security considerations
- `@./content/en/docs/claude-code/sandboxing.md` - Sandboxed bash tool
- `@./content/en/docs/claude-code/iam.md` - Authentication and permissions
- `@./content/en/docs/claude-code/monitoring-usage.md` - OpenTelemetry monitoring
- `@./content/en/docs/claude-code/analytics.md` - Analytics and usage tracking
- `@./content/en/docs/claude-code/costs.md` - Cost management
- `@./content/en/docs/claude-code/data-usage.md` - Data usage policies
- `@./content/en/docs/claude-code/legal-and-compliance.md` - Legal and compliance
- `@./content/en/docs/claude-code/amazon-bedrock.md` - Amazon Bedrock integration
- `@./content/en/docs/claude-code/google-vertex-ai.md` - Google Vertex AI integration
- `@./content/en/docs/claude-code/microsoft-foundry.md` - Microsoft Foundry integration
- `@./content/en/docs/claude-code/llm-gateway.md` - LLM gateway configuration
- `@./content/en/docs/claude-code/model-config.md` - Model configuration
- `@./content/en/docs/claude-code/network-config.md` - Network configuration
- `@./content/en/docs/claude-code/terminal-config.md` - Terminal configuration
- `@./content/en/docs/claude-code/output-styles.md` - Output styling and formatting
- `@./content/en/docs/claude-code/statusline.md` - Status line configuration
- `@./content/en/docs/claude-code/checkpointing.md` - Session checkpointing
- `@./content/en/docs/claude-code/headless.md` - Headless mode
- `@./content/en/docs/claude-code/plugins.md` - Plugin system
- `@./content/en/docs/claude-code/plugins-reference.md` - Plugin reference
- `@./content/en/docs/claude-code/plugin-marketplaces.md` - Plugin marketplaces
- `@./content/en/docs/claude-code/skills.md` - Claude Skills
- `@./content/en/docs/claude-code/sub-agents.md` - Sub-agents
- `@./content/CHANGELOG.md` - Claude Code GitHub CHANGELOG

#### Platform Docs (from platform.claude.com)
- `content/en/api/` - API reference (1,500+ docs)
- `content/en/build-with-claude/` - Platform features, streaming, batch
- `content/en/agents-and-tools/` - Tool use, agent skills, MCP tunnels
- `content/en/manage-claude/` - Admin, billing, organizations
- `content/en/managed-agents/` - Managed agents API
- `content/en/test-and-evaluate/` - Testing and evaluation

#### Product Docs (from claude.com/docs)
- `content/claude/claude-tag/` - Claude Tag / Claude in Slack (65)
- `content/claude/government/` - Government offerings (38)
- `content/claude/connectors/` - Connectors, building + publishing (33)
- `content/claude/claude-science/` - Claude for Science (29)
- `content/claude/third-party/` - Bedrock, Vertex, Foundry desktop setups (28)
- `content/claude/office-agents/` - Claude for Excel, Word, PowerPoint, Outlook (12)
- `content/claude/cowork/` - Claude Cowork (6)

#### MCP Protocol (from modelcontextprotocol.io)
- `content/mcp/docs/` - Getting started, build client/server
- `content/mcp/specification/` - Protocol spec versions
- `content/mcp/seps/` - Specification Enhancement Proposals
- `content/mcp/community/` - Governance, working groups

#### Engineering & Research (from anthropic.com) — FROZEN archive, not auto-updated
- `content/blog/engineering/` - "Building Effective Agents", tool use, harness design
- `content/blog/research/` - Research papers
- `content/blog/news/` - Model releases, announcements

#### GitHub Repos (from github.com/anthropics)
- `content/github/cookbooks/` - 164 recipes + notebooks
- `content/github/skills/` - 90 official Agent Skills
- `content/github/plugins-official/` - 266 plugin docs
- `content/github/courses/` - 80 prompt engineering notebooks
- `content/github/code-action/` - GitHub Actions docs
- `content/github/sdk-python/` - Python SDK reference
- `content/github/sdk-typescript/` - TypeScript SDK reference

## Repository Structure

```
content/                       3,900+ files
  en/docs/claude-code/         Claude Code + Agent SDK (198)
  en/api/                      API reference (1,900+)
  en/build-with-claude/        Platform features
  en/agents-and-tools/         Tool use, agent skills
  claude/                      Product docs (215)
  mcp/                         MCP protocol spec (373)
  blog/                        Engineering, research, news
  github/                      10 repos (718 files)
  support/                     Help articles (365)
scripts/
  fetcher.py                   Multi-source fetcher
sources.json                   Source registry
```

### External Resources

- https://github.com/anthropics/claude-code/issues
- https://code.claude.com/docs/en/overview
- https://platform.claude.com/docs/en/home
- https://modelcontextprotocol.io
- https://claude.com/docs/llms.txt
