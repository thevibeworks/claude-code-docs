> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Code in Claude Desktop on 3P

> How Claude Desktop on 3P configuration applies to the embedded Claude Code engine

Code in Claude Desktop on third-party (3P) is the embedded [Claude Code](https://code.claude.com/docs/en/overview) interface. It runs the same Claude Code engine as the standalone CLI, with a graphical session manager, and it inherits your Claude Desktop on 3P configuration automatically.

## How configuration propagates

When the app starts a Code session, it translates your Claude Desktop on 3P [configuration keys](https://claude.com/docs/third-party/claude-desktop/configuration.md) into the equivalent Claude Code settings and passes them to the session. You configure one profile, and Cowork and Code both honor it.

Each key reaches Claude Code through one of two mechanisms, and the distinction matters if you also deploy Claude Code's own managed settings (see [the next section](#interaction-with-claude-code%E2%80%99s-own-managed-settings)).

### Always applied

These keys are passed directly to the Claude Code process as environment variables or launch options. They take effect on every Code session and cannot be overridden by user-level Claude Code settings or by a separately deployed `managed-settings.json`.

| Claude Desktop on 3P key | Effect in Code sessions |
| - | - |
| `inferenceProvider` and all provider credential keys (`inferenceGateway*`, `inferenceAnthropicApiKey`, `inferenceVertex*`, `inferenceBedrock*`, `inferenceFoundry*`, `inferenceCredentialHelper*`) | Selects the inference backend and supplies credentials. Code sessions use the same provider, endpoint, and credentials as Cowork sessions. |
| `inferenceModels` | Populates the model picker. The first entry is the default for new Code sessions. |
| `autoModeEnabled` | Controls **Auto mode**. When the key isn't set, Code sessions offer **Auto mode** and new sessions start in it unless the user has already chosen another mode or a Claude Code `permissions.defaultMode` applies. Set it to `false` to remove **Auto mode** from Code and Cowork. Set it to `true` to also offer the mode in Cowork, where it appears as **Automatically approve**. In Code sessions, a separately deployed Claude Code [managed-settings file](#interaction-with-claude-code%E2%80%99s-own-managed-settings) that sets `disableAutoMode` to `"disable"` also keeps **Auto mode** hidden, whatever this key is set to. To change what **Auto mode** allows and blocks, see [Tune the Auto mode classifier](#tune-the-auto-mode-classifier). |
| `scheduledTasksEnabled` | When `false`, the routines list in Code is hidden and Code sessions start without Claude Code's in-session scheduling tools, so the `/loop` command cannot schedule recurring work. Cowork's scheduled tasks are turned off by the same key. |
| `disabledBuiltinTools` | Removes the listed tools from Code sessions. A `Read(…)` rule applies to Claude's file tools, and [only in part to shell commands](#file-path-rules-and-shell-commands). Tools your provider does not support, such as WebSearch on Amazon Bedrock, are removed automatically in addition to your list. |
| `builtinToolPolicy` | Tools set to `"ask"` require approval on each call in Code sessions, enforced via a PreToolUse hook and Claude Code `permissions.ask` rules. Argument-scoped rules such as `Bash(curl *)` are [applied as managed policy](#applied-as-managed-policy) instead. |
| `disableBypassPermissionsMode` | Removes bypass permissions mode. The app stops offering the mode and starts a session that requests it in a stricter permission mode instead, independent of Claude Code managed-settings precedence. The key requires Claude Desktop 1.46388.1 or later. A separately deployed Claude Code managed-settings file that sets `permissions.disableBypassPermissionsMode` to `"disable"` removes the mode as well. |
| `skipWebFetchPreflight` | Turns off Claude Code's Web Fetch [domain check](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch) against `api.anthropic.com`. A separately deployed Claude Code managed-settings file that sets `skipWebFetchPreflight` takes precedence. |
| `managedMcpServers` | Makes the same managed MCP servers available in Code sessions. The app handles the connection and authentication; the Code session sees only the resulting tool list. |
| `mcpToolTimeoutSec` | Applies your per-call MCP tool timeout to Code sessions as well, taking precedence over a user-set `MCP_TOOL_TIMEOUT`. |
| `organizationInstructions` | Appended to the Code session's system prompt after Claude Code's own. `CLAUDE.md` instructions still apply. |
| `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes` | Routes Claude Code's OpenTelemetry metrics and logs to your collector. See [Telemetry](https://claude.com/docs/third-party/claude-desktop/telemetry.md). |
| `disableEssentialTelemetry`, `disableNonessentialTelemetry` | Disables Claude Code's crash reporting and usage telemetry to Anthropic, mirroring Cowork. |
| `disableAutoUpdates` | The embedded Claude Code engine never self-updates regardless of this key; its version is managed by the app's own updater. |
| `inferenceMaxTokensPerWindow`, `inferenceTokenWindowHours` | The token budget is shared across Cowork and Code sessions and enforced before each turn. |

[`mcpPersistentAlwaysAllowEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#mcppersistentalwaysallowenabled) also applies to Code sessions. When it's `false`, the approval prompt for an MCP tool offers **Allow for this session** in place of **Always allow**, and the approval isn't saved to Claude Code's settings files. Allow rules already in those files, and hooks, keep allowing the tool until someone removes them. For scheduled tasks, see [Tool approvals on scheduled tasks](https://claude.com/docs/third-party/claude-desktop/configuration.md#tool-approvals-on-scheduled-tasks).

### Applied as managed policy

These keys are translated into Claude Code [managed settings](https://code.claude.com/docs/en/settings#settings-files) and supplied to the session as policy. They take precedence over user and project settings, but they participate in Claude Code's managed-settings precedence if you have also deployed a separate Claude Code policy.

| Claude Desktop on 3P key | Claude Code policy it produces |
| - | - |
| `coworkEgressAllowedHosts` | A network sandbox restricted to your hosts, `allowManagedDomainsOnly`, and `WebFetch` allow rules for the same hosts, which [don't block other hosts](https://claude.com/docs/third-party/claude-desktop/web-tools.md#how-the-egress-allowlist-applies-in-code-sessions). Claude Code's own inference and telemetry connections run outside the sandbox. A shell command or [HTTP hook](https://code.claude.com/docs/en/hooks#http-hook-fields) that calls your inference provider, `api.anthropic.com`, or your OTLP collector needs that host in the list. |
| `allowedWorkspaceFolders` | A filesystem sandbox for shell commands, which can then create or change files only inside your allowed roots and the session's temporary locations. Those commands can still read files outside the roots, except where `blockReadsOutsideWorkingDirectories` or a [`Read(…)` rule](#file-path-rules-and-shell-commands) hides them. The roots are also passed as `additionalDirectories` at launch, which is always applied independent of managed-settings precedence, and the app keeps Claude's file tools inside the roots. The app also refuses to start a Code session outside an allowed root. |
| `blockReadsOutsideWorkingDirectories` | Claude Code's `permissions.blockReadsOutsideWorkingDirectories` for Code sessions. Claude's file tools refuse to read outside the working directories (the session's folder plus your allowed roots, if any) in every permission mode. Where the sandbox from `allowedWorkspaceFolders` or `coworkEgressAllowedHosts` is running, it also hides the user's home directory and similar locations, such as other users' home folders and mounted volumes, from shell commands, so a sandboxed command that reads there fails without a prompt. Without a running sandbox, a shell command that reads outside the working directories, or that Claude Code cannot analyze, asks the user for approval first, even in bypass permissions mode. The key requires Claude Desktop 1.46388.1 or later. The block takes effect only in sessions that run Claude Code v2.1.257 or later; if the app cannot install its current Claude Code engine and a session runs one older than v2.1.257 that is still on the device, that session runs without the block and the app logs a warning. |
| `managedMcpServers` | `strictPluginOnlyCustomization` set to `["mcp"]`, so the Code session does not load MCP servers that users define on Claude Code's side (`~/.claude.json`, a project's `.mcp.json`, or `claude mcp add`); your managed servers, which the app connects and supplies to the session itself, and MCP servers bundled in plugins still load. Per-tool [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers) values on each server are emitted as `permissions.deny` (for `blocked`) or `permissions.ask` (for `ask`) rules against the corresponding `mcp__<server>__<tool>` names. In local Code sessions and Code sessions on an SSH host, `allow` doesn't pre-approve the tool. |
| `isLocalDevMcpEnabled` | When `false` and `allowedPluginMcpServers` is unset, an `allowedMcpServers` list that admits only remote servers, with `allowManagedMcpServersOnly`, whether or not `managedMcpServers` is set. The Code session refuses local (stdio) servers bundled in plugins from marketplaces or that users install themselves, and local servers that users define on Claude Code's side (`~/.claude.json`, a project's `.mcp.json`, or `claude mcp add`). Those plugins' remote servers still connect. Your managed servers and the servers from the organization plugins directory, which the app connects and supplies to the session itself, aren't subject to the list. |
| `allowedPluginMcpServers` | `strictPluginOnlyCustomization` set to `["mcp"]` together with an `allowedMcpServers` list holding your entries and `allowManagedMcpServersOnly`, whether or not `managedMcpServers` is set. MCP servers bundled in plugins from marketplaces, or in plugins users install themselves, connect only when their URL matches an entry; no such plugin's local (stdio) server is admitted, and an empty list admits none. Your managed servers and the servers from the organization plugins directory still load. |
| `deniedPluginMcpServers` | The app sets a `deniedMcpServers` list holding your entries, whether or not `allowedPluginMcpServers` is set. When the key is unset or its list is empty, the app sets no `deniedMcpServers` list. When the value is not a list, or holds an entry that the app can't read, the app sets a list whose one entry is `*`, a pattern that matches every URL. See the [`deniedPluginMcpServers` reference](https://claude.com/docs/third-party/claude-desktop/configuration#deniedpluginmcpservers) for what the setting does and what an entry matches. |
| `userPluginMarketplacesEnabled` | When `false`, a `strictKnownMarketplaces` allowlist. See [Controlling user extensions](https://claude.com/docs/third-party/claude-desktop/extensions.md#controlling-user-extensions) for what the key does. |
| `builtinToolPolicy`, argument-scoped rules such as `Bash(curl *)` | A `permissions.ask` rule for each rule set to `"ask"`. |

The network and filesystem sandboxes apply on macOS, and on Linux devices and [SSH hosts](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#managed-configuration-on-the-remote-host) with Claude Code's [sandbox dependencies](https://code.claude.com/docs/en/sandboxing) installed. Claude Code doesn't sandbox shell commands on Windows devices, and on a Linux device or SSH host without the dependencies commands run unsandboxed. When `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset, Claude Desktop turns on neither sandbox. In all of these cases, `blockReadsOutsideWorkingDirectories` still confines Claude's file tools but can only ask the user to approve shell commands that read outside the working directories or that Claude Code can't verify. For what a remote session shows, see [Sandbox status on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#sandbox-status-on-the-remote-host).

> [!WARNING]
>
> Shell commands that run unsandboxed can reach hosts outside `coworkEgressAllowedHosts` and change files outside `allowedWorkspaceFolders`. Where the sandbox runs, a command that matches [`sandbox.excludedCommands`](https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands) in the user's own Claude Code settings also runs outside it, after Claude Code's regular permission flow. To keep Code off devices where the sandbox can't run, [turn off Code](#disabling-code) in the configuration you deploy to them. For SSH hosts, see [Sandbox status on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#sandbox-status-on-the-remote-host).

Under `blockReadsOutsideWorkingDirectories`, sandboxed shell commands can still read system locations such as `/usr`, the session's plugin and attachment folders (which become read-only), and the user's git configuration files (`~/.gitconfig` and the `config`, `ignore`, and `attributes` files under `~/.config/git`), which can themselves hold credentials such as tokens in remote URLs. Other files under the home folder outside the working directories are hidden from them, including `~/.ssh`, stored git credentials, included git configuration files, signing keys, and the target of a symlinked git configuration file, so git operations that need those files fail in the session until the user re-opens the paths. In a local session Claude also cannot read a file attached or `@`-mentioned from outside the working directories, so users should move such files into the session's folder or an allowed folder first.

An allowed root that is or contains the home directory, such as `~` or `/Users`, leaves the home directory readable, so list folders below it. The block guards against content a session reads steering Claude into the user's files, not against the user, who can re-open any path, up to their whole home folder, with `sandbox.filesystem.allowRead` (shell commands) or `permissions.additionalDirectories` (file tools and shell commands) in their own Claude Code settings, while a settings file tracked in a git repository cannot.

### File path rules and shell commands

A `Read(…)` rule in [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools) applies to Claude's file tools, and only in part to shell commands. Where [the sandbox that Claude Desktop turns on](#applied-as-managed-policy) runs, it hides a folder that the rule lists by its full path, such as `Read(//srv/keys/**)`. Elsewhere, some commands read a denied file without a prompt. Don't rely on the rule, `blockReadsOutsideWorkingDirectories`, or [the sandbox](https://code.claude.com/docs/en/sandboxing#what-runs-outside-the-sandbox) alone, and keep files that must stay secret where the user's OS account can't read them.

## Interaction with Claude Code's own managed settings

Claude Code can also be configured directly by deploying a [`managed-settings.json` file](https://code.claude.com/docs/en/settings#settings-files), an OS configuration profile for Claude Code, or, with the Claude API as the inference provider, [server-managed settings](https://code.claude.com/docs/en/server-managed-settings). If a Code session has any of these, Claude Code treats it as the administrator policy. By default, Claude Code then **ignores** the [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies, except in a Code session that gets [`code` settings from a Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab). The [Always applied](#always-applied) keys are unaffected.

In such a session, the gateway's `code` settings are the administrator policy, and `parentSettingsBehavior` defaults to `"merge"`. Set it in those `code` settings rather than rely on the default: `"merge"` to keep Claude Desktop's policy values, `"first-wins"` to drop them. To keep them, also set `"merge"` in the Claude Code managed settings on each device, because a session that starts without the gateway's `code` settings follows the device's settings instead.

To have Claude Desktop's restrictions apply on top of your Claude Code policy, set `parentSettingsBehavior` to `"merge"` in the Claude Code managed settings you deploy:

```json managed-settings.json theme={null}
{
  "parentSettingsBehavior": "merge"
}
```

With `"merge"`, Claude Desktop's policy values are layered under your Claude Code policy. Your values win any conflict, deny and allow lists are unioned, and Claude Desktop's values are filtered so they can only tighten policy, never loosen it. See [`parentSettingsBehavior`](https://code.claude.com/docs/en/settings-reference#parentsettingsbehavior) in the Claude Code settings reference. Requires Claude Code v2.1.133 or later, which ships with Claude Desktop on 3P.

With `"merge"`, two Claude Code policy keys weaken `blockReadsOutsideWorkingDirectories`. `sandbox.filesystem.allowManagedReadPathsOnly` limits the block to Claude's file tools, so a shell command that reads outside the working directories asks for approval instead of failing, and `allowManagedPermissionRulesOnly` removes the session's read access to its plugin and attachment folders, so skills that read their own files stop working. Leave both out of your Claude Code policy if you rely on the block.

> [!NOTE]
>
> With the [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) as the inference provider, Code sessions ask Anthropic for the server-managed settings of [the organization that owns the credential](https://code.claude.com/docs/en/server-managed-settings#platform-availability). This holds for an API key in your configuration, an API key from a credential helper, and **Sign in with Claude Console**. If that organization has server-managed settings, set [`parentSettingsBehavior`](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy) to `"merge"` in them to keep Claude Desktop's [policy values](#applied-as-managed-policy). While server-managed settings apply, Claude Code by default [ignores most keys](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources) in a file or OS profile on the device, and a `"merge"` set there has no effect.
>
> Without a Claude Code `managed-settings.json` file, OS profile, or server-managed settings, Claude Desktop's policy applies automatically and you don't need to set `parentSettingsBehavior`.

## Tune the Auto mode classifier

In [**Auto mode**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled), which Cowork shows as **Automatically approve**, a safety classifier reviews Claude's actions and blocks the ones it judges risky. To tell it what your organization trusts, or to add block and allow rules, deploy Claude Code's [`autoMode` settings](https://code.claude.com/docs/en/auto-mode-config) in [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) on each device. Check which of your sessions read those settings:

* **Cowork sessions** read the managed settings on the device, and never read [server-managed settings](https://code.claude.com/docs/en/server-managed-settings).
* **Local Code sessions** read the managed settings on the device too, unless server-managed settings or [a Claude apps gateway's `code` settings](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab) [take priority](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources). They also read `autoMode` entries from the user's own `~/.claude/settings.json`, which Cowork sessions don't read.
* **For Code sessions on an SSH host**, see [Managed configuration on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#managed-configuration-on-the-remote-host).

For example, on a device with no other Claude Code managed settings, deploy this file to describe an internal service and add one allow rule:

```json managed-settings.json theme={null}
{
  "parentSettingsBehavior": "merge",
  "autoMode": {
    "environment": [
      "$defaults",
      "Key internal services: the ticket tracker at tickets.example.corp"
    ],
    "allow": [
      "$defaults",
      "Creating and updating tickets in the ticket tracker is allowed: routine support work"
    ]
  }
}
```

* **Start each list with `"$defaults"`** to keep the built-in rules. Without it, a list can [replace its built-in rules](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules), the block lists included.
* **Don't rely on leaving `"$defaults"` out to remove built-in rules.** In local Code sessions, Claude Code combines your lists with Claude Desktop's own `environment`, `allow`, and `soft_deny` lists, which start with `"$defaults"`. A `hard_deny` list without it can replace the built-in `hard_deny` rules.
* **Keep `parentSettingsBehavior`.** Without it, Claude Code ignores the [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies to Cowork and Code sessions, except [in a Code session that gets `code` settings from a Claude apps gateway](#interaction-with-claude-code%E2%80%99s-own-managed-settings). For example, without it, Claude doesn't ask for approval in Cowork's **Automatically approve** before calling a connector tool whose [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers) is `"ask"`, and the classifier reviews the call.
* **Deploy to [Claude Code's policy locations](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy)**, not to [Claude Desktop's configuration locations](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device). In a macOS configuration profile for Claude Code, use the same keys as in `managed-settings.json`, with nested settings as dictionaries and lists as arrays. In a Windows registry policy, put the file's JSON in the `Settings` value under `HKLM\SOFTWARE\Policies\ClaudeCode`.
* **If the device already has a Claude Code managed-settings file, profile, or `HKLM` registry policy, add the `autoMode` block to it.** By default, Claude Code [reads most keys from one managed source](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources), so a second source is either ignored or hides the first.

On a device that has the Claude Code CLI, run `claude auto-mode config` in a terminal to check that the CLI reads your entries. It lists your entries among the built-in rules, and any from the user's `~/.claude/settings.json`. It doesn't list the entries that Claude Desktop adds to local Code sessions.

### Run vetted connector tools without classifier review

In Cowork's [**Automatically approve**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled), the safety classifier reviews calls to a connector tool whose [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers) in `managedMcpServers` is `"allow"`, and can block them. To run a tool without that review, add a `permissions.allow` rule for it to your Claude Code managed settings, beside any `autoMode` block:

```json managed-settings.json theme={null}
{
  "parentSettingsBehavior": "merge",
  "permissions": {
    "allow": ["mcp__tickets__create_ticket"]
  }
}
```

Write the rule as [`mcp__<server>__<tool>`](https://code.claude.com/docs/en/permissions#mcp), from the `name` of the server's `managedMcpServers` entry and the tool's name. In both names, replace each character that isn't an ASCII letter or digit, `_`, or `-` with `_`. For example, a server named `Ticket Tracker` becomes `Ticket_Tracker`. The rule doesn't cover the server's other tools.

> [!WARNING]
>
> Claude runs a connector tool named in `permissions.allow` with no classifier review, whatever the call's arguments and even if the server marks the tool as destructive. A `permissions.ask` or `permissions.deny` rule for the same tool still applies. Without `parentSettingsBehavior` set to `"merge"`, Claude Code ignores a `toolPolicy` of `"ask"` for that tool, except [in a Code session that gets `code` settings from a Claude apps gateway](#interaction-with-claude-code%E2%80%99s-own-managed-settings).
>
> List only tools that you would let run unattended, and leave destructive ones out. The rule matches by name. If a user's own MCP server, such as a local MCP server that the user adds to Claude Desktop, has the same server name, the rule also covers a tool of the same name on it.

## Claude Code mods

Code sessions support Claude Code [mods](https://code.claude.com/docs/en/plugins/mods/overview), code that a plugin runs inside Claude Code, and users can load their own. Cowork sessions and [Chat](https://claude.com/docs/third-party/claude-desktop/chat.md) conversations load mods from plugins users add themselves and [plugins from your marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin). To stop users' own mods from loading in local Code sessions, Cowork sessions, and Chat conversations, deploy this Claude Code managed-settings file on each device:

```json managed-settings.json theme={null}
{
  "parentSettingsBehavior": "merge",
  "pluginConfigs": {
    "cc-plugin-sec-default@builtin": {
      "options": {
        "allowManagedModsOnly": true
      }
    }
  }
}
```

In Cowork sessions and Chat conversations, this file also stops mods in plugins from your marketplaces.

* **Keep `parentSettingsBehavior`.** Without it, Claude Code ignores the sandbox and the other [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies, except [in a Code session that gets `code` settings from a Claude apps gateway](#interaction-with-claude-code%E2%80%99s-own-managed-settings). In Cowork sessions, without it, Claude doesn't ask for approval before a tool call that matches an argument-scoped [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy) rule such as `Read(//**/.env)` set to `"ask"`.
* **Leave out `disableSideloadFlags`**, which a longer sample in the Claude Code docs includes. With it, Code sessions start without the skills and organization plugins that Claude Desktop delivers.
* **Optionally, remove the `/plugin-authoring` command**, which has Claude write a mod. Add `"enabledPlugins": { "cc-plugin-plugin-authoring@builtin": false }` to the file.

[Manage mods for your organization](https://code.claude.com/docs/en/plugins/mods/admin) covers the other controls. For sessions on an SSH host, see [Managed configuration on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#managed-configuration-on-the-remote-host).

## Remote sessions over SSH

A Code session can run its Claude Code engine on a remote host over SSH while the session's interface stays in Claude Desktop on the user's device. In a 3P deployment this is off until you set [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist), because the app forwards the session's inference credential to the host. [SSH remote sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md) lists the credential kinds that work on a remote host and which of the keys above apply there.

## Further reading

* [Claude Code settings reference](https://code.claude.com/docs/en/settings-reference)
* [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)
* [Settings precedence](https://code.claude.com/docs/en/settings#settings-precedence)

## Disabling Code

To turn off Code, set `isClaudeCodeForDesktopEnabled` to `false` in your Claude Desktop on 3P configuration. Users can no longer open Code. Cowork is unaffected, and so is [Chat](https://claude.com/docs/third-party/claude-desktop/chat.md#configuration) if you have enabled it.

With Code off, Claude can't use a remote MCP server that requires OAuth sign-in if a marketplace plugin or a user-added plugin bundles it. With Code on, Claude can use such a server in local Code sessions that load the plugin, once the user has signed in, but still not in Cowork sessions or Chat conversations. To make it available in Cowork sessions and Chat conversations, with Code on or off, add a `managedMcpServers` entry with the same `url`, as described under [Remote MCP servers in plugins](https://claude.com/docs/third-party/claude-desktop/extensions.md#remote-mcp-servers-in-plugins).

If you set `desktopHome` to `off`, keep Code on. For what `desktopHome` does, see [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md).
