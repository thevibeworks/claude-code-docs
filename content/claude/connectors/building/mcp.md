> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Context Protocol (MCP)

> Understanding the open standard powering Claude's connectors

The Model Context Protocol (MCP) is an open standard created by Anthropic for AI applications to connect with tools and data sources.

## What is MCP?

MCP provides a standardized way for AI assistants like Claude to:

* Connect to external tools and services
* Access data from various sources
* Perform actions on behalf of users
* Maintain security and user control

## How MCP works

### Local vs remote servers

| Type           | Description            | Use Case                          |
| -------------- | ---------------------- | --------------------------------- |
| **Local MCP**  | Runs on your device    | Desktop integrations, local tools |
| **Remote MCP** | Hosted on the internet | Web services, cloud applications  |

### Key components

* **Tools**: Actions Claude can perform (search, create, modify)
* **Resources**: Data Claude can access (files, documents, records)
* **Prompts**: Predefined interactions for specific tasks

## Security model

### User control

* You authenticate each connector individually
* Permissions mirror your access on the external service
* You can disconnect at any time

### Tool hints

All MCP tools must declare:

* [`readOnlyHint`](https://modelcontextprotocol.io/specification/latest/schema#toolannotations-readonlyhint): Tool only reads data
* [`destructiveHint`](https://modelcontextprotocol.io/specification/latest/schema#toolannotations-destructivehint): Tool can modify or delete data

This helps Claude and users understand what actions are possible.

## Building with MCP

The [MCP documentation](https://modelcontextprotocol.io/docs) is the source of truth for building MCP servers.

### For developers

* Open specification at [modelcontextprotocol.io](https://modelcontextprotocol.io)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) and [Python SDK](https://github.com/modelcontextprotocol/python-sdk) available
* Cloudflare hosting support with OAuth

### Submitting to directory

Organizations can [submit MCP servers](/docs/connectors/building/submission) to the Connectors Directory for broader availability.

## Related topics

<Columns cols={2}>
  <Card title="MCP in Claude Code" icon="terminal" href="https://code.claude.com/docs/en/mcp">
    Connect MCP servers to Claude Code from the command line.
  </Card>

  <Card title="Submit to Directory" icon="paper-plane" href="/docs/connectors/building/submission">
    Review requirements and submit your connector.
  </Card>
</Columns>
