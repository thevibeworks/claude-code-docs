# Claude Code Documentation MCP Server

A minimal, user-friendly MCP server that automatically installs and provides structured access to Claude Code documentation with interactive prompts.

## ✨ Key Features

### 🚀 Auto-Installation
- Automatically clones documentation to `~/.claude/claude-code-docs/`
- No manual setup required - just install and use
- Falls back to `$(pwd)/.claude/claude-code-docs/` if needed

### 🔍 One Search Tool
- **search_docs** - Fast search through all Claude Code documentation
- Smart relevance ranking with context
- Integrated prompt suggestions

### 🎯 Interactive Prompts
- **claude-code-setup** - Personalized setup guidance
- **claude-code-learn** - Custom learning paths
- **claude-code-troubleshoot** - Problem-solving assistance  
- **claude-code-workflow** - Best practices for your use case

### 📚 MCP Resources
- Direct access to all documentation files
- Release notes and changelogs
- Structured metadata

## 🚀 Quick Start

### Installation

```bash
cd mcp/
bun install
bun run build
```

### Claude Desktop Configuration

Add to your Claude Desktop config:

```json
{
  "mcpServers": {
    "claude-code-docs": {
      "command": "node",
      "args": ["/absolute/path/to/claude-code-docs/mcp/dist/main.js"]
    }
  }
}
```

### Claude Code Configuration

Add to your Claude Code config:

```json
{
  "mcpServers": {
    "claude-code-docs": {
      "command": "node", 
      "args": ["/absolute/path/to/claude-code-docs/mcp/dist/main.js"]
    }
  }
}
```

## 📖 Usage

### Search Tool

```
search_docs("installation setup")
```

### Interactive Prompts

```
claude-code-setup
- platform: "mac" 
- experience: "beginner"
```

```
claude-code-learn
- goal: "integrate with my IDE"
- time: "2hours"
- experience: "intermediate"
```

```
claude-code-troubleshoot
- problem: "MCP server won't connect"
- error_message: "connection timeout"
```

```
claude-code-workflow  
- use_case: "web development"
- tools: "vscode, git"
```

## 🏗️ Architecture

### Simplified Design
- **One search tool** for all documentation queries
- **Four specialized prompts** for common user journeys
- **Auto-installation** eliminates setup friction
- **Hybrid resources + tools** approach

### File Locations
- Documentation: `~/.claude/claude-code-docs/content/`
- Fallback: `$(pwd)/.claude/claude-code-docs/content/`
- Development: relative `../content/`

## 🛠️ Development

```bash
# Install dependencies
bun install

# Build
bun run build

# Format & lint
bun run format
bun run lint

# Create new tool (if needed)
bun run create-tool <name>
```

## 🔄 How It Works

1. **First run**: Server auto-clones documentation repo
2. **Search**: Fast local file search with relevance ranking
3. **Prompts**: Generate contextual guidance based on user needs
4. **Resources**: Direct access to any documentation file
5. **Updates**: User can `git pull` in `~/.claude/claude-code-docs/`

## 🎯 Benefits

- **Zero setup** - Just install and go
- **Always current** - Documentation stays in sync with official sources  
- **Fast offline access** - Local files, no API calls
- **Personalized help** - Prompts adapt to user's situation
- **Best practices** - Follows MCP prompt guidelines

This creates the ideal balance of simplicity and functionality for Claude Code documentation access!