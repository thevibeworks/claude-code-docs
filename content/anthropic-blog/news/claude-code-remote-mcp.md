Title: Remote MCP support in Claude Code

URL Source: https://www.anthropic.com/news/claude-code-remote-mcp

Markdown Content:
Today, we’re announcing support for remote MCP servers in Claude Code. Connect your favorite tools and data sources to personalize your coding experience without needing to manage local servers.

**Using Claude Code as your primary development interface**
-----------------------------------------------------------

Claude Code can access both tools and resources exposed by MCP servers, giving it the ability to pull context from your third-party services—such as dev tools, project management systems, and knowledge bases—and take actions within those services.

You can integrate Claude Code with any remote MCP server, and the growing ecosystem of servers means that new capabilities are constantly coming online.

For example, by integrating Claude Code with the Sentry MCP server, you can access errors and issues from Sentry. Then, you can debug using the context of those issues without leaving your terminal.

You can also integrate Claude Code with the Linear MCP server to work with the context of your active projects.

“Linear's MCP integration brings Linear projects and issues directly into Claude Code,” shares Tom Moor, Head of Engineering at Linear. “With structured, real-time context from Linear, Claude Code can pull in issue details and project status—engineers can now stay in flow when moving between planning, writing code, and managing issues. Fewer tabs, less copy-paste. Better software, faster.”

**Seamless connections with minimal maintenance**
-------------------------------------------------

Remote MCP servers offer a lower maintenance alternative to local servers: just add the vendor’s URL to Claude Code—no manual setup required. Vendors handle updates, scaling, and availability, so you can focus on building instead of managing server infrastructure.

Claude Code also features native OAuth support for remote MCP servers, ensuring secure connections to your existing accounts. Simply authenticate to your servers once, and Claude Code handles the rest—no API keys to manage or credentials to store.

**Getting started**
-------------------

Remote MCP server support is available now in Claude Code. View the [documentation](https://docs.anthropic.com/en/docs/claude-code/mcp) to get started or explore our [MCP directory](http://anthropic.com/partners/mcp) with recommended servers.
