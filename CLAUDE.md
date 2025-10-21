# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Maintenance: Adding New Doc Sections

When Anthropic adds new doc sections (like agents-and-tools), update these files:

**1. `scripts/fetchccdocs.py`** - Update URL pattern matching:
- **`_matches_pattern()` method**: Add new elif block for the section
- **`patterns` dict in `extract_urls()`**: Add regex pattern for the new section
- **`get_output_path()` method**: Add path mapping logic for the section
- **Help text**: Add section name to "Available sections" list

**2. `CLAUDE.md`** (this file):
- Add doc references in "Documentation Resources" section
- Update "Repository Structure" to list new directory

**3. Find URLs**: `curl -sSL "https://docs.claude.com/sitemap.xml" | grep -i "pattern" | grep "/en/" | sort -u`

**Note**: All docs now on docs.claude.com (docs.anthropic.com redirects there). Uses Python 3.14 free-threaded for blazing fast fetches (~5 sec for 282 docs).

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

#### Claude Code Documentation
- `@./content/claude-code-docs/overview.md` - Claude Code overview and capabilities
- `@./content/claude-code-docs/quickstart.md` - Getting started guide
- `@./content/claude-code-docs/setup.md` - Installation and setup
- `@./content/claude-code-docs/settings.md` - Configuration and permissions setup
- `@./content/claude-code-docs/common-workflows.md` - Common usage patterns
- `@./content/claude-code-docs/memory.md` - Memory management and CLAUDE.md
- `@./content/claude-code-docs/interactive-mode.md` - Keyboard shortcuts and interactive features
- `@./content/claude-code-docs/slash-commands.md` - Available slash commands
- `@./content/claude-code-docs/hooks.md` - Hooks configuration and examples
- `@./content/claude-code-docs/hooks-guide.md` - Hooks guide
- `@./content/claude-code-docs/troubleshooting.md` - Problem solving
- `@./content/claude-code-docs/cli-reference.md` - Command line interface reference
- `@./content/claude-code-docs/ide-integrations.md` - IDE integrations
- `@./content/claude-code-docs/jetbrains.md` - JetBrains IDE integration
- `@./content/claude-code-docs/vs-code.md` - VS Code integration
- `@./content/claude-code-docs/mcp.md` - Model Context Protocol
- `@./content/claude-code-docs/github-actions.md` - GitHub Actions integration
- `@./content/claude-code-docs/gitlab-ci-cd.md` - GitLab CI/CD integration
- `@./content/claude-code-docs/sdk.md` - SDK usage
- `@./content/claude-code-docs/third-party-integrations.md` - Third-party integrations
- `@./content/claude-code-docs/devcontainer.md` - Development containers
- `@./content/claude-code-docs/security.md` - Security considerations
- `@./content/claude-code-docs/iam.md` - Authentication and permissions
- `@./content/claude-code-docs/monitoring-usage.md` - OpenTelemetry monitoring
- `@./content/claude-code-docs/analytics.md` - Analytics and usage tracking
- `@./content/claude-code-docs/costs.md` - Cost management
- `@./content/claude-code-docs/data-usage.md` - Data usage policies
- `@./content/claude-code-docs/legal-and-compliance.md` - Legal and compliance
- `@./content/claude-code-docs/amazon-bedrock.md` - Amazon Bedrock integration
- `@./content/claude-code-docs/google-vertex-ai.md` - Google Vertex AI integration
- `@./content/claude-code-docs/corporate-proxy.md` - Corporate proxy setup
- `@./content/claude-code-docs/llm-gateway.md` - LLM gateway configuration
- `@./content/claude-code-docs/model-config.md` - Model configuration
- `@./content/claude-code-docs/network-config.md` - Network configuration
- `@./content/claude-code-docs/terminal-config.md` - Terminal configuration
- `@./content/claude-code-docs/output-styles.md` - Output styling and formatting
- `@./content/claude-code-docs/statusline.md` - Status line configuration
- `@./content/claude-code-docs/checkpointing.md` - Session checkpointing
- `@./content/claude-code-docs/headless.md` - Headless mode
- `@./content/claude-code-docs/plugins.md` - Plugin system
- `@./content/claude-code-docs/plugins-reference.md` - Plugin reference
- `@./content/claude-code-docs/plugin-marketplaces.md` - Plugin marketplaces
- `@./content/claude-code-docs/skills.md` - Claude Skills
- `@./content/claude-code-docs/sub-agents.md` - Sub-agents
- `@./content/release-notes/CHANGELOG.md` - Claude Code GitHub CHANGELOG
- `@./content/claude-code-docs/release-notes/claude-code.md` - Release notes from docs.anthropic.com

#### Build with Claude - Prompt Engineering
- `@./content/build-with-claude/overview.md` - Building with Claude overview
- `@./content/build-with-claude/prompt-engineering/overview.md` - Prompt engineering introduction
- `@./content/build-with-claude/prompt-engineering/be-clear-and-direct.md` - Clear and direct prompting
- `@./content/build-with-claude/prompt-engineering/chain-of-thought.md` - Chain of thought prompting
- `@./content/build-with-claude/prompt-engineering/chain-prompts.md` - Chaining prompts together
- `@./content/build-with-claude/prompt-engineering/claude-4-best-practices.md` - Claude 4 best practices
- `@./content/build-with-claude/prompt-engineering/multishot-prompting.md` - Multishot prompting examples
- `@./content/build-with-claude/prompt-engineering/prefill-claudes-response.md` - Prefilling Claude's response
- `@./content/build-with-claude/prompt-engineering/system-prompts.md` - Using system prompts
- `@./content/build-with-claude/prompt-engineering/use-xml-tags.md` - Using XML tags in prompts
- `@./content/build-with-claude/prompt-engineering/long-context-tips.md` - Long context tips
- `@./content/build-with-claude/prompt-engineering/extended-thinking-tips.md` - Extended thinking tips
- `@./content/build-with-claude/prompt-engineering/prompt-generator.md` - Prompt generator tool
- `@./content/build-with-claude/prompt-engineering/prompt-improver.md` - Prompt improver tool
- `@./content/build-with-claude/prompt-engineering/prompt-templates-and-variables.md` - Templates and variables

#### Build with Claude - Features
- `@./content/build-with-claude/batch-processing.md` - Batch processing
- `@./content/build-with-claude/citations.md` - Working with citations
- `@./content/build-with-claude/context-windows.md` - Understanding context windows
- `@./content/build-with-claude/embeddings.md` - Using embeddings
- `@./content/build-with-claude/extended-thinking.md` - Extended thinking capability
- `@./content/build-with-claude/files.md` - File handling
- `@./content/build-with-claude/multilingual-support.md` - Multilingual capabilities
- `@./content/build-with-claude/pdf-support.md` - PDF support
- `@./content/build-with-claude/prompt-caching.md` - Prompt caching
- `@./content/build-with-claude/search-results.md` - Search results handling
- `@./content/build-with-claude/streaming.md` - Streaming responses
- `@./content/build-with-claude/token-counting.md` - Token counting
- `@./content/build-with-claude/vision.md` - Vision capabilities

#### Agents and Tools - Agent Skills
- `@./content/agents-and-tools/agent-skills/overview.md` - Agent skills overview and concepts
- `@./content/agents-and-tools/agent-skills/quickstart.md` - Getting started with agent skills
- `@./content/agents-and-tools/agent-skills/best-practices.md` - Agent skills authoring best practices

#### Agents and Tools - Tool Use
- `@./content/agents-and-tools/tool-use/overview.md` - Tool use overview
- `@./content/agents-and-tools/tool-use/implement-tool-use.md` - Implementing tool use
- `@./content/agents-and-tools/tool-use/bash-tool.md` - Bash tool
- `@./content/agents-and-tools/tool-use/code-execution-tool.md` - Code execution tool
- `@./content/agents-and-tools/tool-use/computer-use-tool.md` - Computer use tool
- `@./content/agents-and-tools/tool-use/text-editor-tool.md` - Text editor tool
- `@./content/agents-and-tools/tool-use/memory-tool.md` - Memory tool
- `@./content/agents-and-tools/tool-use/web-fetch-tool.md` - Web fetch tool
- `@./content/agents-and-tools/tool-use/web-search-tool.md` - Web search tool
- `@./content/agents-and-tools/tool-use/fine-grained-tool-streaming.md` - Fine-grained tool streaming
- `@./content/agents-and-tools/tool-use/token-efficient-tool-use.md` - Token-efficient tool use

#### Agents and Tools - Other
- `@./content/agents-and-tools/claude-for-sheets.md` - Claude for Google Sheets
- `@./content/agents-and-tools/mcp-connector.md` - MCP connector
- `@./content/agents-and-tools/remote-mcp-servers.md` - Remote MCP servers

#### Agent SDK
- `@./content/claude-code-docs/sdk/sdk-overview.md` - Agent SDK overview
- `@./content/claude-code-docs/sdk/sdk-python.md` - Python SDK
- `@./content/claude-code-docs/sdk/sdk-typescript.md` - TypeScript SDK
- `@./content/claude-code-docs/sdk/custom-tools.md` - Custom tools
- `@./content/claude-code-docs/sdk/sdk-mcp.md` - MCP integration
- `@./content/claude-code-docs/sdk/sdk-permissions.md` - Permissions
- `@./content/claude-code-docs/sdk/sdk-sessions.md` - Sessions
- `@./content/claude-code-docs/sdk/sdk-slash-commands.md` - Slash commands
- `@./content/claude-code-docs/sdk/streaming-vs-single-mode.md` - Streaming vs single mode
- `@./content/claude-code-docs/sdk/subagents.md` - Subagents
- `@./content/claude-code-docs/sdk/todo-tracking.md` - Todo tracking
- `@./content/claude-code-docs/sdk/sdk-cost-tracking.md` - Cost tracking
- `@./content/claude-code-docs/sdk/sdk-headless.md` - Headless mode
- `@./content/claude-code-docs/sdk/modifying-system-prompts.md` - Modifying system prompts

#### API Documentation - Client SDKs & Integrations
- `@./content/claude-code-docs/api/client-sdks.md` - Client SDKs
- `@./content/claude-code-docs/api/openai-sdk.md` - OpenAI SDK compatibility
- `@./content/claude-code-docs/api/claude-code-analytics-api.md` - Analytics API

#### API Documentation - Skills API
- `@./content/claude-code-docs/api/api/skills/overview.md` - Skills API overview
- `@./content/claude-code-docs/api/api/skills/create-skill.md` - Create skill
- `@./content/claude-code-docs/api/api/skills/list-skills.md` - List skills
- `@./content/claude-code-docs/api/api/skills/get-skill.md` - Get skill
- `@./content/claude-code-docs/api/api/skills/delete-skill.md` - Delete skill
- `@./content/claude-code-docs/api/api/skills/create-skill-version.md` - Create skill version
- `@./content/claude-code-docs/api/api/skills/list-skill-versions.md` - List skill versions
- `@./content/claude-code-docs/api/api/skills/get-skill-version.md` - Get skill version
- `@./content/claude-code-docs/api/api/skills/delete-skill-version.md` - Delete skill version

#### API Documentation - Admin API
- `@./content/claude-code-docs/api/admin-api/claude-code/get-claude-code-usage-report.md` - Claude Code usage report
- `@./content/claude-code-docs/api/api/admin-api/organization/get-me.md` - Get organization
- `@./content/claude-code-docs/api/api/admin-api/apikeys/*` - API key management
- `@./content/claude-code-docs/api/api/admin-api/users/*` - User management
- `@./content/claude-code-docs/api/api/admin-api/workspaces/*` - Workspace management
- `@./content/claude-code-docs/api/api/admin-api/workspace_members/*` - Workspace member management
- `@./content/claude-code-docs/api/api/admin-api/invites/*` - Invite management
- `@./content/claude-code-docs/api/api/admin-api/usage-cost/*` - Usage and cost reports

#### API Reference - Core API
- `@./content/claude-code-docs/api/api/messages.md` - Messages API
- `@./content/claude-code-docs/api/api/messages-examples.md` - Messages examples
- `@./content/claude-code-docs/api/api/messages-count-tokens.md` - Token counting
- `@./content/claude-code-docs/api/api/models.md` - Models overview
- `@./content/claude-code-docs/api/api/models-list.md` - List models
- `@./content/claude-code-docs/api/api/files-*.md` - Files API
- `@./content/claude-code-docs/api/api/*-message-batch*.md` - Message batches API
- `@./content/claude-code-docs/api/api/errors.md` - Error handling
- `@./content/claude-code-docs/api/api/rate-limits.md` - Rate limits
- `@./content/claude-code-docs/api/api/versioning.md` - API versioning
- `@./content/claude-code-docs/api/api/supported-regions.md` - Supported regions
- `@./content/claude-code-docs/api/api/service-tiers.md` - Service tiers

#### About Claude
- `@./content/about-claude/glossary.md` - Claude glossary
- `@./content/about-claude/model-deprecations.md` - Model deprecation policy
- `@./content/about-claude/pricing.md` - Pricing information

#### Test and Evaluate
- `@./content/test-and-evaluate/define-success.md` - Defining success criteria
- `@./content/test-and-evaluate/develop-tests.md` - Developing test cases
- `@./content/test-and-evaluate/eval-tool.md` - Evaluation tools

#### Get Started
- `@./content/get-started/intro.md` - Introduction to Claude
- `@./content/get-started/overview.md` - Claude overview
- `@./content/get-started/mcp.md` - Model Context Protocol overview

#### Release Notes
- `@./content/release-notes/claude-code.md` - Claude Code release notes
- `@./content/release-notes/api.md` - API release notes
- `@./content/release-notes/claude-apps.md` - Claude Apps release notes
- `@./content/release-notes/system-prompts.md` - System prompts release notes
- `@./content/release-notes/overview.md` - Release notes overview
- `@./content/release-notes/CHANGELOG.md` - GitHub CHANGELOG

#### Resources and Prompt Library
- `@./content/resources/overview.md` - Resources overview
- `@./content/resources/prompt-library/*` - 65+ curated prompts for various use cases

## Repository Structure

- `content/` - All fetched Claude Code documentation and content
  - `claude-code-docs/` - Official documentation from docs.claude.com
    - `sdk/` - Agent SDK documentation (14 docs)
    - `api/` - API documentation (71 docs: Skills API, Admin API, API Reference)
  - `build-with-claude/` - Build with Claude documentation (29 docs)
  - `agents-and-tools/` - Agents and tools documentation (17 docs)
  - `about-claude/` - About Claude documentation (12 docs)
  - `test-and-evaluate/` - Testing and evaluation guides (10 docs)
  - `get-started/` - Getting started guides (3 docs)
  - `resources/` - Resources and prompt library (66 docs)
  - `release-notes/` - Release notes (6 docs: API, Claude Apps, Claude Code, etc.)
  - `anthropic-blog/` - Blog posts about Claude Code (10 articles)
  - `env-vars/` - Environment variable documentation
  - `claude-code-manifest.json` - NPM package manifest
  - `.metadata.json` - Fetch metadata
- `intro-post.md` - Introduction blog post
- `screenshot.png` - Repository screenshot
- `scripts/` - Repository utilities and automation
  - `fetchccdocs.sh` - Fetch latest Claude Code documentation from Anthropic
  - `check-changes.sh` - Check if meaningful changes in documentation
- `.github/workflows/` - GitHub Actions workflows
- `docs/` - Project documentation

### External Resources for Help

- `@https://github.com/anthropics/claude-code/issues` - Search existing issues
- `@https://docs.anthropic.com/claude-code` - Official documentation

## Commands for fetch and documentation

- `uv run scripts/fetchccdocs.py` - Fetch latest Claude Code documentation (Python 3.14 free-threaded, ~5 sec)
- `uv run scripts/fetchccdocs.py --section agent-sdk` - Fetch specific section only
- `uv run scripts/fetchccdocs.py --incremental` - Skip existing files (use for quick updates)
- `uv run scripts/fetchccdocs.py --help` - Show all available options

Legacy bash script (slower, ~15-20 min):
- `./scripts/fetchccdocs.sh` - Fetch using bash (not recommended)
