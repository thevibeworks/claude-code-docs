> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Building cross-platform MCP Apps

> Build MCP Apps that work with both Claude and ChatGPT using a single codebase

MCP Apps can run in both Claude and ChatGPT from a single codebase. The SDK auto-detects the host environment and uses the appropriate transport, though some platform-specific behaviors require attention.

## How it works

### Server side

Use [`registerAppTool()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html) and [`registerAppResource()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppResource.html) to register your tools and resources. These helper functions automatically generate platform-specific metadata, so you write the registration once and it works on both platforms.

### Client side

Call [`App.connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) without an explicit transport parameter. The SDK detects whether it's running in Claude or ChatGPT and uses the appropriate transport automatically.

## Platform differences

While the SDK handles most cross-platform concerns automatically, some behaviors vary between hosts.

### Domain handling

The [`Resource._meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) field format and validation rules are determined by each host platform. For example, hosts may use hash-based subdomains, URL-derived patterns, or other formats.

For Claude, compute the `Resource._meta.ui.domain` value by running this command, replacing `https://example.com/mcp` with your server URL:

```shell theme={null}
node -e 'const yourServerUrl = "https://example.com/mcp"; console.log(require("crypto").createHash("sha256").update(yourServerUrl).digest("hex").slice(0,32) + ".claudemcpcontent.com")'
```

Example output for `https://example.com/mcp`:

```
c3d80a4ed901ee05b21755a88273b4a4.claudemcpcontent.com
```
