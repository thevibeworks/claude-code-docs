> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a desktop extension with MCPB

> Package a local MCP server as a single-click .mcpb install for Claude Desktop: when to build one, the CLI quickstart, manifest.json, and how users install it.

An MCP Bundle (`.mcpb`) is a zip archive containing a local MCP server and a `manifest.json`, which Claude Desktop installs in a single click the way a browser installs an extension. The server runs on the user's machine over stdio, so it can reach local files, locally installed tools, and systems behind the user's firewall without any cloud infrastructure.

This page is for developers packaging a local MCP server for Claude Desktop, whether for internal use or private distribution. It covers when to choose MCPB over a remote server, building and packing the bundle, the manifest, and how users install the result.

For a directory listing, build a remote MCP server, which reaches people on every surface, or include the local server in a plugin, as [Decide what to include in your plugin](/docs/connectors/building/what-to-build) explains.

<Note>
  * If you're building a remote server, see [Build an MCP server for Claude](/docs/connectors/building/index)
  * If you're deploying desktop extensions across a Team or Enterprise organization, see [Install a local connector in the desktop app](/docs/connectors/custom/add-unlisted#install-a-local-connector-in-the-desktop-app)
</Note>

## Decide when to build an MCPB

An MCPB has these characteristics:

* Runs locally on the user's machine
* Communicates via stdio transport
* Bundles all dependencies
* Works offline
* No OAuth required

MCPBs run on the user's machine via stdio with access to local and internal resources. Remote connectors run on your servers via HTTPS and are accessed through Anthropic's infrastructure. Organizations commonly build MCPBs as secure proxies to internal MCP servers, for internal documentation access, and to connect development tools while preserving their security architecture.

See the [MCPB repository](https://github.com/modelcontextprotocol/mcpb) for the complete specification and the [Desktop Extensions blog post](https://www.anthropic.com/engineering/desktop-extensions) for an architecture overview.

### Choose between MCPB and a remote connector

The table lists the needs that point to each option.

| Choose MCPB when you need                                                                                 | Choose a remote connector when you need                        |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Access to systems behind your firewall, such as your issue tracker, internal wikis, and private databases | Cloud services and public APIs with centralized infrastructure |
| Authentication via existing SSO and browser sessions, no token management                                 | OAuth flows with server-side token management                  |
| Zero-trust compliance inside corporate network boundaries                                                 | Distribution across Claude on web, mobile, and desktop         |
| Direct filesystem access for code editing and Git operations                                              | Centralized updates pushed to all users                        |
| Integration with locally installed tools, such as Docker, IDEs, and databases                             | Public-facing integrations used by multiple organizations      |
| Hardware integration and desktop application control                                                      |                                                                |
| Privacy-sensitive operations that should not leave the user's machine                                     |                                                                |
| One-click install with bundled Node.js runtime, no dependencies to manage                                 |                                                                |
| No cloud infrastructure, VPN configuration, or firewall rules                                             |                                                                |
| Organization-level admin controls, such as custom uploads and allowlists                                  |                                                                |
| Full control over authentication, authorization, and audit logs                                           |                                                                |

## Build the bundle

You write a stdio MCP server, generate a manifest with the MCPB CLI, and pack both into a `.mcpb` file. Choose the language and target platforms before you start.

### Choose a language

Node.js is strongly recommended, for these reasons:

* Included with Claude Desktop on macOS and Windows, so users need no separate runtime
* Best compatibility and reliability with Claude Desktop
* Extensive MCP SDK support

### Platform support

Claude Desktop runs on macOS (`darwin`) and Windows (`win32`). Specify supported platforms in the `compatibility` section of your `manifest.json`. Test on both platforms even if you primarily develop on one.

See the [manifest spec compatibility section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#compatibility) for platform and runtime requirement details.

### Create and pack the bundle

The MCPB CLI generates the manifest and packs the bundle.

<Steps>
  <Step title="Install the MCPB CLI">
    ```bash theme={null}
    npm install -g @anthropic-ai/mcpb
    ```
  </Step>

  <Step title="Create your MCP server">
    Build a stdio MCP server using the [MCP SDK](https://www.npmjs.com/package/@modelcontextprotocol/sdk).
  </Step>

  <Step title="Generate the manifest">
    ```bash theme={null}
    mcpb init
    ```
  </Step>

  <Step title="Bundle">
    ```bash theme={null}
    mcpb pack
    ```
  </Step>

  <Step title="Install and test in Claude Desktop">
    Double-click the generated `.mcpb` file.
  </Step>
</Steps>

For detailed implementation guidance, see the [MCPB repository](https://github.com/modelcontextprotocol/mcpb), the [examples directory](https://github.com/modelcontextprotocol/mcpb/tree/main/examples) including a Hello World, and the [README "For Bundle Developers" section](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md).

<Warning>
  Before distributing your MCPB, review the testing and best-practices guidance in the MCPB README to ensure quality.
</Warning>

## Configure manifest.json

The `manifest.json` file is required metadata describing what your MCPB does, how to run it, which tools it provides, and what configuration it needs. These references document it:

| Reference                                                                                | Contents                    |
| ---------------------------------------------------------------------------------------- | --------------------------- |
| [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md) | Full schema with all fields |
| [Example manifests](https://github.com/modelcontextprotocol/mcpb/tree/main/examples)     | Real-world implementations  |
| [CLI documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md)       | Command reference           |

### Add an icon

Icons are optional but recommended. Place `icon.png` in your bundle root and reference it in `manifest.json`. The icon must meet these requirements:

| Requirement | Value                                    |
| ----------- | ---------------------------------------- |
| File name   | `icon.png`, or a custom path             |
| Size        | 512×512px recommended, 256×256px minimum |
| Format      | PNG with transparency                    |
| Location    | Bundle root or specified path            |

You can also provide multiple icon variants for different sizes and for light and dark themes. See the [manifest spec icons section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#icons) for variant syntax and best practices.

### User configuration

Define a `user_config` section in `manifest.json` and Claude Desktop automatically generates a settings UI for your extension. The [manifest spec user configuration section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#user-configuration) covers the full schema, configuration types, validation constraints, sensitive-data handling, and multi-select patterns.

## Distribute your MCPB

Users install the `.mcpb` file themselves in Claude Desktop. Desktop extension listings in the directory are deprecated, and the directory no longer accepts MCPB submissions. To distribute a local MCP server through the directory, include it in a [plugin](/docs/plugins/overview).

### Understand how users install your MCPB

Users can install your MCPB in any of these ways:

* Double-click the `.mcpb` file
* Drag and drop the `.mcpb` file into the Claude Desktop window
* In Claude Desktop, go to **Settings > Extensions > Advanced settings > Install Extension…** and select the `.mcpb` file

Each of these install methods opens an installation UI where the user reviews extension details and permissions, configures required settings, grants permissions, and completes installation. Installation is per-user, so each user installs separately on their own system.

For the end-user installation experience and Team and Enterprise admin controls, such as organization management, allowlists, and policy configuration, see [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

## Get help with MCPB

* [MCPB GitHub issues](https://github.com/modelcontextprotocol/mcpb/issues): bug reports and feature requests
* [MCP specification repo](https://github.com/modelcontextprotocol/modelcontextprotocol): protocol questions
* [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support): general Claude Desktop support

## Related resources

These external references cover the MCPB format, the MCP protocol, and Claude Desktop.

### MCPB framework

* [MCPB repository](https://github.com/modelcontextprotocol/mcpb): complete specification and tools
* [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md): full manifest schema
* [MCPB CLI documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md): command reference
* [MCPB examples](https://github.com/modelcontextprotocol/mcpb/tree/main/examples): reference implementations

### MCP protocol

* [MCP specification](https://modelcontextprotocol.io/docs/getting-started/intro): protocol documentation
* [MCP quickstart](https://modelcontextprotocol.io/docs/develop/build-server): getting-started guide
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk): Node.js implementation
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk): Python implementation

### Claude Desktop

* [Release notes](https://support.claude.com/en/articles/12138966-release-notes): version updates
* [Desktop Extensions blog](https://www.anthropic.com/engineering/desktop-extensions): architecture overview

## Next steps

* [Install a local connector in the desktop app](/docs/connectors/custom/add-unlisted#install-a-local-connector-in-the-desktop-app): deploy local MCP servers for Claude Desktop across a Team or Enterprise organization
* [Submit your plugin](/docs/plugins/submit): list a plugin that includes your local MCP server in the directory
