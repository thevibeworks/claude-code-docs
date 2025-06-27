#!/bin/bash

# Claude Code Documentation MCP Server Installation Script

set -e

echo "🚀 Installing Claude Code Documentation MCP Server..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    echo "   Visit: https://nodejs.org"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node --version)
NODE_MAJOR_VERSION=$(echo $NODE_VERSION | cut -d'.' -f1 | sed 's/v//')

if [ "$NODE_MAJOR_VERSION" -lt 18 ]; then
    echo "❌ Node.js version $NODE_VERSION is too old. Please upgrade to Node.js 18+."
    exit 1
fi

echo "✅ Node.js $NODE_VERSION detected"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ npm detected"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Build the project
echo "🔨 Building MCP server..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Failed to build MCP server"
    exit 1
fi

echo "✅ MCP server built successfully"

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo "⚠️  Claude Code CLI is not installed."
    echo "   To install: npm install -g @anthropic-ai/claude-code"
    echo "   Then run: claude mcp add claude-docs -- node $(pwd)/dist/index.js"
    echo ""
    echo "🎉 MCP server installation complete!"
    echo "   Server location: $(pwd)/dist/index.js"
    exit 0
fi

echo "✅ Claude Code CLI detected"

# Get current directory
CURRENT_DIR=$(pwd)
SERVER_PATH="$CURRENT_DIR/dist/index.js"

# Check if MCP server is already configured
if claude mcp list 2>/dev/null | grep -q "claude-docs"; then
    echo "⚠️  MCP server 'claude-docs' is already configured."
    echo "   To reconfigure, run: claude mcp remove claude-docs"
    echo "   Then run: claude mcp add claude-docs -- node $SERVER_PATH"
else
    # Add MCP server to Claude Code
    echo "🔧 Configuring MCP server with Claude Code..."
    claude mcp add claude-docs -- node "$SERVER_PATH"
    
    if [ $? -eq 0 ]; then
        echo "✅ MCP server added to Claude Code successfully!"
    else
        echo "❌ Failed to add MCP server to Claude Code"
        echo "   Please run manually: claude mcp add claude-docs -- node $SERVER_PATH"
    fi
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "🔧 Configuration:"
echo "   Server Name: claude-docs"
echo "   Server Path: $SERVER_PATH"
echo ""
echo "📖 Usage examples:"
echo "   claude \"Search the documentation for MCP integration\""
echo "   claude \"I'm new to Claude Code, give me a beginner learning path\""
echo "   claude \"Help me troubleshoot authentication issues\""
echo ""
echo "📚 For more information, see: MCP_SERVER_README.md"
echo ""
echo "🐛 Troubleshooting:"
echo "   - Check MCP servers: claude mcp list"
echo "   - Remove server: claude mcp remove claude-docs"
echo "   - View server logs: Check Claude Code output for errors"