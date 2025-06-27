# Claude Code Documentation MCP Server

This MCP (Model Context Protocol) server provides structured access to Claude Code documentation and learning resources. It enables Claude Code users to query documentation, get personalized learning paths, receive contextual help, and track their learning progress.

## Features

### 🔍 Documentation Search
- Full-text search across all Claude Code documentation
- Category-based filtering (quickstart, setup, workflows, troubleshooting, MCP, integrations, security)
- Fuzzy search with relevance scoring
- Direct links to original documentation

### 📚 Personalized Learning Paths
- Skill-level based tutorial recommendations (beginner, intermediate, advanced)
- Goal-oriented learning tracks (getting started, team collaboration, advanced workflows, integrations)
- Step-by-step guidance with time estimates
- Prerequisites tracking

### 🆘 Contextual Help
- Situation-aware assistance based on current context
- Error message analysis and troubleshooting suggestions
- Quick action recommendations
- Related documentation discovery

### 📈 Progress Tracking
- Learning progress monitoring with badges and achievements
- Streak tracking for consistent learning
- Personalized next-step recommendations
- Progress export and analytics

### 🧠 Concept Explanations
- Detailed explanations of Claude Code concepts
- Adjustable detail levels (overview, detailed, advanced)
- Code examples and best practices
- Related concept recommendations

## Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Build the server:**
   ```bash
   npm run build
   ```

3. **Add to Claude Code:**
   ```bash
   # Add as stdio MCP server
   claude mcp add claude-docs -- node /path/to/claude-code-docs/dist/index.js
   
   # Or add with npm global install path
   claude mcp add claude-docs -- claude-code-docs-mcp
   ```

## Available Tools

### `search_documentation`
Search Claude Code documentation for specific topics.

**Parameters:**
- `query` (required): Search query
- `category` (optional): Filter by category (all, quickstart, setup, workflows, troubleshooting, mcp, integrations, security)
- `limit` (optional): Maximum results (1-20, default: 5)

**Example:**
```json
{
  "query": "github integration setup",
  "category": "integrations",
  "limit": 3
}
```

### `get_tutorial_path`
Get personalized learning paths based on skill level and goals.

**Parameters:**
- `skill_level` (required): beginner, intermediate, or advanced
- `goal` (required): getting_started, team_collaboration, advanced_workflows, integrations, or troubleshooting

**Example:**
```json
{
  "skill_level": "beginner",
  "goal": "getting_started"
}
```

### `get_contextual_help`
Get help based on current situation or problems.

**Parameters:**
- `context` (required): Description of current situation
- `error_message` (optional): Error message if encountering issues

**Example:**
```json
{
  "context": "trying to set up Claude Code with my team project",
  "error_message": "Authentication failed"
}
```

### `track_progress`
Track learning progress and get recommendations.

**Parameters:**
- `action` (required): mark_complete, get_progress, or get_next_steps
- `completed_topic` (optional): Topic completed (for mark_complete action)

**Example:**
```json
{
  "action": "mark_complete",
  "completed_topic": "quickstart guide"
}
```

### `explain_concept`
Get detailed explanations of Claude Code concepts.

**Parameters:**
- `concept` (required): Concept to explain
- `detail_level` (optional): overview, detailed, or advanced

**Example:**
```json
{
  "concept": "extended thinking",
  "detail_level": "detailed"
}
```

## Usage Examples

### Basic Documentation Search
```bash
# In Claude Code with MCP server configured
claude "Search the documentation for information about MCP integration"
```

### Getting Started Path
```bash
claude "I'm new to Claude Code, can you give me a beginner learning path for getting started?"
```

### Troubleshooting Help
```bash
claude "I'm getting authentication errors when trying to use Claude Code with my team project. Can you help?"
```

### Progress Tracking
```bash
claude "I just completed the quickstart guide, please mark it as done and tell me what to learn next"
```

## Configuration

### Environment Variables
- `CLAUDE_CODE_DOCS_PATH`: Custom path to documentation directory (default: current working directory)
- `PROGRESS_FILE_PATH`: Custom path for progress tracking file (default: `.claude-code-progress.json`)

### File Structure
The server expects the following directory structure:
```
claude-code-docs/
├── claude-code-docs/          # Official documentation
├── anthropic-blog/           # Blog posts and articles
├── release-notes/           # Changelog and release notes
└── .claude-code-progress.json # Progress tracking (auto-created)
```

## Development

### Scripts
- `npm run build` - Build TypeScript to JavaScript
- `npm run dev` - Watch mode for development
- `npm start` - Start the server

### Architecture
- **DocumentationService**: Handles loading and parsing documentation files
- **SearchService**: Provides fuzzy search with Fuse.js
- **TutorialService**: Manages learning paths and contextual help
- **ProgressService**: Tracks learning progress and achievements

### Adding New Features
1. Create new tool definition in `setupHandlers()`
2. Add corresponding handler method
3. Implement service logic if needed
4. Update documentation

## Troubleshooting

### Common Issues

**"No files found" error:**
- Ensure you're running the server from the correct directory
- Check that documentation directories exist and contain .md files

**"MCP server not responding":**
- Verify the server is built: `npm run build`
- Check Claude Code MCP configuration: `claude mcp list`
- Review server logs for initialization errors

**"Search returns no results":**
- Wait for documentation indexing to complete
- Try broader search terms
- Check if documentation files are properly formatted

### Debug Mode
Run with verbose logging:
```bash
NODE_ENV=development node dist/index.js
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request with clear description

## License

MIT License - see LICENSE file for details