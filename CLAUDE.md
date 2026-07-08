# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Comprehensive archive of everything Anthropic publishes for building with
Claude. 2,900+ docs from 11 sources; active sources auto-updated four
times daily (blog archive frozen, see Fetcher).

## Fetcher

`scripts/fetcher.py` -- single-file multi-source fetcher.

Sources: code.claude.com, platform.claude.com, modelcontextprotocol.io,
support.claude.com (sitemap + .md), github.com/anthropics/* (10 repos).
anthropic.com blog (engineering/research/news) is a FROZEN archive as of
2026-07: the site is HTML-only and the jina.ai proxy path was removed.

```bash
uv run scripts/fetcher.py                    # Fetch everything
uv run scripts/fetcher.py --section mcp      # Single section
uv run scripts/fetcher.py --tree             # Show sources
uv run scripts/fetcher.py --discover         # Probe for new sources
```

Sections: `claude-code`, `api`, `platform`, `mcp`, `github`, `support`, `all`

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
content/                       2,900+ files
  en/docs/claude-code/         Claude Code + Agent SDK (141)
  en/api/                      API reference (1,500+)
  en/build-with-claude/        Platform features
  en/agents-and-tools/         Tool use, agent skills
  mcp/                         MCP protocol spec (203)
  blog/                        Engineering, research, news
  github/                      10 repos (718 files)
  support/                     Help articles
scripts/
  fetcher.py                   Multi-source fetcher
sources.json                   Source registry
```

### External Resources

- https://github.com/anthropics/claude-code/issues
- https://code.claude.com/docs/en/overview
- https://platform.claude.com/docs/en/home
- https://modelcontextprotocol.io
