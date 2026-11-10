> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with MCP Apps

> See what an MCP App can do in Claude, such as the side panel, app tools, and embedded websites, then try an example and build your own with the SDK.

An MCP App is interactive UI that your MCP server renders inside a Claude conversation, such as an interactive chart or map. You build one with the [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) as part of your own MCP server.

This page is for developers who have an MCP server, or are building one, and want it to show UI in Claude.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Deciding whether your MCP server needs UI**: see [Decide what to include in your plugin](https://claude.com/docs/connectors/building/what-to-build.md)
> * **Building the server first**: see [Build an MCP server for Claude](https://claude.com/docs/connectors/building/index.md)
> * **Finding and using connectors that have an MCP App**: see [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)

Start at the section that matches where you are:

* **Scoping an app, or extending one that already renders in Claude**: see [what an MCP App can do in Claude](#what-an-mcp-app-can-do-in-claude), such as open in the side panel, embed your website, or give Claude tools to call
* **New to MCP Apps**: [try an example in Claude Desktop](#try-an-example-mcp-app-in-claude-desktop) to see how an MCP App looks and behaves
* **Ready to build**: [build your own MCP App](#build-your-own-mcp-app) from a quickstart, an example implementation, or the MCP Apps skills for AI coding agents

## What an MCP App can do in Claude

* **[Side panel and full screen](https://claude.com/docs/connectors/building/mcp-apps/display-modes.md)**: show your app beside the conversation or full screen when it needs more room than the conversation gives it
* **[Entry points](https://claude.com/docs/connectors/building/mcp-apps/entry-points.md)**: let people open your app from the **Artifacts** page in Claude, without asking Claude for the app, and let them pin it to the sidebar
* **[App tools](https://claude.com/docs/connectors/building/mcp-apps/app-tools.md)**: register tools in your app's UI so that Claude can change what your app shows, such as a list on screen or the selected rows
* **[Messages](https://claude.com/docs/connectors/building/mcp-apps/send-messages.md)**: send Claude a message from your app, such as when someone clicks a button in your app that asks Claude for a plan
* **[Embedded websites](https://claude.com/docs/connectors/building/mcp-apps/embedded-sites.md)**: load your own website in an `<iframe>` inside your app, such as your product's editor or dashboard
* **[Downloads](https://claude.com/docs/connectors/building/mcp-apps/download-files.md)**: save a file from your app to the user's device

### Check what a capability requires

Check requirements such as these before you build:

* **Organization access**: before you build on a capability such as the side panel, entry points, or app tools, check whether your organization has access by following the steps on that capability's page
* **Remote server**: app tools, entry points, and embedded websites need a connector that's backed by a [remote server](https://claude.com/docs/connectors/building/index.md#choose-where-the-server-runs)
* **Verified listing**: for a directory connector, entry points and embedded websites are available only under a [Verified](https://claude.com/docs/connectors/verification.md#verified) listing.
  * People who install your connector from a [Community](https://claude.com/docs/connectors/verification.md#community) listing don't get either one, even if both worked while you tested with a custom connector.
  * To compare a directory connector with a custom connector, see [Directory connectors vs custom connectors](https://claude.com/docs/connectors/building/directory-vs-custom.md).

Claude Desktop runs the [example servers](#try-an-example-mcp-app-in-claude-desktop) as local servers, so test app tools, entry points, and embedded websites with your own server.

[Add your server to Claude as a custom connector](https://claude.com/docs/connectors/building/testing.md#test-in-claude-as-a-custom-connector), and [expose it through a tunnel](https://claude.com/docs/connectors/building/testing.md#test-a-local-server) first if it runs on your machine. For the conditions on embedded websites in a custom connector, see [Where embedded sites load](https://claude.com/docs/connectors/building/mcp-apps/embedded-sites.md#where-embedded-sites-load).

## Try an example MCP App in Claude Desktop

The MCP Apps repository publishes example servers that you run locally with `npx` and connect to Claude Desktop through its configuration file.

### Connect an example server

**1. Install Claude Desktop**

Install Claude Desktop and sign in.

**2. Open the configuration file**

Go to [**Settings > Developer**](https://claude.ai/desktop/settings/desktop/developer) and click **Edit Config**.

**3. Add an example server**

Add one of these example servers to your `claude_desktop_config.json`:

| Example | Description |
| - | - |
| [Customer Segmentation](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/customer-segmentation-server) | Data visualization with scatter charts and clustering analysis |
| [Map](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/map-server) | Interactive 3D globe viewer using CesiumJS |
| [ShaderToy](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/shadertoy-server) | Real-time GLSL shader compilation and display |
| [Sheet Music](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/sheet-music-server) | ABC notation rendering with interactive audio playback |

The MCP Apps repository has [more examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), each with a ready-to-use config snippet. The config entry for each example in the table runs its server with `npx`, which fetches the latest published version each time. Pin a version, such as `@modelcontextprotocol/server-map@2.0.1`, if you keep an entry beyond trying it out:

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

**4. Save and restart**

Save the file and restart the desktop app to connect the server.

### Ask Claude to use the app

Once the server is connected, prompt Claude to use it. For example, with the customer segmentation server connected, ask Claude to show you recent customer data.

Claude asks for permission to display the app. Click **Allow once**, or **Always allow** for a server you trust, and the MCP App renders inline in the conversation. If the permission setting in the message box is **Auto**, Claude can display the app without asking.

If the tool runs but no app appears, [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#tool-call-appears-but-the-app-is-invisible) lists what to check.

## Build your own MCP App

* [Add an interactive UI to your MCP server](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md): add a one-tool MCP App to the quickstart server on this site, in plain JavaScript with no build step
* [MCP Apps Quickstart](https://modelcontextprotocol.github.io/ext-apps/api/documents/Quickstart.html): step-by-step guide to building your first MCP App
* [SDK API documentation](https://modelcontextprotocol.github.io/ext-apps/api/index.html): full API reference
* [Example implementations](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples): vanilla JS, React, Vue, Svelte, and more

To test a server on your machine as a custom connector in Claude, see [Test a local server](https://claude.com/docs/connectors/building/testing.md#test-a-local-server).

### Register tools and resources once for every host

An MCP App can run in Claude and in other hosts that support MCP Apps from one codebase.

* **On the server**: register your tools and resources with [`registerAppTool()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html) and [`registerAppResource()`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppResource.html), which generate each host's metadata for you
* **In the app**: call [`App.connect()`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#connect) without a transport argument, and the SDK detects the host and picks the transport

### Set `ui.domain` for Claude

Each host defines its own format for the [`Resource._meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) field, the sandbox origin your app is served from.

For Claude, the value is the first 32 hex characters of the SHA-256 of your server URL, followed by `.claudemcpcontent.com`. Compute it with this command, replacing `https://example.com/mcp` with your server URL:

```shell theme={null}
node -e 'const yourServerUrl = "https://example.com/mcp"; console.log(require("crypto").createHash("sha256").update(yourServerUrl).digest("hex").slice(0,32) + ".claudemcpcontent.com")'
```

For `https://example.com/mcp`, the command prints:

```text theme={null}
c3d80a4ed901ee05b21755a88273b4a4.claudemcpcontent.com
```

If Claude reports `Invalid ui.domain format` or `ui.domain mismatch`, see [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md#ui-domain-validation-fails).

### Build with an AI coding agent

If you use an AI coding agent, the [MCP Apps skills](https://github.com/modelcontextprotocol/ext-apps/tree/main/plugins/mcp-apps) guide it through MCP App development. They work in any agent that supports the [Agent Skills](https://agentskills.io) standard, including Claude Code.

In Claude Code, install the MCP Apps skills plugin with these commands:

```text theme={null}
/plugin marketplace add modelcontextprotocol/ext-apps
/plugin install mcp-apps@mcp-apps
```

Once the MCP Apps skills plugin is installed, ask your agent to "Create an MCP App" or "Add a UI to my MCP tool".

### Migrate from the OpenAI Apps SDK

If you have an existing app built on the OpenAI Apps SDK, follow the [migration reference](https://modelcontextprotocol.github.io/ext-apps/api/documents/Migrate_OpenAI_App.html) to move it to the MCP Apps SDK. The MCP Apps skills can also do the migration: ask your agent to "Migrate from OpenAI Apps SDK" or "Convert my OpenAI App to an MCP App".

If your tools already declare global [entry points](https://claude.com/docs/connectors/building/mcp-apps/entry-points.md) under the `openai/ui` key, check what else each tool needs in Claude in [Mark a tool as a global entry point](https://claude.com/docs/connectors/building/mcp-apps/entry-points.md#mark-a-tool-as-a-global-entry-point).

## Send feedback on MCP Apps

To report a problem or suggest a change to MCP Apps, email [mcp-apps@anthropic.com](mailto:mcp-apps@anthropic.com) or open an issue on the [ext-apps repository](https://github.com/modelcontextprotocol/ext-apps/issues).

## Next steps

* [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md): display modes, mobile layout, and style variables for an app that feels native to Claude
* [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md): developer tools and fixes for an app that doesn't render
* [Submit a connector](https://claude.com/docs/connectors/building/submission.md): list your server and its MCP App screenshots in the directory
* [Manage your listing after publishing](https://claude.com/docs/connectors/building/after-publishing.md#update-a-published-connector-or-plugin): update a connector that's already listed in the directory
