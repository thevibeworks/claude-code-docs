> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Context Protocol (MCP)

> Get oriented to the Model Context Protocol, the open standard behind Claude's connectors: local and remote servers, tools, resources, and prompts.

The Model Context Protocol (MCP) is an open standard created by Anthropic for AI applications to connect with tools and data sources. When you build an MCP server and someone adds it to Claude, they see it as a [connector](/docs/connectors/getting-started).

This page is a short orientation for developers who are new to MCP. The [MCP documentation](https://modelcontextprotocol.io/docs) is the source of truth for building MCP servers, and [Build an MCP server for Claude](/docs/connectors/building/index) lists what Claude's client supports once you're ready to build.

## Understand what MCP provides

MCP gives AI assistants like Claude a standardized way to do the following:

* Connect to external tools and services
* Access data from various sources
* Perform actions on behalf of users
* Maintain security and user control

## Understand how MCP servers work

An MCP server runs either on the user's device or on the internet, and exposes tools, resources, and prompts to Claude.

### Local and remote servers

Where the server runs determines which integrations it suits.

| Type       | Description               | Use case                          |
| ---------- | ------------------------- | --------------------------------- |
| Local MCP  | Runs on the user's device | Desktop integrations, local tools |
| Remote MCP | Hosted on the internet    | Web services, cloud applications  |

### Tools, resources, and prompts

A server exposes its capabilities to Claude as tools, resources, and prompts:

* **Tools**: actions Claude can perform, such as search, create, and modify
* **Resources**: data Claude can access, such as files, documents, and records
* **Prompts**: predefined interactions for specific tasks

## Security model

Users stay in control of each connector, and every tool declares whether it can change data.

### User control

Each person who uses your connector keeps these controls:

* They authenticate each connector individually
* Their permissions mirror their access on the external service
* They can disconnect at any time

### Tool hints

All MCP tools must declare both of these annotations:

* [`readOnlyHint`](https://modelcontextprotocol.io/specification/latest/schema#toolannotations-readonlyhint): the tool only reads data
* [`destructiveHint`](https://modelcontextprotocol.io/specification/latest/schema#toolannotations-destructivehint): the tool can modify or delete data

Claude and users read these hints to understand what actions a tool can take.

## Build with MCP

The [MCP documentation](https://modelcontextprotocol.io/docs) is the source of truth for building MCP servers. Start from these resources:

* Open specification at [modelcontextprotocol.io](https://modelcontextprotocol.io)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) and [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* Cloudflare hosting support with OAuth

Organizations can [submit MCP servers](/docs/connectors/building/submission) to the Connectors Directory for broader availability.

## Next steps

* [Build an MCP server for Claude](/docs/connectors/building/index): the transports, authentication, protocol features, and limits Claude's client supports
* [Authentication for connectors](/docs/connectors/building/authentication): OAuth requirements and supported auth types
* [MCP in Claude Code](https://code.claude.com/docs/en/mcp): connect MCP servers to Claude Code from the command line
* [Submitting to the Connectors Directory](/docs/connectors/building/submission): review requirements and submit your connector
