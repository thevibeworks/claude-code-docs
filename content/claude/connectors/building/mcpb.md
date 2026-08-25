> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a desktop extension with MCPB

> Package a local MCP server as a single-click .mcpb install for Claude Desktop

<Note>
  MCPB is the secondary distribution path. Remote MCP servers are recommended for directory listing—see [what to build](/docs/connectors/building/what-to-build).
</Note>

This guide covers building an MCP Bundle (`.mcpb`) for internal use, private distribution, or as a foundation for [submission to the Connectors Directory](/docs/connectors/building/submission).

## What is an MCPB?

An `.mcpb` file is a zip archive containing a local MCP server and a `manifest.json`. It enables single-click installation in Claude Desktop, similar to a browser extension.

Key characteristics:

* Runs locally on the user's machine
* Communicates via stdio transport
* Bundles all dependencies
* Works offline
* No OAuth required

See the [MCPB repository](https://github.com/modelcontextprotocol/mcpb) for the complete specification and the [Desktop Extensions blog post](https://www.anthropic.com/engineering/desktop-extensions) for an architecture overview.

## Local (MCPB) vs remote: which to build

| Choose MCPB when you need                                                                    | Choose a remote connector when you need                        |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Access to systems behind your firewall (JIRA, Confluence, internal wikis, private databases) | Cloud services and public APIs with centralized infrastructure |
| Authentication via existing SSO and browser sessions, no token management                    | OAuth flows with server-side token management                  |
| Zero-trust compliance inside corporate network boundaries                                    | Distribution across Claude on web, mobile, and desktop         |
| Direct filesystem access for code editing and Git operations                                 | Centralized updates pushed to all users                        |
| Integration with locally installed tools (Docker, IDEs, databases)                           | Public-facing integrations used by multiple organizations      |
| Hardware integration and desktop application control                                         |                                                                |
| Privacy-sensitive operations that should not leave the user's machine                        |                                                                |
| One-click install with bundled Node.js runtime, no dependencies to manage                    |                                                                |
| No cloud infrastructure, VPN configuration, or firewall rules                                |                                                                |
| Organization-level admin controls (custom uploads, allowlists)                               |                                                                |
| Full control over authentication, authorization, and audit logs                              |                                                                |

**Key difference:** MCPBs run on the user's machine via stdio with access to local and internal resources. Remote connectors run on your servers via HTTPS and are accessed through Anthropic's infrastructure.

Organizations commonly build MCPBs as secure proxies to internal MCP servers, for internal documentation access, and to connect development tools while preserving their security architecture.

For remote connector guidance, see [building custom connectors](/docs/connectors/building/index).

## Choose a language

Node.js is strongly recommended:

* Ships with Claude Desktop on macOS and Windows, so users need no separate runtime
* Best compatibility and reliability with Claude Desktop
* Extensive MCP SDK support

## Platform support

Claude Desktop runs on macOS (`darwin`) and Windows (`win32`). Specify supported platforms in the `compatibility` section of your `manifest.json`. Test on both platforms even if you primarily develop on one.

See the [manifest spec compatibility section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#compatibility) for platform and runtime requirement details.

## Quickstart

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

## manifest.json

The `manifest.json` file is required metadata describing what your MCPB does, how to run it, which tools it provides, and what configuration it needs.

| Reference                                                                                |                             |
| ---------------------------------------------------------------------------------------- | --------------------------- |
| [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md) | Full schema with all fields |
| [Example manifests](https://github.com/modelcontextprotocol/mcpb/tree/main/examples)     | Real-world implementations  |
| [CLI documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md)       | Command reference           |

## Add an icon

Icons are optional but recommended. Place `icon.png` in your bundle root and reference it in `manifest.json`.

| Requirement | Value                                     |
| ----------- | ----------------------------------------- |
| File name   | `icon.png` (or a custom path)             |
| Size        | 512×512px recommended (minimum 256×256px) |
| Format      | PNG with transparency                     |
| Location    | Bundle root or specified path             |

You can also provide multiple icon variants for different sizes and themes (light/dark mode). See the [manifest spec icons section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#icons) for variant syntax and best practices.

## User configuration

Define a `user_config` section in `manifest.json` and Claude Desktop automatically generates a settings UI for your extension. The [manifest spec user configuration section](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#user-configuration) covers the full schema, configuration types, validation constraints, sensitive-data handling, and multi-select patterns.

## How users install your MCPB

Users can install three ways:

1. **Double-click** the `.mcpb` file
2. **Drag and drop** the `.mcpb` file into the Claude Desktop window
3. **Settings**: Settings → Extensions → Advanced settings → Install Extension… → select the `.mcpb` file

All three open an installation UI where the user reviews extension details and permissions, configures required settings, grants permissions, and completes installation. Installation is per-user; each user installs separately on their own system.

For the end-user installation experience and Team/Enterprise admin controls (organization management, allowlists, policy configuration), see [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

## Resources

**MCPB framework**

* [MCPB repository](https://github.com/modelcontextprotocol/mcpb): complete specification and tools
* [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md): full manifest schema
* [MCPB CLI documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md): command reference
* [MCPB examples](https://github.com/modelcontextprotocol/mcpb/tree/main/examples): reference implementations

**MCP protocol**

* [MCP specification](https://modelcontextprotocol.io/docs/getting-started/intro): protocol documentation
* [MCP quickstart](https://modelcontextprotocol.io/docs/develop/build-server): getting-started guide
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk): Node.js implementation
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk): Python implementation

**Claude Desktop**

* [Release notes](https://support.claude.com/en/articles/12138966-release-notes): version updates
* [Desktop Extensions blog](https://www.anthropic.com/engineering/desktop-extensions): architecture overview

## Get help

* [MCPB GitHub issues](https://github.com/modelcontextprotocol/mcpb/issues): bug reports and feature requests
* [MCP specification repo](https://github.com/modelcontextprotocol/modelcontextprotocol): protocol questions
* [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support): general Claude Desktop support

Check repository discussions for community Q\&A, follow release notes for updates, and review the examples for implementation patterns.

## Ready for distribution

If you have a working MCPB and want broader distribution and discoverability, submit it to the Connectors Directory. See [submitting to the directory](/docs/connectors/building/submission) for requirements including:

* Mandatory tool annotations for all tools
* Privacy policy requirements
* Working examples that exercise each tool
* Test credentials where applicable
* The complete submission process and review timeline
