# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

- `@./claude-code-docs/overview.md` - Claude Code overview and capabilities
- `@./claude-code-docs/quickstart.md` - Getting started guide
- `@./claude-code-docs/setup.md` - Installation and setup
- `@./claude-code-docs/settings.md` - Configuration and permissions setup
- `@./claude-code-docs/common-workflows.md` - Common usage patterns
- `@./claude-code-docs/memory.md` - Memory management and CLAUDE.md
- `@./claude-code-docs/interactive-mode.md` - Keyboard shortcuts and interactive features
- `@./claude-code-docs/slash-commands.md` - Available slash commands
- `@./claude-code-docs/hooks.md` - Hooks configuration and examples
- `@./claude-code-docs/troubleshooting.md` - Problem solving
- `@./claude-code-docs/cli-reference.md` - Command line interface reference
- `@./claude-code-docs/ide-integrations.md` - IDE integrations
- `@./claude-code-docs/mcp.md` - Model Context Protocol
- `@./claude-code-docs/github-actions.md` - GitHub Actions integration
- `@./claude-code-docs/sdk.md` - SDK usage
- `@./claude-code-docs/third-party-integrations.md` - Third-party integrations
- `@./claude-code-docs/devcontainer.md` - Development containers
- `@./claude-code-docs/security.md` - Security considerations
- `@./claude-code-docs/iam.md` - Authentication and permissions
- `@./claude-code-docs/monitoring-usage.md` - OpenTelemetry monitoring
- `@./claude-code-docs/costs.md` - Cost management
- `@./claude-code-docs/data-usage.md` - Data usage policies
- `@./claude-code-docs/legal-and-compliance.md` - Legal and compliance
- `@./claude-code-docs/amazon-bedrock.md` - Amazon Bedrock integration
- `@./claude-code-docs/google-vertex-ai.md` - Google Vertex AI integration
- `@./claude-code-docs/corporate-proxy.md` - Corporate proxy setup
- `@./claude-code-docs/llm-gateway.md` - LLM gateway configuration
- `@./release-notes/CHANGELOG.md` - Latest features and fixes

## Repository Structure

- `claude-code-docs/` - Official Claude Code documentation from docs.anthropic.com
- `anthropic-blog/` - Blog posts about Claude Code from anthropic.com
- `claude-code/` - Contains official CHANGELOG.md from GitHub releases


### External Resources for Help

- `@https://github.com/anthropics/claude-code/issues` - Search existing issues
- `@https://docs.anthropic.com/claude-code` - Official documentation


## Commands for fetch and documentation

- `./fetchccdocs.sh` - Fetch latest Claude Code documentation from Anthropic
- `./fetchccdocs.sh --format md --out <directory>` - Fetch docs to specific directory
