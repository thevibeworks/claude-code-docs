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

## Repository Structure

- `content/` - All fetched Claude Code documentation and content
  - `claude-code-docs/` - Official documentation from docs.anthropic.com
  - `anthropic-blog/` - Blog posts about Claude Code from anthropic.com
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
