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

1. **Connect.** The user picks an SSH host from the environment picker in the Code tab, or adds one by entering its address, port, and an identity file. Claude Desktop connects with its built-in SSH client, applies the host's entry from the device's `~/.ssh/config` (see [SSH configuration on the device](#ssh-configuration-on-the-device)), and prompts in the app if the host asks for a password or a one-time code.
2. **Deploy.** Claude Desktop places a remote server and the Claude Code engine under `~/.claude/remote/` in the SSH user's home directory on the host ([Host requirements](#host-requirements) lists every path) and reuses them on later connections.
3. **Run.** The remote server starts the engine on the host with the inference credential and policy from your managed configuration. Every file read, edit, shell command, and git operation runs on the host, in the working directory the user chose there. Claude Desktop connects to [managed MCP servers](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin) from the device and exposes them to the engine as tools.
4. **Stream.** Claude's responses and tool output stream back to Claude Desktop. Permission prompts appear in the Code tab, and the engine waits on the host until the user answers.

The engine keeps running on the host through a dropped SSH link, device sleep, or the user quitting Claude Desktop. It finishes the current turn, or stops at a permission prompt, then idles until the user reopens the session. Reopening starts a fresh engine from the transcript stored on the host, so a turn that finished while the app was closed is shown in full; a turn still running at that moment is cut short and not continued automatically. While Claude Desktop is closed, no new turns run and the inference credential is not refreshed, so a turn that outlives the credential fails with an authentication error.

An idle engine stays on the host, with the credential in its environment, until the user reopens, archives, or deletes the session, the host restarts, or a Claude Desktop update replaces the remote server on the host (deferred while a session on that host was active in the last 24 hours, for up to 7 days).

## Enable SSH remote sessions

Set [`sshHostAllowlist`](/docs/third-party/claude-desktop/configuration#sshhostallowlist) in your managed configuration. It appears in the **Code surface** section of the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) while Code is enabled.

| Value                                               | Behavior                                                                                                                                                                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unset                                               | Off, unless a Claude Code managed-settings `sshHostAllowlist` on the device allows hosts (see [Interaction with Claude Code managed settings](#interaction-with-claude-code-managed-settings-on-the-device)) |
| `[]`                                                | Off. Delivered by an administrator, `[]` also overrides a Claude Code managed-settings allowlist on the device                                                                                               |
| `["*"]`                                             | Users can connect to any host                                                                                                                                                                                |
| `["build01.corp.example.com", "*.dev.example.com"]` | Users can connect only to hosts that match an entry                                                                                                                                                          |

While SSH remote sessions are off, the environment picker shows local sessions only, and any attempt to connect to a saved host is refused.

Each entry is an exact hostname, an IP address, or a `*.` wildcard.

* `*.dev.example.com` matches `dev.example.com` and any subdomain of it at any depth.
* Matching is case-insensitive and ignores a `user@` prefix.
* An IP address entry matches only that address.
* Entries do not restrict the port.
* A value that is not an array of strings counts as `[]`.

Both the host the user entered and the `HostName` that the device's `~/.ssh/config` resolves it to must match an entry, so an alias that resolves to a host outside the list is refused. A `ProxyCommand` is permitted when the resolved hostname matches; the app does not inspect where the command itself connects. The allowlist limits which hosts Claude Desktop connects to. It does not limit what the device can reach over SSH from a terminal. Use network controls for that.

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

| Provider                                                            | Works on a remote host                                         | Refused at session start                                                                                      |
| ------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [LLM gateway](/docs/third-party/claude-desktop/gateway)                  | Static API key, single sign-on, credential helper              |                                                                                                               |
| [Claude API](/docs/third-party/claude-desktop/claude-api)                | Static API key, Sign in with Claude Console, credential helper |                                                                                                               |
| [Microsoft Foundry](/docs/third-party/claude-desktop/foundry)            | API key, in-app Entra ID sign-in, credential helper            |                                                                                                               |
| [Amazon Bedrock](/docs/third-party/claude-desktop/bedrock)               | Bearer token, credential helper                                | In-app AWS sign-in (IAM Identity Center), named profile                                                       |
| [Amazon Bedrock Mantle](/docs/third-party/claude-desktop/mantle)         | Bearer token, credential helper                                |                                                                                                               |
| [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex) | In-app Workforce Identity sign-in, credential helper           | In-app Google sign-in, service-account key or credentials file, application default credentials on the device |

When the configured credential is a refused kind, the session fails before anything is deployed to the host, with the card [Remote sessions aren't available with this inference setup](#remote-sessions-aren%E2%80%99t-available-with-this-inference-setup).

When the remote engine's credential expires during a turn, Claude Desktop obtains a new one on the device, by re-running a [credential helper](/docs/third-party/claude-desktop/credential-helper) or using a sign-in's refresh token, and sends it over the SSH connection. When the user signs out of the inference provider in the app, Claude Desktop ends the remote engine.

The host needs its own network route to the inference endpoint and must trust the endpoint's certificate. Claude Desktop passes the endpoint address to the remote engine but not the device's proxy settings, CA certificates, or the user's shell variables such as `AWS_*` or `GOOGLE_*`. A gateway at `localhost` on the device is refused for remote sessions, because the host cannot reach it.

## Managed configuration on the remote host

Most of the policy that Claude Desktop applies to a local Code session applies on the remote host too. The [Code page](/docs/third-party/claude-desktop/code#how-configuration-propagates) describes how each key reaches Claude Code.

* `disableEssentialTelemetry` and `disableNonessentialTelemetry`.
* `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`, and `otlpContentCapture`. Remote sessions appear in your collector under the same `service.name` as local Code sessions. A collector at `localhost` on the device is not forwarded. An `otlpHeadersHelper` runs on the device at session start, and the remote session keeps those headers for its lifetime.
* `disabledBuiltinTools`, `builtinToolPolicy`, and `autoModeEnabled`.
* [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), evaluated against the host's filesystem. `~` is the SSH user's home on the host, `%VAR%` entries are ignored, and Claude Desktop refuses to start a session in a directory outside every entry, so a fleet value such as `~/Documents/Claude` confines remote sessions to that path under the SSH user's home. A folder with `mode` set to `ro` is allowed on the host but not read-only there.
* `coworkEgressAllowedHosts`, as Claude Code managed settings. The network and filesystem sandbox it produces with `allowedWorkspaceFolders` depends on the host having Claude Code's sandbox dependencies installed (see [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)); without them, commands run unsandboxed and Claude Code shows a warning in the session.
* `managedMcpServers`, as the Claude Code managed setting that keeps users from adding their own MCP servers. The managed servers themselves are reached from the device.
* Plugins from your [allowed marketplaces](/docs/third-party/claude-desktop/extensions), copied to the host. A plugin's `hooks` directory is not copied, so its hooks do not run in a remote session, and a plugin whose manifest declares hooks elsewhere is not copied at all.

If the host has its own Claude Code managed settings, those take precedence over the policy Claude Desktop supplies, as described under [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) for local sessions.

## Host requirements

The host needs the following.

* Linux or macOS on x86\_64 or arm64, or Windows on x64 or arm64.
* An SSH server with the SFTP subsystem. On Windows, Microsoft's OpenSSH Server; with other SSH servers, the engine does not survive a dropped connection.
* A POSIX shell, or PowerShell on Windows.
* `git` on the path, for git features.
* Up to about 700 MB of disk space in the SSH user's home directory, for the three Claude Code versions the app keeps.

The Claude Code engine is a standalone executable with no runtime dependencies. The device needs the OpenSSH client (`ssh` and `ssh-keygen`).

Claude Desktop writes the following into the SSH user's home directory on the host. Each user who connects gets their own copy.

| Path on the host                     | Contents                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `~/.claude/remote/srv/<version>/`    | The remote server that Claude Desktop talks to                                                                      |
| `~/.claude/remote/ccd-cli/<version>` | The Claude Code engine, one file per version (the three most recent versions are kept)                              |
| `~/.claude/remote/run/<id>/`         | The server's socket, token, and log                                                                                 |
| `~/.claude/remote/plugins/<hash>/`   | Plugins synced from the device                                                                                      |
| `~/.claude/uploads/<session-id>/`    | Files the user attached to a message. Not removed when the session ends                                             |
| `~/.claude/` and `~/.claude.json`    | Claude Code's own data, including session transcripts. See [Data storage](/docs/third-party/claude-desktop/data-storage) |

Each side of a remote session needs its own network access.

* The device must reach `downloads.claude.ai`, including devices installed with the [offline installer](/docs/third-party/claude-desktop/installation#offline-installation). Claude Desktop downloads the remote server there and uploads it to the host over SFTP.
* The host must reach your inference endpoint and, if configured, your OTLP collector, plus whatever the user's own work needs. It downloads the Claude Code engine from `downloads.claude.ai` when it can; when that fails, Claude Desktop downloads the engine on the device and uploads it over SFTP. Unless you disabled telemetry, the engine on the host also reports to the same Anthropic hosts as a local Code session (see [Telemetry and egress](/docs/third-party/claude-desktop/telemetry)). Blocking them does not affect the session.

### SSH configuration on the device

Claude Desktop applies the host's entry in the user's `~/.ssh/config`: hostname, port, user, identity file, SSH agent, and `ProxyCommand`.

* For hosts behind a bastion, configure a `ProxyCommand`. `ProxyJump` is not supported.
* The host's key must already be in the device's `~/.ssh/known_hosts` as a plain entry; the app does not prompt to accept a new key and does not evaluate `@cert-authority` entries. Have users connect once from a terminal before adding the host in the app.
* An identity file protected by a passphrase is skipped, not prompted for. Load it into the SSH agent, or use an unencrypted key.
* For a host reached through a `ProxyCommand`, the app skips host key verification and relies on the command to authenticate the host.
* The connection times out after 30 seconds. A larger `ConnectTimeout` in the host entry extends it.

## Troubleshoot

### SSH isn't allowed by your organization

The `sshHostAllowlist` in effect on this device is unset, empty, or has no entry that matches the host; the card's details say which. Both the host as the user entered it and the `HostName` from the device's `~/.ssh/config` must match. Which configuration source supplies the key on a device follows [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). The connection test reports the same denial as "Your organization's settings do not allow this connection."

### SSH to this machine isn't available

The host resolves to the device itself (`localhost`, `127.0.0.1`, or a tunnel or port forward that ends on the device) while `allowedWorkspaceFolders` restricts workspace folders. A session over SSH to the device reaches the same disk the policy restricts, so it is refused. Connect to a different host, or use a local session.

### Remote sessions aren't available with this inference setup

The configured inference credential is one of the kinds listed as refused under [Inference credentials on the remote host](#inference-credentials-on-the-remote-host), or the inference endpoint is on the device itself. The card's details say which. Switch the deployment to a credential kind that works on a remote host, or point the app at an endpoint the host can reach.

### SSH host key verification failed

The host's key is not in the device's `~/.ssh/known_hosts`, or it has changed. Connect to the host from a terminal on the device to record the current key, then retry.

## Related

* [Code in Claude Desktop on 3P](/docs/third-party/claude-desktop/code)
* [`sshHostAllowlist` in the configuration reference](/docs/third-party/claude-desktop/configuration#sshhostallowlist)
* [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access)
