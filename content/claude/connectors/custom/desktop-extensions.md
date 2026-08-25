> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Desktop extensions

> Deploy enterprise-grade MCP servers with MCPB

Desktop extensions allow you to deploy local MCP servers for Claude Desktop with enterprise-grade features using MCPB (MCP Bundles).

<Note>
  Available for Team and Enterprise plans with Claude Desktop.
</Note>

## What are desktop extensions?

Desktop extensions are local MCP servers that run on user devices, providing:

* Local tool access without internet dependency
* Enhanced security for sensitive operations
* Custom integrations for internal tools
* Enterprise deployment capabilities

## MCPB (MCP Bundles)

MCPB is Anthropic's utility for building and deploying desktop extensions:

* Package MCP servers for distribution
* Handle cross-platform compatibility
* Manage dependencies
* Support enterprise deployment

### Key features

* **Bundling**: Package your MCP server with all dependencies
* **Distribution**: Deploy to users via your organization's channels
* **Updates**: Manage version updates centrally
* **Security**: Sign and verify extensions

## When to use desktop vs remote

| Use Case                    | Recommended       |
| --------------------------- | ----------------- |
| Access to local files/tools | Desktop Extension |
| Internet-hosted services    | Remote MCP        |
| Sensitive enterprise data   | Desktop Extension |
| Public APIs                 | Remote MCP        |
| Offline capability needed   | Desktop Extension |

## Enterprise deployment

For Team and Enterprise plans, admins can:

1. Build custom desktop extensions
2. Package with MCPB
3. Deploy through enterprise software management
4. Control which extensions are available to users

## Security considerations

Desktop extensions run locally with user permissions:

* Access only what the user can access
* No data transmitted unless explicitly designed
* Full audit capability for enterprise
* Revocable by administrators

## Getting started

1. Review the [MCPB documentation](https://github.com/modelcontextprotocol/mcpb)
2. Build your MCP server
3. Bundle with MCPB
4. Test locally
5. Deploy to your organization

## Related topics

<Columns cols={2}>
  <Card title="Building Connectors" icon="hammer" href="/docs/connectors/building/">
    Learn to build MCP servers.
  </Card>

  <Card title="Remote MCP" icon="globe" href="/docs/connectors/custom/remote-mcp">
    Using cloud-hosted connectors.
  </Card>
</Columns>
