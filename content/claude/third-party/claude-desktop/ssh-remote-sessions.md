> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH remote sessions in Claude Desktop on 3P

> How Code sessions run on a remote host over SSH in Claude Desktop on 3P, the sshHostAllowlist key that enables them, which inference credentials work on a remote host, and what to check before turning them on

An SSH remote session is a [Code](/docs/third-party/claude-desktop/code) session whose Claude Code engine runs on another machine that the user reaches over SSH, while the session's interface stays in Claude Desktop on the user's device. Claude Desktop connects to the host, places the engine there, and starts the session with the inference credential and policy from your managed configuration. Users can work on code that lives on a development server, a build box, or a cloud workstation without copying it to their device. In Claude Desktop on third-party (3P), SSH remote sessions are off until you set the [`sshHostAllowlist`](/docs/third-party/claude-desktop/configuration#sshhostallowlist) key, because enabling them sends your inference credential to the hosts users connect to.

<Note>
  SSH remote sessions are in beta in Claude Desktop on 3P and require Claude Desktop 1.40609.0 or later. The in-app configuration window marks `sshHostAllowlist` with a **Beta** pill.
</Note>

## How a remote session works

1. **Connect.** The user picks an SSH host from the environment picker in Code, or adds one by entering its address, port, and an identity file. Claude Desktop connects through the device's OpenSSH client on macOS and Linux, or its built-in SSH client on Windows (see [Host requirements](#host-requirements) to change either default), applies the host's entry from the device's `~/.ssh/config` (see [SSH configuration on the device](#ssh-configuration-on-the-device)), and prompts in the app if the host asks for a password or a one-time code.
2. **Deploy.** Claude Desktop places a remote server and the Claude Code engine under `~/.claude/remote/` in the SSH user's home directory on the host ([Host requirements](#host-requirements) lists every path) and reuses them on later connections.
3. **Run.** The remote server starts the engine on the host with the inference credential and policy from your managed configuration. Every file read, edit, shell command, and git operation runs on the host, in the working directory the user chose there. Claude Desktop connects to [managed MCP servers](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin) from the device and exposes them to the engine as tools.
4. **Stream.** Claude's responses and tool output stream back to Claude Desktop. Permission prompts appear in Claude Desktop, and the engine waits on the host until the user answers.

The engine keeps running on the host through a dropped SSH link, device sleep, or the user quitting Claude Desktop. It finishes the current turn, or stops at a permission prompt, then idles until the user reopens the session. Reopening starts a fresh engine from the transcript stored on the host, so a turn that finished while the app was closed is shown in full; a turn still running at that moment is cut short and not continued automatically. While Claude Desktop is closed, no new turns run and the inference credential is not refreshed, so a turn that outlives the credential fails with an authentication error.

On a host that ends a user's processes at logout, the remote server and the engine end with the SSH connection that started them, so a turn in progress doesn't survive a disconnect. Linux hosts where systemd-logind's `KillUserProcesses` setting is `yes` and applies to the SSH user behave this way. To keep remote sessions running through a disconnect on such a host, ask the host's administrator to exempt the SSH user, for example by listing the user under `KillExcludeUsers` in the systemd-logind configuration.

An idle engine stays on the host, with the credential in its environment, until one of these happens:

* The user reopens, archives, or deletes the session.
* The host restarts.
* A Claude Desktop update replaces the remote server on the host (deferred while a session on that host was active in the last 24 hours, for up to 7 days).
* On a Linux or macOS host, 30 days pass without a connection from Claude Desktop to the remote server. The remote server then stops and ends its engines. Requires Claude Desktop 1.52386.0 or later.

While Claude Desktop is disconnected, the remote server keeps the most recent output of each running engine in a 16 MiB buffer. It drops older output, and the engine keeps running.

On a Linux or macOS host, if Claude Desktop stayed open, it rejoins the running engine when it reconnects after device sleep or a dropped SSH link. It catches up from the buffer, and loads the part of the conversation that the buffer has dropped from the transcript stored on the host. If it can't load all of it, the session shows "Some output produced while you were disconnected may be missing here."

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

1. `sshHostAllowlist` from the Claude Desktop configuration, when that configuration is delivered by an administrator: through machine-scoped device management (`HKLM` policy on Windows, a configuration profile on macOS, `/etc/claude-desktop` on Linux), or by a bootstrap server the app trusts (a `bootstrapUrl` set through device management or covered by `trustBootstrapDelivery`; see [Keys that require user consent](/docs/third-party/claude-desktop/bootstrap#keys-that-require-user-consent)). User-scope registry policy (`HKCU`) counts as applied locally.
2. `sshHostAllowlist` from Claude Code's managed settings on the device.
3. `sshHostAllowlist` from a Claude Desktop configuration the user applied locally in the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration#apply-locally-or-export-for-a-fleet).
4. Off.

On devices where users applied the configuration locally, deploy `sshHostAllowlist` in Claude Code's managed settings. That restricts SSH without an MDM profile taking ownership of the whole configuration (see [Update keys and managed precedence](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence)).

## Inference credentials on the remote host

<Warning>
  A remote session runs Claude Code on the SSH host with your organization's inference credential in its process environment, for as long as that process runs, including while Claude Desktop is closed. Anyone who can read that process's environment on the host, such as the same user account or a root user, can read the credential. List only hosts you trust with it, and prefer a credential that expires (single sign-on, or a credential helper that issues short-lived tokens) over a long-lived key.
</Warning>

The remote engine uses only the credential Claude Desktop passes in its environment. It ignores credentials already on the host, such as an AWS profile or application default credentials, and Claude Desktop copies no credential files there. Credential kinds that live in a file on the device are refused at session start.

| Provider | Works on a remote host | Refused at session start |
| - | - | - |
| [LLM gateway](/docs/third-party/claude-desktop/gateway) | Static API key, single sign-on, credential helper | |
| [Claude API](/docs/third-party/claude-desktop/claude-api) | Static API key, Sign in with Claude Console, credential helper | |
| [Microsoft Foundry](/docs/third-party/claude-desktop/foundry) | API key, in-app Entra ID sign-in, credential helper | |
| [Amazon Bedrock](/docs/third-party/claude-desktop/bedrock) | Bearer token, identity provider sign-in, credential helper | In-app AWS sign-in (IAM Identity Center), named profile |
| [Amazon Bedrock Mantle](/docs/third-party/claude-desktop/mantle) | Bearer token, credential helper | |
| [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex) | In-app Workforce Identity sign-in, credential helper | In-app Google sign-in, service-account key or credentials file, application default credentials on the device |

When the configured credential is a refused kind, the session fails before anything is deployed to the host, with the card [Remote sessions aren't available with this inference setup](#remote-sessions-aren%E2%80%99t-available-with-this-inference-setup).

When the remote engine's credential expires during a turn, Claude Desktop obtains a new one on the device, by re-running a [credential helper](/docs/third-party/claude-desktop/credential-helper) or using a sign-in's refresh token, and sends it over the SSH connection. When the user signs out of the inference provider in the app, Claude Desktop ends the remote engine.

The host needs its own network route to the inference endpoint and must trust the endpoint's certificate. Claude Desktop passes the endpoint address to the remote engine but not the device's proxy settings, CA certificates, or the user's shell variables such as `AWS_*` or `GOOGLE_*`. A gateway at `localhost` on the device is refused for remote sessions, because the host cannot reach it.

## Managed configuration on the remote host

Most of the policy that Claude Desktop applies to a local Code session applies on the remote host too. The [Code page](/docs/third-party/claude-desktop/code#how-configuration-propagates) describes how each key reaches Claude Code.

* `disableEssentialTelemetry` and `disableNonessentialTelemetry`.
* `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`, and `otlpContentCapture`. Remote sessions appear in your collector under the same `service.name` as local Code sessions. A collector at `localhost` on the device is not forwarded. An `otlpHeadersHelper` runs on the device at session start, and the remote session keeps those headers for its lifetime.
* `disabledBuiltinTools`, `builtinToolPolicy`, `autoModeEnabled`, and `disableBypassPermissionsMode`.
* [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), evaluated against the host's filesystem. `~` is the SSH user's home on the host, `%VAR%` entries are ignored, and Claude Desktop refuses to start a session in a directory outside every entry, so a fleet value such as `~/Documents/Claude` confines remote sessions to that path under the SSH user's home. A folder with `mode` set to `ro` is allowed on the host but not read-only there.
* [`blockReadsOutsideWorkingDirectories`](/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories), evaluated on the host, so the working directories and the home directory it hides from shell commands are the SSH user's there. Hiding files from shell commands needs the host's sandbox dependencies (next item); on a host without them, or a Windows host, shell reads outside the working directories ask for approval instead, and the file-tool restriction applies regardless. Files a user attaches to a remote session stay readable, except on a Windows host, where the session's plugin files and attachments stay outside the file tools' reach under this key.
* `coworkEgressAllowedHosts`, as Claude Code managed settings. The network and filesystem sandbox it produces with `allowedWorkspaceFolders` depends on the host having Claude Code's sandbox dependencies installed (see [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)). Without them, commands run unsandboxed. See [Sandbox status on the remote host](#sandbox-status-on-the-remote-host) for the message the session shows.
* `managedMcpServers`, as the Claude Code managed setting that keeps users from adding their own MCP servers. The managed servers themselves are reached from the device.
* Plugins from your [allowed marketplaces](/docs/third-party/claude-desktop/extensions), copied to the host. A plugin's `hooks` directory is not copied, so its hooks do not run in a remote session, and a plugin whose manifest declares hooks elsewhere is not copied at all.

If the host has its own Claude Code managed settings, those take precedence over the policy Claude Desktop supplies, as described under [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) for local sessions.

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
| `~/.claude/remote/ccd-cli/<version>` | The Claude Code engine, one file per version (the three most recent versions are kept) |
| `~/.claude/remote/run/<id>/` | The server's socket, token, and log |
| `~/.claude/remote/plugins/<id>/` | Plugins synced from the device, in one folder for each Claude Desktop installation that connects |
| `~/.claude/uploads/<session-id>/` | Files the user attached to a message. Not removed when the session ends |
| `~/.claude/` and `~/.claude.json` | Claude Code's own data, including session transcripts. See [Data storage](/docs/third-party/claude-desktop/data-storage) |

Each side of a remote session needs its own network access.

* Devices installed with the regular installer must reach `downloads.claude.ai`: Claude Desktop downloads the remote server there and uploads it to the host over SFTP. Devices installed with the [offline installer](/docs/third-party/claude-desktop/installation#offline-installation) don't: it bundles the remote server and the Claude Code engine for Linux x64 and arm64 hosts, and Claude Desktop uploads both over SFTP. Hosts on other platforms still need the download, so an offline-installed device that cannot reach `downloads.claude.ai` fails the session with a message saying the installer doesn't include remote components for that platform.
* The host must reach your inference endpoint and, if configured, your OTLP collector, plus whatever the user's own work needs. With the regular installer, it downloads the Claude Code engine from `downloads.claude.ai` when it can; when that fails, Claude Desktop downloads the engine on the device and uploads it over SFTP. Unless you disabled telemetry, the engine on the host also reports to the same Anthropic hosts as a local Code session (see [Telemetry and egress](/docs/third-party/claude-desktop/telemetry)). Blocking them does not affect the session.

### SSH configuration on the device

Claude Desktop applies the host's entry in the user's `~/.ssh/config`. With the device's OpenSSH client (the default on macOS and Linux), `ssh` reads the entry itself, so settings such as `ProxyJump`, certificate host keys, and GSSAPI authentication apply, and the app still connects only to the resolved hostname that passed `sshHostAllowlist`. The built-in client (the default on Windows) applies the hostname, port, user, identity file, SSH agent, and `ProxyCommand`.

* For hosts behind a bastion, configure a `ProxyJump` or `ProxyCommand`. `ProxyJump` works only when the device's OpenSSH client carries the connection (the default on macOS and Linux); the built-in client refuses it with a message suggesting `ProxyCommand`.
* With the device's OpenSSH client, OpenSSH's own host key checking applies. For a host whose key isn't on record yet, where the app can show a prompt, it shows the key's fingerprint, asks the user whether to trust it, and records a trusted key in the user's `known_hosts` file, unless the user's own SSH configuration accepts new keys without asking. The app can't show a prompt on every connection, for example when it reconnects in the background. Distribute the host keys or a host certificate authority to the devices, so that each host's key is on record before users connect. `@cert-authority` entries are honored. A key that differs from the one on record for the host is refused, whatever the entry's `StrictHostKeyChecking` says, unless another setting in the SSH configuration that applies to the host takes that check away, such as `NoHostAuthenticationForLocalhost yes` for a host on a loopback address.
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

### SSH isn't allowed by your organization

The `sshHostAllowlist` in effect on this device is unset, empty, or has no entry that matches the host. The card's details say which. The name that must match is the `HostName` that the device's `~/.ssh/config` resolves the entered host to, so an entry that lists only an alias doesn't allow the host. Which configuration source supplies the key on a device follows [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). The connection test reports the same denial as "Your organization's settings do not allow this connection."

### SSH to this machine isn't available

The host resolves to the device itself (`localhost`, `127.0.0.1`, or a tunnel or port forward that ends on the device) while `allowedWorkspaceFolders` restricts workspace folders. A session over SSH to the device reaches the same disk the policy restricts, so it is refused. Connect to a different host, or use a local session.

### Remote sessions aren't available with this inference setup

The configured inference credential is one of the kinds listed as refused under [Inference credentials on the remote host](#inference-credentials-on-the-remote-host), or the inference endpoint is on the device itself. The card's details say which. Switch the deployment to a credential kind that works on a remote host, or point the app at an endpoint the host can reach.

### SSH host key verification failed

The host's key has changed, or it is not in the device's `~/.ssh/known_hosts` and was not trusted in the app (the built-in client never asks). Connect to the host from a terminal on the device to check and record the current key, then retry.

### Setup on the host fails after SSH connects

SSH connected, but Claude Desktop couldn't place or start the remote server or the engine on the host. Select **View details** on the failure card to read the app's own message, which can end with a code in square brackets. Match the code, or the start of the message:

* **`[SFTP_UNAVAILABLE]`**: the host's SSH server refused the SFTP subsystem. Enable `Subsystem sftp` in the server's `sshd_config`.
* **`[ENOSPC]` or `[EDQUOT]`**: a disk is full, or a quota is used up. In a message that starts with `Couldn't prepare the deploy locally`, the disk is the device's. In any other message it is the host's, so free space in the SSH user's home directory. [Host requirements](#host-requirements) gives the space the app needs.
* **`Unsupported remote platform`**: the host's operating system or processor isn't among those under [Host requirements](#host-requirements).
* **`Couldn't install the Claude CLI on the remote (cli archive)`, with no code**: the engine's install on the host failed. One cause is a glibc older than 2.17, where the engine can't start and the remote server removes it. Run `ldd --version` on the host to check.
* **`[NO_INSTALL_RESULT]`**: the remote server's install step printed no result. A home directory mounted `noexec` is one cause.

## Related

* [Code in Claude Desktop on 3P](/docs/third-party/claude-desktop/code)
* [`sshHostAllowlist` in the configuration reference](/docs/third-party/claude-desktop/configuration#sshhostallowlist)
* [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access)
