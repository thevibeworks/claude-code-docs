> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Inspector

> Interactive developer tooling for testing and debugging MCP servers, in the browser, on the command line, and in the terminal

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is the reference developer tool for testing and debugging [MCP servers](https://modelcontextprotocol.io/docs/draft/learn/server-concepts.md). It ships as a single package, `@modelcontextprotocol/inspector`, providing **three clients behind one binary**:

| Client | Invocation | What it's for |
| - | - | - |
| **Web** | `npx @modelcontextprotocol/inspector` | A full graphical inspector in the browser. The default, and the richest surface. |
| **CLI** | `npx @modelcontextprotocol/inspector --cli` | A scriptable, machine-readable client for CI, shell pipelines, and coding agents. |
| **TUI** | `npx @modelcontextprotocol/inspector --tui` | An interactive terminal UI, for when a browser isn't available or wanted. |

All three are built on the same shared core, so a connection behaves identically across them: the same transports, the same configuration files, the same OAuth state on disk, and the same [protocol-era](https://modelcontextprotocol.io/docs/draft/tools/inspector/protocol-eras.md) negotiation (legacy vs. modern 2026-07-28).

The package also installs **`mcpdo`**, an experimental [connection client](https://modelcontextprotocol.io/docs/draft/tools/inspector/mcpdo.md) that connects to a server once and keeps it open across many commands, on the same core.

![](https://mintcdn.com/mcp/pUebPdrb6PY5_mfH/images/inspector/web-monitor-sidebar.png?fit=max\&auto=format\&n=pUebPdrb6PY5_mfH\&q=85\&s=2ced9eeefa020be53fe4fe957b7d07c6)

The MCP Inspector web client after a tool call, with the monitoring sidebar pinned and widened so the JSON-RPC exchange stays readable while you work.

## Quickstart

The Inspector requires **Node 22.19.0 or newer** and runs directly through `npx`. No installation is required:

**Web**

```bash theme={null}
# Launch the web UI and connect to a local stdio server
npx @modelcontextprotocol/inspector node path/to/server/index.js

# Or launch with no target and add servers from the UI
npx @modelcontextprotocol/inspector
```

The command prints a URL carrying a per-launch API token and opens it in your browser (set `MCP_AUTO_OPEN_ENABLED=false` to stop it opening). See [Web client](https://modelcontextprotocol.io/docs/draft/tools/inspector/web.md).

**CLI**

```bash theme={null}
# List a server's tools and exit
npx @modelcontextprotocol/inspector --cli node path/to/server/index.js --method tools/list

# Call a tool and pipe the result into jq
npx @modelcontextprotocol/inspector --cli https://api.example.com/mcp --transport http \
  --method tools/call --tool-name get_weather --tool-arg city=Boston --format json | jq .result
```

See [CLI client](https://modelcontextprotocol.io/docs/draft/tools/inspector/cli.md).

**TUI**

```bash theme={null}
npx @modelcontextprotocol/inspector --tui node path/to/server/index.js
```

See [TUI client](https://modelcontextprotocol.io/docs/draft/tools/inspector/tui.md).

### Inspecting published servers

Pass the command that launches the server as the Inspector's arguments, or point it at a remote server with `--server-url`:

**npm package**

```bash theme={null}
npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ~/Desktop
```

**PyPI package**

```bash theme={null}
npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
```

**Remote HTTP server**

```bash theme={null}
npx @modelcontextprotocol/inspector --server-url https://api.example.com/mcp --transport http
```

Always read a server's own README first, since every server requires different commands and arguments.

> [!WARNING]
>
> **The Inspector stores secrets (OAuth tokens, OAuth client secrets, and stdio
> `env:` values) in the OS keychain when one is available.** On a machine with
> no keychain (Linux without libsecret or a Secret Service, headless and SSH
> sessions, Termux, and containers with a mounted volume) they are saved to
> `~/.mcp-inspector/secrets.json` instead, **unencrypted unless you supply a
> key**. See [Where secrets are
> stored](https://modelcontextprotocol.io/docs/draft/tools/inspector/configuration.md#where-secrets-are-stored)
> for how to get a keychain back, encrypt the file, or keep secrets in memory
> only.

## Launcher flags vs. client flags

`mcp-inspector`, the binary that `npx @modelcontextprotocol/inspector` runs, is a thin launcher. It owns only two things:

1. **The mode flag:** `--web` (default), `--cli`, or `--tui`. At most one; passing two errors with `Specify at most one of --web, --cli, or --tui.`
2. **`-h` / `--help`.**

Everything else (`--catalog`, `--config`, `--server-url`, `--transport`, `--method`, the OAuth flags) is defined by the *client*, not the launcher, and the clients do not all define the same set. The [Configuration and flags](https://modelcontextprotocol.io/docs/draft/tools/inspector/configuration.md) page is organized that way, by owner.

> [!NOTE]
>
> Mode flags are recognized only at the front of the command line: the first token that isn't `--web` / `--cli` / `--tui` ends launcher parsing, and everything after it is forwarded to the client unchanged. That's what lets a literal `--cli` appear later as one of your server's own arguments:
>
> ```bash theme={null}
> mcp-inspector --cli node server.js --cli   # mode is CLI; the trailing --cli goes to server.js
> ```

> [!NOTE]
>
> `--help` behaves differently with and without a mode flag. Without one,
> `-h`/`--help` anywhere on the command line (even after a server command)
> prints the launcher's help and exits. With a mode flag it is forwarded, so
> `mcp-inspector --cli --help` prints the CLI's full flag reference instead.

## Where to go next

> **[Web client](https://modelcontextprotocol.io/docs/draft/tools/inspector/web.md)**
>
> A tab-by-tab walkthrough of the graphical inspector.

> **[CLI client](https://modelcontextprotocol.io/docs/draft/tools/inspector/cli.md)**
>
> Method reference, output formats, exit codes, and CI recipes.

> **[TUI client](https://modelcontextprotocol.io/docs/draft/tools/inspector/tui.md)**
>
> Terminal navigation and keyboard reference.

> **[Configuration and flags](https://modelcontextprotocol.io/docs/draft/tools/inspector/configuration.md)**
>
> Catalog vs. config files, the full per-client flag reference, and
> environment variables.

> **[Authorization](https://modelcontextprotocol.io/docs/draft/tools/inspector/authorization.md)**
>
> The OAuth flow end to end, mid-session re-authorization, and loopback
> callbacks.

> **[Protocol eras](https://modelcontextprotocol.io/docs/draft/tools/inspector/protocol-eras.md)**
>
> Legacy vs. modern (2026-07-28) operation, and how every tab changes between
> protocol eras.

> **[mcpdo connection client](https://modelcontextprotocol.io/docs/draft/tools/inspector/mcpdo.md)**
>
> Connect once, then run many commands against a named connection.

> **[Security](https://modelcontextprotocol.io/docs/draft/tools/inspector/security.md)**
>
> The threat model: the web backend's token, Docker, secret storage, stdio
> servers, and the mcpdo daemon.

> **[Recipes](https://modelcontextprotocol.io/docs/draft/tools/inspector/recipes.md)**
>
> Importing client configs, reviewing MCP Apps, Docker, and network hosting.

> **[Debugging guide](https://modelcontextprotocol.io/docs/draft/tools/debugging.md)**
>
> Broader debugging strategies beyond the Inspector.
