> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with MCP Apps

> Try example MCP Apps in Claude Desktop, then use the MCP Apps SDK, examples, and agent skills to add interactive UI to your own MCP server.

An MCP App is interactive UI that your MCP server renders inside a Claude conversation, such as an interactive chart or map. You build one with the [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) as part of your own MCP server, so it reaches people the same way the rest of your plugin's connector does.

This page is for developers who have an MCP server, or are building one, and want it to show UI in Claude.

<Note>
  If you haven't built the server yet, see [Build an MCP server for Claude](/docs/connectors/building/index).
</Note>

To see how an MCP App looks and behaves, [try an example in Claude Desktop](#try-an-example-mcp-app-in-claude-desktop) first, then [build your own](#build-your-own-mcp-app) from the SDK quickstart, the examples, or the agent skills.

## Try an example MCP App in Claude Desktop

The MCP Apps repository publishes example servers that you run locally with `npx` and connect to Claude Desktop through its configuration file.

### Connect an example server

Connecting an example server means adding its entry to Claude Desktop's configuration file, so that the desktop app runs the server locally with `npx`. To connect one:

<Steps>
  <Step title="Install Claude Desktop">
    Install Claude Desktop and sign in.
  </Step>

  <Step title="Open the configuration file">
    Go to [**Settings > Developer**](https://claude.ai/desktop/settings/desktop/developer) and click **Edit Config**.
  </Step>

  <Step title="Add an example server">
    Add one of these example servers to your `claude_desktop_config.json`:

    | Example                                                                                                                   | Description                                                    |
    | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
    | [Customer Segmentation](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/customer-segmentation-server) | Data visualization with scatter charts and clustering analysis |
    | [Map](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/map-server)                                     | Interactive 3D globe viewer using CesiumJS                     |
    | [ShaderToy](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/shadertoy-server)                         | Real-time GLSL shader compilation and display                  |
    | [Sheet Music](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/sheet-music-server)                     | ABC notation rendering with interactive audio playback         |

    The MCP Apps repository has [more examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), each with a ready-to-use config snippet. The config entry for each example in the table runs its server with `npx`, which fetches the latest published version each time. Pin a version, such as `@modelcontextprotocol/server-map@2.0.1`, if you keep an entry beyond trying it out:

    <CodeGroup>
      ```json Customer Segmentation theme={null}
      {
        "mcpServers": {
          "customer-segmentation": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-customer-segmentation", "--stdio"]
          }
        }
      }
      ```

      ```json Map theme={null}
      {
        "mcpServers": {
          "map": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-map", "--stdio"]
          }
        }
      }
      ```

      ```json ShaderToy theme={null}
      {
        "mcpServers": {
          "shadertoy": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-shadertoy", "--stdio"]
          }
        }
      }
      ```

      ```json Sheet Music theme={null}
      {
        "mcpServers": {
          "sheet-music": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-sheet-music", "--stdio"]
          }
        }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Save and restart">
    Save the file and restart the desktop app to connect the server.
  </Step>
</Steps>

### Ask Claude to use the app

Once the server is connected, prompt Claude to use it. For example, with the customer segmentation server connected, ask Claude to show you recent customer data.

Claude asks for permission to display the app. Click **Allow**, or **Always allow** for a server you trust, and the MCP App renders inline in the conversation.

## Build your own MCP App

To add an MCP App to your own MCP server, start from the SDK documentation and examples:

* [Add an interactive UI to your MCP server](/docs/connectors/building/mcp-apps/quickstart): add a one-tool MCP App to the quickstart server on this site, in plain JavaScript with no build step
* [MCP Apps Quickstart](https://modelcontextprotocol.github.io/ext-apps/api/documents/Quickstart.html): step-by-step guide to building your first MCP App
* [SDK API documentation](https://modelcontextprotocol.github.io/ext-apps/api/index.html): full API reference
* [Example implementations](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples): vanilla JS, React, Vue, Svelte, and more

<Tip>To test a remote MCP App locally, connect to it through a proxy such as [mcp-remote](https://www.npmjs.com/package/mcp-remote).</Tip>

### Register tools and resources once for every host

An MCP App can run in Claude and in other hosts that support MCP Apps from one codebase. On the server, register your tools and resources with [`registerAppTool()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html) and [`registerAppResource()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppResource.html), which generate each host's metadata for you. In the app, call [`App.connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) without a transport argument, and the SDK detects the host and picks the transport.

### Set `ui.domain` for Claude

Each host defines its own format for the [`Resource._meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) field, the sandbox origin your app is served from. For Claude, the value is the first 32 hex characters of the SHA-256 of your server URL, followed by `.claudemcpcontent.com`. Compute it with this command, replacing `https://example.com/mcp` with your server URL:

```shell theme={null}
node -e 'const yourServerUrl = "https://example.com/mcp"; console.log(require("crypto").createHash("sha256").update(yourServerUrl).digest("hex").slice(0,32) + ".claudemcpcontent.com")'
```

For `https://example.com/mcp`, the command prints:

```text theme={null}
c3d80a4ed901ee05b21755a88273b4a4.claudemcpcontent.com
```

If Claude reports `Invalid ui.domain format` or `ui.domain mismatch`, see [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting#ui-domain-validation-fails).

### Build with an AI coding agent

If you use an AI coding agent, the [MCP Apps skills](https://github.com/modelcontextprotocol/ext-apps/tree/main/plugins/mcp-apps) guide it through MCP App development. They work in any agent that supports the [Agent Skills](https://agentskills.io) standard, including Claude Code. In Claude Code, install the MCP Apps skills plugin with these commands:

```text theme={null}
/plugin marketplace add modelcontextprotocol/ext-apps
/plugin install mcp-apps@mcp-apps
```

Once the MCP Apps skills plugin is installed, ask your agent to "Create an MCP App" or "Add a UI to my MCP tool".

### Migrate from the OpenAI Apps SDK

If you have an existing app built on the OpenAI Apps SDK, follow the [migration reference](https://modelcontextprotocol.github.io/ext-apps/api/documents/Migrate_OpenAI_App.html) to move it to the MCP Apps SDK. The MCP Apps skills can also do the migration: ask your agent to "Migrate from OpenAI Apps SDK" or "Convert my OpenAI App to an MCP App".

## Send feedback on MCP Apps

To report a problem or suggest a change to MCP Apps, email [mcp-apps@anthropic.com](mailto:mcp-apps@anthropic.com) or open an issue on the [ext-apps repository](https://github.com/modelcontextprotocol/ext-apps/issues).

## Next steps

* [Design guidelines](/docs/connectors/building/mcp-apps/design-guidelines): display modes, mobile layout, and style variables for an app that feels native to Claude
* [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting): developer tools and fixes for an app that doesn't render
* [Submit a connector](/docs/connectors/building/submission): list your server and its MCP App screenshots in the directory
