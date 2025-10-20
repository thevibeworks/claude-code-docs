# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Maintenance: Adding New Doc Sections

When Anthropic adds new doc sections (like agents-and-tools), update these files:

**1. `scripts/fetchccdocs.sh`** - 7 locations:
- **Directory creation**: `mkdir -p "$OUTPUT_DIR/new-section"`
- **process_sitemap() function**: Add elif block for path processing (check if docs.claude.com vs docs.anthropic.com)
- **Process sitemaps section**: `NEW_RESULT=$(process_sitemap "$SITEMAP_URL" "name" "URL_PATTERN" "direct" "")`
- **Parse results section**: `read NEW_SUCCESS NEW_FAIL <<<"${NEW_RESULT:-0 0}"`
- **Ensure numeric values section**: `NEW_SUCCESS=${NEW_SUCCESS:-0}` and `NEW_FAIL=${NEW_FAIL:-0}`
- **Calculate totals section**: Update SUCCESS/FAIL to include NEW_SUCCESS/NEW_FAIL
- **Metadata generation** (both if/else blocks): Add section to sources{}, increment total_sources

**2. `CLAUDE.md`** (this file):
- Add doc references in "Documentation Resources" section
- Update "Repository Structure" to list new directory

**3. Find URLs**: `curl -sSL "https://docs.anthropic.com/sitemap.xml" | grep -i "pattern" | grep "/en/" | sort -u`

**Note**: agents-and-tools uses docs.claude.com (not docs.anthropic.com). Check domain carefully.

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
- `@./content/claude-code-docs/troubleshooting.md` - Problem solving
- `@./content/claude-code-docs/cli-reference.md` - Command line interface reference
- `@./content/claude-code-docs/ide-integrations.md` - IDE integrations
- `@./content/claude-code-docs/mcp.md` - Model Context Protocol
- `@./content/claude-code-docs/github-actions.md` - GitHub Actions integration
- `@./content/claude-code-docs/sdk.md` - SDK usage
- `@./content/claude-code-docs/third-party-integrations.md` - Third-party integrations
- `@./content/claude-code-docs/devcontainer.md` - Development containers
- `@./content/claude-code-docs/security.md` - Security considerations
- `@./content/claude-code-docs/iam.md` - Authentication and permissions
- `@./content/claude-code-docs/monitoring-usage.md` - OpenTelemetry monitoring
- `@./content/claude-code-docs/costs.md` - Cost management
- `@./content/claude-code-docs/data-usage.md` - Data usage policies
- `@./content/claude-code-docs/legal-and-compliance.md` - Legal and compliance
- `@./content/claude-code-docs/amazon-bedrock.md` - Amazon Bedrock integration
- `@./content/claude-code-docs/google-vertex-ai.md` - Google Vertex AI integration
- `@./content/claude-code-docs/corporate-proxy.md` - Corporate proxy setup
- `@./content/claude-code-docs/llm-gateway.md` - LLM gateway configuration
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

## Repository Structure

- `content/` - All fetched Claude Code documentation and content
  - `claude-code-docs/` - Official documentation from docs.anthropic.com
  - `anthropic-blog/` - Blog posts about Claude Code from anthropic.com
  - `build-with-claude/` - Build with Claude documentation
  - `agents-and-tools/` - Agents and tools documentation
  - `release-notes/` - Claude Code release notes (GitHub CHANGELOG.md)
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

- `./scripts/fetchccdocs.sh` - Fetch latest Claude Code documentation from Anthropic
- `./scripts/fetchccdocs.sh --format md --out <directory>` - Fetch docs to specific directory
