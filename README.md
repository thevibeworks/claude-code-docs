# Start Vibe Coding with Claude Code

> 🤖 **Claude Code is Auto Managing this Repo**: This repository is automatically updated and managed by Claude via GitHub Actions. See `.github/workflows/` for automation details.

This repository contains Claude Code documentation and resources for **learning about [Claude Code](https://claude.ai/code)**

![Claude Code in Action](https://raw.githubusercontent.com/lroolle/claude-code-docs/main/screenshot.png)


## Quick Start for How to Use Claude Code

### Prerequisites

First, install Claude Code CLI:

```bash
npm install -g @anthropic-ai/claude-code
```

### Getting Started


> **GitHub Repository**: https://github.com/lroolle/claude-code-docs

1. **Clone this repository**:
   ```bash
   git clone https://github.com/lroolle/claude-code-docs
   cd claude-code-docs
   ```


2. **Start using Claude Code with the documentation as context**:
   ```bash
   claude "show me claude code workflow"
   claude "what's the best practice for using claude code? what's ultrathink?"
   claude "what are the main features of claude code?"
   claude "how do I use claude code with github?"
   claude "explain claude code memory management"
   claude "how do I save money when using claude code?"
   ```

## Practical Usage Examples

Once you have this documentation repository, here's how to use it with Claude Code:

### Learning Claude Code Basics
```bash
claude "Based on the documentation in this repo, what is Claude Code?"
claude "How do I install and set up Claude Code for the first time?"
claude "What are the key features I should know about?"
claude "Show me the most important commands to get started"
```

### Understanding Advanced Features
```bash
claude "What is extended thinking and how do I use it?"
claude "How does Claude Code integrate with GitHub Actions?"
claude "What are MCP integrations and when should I use them?"
```

### Getting Help with Workflows
```bash
claude "Based on these docs, what's the recommended workflow for team collaboration?"
claude "How should I structure my prompts for better results?"
claude "What are common mistakes to avoid when using Claude Code?"
claude "Show me examples of effective Claude Code usage patterns"
```

### Troubleshooting with Documentation
```bash
claude "I'm having authentication issues - help me debug using the troubleshooting docs"
claude "Claude Code seems slow - what optimization tips are in the documentation?"
claude "How do I configure Claude Code according to the setup guide?"
```

### Configuring Claude Code Settings
```bash
claude "Based on the settings.md file, show me how to set up project-level permissions"
claude "How do I create a settings.json file to allow npm commands but deny curl?"
claude "What's the difference between .claude/settings.json and .claude/settings.local.json?"
claude "Help me configure environment variables for my team using the settings docs"

# Example: Set up permissions for a web development project
claude "Using the settings documentation, create a settings.json that allows npm scripts, git commands, but blocks network requests"
```

## 🚀 MCP Server Integration

This repository now includes a **Model Context Protocol (MCP) server** that provides structured access to all Claude Code documentation through Claude Code itself!

### Quick Setup

1. **Install the MCP server:**
   ```bash
   ./install-mcp-server.sh
   ```

2. **Start using it with Claude Code:**
   ```bash
   claude "Search the documentation for MCP integration"
   claude "I'm new to Claude Code, give me a beginner learning path"
   claude "Help me troubleshoot authentication issues"
   ```

### MCP Server Features

- 🔍 **Smart Documentation Search** - Find answers across all Claude Code docs
- 📚 **Personalized Learning Paths** - Get step-by-step guidance based on your skill level
- 🆘 **Contextual Help** - Get specific help for your current situation or errors  
- 📈 **Progress Tracking** - Track your learning journey with badges and achievements
- 🧠 **Concept Explanations** - Deep dive into Claude Code concepts with examples

[📖 Read the full MCP Server documentation](MCP_SERVER_README.md)

## Disclaimer

This is an unofficial mirror for **educational purposes**. For official documentation, visit https://docs.anthropic.com/claude-code. For commercial use, please consult Anthropic's [commercial terms](https://www.anthropic.com/legal/commercial-terms).

- **Documentation content** is sourced from https://docs.anthropic.com and https://www.anthropic.com
- **Repository code** (CHANGELOG.md, commits) is sourced from https://github.com/anthropics/claude-code
- **Redistribution** should comply with Anthropic's [commercial terms](https://www.anthropic.com/legal/commercial-terms)
- **Commercial use** of this content may require permission from Anthropic
