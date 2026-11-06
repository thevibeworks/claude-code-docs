> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH remote sessions in Claude Desktop on 3P

> How Code sessions run on a remote host over SSH in Claude Desktop on 3P, the sshHostAllowlist key that enables them, which inference credentials work on a remote host, and what to check before turning them on

An SSH remote session is a [Code](https://claude.com/docs/third-party/claude-desktop/code.md) session whose Claude Code engine runs on another machine that the user reaches over SSH, while the session's interface stays in Claude Desktop on the user's device. Claude Desktop connects to the host, places the engine there, and starts the session with the inference credential and policy from your managed configuration. Users can work on code that lives on a development server, a build box, or a cloud workstation without copying it to their device. In Claude Desktop on third-party (3P), SSH remote sessions are off until you set the [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist) key, because enabling them sends your inference credential to the hosts users connect to.

> [!NOTE]
>
> SSH remote sessions are in beta in Claude Desktop on 3P and require Claude Desktop 1.40609.0 or later. The in-app configuration window marks `sshHostAllowlist` with a **Beta** pill.

## How a remote session works

1. **Connect.** The user picks an SSH host from the environment picker in Code, or adds one by entering its address, port, and an identity file. Claude Desktop connects through the device's OpenSSH client, or in some cases through its built-in SSH client (see [Host requirements](#host-requirements)), applies the host's entry from the device's `~/.ssh/config` (see [SSH configuration on the device](#ssh-configuration-on-the-device)), and prompts in the app if the host asks for a password or a one-time code.
2. **Deploy.** Claude Desktop places a remote server and the Claude Code engine under `~/.claude/remote/` in the SSH user's home directory on the host ([Host requirements](#host-requirements) lists every path) and reuses them on later connections.
3. **Run.** The remote server starts the engine on the host with the inference credential and policy from your managed configuration. Every file read, edit, shell command, and git operation runs on the host, in the working directory the user chose there. Claude Desktop connects to [managed MCP servers](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin) from the device and exposes them to the engine as tools.
4. **Stream.** Claude's responses and tool output stream back to Claude Desktop. Permission prompts appear in Claude Desktop, and the engine waits on the host until the user answers.

The engine keeps running on the host through a dropped SSH link, device sleep, or the user quitting Claude Desktop. It finishes the current turn, or stops at a permission prompt, then idles until the user reopens the session. While Claude Desktop is closed, no new turns run and the inference credential is not refreshed, so a turn that outlives the credential fails with an authentication error. A restart of the app for an update counts as a quit.

When the user reopens the session after a quit, Claude Desktop rejoins the engine or replaces it, unless it refuses to start the session:

* **Rejoins**: on a macOS or Linux device, Claude Desktop 2.42304.0 or later tries to rejoin an engine that 2.42304.0 or later started. On a Windows device, Claude Desktop 3.1623.0 or later tries to rejoin an engine that 3.1623.0 or later started. If it rejoins, a turn still running goes on. It can fail to rejoin, for example after some Claude Desktop updates or after a change to the managed configuration since the engine started.
* **Replaces**: if Claude Desktop doesn't rejoin the engine, for example because a version older than the minimums above started it, Claude Desktop ends the engine and starts a fresh one from the transcript stored on the host. A turn that finished while the app was closed is shown in full, and a turn that still runs is cut short. If the turn stays stopped, the user sends a message to continue it.

On a host that ends a user's processes at logout, the remote server and the engine end with the SSH connection that started them, so a turn in progress doesn't survive a disconnect. Linux hosts where systemd-logind's `KillUserProcesses` setting is `yes` and applies to the SSH user behave this way. To keep remote sessions running through a disconnect on such a host, ask the host's administrator to exempt the SSH user, for example by listing the user under `KillExcludeUsers` in the systemd-logind configuration.

An idle engine stays on the host, with the credential in its environment, until one of these happens:

* The user archives or deletes the session.
* The user reopens the session and Claude Desktop ends the engine to start a fresh one.
* The host restarts.
* After an update that includes a new remote server, Claude Desktop replaces the host's remote server at a later connection. This ends the engines under the old server. Claude Desktop can put the replacement off while it believes that work is running on that host.
* After an update that includes a newer Claude Code, the user sends a message in the session. Claude Desktop 4.29.0 or later can then replace the engine with the newer version, if the engine has reported that it has no background or scheduled work.
* On a Linux or macOS host, 30 days pass without a connection from Claude Desktop to the remote server. The remote server then stops and ends its engines. Requires Claude Desktop 1.52386.0 or later.
* Someone ends the engine's process on the host. To list or end the engines and the remote server yourself on a Linux or macOS host, see [Files and processes on the remote machine](https://code.claude.com/docs/en/desktop#files-and-processes-on-the-remote-machine). There the engine is called Claude Code, and the remote server the helper.

While Claude Desktop is disconnected, the remote server keeps the most recent output of each running engine in a 16 MiB buffer. It drops older output, and the engine keeps running.

On a Linux or macOS host, if Claude Desktop stayed open, it rejoins the running engine when it reconnects after device sleep or a dropped SSH link. It catches up from the buffer, and loads the part of the conversation that the buffer has dropped from the transcript stored on the host. If it can't load all of it, the session shows "Some output produced while you were disconnected may be missing here."

Some tool calls wait for an answer from Claude Desktop, and fail while it is disconnected:

* **File tools under a folder restriction**: if you set [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), Claude Desktop checks each file read, search, and edit before it happens. While Claude Desktop is disconnected, each of these calls waits up to 10 minutes and then fails.
* **Tools that your policy sets to ask**: if [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy) sets a bare tool name, such as `Bash`, to `ask`, Claude Desktop is consulted before each call to that tool. While Claude Desktop is disconnected, each call waits up to 10 minutes and then fails.
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

* Each file read, search, and edit, if you set [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders)
* Each call to a tool that [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy) sets to `ask` by its bare name, such as `Bash`
* Each call to a tool from an MCP server that runs on the device

While Claude Desktop is disconnected, each of these calls waits and then fails, after up to 10 minutes for file tools and tools set to `ask` (for each limit, see [How a remote session works](#how-a-remote-session-works)). Claude receives the failure as the call's result, and a further call of the same kind waits again, which delays the `Stop` hook. For a task that makes these calls, have the user keep the device awake and connected.

To cover every user of a host, put the hooks in [Claude Code managed settings](https://code.claude.com/docs/en/settings#settings-files) on the host instead, which on a Linux host is the file `/etc/claude-code/managed-settings.json`. If the host already has Claude Code managed settings, add the hooks to those and leave [`parentSettingsBehavior`](https://code.claude.com/docs/en/settings-reference#parentsettingsbehavior) as it is, set or unset. Changing it changes how those settings combine with the policy that Claude Desktop supplies. If the host has none yet, also set `parentSettingsBehavior` to `"merge"` in the managed settings that you create.

> [!WARNING]
>
> By default, Claude Code managed settings on the host replace the policy that Claude Desktop supplies, even if they hold only hooks (see [Managed configuration on the remote host](#managed-configuration-on-the-remote-host)). With `parentSettingsBehavior` set to `"merge"`, the policy that Claude Desktop supplies still applies, layered under the host's own policy.

### Where MCP servers run in a remote session

An MCP server in a remote session runs on the device or on the host, depending on how it was added.

* **[Managed MCP servers](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin), and servers from plugins in the [`org-plugins` directory](https://claude.com/docs/third-party/claude-desktop/extensions#organization-plugins-admin)**: the device. Claude Desktop connects to the remote (HTTP or SSE) MCP servers and starts the local (stdio) ones on the device, and exposes them to the engine as tools.
* **Local servers that a user adds under Settings > Developer**: the host, not the device. Claude Desktop sends the host a server's command, its arguments, and only those of its environment variables whose names start with `MCP_` or are one of a few fixed logging and runtime names, such as `DEBUG` and `NODE_ENV`. A secret in an argument or in an `MCP_` variable reaches the host. On a Linux or macOS host, Claude Desktop leaves out a server whose command is a path under a macOS or Windows folder, such as `/Applications/` or `C:\`.
* **Servers bundled in any other plugin that Claude Desktop copies to the host**: the host. The engine starts the plugin's local servers there, and connects to its remote MCP servers from there.
* **Servers in Claude Code's own configuration on the host**: the host. The engine reads files such as `~/.claude.json` in the SSH user's home directory and a project's `.mcp.json`, and starts their local servers and connects to their remote MCP servers from there.

With the device's OpenSSH client, the user's first message can wait up to ten seconds, with the line `Setting up your MCP servers on <host>…` under it. This can happen after a session starts, and after a quit, once Claude Desktop rejoins the running engine. Claude Desktop is handing the engine the local servers that the user added under **Settings > Developer**. If the engine doesn't get them in time, the message goes anyway, and the conversation shows `This message went without your MCP servers. If you need them, send it again once they're connected.` If the task needs those servers, have the user wait until Claude finishes responding, then send the message again. Requires Claude Desktop 4.4212.0 or later.

[`isLocalDevMcpEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled), `managedMcpServers`, `allowedPluginMcpServers`, and `deniedPluginMcpServers` decide which of these servers a remote session loads, as they do for a local Code session (see [Applied as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy)). If the host has its own Claude Code managed settings, those take precedence over the Claude Code policy these keys produce (see [Managed configuration on the remote host](#managed-configuration-on-the-remote-host)).

## Enable SSH remote sessions

Set [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist) in your managed configuration. It appears in the **Code surface** section of the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) while Code is enabled.

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

A session's [jump hosts](#jump-hosts-and-the-allowlist) must match an entry too. The allowlist limits which hosts Claude Desktop connects to. It doesn't limit what the device can reach over SSH from a terminal. Use network controls for that, and for a hard boundary.

For example, this Linux managed-settings file turns the feature on for one domain:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "sshHostAllowlist": ["*.dev.example.com"]
}
```

In a `.mobileconfig` or registry policy, write the array as a JSON string as described under [Value types](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types). In a [bootstrap](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) response, the key sits inside the `codeSurface` object.

### Jump hosts and the allowlist

Add each jump host, or bastion, that Claude Desktop checks to `sshHostAllowlist`, by the `HostName` that the device's `~/.ssh/config` gives for it. Add the jump hosts before devices update to Claude Desktop 3.1623.0 or later, or users can't connect through them. To hold updates until devices have the new allowlist, see [Auto-updates](https://claude.com/docs/third-party/claude-desktop/telemetry.md#auto-updates).

> [!WARNING]
>
> The allowlist has one kind of entry, so users can also start a session on any host that you list, and that session receives your [inference credential](#inference-credentials-on-the-remote-host). List only jump hosts that you'd also let users run sessions on.

Claude Desktop checks jump hosts in the `ProxyJump` that the device's `~/.ssh/config` sets for the session's host, or in a `ProxyCommand` written as `ssh -W %h:%p <host>`. If one that it checks isn't on the allowlist when the app connects or reconnects a session, the connection fails. When the user starts a session or sends a message, they see [Your organization doesn't allow this SSH connection](#your-organization-doesn%E2%80%99t-allow-this-ssh-connection), and the card's details give that jump host's `HostName`.

Find the names to add in a terminal on a user's device. Skip `proxyjump` lines only on devices where the built-in client makes every connection, for example with `sshTransport` set to `builtin`. The built-in client [refuses every `ProxyJump`](#ssh-configuration-on-the-device), listed or not.

1. Run `ssh -G` with a host that users connect to, for example `ssh -G build01`. Look for a `proxyjump` line, or a `proxycommand` line written as `ssh -W %h:%p <host>`. The command still counts with any of `-l`, `-p`, `-J`, `-q`, `-v`, `-N`, `-T`, `-x`, or `-a`, and the hosts after `-J` are jump hosts too. If a `proxycommand` line runs a program other than `ssh`, add nothing for it.
2. Run `ssh -G` with each jump host on that line, without any `:port`, and note the `hostname` that it prints. If the output for the first jump host on that line has a line of either kind, repeat this step with it. Ignore such a line in a later jump host's output.
3. Add each hostname, or a wildcard that covers it, to the `sshHostAllowlist` that applies on the device. To tell which one applies, see [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). Then have users quit and reopen Claude Desktop, because an open app keeps the list from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#availability) or the [admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-updates) until it restarts.

### Interaction with Claude Code managed settings on the device

Claude Code has its own `sshHostAllowlist` setting, which you can deploy on the device through a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy. The app resolves the two sources in this order:

1. `sshHostAllowlist` from the Claude Desktop configuration, when that configuration is delivered by an administrator: through machine-scoped device management (`HKLM` policy on Windows, a configuration profile on macOS, `/etc/claude-desktop` on Linux), through the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), or by a bootstrap server the app trusts (a `bootstrapUrl` set through device management or covered by `trustBootstrapDelivery`; see [Keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent)). User-scope registry policy (`HKCU`) counts as applied locally.
2. `sshHostAllowlist` from Claude Code's managed settings on the device.
3. `sshHostAllowlist` from a Claude Desktop configuration the user applied locally in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#apply-locally-or-export-for-a-fleet).
4. Off.

On devices where users applied the configuration locally, deploy `sshHostAllowlist` in Claude Code's managed settings. That restricts SSH without an MDM profile taking ownership of the whole configuration (see [Update keys and managed precedence](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence)).

To turn off Code sessions that run on the device, so that users work in SSH remote sessions, set [`disableDesktopLocalSessions`](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions) to `true` in a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy on the device. Claude Desktop then refuses to start or resume a Code session that runs on the device. If the device already has Claude Code managed settings, add the key to those and leave `parentSettingsBehavior` as it is, set or unset. Changing it changes how those settings combine with the policy that Claude Desktop supplies. If the device has none yet, also set `parentSettingsBehavior` to `"merge"` in the managed settings that you create. Without `"merge"`, the new managed settings replace the policy that Claude Desktop supplies to Claude Code on the device (see [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) on the Code page).

Before you deploy `disableDesktopLocalSessions`, make sure that the `sshHostAllowlist` that applies on the device, by [the order of its sources](#interaction-with-claude-code-managed-settings-on-the-device), allows the hosts that users need. While SSH remote sessions are off, a device that has `disableDesktopLocalSessions` set can start neither a local Code session nor an SSH remote session.

### Devices that move to an admin console organization

A device that gets its SSH keys from a managed profile, a registry policy, or the profile's bootstrap server moves to the configuration from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) when its user signs in to an organization that uses the console and chooses that organization in the dialog that follows. The app then restarts. A device that used such an organization before its profile arrived, and whose user hasn't signed out of the app since, moves back at its first launch on Claude Desktop 2.37337.0 or later, with no new sign-in and without asking the user, even if the stored sign-in has expired. To prevent that, add `disableDeploymentModeChooser` to the profile before devices update. `forceLoginOrgUUID` prevents it only for organizations it leaves out. Before Claude Desktop 2.37337.0, a device with such a profile ignores the admin console.

After the move, `sshHostAllowlist`, `sshTransport`, and `sshClientPath` from the profile, or from the profile's bootstrap server, don't apply, even where the console leaves them unset. For the profile's other settings, see [Which settings apply on a device with a managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#which-settings-apply-on-a-device-with-a-managed-profile).

* **Which hosts**: the console's `sshHostAllowlist` applies. If the console leaves the key unset (**Not set**), or the app hasn't yet downloaded the console's configuration at this launch (the copy a device keeps of the last download holds no lists), `sshHostAllowlist` from Claude Code's managed settings on the device applies. With neither, SSH remote sessions are off.
* **Which SSH client**: the console's `sshTransport` and `sshClientPath` apply. On a Windows device, a client that the console's `sshClientPath` names makes the connection only if it is Microsoft's OpenSSH. With `system-openssh`, SSH connections fail under any other client. A key that the console leaves unset takes its default under [Host requirements](#host-requirements). Until the app has downloaded the console's configuration at a launch, both keys count as unset, so no client is pinned. Until then the built-in client makes the connection on a Windows device, even where the console sets `system-openssh`. The device's OpenSSH client makes it on a macOS or Linux device, even where the console sets `builtin`.

To prevent or limit the move, set one of these keys in the profile itself:

* **Keep the device on its profile**: set [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) to `true`. The app ignores the admin console, and the sign-in screen doesn't offer **Or sign in with Claude.ai**. A device that has already moved returns to its profile at its next launch.
* **Allow only your organization**: set [`forceLoginOrgUUID`](https://claude.com/docs/cowork/hipaa-setup#what-each-claude-desktop-key-does) to your organization ID, and set the SSH keys you rely on in the console too. The key also limits standard Claude Desktop sign-in on the device to your organization.

Before you add either key to a profile that sets only [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), such as `disableAutoUpdates`, read the warning under [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

## Inference credentials on the remote host

> [!WARNING]
>
> A remote session runs Claude Code on the SSH host with your organization's inference credential in its process environment, for as long as that process runs, including while Claude Desktop is closed. Anyone who can read that process's environment on the host, such as the same user account or a root user, can read the credential. List only hosts you trust with it, and prefer a credential that expires (single sign-on, or a credential helper that issues short-lived tokens) over a long-lived key.

The remote engine uses only the credential Claude Desktop passes in its environment. It ignores credentials already on the host, such as an AWS profile or application default credentials, and Claude Desktop copies no credential files there. Credential kinds that live in a file on the device are refused at session start.

| Provider | Works on a remote host | Refused at session start |
| - | - | - |
| [LLM gateway](https://claude.com/docs/third-party/claude-desktop/gateway.md) | Static API key, single sign-on, credential helper | |
| [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) | Static API key, Sign in with Claude Console, credential helper | |
| [Microsoft Foundry](https://claude.com/docs/third-party/claude-desktop/foundry.md) | API key, in-app Entra ID sign-in, credential helper | |
| [Amazon Bedrock](https://claude.com/docs/third-party/claude-desktop/bedrock.md) | Bearer token, identity provider sign-in, credential helper | In-app AWS sign-in (IAM Identity Center), named profile |
| [Amazon Bedrock Mantle](https://claude.com/docs/third-party/claude-desktop/mantle.md) | Bearer token, credential helper | |
| [Google Cloud's Agent Platform](https://claude.com/docs/third-party/claude-desktop/vertex.md) | In-app Workforce Identity sign-in, credential helper | In-app Google sign-in, service-account key or credentials file, application default credentials on the device |

When the configured credential is a refused kind, the session fails at session start, with the card [SSH sessions can't use your model provider settings](#ssh-sessions-can%E2%80%99t-use-your-model-provider-settings).

When the remote engine's credential expires during a turn, Claude Desktop obtains a new one on the device, by re-running a [credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper.md) or using a sign-in's refresh token, and sends it over the SSH connection. When the user signs out of the inference provider in the app, Claude Desktop ends the remote engine.

Where the host's [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) starts Claude Code, Claude Desktop passes no inference credential and refuses no credential kind. Claude Code uses the credential that the launcher or the SSH account's own environment sets, or, on Google Cloud's Agent Platform, the account's application default credentials.

The host needs its own network route to the inference endpoint and must trust the endpoint's certificate. Claude Desktop passes the endpoint address to the remote engine but not the device's proxy settings, CA certificates, or the user's shell variables such as `AWS_*` or `GOOGLE_*`. A gateway at `localhost` on the device is refused for remote sessions, because the host cannot reach it.

## Managed configuration on the remote host

Most of the policy that Claude Desktop applies to a local Code session applies on the remote host too. The [Code page](https://claude.com/docs/third-party/claude-desktop/code.md#how-configuration-propagates) describes how each key reaches Claude Code.

* `disableEssentialTelemetry` and `disableNonessentialTelemetry`.
* `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`, and `otlpContentCapture`. Remote sessions appear in your collector under the same `service.name` as local Code sessions. A collector at `localhost` on the device is not forwarded. An `otlpHeadersHelper` runs on the device at session start, and the remote session keeps those headers for its lifetime.
* `disabledBuiltinTools`, `builtinToolPolicy`, `autoModeEnabled`, and `disableBypassPermissionsMode`.
* [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), evaluated against the host's filesystem. `~` is the SSH user's home on the host, `%VAR%` entries are ignored, and Claude Desktop refuses to start a session in a directory outside every entry, so with a fleet value such as `~/Documents/Claude`, remote sessions start only under that path in the SSH user's home. For an entry with `mode` set to `ro`, see [Read-only folders on the remote host](#read-only-folders-on-the-remote-host).
* [`blockReadsOutsideWorkingDirectories`](https://claude.com/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories), evaluated on the host, so the working directories and the home directory it hides from shell commands are the SSH user's there. Hiding files from shell commands needs the host's sandbox dependencies (next item); on a host without them, or a Windows host, shell reads outside the working directories ask for approval instead, and the file-tool restriction applies regardless. Files a user attaches to a remote session stay readable, except on a Windows host, where the session's plugin files and attachments stay outside the file tools' reach under this key.
* `coworkEgressAllowedHosts`, as Claude Code managed settings. The network and filesystem sandbox it produces with `allowedWorkspaceFolders` depends on the host having Claude Code's sandbox dependencies installed (see [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)). Without them, commands run unsandboxed. See [Sandbox status on the remote host](#sandbox-status-on-the-remote-host) for the message the session shows.
* `managedMcpServers`, as the Claude Code managed setting that keeps the session from loading MCP servers that users define in Claude Code's own configuration on the host. The managed servers themselves are reached from the device (see [Where MCP servers run in a remote session](#where-mcp-servers-run-in-a-remote-session)).
* Plugins from your [allowed marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md), copied to the host. A plugin's `hooks` directory is not copied, so its hooks do not run in a remote session, and a plugin whose manifest declares hooks elsewhere is not copied at all.

If the host has its own Claude Code managed settings, those take precedence over the policy Claude Desktop supplies, as described under [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) for local sessions.

### Read-only folders on the remote host

On a Linux or macOS host, Claude Desktop applies `mode` set to `ro` on an [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) entry by supplying Claude Code with permission rules that deny edits under the entry's path. The rules are Claude Code's own checks on what Claude does, not file permissions on the host. Where a folder must not change, use the host's file permissions to keep the SSH user from writing to it. Before Claude Desktop 2.31226.0, a folder with `mode` set to `ro` was allowed on the host but not read-only there.

A remote session doesn't enforce `mode` in these cases:

* **Windows hosts.**
* **Hosts with their own Claude Code managed settings**: Claude Code ignores the rules, and the sandbox settings that Claude Desktop supplies with them, unless those settings set `parentSettingsBehavior` to `"merge"`. Under `"merge"` the host's own values still win where the two differ, so `sandbox.enabled` set to `false` there leaves shell commands unsandboxed (see [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings)).
* **An entry that is or contains the SSH user's `~/.claude` folder, such as `~`**: Claude Code keeps its own files there. List narrower folders.

Where the rules apply, they cover the following:

* **Claude's file tools**: they refuse to create or change a file under the path, even in bypass permissions mode. A writable entry listed inside a read-only one is read-only for them too.
* **Shell commands that Claude runs with its Bash tool**: Claude Code's sandbox keeps them from writing under the path on a host where it runs, which on Linux needs Claude Code's [sandbox dependencies](https://code.claude.com/docs/en/sandboxing). The sandbox doesn't cover commands listed in Claude Code's `sandbox.excludedCommands`, or a path that contains one of `* ? [ ] ( ) { } | +` or a double quote. It may not stop commands in a folder that is listed through a symbolic link, so list each read-only folder by its real path, and keep it outside writable entries. On a host where the sandbox doesn't run, shell commands can still change the folder. For how the app reports that, see [Sandbox status on the remote host](#sandbox-status-on-the-remote-host).

The rules don't bind the SSH user, or other programs that run under that account. MCP servers on the host, hooks from Claude Code's configuration on the host, and the session's terminal (including commands that Claude runs there) can change the folder, and Claude Desktop and Claude Code can create git worktrees inside it.

### Sandbox status on the remote host

Claude Desktop asks Claude Code on the host whether the [sandbox](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) from your Claude Desktop policy is turned on and running there. Requires Claude Desktop 2.26454.0 or later. If `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset, your policy has no sandbox. For what Claude Desktop checks then, see [Sandbox from the host's managed settings](#sandbox-from-the-host%E2%80%99s-managed-settings). For a key that isn't set, see [Unset allowlist in Code sessions](https://claude.com/docs/third-party/claude-desktop/web-tools.md#unset-allowlist-in-code-sessions).

The answer is Claude Code's own report, and Claude Desktop compares only part of it with your policy:

* **Folders**: Claude Desktop doesn't compare the folders that the sandbox allows with the folders in your policy.
* **Network hosts**: if the answer lists the network hosts that the sandbox allows, and a network host from your policy is missing from the list, Claude Desktop reports the reason `overridden`. Claude Desktop doesn't check for network hosts that the remote host's own settings add. Requires Claude Desktop 3.6556.1 or later.

When the sandbox isn't confirmed, the session continues and shell commands can run outside the sandbox. To keep Claude Code from starting on a host whose operating system has no sandbox or that lacks a dependency, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) to `true` and [`parentSettingsBehavior`](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) to `"merge"` in the host's Claude Code managed settings. With `"merge"`, that setting applies together with your policy.

Find the message, or the `reason` your collector received, for the cause and the fix.

| Message in the session | `reason` your collector receives | Cause | Fix |
| - | - | - | - |
| Shell commands on `<host>` are running outside your organization's sandbox, which couldn't start | `cannot_start` | The sandbox is turned on but isn't running, for example because a Linux host lacks the sandbox dependencies | Install the [dependencies](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) on the host, then start a new session |
| Your organization's sandbox isn't running on `<host>`. Claude Code has no sandbox for that operating system | `unsupported` | The host runs an operating system that Claude Code reports no sandbox for, such as Windows | Use a macOS or Linux host |
| Your organization's sandbox policy isn't fully applied on `<host>`, so shell commands there may run outside it | `overridden` | Claude Code managed settings on the host replace your policy, even when they say nothing about the sandbox, or they turn the sandbox off or loosen it | Set `parentSettingsBehavior` to `"merge"` in the host's managed settings, and remove `sandbox` values there that conflict with your policy |
| No message | `unknown` | Claude Code gives no answer that Claude Desktop can read | In a session on that host, ask Claude to run the two commands under [Confirm commands run inside the sandbox](https://code.claude.com/docs/en/sandboxing#confirm-commands-run-inside-the-sandbox) |

The fix for the `overridden` message and the fix for the message under [Policy status on the remote host](#policy-status-on-the-remote-host) start at the same setting, `parentSettingsBehavior`. With Claude Desktop 3.6556.1 or later, a session that shows one of the two messages doesn't add the other until the first no longer applies. Your collector still receives the event of the check whose message is held back, and the **Sandbox** row of `/status` still shows the sandbox's state.

To check one session, have the user open it, wait until Claude has finished replying, and enter `/status` in the message box. Where your policy includes the sandbox, the **Session info** card shows what Claude Desktop last learned in a **Sandbox** row. Requires Claude Desktop 2.31226.0 or later. Find the value's `reason` in the table of messages and reasons for the cause and the fix:

* **On · Strict**: no reason. Claude Code reports the sandbox from your policy turned on and running.
* **Off · can't start**: `cannot_start` or `unsupported`
* **Off**: `overridden`, and Claude Code reports no sandbox running
* **On · not fully applied**: `overridden`, and Claude Code reports a sandbox that Claude Desktop can't match to your policy
* **Couldn't check**: `unknown`

If your policy includes the sandbox and the card has no **Sandbox** row, have the user send a message, and enter `/status` again after Claude's reply.

With [`otlpEndpoint`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpendpoint) set, your collector receives a `desktop_ssh_sandbox_check_failed` event under the `service.name` value `claude-desktop`, unless [`otlpDesktopLogLevel`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpdesktoploglevel) is `off`. A session can send the event more than once, for example when the reason changes or after Claude Desktop restarts, so count distinct `session_id` values rather than events. The event carries these attributes:

* **`reason`**: `cannot_start`, `unsupported`, `overridden`, or `unknown`
* **`sandbox_on`**: `false` when Claude Code reports no sandbox running, `true` when it reports one that Claude Desktop can't match to your policy, and absent when Claude Code doesn't say
* **`session_id`**: Claude Desktop's ID for the session
* **`backend_kind`**: `ssh`

The event doesn't name the host. To find the host, ask the user that the [user attribution](https://claude.com/docs/third-party/claude-desktop/telemetry.md#user-attribution) attributes identify.

### Sandbox from the host's managed settings

Where your policy has no sandbox, Claude Desktop 4.16336.0 or later asks Claude Code whether managed settings on the host turn a sandbox on, and reports one that isn't running.

Expect fewer reports than for a sandbox from your policy:

* **The session**: it continues, and shell commands run outside the sandbox. To keep Claude Code from starting instead, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) to `true` in the same managed settings.
* **Reasons**: only `cannot_start` and `unsupported`, with the same messages, `/status` value, and event as under [Sandbox status on the remote host](#sandbox-status-on-the-remote-host). The table's rows for those two apply here too. Claude Desktop never reports `overridden` or `unknown` here.
* **A host that has the packages**: it can still report `cannot_start`, for example Ubuntu 24.04 or later without an AppArmor profile for bubblewrap. [Set up Linux and WSL2](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) covers the profile too.
* **`/status`**: the **Sandbox** row appears only after Claude Desktop has reported that sandbox as not running. After `cannot_start`, the row can stay for the rest of that session, so check a fix in a new session.
* **No report**: don't take it as proof that the sandbox runs. To confirm, have the user ask Claude to run the two commands under [Confirm commands run inside the sandbox](https://code.claude.com/docs/en/sandboxing#confirm-commands-run-inside-the-sandbox).
* **The event**: it doesn't say which sandbox it is about. From a device whose policy has no sandbox, it is about the host's.
* **A device where the local configuration file governs**: Claude Desktop doesn't ask there. The file governs where neither device management, the Enterprise Admin Console, nor a bootstrap server delivers the configuration. It still governs beside a device management profile that sets only app-behavior keys, such as `disableAutoUpdates`.

### Policy status on the remote host

To find a host that doesn't apply your policy, Claude Desktop asks Claude Code on the host which permission rules apply there. In the answer, Claude Desktop looks for the deny and ask rules sent with your policy. Requires Claude Desktop 3.6556.1 or later.

Keys that produce such rules include:

* [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy) entries other than `allow`
* Scoped [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools) entries such as `Bash(curl *)`
* [Read-only folders](#read-only-folders-on-the-remote-host)
* A managed MCP server's `toolPolicy` entries set to `blocked` or `ask`

The check fails if Claude Code lists none of those rules as managed policy, or itself reports that it left out the sent policy. The session continues and shows this message, unless it already shows the `overridden` message under [Sandbox status on the remote host](#sandbox-status-on-the-remote-host):

```text theme={null}
Your organization's policy isn't fully applied on <host>. Ask your admin to check parentSettingsBehavior in that host's Claude Code managed settings.
```

A session that shows one of the two messages doesn't add the other until the first no longer applies. Your collector still receives the event of the check whose message is held back.

To fix the host, set `parentSettingsBehavior` to `"merge"` in the host's Claude Code managed settings, which otherwise replace your policy. See [Managed configuration on the remote host](#managed-configuration-on-the-remote-host). Claude Desktop asks again when Claude Code starts, when Claude Desktop rejoins a running Claude Code process, and after each turn. Once the check passes again, a session that still shows the message also shows "Your organization's policy applies on `<host>` again."

With [`otlpEndpoint`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpendpoint) set, your collector receives a `desktop_ssh_policy_check_failed` event under the `service.name` value `claude-desktop` when the check fails, unless [`otlpDesktopLogLevel`](https://claude.com/docs/third-party/claude-desktop/configuration#otlpdesktoploglevel) is `off`. A session can send the event more than once, for example after Claude Code or Claude Desktop restarts, so count distinct `session_id` values rather than events. No event marks the recovery. The event carries these attributes:

* **`reason`**: `rules` when Claude Code lists none of the sent rules as managed policy, or `claude_code` when Claude Code itself reports that it left out the sent policy
* **`session_id`**: Claude Desktop's ID for the session
* **`backend_kind`**: `ssh`

The event doesn't name the host. To find the host, identify the user from the event's [user attribution](https://claude.com/docs/third-party/claude-desktop/telemetry.md#user-attribution) attributes, and ask that user.

The absence of the message and the event doesn't show that a host applies your policy:

* **Any host**: the answer is Claude Code's own report from the host, not proof. A failed check blocks nothing.
* **A host that lists at least one sent rule**: the check passes as soon as Claude Code lists one sent rule as managed policy. That holds even if the host's own managed settings supply that rule or replace other parts of your policy.
* **A policy without a deny or ask rule**: Claude Desktop shows no message and sends no event, unless Claude Code itself reports that it left the policy out.
* **A Claude Code version on the host that doesn't report its permission rules**: Claude Desktop shows no message and sends no event.
* **A restart of Claude Desktop**: a session that showed the message doesn't show it again until Claude Code has answered again.

## Host requirements

The host needs the following.

* Linux or macOS on x86\_64 or arm64, or Windows on x64 or arm64.
* On a Linux host, glibc 2.17 or later, or musl. The Claude Code engine is a single executable, and its glibc build links only against glibc's own libraries. Version 2.17 is the oldest glibc that build can load, and Claude Code's [system requirements](https://code.claude.com/docs/en/setup#system-requirements) still apply. To see the host's C library and its version, run `ldd --version` on the host. For a musl host, see [Alpine Linux and musl-based distributions](https://code.claude.com/docs/en/setup#alpine-linux-and-musl-based-distributions).
* An SSH server. On Windows, Microsoft's OpenSSH Server; with other SSH servers, the engine does not survive a dropped connection.
* The SSH server's SFTP subsystem. For a Linux or macOS host that lacks it, see [Hosts without SFTP](#hosts-without-sftp).
* If devices connect with Claude Desktop's built-in SSH client, an SSH server that accepts several sessions on one connection. Before Claude Desktop 4.5284.0, that client is the default on Windows devices, and later it still connects to hosts already in use. The built-in client can't connect where the server's `sshd_config` sets `MaxSessions 1`. Raise that limit, for example to OpenSSH's default of 10, or see [Hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection).
* The server doesn't need to allow TCP, Unix socket, agent, or X11 forwarding. A `ProxyJump` host must allow TCP forwarding to the host's SSH port.
* A POSIX shell, or PowerShell on Windows.
* `git` on the path, for git features.
* A home directory that the SSH user can write to and run programs from, with about 1 GB of disk space for the three Claude Code versions the app keeps and a fourth while an update installs. A home directory mounted `noexec` doesn't work.

The device needs the OpenSSH client (`ssh` and `ssh-keygen`). Claude Desktop runs the first `ssh` on the user's `PATH`. For the `ssh` that carries the connection on a Windows device, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

To pin a specific OpenSSH installation instead, set [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath) (beta, Claude Desktop 1.46388.1 or later) to the program's absolute path:

* **Companion tools**: Claude Desktop takes `ssh-keygen` and `ssh-add` from the same directory when they exist there. Otherwise it takes `ssh-keygen` from the user's `PATH`, and `ssh-add` from the operating system's own OpenSSH or else the `PATH`.
* **macOS and Linux devices**: the program can be a wrapper script that runs an OpenSSH client. For what Claude Desktop 4.16336.0 or later needs of a wrapper, see the paragraph on wrapper scripts below this list.
* **Windows devices**: the program must be an `.exe` file, not a `.cmd`, `.bat`, or `.ps1` script. Stricter rules apply to its version and folder. See **Client version** under [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client), and [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows). For a value that starts with `%LOCALAPPDATA%\`, see [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user).
* **A program that can't be used**: if the pinned program is missing, or on macOS and Linux can't be run, SSH connections fail with an error that shows the configured path. Where the OpenSSH client makes the connection, they also fail if the program is older than OpenSSH 7.6. Claude Desktop never runs another `ssh` program in its place. On Windows, if the program exists but can't be started, Claude Desktop's built-in client can still make the connection.
* **Every source of settings**: a bootstrap server or the Enterprise Admin Console that leaves `sshClientPath` out cancels the value that device management sets. A bootstrap server does so once its response has loaded at a launch, and the console as soon as the app starts. Claude Desktop then chooses the `ssh` program as if you had pinned nothing. Set the key everywhere you manage settings. From a bootstrap server, return each platform's path only to devices of that platform.

With Claude Desktop 4.16336.0 or later, on macOS and Linux `ssh` shows its prompts through `claude-ssh-askpass`, a helper that ships with the app. If you allow programs by list, allow Claude Desktop and `ssh` to start it:

* **macOS**: allow `Claude.app/Contents/Helpers/claude-ssh-askpass`, which is signed with the app.
* **Linux**: allow `claude-ssh-askpass` in the `resources` folder of the app's installation.

Claude Desktop runs the helper as a test before a connection that can prompt, and `ssh` runs it for each prompt. Without the helper, the app also can't ask the user to trust a host key that isn't on record, and `ssh` refuses that host.

A wrapper script that stands in for `ssh`, whether `sshClientPath` names it or it comes first on the `PATH`, must leave `ssh`'s standard error untouched. If it sends that stream through a pipe, a file, or a terminal of its own, sign-ins that need a prompt fail. See [Claude's SSH sign-in helper isn't working on this computer](#claude%E2%80%99s-ssh-sign-in-helper-isn%E2%80%99t-working-on-this-computer).

Claude Desktop makes the SSH connection by running the device's OpenSSH client, so your own OpenSSH build's Kerberos (GSSAPI), certificate, and `ssh_config` support handles authentication. The program is the one `sshClientPath` names, or else, on macOS and Linux, the first `ssh` on the user's `PATH`, and it must be OpenSSH 7.6 or later. On Windows, the device's OpenSSH client is the default in Claude Desktop 4.5284.0 or later, and only for hosts that are new to the device. See [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

To use one client for every host, set [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) (beta) to `system-openssh` or `builtin`. Both apply on every platform. A change applies to new connections, and sessions that are already connected keep their client.

* **`system-openssh`**: use the device's OpenSSH client.
* **`builtin`**: use the app's built-in SSH client. The app still runs the device's OpenSSH tools to evaluate the user's SSH configuration, look up host keys, and run the session's terminal. The in-app help and some cards call this client the built-in library.
* **`auto`**: the same as leaving the key unset.
* **Any other value**: the app can't read it, for example a misspelling, and the built-in client makes every connection.

The built-in client also makes the connection in these cases, and on Windows in the cases under [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client):

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
| `~/.claude/` and `~/.claude.json` | Claude Code's own data, including session transcripts. See [Data storage](https://claude.com/docs/third-party/claude-desktop/data-storage.md) |

Each side of a remote session needs its own network access.

* Devices installed with the regular installer must reach `downloads.claude.ai`: Claude Desktop downloads the remote server there and uploads it to the host. Devices installed with the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation) don't: it bundles the remote server and the Claude Code engine for Linux x64 and arm64 hosts, and Claude Desktop uploads both. Hosts on other platforms still need the download, so an offline-installed device that cannot reach `downloads.claude.ai` fails the session with a message saying the installer doesn't include remote components for that platform.
* The host must reach your inference endpoint and, if configured, your OTLP collector, plus whatever the user's own work needs. With the regular installer, it downloads the Claude Code engine from `downloads.claude.ai` when it can; when that fails, Claude Desktop downloads the engine on the device and uploads it. Unless you disabled telemetry, the engine on the host also reports to the same Anthropic hosts as a local Code session (see [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md)). Blocking them does not affect the session.

### Hosts without SFTP

A remote session can start on a Linux or macOS host where SFTP is turned off or doesn't work. Claude Desktop then places its own setup files on the host with shell commands instead of SFTP. Before Claude Desktop 3.1623.0, setup fails on such a host.

These features need SFTP, so they are off in that session. Users can keep working without them.

* Image and document previews
* File attachments
* The Changes pane
* Plugins that Claude Desktop copies from the device
* Downloads of PDF and Office files: the download option is missing, or the download fails with `Couldn't download <name>`

A session without SFTP needs at least the following. Where one is missing, setup fails (see [Setup on the host fails after SSH connects](#setup-on-the-host-fails-after-ssh-connects)).

* **Version**: Claude Desktop 3.1623.0 or later on the device.
* **Client**: the device's OpenSSH client makes the connection. The built-in client needs SFTP. Before Claude Desktop 4.5284.0 it is the default on Windows devices, and in Claude Desktop 4.5284.0 or later it still makes the connection in some cases. To have the device's OpenSSH client make every connection, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).
* **Shell**: a POSIX shell on the host, with `sh` and the standard Unix tools such as `ls`, `cat`, and `rm`.
* **Base64 decoder**: `base64` or `openssl` on the host.
* **SHA-256 tool**: `sha256sum`, `shasum`, or `openssl` on the host.

To bring back what is off, go by the second sentence of the notice that the user sees in the conversation. The notice begins, for example, "Image and document previews, file attachments, the Changes pane, and your computer's plugins are off."

* **"turn on SFTP"**: the SSH server refuses SFTP. Enable `Subsystem sftp` in the server's `sshd_config`, and reload the SSH server.
* **"see why SFTP doesn't start"**: the SSH server accepts the request for SFTP, but SFTP never starts. In a terminal on the device, run `sftp` with the same host to see what stops it, then fix that on the host.
* **"let SFTP reach your home folder"**: over SFTP, Claude Desktop didn't find a folder it made under the SSH user's home directory, as when SFTP is confined to a folder. Set up the SSH server so that SFTP sees the home directory at the same path as the login shell does.
* **"refused the second sign-in"**: SFTP isn't at fault. The host refused what the user entered at the sign-in for file transfer, as it can when the user enters the same one-time code twice. Claude Desktop makes that second sign-in on [hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection) and from [Windows devices that use the device's OpenSSH client](#prepare-windows-devices-for-the-openssh-client). If the host refuses it each time, have the user sign in by a method that needs no prompt, such as a key that an SSH agent holds. Before Claude Desktop 4.29.0, the connection fails.

After the change, or to try the sign-in again, have the user quit and reopen Claude Desktop and start a new session.

### Hosts that allow one session per connection

A device can connect to a host whose `sshd_config` sets `MaxSessions 1` only when the device's OpenSSH client makes the connection:

* **macOS and Linux devices**: the device's OpenSSH client is the default. The device also needs Claude Desktop 3.1623.0 or later.
* **Windows devices**: the built-in client can't connect to such a host. Before Claude Desktop 4.5284.0 it is the default, and in Claude Desktop 4.5284.0 or later it still makes the connection in some cases. To have the device's OpenSSH client make every connection, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

Connecting to a host with this limit changes what the SSH server's log shows and how often devices sign in:

* **Refused sessions**: when a macOS or Linux device first connects to the host, the SSH server's log shows a sign-in followed by `no more sessions`. Claude Desktop remembers the limit for 7 days at a time: at the device's next connection after that, the log shows the sign-in and the refusal again. The refusal is how Claude Desktop learns of the limit, so you don't need to act on it. A Windows device that connects through the device's OpenSSH client causes no such refusal.
* **More sign-ins**: each time a device connects or reconnects, it signs in at least twice, to run commands and to transfer files. Expect at least one more sign-in for each terminal tab, and for each Claude Desktop session in which the user runs commands that start with `!`.
* **One-time codes**: if the host also asks for a one-time code, users get a prompt at each sign-in for a connection or a terminal tab. Commands that start with `!` fail on that host, so have users run commands in a terminal tab.

### Prepare Windows devices for the OpenSSH client

With Claude Desktop 4.5284.0 or later, a Windows device connects to each host that is new to it through the device's OpenSSH client. A host that the device already connects to stays on the app's built-in SSH client, with no action required. A new or re-imaged PC, or a virtual desktop that keeps no local app data, has no hosts in use, so every host is new to it. The same holds where the app's record of earlier connections is damaged, because the app then resets it. A host that the device last connected to before Claude Desktop 1.46388.1 can count as new too, because earlier versions may have kept no record of it. Before Claude Desktop 4.5284.0, the built-in client makes every connection on Windows unless [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) (beta) is `system-openssh`.

Choose what your Windows devices do. For the first and the third choice, check what the device's OpenSSH client needs, under **Check what the device's OpenSSH client needs on Windows** below.

* **Leave `sshTransport` unset**: new hosts and new PCs use the OpenSSH client.
* **Keep the built-in client for every host**: set `sshTransport` to `builtin`. It holds for new hosts and new PCs too. If `sshClientPath` starts with `%LOCALAPPDATA%\`, remove it too, or SSH connections fail. See **If you set `sshTransport`** below.
* **Use the OpenSSH client for every host**: set `sshTransport` to `system-openssh`. To go back, set `builtin`, and if `sshClientPath` starts with `%LOCALAPPDATA%\`, remove it too. See **If you set `sshTransport`** below.

With `sshTransport` unset or `auto`, the built-in client still connects in these cases, and in those under [Host requirements](#host-requirements):

* **Hosts already in use**: a host that the device has reached only with the built-in client stays on it. A host that the device first reaches while `builtin` is set, or while it has no usable OpenSSH client, stays on the built-in client too. The same goes for a host first reached with a `.ppk` file that the built-in client can read, or after Windows denied the sign-in helper's start.
* **Configuration that hasn't loaded**: on a device that takes its configuration from the Enterprise Admin Console or a bootstrap server, the built-in client makes every connection at each launch until that configuration has loaded. If your bootstrap response sets `system-openssh`, set it in the registry too, so that it holds in this case.
* **A record that can't be read**: while the app can't read its own record of earlier connections, for example while a scanner holds the file, the built-in client makes that connection, whatever the host.
* **PuTTY key files**: a host whose identity file in the app is a PuTTY `.ppk` file that the built-in client can read, for example version 2, RSA, with no passphrase.
* **A blocked sign-in helper**: a host that asks for a password or a one-time code, where Windows denies the app the start of its sign-in helper while a user waits for the connection. Where the helper is missing or gives no answer, or only `ssh.exe` can't start it, the sign-in fails instead.
* **Another `ssh` program**: `sshClientPath` names an OpenSSH that isn't Microsoft's, or a Microsoft OpenSSH (Win32-OpenSSH) before 9.4. Unless the value starts with `%LOCALAPPDATA%\`, the app still runs the named program to read the user's SSH configuration and to run the session's terminal. With such a value and no `system-openssh`, the app doesn't start the program, and SSH connections fail.
* **No usable OpenSSH client, and no `sshClientPath`**: the built-in client makes every connection, whatever `sshTransport` says. See **Devices without a usable client** below.
* **An `sshClientPath` program that gives no answer**: the built-in client tries the connection, whatever `sshTransport` says. See [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows).

Four of these cases pass with time. They are configuration that hasn't loaded, a record that can't be read, an `ssh.exe` that Windows wouldn't start, and an `sshClientPath` program that gave no answer. A new host first reached in such a case isn't kept: once the case has passed, its connections use the OpenSSH client.

A host under **Hosts already in use** moves to the OpenSSH client, or counts as new, in these cases. Once the OpenSSH client has connected to it, the host stays there. A connection that fails for another reason moves nothing.

* **You set `system-openssh`**: once one connection has succeeded under it, the device keeps no host on the built-in client for having used it before, even if you remove the setting later. Cases such as **PuTTY key files** still apply.
* **A host key that the built-in client can't check**: the user's `known_hosts` file has no plain entry for the host, and `ssh` would check its key against a certificate authority or another `known_hosts` file. The system-wide file is one such file. The host moves at its next connection.
* **A jump host**: a host that is given a jump host moves at its first connection after the user has quit and reopened Claude Desktop. Until then the built-in client dials the host without the jump host.
* **A record that is lost**: on a re-imaged PC, or once the app has reset a damaged record, every host counts as new.

Nothing that a user does to a saved connection in Claude Desktop moves its host. Removing the connection and adding it again at the same address, or editing its address, keeps the client. The same machine added under another name, address, or port counts as a new host. A user who edits their own `~/.ssh/config` or `known_hosts` file can bring about the second or third case above.

While hosts stay on the built-in client:

* **Host key checks**: a host on the built-in client keeps that client's [host key check](#ssh-configuration-on-the-device), which reads the user's `known_hosts` file alone, not the system-wide one or a `RevokedHostKeys` file. To move those hosts to `ssh`'s own check, on a device with a usable OpenSSH client, set `sshTransport` to `system-openssh`.
* **Which client connected**: search `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) for `master ready for` (the OpenSSH client) or `[SSH2Connection] Connected to` (the built-in client). If both appear for one connection, the later one counts. For the reason, search for `this connection attempt uses`: the line ends with the source of the choice, such as `host_kept` for a host already in use. The app doesn't show which client connected, and two devices can differ at one host.

With the device's OpenSSH client on a Windows device:

* **Repeated sign-ins**: each time Claude Desktop connects or reconnects to a host, it signs in at least twice, to run commands and to transfer files, and once more for each terminal that opens. A Windows host takes at least one more sign-in each time. On a Windows device, each sign-in is a separate `ssh` process. They stay open together, so a per-user login limit on the host has to leave room for them. Each process connects to the host by name, so a name that stands for several machines, such as a load balancer or round-robin DNS, must send all connections from one device to the same machine. Claude Desktop repeats a typed password or key passphrase itself for the other sign-ins of that connection. A host that asks for a one-time code, a push approval, or a security key touch asks again at each sign-in.
* **Key files that other accounts can read**: `ssh` ignores a private key file that any account but the user, SYSTEM, or Administrators can read. After a sign-in fails over one, Claude Desktop tightens the file's access list where it can, and connects again. `ssh.log` records the list before and after.
* **Host keys that aren't on record**: where the app can show a prompt, it asks the user whether to trust the key, and records a trusted key in the user's `known_hosts` file. To distribute host keys instead, see [SSH configuration on the device](#ssh-configuration-on-the-device).
* **Saved passwords**: when the session's host asks for the account password, the sign-in dialog has a **Remember password for `<host>`** checkbox. To turn saved passwords off, set [`disableSshSavedPasswords`](https://code.claude.com/docs/en/desktop#managed-settings) to `true` in Claude Code's managed settings on the device, by the steps for `disableDesktopLocalSessions` under [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). The dialog then has no checkbox, and the app stops using passwords that it saved earlier. It doesn't delete them, and the user's settings no longer offer to forget one. Removing the connection in the app still deletes its saved password. Deliver the setting before devices start to use the OpenSSH client. Neither the Enterprise Admin Console nor a bootstrap server can deliver it.

Check what the device's OpenSSH client needs on Windows:

* **Client version**: with no [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath), a usable client prints a version that starts with `OpenSSH_for_Windows_` and is 9.4 or later. That is Microsoft OpenSSH, also called Win32-OpenSSH. Run `ssh -V` in a Command Prompt window on a device, signed in as the user. If that output is anything else, run `ssh.exe -V` in `%SystemRoot%\System32\OpenSSH` and in `%ProgramFiles%\OpenSSH`: Claude Desktop uses the first usable client that it finds, on the `PATH`, then in those two folders in that order. If you set `sshClientPath`, run that program with `-V` instead. With `sshTransport` unset or `auto`, or in Claude Desktop 3.1623 and earlier, it has to pass the same test. With `system-openssh`, it can instead be an OpenSSH client that isn't Microsoft's. Such a client has to meet the conditions in [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) or in [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user). Each section names the Claude Desktop version that it requires.
* **Devices without a usable client**: on a Windows device with no usable OpenSSH client and no `sshClientPath`, the built-in client is used, whatever `sshTransport` says. Add the **OpenSSH Client** optional feature in Windows and install pending Windows updates, or install [Microsoft's newer build](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release). Run the version check again, then have users quit and reopen Claude Desktop. Hosts that the device first reached without a usable client stay on the built-in client. To move them, set `sshTransport` to `system-openssh`.
* **Application control**: `ssh` shows its prompts through three helper programs that ship with Claude Desktop, `claude-ssh-askpass.exe`, `claude-ssh-broker.exe`, and `claude-ssh-proxy.exe`. Allow them in your application control policy by their publisher, Anthropic, PBC. Their folder changes with each update, and the files carry no product name or version. Allow the `ssh.exe` that the version check found too. If Windows refuses to start the helpers, the app can't ask for a key passphrase, and `ssh` refuses a host whose key isn't on record. Sign-ins that need a password or a one-time code fail where `sshTransport` is `system-openssh`. Otherwise the built-in client makes them where the app itself can't start the helper. See [This computer won't start Claude's SSH sign-in helper](#this-computer-won%E2%80%99t-start-claude%E2%80%99s-ssh-sign-in-helper).
* **Firewall and endpoint security**: allow `ssh.exe` outbound wherever you allow Claude Desktop itself. With `sshTransport` unset or `auto` and no `sshClientPath`, the built-in client takes over where Windows refuses to start `ssh.exe`, but not where `ssh.exe` starts and can't reach the network. Each connection that the OpenSSH client makes then fails or times out, and the card points to the network or the host, not to `ssh.exe`.
* **While `ssh.exe` can't reach the network**: a host that stays on the built-in client still connects. For other hosts, set `sshTransport` to `builtin`, for Windows devices only, until you can allow `ssh.exe` (see **One value for all platforms** below). A host that the device first reaches meanwhile stays on the built-in client afterwards. The session's terminal runs `ssh.exe` with either client, so it stays blocked until then.
* **Key files**: `ssh` doesn't read a PuTTY `.ppk` key file. Unless the host stays on the built-in client for that file (see **PuTTY key files** above), export the key in OpenSSH format, and have the user select the exported file as the connection's identity file.
* **SSH configuration files**: `ssh` reads the user's `~/.ssh/config` itself, and the connection fails if `ssh` rejects the file. In a Command Prompt window on a device, signed in as the user, run the usable client with `-G` and a host, for example `ssh -G build01.corp.example.com`. Use the client's full path if it isn't the first `ssh` on the `PATH`. `ssh` prints the host's settings if it accepts the file, and an error if it doesn't.

If you set `sshTransport`:

* **One value for all platforms**: `sshTransport` has no per-platform form. A Windows registry policy reaches Windows devices only. A value from a bootstrap server or the Enterprise Admin Console reaches the macOS and Linux devices that it serves too. The device's OpenSSH client already makes the connection there by default, so `builtin` moves them to the built-in client. To change Windows devices alone from a bootstrap server, return the key only in responses that go to them.
* **Devices with a bootstrap server**: an available [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) replaces the `sshTransport` and `sshClientPath` that device management sets in the registry, even if it leaves a key out. A response without `sshTransport` puts the device back on the default. A response without `sshClientPath` cancels your pin. Claude Desktop then chooses the client as if you had pinned nothing (see **Client version** above). Where the built-in client connects, the first `ssh` on the user's `PATH` reads the SSH configuration and runs the terminal. Return both keys in the response too. Return a Windows path only in responses that go to Windows devices. `sshClientPath` has no per-platform form either, and SSH connections fail on a macOS or Linux device that gets a Windows path.
* **Keys that a bootstrap response leaves out**: where a response leaves out `sshTransport` or `sshClientPath` and the registry sets it, Claude Desktop 4.29.0 or later writes a line to `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) each time it connects to an SSH host. The line contains `the device profile sets` and names the key.
* **Devices on the Enterprise Admin Console**: the console's configuration replaces the registry's `sshTransport` and `sshClientPath`, even where the console leaves them unset. Set them in the console too. A client that isn't Microsoft's, or a value that starts with `%LOCALAPPDATA%\`, doesn't connect when it comes from the console. The console's `sshClientPath` reaches its macOS and Linux devices too, and SSH connections fail there under a Windows path. See [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization).
* **When a change takes effect**: at each host's next connection. An open app takes a change in the registry at its next configuration check. From a bootstrap server or the Enterprise Admin Console, an open app applies a new value only if it is `builtin`, once two configuration checks in a row return it. Other values wait, at the latest, until the app is reopened and has downloaded the configuration. A host that is connected keeps its client until the connection drops, which can take days. To move it at once on a Windows device, have the user quit and reopen Claude Desktop. After a change to the managed configuration the reopened app can fail to rejoin the engine, and a turn that still runs on the host is then cut short, as [How a remote session works](#how-a-remote-session-works) describes. A host that connects before the reopened app has downloaded the configuration goes by the registry's value with a bootstrap server. Where the registry sets none, and with the console, see **Configuration that hasn't loaded** above.
* **What `builtin` leaves on the device**: going back undoes nothing that was written while the OpenSSH client was in use. Saved passwords and new entries in the user's `known_hosts` file stay. The access list of a private key file that the app tightened stays too, and `ssh.log` recorded that list as it was before. The user's settings don't offer to forget a saved password under `builtin`, but removing the connection deletes it.

### SSH configuration on the device

Claude Desktop applies the host's entry in the user's `~/.ssh/config`. With the device's OpenSSH client, `ssh` reads the entry itself, so settings such as `ProxyJump`, certificate host keys, and GSSAPI authentication apply, and the app still connects only to the resolved hostname that passed `sshHostAllowlist`. The built-in client applies the hostname, port, user, identity file, SSH agent, and `ProxyCommand`.

* For hosts behind a bastion, configure a `ProxyJump` or `ProxyCommand`. `ProxyJump` works only when the device's OpenSSH client carries the connection. The built-in client refuses it. For the card that the user sees, see [Ask your IT administrator to set sshTransport to system-openssh](#ask-your-it-administrator-to-set-sshtransport-to-system-openssh).
* A bastion must match `sshHostAllowlist` too. See [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist).
* With the device's OpenSSH client, OpenSSH's own host key checking applies. For a host whose key isn't on record yet, where the app can show a prompt, it shows the key's fingerprint, asks the user whether to trust it, and records a trusted key in the user's `known_hosts` file, unless the user's own SSH configuration accepts new keys without asking. The app can't show a prompt on every connection, for example when it reconnects in the background. Distribute the host keys or a host certificate authority to the devices, so that each host's key is on record before users connect. `@cert-authority` entries are honored. A key that differs from the one on record for the host is refused, whatever the entry's `StrictHostKeyChecking` says, unless another setting in the SSH configuration that applies to the host takes that check away, such as `NoHostAuthenticationForLocalhost yes` for a host on a loopback address.
* With the device's OpenSSH client, you can keep the app from asking users to trust the key of a host that isn't on record yet. Distribute the host keys in the client's system-wide `known_hosts` file, such as `/etc/ssh/ssh_known_hosts`, or distribute a host certificate authority. Then set `StrictHostKeyChecking yes`, for example under `Host *`, in the client's system-wide configuration file, such as `/etc/ssh/ssh_config`, which also governs other uses of that client, such as `git` over SSH. Where the SSH configuration that applies to a host has `StrictHostKeyChecking yes`, Claude Desktop doesn't ask the user to trust such a key, and `ssh` refuses the host if it can't verify the key. A key that differs from the one on record is handled the same way with or without this setting. The setting doesn't bind the user. By OpenSSH's own rules, `ssh` reads the user's `~/.ssh/config` before the system-wide file and keeps the first value it finds for a setting, so a `StrictHostKeyChecking` line there applies in place of yours. `ssh` also accepts a key that the user adds to their own `known_hosts` file, but under `yes` a connection from a terminal doesn't record the key. A user who picks a host that `ssh` refuses sees "Couldn't connect to" followed by the host, with [SSH host key verification failed](#ssh-host-key-verification-failed) under **View details**.
* With the built-in client, the host's key must already be in the device's `~/.ssh/known_hosts` as a plain entry. The app does not prompt to accept a new key and does not evaluate `@cert-authority` entries, so have users connect once from a terminal before adding the host in the app.
* With the built-in client, an identity file protected by a passphrase is skipped, not prompted for. Load it into the SSH agent, or use an unencrypted key. With the device's OpenSSH client, the app asks for the passphrase once the host's key is verified, and skips the key if the user cancels.
* With the built-in client, a host reached through a `ProxyCommand` gets the same host key check as a host reached directly. Before Claude Desktop 2.9939.0, the built-in client skipped host key verification for such a host.
* With the built-in client, a host connects with its key unchecked when its entry sets `StrictHostKeyChecking no`, sets `UserKnownHostsFile` to `none` or `/dev/null`, and sets no `RevokedHostKeys`. The app shows no password or one-time code prompt for such a host, so it needs a key or SSH agent sign-in.
* The connection times out after 30 seconds. A larger `ConnectTimeout` in the host entry extends it, and then applies to every try.
* With the device's OpenSSH client on macOS and Linux, a route through a jump host or a `ProxyCommand` gets more time where no `ConnectTimeout` applies, except to a [host that allows one session per connection](#hosts-that-allow-one-session-per-connection). When a user starts a session and the first try times out, the second try has 90 seconds. The time that a sign-in dialog for a `ProxyJump` host is open doesn't count. A jump host's push approval or security key touch counts, and so does anything that a `ProxyCommand` waits for. If a connection still times out while the user types or approves, set a `ConnectTimeout` that leaves time for it. Reconnects that Claude Desktop starts on its own have 30 seconds a try, so a route that is always slow still needs `ConnectTimeout`. Before Claude Desktop 4.4212.0, the second try has 30 seconds, and the dialog's time counts.

With either client, the connection that carries the session leaves these settings off, whatever the entry says:

* **Forwarding**: `ForwardAgent`, `ForwardX11`, `Tunnel`, `LocalForward`, `RemoteForward`, and `DynamicForward`.
* **Kerberos delegation**: `GSSAPIDelegateCredentials`. The host doesn't receive the user's Kerberos ticket over this connection, even where the entry says `GSSAPIDelegateCredentials yes`. A `ProxyJump` host is reached by a separate `ssh`, which applies the jump host's own entry.
* **Commands**: `RemoteCommand` and `LocalCommand`.

Where the session's terminal can't use that connection, and always with the built-in client, the terminal runs its own `ssh`, which applies the entry's forwarding and Kerberos delegation settings. With `ForwardAgent yes` in the entry, that `ssh` forwards the user's SSH agent to the host.

### Use the OpenSSH client of Git for Windows

To have Windows devices connect with an OpenSSH client that isn't Microsoft's, such as the `ssh.exe` of Git for Windows, name the client in [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath). Unless `sshClientPath` names another client, the OpenSSH client that makes the connection on a Windows device is Microsoft's. Placing another client first on the `PATH` never lets that client make the connection. Requires Claude Desktop 3.6556.1 or later.

Name another client only on devices with one user, not on devices that several users share.

The client that you name makes the connection only if all of these conditions hold:

* **Folder**: the program is an `.exe` file under Program Files or Program Files (x86). For a program under a user's `AppData\Local` folder, see [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user).
* **Links**: with every link and junction on the path followed, the program is still under Program Files or Program Files (x86), and Windows can resolve the path. Before Claude Desktop 4.4212.0, Claude Desktop checked only the path as written, so a client that a junction places outside Program Files stops connecting when the device updates.
* **Version**: the program is OpenSSH 8.5 or later. To check, run the program with `-V` in a Command Prompt window, for example `"C:\Program Files\Git\usr\bin\ssh.exe" -V`.
* **`sshClientPath` and `sshTransport`**: `sshClientPath` holds the program's absolute path, and [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) is `system-openssh`.
* **Source of both settings**: both values come from [machine policy](https://claude.com/docs/third-party/claude-desktop/mdm.md#4-deploy-the-configuration) under `HKLM\SOFTWARE\Policies\Claude`, or from the [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) that machine policy names. Values from a user's own configuration file or from `HKCU` don't count. Neither do values from an admin-console organization that a user's own sign-in points the device to.
* **Trial start**: in each run of Claude Desktop, before the first connection, Claude Desktop starts the program without connecting. The program must accept the arguments and options that Claude Desktop passes. The `ssh.exe` of a current Git for Windows takes them.

Before you deliver `sshClientPath` and `sshTransport`, check for these devices:

* **Devices without the program**: with no file at the path that `sshClientPath` names, every SSH connection fails, whatever the value of `sshTransport`, and Claude Desktop's built-in SSH client doesn't take over. Install the program first, or deliver both settings only to devices that have it. A device that gets neither setting connects as before.
* **Devices with a bootstrap server**: once loaded, the server's response replaces machine policy's values, even for a setting that the response leaves out. A response that leaves `sshClientPath` out cancels your choice of client, and Microsoft's OpenSSH or the built-in client then connects. Return both settings in the response as well as in machine policy. Return `sshClientPath` only to Windows devices, because SSH connections fail on a macOS or Linux device that gets a Windows path.

If `sshTransport` is `system-openssh` and any other condition in the list doesn't hold, connections fail with the card "Ask your IT administrator to fix the configured SSH program". Claude Desktop never runs another `ssh` in the program's place.

With `system-openssh` and a client named in `sshClientPath`, Claude Desktop's built-in client tries the connection in one case only. In that case the program's file exists, but Windows won't start the program, or the program gives no answer when Claude Desktop starts it without connecting. That case ends as soon as the program has answered once since Claude Desktop opened.

To find the condition that doesn't hold, select **View details** on the card and read the line that starts with `Claude needs:`. `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the device names the condition too. The card says less in these cases:

* **The source of both settings is what fails**: the `Claude needs:` line names only Microsoft's OpenSSH, and the reason is in `ssh.log`.
* **The path isn't absolute, isn't an `.exe` file, or names no file**: **View details** shows no `Claude needs:` line, and `ssh.log` says only that the program is missing or can't be used.

With a client that isn't Microsoft's, plan for the following:

* **SSH files**: Claude Desktop points the client at the `.ssh` folder of the user's Windows profile. Git Bash on the same device can use another folder, so an SSH key or a `known_hosts` entry that works in Git Bash can be missing for Claude Desktop. **View details** on a failed sign-in then names both folders. For system-wide settings the client reads `etc\ssh` under Git's folder, not `%ProgramData%\ssh`.
* **Prompts**: Claude Desktop asks for a password, a one-time code, or a key passphrase only on a direct connection. A connection is direct if the SSH configuration gives the host no jump host, `ProxyCommand`, `KnownHostsCommand`, `PKCS11Provider`, or `SecurityKeyProvider`, and holds no `Match exec` line. Claude Desktop must also be able to confirm that the client uses the Windows profile's `.ssh` folder.
* **Sign-ins where Claude Desktop can't ask**: only an SSH key that needs nothing typed signs in. A sign-in that needs a prompt fails with the card "Ask your IT administrator about your organization's SSH program", and `ssh.log` names the cause.
* **Application control**: allow the client and the `ssh-keygen.exe` beside the client in your application control policy, as well as Claude Desktop's own [sign-in helpers](#this-computer-won%E2%80%99t-start-claude%E2%80%99s-ssh-sign-in-helper). Claude Desktop tests its prompts with that `ssh-keygen.exe`. While the test fails, only an SSH key that needs nothing typed signs in.

### Use an OpenSSH client installed per user

To have Windows devices connect with an OpenSSH client that your packaging installs under each user's `AppData\Local` folder, such as a per-user copy of Git for Windows, start the value of [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath) with `%LOCALAPPDATA%\`, for example `%LOCALAPPDATA%\Programs\Git\usr\bin\ssh.exe`. Such a value also needs [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) set to `system-openssh`. Requires Claude Desktop 4.4212.0 or later. An earlier version rejects the value, and every SSH connection on that device fails, so deliver the value only to devices that have updated.

> [!WARNING]
>
> Install the client under Program Files where your packaging allows it. Under `AppData\Local`, the user, and any program that runs as the user, can replace the client and the files that it loads. On these devices, the user can get around `sshClientPath` and `sshHostAllowlist`. A replaced client also sees SSH passwords and key passphrases, saved passwords included, and everything that the session sends and receives.

Use a per-user client only on devices with one user, not on devices that several users share.

The client makes the connection only if it meets the **Version**, **Source of both settings**, and **Trial start** conditions in [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows), and all of these conditions too:

* **Value in machine policy**: `sshClientPath` under `HKLM\SOFTWARE\Policies\Claude` is a string value (`REG_SZ`), not an expandable string (`REG_EXPAND_SZ`), and still starts with the text `%LOCALAPPDATA%\`. The tool that writes the value can expand the variable, so read the value back from the registry.
* **Same value from the bootstrap server**: on a device with a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md), set the value in machine policy and in the response. The response replaces machine policy's `sshClientPath` and `sshTransport`, even if it leaves them out, so return both. Claude Desktop accepts the value from a response only if machine policy has the same value, character for character. In JSON, write each backslash twice. Return the value to Windows devices only, because SSH connections fail on a macOS or Linux device that gets it.
* **No value from the admin console**: Claude Desktop rejects a value that the device gets from an [admin console organization](https://claude.com/docs/third-party/claude-desktop/admin-console.md), even if machine policy has the same value.
* **Real location**: with every link and junction on the path followed, the client is in `AppData\Local` under the signed-in user's profile folder, and Windows can resolve the path. Claude Desktop checks where the client is, not who can write to its folder, so make sure that no other user can.
* **No administrator rights**: Claude Desktop runs without administrator rights. It has those rights when it is started as administrator, and it can have them when a service, a scheduled task, or an SSH session starts it. It also has them under the built-in Administrator account, and for an administrator on a device with User Account Control turned off.

If a condition doesn't hold, or `sshTransport` is unset, `auto`, or `builtin`, SSH connections fail with the card "Ask your IT administrator to fix the configured SSH program". Claude Desktop's built-in SSH client tries the connection in one case only, where the per-user client's file exists but Windows won't start it or it gives no answer.

To find the cause, select **View details** on the card and read the line that starts with `ssh:`.

* **The line shows `%LOCALAPPDATA%`**: Claude Desktop rejected the value, and the card says that the program is missing or can't be run, even if it is there. Check the value in machine policy, the bootstrap response, the admin console, `sshTransport`, and administrator rights. To narrow the cause down, search `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the device for `sshClientPath begins with`. The last line that you find names the cause.
* **The line shows a path without the variable**: in the path, `~` stands for the user's profile folder. If no line under it starts with `Claude needs:`, the user has no `.exe` file at that path. A path in another account's folder, such as `C:\Windows\System32\config\systemprofile`, means that the tool that wrote the value expanded the variable. A `Claude needs:` line that asks for Program Files means that a link leads out of the user's `AppData\Local` folder, or that the value is a full path without the variable, in the registry or in the bootstrap response.
* **The line says that `sshClientPath` isn't a local absolute path**: the device runs an earlier version, the registry value is an expandable string, which Claude Desktop doesn't read, or the value has a mistake such as `..` or a second `%`.

With a per-user client, plan for the SSH files, prompts, and sign-ins that [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) describes, and for the following:

* **Application control**: allow the client and the `ssh-keygen.exe` beside the client in your application control policy. If your policy blocks the client, users don't see the card "Ask your IT administrator to fix the configured SSH program". The built-in client tries the connection, and `ssh.log` says that the program gave no answer.
* **Upgrades**: if the name of the client's folder contains a version number, change the value in machine policy and in the bootstrap response together with each upgrade. Prefer a folder name without a version to a junction, because through a junction Claude Desktop can stop reusing saved SSH passwords.
* **Moved or mounted profiles**: Claude Desktop looks in `AppData\Local` under the user's profile folder, even where the `LOCALAPPDATA` variable points elsewhere. It refuses a profile folder that is a UNC path, such as `\\server\profiles\user`. Where Windows mounts the profile from a profile container, test one device before you deliver the value to the others.
* **A changed or removed value**: a running Claude Desktop can keep using the client after you change or remove the value. Have users quit and reopen Claude Desktop.

## Troubleshoot

### Your organization doesn't allow this SSH connection

The `sshHostAllowlist` in effect on this device is unset, empty, or has no entry that matches the host or a jump host on the way to it. The card's details say which. The name that must match is the `HostName` that the device's `~/.ssh/config` resolves the entered host to, so an entry that lists only an alias doesn't allow the host. Which configuration source supplies the key on a device follows [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). For a device that moved to an admin console organization, see [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization). The connection test, and the "Couldn't connect to" card on the New session page, report the same denial as "Your organization's settings do not allow this connection." Before Claude Desktop 2.31226.0, the card's title was "SSH isn't allowed by your organization".

For a jump host, read the warning under [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist), then add the first name in the details to the allowlist. That name is the jump host's `HostName`, and the second name is the host that the user entered.

```text theme={null}
SSH host "bastion.corp.example.com" is not allowed by your organization's managed settings. It is a jump host on the way to "build01".
```

If the next attempt names another jump host, add that one too. To find every name beforehand, see [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist). Requires Claude Desktop 3.1623.0 or later.

### SSH to this device isn't available

The host resolves to the device itself (`localhost`, `127.0.0.1`, or a tunnel or port forward that ends on the device) while `allowedWorkspaceFolders` restricts workspace folders. A session over SSH to the device reaches the same disk the policy restricts, so it is refused. Connect to a different host, or use a local session unless `disableDesktopLocalSessions` turns those off. Before Claude Desktop 2.31226.0, the card's title was "SSH to this machine isn't available".

### SSH sessions can't use your model provider settings

The configured inference credential is one of the kinds listed as refused under [Inference credentials on the remote host](#inference-credentials-on-the-remote-host), or the inference endpoint is on the device itself. The card's details say which. Switch the deployment to a credential kind that works on a remote host, or point the app at an endpoint the host can reach. Before Claude Desktop 2.31226.0, the card's title was "Remote sessions aren't available with this inference setup".

### SSH host key verification failed

The host's key has changed, or it is not in the device's `~/.ssh/known_hosts` and was not trusted in the app (the built-in client never asks). Connect to the host from a terminal on the device to check and record the current key, then retry.

With the device's OpenSSH client, if `StrictHostKeyChecking yes` applies to the host, connecting from a terminal doesn't record its key. Instead, check the key and add it to the system-wide `known_hosts` file, or give the host a certificate from your host certificate authority (see [SSH configuration on the device](#ssh-configuration-on-the-device)).

### Ask your IT administrator to set sshTransport to system-openssh

The built-in client made the connection, and the host needs the device's OpenSSH client. Where the app can name a step, the card's title gives it, and the card's text gives the cause, either "Claude's built-in SSH library can't connect through a jump host (ProxyJump)." or "Claude's built-in SSH library can't check host keys against a certificate authority or another known\_hosts file."

* **"Ask your IT administrator to set sshTransport to system-openssh"**: the built-in client is the device's default, and the device has a usable OpenSSH client. Set [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) to `system-openssh`. Claude Desktop 4.5284.0 or later doesn't show this title: the OpenSSH client makes the connection instead.
* **"Ask your IT administrator to change sshTransport from builtin to system-openssh"**: your configuration sets `sshTransport` to `builtin`. Change it to `system-openssh`.
* **"Ask your admin to correct the sshTransport setting"**: the app can't read the value that your configuration gives `sshTransport`, for example a misspelling, so the built-in client makes the connection. Correct the value. Requires Claude Desktop 2.37337.0 or later.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer and set sshTransport to system-openssh, then quit and reopen Claude"**: the built-in client is the device's default, and the app found no usable OpenSSH client on the device. Install the client, and set the key. Claude Desktop 4.5284.0 or later shows the next title instead.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer, then quit and reopen Claude"**: the app found no usable OpenSSH client on the device. Install the client. Before Claude Desktop 4.5284.0, this title appears only where `sshTransport` is `system-openssh`.
* **"Check your network or VPN and try again, or quit and reopen Claude"**: the device's configuration from the Enterprise Admin Console or a bootstrap server hasn't loaded, so the built-in client made the connection. Requires Claude Desktop 4.5284.0 or later.
* **"Quit and reopen Claude; if this comes back, ask your IT administrator to let Claude use the system OpenSSH client"**: the device couldn't start the OpenSSH client earlier in this run of the app (see [Host requirements](#host-requirements)).

Where the app can name no step, the card's title gives the cause, either `<host> needs a jump host, which Claude can't use here` or `Claude can't check <host>'s key here`.

These cards require Claude Desktop 2.31226.0 or later. Before Claude Desktop 2.31226.0, the built-in client refused a `ProxyJump` host with a message that suggests `ProxyCommand`.

### Ask your IT administrator to fix the configured SSH program

The program that `sshClientPath` names is missing, can't be run, is too old, or on Windows doesn't meet the conditions for its kind. Claude Desktop never runs another `ssh` in its place. Select **View details** on the card for the program's path. On a Windows device, to find the condition, see [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) or [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user). With no `sshClientPath`, the card appears on a macOS or Linux device where `sshTransport` is `system-openssh` and the device can't start its own `ssh`. A Windows device in that state connects with the built-in client.

### This computer won't start Claude's SSH sign-in helper

Where the device's OpenSSH client makes the connection, the operating system refused to start one of the helper programs that show `ssh`'s prompts. Without them the app can't ask for a password, a one-time code, or a key passphrase, so a sign-in that needs one fails. Select **View details** on the card for the blocked program's path and, where the operating system gave one, the error code. Allow the program:

* **Windows devices**, with Claude Desktop 2.37337.0 or later: allow the helper programs as described under [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client), then have the user try again. With Claude Desktop 4.5284.0 or later and `sshTransport` unset or `auto`, the [built-in client connects instead](#prepare-windows-devices-for-the-openssh-client) where the app itself can't start the helper. The host then stays on that client.
* **macOS and Linux devices**, with Claude Desktop 4.16336.0 or later: allow `claude-ssh-askpass` in the folder that **View details** names, then have the user try again. On these devices the built-in client never connects instead. With `spawn EACCES` on a Linux device, check too that the folder isn't mounted `noexec`.

While the fault lasts, Claude Desktop can't reconnect by itself with a saved password. It shows the card only while a user waits for the connection, for example after they start a session or send a message. On a Windows device, the card appears only for a host that accepts a password or a one-time code.

### Claude's SSH sign-in helper isn't working on this computer

On a macOS or Linux device, `claude-ssh-askpass` is missing or doesn't work, though the operating system didn't refuse to start it. Without it the app can't ask for a password, a one-time code, or a key passphrase, so a sign-in that needs one fails. Select **View details** and match the line that starts with `What failed:`:

* **`it is missing`**: reinstall Claude Desktop, then have the user try again.
* **`its test run failed`, `its test run timed out`, `its test run sent no answer`, or `its test run could not be started`**: have the user try again. If the card comes back, have them quit and reopen Claude Desktop, which an update installed under the running app can call for. If it still comes back, reinstall the app.
* **`ssh seems unable to start it, though Claude can`**: allow `ssh` to start the helper in your application control policy. Have the user wait until then, because each try can send the host empty passwords, which can count toward an account lockout.
* **`it cannot reach Claude because ssh's stderr is redirected, for example by a wrapper script`**: look for a wrapper around `ssh`. Change the program that `sshClientPath` names, or the `ssh` first on the user's `PATH`, so that it leaves standard error untouched.

While the fault lasts, Claude Desktop can't reconnect by itself with a saved password. It shows the card only while a user waits for the connection, for example after they start a session or send a message. Requires Claude Desktop 4.16336.0 or later.

### This computer's ssh refuses a backslash or dollar sign in user names

On a macOS or Linux device where the device's OpenSSH client makes the connection, that client refuses the user name on its command line because the name has a `\` or a `$`, as in `DOMAIN\user`. Claude Desktop passes such a name to `ssh` in a configuration file that it writes, and shows this card where it can't. Select **View details** on the card and match the last line:

* **`needs the Include line in this file to use a full path`**: the system's `ssh_config`, or a file read through it, has an `Include` with a relative path. The line names the file. Write that path in full, starting with `/`.
* **`couldn't find which system ssh_config this ssh reads` or `couldn't write that file`**: have the user try again. With the second, the app couldn't write the file in a private temporary folder.
* **`the name is the jump host's`**: the card's title is "This computer's ssh refuses the jump host's user name". In the user's `~/.ssh/config`, move the name from `ProxyJump` to a `User` line in the jump host's own `Host` block.

This card requires Claude Desktop 2.37337.0 or later.

### Setup on the host fails after SSH connects

SSH connected, but Claude Desktop couldn't place or start the remote server or the engine on the host. Select **View details** on the failure card to read the app's own message, which can end with a code in square brackets. Match the code, or the start of the message:

* **`[SFTP_UNAVAILABLE]`**: the host's SSH server refused the SFTP subsystem. Enable `Subsystem sftp` in the server's `sshd_config`, or see what a session needs under [Hosts without SFTP](#hosts-without-sftp).
* **`[SESSION_LIMIT]`**: the host's SSH server refused to open another session on the connection. If the host has to keep its `MaxSessions` limit, update the macOS or Linux device to Claude Desktop 3.1623.0 or later, and see [Hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection). Otherwise, raise `MaxSessions` in the server's `sshd_config`, for example to OpenSSH's default of 10, and reload the SSH server.
* **`[SFTP_NOT_STARTED]`**: the host's SSH server accepted the request for SFTP, but the SFTP server ended before its first answer, or text arrived in place of that answer. In a terminal on the device, run `sftp` with the same host, for example `sftp user@build01.corp.example.com`, to see what stops it. Then check the settings and files that the message names, or see what a session needs under [Hosts without SFTP](#hosts-without-sftp).
* **`[EXEC_NO_INPUT]`**: the host's SSH server ran the app's command but passed it no input, which setup and the session's own link need. In a terminal on the device, run `echo hi | ssh` with the same host and `cat`, for example `echo hi | ssh user@build01.corp.example.com cat`. It prints `hi` on a host that passes input. Have the host's administrator let commands run over SSH receive input.
* **`[ENOSPC]` or `[EDQUOT]`**: a disk is full, or a quota is used up. In a message that starts with `Couldn't prepare the deploy locally`, the disk is the device's. In any other message it is the host's, so free space in the SSH user's home directory. [Host requirements](#host-requirements) gives the space the app needs.
* **`Unsupported remote platform`**: the host's operating system or processor isn't among those under [Host requirements](#host-requirements).
* **`[CLI_NOT_RUNNABLE]`**: the remote server installed the engine, but the engine's first run didn't start or didn't exit cleanly, so the remote server removed it. One cause is a glibc older than 2.17. Run `ldd --version` on the host to check. Before Claude Desktop 2.37337.0, the message has no code and starts with `Couldn't install the Claude CLI on the remote (cli archive)`.
* **`[NO_INSTALL_RESULT]`**: the remote server's install step printed no result. A home directory mounted `noexec` is one cause, where the host's error message doesn't say `Permission denied` or `Operation not permitted`. Where it does, the code is `[SERVER_NOT_RUNNABLE]`. Before Claude Desktop 4.4212.0, a host with SFTP gets `[NO_INSTALL_RESULT]` in both cases.
* **`[SETUP_DIR_NOEXEC]`**: on a [host without SFTP](#hosts-without-sftp), the host didn't run a test program from `~/.claude/remote` in the SSH user's home directory, so the app didn't copy the remote server. A home directory mounted `noexec` and a restricted login shell are two causes. Have the host's administrator let the SSH user run programs from `~/.claude/remote`.
* **`[SERVER_NOT_RUNNABLE]`**: the remote server didn't run from `~/.claude/remote` in the SSH user's home directory, or stopped before it answered. A home directory mounted `noexec` is one cause, and security software on the host that keeps programs from running there is another. Have the host's administrator check that programs can run from that folder. Before Claude Desktop 4.4212.0, the code appears only on a [host without SFTP](#hosts-without-sftp).
* **`[DOWNLOAD_BUSY]`**: Anthropic's download server answered that it is busy, so Claude Desktop couldn't download the engine or the remote server to the device. Claude Desktop has already waited and asked again. Have the user try again in a few minutes. If the code keeps coming back, check whether a proxy on the device's network limits downloads from `downloads.claude.ai`, because a proxy can give the same answer.

`[SESSION_LIMIT]` and `[SFTP_NOT_STARTED]` require Claude Desktop 2.31226.0 or later, and appear only when the device's OpenSSH client makes the connection. `[SESSION_LIMIT]` appears only on macOS and Linux devices. Their cards are titled `<host> allows too few SSH sessions per connection` and `SFTP doesn't start on <host>`.

`[CLI_NOT_RUNNABLE]` and `[EXEC_NO_INPUT]` require Claude Desktop 2.37337.0 or later. `[EXEC_NO_INPUT]` appears only where the device's OpenSSH client makes the connection. Their cards are titled `Claude Code didn't run on <host>` and `Ask <host>'s administrator to let SSH commands receive input`. From the same version, the card is titled `Couldn't copy Claude Code to <host>` where the app couldn't put its files on the host, and `Couldn't install Claude Code on <host>` where the engine's install failed, each for a cause with no card of its own.

Before Claude Desktop 4.29.0, the `[EXEC_NO_INPUT]` card is titled `<host> doesn't pass input to commands run over SSH`.

`[SETUP_DIR_NOEXEC]` and `[SERVER_NOT_RUNNABLE]` require Claude Desktop 3.1623.0 or later. Their card is titled `Ask <host>'s administrator to let Claude's server run`.

`[DOWNLOAD_BUSY]` requires Claude Desktop 4.4212.0 or later, and its card is titled `Try again in a few minutes`. Before Claude Desktop 4.4212.0, the card for `[SETUP_DIR_NOEXEC]` and `[SERVER_NOT_RUNNABLE]` is titled `Claude's server didn't run on <host>`.

### Git commands fail with Read-only file system

Git commands fail with this error when the user opens the session in a subfolder of a Git repository, on a Linux host where the sandbox from your policy runs. Git's message then reads, for example, `Unable to create '<path>/.git/index.lock': Read-only file system`. To find out whether the sandbox runs there, see [Sandbox status on the remote host](#sandbox-status-on-the-remote-host).

The sandbox lets shell commands that Claude runs with its Bash tool write in the folder the session was opened in, and the repository's `.git` folder is outside that folder. Of these commands, the ones that write to the `.git` folder fail, such as `git add` and `git commit`. Have the user start a new session at the top of the repository.

> [!NOTE]
>
> These cases are covered elsewhere:
>
> * **An `allowedWorkspaceFolders` entry with `mode` set to `ro`**: see [Read-only folders on the remote host](#read-only-folders-on-the-remote-host)
> * **A message with `unable to unlink old`**: see [A git command fails with `unable to unlink old`](https://code.claude.com/docs/en/sandboxing#a-git-command-fails-with-unable-to-unlink-old)
> * **The other places that the sandbox lets these commands write to**: see [Filesystem isolation](https://code.claude.com/docs/en/sandboxing#filesystem-isolation) and the `allowedWorkspaceFolders` row under [Applied as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy)

## Related

* [Code in Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/code.md)
* [`sshHostAllowlist` in the configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist)
* [Desktop and filesystem access](https://claude.com/docs/third-party/claude-desktop/local-access.md)
