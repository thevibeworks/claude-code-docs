> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What should I build: MCP, plugin, or both?

> Decide between an MCP server, a plugin, or both for your Claude integration

Most partners ship two things: a remote MCP server and a plugin that wraps it. They serve different purposes, and together they give users the best experience.

## The recommendation

Build a **remote MCP server with OAuth** first to provide connectivity and core functionality. Then create a **plugin with skills** that helps users get the most out of that MCP server.

|                  | MCP server                                       | Plugin                                           |
| ---------------- | ------------------------------------------------ | ------------------------------------------------ |
| **What it is**   | A live tool surface Claude calls over HTTP       | An installable bundle of skills and connectors   |
| **Mental model** | "Claude can call your API"                       | "Claude knows how to *use* your product"         |
| **Contains**     | Tools, prompts, resources, optionally MCP App UI | Skills, MCP connector references, slash commands |
| **Works in**     | Claude.ai, Desktop, mobile, Cowork, Claude Code  | Claude Code, Cowork                              |

## When to build only one

**MCP server only** is fine when your integration is simple and doesn't need skills—a few well-named tools that Claude can use without additional guidance.

**Plugin only** is fine when you already have a public API or CLI that doesn't need an MCP wrapper. A plugin can ship skills that teach Claude to use that API or CLI directly.

## What a plugin can bundle

A plugin can contain any combination of:

* Skills only
* A single MCP connector reference
* Skills plus one or more MCP connectors
* Multiple MCP connectors

Plugins can reference both remote and local MCP servers. A remote MCP works on every Claude surface (web, mobile, Cowork, Desktop, Claude Code); a local MCP works only in Claude Desktop and Claude Code. Most MCP servers are remote.

## How they coexist

A plugin references a remote MCP server by **URL**. If a user has both your directory connector and your plugin installed, Claude sees one set of tools—the plugin and the connector point at the same server. If a plugin references an MCP URL that isn't in the directory, the connector appears as **Custom** in the user's settings.

Both MCP servers and plugins can update without Anthropic involvement. When you add tools to your MCP server, plugins that reference it pick them up automatically. Plugin updates are pushed via GitHub and pass through automated screening.

## Skills are not a standalone directory type

Skills are user-shared micro-workflows. **Plugins are the distribution mechanism for skills**—you can't submit a skill to the directory on its own. If you have skills to ship, bundle them in a plugin.

## Build it with Claude

The fastest way to scaffold an MCP server is with Claude itself. Install the official [`mcp-server-dev` plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev) in Claude Code and run `/mcp-server-dev:build-mcp-server`—it interviews you about your use case, picks the right deployment model, and generates a working server.

## Next steps

<Columns cols={2}>
  <Card title="Build an MCP server" icon="server" href="/docs/connectors/building/index">
    Start with the MCP building guide.
  </Card>

  <Card title="Build a plugin" icon="puzzle-piece" href="/docs/plugins/overview">
    Bundle skills and connectors together.
  </Card>
</Columns>
