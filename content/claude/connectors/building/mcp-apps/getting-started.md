> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with MCP Apps

> Learn how to test MCP Apps in Claude

## Try an example MCP App

### Connect an example server

Make sure you have installed and logged into Claude Desktop. Navigate to the [developer settings page](https://claude.ai/desktop/settings/desktop/developer) (**Settings > Developer**) and click the "Edit Config" button.

Add one of the example servers to your `claude_desktop_config.json`:

| Example                                                                                                                       | Description                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [**Customer Segmentation**](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/customer-segmentation-server) | Data visualization with scatter charts and clustering analysis                                                                       |
| [**Map**](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/map-server)                                     | Interactive 3D globe viewer using CesiumJS                                                                                           |
| [**QR Code**](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/qr-server)                                  | QR code generation with customizable colors and styling                                                                              |
| [**ShaderToy**](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/shadertoy-server)                         | Real-time GLSL shader compilation and display                                                                                        |
| [**Sheet Music**](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/sheet-music-server)                     | ABC notation rendering with interactive audio playback                                                                               |
| ⋮                                                                                                                             | Explore [more examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples)—each with ready-to-use config snippets! |

<CodeGroup>
  ```json Customer Segmentation theme={null}
  {
    "mcpServers": {
      "customer-segmentation": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/customer-segmentation-server", "--stdio"]
      }
    }
  }
  ```

  ```json Map theme={null}
  {
    "mcpServers": {
      "map": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/map-server", "--stdio"]
      }
    }
  }
  ```

  ```json QR Code theme={null}
  {
    "mcpServers": {
      "qr": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/qr-server", "--stdio"]
      }
    }
  }
  ```

  ```json ShaderToy theme={null}
  {
    "mcpServers": {
      "shadertoy": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/shadertoy-server", "--stdio"]
      }
    }
  }
  ```

  ```json Sheet Music theme={null}
  {
    "mcpServers": {
      "sheet-music": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/sheet-music-server", "--stdio"]
      }
    }
  }
  ```
</CodeGroup>

Save and restart the desktop app to connect.

### See it in action

Once your local server is connected, prompt Claude to use it. For example, with the customer segmentation server, ask Claude to show you recent customer data.

Claude will prompt you for permission to display the App. Click "Always allow", and you'll see the MCP App render inline in the conversation.

## Build your own MCP App

Ready to add an MCP App to your own MCP server? Here are the key resources:

* [MCP Apps Quickstart](https://modelcontextprotocol.github.io/ext-apps/api/documents/Quickstart.html) - Step-by-step guide to building your first MCP App
* [SDK API Documentation](https://modelcontextprotocol.github.io/ext-apps/api/index.html) - Full API reference
* [Example implementations](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples) - Vanilla JS, React, Vue, Svelte, and more

If you are using an AI coding agent, [MCP Apps skills](https://github.com/modelcontextprotocol/ext-apps/tree/main/plugins/mcp-apps) provide guided development for agents that support the [Agent Skills](https://agentskills.io) standard, including Claude Code, Cursor, Gemini CLI, and others. In Claude Code, you can install the MCP Apps skills plugin with the following commands:

```
/plugin marketplace add modelcontextprotocol/ext-apps
/plugin install mcp-apps@modelcontextprotocol-ext-apps
```

Once installed, ask your agent to "Create an MCP App" or "Add a UI to my MCP tool".

<Tip>You can test remote MCP Apps locally via a proxy like [mcp-remote](https://www.npmjs.com/package/mcp-remote).</Tip>

## Migrate from OpenAI Apps SDK

If you are migrating an existing app from the OpenAI Apps SDK to the MCP Apps SDK, see the [migration reference](https://modelcontextprotocol.github.io/ext-apps/api/documents/Migrate_OpenAI_App.html).

You can also use the MCP Apps skills mentioned above to help migrate your apps. Ask your agent to "Migrate from OpenAI Apps SDK" or "Convert my OpenAI App to an MCP App".

***

We'd love to see what you build! Send feedback to [mcp-apps@anthropic.com](mailto:mcp-apps@anthropic.com) or open an issue on the [ext-apps repository](https://github.com/modelcontextprotocol/ext-apps/issues).
