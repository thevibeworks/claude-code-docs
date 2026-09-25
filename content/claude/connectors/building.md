> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build an MCP server for Claude

> Build a remote MCP server that people use as a connector in Claude: where it runs, authentication, what it exposes, size and timeout limits, and distribution.

An MCP server gives Claude access to your product or data, and people who use Claude see it as a connector. It's the piece of your [plugin](/docs/build/overview) that reaches your product: the plugin's `.mcp.json` points at the server you build and host, and any skills you include teach Claude how to use it. Claude connects to your server from claude.ai, Claude Desktop, Claude mobile, Cowork, and Claude Code, and the same connector infrastructure backs all of them.

This page is for developers building a remote MCP server for other people to use in Claude. It covers the decisions you make as you build, in the order you meet them, and what Claude's MCP client supports for each one.

<Note>
  * If you're new to the protocol itself, see [Model Context Protocol (MCP)](/docs/connectors/building/mcp) for a short orientation
  * If you want to build a minimal server first and watch Claude call it, see [Build your first MCP server for Claude](/docs/connectors/building/quickstart)
  * If you're not sure your plugin needs an MCP server, see [Decide what to include in your plugin](/docs/connectors/building/what-to-build)
</Note>

## Plan your server

Claude implements a subset of the MCP specification, with its own callback URL and its own size and timeout limits.

<Tip>
  To build with Claude's help, install the official [`mcp-server-dev` plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev) in Claude Code. It walks you through building, testing, and packaging an MCP server interactively, using these docs as its reference.
</Tip>

### Choose where the server runs

A remote server runs on infrastructure you host and is reachable over the internet. Claude connects to it from every Claude app, and a remote server is the recommended kind for a directory listing.

A local server runs on the user's computer. To package one for the Claude desktop app, see [Build a desktop extension with MCPB](/docs/connectors/building/mcpb).

A transport is how Claude and your server exchange MCP messages. Use [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http), which the MCP specification defines for remote servers. Claude also supports the legacy [HTTP+SSE transport](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse), which is being deprecated in favor of Streamable HTTP.

### Choose how users authenticate

Decide on authentication before you write tool code. Claude's OAuth client differs from the generic MCP specification in a few places.

Your server can let Claude in with OAuth 2.0, where each user signs in with their own account; with a static credential that an organization Owner enters once and Claude sends as a request header; or with no authentication at all. [Supported authentication types](/docs/connectors/building/authentication#supported-authentication-types) lists each type and which ones you contact Anthropic to use.

If you use OAuth, check these parts of your setup against Claude's client:

* **Specification version**: Claude follows the [2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization), [2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), and [2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) authorization specifications
* **Client registration**: Claude can register itself with your authorization server through Dynamic Client Registration (DCR). If your server doesn't support DCR, [Register Claude as an OAuth client](/docs/connectors/building/authentication#register-claude-as-an-oauth-client) lists the other ways to give Claude a client identity
* **Redirect URI**: allow `https://claude.ai/api/mcp/auth_callback` for the hosted surfaces and a loopback redirect for Claude Code, as [Callback URLs](/docs/connectors/building/authentication#callback-urls) describes
* **Token refresh**: Claude refreshes access tokens when they expire. [Token refresh](/docs/connectors/building/authentication#token-refresh) has the requirements for your token endpoint

If you need one of these related flows, follow its page:

* **[Lazy authentication](/docs/connectors/building/lazy-authentication)**: if some of your tools work without the user's account, people can use those right away and sign in only when Claude reaches a tool that needs it
* **[Enterprise Managed Auth](/docs/connectors/building/enterprise-managed-auth)**: lets enterprise users connect through their organization's SSO without a consent screen

### Decide what the server exposes

Your server can expose these to Claude:

* [Tools](https://modelcontextprotocol.io/specification/latest/server/tools), [prompts](https://modelcontextprotocol.io/specification/latest/server/prompts), and [resources](https://modelcontextprotocol.io/specification/latest/server/resources)
* [Text](https://modelcontextprotocol.io/specification/latest/schema#textcontent) and [image-based](https://modelcontextprotocol.io/specification/latest/server/tools#image-content) tool results
* [Text](https://modelcontextprotocol.io/specification/latest/schema#textresourcecontents) and [binary](https://modelcontextprotocol.io/specification/latest/schema#blobresourcecontents) resources

Claude doesn't yet support these MCP features, so don't build a feature that depends on them:

* Resource subscriptions
* Sampling
* Advanced or draft capabilities

If you plan to list the server in the directory, [Design tools that pass review](/docs/connectors/building/review-criteria#design-tools-that-pass-review) covers how to name, describe, and annotate tools.

### Design within the size and timeout limits

Keep tool results and tool call durations within these limits. They differ between the hosted surfaces and Claude Code.

| Limit                    | claude.ai and Desktop     | Claude Code                                              |
| ------------------------ | ------------------------- | -------------------------------------------------------- |
| Maximum tool result size | \~150,000 characters      | 25,000 tokens, configurable with `MAX_MCP_OUTPUT_TOKENS` |
| Tool call timeout        | 240 seconds per tool call | Configurable with `MCP_TOOL_TIMEOUT`                     |

### Decide whether to add interactive UI

An MCP App is interactive UI that your MCP server renders inside a Claude conversation, such as an interactive chart or map. It's optional, and you build it as part of the same server. [Get started with MCP Apps](/docs/connectors/building/mcp-apps/getting-started) shows an example and how to build your own.

## Test your server against Claude

You test against the real Claude client, not a staging environment. [Test your connector](/docs/connectors/building/testing) covers adding the server to Claude as a custom connector, validating auth flows with the MCP Inspector, tunneling a local server, and preparing test credentials for review. To connect and debug from the Claude Code command line, see the [Claude Code MCP quickstart](https://code.claude.com/docs/en/mcp-quickstart).

## Decide how people get your server

People add your server to Claude as a connector in one of these ways:

* **As a custom connector**: a user or an organization Owner adds it by entering its URL, with no review by Anthropic
* **From the directory**: Anthropic lists it in the directory after review, so people find it in Claude. [Publish to the directory](/docs/directory/publish) covers who can submit and what review involves
* **Inside a plugin**: you bundle the server with the skills that teach Claude to use it, so people install both together. See [Plugin structure and testing](/docs/plugins/build)

Directory and custom connectors run on the same infrastructure. [Directory connectors vs custom connectors](/docs/connectors/building/directory-vs-custom) compares the two and explains when to offer both.

## Related resources

These resources cover the MCP protocol itself rather than Claude's client:

* **SDKs**: the [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) and [Python](https://github.com/modelcontextprotocol/python-sdk) SDKs contain server implementation examples
* **Protocol specification**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
* **Authorization specification**: read the [authorization spec](https://modelcontextprotocol.io/specification/latest/basic/authorization), especially the third-party service flows
* **MCP Inspector**: validate auth flows outside Claude with the [inspector](https://modelcontextprotocol.io/docs/tools/inspector)

## Next steps

* [Authentication for connectors](/docs/connectors/building/authentication): pick an authentication type and meet Claude's OAuth requirements
* [Test your connector](/docs/connectors/building/testing): add your server as a custom connector and debug connection failures
* [Plugin structure and testing](/docs/plugins/build): bundle your connector with skills so people install both together
* [Publish to the directory](/docs/directory/publish): submit your connector for review so people find it in claude.ai on the web, the desktop and mobile apps, and Cowork. Anyone on a paid Claude plan can submit, and on Team and Enterprise an Owner submits
