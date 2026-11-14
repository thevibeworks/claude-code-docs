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
| `inferenceProvider` and all provider credential keys (`inferenceGateway*`, `inferenceAnthropicApiKey`, `inferenceVertex*`, `inferenceBedrock*`, `inferenceFoundry*`, `inferenceCredentialHelper*`) | Selects the inference backend and supplies credentials. Code sessions use the same provider and endpoint as Cowork sessions, and the same credentials unless [your organization's launcher](#start-code-sessions-through-a-corporate-launcher) starts them. |
| `inferenceModels` | Populates the model picker. The first entry is the default for new Code sessions. |
| `autoModeEnabled` | Controls **Auto mode**, which needs a [model that supports it](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). When the key isn't set, Code sessions offer **Auto mode** and new sessions start in it unless the user has already chosen another mode or a Claude Code `permissions.defaultMode` applies. Set it to `false` to remove **Auto mode** from Code and Cowork. Set it to `true` to also offer the mode in Cowork, where it appears as **Automatically approve**. In Code sessions, a separately deployed Claude Code [managed-settings file](#interaction-with-claude-code%E2%80%99s-own-managed-settings) that sets `disableAutoMode` to `"disable"` also keeps **Auto mode** hidden, whatever this key is set to. To change what **Auto mode** allows and blocks, see [Tune the Auto mode classifier](#tune-the-auto-mode-classifier). To have the model provider review actions on a gateway deployment, see [Auto mode checks](https://claude.com/docs/third-party/claude-desktop/gateway.md#auto-mode-checks). |
| `autoModeClassifierModel` | Sets the model for Claude Code's built-in safety check in **Auto mode**. See [Choose the Auto mode classifier model](#choose-the-auto-mode-classifier-model). |
| `scheduledTasksEnabled` | When `false`, the routines list in Code is hidden and Code sessions start without Claude Code's in-session scheduling tools, so the `/loop` command cannot schedule recurring work. Cowork's scheduled tasks are turned off by the same key. |
| `disabledBuiltinTools` | Removes the listed tools from Code sessions. A `Read(…)` rule applies to Claude's file tools, and [only in part to shell commands](#file-path-rules-and-shell-commands). Tools your provider doesn't support, such as WebSearch on Amazon Bedrock, are removed automatically in addition to your list. To stop Claude from starting nested sessions (separate sessions for a task), add `mcp__ccd_session__start_session` and `mcp__ccd_session__hand_off_to_session`. Claude then can't start a nested session, even at a user's request or from inside one. In the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#set-up-a-device-without-mdm) or the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#start-from-an-existing-configuration-file), where the tool picker doesn't list these names, import your full configuration as JSON with the names added. Otherwise, add them to your MDM profile or bootstrap server's response. |
| `builtinToolPolicy` | Tools set to `"ask"` require approval on each call in Code sessions. Argument-scoped rules such as `Bash(curl *)` are [applied as managed policy](#applied-as-managed-policy) instead. |
| `disableBypassPermissionsMode` | Removes bypass permissions mode. The app stops offering the mode and starts a session that requests it in a stricter permission mode instead, independent of Claude Code managed-settings precedence. The key requires Claude Desktop 1.46388.1 or later. A separately deployed Claude Code managed-settings file that sets `permissions.disableBypassPermissionsMode` to `"disable"` removes the mode as well. |
| `skipWebFetchPreflight` | Turns off Claude Code's Web Fetch [domain check](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch) against `api.anthropic.com`. A separately deployed Claude Code managed-settings file that sets `skipWebFetchPreflight` takes precedence. |
| `managedMcpServers` | Makes the same managed MCP servers available in Code sessions. The app handles the connection and authentication; the Code session sees only the resulting tool list. |
| `mcpToolTimeoutSec` | Applies your per-call MCP tool timeout to Code sessions as well, taking precedence over a user-set `MCP_TOOL_TIMEOUT`. |
| `organizationInstructions` | Appended to the Code session's system prompt after Claude Code's own. `CLAUDE.md` instructions still apply. |
| `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes` | Routes Claude Code's OpenTelemetry metrics and logs to your collector. See [Telemetry](https://claude.com/docs/third-party/claude-desktop/telemetry.md). |
| `disableEssentialTelemetry`, `disableNonessentialTelemetry` | Disables Claude Code's crash reporting and usage telemetry to Anthropic, mirroring Cowork. |
| `disableAutoUpdates` | The embedded Claude Code engine never self-updates regardless of this key; its version is managed by the app's own updater. |
| `inferenceMaxTokensPerWindow`, `inferenceTokenWindowHours` | The token budget is shared across Chat conversations, Cowork sessions, and Code sessions, and enforced before each turn. Tokens from [subagents](https://code.claude.com/docs/en/sub-agents) and [conversation compaction](https://claude.com/docs/third-party/claude-desktop/gateway.md#context-window-and-compaction) count toward it in Claude Desktop 5.1231.0 or later. |

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

The network and filesystem sandboxes apply on macOS, and on Linux devices and [SSH hosts](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#managed-configuration-on-the-remote-host) with Claude Code's [sandbox dependencies](https://code.claude.com/docs/en/sandboxing) installed. Claude Code doesn't sandbox shell commands on Windows devices, and on a Linux device or SSH host without the dependencies commands run unsandboxed. When `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset, Claude Desktop turns on neither sandbox. In all of these cases, `blockReadsOutsideWorkingDirectories` still confines Claude's file tools but can only ask the user to approve shell commands that read outside the working directories or that Claude Code can't verify. On a device whose only configuration is the local configuration file, an unset `coworkEgressAllowedHosts` can also leave both sandboxes off. See [Unset allowlist in Code sessions](https://claude.com/docs/third-party/claude-desktop/web-tools.md#unset-allowlist-in-code-sessions). For what a remote session shows, see [Sandbox status on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#sandbox-status-on-the-remote-host).

> [!WARNING]
>
> Shell commands that run unsandboxed can reach hosts outside `coworkEgressAllowedHosts` and change files outside `allowedWorkspaceFolders`. Where the sandbox runs, a command that matches [`sandbox.excludedCommands`](https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands) in the user's own Claude Code settings also runs outside it, after Claude Code's regular permission flow. To keep Code off devices where the sandbox can't run, [turn off Code](#disabling-code) in the configuration you deploy to them. For SSH hosts, see [Sandbox status on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#sandbox-status-on-the-remote-host).
>
> Even where the sandbox runs, [hooks that run a command](https://code.claude.com/docs/en/hooks#hook-handler-fields), local (stdio) MCP servers, and [Claude Code mods](#claude-code-mods) run outside it, and so do the [other processes that Claude Code starts](https://code.claude.com/docs/en/sandboxing#what-runs-outside-the-sandbox). All of these can reach hosts outside `coworkEgressAllowedHosts`, change files outside `allowedWorkspaceFolders`, and read files that `blockReadsOutsideWorkingDirectories` hides from shell commands. To limit which hooks, local MCP servers, and mods run, follow [Turn off user hooks](https://claude.com/docs/third-party/claude-desktop/extensions.md#turn-off-user-hooks) and [Stop user-installed mods from loading](#stop-user-installed-mods-from-loading), and set [`isLocalDevMcpEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled) to `false`.

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

With `"merge"`, Claude Desktop's policy values are layered under your Claude Code policy. For how Claude Code combines the two policies, see [Let an embedding host add policy](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy) in the Claude Code documentation. Requires Claude Code v2.1.133 or later, which ships with Claude Desktop on 3P.

With `"merge"`, two Claude Code policy keys weaken `blockReadsOutsideWorkingDirectories`. `sandbox.filesystem.allowManagedReadPathsOnly` limits the block to Claude's file tools, so a shell command that reads outside the working directories asks for approval instead of failing, and `allowManagedPermissionRulesOnly` removes the session's read access to its plugin and attachment folders, so skills that read their own files stop working. Leave both out of your Claude Code policy if you rely on the block.

> [!NOTE]
>
> With the [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) as the inference provider, Code sessions ask Anthropic for the server-managed settings of [the organization that owns the credential](https://code.claude.com/docs/en/server-managed-settings#platform-availability). This holds for an API key in your configuration, an API key from a credential helper, and **Sign in with Claude Console**. If that organization has server-managed settings, set [`parentSettingsBehavior`](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy) to `"merge"` in them to keep Claude Desktop's [policy values](#applied-as-managed-policy). While server-managed settings apply, Claude Code by default [ignores most keys](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources) in a file or OS profile on the device, and a `"merge"` set there has no effect.
>
> Without a Claude Code `managed-settings.json` file, OS profile, or server-managed settings, Claude Desktop's policy applies automatically and you don't need to set `parentSettingsBehavior`.

### Start Code sessions through a corporate launcher

If your organization starts Claude Code through a [corporate launcher](https://code.claude.com/docs/en/corporate-launcher), Code sessions in Claude Desktop can go through it too. This takes two settings:

1. In Claude Desktop's configuration, set [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudecodeprocesswrapperenabled) to `true`. Without it, Claude Desktop starts Claude Code directly.
2. In Claude Code's managed settings, name the launcher with `processWrapper`, or with `CLAUDE_CODE_PROCESS_WRAPPER` in the `env` block. If these are the first Claude Code managed settings on the device or host, also set `parentSettingsBehavior` to `"merge"` in them, or Claude Code ignores the [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies.

Name the launcher where the session runs:

* **On a macOS or Linux device**: in that device's Claude Code managed settings, not in server-managed settings or the user's own settings
* **On a macOS or Linux host over SSH**, from any device, Windows included: in the host's Claude Code `managed-settings.json` file or `managed-settings.d` folder, not in a configuration profile
* **On a Windows device itself, in WSL, and on a Windows host over SSH**: sessions start without a launcher

Code sessions still use the provider and endpoint in Claude Desktop's configuration, but Claude Desktop passes no inference credential and no [`inferenceCustomHeaders`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecustomheaders) to Claude Code when the launcher starts it. The launcher must set a credential in Claude Code's environment, such as `ANTHROPIC_AUTH_TOKEN` for a gateway or the variable that your provider's credential uses. It must also pass on the `ANTHROPIC_BASE_URL` that it receives, or set your gateway's address in its place. With no credential, the session still starts, and each reply fails with a message that Claude Code has no working credentials. Cowork, the connection test, and session titles don't go through the launcher. They use the credential in Claude Desktop's configuration, so a passing connection test doesn't show that the launcher supplies one.

A session doesn't start if Claude Desktop can't use the launcher you named: for example, if the file is missing or isn't executable, or the value doesn't follow Claude Code's [launcher value format](https://code.claude.com/docs/en/corporate-launcher#format-of-the-launcher-value).

To keep users from turning the launcher off, set `claudeCodeProcessWrapperEnabled` in the device's [managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#devices-with-a-managed-profile), which users can't change. The key is an [app-behavior key](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), so add every other app-behavior key you use, such as the update keys, to the same profile. If the profile sets any other kind of key, also [keep the device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

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
* **Don't rely on leaving `"$defaults"` out to remove built-in rules.** In Cowork sessions and local Code sessions, Claude Code combines your lists with the `environment`, `allow`, and `soft_deny` lists that Claude Desktop sends, which start with `"$defaults"`. If your `allow` list has entries but not `"$defaults"`, Claude Desktop's list doesn't restore the built-in `allow` rules, and Claude Desktop's own `allow` entries still apply. A `hard_deny` list without `"$defaults"` can replace the built-in `hard_deny` rules.
* **Keep `parentSettingsBehavior`.** Without it, Claude Code ignores the [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies to Cowork and Code sessions, except [in a Code session that gets `code` settings from a Claude apps gateway](#interaction-with-claude-code%E2%80%99s-own-managed-settings).
* **Deploy to [Claude Code's policy locations](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy)**, not to [Claude Desktop's configuration locations](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device). In a macOS configuration profile for Claude Code, use the same keys as in `managed-settings.json`, with nested settings as dictionaries and lists as arrays. In a Windows registry policy, put the file's JSON in the `Settings` value under `HKLM\SOFTWARE\Policies\ClaudeCode`.
* **If the device already has a Claude Code managed-settings file, profile, or `HKLM` registry policy, add the `autoMode` block to it.** By default, Claude Code [reads most keys from one managed source](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources), so a second source is either ignored or hides the first.

On a device that has the Claude Code CLI, run `claude auto-mode config` in a terminal to check that the CLI reads your entries. It lists your entries among the built-in rules, and any from the user's `~/.claude/settings.json`. It doesn't list the entries that Claude Desktop adds to Cowork sessions and local Code sessions.

### Choose the Auto mode classifier model

In [**Auto mode**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled), which Cowork shows as **Automatically approve**, a safety classifier reviews Claude's actions. Except [on a gateway](https://claude.com/docs/third-party/claude-desktop/gateway.md#auto-mode-checks), sessions [ask your model provider for a review first](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review), and Claude Code's built-in safety check takes over when the provider doesn't review the session. The built-in safety check uses Claude Sonnet 5 by default, and [some sessions use a different model](https://code.claude.com/docs/en/permission-modes#default-classifier-model). The model you choose for it doesn't affect your provider's reviews.

Requires Claude Desktop 5.11492.0 or later. To choose the model for Cowork and Code sessions, set [`autoModeClassifierModel`](https://claude.com/docs/third-party/claude-desktop/configuration#automodeclassifiermodel) where your devices [get their configuration](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device):

* **MDM profile**: add the key
* **Bootstrap server**: return the key in the response
* **[In-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md)**: enter the model's ID in the **Auto mode classifier model** field under **Capabilities**
* **[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configure-claude-desktop)**: open **Organization settings**, go to the **Capabilities** page under **Desktop 3P**, enter the model's ID in the **Auto mode classifier model** field, and click **Save changes**. A device on the [console's configuration](https://claude.com/docs/third-party/claude-desktop/admin-console.md#which-settings-apply-on-a-device-with-a-managed-profile) ignores the key from the other sources.

This example sets Claude Sonnet 4.6. Replace the IDs with your provider's:

```json theme={null}
{
  "inferenceModels": ["claude-sonnet-5", "claude-sonnet-4-6"],
  "autoModeClassifierModel": "claude-sonnet-4-6"
}
```

* **Use [your provider's ID](https://claude.com/docs/third-party/claude-desktop/models.md#model-list-and-default-model) for an Anthropic model that it serves.** Claude Desktop ignores a value that it can tell is something else, such as the Claude API's ID on Amazon Bedrock. If the provider refuses the ID, every action that the built-in safety check reviews is [blocked](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action).
* **If you set [`inferenceModels`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodels), also list the ID there and in any [permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies) that narrows the model list.** A model that isn't listed doesn't take effect.
* **Don't use Claude Opus 5, Sonnet 5.5, or Opus 5.5.** These models [can't do the review](https://code.claude.com/docs/en/permission-modes#classifier-model-not-reviewing).
* **A weaker model may allow actions that the default would block**

Set `autoModeClassifierModel` even if your devices already set [`CLAUDE_CODE_AUTO_MODE_MODEL`](https://code.claude.com/docs/en/permission-modes#choose-the-classifier-model), Claude Code's environment variable for this model:

* **In [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) on the device, or in a user's `~/.claude/settings.json`**: Cowork and Code sessions ignore the value
* **In a user's shell profile, the device's environment variables, or [the variables that a user saves in Code](https://code.claude.com/docs/en/desktop#environment-variables-in-local-sessions)**: Cowork and Code sessions ignore the value. Before Claude Desktop 5.11492.0, Code sessions could use it.

Confirm the change on one device:

1. Quit and reopen Claude Desktop
2. Start a session in **Auto mode** on a model other than the one you set
3. Have Claude call a connector tool
4. Check your provider's or gateway's logs for requests to the model you set

If these requests don't appear, see [When your model doesn't review](https://code.claude.com/docs/en/permission-modes#classifier-model-not-reviewing).

### Run vetted connector tools without classifier review

In Cowork's [**Automatically approve**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled), the safety classifier reviews Claude's calls to a connector tool whose [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers) in `managedMcpServers` is `"allow"`, and can block them. To run a tool without that review, add a `permissions.allow` rule for it to your Claude Code managed settings, beside any `autoMode` block:

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
> Claude runs a connector tool named in `permissions.allow` with no classifier review, whatever the call's arguments and even if the server marks the tool as destructive. A `permissions.ask` or `permissions.deny` rule for the same tool still applies. Keep `parentSettingsBehavior` set to `"merge"` in that file, so that a `toolPolicy` of `"ask"` for the tool goes on asking.
>
> List only tools that you would let run unattended, and leave destructive ones out. The rule matches by name. If a user's own MCP server, such as a local MCP server that the user adds to Claude Desktop, has the same server name, the rule also covers a tool of the same name on it.

## Claude Code mods

Code sessions support Claude Code [mods](https://code.claude.com/docs/en/plugins/mods/overview), code that a plugin runs inside Claude Code, and users can load their own. Cowork sessions and [Chat](https://claude.com/docs/third-party/claude-desktop/chat.md) conversations load mods from plugins users add themselves and [plugins from your marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin).

### What a mod can do without approval

A [mod](https://code.claude.com/docs/en/plugins/mods/overview) is code that a plugin runs inside Claude Code. That code runs as the user, [outside the sandbox](https://code.claude.com/docs/en/sandboxing#what-runs-outside-the-sandbox). It can read and write files, run programs, and make network requests itself, and your tool policies don't apply to those actions. For example, in a Code session it can reach hosts that aren't in [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts).

A mod can also call the session's tools, such as the shell tool (`Bash`) or a connector tool. Claude Code doesn't ask the user to approve a call that a mod makes, and treats the call according to your policy for the tool:

* **No policy**: the mod's call can run with no prompt
* **`"allow"`** in [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers): the mod's call can run with no prompt, even in Code sessions, where `"allow"` doesn't pre-approve Claude's own calls
* **`"ask"`** in `toolPolicy`: under the `permissions.ask` rule that [Claude Desktop supplies](#applied-as-managed-policy), Claude Code refuses the mod's call, and the user sees no prompt. In a Code session, the same holds for a built-in tool set to `"ask"` in [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy). Claude's own calls to the tool still prompt the user each time.
* **Blocked**, by `"blocked"` in `toolPolicy` or by the tool's name in [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools): a mod can't call the tool

Claude Code's own managed settings can [replace the policy](#interaction-with-claude-code%E2%80%99s-own-managed-settings) that holds the `permissions.ask` rule. For a tool that a mod must never call, block the tool, which removes it from the session.

In **Auto mode** and in Cowork's **Automatically approve**, the safety classifier doesn't review a mod's calls, so your [`autoMode` rules](#tune-the-auto-mode-classifier) don't apply to them.

### Stop user-installed mods from loading

To stop users' own mods from loading in local Code sessions, Cowork sessions, and Chat conversations, deploy this Claude Code managed-settings file on each device:

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

* **Deploy it to [Claude Code's policy locations](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy)**, not to [Claude Desktop's configuration locations](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device). If the device already has Claude Code managed settings, such as an [`autoMode` block](#tune-the-auto-mode-classifier), add these keys to them and leave their `parentSettingsBehavior` as it is.
* **Keep `parentSettingsBehavior`.** Without it, Claude Code ignores the sandbox and the other [managed policy](#applied-as-managed-policy) values that Claude Desktop supplies, except [in a Code session that gets `code` settings from a Claude apps gateway](#interaction-with-claude-code%E2%80%99s-own-managed-settings). In Cowork sessions, without it, Claude doesn't ask for approval before a tool call that matches an argument-scoped [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy) rule such as `Read(//**/.env)` set to `"ask"`.
* **Leave out `disableSideloadFlags`**, which a longer sample in the Claude Code docs includes. With it, Code sessions start without the skills, organization plugins, and uploaded plugins that Claude Desktop delivers.
* **Optionally, remove the `/plugin-authoring` command**, which has Claude write a mod. Add `"enabledPlugins": { "cc-plugin-plugin-authoring@builtin": false }` to the file.

[Manage mods for your organization](https://code.claude.com/docs/en/plugins/mods/admin) covers the other controls. For sessions on an SSH host, see [Managed configuration on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#managed-configuration-on-the-remote-host).

## Remote sessions over SSH

A Code session can run its Claude Code engine on a remote host over SSH while the session's interface stays in Claude Desktop on the user's device. In a 3P deployment this is off until you set [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist), because the app forwards the session's inference credential to the host. It forwards none where [a launcher on the host](#start-code-sessions-through-a-corporate-launcher) starts Claude Code. [SSH remote sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md) lists the credential kinds that work on a remote host and which keys apply there.

## Disabling Code

To turn off Code, set `isClaudeCodeForDesktopEnabled` to `false` in your Claude Desktop on 3P configuration. Users can no longer open Code. Cowork is unaffected, and so is [Chat](https://claude.com/docs/third-party/claude-desktop/chat.md#configuration).

If you set `desktopHome` to `off`, keep Code on. For what `desktopHome` does, see [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md).
