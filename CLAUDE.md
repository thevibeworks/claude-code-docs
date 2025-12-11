# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Maintenance: Documentation Sources

Documentation is now split across two domains (Dec 2025):
- **platform.claude.com** - API docs, Agent SDK, prompt engineering (sitemap.xml)
- **code.claude.com** - Claude Code docs (llms.txt)

**Fetcher script**: `scripts/fetcher.py`
- Uses `platform.claude.com/sitemap.xml` for API/platform docs
- Uses `code.claude.com/docs/llms.txt` for Claude Code docs
- Supports `--section claude-code|api|blog` filtering

**When adding new sections**:
1. Update `get_output_path()` method for path mapping
2. Update `CLAUDE.md` doc references
3. Check for new URLs: `uv run scripts/fetcher.py --tree`

**Note**: Python 3.14 free-threaded, ~40 sec for 575+ docs.

## Repository Purpose

Acting as the Claude Code tutor, teach "vibe coders" / "vibe learners" to learn how to get started with claude-code according to the claude-docs and related resources.

## Teaching Approach

Focus on practical examples using the repository's documentation to help beginners understand:
1. How to install and configure Claude Code
2. Settings and permissions management
3. Common workflows and best practices
4. Troubleshooting common issues

Always reference specific documentation files in this repository when providing guidance.


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
Build with Claude, Agent SDK, Tool Use docs now at `content/en/` (mirroring platform.claude.com/docs/en/).
Use `uv run scripts/fetcher.py --tree` to see current structure.

Key sections: `build-with-claude/`, `agent-sdk/`, `agents-and-tools/`, `api/`, `resources/`

#### Other Platform Sections
- `content/en/api/` - API reference (359 docs)
- `content/en/about-claude/` - Models, pricing, glossary
- `content/en/test-and-evaluate/` - Testing and evaluation
- `content/en/release-notes/` - Release notes
- `content/en/resources/prompt-library/` - 65+ curated prompts

## Repository Structure

```
content/
├── en/docs/claude-code/   # Claude Code docs (47 from code.claude.com)
├── en/build-with-claude/  # Prompt engineering, features (from platform.claude.com)
├── en/agent-sdk/          # Agent SDK docs
├── en/agents-and-tools/   # Tool use, agent skills
├── en/api/                # API reference (359 docs)
├── en/resources/          # Prompt library
├── blog/                  # Blog posts
├── CHANGELOG.md           # GitHub CHANGELOG
└── claude-code-manifest.json
scripts/
├── fetcher.py             # Main fetch script
└── README.md
```

### External Resources

- https://github.com/anthropics/claude-code/issues
- https://code.claude.com/docs/en/overview
- https://platform.claude.com/docs/en/home

## Commands

```bash
uv run scripts/fetcher.py                      # Fetch all (575+ docs)
uv run scripts/fetcher.py --section claude-code # Claude Code only (47 docs)
uv run scripts/fetcher.py --section api         # API docs only
uv run scripts/fetcher.py --tree                # Show structure
uv run scripts/fetcher.py --incremental         # Skip existing
```
