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

- `@./claude-code-docs/settings.md` - Configuration and permissions setup
- `@./claude-code-docs/quickstart.md` - Getting started guide
- `@./claude-code-docs/common-workflows.md` - Common usage patterns
- `@./claude-code-docs/troubleshooting.md` - Problem solving
- `@./release-notes/CHANGELOG.md` - Latest features and fixes

### External Resources for Help

- `@https://github.com/anthropics/claude-code/issues` - Search existing issues
- `@https://docs.anthropic.com/claude-code` - Official documentation


## Commands for fetch and documentation

- `./fetchccdocs.sh` - Fetch latest Claude Code documentation from Anthropic
- `./fetchccdocs.sh --format md --out <directory>` - Fetch docs to specific directory

## Repository Structure

- `claude-code-docs/` - Official Claude Code documentation from docs.anthropic.com
- `anthropic-blog/` - Blog posts about Claude Code from anthropic.com
- `claude-code/` - Contains official CHANGELOG.md from 
