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
- `@./content/en/docs/claude-code/overview.md` - Claude Code overview and capabilities
- `@./content/en/docs/claude-code/quickstart.md` - Getting started guide
- `@./content/en/docs/claude-code/setup.md` - Installation and setup
- `@./content/en/docs/claude-code/settings.md` - Configuration and permissions setup
- `@./content/en/docs/claude-code/common-workflows.md` - Common usage patterns
- `@./content/en/docs/claude-code/memory.md` - Memory management and CLAUDE.md
- `@./content/en/docs/claude-code/interactive-mode.md` - Keyboard shortcuts and interactive features
- `@./content/en/docs/claude-code/slash-commands.md` - Available slash commands
- `@./content/en/docs/claude-code/hooks.md` - Hooks configuration and examples
- `@./content/en/docs/claude-code/hooks-guide.md` - Hooks guide
- `@./content/en/docs/claude-code/troubleshooting.md` - Problem solving
- `@./content/en/docs/claude-code/cli-reference.md` - Command line interface reference
- `@./content/en/docs/claude-code/ide-integrations.md` - IDE integrations
- `@./content/en/docs/claude-code/jetbrains.md` - JetBrains IDE integration
- `@./content/en/docs/claude-code/vs-code.md` - VS Code integration
- `@./content/en/docs/claude-code/mcp.md` - Model Context Protocol
- `@./content/en/docs/claude-code/github-actions.md` - GitHub Actions integration
- `@./content/en/docs/claude-code/gitlab-ci-cd.md` - GitLab CI/CD integration
- `@./content/en/docs/claude-code/sdk.md` - SDK usage
- `@./content/en/docs/claude-code/third-party-integrations.md` - Third-party integrations
- `@./content/en/docs/claude-code/devcontainer.md` - Development containers
- `@./content/en/docs/claude-code/security.md` - Security considerations
- `@./content/en/docs/claude-code/iam.md` - Authentication and permissions
- `@./content/en/docs/claude-code/monitoring-usage.md` - OpenTelemetry monitoring
- `@./content/en/docs/claude-code/analytics.md` - Analytics and usage tracking
- `@./content/en/docs/claude-code/costs.md` - Cost management
- `@./content/en/docs/claude-code/data-usage.md` - Data usage policies
- `@./content/en/docs/claude-code/legal-and-compliance.md` - Legal and compliance
- `@./content/en/docs/claude-code/amazon-bedrock.md` - Amazon Bedrock integration
- `@./content/en/docs/claude-code/google-vertex-ai.md` - Google Vertex AI integration
- `@./content/en/docs/claude-code/corporate-proxy.md` - Corporate proxy setup
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
- `@./content/en/release-notes/claude-code.md` - Release notes from docs.anthropic.com

#### Build with Claude - Prompt Engineering
- `@./content/en/docs/build-with-claude/overview.md` - Building with Claude overview
- `@./content/en/docs/build-with-claude/prompt-engineering/overview.md` - Prompt engineering introduction
- `@./content/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct.md` - Clear and direct prompting
- `@./content/en/docs/build-with-claude/prompt-engineering/chain-of-thought.md` - Chain of thought prompting
- `@./content/en/docs/build-with-claude/prompt-engineering/chain-prompts.md` - Chaining prompts together
- `@./content/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices.md` - Claude 4 best practices
- `@./content/en/docs/build-with-claude/prompt-engineering/multishot-prompting.md` - Multishot prompting examples
- `@./content/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response.md` - Prefilling Claude's response
- `@./content/en/docs/build-with-claude/prompt-engineering/system-prompts.md` - Using system prompts
- `@./content/en/docs/build-with-claude/prompt-engineering/use-xml-tags.md` - Using XML tags in prompts
- `@./content/en/docs/build-with-claude/prompt-engineering/long-context-tips.md` - Long context tips
- `@./content/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips.md` - Extended thinking tips
- `@./content/en/docs/build-with-claude/prompt-engineering/prompt-generator.md` - Prompt generator tool
- `@./content/en/docs/build-with-claude/prompt-engineering/prompt-improver.md` - Prompt improver tool
- `@./content/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables.md` - Templates and variables

#### Build with Claude - Features
- `@./content/en/docs/build-with-claude/batch-processing.md` - Batch processing
- `@./content/en/docs/build-with-claude/citations.md` - Working with citations
- `@./content/en/docs/build-with-claude/context-windows.md` - Understanding context windows
- `@./content/en/docs/build-with-claude/embeddings.md` - Using embeddings
- `@./content/en/docs/build-with-claude/extended-thinking.md` - Extended thinking capability
- `@./content/en/docs/build-with-claude/files.md` - File handling
- `@./content/en/docs/build-with-claude/multilingual-support.md` - Multilingual capabilities
- `@./content/en/docs/build-with-claude/pdf-support.md` - PDF support
- `@./content/en/docs/build-with-claude/prompt-caching.md` - Prompt caching
- `@./content/en/docs/build-with-claude/search-results.md` - Search results handling
- `@./content/en/docs/build-with-claude/streaming.md` - Streaming responses
- `@./content/en/docs/build-with-claude/token-counting.md` - Token counting
- `@./content/en/docs/build-with-claude/vision.md` - Vision capabilities

#### Agents and Tools - Agent Skills
- `@./content/en/docs/agents-and-tools/agent-skills/overview.md` - Agent skills overview and concepts
- `@./content/en/docs/agents-and-tools/agent-skills/quickstart.md` - Getting started with agent skills
- `@./content/en/docs/agents-and-tools/agent-skills/best-practices.md` - Agent skills authoring best practices

#### Agents and Tools - Tool Use
- `@./content/en/docs/agents-and-tools/tool-use/overview.md` - Tool use overview
- `@./content/en/docs/agents-and-tools/tool-use/implement-tool-use.md` - Implementing tool use
- `@./content/en/docs/agents-and-tools/tool-use/bash-tool.md` - Bash tool
- `@./content/en/docs/agents-and-tools/tool-use/code-execution-tool.md` - Code execution tool
- `@./content/en/docs/agents-and-tools/tool-use/computer-use-tool.md` - Computer use tool
- `@./content/en/docs/agents-and-tools/tool-use/text-editor-tool.md` - Text editor tool
- `@./content/en/docs/agents-and-tools/tool-use/memory-tool.md` - Memory tool
- `@./content/en/docs/agents-and-tools/tool-use/web-fetch-tool.md` - Web fetch tool
- `@./content/en/docs/agents-and-tools/tool-use/web-search-tool.md` - Web search tool
- `@./content/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming.md` - Fine-grained tool streaming
- `@./content/en/docs/agents-and-tools/tool-use/token-efficient-tool-use.md` - Token-efficient tool use

#### Agents and Tools - Other
- `@./content/en/docs/agents-and-tools/claude-for-sheets.md` - Claude for Google Sheets
- `@./content/en/docs/agents-and-tools/mcp-connector.md` - MCP connector
- `@./content/en/docs/agents-and-tools/remote-mcp-servers.md` - Remote MCP servers

#### Agent SDK
- `@./content/en/api/agent-sdk/sdk-overview.md` - Agent SDK overview
- `@./content/en/api/agent-sdk/sdk-python.md` - Python SDK
- `@./content/en/api/agent-sdk/sdk-typescript.md` - TypeScript SDK
- `@./content/en/api/agent-sdk/custom-tools.md` - Custom tools
- `@./content/en/api/agent-sdk/sdk-mcp.md` - MCP integration
- `@./content/en/api/agent-sdk/sdk-permissions.md` - Permissions
- `@./content/en/api/agent-sdk/sdk-sessions.md` - Sessions
- `@./content/en/api/agent-sdk/sdk-slash-commands.md` - Slash commands
- `@./content/en/api/agent-sdk/streaming-vs-single-mode.md` - Streaming vs single mode
- `@./content/en/api/agent-sdk/subagents.md` - Subagents
- `@./content/en/api/agent-sdk/todo-tracking.md` - Todo tracking
- `@./content/en/api/agent-sdk/sdk-cost-tracking.md` - Cost tracking
- `@./content/en/api/agent-sdk/sdk-headless.md` - Headless mode
- `@./content/en/api/agent-sdk/modifying-system-prompts.md` - Modifying system prompts

#### API Documentation - Client SDKs & Integrations
- `@./content/en/api/client-sdks.md` - Client SDKs
- `@./content/en/api/openai-sdk.md` - OpenAI SDK compatibility
- `@./content/en/api/claude-code-analytics-api.md` - Analytics API

#### API Documentation - Skills API
- `@./content/en/api/api/skills/overview.md` - Skills API overview
- `@./content/en/api/api/skills/create-skill.md` - Create skill
- `@./content/en/api/api/skills/list-skills.md` - List skills
- `@./content/en/api/api/skills/get-skill.md` - Get skill
- `@./content/en/api/api/skills/delete-skill.md` - Delete skill
- `@./content/en/api/api/skills/create-skill-version.md` - Create skill version
- `@./content/en/api/api/skills/list-skill-versions.md` - List skill versions
- `@./content/en/api/api/skills/get-skill-version.md` - Get skill version
- `@./content/en/api/api/skills/delete-skill-version.md` - Delete skill version

#### API Documentation - Admin API
- `@./content/en/api/admin-api/claude-code/get-claude-code-usage-report.md` - Claude Code usage report
- `@./content/en/api/api/admin-api/organization/get-me.md` - Get organization
- `@./content/en/api/api/admin-api/apikeys/*` - API key management
- `@./content/en/api/api/admin-api/users/*` - User management
- `@./content/en/api/api/admin-api/workspaces/*` - Workspace management
- `@./content/en/api/api/admin-api/workspace_members/*` - Workspace member management
- `@./content/en/api/api/admin-api/invites/*` - Invite management
- `@./content/en/api/api/admin-api/usage-cost/*` - Usage and cost reports

#### API Reference - Core API
- `@./content/en/api/api/messages.md` - Messages API
- `@./content/en/api/api/messages-examples.md` - Messages examples
- `@./content/en/api/api/messages-count-tokens.md` - Token counting
- `@./content/en/api/api/models.md` - Models overview
- `@./content/en/api/api/models-list.md` - List models
- `@./content/en/api/api/files-*.md` - Files API
- `@./content/en/api/api/*-message-batch*.md` - Message batches API
- `@./content/en/api/api/errors.md` - Error handling
- `@./content/en/api/api/rate-limits.md` - Rate limits
- `@./content/en/api/api/versioning.md` - API versioning
- `@./content/en/api/api/supported-regions.md` - Supported regions
- `@./content/en/api/api/service-tiers.md` - Service tiers

#### About Claude
- `@./content/en/docs/about-claude/glossary.md` - Claude glossary
- `@./content/en/docs/about-claude/model-deprecations.md` - Model deprecation policy
- `@./content/en/docs/about-claude/pricing.md` - Pricing information

#### Test and Evaluate
- `@./content/en/docs/test-and-evaluate/define-success.md` - Defining success criteria
- `@./content/en/docs/test-and-evaluate/develop-tests.md` - Developing test cases
- `@./content/en/docs/test-and-evaluate/eval-tool.md` - Evaluation tools

#### Get Started
- `@./content/en/docs/get-started/intro.md` - Introduction to Claude
- `@./content/en/docs/get-started/overview.md` - Claude overview
- `@./content/en/docs/get-started/mcp.md` - Model Context Protocol overview

#### Release Notes
- `@./content/en/release-notes/claude-code.md` - Claude Code release notes
- `@./content/en/release-notes/api.md` - API release notes
- `@./content/en/release-notes/claude-apps.md` - Claude Apps release notes
- `@./content/en/release-notes/system-prompts.md` - System prompts release notes
- `@./content/en/release-notes/overview.md` - Release notes overview
- `@./content/en/release-notes/CHANGELOG.md` - GitHub CHANGELOG

#### Resources and Prompt Library
- `@./content/en/resources/overview.md` - Resources overview
- `@./content/en/resources/prompt-library/*` - 65+ curated prompts for various use cases

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
