> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH remote sessions in Claude Desktop on 3P

> How Code sessions run on a remote host over SSH in Claude Desktop on 3P, the sshHostAllowlist key that enables them, which inference credentials work on a remote host, and what to check before turning them on

An SSH remote session is a [Code](/docs/third-party/claude-desktop/code) session whose Claude Code engine runs on another machine that the user reaches over SSH, while the session's interface stays in Claude Desktop on the user's device. Claude Desktop connects to the host, places the engine there, and starts the session with the inference credential and policy from your managed configuration. Users can work on code that lives on a development server, a build box, or a cloud workstation without copying it to their device. In Claude Desktop on third-party (3P), SSH remote sessions are off until you set the [`sshHostAllowlist`](/docs/third-party/claude-desktop/configuration#sshhostallowlist) key, because enabling them sends your inference credential to the hosts users connect to.

> [!NOTE]
>
> SSH remote sessions are in beta in Claude Desktop on 3P and require Claude Desktop 1.40609.0 or later. The in-app configuration window marks `sshHostAllowlist` with a **Beta** pill.

## How a remote session works

1. **Connect.** The user picks an SSH host from the environment picker in Code, or adds one by entering its address, port, and an identity file. Claude Desktop connects through the device's OpenSSH client on macOS and Linux, or its built-in SSH client on Windows (see [Host requirements](#host-requirements) to change either default), applies the host's entry from the device's `~/.ssh/config` (see [SSH configuration on the device](#ssh-configuration-on-the-device)), and prompts in the app if the host asks for a password or a one-time code.
2. **Deploy.** Claude Desktop places a remote server and the Claude Code engine under `~/.claude/remote/` in the SSH user's home directory on the host ([Host requirements](#host-requirements) lists every path) and reuses them on later connections.
3. **Run.** The remote server starts the engine on the host with the inference credential and policy from your managed configuration. Every file read, edit, shell command, and git operation runs on the host, in the working directory the user chose there. Claude Desktop connects to [managed MCP servers](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin) from the device and exposes them to the engine as tools.
4. **Stream.** Claude's responses and tool output stream back to Claude Desktop. Permission prompts appear in Claude Desktop, and the engine waits on the host until the user answers.

The engine keeps running on the host through a dropped SSH link, device sleep, or the user quitting Claude Desktop. It finishes the current turn, or stops at a permission prompt, then idles until the user reopens the session. While Claude Desktop is closed, no new turns run and the inference credential is not refreshed, so a turn that outlives the credential fails with an authentication error. A restart of the app for an update counts as a quit.

When the user reopens the session after a quit, Claude Desktop rejoins the engine or replaces it, unless it refuses to start the session:

* **Rejoins**: on a macOS or Linux device, Claude Desktop 2.42304.0 or later tries to rejoin an engine that 2.42304.0 or later started. If it rejoins, a turn still running goes on. It can fail to rejoin, for example after some Claude Desktop updates or after a change to the managed configuration since the engine started. After a quit it never rejoins on a Windows device, and never rejoins an engine that an earlier version started.
* **Replaces**: otherwise, Claude Desktop ends the engine and starts a fresh one from the transcript stored on the host. A turn that finished while the app was closed is shown in full, and a turn that still runs is cut short. If the turn stays stopped, the user sends a message to continue it.

On a host that ends a user's processes at logout, the remote server and the engine end with the SSH connection that started them, so a turn in progress doesn't survive a disconnect. Linux hosts where systemd-logind's `KillUserProcesses` setting is `yes` and applies to the SSH user behave this way. To keep remote sessions running through a disconnect on such a host, ask the host's administrator to exempt the SSH user, for example by listing the user under `KillExcludeUsers` in the systemd-logind configuration.

An idle engine stays on the host, with the credential in its environment, until one of these happens:

* The user archives or deletes the session.
* The user reopens the session and Claude Desktop ends the engine to start a fresh one.
* The host restarts.
* After an update that includes a new remote server, Claude Desktop replaces the host's remote server at a later connection. This ends the engines under the old server. Claude Desktop can put the replacement off while it believes that work is running on that host.
* On a Linux or macOS host, 30 days pass without a connection from Claude Desktop to the remote server. The remote server then stops and ends its engines. Requires Claude Desktop 1.52386.0 or later.
* Someone ends the engine's process on the host. To list or end the engines and the remote server yourself on a Linux or macOS host, see [Files and processes on the remote machine](https://code.claude.com/docs/en/desktop#files-and-processes-on-the-remote-machine). There the engine is called Claude Code, and the remote server the helper.

While Claude Desktop is disconnected, the remote server keeps the most recent output of each running engine in a 16 MiB buffer. It drops older output, and the engine keeps running.

On a Linux or macOS host, if Claude Desktop stayed open, it rejoins the running engine when it reconnects after device sleep or a dropped SSH link. It catches up from the buffer, and loads the part of the conversation that the buffer has dropped from the transcript stored on the host. If it can't load all of it, the session shows "Some output produced while you were disconnected may be missing here."

Some tool calls wait for an answer from Claude Desktop, and fail while it is disconnected:

* **File tools under a folder restriction**: if you set [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), Claude Desktop checks each file read, search, and edit before it happens. While Claude Desktop is disconnected, each of these calls waits up to 10 minutes and then fails.
* **Tools that your policy sets to ask**: if [`builtinToolPolicy`](/docs/third-party/claude-desktop/configuration#builtintoolpolicy) sets a bare tool name, such as `Bash`, to `ask`, Claude Desktop is consulted before each call to that tool. While Claude Desktop is disconnected, each call waits up to 10 minutes and then fails.
* **Tools from MCP servers that run on the device**: these include your managed MCP servers (see [Where MCP servers run in a remote session](#where-mcp-servers-run-in-a-remote-session)). While Claude Desktop is disconnected, each call to one of their tools fails after about 30 seconds. The 30-second limit requires Claude Desktop 2.2553.0 or later.

For a task that uses these tools, have the user keep the device awake and connected. For other limits, see [Limits while Desktop is disconnected](https://code.claude.com/docs/en/desktop#limits-while-desktop-is-disconnected).

### Account that a remote session runs under

On a Linux or macOS host, the remote server and the engine run as the SSH user. Installing and starting them takes no `sudo`. The shell commands and [MCP servers](#where-mcp-servers-run-in-a-remote-session) that the engine starts there also start as the SSH user. Review the SSH user's rights on the host, `sudo` rules included, as you would for a person who runs commands there.

### Alert the user with hooks on the host

A [hook](https://code.claude.com/docs/en/hooks) is a command of yours that the engine runs on the host at a set point in a session. With hooks, the host can tell the user that a turn is waiting at a permission prompt, has finished, or has failed with an API error, including while Claude Desktop is disconnected. To set them up, add this `hooks` key to `~/.claude/settings.json` in the SSH user's home directory on the host before the user starts the session.

```json ~/.claude/settings.json theme={null}
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [{ "type": "command", "command": "/path/to/alert-user.sh" }]
      }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "/path/to/alert-user.sh" }] }
    ],
    "StopFailure": [
      { "hooks": [{ "type": "command", "command": "/path/to/alert-user.sh" }] }
    ]
  }
}
```

Replace `/path/to/alert-user.sh` with a script that you write and place on the host, for example one that posts to a messaging service that the host can reach. The engine runs the script as the SSH user and passes it the event as JSON on standard input, with fields such as `hook_event_name`, `session_id`, and `cwd`. The `Stop` event also carries Claude's last message, so forward only the fields that the alert needs.

Have the script print nothing and exit with code 0, because a `Stop` hook's output and exit code can keep the turn going (see [Stop decision control](https://code.claude.com/docs/en/hooks#stop-decision-control)). To confirm the setup, have the user start a remote session on the host and send a message. The script runs when Claude finishes responding.

The hooks run in these cases:

* **A permission prompt waits for the user's answer**: the [`Notification`](https://code.claude.com/docs/en/hooks#notification) hook runs once the prompt has waited about six seconds
* **Claude finishes responding**: the [`Stop`](https://code.claude.com/docs/en/hooks#stop) hook runs
* **An API error, such as an authentication error, ends the turn**: the [`StopFailure`](https://code.claude.com/docs/en/hooks#stopfailure) hook runs in place of `Stop`

The `Notification` hook doesn't run for a tool call that is waiting for Claude Desktop's own check. That check comes before any permission prompt for the call. Calls that wait for that check include these:

* Each file read, search, and edit, if you set [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders)
* Each call to a tool that [`builtinToolPolicy`](/docs/third-party/claude-desktop/configuration#builtintoolpolicy) sets to `ask` by its bare name, such as `Bash`
* Each call to a tool from an MCP server that runs on the device

While Claude Desktop is disconnected, each of these calls waits and then fails, after up to 10 minutes for file tools and tools set to `ask` (for each limit, see [How a remote session works](#how-a-remote-session-works)). Claude receives the failure as the call's result, and a further call of the same kind waits again, which delays the `Stop` hook. For a task that makes these calls, have the user keep the device awake and connected.

To cover every user of a host, put the hooks in [Claude Code managed settings](https://code.claude.com/docs/en/settings#settings-files) on the host instead, which on a Linux host is the file `/etc/claude-code/managed-settings.json`. If the host already has Claude Code managed settings, add the hooks to those and leave [`parentSettingsBehavior`](https://code.claude.com/docs/en/settings-reference#parentsettingsbehavior) as it is, set or unset. Changing it changes how those settings combine with the policy that Claude Desktop supplies. If the host has none yet, also set `parentSettingsBehavior` to `"merge"` in the managed settings that you create.

> [!WARNING]
>
> By default, Claude Code managed settings on the host replace the policy that Claude Desktop supplies, even if they hold only hooks (see [Managed configuration on the remote host](#managed-configuration-on-the-remote-host)). With `parentSettingsBehavior` set to `"merge"`, the policy that Claude Desktop supplies still applies, layered under the host's own policy.

### Where MCP servers run in a remote session

An MCP server in a remote session runs on the device or on the host, depending on how it was added.

* **[Managed MCP servers](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin), and servers from plugins in the [`org-plugins` directory](/docs/third-party/claude-desktop/extensions#organization-plugins-admin)**: the device. Claude Desktop connects to the remote (HTTP or SSE) MCP servers and starts the local (stdio) ones on the device, and exposes them to the engine as tools.
* **Local servers that a user adds under Settings > Developer**: the host, not the device. Claude Desktop sends the host a server's command, its arguments, and only those of its environment variables whose names start with `MCP_` or are one of a few fixed logging and runtime names, such as `DEBUG` and `NODE_ENV`. A secret in an argument or in an `MCP_` variable reaches the host. On a Linux or macOS host, Claude Desktop leaves out a server whose command is a path under a macOS or Windows folder, such as `/Applications/` or `C:\`.
* **Servers bundled in any other plugin that Claude Desktop copies to the host**: the host. The engine starts the plugin's local servers there, and connects to its remote MCP servers from there.
* **Servers in Claude Code's own configuration on the host**: the host. The engine reads files such as `~/.claude.json` in the SSH user's home directory and a project's `.mcp.json`, and starts their local servers and connects to their remote MCP servers from there.

[`isLocalDevMcpEnabled`](/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled), `managedMcpServers`, `allowedPluginMcpServers`, and `deniedPluginMcpServers` decide which of these servers a remote session loads, as they do for a local Code session (see [Applied as managed policy](/docs/third-party/claude-desktop/code#applied-as-managed-policy)). If the host has its own Claude Code managed settings, those take precedence over the Claude Code policy these keys produce (see [Managed configuration on the remote host](#managed-configuration-on-the-remote-host)).

## Enable SSH remote sessions

Set [`sshHostAllowlist`](/docs/third-party/claude-desktop/configuration#sshhostallowlist) in your managed configuration. It appears in the **Code surface** section of the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) while Code is enabled.

| Value | Behavior |
| - | - |
| Unset | Off, unless a Claude Code managed-settings `sshHostAllowlist` on the device allows hosts (see [Interaction with Claude Code managed settings](#interaction-with-claude-code-managed-settings-on-the-device)) |
| `[]` | Off. Delivered by an administrator, `[]` also overrides a Claude Code managed-settings allowlist on the device |
| `["*"]` | Users can connect to any host |
| `["build01.corp.example.com", "*.dev.example.com"]` | Users can connect only to hosts that match an entry |

While SSH remote sessions are off, the environment picker shows local sessions only, and any attempt to connect to a saved host is refused.

Each entry is an exact hostname, an IP address, or a `*.` wildcard.

* `*.dev.example.com` matches `dev.example.com` and any subdomain of it at any depth.
* Matching is case-insensitive and ignores a `user@` prefix.
* An IP address entry matches only that address.
* Entries do not restrict the port.
* A value that is not an array of strings counts as `[]`.

Claude Desktop matches entries against the `HostName` that the device's `~/.ssh/config` gives for the entered host, or against the entered host itself when the configuration has no entry for it or can't be evaluated. An alias is allowed when it resolves to a listed host, whatever the alias is called, and is refused when it resolves to a host outside the list. In the allowlist, enter the hostnames that aliases resolve to.

A `ProxyCommand` is permitted when the resolved hostname matches. The app doesn't inspect where the command itself connects. The allowlist limits which hosts Claude Desktop connects to. It doesn't limit what the device can reach over SSH from a terminal. Use network controls for that.

For example, this Linux managed-settings file turns the feature on for one domain:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "sshHostAllowlist": ["*.dev.example.com"]
}
```

In a `.mobileconfig` or registry policy, write the array as a JSON string as described under [Value types](/docs/third-party/claude-desktop/configuration#value-types). In a [bootstrap](/docs/third-party/claude-desktop/bootstrap) response, the key sits inside the `codeSurface` object.

### Interaction with Claude Code managed settings on the device

Claude Code has its own `sshHostAllowlist` setting, which you can deploy on the device through a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy. The app resolves the two sources in this order:

1. `sshHostAllowlist` from the Claude Desktop configuration, when that configuration is delivered by an administrator: through machine-scoped device management (`HKLM` policy on Windows, a configuration profile on macOS, `/etc/claude-desktop` on Linux), through the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), or by a bootstrap server the app trusts (a `bootstrapUrl` set through device management or covered by `trustBootstrapDelivery`; see [Keys that require user consent](/docs/third-party/claude-desktop/bootstrap#keys-that-require-user-consent)). User-scope registry policy (`HKCU`) counts as applied locally.
2. `sshHostAllowlist` from Claude Code's managed settings on the device.
3. `sshHostAllowlist` from a Claude Desktop configuration the user applied locally in the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration#apply-locally-or-export-for-a-fleet).
4. Off.

On devices where users applied the configuration locally, deploy `sshHostAllowlist` in Claude Code's managed settings. That restricts SSH without an MDM profile taking ownership of the whole configuration (see [Update keys and managed precedence](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence)).

To turn off Code sessions that run on the device, so that users work in SSH remote sessions, set [`disableDesktopLocalSessions`](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions) to `true` in a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy on the device. Claude Desktop then refuses to start or resume a Code session that runs on the device. If the device already has Claude Code managed settings, add the key to those and leave `parentSettingsBehavior` as it is, set or unset. Changing it changes how those settings combine with the policy that Claude Desktop supplies. If the device has none yet, also set `parentSettingsBehavior` to `"merge"` in the managed settings that you create. Without `"merge"`, the new managed settings replace the policy that Claude Desktop supplies to Claude Code on the device (see [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) on the Code page).

Before you deploy `disableDesktopLocalSessions`, make sure that the `sshHostAllowlist` that applies on the device, by [the order of its sources](#interaction-with-claude-code-managed-settings-on-the-device), allows the hosts that users need. While SSH remote sessions are off, a device that has `disableDesktopLocalSessions` set can start neither a local Code session nor an SSH remote session.

### Devices that move to an admin console organization

A device that gets its SSH keys from a managed profile, a registry policy, or the profile's bootstrap server moves to the configuration from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console) when its user signs in to an organization that uses the console and chooses that organization in the dialog that follows. The app then restarts. A device that used such an organization before its profile arrived, and whose user hasn't signed out of the app since, moves back at its first launch on Claude Desktop 2.37337.0 or later, with no new sign-in and without asking the user, even if the stored sign-in has expired. To prevent that, add `disableDeploymentModeChooser` to the profile before devices update. `forceLoginOrgUUID` prevents it only for organizations it leaves out. Before Claude Desktop 2.37337.0, a device with such a profile ignores the admin console.

After the move, `sshHostAllowlist`, `sshTransport`, and `sshClientPath` from the profile, or from the profile's bootstrap server, don't apply, even where the console leaves them unset. For the profile's other settings, see [Which settings apply on a device with a managed profile](/docs/third-party/claude-desktop/admin-console#which-settings-apply-on-a-device-with-a-managed-profile).

* **Which hosts**: the console's `sshHostAllowlist` applies. If the console leaves the key unset (**Not set**), or the app hasn't yet downloaded the console's configuration at this launch (the copy a device keeps of the last download holds no lists), `sshHostAllowlist` from Claude Code's managed settings on the device applies. With neither, SSH remote sessions are off.
* **Which SSH client**: the console's `sshTransport` and `sshClientPath` apply. A key that the console leaves unset takes its default under [Host requirements](#host-requirements). Until the app has downloaded the console's configuration at a launch, both keys count as unset.

To prevent or limit the move, set one of these keys in the profile itself:

* **Keep the device on its profile**: set [`disableDeploymentModeChooser`](/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) to `true`. The app ignores the admin console, and the sign-in screen doesn't offer **Or sign in with Claude.ai**. A device that has already moved returns to its profile at its next launch.
* **Allow only your organization**: set [`forceLoginOrgUUID`](/docs/cowork/hipaa-setup#what-each-claude-desktop-key-does) to your organization ID, and set the SSH keys you rely on in the console too. The key also limits standard Claude Desktop sign-in on the device to your organization.

Before you add either key to a profile that sets only [app-behavior keys](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence), such as `disableAutoUpdates`, read the warning under [Keep a device on its managed profile](/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile).

## Inference credentials on the remote host

> [!WARNING]
>
> A remote session runs Claude Code on the SSH host with your organization's inference credential in its process environment, for as long as that process runs, including while Claude Desktop is closed. Anyone who can read that process's environment on the host, such as the same user account or a root user, can read the credential. List only hosts you trust with it, and prefer a credential that expires (single sign-on, or a credential helper that issues short-lived tokens) over a long-lived key.

The remote engine uses only the credential Claude Desktop passes in its environment. It ignores credentials already on the host, such as an AWS profile or application default credentials, and Claude Desktop copies no credential files there. Credential kinds that live in a file on the device are refused at session start.

| Provider | Works on a remote host | Refused at session start |
| - | - | - |
| [LLM gateway](/docs/third-party/claude-desktop/gateway) | Static API key, single sign-on, credential helper | |
| [Claude API](/docs/third-party/claude-desktop/claude-api) | Static API key, Sign in with Claude Console, credential helper | |
| [Microsoft Foundry](/docs/third-party/claude-desktop/foundry) | API key, in-app Entra ID sign-in, credential helper | |
| [Amazon Bedrock](/docs/third-party/claude-desktop/bedrock) | Bearer token, identity provider sign-in, credential helper | In-app AWS sign-in (IAM Identity Center), named profile |
| [Amazon Bedrock Mantle](/docs/third-party/claude-desktop/mantle) | Bearer token, credential helper | |
| [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex) | In-app Workforce Identity sign-in, credential helper | In-app Google sign-in, service-account key or credentials file, application default credentials on the device |

When the configured credential is a refused kind, the session fails at session start, with the card [SSH sessions can't use your model provider settings](#ssh-sessions-can%E2%80%99t-use-your-model-provider-settings).

When the remote engine's credential expires during a turn, Claude Desktop obtains a new one on the device, by re-running a [credential helper](/docs/third-party/claude-desktop/credential-helper) or using a sign-in's refresh token, and sends it over the SSH connection. When the user signs out of the inference provider in the app, Claude Desktop ends the remote engine.

The host needs its own network route to the inference endpoint and must trust the endpoint's certificate. Claude Desktop passes the endpoint address to the remote engine but not the device's proxy settings, CA certificates, or the user's shell variables such as `AWS_*` or `GOOGLE_*`. A gateway at `localhost` on the device is refused for remote sessions, because the host cannot reach it.

## Managed configuration on the remote host

Most of the policy that Claude Desktop applies to a local Code session applies on the remote host too. The [Code page](/docs/third-party/claude-desktop/code#how-configuration-propagates) describes how each key reaches Claude Code.

* `disableEssentialTelemetry` and `disableNonessentialTelemetry`.
* `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`, and `otlpContentCapture`. Remote sessions appear in your collector under the same `service.name` as local Code sessions. A collector at `localhost` on the device is not forwarded. An `otlpHeadersHelper` runs on the device at session start, and the remote session keeps those headers for its lifetime.
* `disabledBuiltinTools`, `builtinToolPolicy`, `autoModeEnabled`, and `disableBypassPermissionsMode`.
* [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), evaluated against the host's filesystem. `~` is the SSH user's home on the host, `%VAR%` entries are ignored, and Claude Desktop refuses to start a session in a directory outside every entry, so with a fleet value such as `~/Documents/Claude`, remote sessions start only under that path in the SSH user's home. For an entry with `mode` set to `ro`, see [Read-only folders on the remote host](#read-only-folders-on-the-remote-host).
* [`blockReadsOutsideWorkingDirectories`](/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories), evaluated on the host, so the working directories and the home directory it hides from shell commands are the SSH user's there. Hiding files from shell commands needs the host's sandbox dependencies (next item); on a host without them, or a Windows host, shell reads outside the working directories ask for approval instead, and the file-tool restriction applies regardless. Files a user attaches to a remote session stay readable, except on a Windows host, where the session's plugin files and attachments stay outside the file tools' reach under this key.
* `coworkEgressAllowedHosts`, as Claude Code managed settings. The network and filesystem sandbox it produces with `allowedWorkspaceFolders` depends on the host having Claude Code's sandbox dependencies installed (see [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)). Without them, commands run unsandboxed. See [Sandbox status on the remote host](#sandbox-status-on-the-remote-host) for the message the session shows.
* `managedMcpServers`, as the Claude Code managed setting that keeps the session from loading MCP servers that users define in Claude Code's own configuration on the host. The managed servers themselves are reached from the device (see [Where MCP servers run in a remote session](#where-mcp-servers-run-in-a-remote-session)).
* Plugins from your [allowed marketplaces](/docs/third-party/claude-desktop/extensions), copied to the host. A plugin's `hooks` directory is not copied, so its hooks do not run in a remote session, and a plugin whose manifest declares hooks elsewhere is not copied at all.

If the host has its own Claude Code managed settings, those take precedence over the policy Claude Desktop supplies, as described under [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) for local sessions.

### Read-only folders on the remote host

On a Linux or macOS host, Claude Desktop applies `mode` set to `ro` on an [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) entry by supplying Claude Code with permission rules that deny edits under the entry's path. The rules are Claude Code's own checks on what Claude does, not file permissions on the host. Where a folder must not change, use the host's file permissions to keep the SSH user from writing to it. Before Claude Desktop 2.31226.0, a folder with `mode` set to `ro` was allowed on the host but not read-only there.

A remote session doesn't enforce `mode` in these cases:

* **Windows hosts.**
* **Hosts with their own Claude Code managed settings**: Claude Code ignores the rules, and the sandbox settings that Claude Desktop supplies with them, unless those settings set `parentSettingsBehavior` to `"merge"`. Under `"merge"` the host's own values still win where the two differ, so `sandbox.enabled` set to `false` there leaves shell commands unsandboxed (see [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings)).
* **An entry that is or contains the SSH user's `~/.claude` folder, such as `~`**: Claude Code keeps its own files there. List narrower folders.

Where the rules apply, they cover the following:

* **Claude's file tools**: they refuse to create or change a file under the path, even in bypass permissions mode. A writable entry listed inside a read-only one is read-only for them too.
* **Shell commands that Claude runs with its Bash tool**: Claude Code's sandbox keeps them from writing under the path on a host where it runs, which on Linux needs Claude Code's [sandbox dependencies](https://code.claude.com/docs/en/sandboxing). The sandbox doesn't cover commands listed in Claude Code's `sandbox.excludedCommands`, or a path that contains one of `* ? [ ] ( ) { } | +` or a double quote. It may not stop commands in a folder that is listed through a symbolic link, so list each read-only folder by its real path, and keep it outside writable entries. On a host where the sandbox doesn't run, shell commands can still change the folder. For how the app reports that, see [Sandbox status on the remote host](#sandbox-status-on-the-remote-host).

The rules don't bind the SSH user, or other programs that run under that account. MCP servers on the host, hooks from Claude Code's configuration on the host, and the session's terminal (including commands that Claude runs there) can change the folder, and Claude Desktop and Claude Code can create git worktrees inside it.

### Sandbox status on the remote host

Claude Desktop asks Claude Code on the host whether the [sandbox](/docs/third-party/claude-desktop/code#applied-as-managed-policy) from your Claude Desktop policy is turned on and running there. The answer is Claude Code's own report, and it doesn't compare each allowed host or folder. Your policy includes the sandbox, and Claude Desktop asks, unless `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset. Requires Claude Desktop 2.26454.0 or later.

When the sandbox isn't confirmed, the session continues and shell commands can run outside the sandbox. To keep Claude Code from starting on a host whose operating system has no sandbox or that lacks a dependency, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) to `true` and [`parentSettingsBehavior`](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) to `"merge"` in the host's Claude Code managed settings. With `"merge"`, that setting applies together with your policy.

Find the message, or the `reason` your collector received, for the cause and the fix.

| Message in the session | `reason` your collector receives | Cause | Fix |
| - | - | - | - |
| Shell commands on `<host>` are running outside your organization's sandbox, which couldn't start | `cannot_start` | The sandbox is turned on but isn't running, for example because a Linux host lacks the sandbox dependencies | Install the [dependencies](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) on the host, then start a new session |
| Your organization's sandbox isn't running on `<host>`. Claude Code has no sandbox for that operating system | `unsupported` | The host runs an operating system that Claude Code reports no sandbox for, such as Windows | Use a macOS or Linux host |
| Your organization's sandbox policy isn't fully applied on `<host>`, so shell commands there may run outside it | `overridden` | Claude Code managed settings on the host replace your policy, even when they say nothing about the sandbox, or they turn the sandbox off or loosen it | Set `parentSettingsBehavior` to `"merge"` in the host's managed settings, and remove `sandbox` values there that conflict with your policy |
| No message | `unknown` | Claude Code gives no answer that Claude Desktop can read | In a session on that host, ask Claude to run the two commands under [Confirm commands run inside the sandbox](https://code.claude.com/docs/en/sandboxing#confirm-commands-run-inside-the-sandbox) |

To check one session, have the user open it, wait until Claude has finished replying, and enter `/status` in the message box. Where your policy includes the sandbox, the **Session info** card shows what Claude Desktop last learned in a **Sandbox** row. Requires Claude Desktop 2.31226.0 or later. Find the value's `reason` in the table of messages and reasons for the cause and the fix:

* **On · Strict**: no reason. Claude Code reports the sandbox from your policy turned on and running.
* **Off · can't start**: `cannot_start` or `unsupported`
* **Off**: `overridden`, and Claude Code reports no sandbox running
* **On · not fully applied**: `overridden`, and Claude Code reports a sandbox that Claude Desktop can't match to your policy
* **Couldn't check**: `unknown`

If the card has no **Sandbox** row, have the user send a message, and enter `/status` again after Claude's reply.

With [`otlpEndpoint`](/docs/third-party/claude-desktop/configuration#otlpendpoint) set, your collector receives a `desktop_ssh_sandbox_check_failed` event under the `service.name` value `claude-desktop`, unless [`otlpDesktopLogLevel`](/docs/third-party/claude-desktop/configuration#otlpdesktoploglevel) is `off`. A session can send the event more than once, for example when the reason changes or after Claude Desktop restarts, so count distinct `session_id` values rather than events. The event carries these attributes:

* **`reason`**: `cannot_start`, `unsupported`, `overridden`, or `unknown`
* **`sandbox_on`**: `false` when Claude Code reports no sandbox running, `true` when it reports one that Claude Desktop can't match to your policy, and absent when Claude Code doesn't say
* **`session_id`**: Claude Desktop's ID for the session
* **`backend_kind`**: `ssh`

The event doesn't name the host. To find the host, ask the user that the [user attribution](/docs/third-party/claude-desktop/telemetry#user-attribution) attributes identify.

## Host requirements

The host needs the following.

* Linux or macOS on x86\_64 or arm64, or Windows on x64 or arm64.
* On a Linux host, glibc 2.17 or later, or musl. The Claude Code engine is a single executable, and its glibc build links only against glibc's own libraries. Version 2.17 is the oldest glibc that build can load, and Claude Code's [system requirements](https://code.claude.com/docs/en/setup#system-requirements) still apply. To see the host's C library and its version, run `ldd --version` on the host. For a musl host, see [Alpine Linux and musl-based distributions](https://code.claude.com/docs/en/setup#alpine-linux-and-musl-based-distributions).
* An SSH server with the SFTP subsystem. On Windows, Microsoft's OpenSSH Server; with other SSH servers, the engine does not survive a dropped connection.
* An SSH server that accepts several sessions on one connection. The device's OpenSSH client on macOS and Linux, and the built-in client, open a remote session's channels on one SSH connection, so `MaxSessions 1` in the server's `sshd_config` doesn't work. OpenSSH's default is 10. The server doesn't need to allow TCP, Unix socket, agent, or X11 forwarding. A `ProxyJump` host must allow TCP forwarding to the host's SSH port.
* A POSIX shell, or PowerShell on Windows.
* `git` on the path, for git features.
* A home directory that the SSH user can write to and run programs from, with about 1 GB of disk space for the three Claude Code versions the app keeps and a fourth while an update installs. A home directory mounted `noexec` doesn't work.

The device needs the OpenSSH client (`ssh` and `ssh-keygen`). Claude Desktop runs the first `ssh` on the user's `PATH`; to pin a specific OpenSSH installation instead, set [`sshClientPath`](/docs/third-party/claude-desktop/configuration#sshclientpath) (beta, Claude Desktop 1.46388.1 or later) to the program's absolute path, and `ssh-keygen` is then taken from the same directory when present. If the pinned program is missing or cannot be run, SSH connections fail with an error that shows the configured path, rather than falling back to another `ssh`.

On macOS and Linux, Claude Desktop makes the SSH connection by running the device's OpenSSH client, so your own OpenSSH build's Kerberos (GSSAPI), certificate, and `ssh_config` support handles authentication. The program is the one `sshClientPath` names, or else the first `ssh` on the user's `PATH`, and it must be OpenSSH 7.6 or newer. On Windows, the app's built-in SSH client makes the connection by default, and the app runs the device's OpenSSH tools to evaluate the user's SSH configuration, look up host keys, and run the session's terminal. To have the device's OpenSSH client carry the connection on Windows too, set [`sshTransport`](/docs/third-party/claude-desktop/configuration#sshtransport) (beta) to `system-openssh`; the client must be Win32-OpenSSH 9.4 or newer. On a Windows device with no usable OpenSSH client and no `sshClientPath`, the built-in client is used regardless. Set `sshTransport` to `builtin` to use the built-in client on every platform. A change applies to new connections, and sessions that are already connected keep their client.

The built-in client also makes the connection in these cases:

* **The device can't start the OpenSSH client**: while `sshTransport` is unset or `auto` and `sshClientPath` is unset, the built-in client makes every connection until Claude Desktop restarts. Requires Claude Desktop 2.7032.0 or later.
* **Claude Desktop is installed from the Microsoft Store**: the built-in client makes the connection unless `sshTransport` is `system-openssh`. With `system-openssh`, the device's OpenSSH client makes the connection, but the app can't show its prompts for a password, a one-time code, or a key passphrase, or its question about a host key that isn't on record. Use a sign-in method that needs no prompt, such as a key held by the SSH agent, and have users connect to each host once from a terminal before adding it in the app, so that the host's key is in the user's `known_hosts` file.

Claude Desktop writes the following into the SSH user's home directory on the host. Each user who connects gets their own copy.

| Path on the host | Contents |
| - | - |
| `~/.claude/remote/srv/<version>/` | The remote server that Claude Desktop talks to |
| `~/.claude/remote/ccd-cli/` | The Claude Code engine, one file per build, under a name that starts with its version (the three most recent are kept) |
| `~/.claude/remote/run/<id>/` | The server's socket, token, and log |
| `~/.claude/remote/plugins/<id>/` | Plugins synced from the device, in one folder for each Claude Desktop installation that connects |
| `~/.claude/uploads/<session-id>/` | Files the user attached to a message. Not removed when the session ends |
| `~/.claude/` and `~/.claude.json` | Claude Code's own data, including session transcripts. See [Data storage](/docs/third-party/claude-desktop/data-storage) |

Each side of a remote session needs its own network access.

* Devices installed with the regular installer must reach `downloads.claude.ai`: Claude Desktop downloads the remote server there and uploads it to the host over SFTP. Devices installed with the [offline installer](/docs/third-party/claude-desktop/installation#offline-installation) don't: it bundles the remote server and the Claude Code engine for Linux x64 and arm64 hosts, and Claude Desktop uploads both over SFTP. Hosts on other platforms still need the download, so an offline-installed device that cannot reach `downloads.claude.ai` fails the session with a message saying the installer doesn't include remote components for that platform.
* The host must reach your inference endpoint and, if configured, your OTLP collector, plus whatever the user's own work needs. With the regular installer, it downloads the Claude Code engine from `downloads.claude.ai` when it can; when that fails, Claude Desktop downloads the engine on the device and uploads it over SFTP. Unless you disabled telemetry, the engine on the host also reports to the same Anthropic hosts as a local Code session (see [Telemetry and egress](/docs/third-party/claude-desktop/telemetry)). Blocking them does not affect the session.

### SSH configuration on the device

Claude Desktop applies the host's entry in the user's `~/.ssh/config`. With the device's OpenSSH client (the default on macOS and Linux), `ssh` reads the entry itself, so settings such as `ProxyJump`, certificate host keys, and GSSAPI authentication apply, and the app still connects only to the resolved hostname that passed `sshHostAllowlist`. The built-in client (the default on Windows) applies the hostname, port, user, identity file, SSH agent, and `ProxyCommand`.

* For hosts behind a bastion, configure a `ProxyJump` or `ProxyCommand`. `ProxyJump` works only when the device's OpenSSH client carries the connection (the default on macOS and Linux). The built-in client refuses it. For the card that the user sees, see [Ask your IT administrator to set sshTransport to system-openssh](#ask-your-it-administrator-to-set-sshtransport-to-system-openssh).
* With the device's OpenSSH client, OpenSSH's own host key checking applies. For a host whose key isn't on record yet, where the app can show a prompt, it shows the key's fingerprint, asks the user whether to trust it, and records a trusted key in the user's `known_hosts` file, unless the user's own SSH configuration accepts new keys without asking. The app can't show a prompt on every connection, for example when it reconnects in the background. Distribute the host keys or a host certificate authority to the devices, so that each host's key is on record before users connect. `@cert-authority` entries are honored. A key that differs from the one on record for the host is refused, whatever the entry's `StrictHostKeyChecking` says, unless another setting in the SSH configuration that applies to the host takes that check away, such as `NoHostAuthenticationForLocalhost yes` for a host on a loopback address.
* With the device's OpenSSH client, you can keep the app from asking users to trust the key of a host that isn't on record yet. Distribute the host keys in the client's system-wide `known_hosts` file, such as `/etc/ssh/ssh_known_hosts`, or distribute a host certificate authority. Then set `StrictHostKeyChecking yes`, for example under `Host *`, in the client's system-wide configuration file, such as `/etc/ssh/ssh_config`, which also governs other uses of that client, such as `git` over SSH. Where the SSH configuration that applies to a host has `StrictHostKeyChecking yes`, Claude Desktop doesn't ask the user to trust such a key, and `ssh` refuses the host if it can't verify the key. A key that differs from the one on record is handled the same way with or without this setting. The setting doesn't bind the user. By OpenSSH's own rules, `ssh` reads the user's `~/.ssh/config` before the system-wide file and keeps the first value it finds for a setting, so a `StrictHostKeyChecking` line there applies in place of yours. `ssh` also accepts a key that the user adds to their own `known_hosts` file, but under `yes` a connection from a terminal doesn't record the key. A user who picks a host that `ssh` refuses sees "Couldn't connect to" followed by the host, with [SSH host key verification failed](#ssh-host-key-verification-failed) under **View details**.
* With the built-in client, the host's key must already be in the device's `~/.ssh/known_hosts` as a plain entry. The app does not prompt to accept a new key and does not evaluate `@cert-authority` entries, so have users connect once from a terminal before adding the host in the app.
* With the built-in client, an identity file protected by a passphrase is skipped, not prompted for. Load it into the SSH agent, or use an unencrypted key. With the device's OpenSSH client, the app asks for the passphrase once the host's key is verified, and skips the key if the user cancels.
* With the built-in client, a host reached through a `ProxyCommand` gets the same host key check as a host reached directly. Before Claude Desktop 2.9939.0, the built-in client skipped host key verification for such a host.
* With the built-in client, a host connects with its key unchecked when its entry sets `StrictHostKeyChecking no`, sets `UserKnownHostsFile` to `none` or `/dev/null`, and sets no `RevokedHostKeys`. The app shows no password or one-time code prompt for such a host, so it needs a key or SSH agent sign-in.
* The connection times out after 30 seconds. A larger `ConnectTimeout` in the host entry extends it.

With either client, the connection that carries the session leaves these settings off, whatever the entry says:

* **Forwarding**: `ForwardAgent`, `ForwardX11`, `Tunnel`, `LocalForward`, `RemoteForward`, and `DynamicForward`.
* **Kerberos delegation**: `GSSAPIDelegateCredentials`. The host doesn't receive the user's Kerberos ticket over this connection, even where the entry says `GSSAPIDelegateCredentials yes`. A `ProxyJump` host is reached by a separate `ssh`, which applies the jump host's own entry.
* **Commands**: `RemoteCommand` and `LocalCommand`.

Where the session's terminal can't use that connection, and always with the built-in client, the terminal runs its own `ssh`, which applies the entry's forwarding and Kerberos delegation settings. With `ForwardAgent yes` in the entry, that `ssh` forwards the user's SSH agent to the host.

## Troubleshoot

### Your organization doesn't allow this SSH connection

The `sshHostAllowlist` in effect on this device is unset, empty, or has no entry that matches the host. The card's details say which. The name that must match is the `HostName` that the device's `~/.ssh/config` resolves the entered host to, so an entry that lists only an alias doesn't allow the host. Which configuration source supplies the key on a device follows [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). For a device that moved to an admin console organization, see [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization). The connection test reports the same denial as "Your organization's settings do not allow this connection." Before Claude Desktop 2.31226.0, the card's title was "SSH isn't allowed by your organization".

### SSH to this device isn't available

The host resolves to the device itself (`localhost`, `127.0.0.1`, or a tunnel or port forward that ends on the device) while `allowedWorkspaceFolders` restricts workspace folders. A session over SSH to the device reaches the same disk the policy restricts, so it is refused. Connect to a different host, or use a local session. Before Claude Desktop 2.31226.0, the card's title was "SSH to this machine isn't available".

### SSH sessions can't use your model provider settings

The configured inference credential is one of the kinds listed as refused under [Inference credentials on the remote host](#inference-credentials-on-the-remote-host), or the inference endpoint is on the device itself. The card's details say which. Switch the deployment to a credential kind that works on a remote host, or point the app at an endpoint the host can reach. Before Claude Desktop 2.31226.0, the card's title was "Remote sessions aren't available with this inference setup".

### SSH host key verification failed

The host's key has changed, or it is not in the device's `~/.ssh/known_hosts` and was not trusted in the app (the built-in client never asks). Connect to the host from a terminal on the device to check and record the current key, then retry.

With the device's OpenSSH client (the default on macOS and Linux), if `StrictHostKeyChecking yes` applies to the host, connecting from a terminal doesn't record its key. Instead, check the key and add it to the system-wide `known_hosts` file, or give the host a certificate from your host certificate authority (see [SSH configuration on the device](#ssh-configuration-on-the-device)).

### Ask your IT administrator to set sshTransport to system-openssh

The built-in client made the connection, and the host needs the device's OpenSSH client. Where the app can name a step, the card's title gives it, and the card's text gives the cause, either "Claude's built-in SSH library can't connect through a jump host (ProxyJump)." or "Claude's built-in SSH library can't check host keys against a certificate authority or another known\_hosts file."

* **"Ask your IT administrator to set sshTransport to system-openssh"**: the built-in client is the device's default, and the device has a usable OpenSSH client. Set [`sshTransport`](/docs/third-party/claude-desktop/configuration#sshtransport) to `system-openssh`.
* **"Ask your IT administrator to change sshTransport from builtin to system-openssh"**: your configuration sets `sshTransport` to `builtin`. Change it to `system-openssh`.
* **"Ask your admin to correct the sshTransport setting"**: the app can't read the value that your configuration gives `sshTransport`, for example a misspelling, so the built-in client makes the connection. Correct the value. Requires Claude Desktop 2.37337.0 or later.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer and set sshTransport to system-openssh, then quit and reopen Claude"**: the built-in client is the device's default, and the app found no usable OpenSSH client on the device. Install the client, and set the key.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer, then quit and reopen Claude"**: `sshTransport` is `system-openssh`, and the app found no usable OpenSSH client on the device. Install the client.
* **"Quit and reopen Claude; if this comes back, ask your IT administrator to let Claude use the system OpenSSH client"**: the device couldn't start the OpenSSH client earlier in this run of the app (see [Host requirements](#host-requirements)).

Where the app can name no step, the card's title gives the cause: `<host> needs a jump host, which Claude can't use here`, with the text "A ProxyCommand for this host may work instead, once you quit and reopen Claude.", or `Claude can't check <host>'s key here`.

These cards require Claude Desktop 2.31226.0 or later. Before Claude Desktop 2.31226.0, the built-in client refused a `ProxyJump` host with a message that suggests `ProxyCommand`.

### This computer won't start Claude's SSH sign-in helper

On a Windows device where the device's OpenSSH client makes the connection, Windows refused to start one of the helper programs through which Claude Desktop shows `ssh`'s prompts. Without them the app can't ask for a password or a one-time code, so the user can't sign in to a host that needs one. Select **View details** on the card for the blocked program's path and the error code. Allow `claude-ssh-askpass.exe`, `claude-ssh-broker.exe`, and `claude-ssh-proxy.exe` in that folder, then have the user try again. Requires Claude Desktop 2.37337.0 or later.

### This computer's ssh refuses a backslash or dollar sign in user names

On a macOS or Linux device where the device's OpenSSH client makes the connection, that client refuses the user name on its command line because the name has a `\` or a `$`, as in `DOMAIN\user`. Claude Desktop passes such a name to `ssh` in a configuration file that it writes, and shows this card where it can't. Select **View details** on the card and match the last line:

* **`needs the Include line in this file to use a full path`**: the system's `ssh_config`, or a file read through it, has an `Include` with a relative path. The line names the file. Write that path in full, starting with `/`.
* **`couldn't find which system ssh_config this ssh reads` or `couldn't write that file`**: have the user try again. With the second, the app couldn't write the file in a private temporary folder.
* **`the name is the jump host's`**: the card's title is "This computer's ssh refuses the jump host's user name". In the user's `~/.ssh/config`, move the name from `ProxyJump` to a `User` line in the jump host's own `Host` block.

This card requires Claude Desktop 2.37337.0 or later.

### Setup on the host fails after SSH connects

SSH connected, but Claude Desktop couldn't place or start the remote server or the engine on the host. Select **View details** on the failure card to read the app's own message, which can end with a code in square brackets. Match the code, or the start of the message:

* **`[SFTP_UNAVAILABLE]`**: the host's SSH server refused the SFTP subsystem. Enable `Subsystem sftp` in the server's `sshd_config`.
* **`[SESSION_LIMIT]`**: the host's SSH server refused to open another session on the connection. Raise `MaxSessions` in the server's `sshd_config`, and reload the SSH server. See [Host requirements](#host-requirements).
* **`[SFTP_NOT_STARTED]`**: the host's SSH server accepted the request for SFTP, but the SFTP server ended before its first answer, or text arrived in place of that answer. In a terminal on the device, run `sftp` with the same host, for example `sftp user@build01.corp.example.com`, to see what stops it. Then check the settings and files that the message names.
* **`[EXEC_NO_INPUT]`**: the host's SSH server ran the app's command but passed it no input, which setup and the session's own link need. In a terminal on the device, run `echo hi | ssh` with the same host and `cat`, for example `echo hi | ssh user@build01.corp.example.com cat`. It prints `hi` on a host that passes input. Have the host's administrator let commands run over SSH receive input.
* **`[ENOSPC]` or `[EDQUOT]`**: a disk is full, or a quota is used up. In a message that starts with `Couldn't prepare the deploy locally`, the disk is the device's. In any other message it is the host's, so free space in the SSH user's home directory. [Host requirements](#host-requirements) gives the space the app needs.
* **`Unsupported remote platform`**: the host's operating system or processor isn't among those under [Host requirements](#host-requirements).
* **`[CLI_NOT_RUNNABLE]`**: the remote server installed the engine, but the engine's first run didn't start or didn't exit cleanly, so the remote server removed it. One cause is a glibc older than 2.17. Run `ldd --version` on the host to check. Before Claude Desktop 2.37337.0, the message has no code and starts with `Couldn't install the Claude CLI on the remote (cli archive)`.
* **`[NO_INSTALL_RESULT]`**: the remote server's install step printed no result. A home directory mounted `noexec` is one cause.

`[SESSION_LIMIT]` and `[SFTP_NOT_STARTED]` require Claude Desktop 2.31226.0 or later, and appear only when the device's OpenSSH client makes the connection. `[SESSION_LIMIT]` appears only on macOS and Linux devices. Their cards are titled `<host> allows too few SSH sessions per connection` and `SFTP doesn't start on <host>`.

`[CLI_NOT_RUNNABLE]` and `[EXEC_NO_INPUT]` require Claude Desktop 2.37337.0 or later. `[EXEC_NO_INPUT]` appears only on Windows devices where the device's OpenSSH client makes the connection. Their cards are titled `Claude Code didn't run on <host>` and `<host> doesn't pass input to commands run over SSH`. From the same version, the card is titled `Couldn't copy Claude Code to <host>` where the app couldn't put its files on the host, and `Couldn't install Claude Code on <host>` where the engine's install failed, each for a cause with no card of its own.

### Git commands fail with Read-only file system

Git commands fail with this error when the user opens the session in a subfolder of a Git repository, on a Linux host where the sandbox from your policy runs. Git's message then reads, for example, `Unable to create '<path>/.git/index.lock': Read-only file system`. To find out whether the sandbox runs there, see [Sandbox status on the remote host](#sandbox-status-on-the-remote-host).

The sandbox lets shell commands that Claude runs with its Bash tool write in the folder the session was opened in, and the repository's `.git` folder is outside that folder. Of these commands, the ones that write to the `.git` folder fail, such as `git add` and `git commit`. Have the user start a new session at the top of the repository.

> [!NOTE]
>
> These cases are covered elsewhere:
>
> * **An `allowedWorkspaceFolders` entry with `mode` set to `ro`**: see [Read-only folders on the remote host](#read-only-folders-on-the-remote-host)
> * **A message with `unable to unlink old`**: see [A git command fails with `unable to unlink old`](https://code.claude.com/docs/en/sandboxing#a-git-command-fails-with-unable-to-unlink-old)
> * **The other places that the sandbox lets these commands write to**: see [Filesystem isolation](https://code.claude.com/docs/en/sandboxing#filesystem-isolation) and the `allowedWorkspaceFolders` row under [Applied as managed policy](/docs/third-party/claude-desktop/code#applied-as-managed-policy)

## Related

* [Code in Claude Desktop on 3P](/docs/third-party/claude-desktop/code)
* [`sshHostAllowlist` in the configuration reference](/docs/third-party/claude-desktop/configuration#sshhostallowlist)
* [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access)
