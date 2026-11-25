> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH remote sessions in Claude Desktop on 3P

> How Code sessions run on a remote host over SSH in Claude Desktop on 3P, the sshHostAllowlist key that enables them, which inference credentials work on a remote host, and what to check before turning them on

An SSH remote session is a [Code](https://claude.com/docs/third-party/claude-desktop/code.md) session whose Claude Code engine runs on another machine that the user reaches over SSH, while the session's interface stays in Claude Desktop on the user's device. Claude Desktop connects to the host, places the engine there, and starts the session with the policy from your managed configuration and, for most credential kinds, its inference credential. Users can work on code that lives on a development server, a build box, or a cloud workstation without copying it to their device. In Claude Desktop on third-party (3P), SSH remote sessions are off until you set the [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist) key, because enabling them sends your inference credential to the hosts users connect to, unless the credential is one that stays on the device (see [Inference credentials on the remote host](#inference-credentials-on-the-remote-host)).

> [!NOTE]
>
> SSH remote sessions are in beta in Claude Desktop on 3P and require Claude Desktop 1.40609.0 or later. The in-app configuration window marks `sshHostAllowlist` with a **Beta** pill.

## How a remote session works

1. **Connect.** The user picks an SSH host from the environment picker in Code, or adds one by entering its address, port, and an identity file. Claude Desktop connects through the device's OpenSSH client, or in some cases through its built-in SSH client (see [Host requirements](#host-requirements)), applies the host's entry from the device's `~/.ssh/config` (see [SSH configuration on the device](#ssh-configuration-on-the-device)), and prompts in the app if the host asks for a password or a one-time code.
2. **Deploy.** Claude Desktop places a remote server and the Claude Code engine under `~/.claude/remote/` in the SSH user's home directory on the host ([Host requirements](#host-requirements) lists every path) and reuses them on later connections.
3. **Run.** The remote server starts the engine on the host with the policy from your managed configuration and the inference credential that Claude Desktop passes, if it passes one. Every file read, edit, shell command, and git operation runs on the host, in the working directory the user chose there. Claude Desktop connects to [managed MCP servers](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin) from the device and exposes them to the engine as tools.
4. **Stream.** Claude's responses and tool output stream back to Claude Desktop. Permission prompts appear in Claude Desktop, and the engine waits on the host until the user answers.

The engine keeps running on the host through a dropped SSH link, device sleep, or the user quitting Claude Desktop. It finishes the current turn, or stops at a permission prompt, then idles. While Claude Desktop is disconnected or closed, an idle engine can still start a turn by itself, for example when scheduled work comes due (a `/loop` task, say) or when a background command ends. An engine that starts while [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled) is `false` starts without Claude Code's scheduling tools, so `/loop` can't schedule work there. An engine that already runs keeps those tools until Claude Desktop replaces it. Whatever else can start a turn still can, a background command's end included. While Claude Desktop is disconnected or closed, a credential that it passed is not refreshed, so a turn that outlives that credential, or starts after it expires, can fail with an authentication error. A restart of the app for an update counts as a quit.

When the user reopens the session after a quit, Claude Desktop rejoins the engine or replaces it, unless it refuses to start the session:

* **Rejoins**: on a macOS or Linux device, Claude Desktop 2.42304.0 or later tries to rejoin an engine that 2.42304.0 or later started. On a Windows device, Claude Desktop 3.1623.0 or later tries to rejoin an engine that 3.1623.0 or later started. If it rejoins, a turn still running goes on. It can fail to rejoin, for example after some Claude Desktop updates or after a change to the managed configuration since the engine started.
* **Replaces**: if Claude Desktop doesn't rejoin the engine, for example because a version older than the minimums above started it, Claude Desktop ends the engine and starts a fresh one from the transcript stored on the host. A turn that finished while the app was closed is shown in full, and a turn that still runs is cut short. If the turn stays stopped, the user sends a message to continue it.

On a host that ends a user's processes at logout, the remote server and the engine end with the SSH connection that started them, so a turn in progress doesn't survive a disconnect. Linux hosts where systemd-logind's `KillUserProcesses` setting is `yes` and applies to the SSH user behave this way. To keep remote sessions running through a disconnect on such a host, ask the host's administrator to exempt the SSH user, for example by listing the user under `KillExcludeUsers` in the systemd-logind configuration.

An idle engine stays on the host, and keeps any credential that Claude Desktop passed, until one of these happens:

* The user archives or deletes the session while Claude Desktop is connected to the host.
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

On a Linux or macOS host, the remote server and the engine run as the SSH user. Installing and starting them needs no `sudo`. The shell commands and [MCP servers](#where-mcp-servers-run-in-a-remote-session) that the engine starts there also start as the SSH user. Review the SSH user's rights on the host, `sudo` rules included, as you would for a person who runs commands there.

### Alert the user with hooks on the host

A [hook](https://code.claude.com/docs/en/hooks) is a command that you choose, which the engine runs on the host at a set point in a session. With hooks, the host can tell the user that a turn is waiting at a permission prompt, has finished, or has failed with an API error, including while Claude Desktop is disconnected. To set them up, add this `hooks` key to `~/.claude/settings.json` in the SSH user's home directory on the host before the user starts the session.

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

Claude Desktop starts a managed local (stdio) server on the device, so its tools read and write the device's files, while the session's own file edits and commands run on the host. If a local server that only Code sessions use has to work on the session's files, deliver it in a plugin from one of your [plugin marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin) instead of in `managedMcpServers`. Claude Desktop copies the plugin to the host, which needs [SFTP](#hosts-without-sftp), and the engine starts the server there. In a local Code session, the engine starts it on the device, so its command has to work on both the device and the host.

Before you move a server, check the following:

* **Your MCP keys**: this works only with `isLocalDevMcpEnabled` at `true` and `allowedPluginMcpServers` unset. Otherwise, the session refuses a plugin's local servers.
* **The last managed server**: if you remove your last server from `managedMcpServers`, Code sessions again load the MCP servers that users define in Claude Code's own configuration.
* **Tool policy**: `toolPolicy` doesn't move with the server. To keep it, see [Plugin structure](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-structure).
* **Users**: with `installationPreference` set to `"required"`, users can't turn off the plugin in the app, but they can in their own Claude Code settings.
* **Secrets**: a secret in the plugin's `.mcp.json` file reaches every device that installs the plugin and every host where a user starts a remote session. A secret in the plugin's `hooks` directory can reach the same devices and hosts (see [Plugin hooks on the remote host](#plugin-hooks-on-the-remote-host)).
* **The host's policy**: a [`managed-mcp.json`](https://code.claude.com/docs/en/managed-mcp) file on the host, or `disableSideloadFlags`, `allowedMcpServers`, or `deniedMcpServers` in its Claude Code managed settings, or a setup in which your organization starts Claude Code on the host itself, can keep the server out.

A copy of the server in Claude Code's own configuration on the host is no substitute. The engine never loads a server there that has a managed server's name, and the session shows no message about it.

With the device's OpenSSH client, the user's first message can wait up to ten seconds, with the line `Setting up your MCP servers on <host>…` under it. This can happen after a session starts, and after a quit, once Claude Desktop rejoins the running engine. Claude Desktop is handing the engine the local servers that the user added under **Settings > Developer**. If the engine doesn't get them in time, the message is sent anyway, and the conversation shows `This message went without your MCP servers. If you need them, send it again once they're connected.` If the task needs those servers, have the user wait until Claude finishes responding, then send the message again. Requires Claude Desktop 4.4212.0 or later.

[`isLocalDevMcpEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled), `managedMcpServers`, `allowedPluginMcpServers`, and `deniedPluginMcpServers` decide which of these servers a remote session loads, as they do for a local Code session (see [Applied as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy)). If the host has its own Claude Code managed settings, those take precedence over the Claude Code policy these keys produce (see [Managed configuration on the remote host](#managed-configuration-on-the-remote-host)).

### Resume a session that is saved on the host

On Amazon Bedrock, a user can continue in Claude Desktop a Claude Code session that is saved on a Linux or macOS host, such as one that they began in a terminal there. Requires Claude Desktop 6.28899.6 or later. The user takes these steps:

1. In **Code**, the user starts a new session on the SSH host and picks the folder that the earlier session ran in.
2. Before sending anything, the user types `/resume` in the message box, and selects **Trust workspace** if Claude Desktop asks about the folder. Claude Desktop lists the newest sessions that are saved for that folder, by title and time.
3. The user selects a session. It opens with its earlier messages, and doesn't start yet.
4. The user sends a message. The engine then starts on the host and resumes the session. It starts with the model and effort level that were selected in the new session when the user typed `/resume`, and the user can change both before sending. It doesn't go back to the model that the session used before. Before Claude Desktop 7.37095.0, it starts with the first model in your model list, even where the session shows another, unless, before sending, the user picks a model other than the one shown.

If users don't find `/resume`, or it fails, see [Resume is missing or fails on an SSH host](#resume-is-missing-or-fails-on-an-ssh-host).

#### Where resuming a saved session is available

A saved session can be resumed on a Linux or macOS host where the device, the host, and the saved session all use Amazon Bedrock. Check these conditions:

* **The device sends requests straight to Amazon Bedrock.** [`inferenceProvider`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceprovider) is `bedrock` or `mantle`, and [`inferenceBedrockBaseUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencebedrockbaseurl) is unset or names Amazon's own Bedrock endpoint. A VPC endpoint for `bedrock-runtime`, `bedrock-runtime-fips`, or `bedrock-mantle` counts. Before Claude Desktop 7.37095.0, a VPC endpoint counts only if it is for `bedrock-runtime`. Identity provider sign-in needs a proxy address in that key, so it doesn't qualify. With an address that doesn't count, such as a proxy or gateway, `/resume` is missing from the slash menu, and no message says why. The other conditions don't hide the command.
* **The engine has a credential on the host.** The credential kind [works on a remote host](#inference-credentials-on-the-remote-host), or the host starts Claude Code through a launcher. The launcher then supplies the credential, and must be one that the host's managed settings name (see [Resume through a corporate launcher](#resume-through-a-corporate-launcher)).
* **The host's Claude Code managed settings hold the session to Amazon Bedrock.** A host without managed settings needs nothing. If a host has managed settings, they must contain an [`allowedProviders`](https://code.claude.com/docs/en/settings-reference#allowedproviders) list with only `bedrock` and `mantle`, or contain no such list and set `"parentSettingsBehavior": "merge"`. Otherwise the user sees `Sessions on this host can't be listed.`
* **All of the session ran on Amazon Bedrock.** Claude Desktop leaves out a session that holds a reply from another provider, and one that was ever opened under a Claude sign-in.

These keys refuse both the list and the selection:

* **[`isClaudeCodeForDesktopEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#isclaudecodefordesktopenabled)** set to `false`, which hides Code
* **[`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist)**, for a host that it doesn't allow
* **[`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders)**, for a folder whose real location on the host is outside the list, and for every folder if the list is empty

#### Resume through a corporate launcher

`/resume` works with a [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) that the host's Claude Code managed settings name, where [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudecodeprocesswrapperenabled) is `true` on the device. It isn't available on a host whose launcher isn't named there and locates Claude Code itself. Check the launcher against these points:

* **The provider check**: Claude Desktop calls the launcher with `auth status --json` before it lists sessions, when the user selects one, and at the first message, to learn which provider Claude Code on the host uses. The launcher must pass its arguments on, and print no `{` or `}` of its own to standard output. If that call takes longer than 33 seconds or fails at the list, the user sees `Couldn't load sessions from the host.` Before Claude Desktop 7.37095.0, the limit is 15 seconds.
* **Options and variables**: have the launcher pass on every option and every environment variable that it receives, apart from the credential that it sets. Some of them hold the session to Amazon Bedrock, and keep the engine from using a system prompt or tool definitions that the session file records. Claude Desktop can't always tell if a launcher drops them.
* **The Amazon Bedrock address**: a resumed session doesn't start if the launcher points Amazon Bedrock requests at a proxy or gateway address, for example in `ANTHROPIC_BEDROCK_BASE_URL`. A new session through the same launcher starts. For the message, see [Resume is missing or fails on an SSH host](#resume-is-missing-or-fails-on-an-ssh-host).
* **An expired credential**: if the credential that the launcher supplies has expired, for example because a company sign-in on the host has lapsed, the list and the selection can still work. The first message then fails with the card `Claude Code on <host> has no working credentials`. After signing in again on the host, the user selects **Try again**.

#### What Claude Desktop copies from the host

Resuming a session brings its conversation from the host to the user's device:

* **At the list**: Claude Desktop first runs `claude auth status` on the host, which opens no session. It then skips the sessions that it already has for this host, and checks up to 60 of the folder's other session files, from the newest, or fewer on a slow host. From each session file that passes its Amazon Bedrock check, Claude Desktop fetches the first and the last 64 KiB. For the folder's other session files, only the name, the project folder's name, the size, and the time reach the device. Those details reach the device for up to the folder's 200 newest session files (more where the folder's path on the host is over 200 characters long) and up to 20 for each of the folder's worktrees. Before Claude Desktop 7.37095.0, Claude Desktop checks the folder's 30 newest, and the sessions that it already has count among them.
* **At the selection**: it copies the whole conversation to the user's device, before the user sends anything, with the conversation's subagent files and every `agent-*.jsonl` file in the same project folder, which it doesn't check. The copy goes to Claude Code's store on the device, as for every SSH session (see [Removing data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#removing-data)).
* **Afterward**: the copy follows the host's file. What someone later adds to that conversation in a terminal reaches the device too, unchecked.
* **On the device**: other Claude Code sessions there can read the copy, in Claude Desktop or in a terminal, under whatever provider or sign-in they use. The conversation can leave Amazon Bedrock that way.
* **From the first message**: the engine sends the earlier conversation to Amazon Bedrock, tool results included.

The copying stops when the user deletes the session in Claude Desktop. That removes the copy from the device and leaves the host's file, with the turns that Claude Desktop added. Automatic deletion with [`codeSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#codesessionretentiondays) leaves the session and the copy in place (see [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions)).

`allowedWorkspaceFolders` applies to the folder that the user picks. A terminal session isn't bound by the list, so file contents from elsewhere on the host can be in a conversation that reaches the device.

#### Security limits of a resumed session

`/resume` has no configuration key of its own. Users get it with the update, [where the conditions hold](#where-resuming-a-saved-session-is-available), on the hosts and folders that `sshHostAllowlist` and `allowedWorkspaceFolders` allow. Review these limits:

* **The Amazon Bedrock check reads the session file.** The check's result can be trusted only as far as that file can be trusted. The check can't tell one AWS account or region from another, so a session from an account with its own retention rules can continue in another account.
* **Several people on one SSH user see each other's sessions.** If a user selects a colleague's session, Claude Desktop copies it to that user's device and then writes in the colleague's file. Give each person an SSH user of their own.
* **The engine treats a resumed conversation as its own earlier turns.** The engine also acts on what the file records, without asking the user, as `claude --resume` does. For example, it sets up the session's scheduled prompts again, so they run when they are due. Claude Desktop doesn't vouch for what a session file holds, and a user can select, by its title alone, a conversation that they have never seen.
* **Claude Desktop checks a session file's owner and mode, and nothing finer, and only where the host can tell who owns a file.** Where the host can tell, Claude Desktop refuses a session file that another user owns, or that the file's group or everyone can write, at the selection and again at the first message. Keep `~/.claude` on the host writable by the SSH user alone.
* **The first message can run in Auto mode on a conversation that the user hasn't read**, and Auto mode is no guard against what the file holds. A resumed session starts in the mode that the new session would have started in. A saved choice or a setting can decide that mode. Where that mode would be Bypass permissions, the resumed session starts in Accept edits. It doesn't start in the mode that the session had in the terminal. The user can change the mode afterward.
* **Use the session in one place at a time.** The session continues in its own file on the host, as with `claude --resume`. Have users end it where it ran, with `/exit` in a terminal, before they continue it. If it stays open in two places, messages can drop out of the conversation. Claude Desktop warns with `This session may be open somewhere else` when it sees another process on the host, but it doesn't always see one.
* **Keep the host's conditions in place after a session is resumed.** Claude Desktop checks which provider the host uses up to the first message, and again only if the host's address is edited. Keep [what holds the session to Amazon Bedrock](#where-resuming-a-saved-session-is-available) in any managed settings that the host has or gets, and keep the launcher passing on every option and variable. Without them, a resumed conversation is no longer held to Amazon Bedrock, and no message says so.
* **An earlier release starts a resumed session without these checks.** Don't move a device back to one once its user has resumed a session this way.

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

A session's [jump hosts](#jump-hosts-and-the-allowlist) must match an entry too. The allowlist limits which hosts Claude Desktop connects to. It doesn't limit what the device can reach over SSH from a terminal. To limit that, or wherever you need a hard boundary, use network controls.

For example, this key in [Claude Desktop's Linux configuration file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file), alongside your other settings, turns the feature on for one domain:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "sshHostAllowlist": ["*.dev.example.com"]
}
```

In a `.mobileconfig` or registry policy, write the array as a JSON string as described under [Value types](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types). In a [bootstrap](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) response, the key sits inside the `codeSurface` object.

When a device applies an allowlist that no longer allows a host, Claude Desktop refuses new sessions on that host and new connections to it. It doesn't stop a session that is already running there. After that session's connection drops, Claude Desktop doesn't reconnect, and the engine on the host goes on as it does through any dropped connection (see [How a remote session works](#how-a-remote-session-works)). To end the session, stop its processes on the host.

To replace an entry in an allowlist that a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#availability) or the [admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-updates) delivers, add the new entry first, and remove the old entry after Claude Desktop has restarted on users' devices.

### Jump hosts and the allowlist

Add each jump host, or bastion, that Claude Desktop checks to `sshHostAllowlist`, by the `HostName` that the device's `~/.ssh/config` gives for it. Add the jump hosts before devices update to Claude Desktop 3.1623.0 or later, or users can't connect through them. To hold updates until devices have the new allowlist, see [Auto-updates](https://claude.com/docs/third-party/claude-desktop/telemetry.md#auto-updates).

> [!WARNING]
>
> The allowlist has one kind of entry, so users can also start a session on any host that you list, and that session receives your [inference credential](#inference-credentials-on-the-remote-host), where Claude Desktop passes one. List only jump hosts that you'd also let users run sessions on.

Claude Desktop checks jump hosts in the `ProxyJump` that the device's `~/.ssh/config` sets for the session's host, or in a `ProxyCommand` written as `ssh -W %h:%p <host>`. If a jump host that Claude Desktop checks isn't on the allowlist when the app connects or reconnects a session, the connection fails. When the user starts a session or sends a message, they see [Your organization doesn't allow this SSH connection](#your-organization-doesn%E2%80%99t-allow-this-ssh-connection), and the card's details give that jump host's `HostName`.

Find the names to add in a terminal on a user's device. Skip `proxyjump` lines only on devices where the built-in client makes every connection, for example with `sshTransport` set to `builtin`. The built-in client [refuses every `ProxyJump`](#ssh-configuration-on-the-device), listed or not.

1. Run `ssh -G` with a host that users connect to, for example `ssh -G build01`. Look for a `proxyjump` line, or a `proxycommand` line written as `ssh -W %h:%p <host>`. The command still counts with any of `-l`, `-p`, `-J`, `-q`, `-v`, `-N`, `-T`, `-x`, or `-a`, and the hosts after `-J` are jump hosts too. If a `proxycommand` line runs a program other than `ssh`, add nothing for it.
2. Run `ssh -G` with each jump host on that line, without any `:port`, and note the `hostname` that it prints. If the output for the first jump host on that line has a line of either kind, repeat this step with the jump hosts on the new line. Ignore a line of either kind in the output for a later jump host.
3. Add each hostname, or a wildcard that covers it, to the `sshHostAllowlist` that applies on the device. To tell which one applies, see [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). Then have users quit and reopen Claude Desktop, because when a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#availability) or the [admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-updates) delivers the list, an open app allows the hosts that you added only after the app restarts.

### Interaction with Claude Code managed settings on the device

Claude Code has its own `sshHostAllowlist` setting, which you can deploy on the device through a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy. The app resolves the two sources in this order:

1. `sshHostAllowlist` from the Claude Desktop configuration, when that configuration is delivered by an administrator: through machine-scoped device management (`HKLM` policy on Windows, a configuration profile on macOS, `/etc/claude-desktop` on Linux), through the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), or by a bootstrap server the app trusts (a `bootstrapUrl` set through device management or covered by `trustBootstrapDelivery`; see [Keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent)). User-scope registry policy (`HKCU`) counts as applied locally.
2. `sshHostAllowlist` from Claude Code's managed settings on the device.
3. `sshHostAllowlist` from a Claude Desktop configuration the user applied locally in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#apply-locally-or-export-for-a-fleet).
4. Off.

On devices where users applied the configuration locally, deploy `sshHostAllowlist` in Claude Code's managed settings. That list takes priority over a list in the configuration that users applied, without an MDM profile taking ownership of the whole configuration (see [Update keys and managed precedence](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence)).

Until a Claude Desktop managed profile governs the device's configuration, the user chooses which configuration the app uses. A list from another organization's admin console, or from a bootstrap server that your organization doesn't run, can then take priority over the list in Claude Code's managed settings. To control which configuration the app uses, deploy a machine-scoped Claude Desktop profile that does one of the following:

* **Provides your organization's third-party configuration**: put your inference provider keys or bootstrap keys in the profile. In the same profile, set [`forceLoginOrgUUID`](https://claude.com/docs/cowork/hipaa-setup#what-each-claude-desktop-key-does) to your Claude organization's ID, so that users can't [move the device to another organization's admin console configuration](#devices-that-move-to-an-admin-console-organization) by signing in.
* **Limits sign-in to your admin console organization**: in the profile, set `forceLoginOrgUUID` to your Claude organization's ID. Configure your inference provider in the admin console.
* **Keeps the device on standard Claude Desktop**: in the profile, set [`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentmode) to `1p`. Users then sign in to claude.ai instead of using your inference provider.

With any of these profiles, the app stops reading the configuration that users applied, including its inference provider and its other settings. Before you deploy one, read [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

To turn off Code sessions that run on the device, so that users work in SSH remote sessions, set [`disableDesktopLocalSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledesktoplocalsessions) to `true` in the Claude Desktop configuration that you deliver to devices, alongside your other settings. Claude Desktop then refuses to start or resume a Code session that runs on the device. Where a bootstrap server or the Enterprise Admin Console delivers the configuration, set the key in the server's response or in the console. That configuration replaces the value from device management, even where it leaves the key out.

On devices where users applied the configuration locally, set [the key of the same name](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions) in a [Claude Code managed-settings file](https://code.claude.com/docs/en/settings#settings-files) or OS policy on the device instead.

* If the device already has Claude Code managed settings, add the key to those and leave `parentSettingsBehavior` as it is, set or unset. Changing it changes how those settings combine with the policy that Claude Desktop supplies.
* If the device has none yet, also set `parentSettingsBehavior` to `"merge"` in the managed settings that you create. Without `"merge"`, the new managed settings replace the policy that Claude Desktop supplies to Claude Code on the device (see [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) on the Code page). Once the device has these managed settings, an unset [`remoteFileDownloads`](#file-downloads-from-the-remote-host) means `limited` on that device.

If you set the key in both Claude Desktop's configuration and Claude Code's managed settings, `true` in either one turns local Code sessions off.

Before you deploy `disableDesktopLocalSessions`, make sure that the `sshHostAllowlist` that applies on the device, by [the order of its sources](#interaction-with-claude-code-managed-settings-on-the-device), allows the hosts that users need. While SSH remote sessions are off, a device that has `disableDesktopLocalSessions` set can start neither a local Code session nor an SSH remote session.

To keep HTML previews in SSH remote sessions from running the scripts in the previewed file, set [`disableRemotePreviewScripts`](https://code.claude.com/docs/en/desktop#turn-off-scripts-in-ssh-and-wsl-previews-for-your-organization) to `true` in Claude Code's managed settings on the device, by the same steps as for `disableDesktopLocalSessions` in those settings.

### Pre-configure SSH connections for users

To put named SSH connections in each user's environment picker, set [`sshConfigs`](https://claude.com/docs/third-party/claude-desktop/configuration#sshconfigs) in the Claude Desktop configuration that you deliver to devices, alongside your other settings. For example, these keys in [Claude Desktop's Linux configuration file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file) allow one domain and add one connection:

```json /etc/claude-desktop/managed-settings.json theme={null}
{
  "sshHostAllowlist": ["*.dev.example.com"],
  "sshConfigs": [
    {
      "id": "build01",
      "name": "Build server",
      "sshHost": "build01.dev.example.com"
    }
  ]
}
```

**Build server** appears under **SSH** in the environment picker after the user quits and reopens Claude Desktop. In a `.mobileconfig` or registry policy, write the `sshConfigs` array as a JSON string, as described under [Value types](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types). Where a bootstrap server delivers your configuration, put the key in its response, inside the `codeSurface` object. In that response, `sshConfigs` is one of the [keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent).

* **Allowed hosts**: `sshConfigs` doesn't turn SSH remote sessions on. A managed connection whose resolved hostname matches no `sshHostAllowlist` entry still appears, and Claude Desktop refuses to connect to it (see [Your organization doesn't allow this SSH connection](#your-organization-doesn%E2%80%99t-allow-this-ssh-connection)).
* **Invalid entries**: Claude Desktop ignores an entry with a missing or invalid field, such as `sshPort` in quotes, and keeps the other entries.
* **What users can change**: in the app, users can't edit or delete a managed connection. They can add connections of their own, and a connection with the same `id` in the user's own Claude Code settings replaces the managed one. `sshHostAllowlist` applies to those connections too.

With local Code sessions turned off, Claude Desktop selects a connection for each user who has none selected: the first that the user added in the app, or else the first `sshConfigs` entry. Make the first `sshConfigs` entry a host that `sshHostAllowlist` allows and that all of these users can use.

On devices where users applied the configuration locally, set [`sshConfigs`](https://code.claude.com/docs/en/settings-reference#sshconfigs) in Claude Code's managed settings on the device instead, in a [managed-settings file or OS policy](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy). If Claude Desktop's own configuration profile, registry policy, or Linux file held the key, it would govern the whole Claude Desktop configuration, and the app would stop reading the configuration that users applied (see [Update keys and managed precedence](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence)). For how to add the key, and when to set `parentSettingsBehavior`, see the steps for `disableDesktopLocalSessions` under [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). If you create a managed-settings file on Windows, users also lose WSL sessions until you allow them, as described under [WSL sessions in Claude Code Desktop](https://code.claude.com/docs/en/admin-setup#wsl-sessions-in-claude-code-desktop). The registry value that allows them, [`disableWslSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disablewslsessions), is one of the [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence).

* **Connections from both sources**: the environment picker shows the connections from both. Where both use the same `id`, it shows the one from your Claude Desktop configuration. When Claude Desktop selects the first `sshConfigs` entry for a user, it goes through Claude Code's entries before those in your Claude Desktop configuration.
* **An invalid entry in Claude Code's managed settings**: Claude Code drops the whole `sshConfigs` key from that file or policy, so every connection it lists disappears from the environment picker. The app shows no message, and the other keys in the managed settings still apply. If one of them is `disableDesktopLocalSessions`, local Code sessions stay off, and a user with no other connection has no environment to select until they add one.

### Devices that move to an admin console organization

A device that gets its SSH keys from a managed profile, a registry policy, or the profile's bootstrap server moves to the configuration from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) when its user signs in to an organization that uses the console and chooses that organization in the dialog that follows. The app then restarts. A device that used such an organization before its profile arrived, and whose user hasn't signed out of the app since, moves back at its first launch on Claude Desktop 2.37337.0 or later, with no new sign-in and without asking the user, even if the stored sign-in has expired. To prevent that, add `disableDeploymentModeChooser` to the profile before devices update. `forceLoginOrgUUID` prevents it only for organizations it leaves out. Before Claude Desktop 2.37337.0, a device with such a profile ignores the admin console.

After the move, `sshHostAllowlist`, `sshConfigs`, `disableDesktopLocalSessions`, `sshTransport`, `sshClientPath`, and `sshHostSandboxUnavailable` from the profile, or from the profile's bootstrap server, don't apply, even where the console leaves them unset. For the profile's other settings, see [Which settings apply on a device with a managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#which-settings-apply-on-a-device-with-a-managed-profile).

* **Which hosts**: the console's `sshHostAllowlist` applies. If the console leaves the key unset (**Not set**), or the app hasn't yet downloaded the console's configuration at this launch (the copy a device keeps of the last download holds no lists), `sshHostAllowlist` from Claude Code's managed settings on the device applies. With neither, SSH remote sessions are off.
* **Which SSH client**: the console's `sshTransport` and `sshClientPath` apply. On a Windows device, a client that the console's `sshClientPath` names makes the connection only if it is Microsoft's OpenSSH. With `system-openssh`, SSH connections fail under any other client. A key that the console leaves unset takes its default under [Host requirements](#host-requirements). Until the app has downloaded the console's configuration at a launch, both keys count as unset, so no client is pinned. Until then the built-in client makes the connection on a Windows device, even where the console sets `system-openssh`. The device's OpenSSH client makes it on a macOS or Linux device, even where the console sets `builtin`.
* **Connections and local sessions**: the console's `sshConfigs` and `disableDesktopLocalSessions` apply, together with those in Claude Code's managed settings on the device. Until the app has downloaded the console's configuration at a launch, the console's connections are missing, and local Code sessions stay off if the last download turned them off.

To prevent or limit the move, set one of these keys in the profile itself:

* **Keep the device on its profile**: set [`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentmode) to `3p`. The app ignores the admin console, and the sign-in screen doesn't offer **Or sign in with Claude.ai**. A device that has already moved returns to its profile at its next launch. For devices on versions that don't read `deploymentMode`, also set `disableDeploymentModeChooser` to `true`, as described under [Restrict a device to one deployment mode](https://claude.com/docs/third-party/claude-desktop/mdm.md#restrict-a-device-to-one-deployment-mode).
* **Allow only your organization**: set [`forceLoginOrgUUID`](https://claude.com/docs/cowork/hipaa-setup#what-each-claude-desktop-key-does) to your organization ID, and set the SSH keys you rely on in the console too. The key also limits standard Claude Desktop sign-in on the device to your organization. If users click **Sign in with Claude Console**, also add the ID of each Claude Console organization that you allow, as described under [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

Before you add one of these keys to a profile that sets only [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), such as `disableAutoUpdates`, read the warning under [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

### File downloads from the remote host

Users can download files from a remote session's folders to their device. For example, they right-click a file in the **Files** pane and select **Download file**. The [`remoteFileDownloads`](https://claude.com/docs/third-party/claude-desktop/configuration#remotefiledownloads) key sets which files they can download from an SSH host and from a Code session in Windows Subsystem for Linux (WSL).

The key requires Claude Desktop 5.1231.0 or later. Earlier versions don't read the value and offer at most what `limited` allows. Before you put the key in a profile or policy that an earlier version reads, see [Deploy remoteFileDownloads through device management](#deploy-remotefiledownloads-through-device-management).

Each value lets users download these files.

| Value | Files that users can download |
| - | - |
| `limited` | `.pdf`, `.docx`, `.xlsx`, and `.pptx` files up to 25 MiB, images up to 10 MiB, and text files up to 1 MiB |
| `all` | Files of any size, of any type that Claude Desktop doesn't refuse |
| `none` | No files. Claude Desktop hides its **Download file** options. |

With the key unset, Claude Desktop applies `limited` on a device where it finds one of these signs of an administrator, or can't check for them:

* **A profile or policy for Claude Desktop**: a profile or policy in a [managed location](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#where-claude-desktop-reads-configuration-on-a-device) on the device, whichever keys it holds. A per-user profile or policy counts too.
* **A bootstrap server or the Enterprise Admin Console**: the device gets its configuration from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) or the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)
* **Claude Code's managed settings on the device**: a file, profile, or policy on the device in one of [Claude Code's policy locations](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy). [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings) don't count, and neither do managed settings on the SSH host or in the WSL distribution.

An empty `SOFTWARE\Policies\Claude` or `SOFTWARE\Policies\ClaudeCode` registry key counts too, in `HKLM` or `HKCU`. The directory for Claude Code's `managed-settings.json` file counts too, even when the directory is empty.

On a device without any of these signs, an unset key means `all`. Before Claude Desktop 6.6395.0, an unset key means `limited` on such a device.

> [!WARNING]
>
> An unset key means `all` on a device that your organization manages if the device has none of these signs of an administrator. One example is a device where users applied the configuration locally in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#apply-locally-or-export-for-a-fleet). Another is a device to which a script copied the local configuration file. Enrolling a device in MDM isn't a sign by itself.
>
> To apply `limited` on such a device, set the key to `limited` in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md). The user can change the value there. To set it where users can't change it, use a machine-scoped profile or policy (see [Deploy remoteFileDownloads through device management](#deploy-remotefiledownloads-through-device-management)).

Under `limited` and `all`, Claude Desktop refuses a fixed list of file types that an operating system can run or act on when opened, such as `.exe`, `.js`, `.ps1`, and `.jar`. Claude Desktop decides by the file's extension. Scripts such as `.py` and `.sh` aren't on the list.

Where file downloads are off on a [host without SFTP](#hosts-without-sftp), `limited` and `all` both still allow text files up to 1 MiB, and nothing else.

> [!WARNING]
>
> Where Claude Desktop is the only program on a device that can reach the host, `all` gives users a way to take files off the host in bulk. Claude Desktop's logs and telemetry keep no list of the files that were downloaded. `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the device names the hosts that Claude Desktop connects to and, under `all`, records each copy's size and duration. On such devices, set the key to `limited` where users can't change it (see [Deploy remoteFileDownloads through device management](#deploy-remotefiledownloads-through-device-management)), unless users need other file types or larger files.

`none` isn't a security boundary. In Claude Desktop, users can still open the files that they can't download, and Claude can still read them. To limit which files a user can reach on the host, review the SSH user's rights there (see [Account that a remote session runs under](#account-that-a-remote-session-runs-under)).

Claude Desktop reads and applies the value by these rules:

* **Spelling**: Claude Desktop ignores letter case. It treats a value that isn't `limited`, `all`, `none`, or empty as `none`, so a mistyped `all` turns downloads off. An empty value counts as unset. On Windows, a mistyped value in a machine policy also makes Claude Desktop refuse WSL sessions, even where machine policy sets [`disableWslSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disablewslsessions) to `false`.
* **When a change takes effect**: an open app applies a new value from device management, the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), or a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) without a relaunch, once a [re-check](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#when-a-configuration-change-on-a-device-takes-effect) reads it and a second check about 30 seconds later confirms it. A value set in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) applies no later than the relaunch that **Apply Changes** asks for.
* **An unset key in an open app**: the app goes from `all` to `limited` at the next download after a profile, a policy, or Claude Code's managed settings appear on the device. After you remove every sign of an administrator from the device, the app keeps `limited` until its next launch.

You can set the key in these places:

* **Device management**: users can't edit a machine-scoped profile or policy. For when its value applies, see [Deploy remoteFileDownloads through device management](#deploy-remotefiledownloads-through-device-management).
* **Enterprise Admin Console**: the console's value applies unless the device has a profile or policy that holds this key and, apart from it, nothing but the [app-behavior keys and the keys treated like them](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence). On a Windows device with no machine policy (`HKLM`), a per-user policy (`HKCU`) counts as such a policy. Whoever can write to `HKCU` can then set `all` over the console's `none` (see **A machine policy on Windows** under [Deploy remoteFileDownloads through device management](#deploy-remotefiledownloads-through-device-management)).
* **Bootstrap response**: put the key inside the `codeSurface` object.
* **In-app configuration window**: the key appears in the **Code surface** section while Code is enabled, in Claude Desktop 5.11492.0 or later. The user can change a value that is set there.

### Deploy remoteFileDownloads through device management

Connection settings are the keys that say where Claude Desktop gets inference or its configuration, such as the inference provider keys or the bootstrap keys. Before you deploy [`remoteFileDownloads`](#file-downloads-from-the-remote-host) through [device management](https://claude.com/docs/third-party/claude-desktop/mdm.md), plan for these cases:

* **Devices on a version before 5.1231.0**: update all devices to Claude Desktop 5.1231.0 or later first. On earlier versions, on Windows and Linux, a profile or policy that holds this key can turn off other settings, connection settings included. On macOS, Claude Desktop doesn't see the key. For each platform's case, see [Keys that an earlier version does not recognize](https://claude.com/docs/third-party/claude-desktop/mdm.md#keys-that-an-earlier-version-does-not-recognize).
* **A profile or policy that holds your connection settings**: set the key in that same profile or policy, and set the same value in the bootstrap response or the console too. Connection settings are outside the [app-behavior keys and the keys treated like them](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence). Where a profile or policy holds any key outside that group, a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) or an [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) that leaves `remoteFileDownloads` out overrides the profile's value. The key then counts as unset, which means `limited` on a device with a profile or policy.
* **A profile or policy that holds this key and, apart from it, nothing but the app-behavior keys and the keys treated like them**: the user's or the console's configuration stays in place. The profile's value takes precedence over the value from the Enterprise Admin Console, a bootstrap server, or the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md).
* **A machine policy on Windows**: while machine policy (`HKLM`) holds this key, Claude Desktop applies nothing from a per-user policy (`HKCU`). Move what the per-user policy holds, connection settings included, into the machine policy.

A profile or policy, even one that holds only this key, also changes how WSL sessions and shell commands in Code sessions work on the device (see [What a profile or policy changes on a device](https://claude.com/docs/third-party/claude-desktop/mdm.md#what-a-profile-or-policy-changes-on-a-device)).

## Inference credentials on the remote host

> [!WARNING]
>
> In `sshHostAllowlist`, list only hosts that you trust. Where Claude Desktop passes a credential, a remote session runs Claude Code on the SSH host with your organization's inference credential, for as long as that process runs, including while Claude Desktop is closed. The same user account on the host, or a root user, can get the credential, so prefer one that expires (single sign-on, or a credential helper that issues short-lived tokens) over a long-lived key. With [Amazon Bedrock and a named profile](#amazon-bedrock-with-a-named-profile), the engine uses AWS credentials that are kept on the host, also while Claude Desktop is closed, and the same accounts can get those.

Unless the host's [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) starts Claude Code or the deployment uses [Amazon Bedrock with a named profile](#amazon-bedrock-with-a-named-profile), Claude Desktop passes the session's credential to the remote engine. For model requests, the engine then doesn't use these on the host: an AWS profile, SSO cache, or instance or container role; an Azure CLI sign-in or managed identity; or Google application default credentials. Commands, hooks, and local MCP servers that run on the host run as the SSH user, and may be able to use them. Claude Desktop copies no AWS, Azure, or Google credential files to the host. Which credential kinds work on a remote host depends on the provider:

| Provider | Works on a remote host | Refused at session start |
| - | - | - |
| [LLM gateway](https://claude.com/docs/third-party/claude-desktop/gateway.md) | Static API key, single sign-on, credential helper | |
| [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) | Static API key, Sign in with Claude Console, credential helper | |
| [Microsoft Foundry](https://claude.com/docs/third-party/claude-desktop/foundry.md) | API key, in-app Entra ID sign-in, credential helper | |
| [Amazon Bedrock](https://claude.com/docs/third-party/claude-desktop/bedrock.md) | Bearer token, identity provider sign-in, credential helper, [named profile](#amazon-bedrock-with-a-named-profile) on a Linux or macOS host | In-app AWS sign-in (IAM Identity Center); named profile on a Windows host, or with `inferenceBedrockAwsDir` not below the user's home directory, or with no `inferenceBedrockProfile` where the folder is `~/.aws` |
| [Amazon Bedrock Mantle](https://claude.com/docs/third-party/claude-desktop/mantle.md) | Bearer token, credential helper | |
| [Google Cloud's Agent Platform](https://claude.com/docs/third-party/claude-desktop/vertex.md) | In-app Workforce Identity sign-in, credential helper | In-app Google sign-in, service-account key or credentials file, application default credentials on the device |

When the configured credential is a refused kind, the session fails at session start unless a launcher starts Claude Code. The card is [SSH sessions can't use your model provider settings](#ssh-sessions-can%E2%80%99t-use-your-model-provider-settings). Where `claudeCodeProcessWrapperEnabled` is on and a Linux or macOS host names no launcher, the card is `Your organization's launcher isn't set up on <host>` instead.

When a credential that Claude Desktop passed expires during a turn, Claude Desktop obtains a new one on the device, by re-running a [credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper.md) or using a sign-in's refresh token, and sends it over the SSH connection.

Where the host's [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) starts Claude Code, Claude Desktop passes no inference credential and refuses no credential kind. Claude Code uses the credential that the launcher or the SSH account's own environment sets, or, on Google Cloud's Agent Platform, the account's application default credentials.

The host needs its own network route to the inference endpoint and must trust the endpoint's certificate. Claude Desktop passes the endpoint address to the remote engine but not the device's proxy settings, CA certificates, or the `AWS_*` and `GOOGLE_*` variables in the user's shell. A gateway at `localhost` on the device is refused for remote sessions, because the host cannot reach it.

### Amazon Bedrock with a named profile

Requires Claude Desktop 7.37095.0 or later, and a Linux or macOS host. Before Claude Desktop 7.37095.0, SSH sessions with a named profile are refused unless a launcher starts Claude Code.

With a [named profile](https://claude.com/docs/third-party/claude-desktop/bedrock.md#named-profile), the device's AWS credentials stay on the device. Claude Desktop sends the host the profile's name and the folder that holds the AWS files, and nothing else from the profile. The engine signs in to AWS with the profile of that name on the host, in the AWS Region that your Claude Desktop configuration sets. Your `inferenceCustomHeaders` and your collector's endpoint and headers still go to the host. Session titles, Cowork, and the connection test still use the profile on the device.

This behavior has no configuration key of its own. It applies to every Linux or macOS host that `sshHostAllowlist` allows, and sessions start if the host has the files set up as the steps in this section describe. A profile of that name that is already on a host is used as it is, so check existing hosts before you update Claude Desktop. Windows hosts aren't supported. You can keep new sessions from using the host's profile in three ways:

* **On one host**: keep the host's name off `sshHostAllowlist` and outside its wildcards, which refuses new SSH sessions and connections under that name (see [Enable SSH remote sessions](#enable-ssh-remote-sessions)).
* **On a host that names a launcher**: turn `claudeCodeProcessWrapperEnabled` on, and the launcher starts Claude Code there, as the last paragraph of this section describes.
* **For the whole deployment**: set `inferenceBedrockAwsDir` to a folder outside the user's home directory, and move the device's AWS files there. SSH sessions are then refused unless a launcher on the host starts Claude Code. This doesn't suit a single sign-on profile, which must stay in `~/.aws`.

Don't count on any of them to end an engine that already runs: stop its processes on the host, and revoke its credentials in AWS. Deliver these keys where users can't change them.

Set up each host, for each user who connects to it:

1. **Add the profile.** Create it on the host, in `~/.aws` or in the folder that `inferenceBedrockAwsDir` names: a `config` file, a `credentials` file, or both. Claude Desktop copies nothing there. Claude Code runs on the host as the user and must be able to read the files. Where security software on the host keeps it out of `~/.aws`, the engine can't sign in: agree an exception or another folder with your security team. Keep a single sign-on profile in `~/.aws`, on the host and on the device: AWS keeps its token cache in `~/.aws/sso/cache`, whichever folder holds the profile. Give the profile the name that you set in [`inferenceBedrockProfile`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencebedrockprofile). Set that key: with no name, and `~/.aws` as the folder, SSH sessions are refused unless a launcher starts Claude Code. With another folder and no name, the engine uses the profile `default`.
2. **Limit its permissions.** Give the profile access to Amazon Bedrock only. The `aws` commands that Claude runs on the host use the same profile. The files on the host decide which AWS account receives the engine's requests and which `credential_process` program runs, outside the sandbox.
3. **Keep the files separate.** Use regular files, not links, in a folder of their own directly under the home directory, such as `~/.aws`, that holds no project files. Only the user who signs in should be able to read or write the files and their folder. Claude's file-editing tools are blocked for everything under that folder. Where [Claude Code's sandbox](#sandbox-status-on-the-remote-host) runs, it also keeps sandboxed shell commands from writing to the `config` and `credentials` files. Don't rely on that in a session that can write to their folder, such as one opened in the home directory. Your policy includes the sandbox where you set `allowedWorkspaceFolders`. Without that key, the sandbox can be off (see [Applied as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy)). The block is Claude Code's own check, not a file permission: Claude can read these files, and other programs that run as the user can change them. Keep sessions from starting in the home directory itself with [`allowedWorkspaceFolders`](#managed-configuration-on-the-remote-host), and prefer credentials that expire. If the profile names a `credential_process` program, keep that program where the user can't write.
4. **Sign in, if the profile needs it.** The user signs in to AWS from a terminal on the host, which for single sign-on needs version 2 of the AWS CLI there. Claude Desktop can't sign in on the host or renew the sign-in there. When it expires, turns fail until the user signs in on the host again.

The engine signs in only through the named profile. An instance role on the host isn't enough by itself: the profile must name its own source of credentials. The host must also reach the AWS hosts that the profile signs in through (see [Inference provider](https://claude.com/docs/third-party/claude-desktop/telemetry.md#inference-provider)). On a host that reaches AWS only through a proxy, a profile that assumes a role doesn't sign in, even where a terminal on that host does.

[`inferenceBedrockAwsDir`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencebedrockawsdir) names the folder on the device and on the host alike, so the device's files must be there too. Use a folder under the user's home directory, not the home directory itself, for example `~/corp-aws`, and put each machine's files in it. With a folder anywhere else, SSH sessions are refused unless a launcher on the host starts Claude Code. Keep a single sign-on profile in `~/.aws`: `aws sso login` saves its token in `~/.aws/sso/cache` whichever folder holds the profile, and Claude Code looks for it first beside the profile's files. With the profile in another folder, the engine doesn't sign in on a host that reaches AWS only through a proxy. Each folder name in the files' path on the host, the home directory's included, can hold only letters, digits, and `. _ @ + = : ~ -`. With a space or another symbol in one, the session is refused, and the details of the card `Couldn't start Claude Code on <host>` say so.

With [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/code#start-code-sessions-through-a-corporate-launcher) on, a launcher that the host names starts Claude Code. Where the key is off or unset, or Claude Desktop finds no launcher on the host, a new session signs in with the host's profile. To keep sessions on a launcher, name it on every host that `sshHostAllowlist` allows, and set the key in the device's [managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#devices-with-a-managed-profile) so that users can't turn it off. To have sessions refused where no launcher is found, also set `inferenceBedrockAwsDir` to a folder outside the user's home directory, as under **For the whole deployment**. Claude Desktop learns whether a host names a launcher, and which, from the host itself, as the account that signed in, so it can't make sure that a host with no launcher really has none, or that the launcher is yours. Keeping Claude Code from running without your launcher stays the work of your own controls on the host.

## Managed configuration on the remote host

Most of the policy that Claude Desktop applies to a local Code session applies on the remote host too. The [Code page](https://claude.com/docs/third-party/claude-desktop/code.md#how-configuration-propagates) describes how each key reaches Claude Code.

* `disableEssentialTelemetry` and `disableNonessentialTelemetry`.
* `otlpEndpoint`, `otlpProtocol`, `otlpHeaders`, `otlpResourceAttributes`, and `otlpContentCapture`. Remote sessions appear in your collector under the same `service.name` as local Code sessions. If the collector's address is `localhost` on the device, Claude Desktop doesn't send the collector settings to the host. An `otlpHeadersHelper` runs on the device at session start, and the remote session keeps those headers for its lifetime.
* `disabledBuiltinTools`, `builtinToolPolicy`, `autoModeEnabled`, and `disableBypassPermissionsMode`.
* [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), evaluated against the host's filesystem. `~` is the SSH user's home on the host, `%VAR%` entries are ignored, and Claude Desktop refuses to start a session in a directory outside every entry, so with a fleet value such as `~/Documents/Claude`, remote sessions start only under that path in the SSH user's home. List the folders that users work in on the host rather than `~` or a folder that contains it, such as `/home`. The SSH user's home holds SSH keys and shell startup files, which Claude can read in a listed folder, and setting `mode` to `ro` on `~` doesn't keep Claude from changing them. For an entry with `mode` set to `ro`, see [Read-only folders on the remote host](#read-only-folders-on-the-remote-host).
* [`blockReadsOutsideWorkingDirectories`](https://claude.com/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories), evaluated on the host, so the working directories and the home directory it hides from shell commands are the SSH user's there. Hiding files from shell commands needs the host's sandbox dependencies (next item). On a host without those dependencies, or a Windows host, the key still confines Claude's file tools. For shell commands, the key can only ask the user to approve those that Claude Code recognizes as reading outside the working directories, or whose command lines it can't analyze. Files a user attaches to a remote session stay readable, except on a Windows host, where the session's plugin files and attachments stay outside the file tools' reach under this key.
* `coworkEgressAllowedHosts`, as Claude Code managed settings. The network and filesystem sandbox it produces with `allowedWorkspaceFolders` depends on the host having Claude Code's sandbox dependencies installed (see [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing)). Without them, commands run unsandboxed, unless you [refuse such sessions](#refuse-sessions-on-a-host-without-a-working-sandbox). See [Sandbox status on the remote host](#sandbox-status-on-the-remote-host) for the message the session shows.
* `managedMcpServers`, as the Claude Code managed setting that keeps the session from loading MCP servers that users define in Claude Code's own configuration on the host. The managed servers themselves are reached from the device (see [Where MCP servers run in a remote session](#where-mcp-servers-run-in-a-remote-session)).
* Plugins from your [allowed marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md), copied to the host. A plugin's `hooks` directory is copied too, within the limits under [Plugin hooks on the remote host](#plugin-hooks-on-the-remote-host). For a hook that has to run on every host, see [Run a hook for every user](https://claude.com/docs/third-party/claude-desktop/extensions.md#run-a-hook-for-every-user).

If the host has its own Claude Code managed settings, those take precedence over the policy Claude Desktop supplies, as described under [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) for local sessions.

### Plugin hooks on the remote host

Requires Claude Desktop 7.37095.0 or later. From a macOS or Linux device to a macOS or Linux host, Claude Desktop copies a plugin's `hooks` directory with the rest of the plugin. The plugin's [hooks](https://code.claude.com/docs/en/hooks) then run on the host in a remote session. Plugins that users add themselves are copied this way too. In this section, a plugin's hooks are those in its `hooks` directory.

This is on by default for deployments on Amazon Bedrock, Amazon Bedrock Mantle, Google Cloud's Agent Platform, Microsoft Foundry, or an [LLM gateway](https://claude.com/docs/third-party/claude-desktop/gateway.md), including a [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway) that serves Code sessions no `code` settings, for example because its policies use [`cli`](https://code.claude.com/docs/en/claude-apps-gateway-config#choose-cli-or-code). To stop it, use the settings in the table below.

Hooks run as the SSH user, outside the [sandbox](#sandbox-status-on-the-remote-host), on each host that the user connects to, and nobody is asked first. As on a device, a hook can approve Claude's tool calls, so that the user isn't asked. Deny rules in the host's managed settings still hold for Claude's calls, but not for what a hook itself does.

A plugin runs on the host without its hooks in cases such as these:

* **Mods**: the plugin has a [mod](https://claude.com/docs/third-party/claude-desktop/code.md#claude-code-mods). Claude Desktop leaves out the whole `hooks` directory, which declares the mod, so neither the mod nor the plugin's hooks run on the host.
* **Enterprise Admin Console**: the device gets its configuration from the [console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)
* **Inference provider**: it is the [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md), or Code sessions get [`code` (not `cli`) settings from a Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab)
* **Policy on the device**: the device's Claude Code managed settings set a key such as `allowManagedHooksOnly`, `pluginConfigs`, or `disableSideloadFlags`
* **The plugin**: it declares `userConfig` options or dependencies, or comes from a marketplace that the user added from a folder or file on the device, or from one whose address in the device's Claude Code managed settings differs from where the device fetched it, until the device fetches it again

In other cases, such as these, the plugin isn't copied at all:

* **Hooks in the manifest**: the plugin's manifest declares hooks
* **Plugins that only managed settings turn on**: a plugin that only the device's Claude Code managed settings install and turn on stays on the device
* **A launcher that locates Claude Code itself**: where the session starts through a [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) on the host that the host's managed settings don't name, no plugin from the device is copied

Where a plugin runs without its hooks, a session shows a message, in some cases only the first time on a host, such as `A plugin from your organization runs without its hooks on <host>`, followed by the reason, or `A plugin from your organization has hooks that can’t be sent over SSH, so it runs without them on <host>.` Where `allowManagedHooksOnly` or `disableAllHooks` on the device stops plugin hooks in local sessions too, the session shows no message. No message doesn't mean that the hooks run.

Don't count on the deployment, the plugin, or a launcher to keep hooks off a host. To keep these hooks from running on your hosts, set one of these to `true` in [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy), deployed as a file or an OS policy on the device or the host. A Claude apps gateway's `cli` settings don't reach these sessions on a Claude Desktop that gets its configuration from the gateway.

| Setting | Where to set it | Effect |
| - | - | - |
| [`allowManagedHooksOnly`](https://code.claude.com/docs/en/settings-reference#allowmanagedhooksonly) or [`disableAllHooks`](https://code.claude.com/docs/en/settings-reference#disableallhooks) | Each device | Claude Desktop copies no `hooks` directory to any host. The setting also stops plugins' and users' hooks in [Cowork, Chat, and local Code sessions](https://claude.com/docs/third-party/claude-desktop/extensions.md#turn-off-user-hooks) on the device (under `allowManagedHooksOnly`, except those of plugins that the managed settings themselves turn on), and `disableAllHooks` stops the hooks in the device's own managed settings too. |
| [`disableSideloadFlags`](https://code.claude.com/docs/en/settings-reference#disablesideloadflags) | The host | Sessions load no plugin from the device, and show `Desktop skills and plugins are off in this session.` Hooks that are set up on the host keep running. |
| [`allowManagedHooksOnly`](https://code.claude.com/docs/en/settings-reference#allowmanagedhooksonly) or [`disableAllHooks`](https://code.claude.com/docs/en/settings-reference#disableallhooks) | The host | Copied plugins' hooks don't run. Neither do the hooks that users set up on the host, such as [alert hooks](#alert-the-user-with-hooks-on-the-host), or those of plugins that they installed there. `disableAllHooks` also stops the hooks in the host's own managed settings. |

For a host where no hook from any part of a copied plugin may run, use one of the host's settings. Under `allowManagedHooksOnly` or `disableAllHooks`, the plugins themselves still load on the host, with their MCP servers and skills. To keep those off too, use `disableSideloadFlags`.

A change on a device applies to sessions that start after it: a remote session that is already running keeps the hooks that were copied for it. `disableSideloadFlags` on a host also applies only to sessions that start after it. To stop the hooks of a session that is already running, [end its engine on the host](#how-a-remote-session-works).

In a device's or a host's first Claude Code managed settings, also set `parentSettingsBehavior` to `"merge"`, or they replace the [policy that Claude Desktop supplies](#managed-configuration-on-the-remote-host) (for a device, see [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device)). Where managed settings exist already, add the key to them and leave `parentSettingsBehavior` as it is.

A plugin's hooks aren't guaranteed to run on a host: some sessions start without them, and by default a hook that can't start lets the action go ahead. Check these limits before you rely on hooks, or on your policy, in remote sessions:

* **Policy that only devices have**: Claude Code on the host doesn't read the device's Claude Code managed settings. A [policy mod](https://code.claude.com/docs/en/plugins/mods/admin#enforce-a-policy-with-a-mod-of-your-own) that those settings install isn't copied, so copied hooks run without it. Install it through each host's managed settings too.
* **Policy on files and network**: `allowedWorkspaceFolders`, `blockReadsOutsideWorkingDirectories`, `coworkEgressAllowedHosts`, and permission rules don't apply to a command that a hook runs.
* **Marketplace lists on a host**: `strictKnownMarketplaces` and `blockedMarketplaces` in the host's managed settings don't stop a copied plugin's hooks. To stop them, set `disableSideloadFlags` there.
* **A [launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher) that the host's managed settings name**: hooks are copied to such a host too
* **The host's environment**: hooks run with the host's environment, not the device's. A variable that only the device sets, and that Claude Desktop doesn't send, is empty on the host, so a hook that deletes or writes under it can hit other files.
* **A hook that can't start on the host**: the tool call goes ahead. For a `PreToolUse` hook, the session shows `A hook of the "<plugin>" plugin gave no usable answer, so it didn't check this action.` the first time only; later calls go ahead with no message. To stop the call instead, see [Block the action when a hook fails](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails).
* **Files in the `hooks` directory**: files that a hook wrote there on the device, such as logs or state, are copied with it, and whoever administers the host can read them. The copy stays on the host for at least 30 days after its last use, or for good if no session starts there again, and of the settings above, count on the device's alone to stop the copying. Have hooks write outside the plugin's directory, for example in [`${CLAUDE_PLUGIN_DATA}`](https://code.claude.com/docs/en/plugins/components#path-variables-and-persistent-data).
* **A plugin that is turned off or removed on the device**: new sessions start without it. Remote sessions that are already running keep its hooks until you end their engines, as above.

### Read-only folders on the remote host

On a Linux or macOS host, Claude Desktop applies `mode` set to `ro` on an [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) entry by supplying Claude Code with permission rules that deny edits under the entry's path. The rules are Claude Code's own checks on what Claude does, not file permissions on the host. Where a folder must not change, use the host's file permissions to keep the SSH user from writing to it. Before Claude Desktop 2.31226.0, a folder with `mode` set to `ro` was allowed on the host but not read-only there.

A remote session doesn't enforce `mode` in these cases:

* **Windows hosts.**
* **Hosts with their own Claude Code managed settings**: Claude Code ignores the rules, and the sandbox settings that Claude Desktop supplies with them, unless the host's managed settings set `parentSettingsBehavior` to `"merge"`. Under `"merge"` the host's own values still win where the two differ, so `sandbox.enabled` set to `false` there leaves shell commands unsandboxed (see [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings)).
* **An entry that is or contains the SSH user's `~/.claude` folder, such as `~`**: Claude Code keeps its own files there. List narrower folders.

Where the rules apply, they cover the following:

* **Claude's file tools**: they refuse to create or change a file under the path, even in bypass permissions mode. A writable entry listed inside a read-only one is read-only for them too.
* **Shell commands that Claude runs with its Bash tool**: Claude Code's sandbox keeps them from writing under the path on a host where it runs, which on Linux needs Claude Code's [sandbox dependencies](https://code.claude.com/docs/en/sandboxing). The sandbox doesn't cover commands listed in Claude Code's `sandbox.excludedCommands`, or a path that contains one of `* ? [ ] ( ) { } | +` or a double quote. It may not stop commands in a folder that is listed through a symbolic link, so list each read-only folder by its real path, and keep it outside writable entries. On a host where the sandbox doesn't run, shell commands can still change the folder. For how the app reports that, see [Sandbox status on the remote host](#sandbox-status-on-the-remote-host).

The rules don't apply to the SSH user, or to other programs that run under that account. MCP servers on the host, hooks from Claude Code's configuration on the host, [mods](https://code.claude.com/docs/en/plugins/mods/overview) in plugins installed on the host, the [hooks of copied plugins](#plugin-hooks-on-the-remote-host), and the session's terminal (including commands that Claude runs there) can change the folder, and Claude Desktop and Claude Code can create git worktrees inside it.

### Sandbox status on the remote host

Claude Desktop asks Claude Code on the host whether the [sandbox](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) from your Claude Desktop policy is turned on and running there. Requires Claude Desktop 2.26454.0 or later. If `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset, your policy has no sandbox. For what Claude Desktop checks then, see [Sandbox from the host's managed settings](#sandbox-from-the-host%E2%80%99s-managed-settings). For a key that isn't set, see [Unset allowlist in Code sessions](https://claude.com/docs/third-party/claude-desktop/web-tools.md#unset-allowlist-in-code-sessions).

The answer is Claude Code's own report, and Claude Desktop compares only part of it with your policy:

* **Folders**: Claude Desktop doesn't compare the folders that the sandbox allows with the folders in your policy.
* **Network hosts**: if the answer lists the network hosts that the sandbox allows, and a network host from your policy is missing from the list, Claude Desktop reports the reason `overridden`. Claude Desktop doesn't check for network hosts that the remote host's own settings add. Requires Claude Desktop 3.6556.1 or later.

When the sandbox isn't confirmed, the session continues and shell commands can run outside the sandbox. To keep Claude Code from starting on a host whose operating system has no sandbox or that lacks a dependency, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) to `true` and [`parentSettingsBehavior`](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) to `"merge"` in the host's Claude Code managed settings. With `"merge"`, that setting applies together with your policy, where no server-managed or gateway settings apply. To require the sandbox from Claude Desktop's configuration, see [Refuse sessions on a host without a working sandbox](#refuse-sessions-on-a-host-without-a-working-sandbox).

Find the message, or the `reason` your collector received, for the cause and the fix.

| Message in the session | `reason` your collector receives | Cause | Fix |
| - | - | - | - |
| Shell commands on `<host>` are running outside your organization's sandbox, which couldn't start | `cannot_start` | The sandbox is turned on but isn't running, for example because a Linux host lacks the sandbox dependencies | Install the [dependencies](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) on the host, then start a new session |
| Your organization's sandbox isn't running on `<host>`. Claude Code has no sandbox for that operating system | `unsupported` | The host runs an operating system that Claude Code reports no sandbox for, such as Windows | Use a macOS or Linux host |
| Your organization's sandbox policy isn't fully applied on `<host>`, so shell commands there may run outside it | `overridden` | Claude Code managed settings on the host replace your policy, even when they say nothing about the sandbox, or they turn the sandbox off or loosen it | Set `parentSettingsBehavior` to `"merge"` in the host's managed settings, and remove `sandbox` values there that conflict with your policy |
| No message | `unknown` | Claude Code gives no answer that Claude Desktop can read | In a session on that host, ask Claude to run the two commands under [Confirm commands run inside the sandbox](https://code.claude.com/docs/en/sandboxing#confirm-commands-run-inside-the-sandbox) |

> [!NOTE]
>
> On a device where the [local configuration file governs](#sandbox-from-the-host%E2%80%99s-managed-settings), Claude Desktop 4.16336.0 or later words these messages differently. They name `the sandbox from your inference configuration`, not your organization's sandbox or sandbox policy.

The fix for the `overridden` message and the fix for the message under [Policy status on the remote host](#policy-status-on-the-remote-host) start at the same setting, `parentSettingsBehavior`. With Claude Desktop 3.6556.1 or later, a session that shows one of the two messages doesn't add the other until the first no longer applies. Your collector still receives the event of the check whose message is held back, and the **Sandbox** row of `/status` still shows the sandbox's state.

To check one session, have the user open it, wait until Claude has finished replying, and enter `/status` in the message box. Where your policy includes the sandbox, the **Session info** card has a **Sandbox** row, which shows what Claude Desktop last learned. Requires Claude Desktop 2.31226.0 or later. Find the value's `reason` in the table of messages and reasons for the cause and the fix:

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
* **`refuse_set`**: `true` when Claude Desktop sent the [`refuse`](#refuse-sessions-on-a-host-without-a-working-sandbox) requirement with the session's start, and absent otherwise.

The event doesn't name the host. To find the host, ask the user that the [user attribution](https://claude.com/docs/third-party/claude-desktop/telemetry.md#user-attribution) attributes identify.

### Refuse sessions on a host without a working sandbox

To stop Code sessions over SSH on a host where the [sandbox](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) from your policy can't start, set [`sshHostSandboxUnavailable`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostsandboxunavailable) to `refuse` in Claude Desktop's configuration. With the key unset or set to `warn`, such sessions run with a [warning](#sandbox-status-on-the-remote-host), and shell commands can run outside the sandbox.

Deliver the key as follows:

* **Versions**: update your devices first, and a Claude apps gateway that delivers your configuration, because an older gateway doesn't start with the key. Earlier versions of Claude Desktop run sessions as under `warn`, and on Windows and Linux a profile with the key [can turn off their other settings](https://claude.com/docs/third-party/claude-desktop/mdm.md#keys-that-an-earlier-version-does-not-recognize). The [configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md) gives the versions.
* **Source**: where a bootstrap server or the Enterprise Admin Console delivers your configuration, set the key there, not in a device management profile, whose value Claude Desktop then drops. Elsewhere, add the key to a profile that holds your whole configuration, because a profile that sets it replaces the local configuration. A device's first profile [changes more than that](https://claude.com/docs/third-party/claude-desktop/mdm.md#what-a-profile-or-policy-changes-on-a-device). A device that gets the key from a profile, or from the profile's bootstrap server, can move to an Enterprise Admin Console organization, and that `refuse` then doesn't apply: see [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization).
* **Value**: write `refuse` or `warn` in lower case. Any other value that isn't empty, such as `Warn`, counts as `refuse`.
* **Restart**: expect Claude Desktop to ask users to restart it after the key changes, whether or not they use SSH.

#### What refuse does on a host

Claude Code on the host checks the sandbox each time it starts for a session, and exits if the sandbox isn't available. The session shows the card [A required sandbox isn't available](#a-required-sandbox-isn%E2%80%99t-available), and tries again when the user sends a message.

* **Linux hosts**: the check fails, for example, where a [sandbox dependency](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) is missing or AppArmor keeps bubblewrap from starting.
* **Windows hosts**: Claude Code reports no sandbox there, so sessions don't start, apart from the [cases where sessions still run](#where-sessions-still-run-under-refuse).
* **Sessions that are already running**: they continue until their next start. A resumed session, a scheduled run, and a side chat each count as a start.

#### Where sessions still run under refuse

Check your policy and your hosts for these cases:

* **Your configuration asks for no sandbox**: it asks for none where `coworkEgressAllowedHosts` contains `*` and `allowedWorkspaceFolders` is unset. On a device whose only configuration is the local configuration file, [an unset `coworkEgressAllowedHosts` doesn't turn on the sandbox by itself](https://claude.com/docs/third-party/claude-desktop/web-tools#unset-allowlist-in-code-sessions) either. Both keys reach well beyond SSH, so read the entries for [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) and [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) before you change them.
* **Claude Code managed settings on the host replace your policy**: they do so unless `parentSettingsBehavior` there is `"merge"`, and settings from a policy helper do so either way. `refuse` then applies only if settings on the host turn a sandbox on. Where none do, a Windows host starts sessions too.
* **Server-managed or gateway settings replace your policy**: with the [Claude API](https://claude.com/docs/third-party/claude-desktop/claude-api.md) as the inference provider, Claude Code on the host fetches the [server-managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) of the organization that owns the credential. If that organization has any, they replace your policy on every host, even one with no managed settings of its own, unless `parentSettingsBehavior` in them is `"merge"`. While they apply, Claude Code by default ignores most keys in a file or profile on the host, `"merge"` among them. A [Claude apps gateway's `code` settings](https://claude.com/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) rank the same way, but merge unless they set `"first-wins"`.
* **Managed settings loosen the sandbox**: even under `"merge"`, the values in the host's managed settings, the server-managed settings, or a gateway's `code` settings take priority over the values in your policy, for example `sandbox.enabled` or `sandbox.failIfUnavailable` set to `false`.
* **A launcher on the host locates Claude Code itself**: with [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudecodeprocesswrapperenabled) on, a session through such a launcher gets no sandbox settings from your policy, whatever `parentSettingsBehavior` says. A launcher that the host's managed settings name in `processWrapper` is different. `refuse` applies through it where those settings set `"merge"`, no server-managed or gateway settings apply, and the launcher passes its arguments on.
* **The sandbox passes the check and fails later**: the session starts with no card, and each shell command that would run in the sandbox fails or is refused. Have the host's administrator repair the sandbox.

Where Claude Code's managed settings replace your policy, set `parentSettingsBehavior` to `"merge"` in them, as [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) describes. `"merge"` applies to every application that starts Claude Code under those settings, Claude Desktop's local Code sessions included, and lets that application's allow rules and sandbox allowlists apply: see [Let an embedding host add policy](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy), which also says which source Claude Code reads the key from. If the same settings set `sandbox.failIfUnavailable` to `true`, the sessions for which your policy asks for a sandbox then [don't start on Windows](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings), or on any machine where the sandbox can't start.

The rest is Claude Code's own policy, which applies to every Claude Code that reads it, including Claude Code in a terminal. To require a sandbox in that policy, which is the only way for a session through a launcher that locates Claude Code, follow [Enforce sandboxing with managed settings](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) and [How Claude Code combines managed sources](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources) in the Claude Code documentation. Settings that you create for this replace your policy too, unless they set `"merge"`.

Where a sandbox starts that didn't run before, a `true` for [`sandbox.autoAllowBashIfSandboxed`](https://code.claude.com/docs/en/settings-reference#sandbox-autoallowbashifsandboxed) in a user's, a project's, or a local settings file on the host takes effect: sandboxed Bash commands then run without a prompt, even past an ask rule for all of Bash.

To find sessions that started under `refuse` and run without a confirmed sandbox, look for `refuse_set` on the [`desktop_ssh_sandbox_check_failed`](#sandbox-status-on-the-remote-host) event. The attribute is absent for a session through a launcher that locates Claude Code, and for a process that started before you set the key. A sandbox that fails later and a refused start send no such event, so a missing event is no proof that the sandbox runs.

#### What refuse leaves out

Don't count on `refuse` to keep everything on the host inside the sandbox:

* **A refused host**: Claude Desktop still connects to it and installs Claude Code there, and MCP servers and `SessionStart` hooks can run before Claude Code exits.
* **Excluded commands**: the sandbox doesn't cover commands listed in Claude Code's `sandbox.excludedCommands`. Under `refuse`, Claude Desktop shows the [`overridden`](#sandbox-status-on-the-remote-host) warning where Claude Code reports such commands, and the session continues.
* **Other programs**: MCP servers on the host, hooks, `!` commands, and the session's terminal (including commands that Claude runs there) run outside the sandbox.
* **The SSH account and repositories**: `refuse` doesn't protect against the SSH user, or against settings in that account or in a repository.

### Sandbox from the host's managed settings

Where your policy has no sandbox, Claude Desktop 4.16336.0 or later asks Claude Code whether managed settings on the host turn a sandbox on, and reports one that isn't running.

Expect fewer reports than for a sandbox from your policy:

* **The session**: it continues, and shell commands run outside the sandbox. To keep Claude Code from starting instead, set [`sandbox.failIfUnavailable`](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings) to `true` in the same managed settings.
* **Reasons**: only `cannot_start` and `unsupported`, with the same messages, `/status` value, and event as under [Sandbox status on the remote host](#sandbox-status-on-the-remote-host). The table's rows for those two apply here too. Claude Desktop never reports `overridden` or `unknown` here.
* **A host that has the packages**: it can still report `cannot_start`, for example Ubuntu 24.04 without an AppArmor profile for bubblewrap. [Set up Linux and WSL2](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) covers the profile too.
* **`/status`**: the **Sandbox** row appears only after Claude Desktop has reported that sandbox as not running. After `cannot_start`, the row can stay for the rest of that session, so check a fix in a new session.
* **No report**: don't take it as proof that the sandbox runs. To confirm, have the user ask Claude to run the two commands under [Confirm commands run inside the sandbox](https://code.claude.com/docs/en/sandboxing#confirm-commands-run-inside-the-sandbox).
* **The event**: it doesn't say which sandbox it is about. From a device whose policy has no sandbox, it is about the host's sandbox.
* **A device where the local configuration file governs**: Claude Desktop doesn't ask there. The file governs where neither device management, the Enterprise Admin Console, nor a bootstrap server delivers the configuration. It still governs where a device management profile sets only app-behavior keys, such as `disableAutoUpdates`.

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

> [!NOTE]
>
> On a device where the local configuration file governs, Claude Desktop 4.16336.0 or later starts the message with `The policy from your inference configuration`, and doesn't mention an admin. The message after a fix starts with the same words.

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
* On a Linux host, glibc 2.17 or later, or musl. The Claude Code engine is a single executable, and its glibc build links only against glibc's own libraries. Version 2.17 is the oldest glibc that the glibc build can load, and Claude Code's [system requirements](https://code.claude.com/docs/en/setup#system-requirements) still apply. To see the host's C library and its version, run `ldd --version` on the host. For a musl host, see [Alpine Linux and musl-based distributions](https://code.claude.com/docs/en/setup#alpine-linux-and-musl-based-distributions).
* An SSH server. On Windows, Microsoft's OpenSSH Server; with other SSH servers, the engine does not survive a dropped connection.
* The SSH server's SFTP subsystem. For a Linux or macOS host that lacks it, see [Hosts without SFTP](#hosts-without-sftp).
* If devices connect with Claude Desktop's built-in SSH client, an SSH server that accepts several sessions on one connection. Before Claude Desktop 4.16336.0, that client is the default on Windows devices, and in later versions it still connects to hosts already in use. The built-in client can't connect where the server's `sshd_config` sets `MaxSessions 1`. Raise that limit, for example to OpenSSH's default of 10, or see [Hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection).
* The server doesn't need to allow TCP, Unix socket, agent, or X11 forwarding. A `ProxyJump` host must allow TCP forwarding to the SSH port of the session's host.
* A POSIX shell, or PowerShell on Windows.
* `git` on the path, for git features.
* A home directory that the SSH user can write to and run programs from, with about 1 GB of disk space for the three Claude Code versions the app keeps and a fourth while an update installs. A home directory mounted `noexec` doesn't work.

The device needs the OpenSSH client (`ssh` and `ssh-keygen`). Claude Desktop runs the first `ssh` on the user's `PATH`. On Windows, that is the first `ssh.exe`, and a `.bat`, `.cmd`, or `.ps1` wrapper named `ssh` isn't run. For the `ssh` that carries the connection on a Windows device, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

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

Claude Desktop makes the SSH connection by running the device's OpenSSH client, so authentication uses the Kerberos (GSSAPI), certificate, and `ssh_config` support of your own OpenSSH build. The program is the one `sshClientPath` names, or else, on macOS and Linux, the first `ssh` on the user's `PATH`, and it must be OpenSSH 7.6 or later. On Windows, the device's OpenSSH client is the default in Claude Desktop 4.16336.0 or later, and only for hosts that are new to the device. See [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

To use one client for every host, set [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) (beta) to `system-openssh` or `builtin`. Both apply on every platform. A change applies to new connections, and sessions that are already connected keep their client.

* **`system-openssh`**: use the device's OpenSSH client.
* **`builtin`**: use the app's built-in SSH client. The app still runs the device's OpenSSH tools to evaluate the user's SSH configuration, look up host keys, and run the session's terminal. Where it can't run `ssh-keygen`, connections to hosts whose keys it checks fail (see [SSH host key verification failed](#ssh-host-key-verification-failed)). The in-app help and some cards call this client the built-in library.
* **`auto`**: the same as leaving the key unset.
* **Any other value**: the app can't read a value such as a misspelling, and the built-in client makes every connection.

The app also uses the built-in client in these cases, and on Windows in the cases under [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client):

* **The device can't start the OpenSSH client**: while `sshTransport` is unset or `auto` and `sshClientPath` is unset, the app uses the built-in client for every connection until Claude Desktop restarts. If the device can't start `ssh-keygen` either, connections fail at the host key check (see [SSH host key verification failed](#ssh-host-key-verification-failed)). Requires Claude Desktop 2.7032.0 or later.
* **Claude Desktop is installed from the Microsoft Store**: the built-in client makes the connection unless `sshTransport` is `system-openssh`. With `system-openssh`, the device's OpenSSH client makes the connection, but the app can't show its prompts for a password, a one-time code, or a key passphrase, or its question about a host key that isn't on record. Use a sign-in method that needs no prompt, such as a key held by the SSH agent, and have users connect to each host once from a terminal before adding it in the app, so that the host's key is in the user's `known_hosts` file.

Claude Desktop writes the following into the SSH user's home directory on the host. Each user who connects gets their own copy.

| Path on the host | Contents |
| - | - |
| `~/.claude/remote/srv/<version>/` | The remote server that Claude Desktop talks to |
| `~/.claude/remote/ccd-cli/` | The Claude Code engine, one file per build, under a name that starts with its version (the three most recent are kept) |
| `~/.claude/remote/run/<id>/` | The server's socket, token, and log |
| `~/.claude/remote/plugins/<id>/` | Plugins synced from the device, in one folder for each Claude Desktop installation that connects |
| `~/.claude/remote/session-folders/` | The remote server's record of the folders that sessions have worked in, kept as small files. Requires Claude Desktop 4.16336.0 or later |
| `~/.claude/uploads/<session-id>/` | Files the user attached to a message. Not removed when the session ends |
| `~/.claude/` and `~/.claude.json` | Claude Code's own data, including session transcripts. See [Data storage](https://claude.com/docs/third-party/claude-desktop/data-storage.md) |

Each side of a remote session needs its own network access.

* Devices installed with the regular installer must reach `downloads.claude.ai`: Claude Desktop downloads the remote server there and uploads it to the host. Devices installed with the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation) don't: it bundles the remote server and the Claude Code engine for Linux x64 and arm64 hosts, and Claude Desktop uploads both. Hosts on other platforms still need the download, so an offline-installed device that cannot reach `downloads.claude.ai` fails the session with a message saying the installer doesn't include remote components for that platform.
* The host must reach your inference endpoint and, if configured, your OTLP collector, plus whatever the user's own work needs. With the regular installer, it downloads the Claude Code engine from `downloads.claude.ai` when it can; when that fails, Claude Desktop downloads the engine on the device and uploads it. Unless you disabled telemetry, the engine on the host also reports to the same Anthropic hosts as a local Code session (see [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md)). Blocking them does not affect the session.

### Hosts without SFTP

A remote session can start on a Linux or macOS host where SFTP is turned off or doesn't work. Claude Desktop then places its own setup files on the host with shell commands instead of SFTP. Before Claude Desktop 3.1623.0, setup fails on such a host.

These features need SFTP, so they are off in that session. Users can keep working without them. With Claude Desktop 4.23118.0 or later, some connections from Windows devices don't use the host's SFTP service for these features. On those connections they can go on working for up to seven days after SFTP is turned off or stops working, or longer on a connection that stays open.

* Image and document previews
* File attachments
* The Changes pane
* Plugins that Claude Desktop copies from the device
* [File downloads](#file-downloads-from-the-remote-host), except text files up to 1 MiB: the download option is missing, or the download fails with `Couldn't download <name>`

A session without SFTP needs at least the following. Where one is missing, setup fails (see [Setup on the host fails after SSH connects](#setup-on-the-host-fails-after-ssh-connects)).

* **Version**: Claude Desktop 3.1623.0 or later on the device.
* **Client**: the device's OpenSSH client makes the connection. The built-in client needs SFTP. Before Claude Desktop 4.16336.0 it is the default on Windows devices, and in Claude Desktop 4.16336.0 or later it still makes the connection in some cases. To have the device's OpenSSH client make every connection, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).
* **Shell**: a POSIX shell on the host, with `sh` and the standard Unix tools such as `ls`, `cat`, and `rm`.
* **Base64 decoder**: `base64` or `openssl` on the host.
* **SHA-256 tool**: `sha256sum`, `shasum`, or `openssl` on the host.

To bring back the features that are off, match the second sentence of the notice that the user sees in the conversation. The notice begins, for example, "Image and document previews, file attachments, the Changes pane, and your computer's plugins are off."

* **"turn on SFTP"**: the SSH server refuses SFTP. Enable `Subsystem sftp` in the server's `sshd_config`, and reload the SSH server.
* **"see why SFTP doesn't start"**: the SSH server accepts the request for SFTP, but SFTP never starts. In a terminal on the device, run `sftp` with the same host to see what stops it, then fix that on the host.
* **"let SFTP reach your home folder"**: over SFTP, Claude Desktop didn't find a folder it made under the SSH user's home directory, as when SFTP is confined to a folder. Set up the SSH server so that SFTP sees the home directory at the same path as the login shell does.
* **"refused the second sign-in"**: SFTP isn't at fault. The host refused what the user entered at the sign-in for file transfer, as it can when the user enters the same one-time code twice. Claude Desktop makes that second sign-in on [hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection) and from [Windows devices that use the device's OpenSSH client](#prepare-windows-devices-for-the-openssh-client). If the host refuses it each time, have the user sign in by a method that needs no prompt, such as a key that an SSH agent holds. Before Claude Desktop 4.29.0, the connection fails.

After the change, or to try the sign-in again, have the user quit and reopen Claude Desktop and start a new session.

### Hosts that allow one session per connection

A device can connect to a host whose `sshd_config` sets `MaxSessions 1` only when the device's OpenSSH client makes the connection:

* **macOS and Linux devices**: the device's OpenSSH client is the default. The device also needs Claude Desktop 3.1623.0 or later.
* **Windows devices**: the built-in client can't connect to such a host. Before Claude Desktop 4.16336.0 it is the default, and in Claude Desktop 4.16336.0 or later it still makes the connection in some cases. To have the device's OpenSSH client make every connection, see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client).

Connecting to a host with this limit changes what the SSH server's log shows and how often devices sign in:

* **Refused sessions**: when a macOS or Linux device first connects to the host, the SSH server's log shows a sign-in followed by `no more sessions`. Claude Desktop remembers the limit for 7 days at a time: at the device's next connection after that, the log shows the sign-in and the refusal again. The refusal is how Claude Desktop learns of the limit, so you don't need to act on it. A Windows device that connects through the device's OpenSSH client causes no such refusal.
* **More sign-ins**: each time a device connects or reconnects, it signs in at least twice, to run commands and to transfer files. Expect at least one more sign-in for each terminal tab, and for each Claude Desktop session in which the user runs commands that start with `!`.
* **One-time codes**: if the host also asks for a one-time code, users get a prompt at each sign-in for a connection or a terminal tab. Commands that start with `!` fail on that host, so have users run commands in a terminal tab.

### Prepare Windows devices for the OpenSSH client

With Claude Desktop 4.16336.0 or later, a Windows device connects to each host that is new to it through the device's OpenSSH client. A host that the device already connects to stays on the app's built-in SSH client, with no action required. A new or re-imaged PC, or a virtual desktop that keeps no local app data, has no hosts in use, so every host is new to it. The same holds where the app's record of earlier connections is damaged, because the app then resets it. A host that the device last connected to before Claude Desktop 1.46388.1 can count as new too, because earlier versions may have kept no record of it. Before Claude Desktop 4.16336.0, the built-in client makes every connection on Windows unless [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) (beta) is `system-openssh`.

Choose what your Windows devices do. For the first and the third choice, check what the device's OpenSSH client needs, under **Check what the device's OpenSSH client needs on Windows** below.

* **Leave `sshTransport` unset**: new hosts and new PCs use the OpenSSH client.
* **Keep the built-in client for every host**: set `sshTransport` to `builtin`. The setting applies to new hosts and new PCs too. If `sshClientPath` starts with `%LOCALAPPDATA%\`, remove it too, or SSH connections fail. See **If you set `sshTransport`** below.
* **Use the OpenSSH client for every host**: set `sshTransport` to `system-openssh`. To go back, set `builtin`, and if `sshClientPath` starts with `%LOCALAPPDATA%\`, remove it too. See **If you set `sshTransport`** below.

With `sshTransport` unset or `auto`, the app still uses the built-in client in these cases, and in those under [Host requirements](#host-requirements):

* **Hosts already in use**: a host that the device has reached only with the built-in client stays on it. A host that the device first reaches while `builtin` is set, or while it has no usable OpenSSH client, stays on the built-in client too. The same goes for a host first reached with a `.ppk` file that the built-in client can read, or after Windows didn't let the app start its sign-in helper.
* **Configuration that hasn't loaded**: on a device that takes its configuration from the Enterprise Admin Console or a bootstrap server, the built-in client makes every connection at each launch until that configuration has loaded. If your bootstrap response sets `system-openssh`, set it in the registry too, so that it applies in this case.
* **A record that can't be read**: while the app can't read its own record of earlier connections, for example while a scanner holds the file, the built-in client makes that connection, whatever the host.
* **PuTTY key files**: a host whose identity file in the app is a PuTTY `.ppk` file that the built-in client can read, for example version 2, RSA, with no passphrase.
* **A blocked sign-in helper**: a host that asks for a password or a one-time code, where Windows doesn't let the app start its sign-in helper while a user waits for the connection. Where the helper is missing or gives no answer, or where the app can start the helper but `ssh.exe` can't, the sign-in fails instead.
* **Another `ssh` program**: `sshClientPath` names an OpenSSH that isn't Microsoft's, or a Microsoft OpenSSH (Win32-OpenSSH) before 9.4. Unless the value starts with `%LOCALAPPDATA%\`, the app still runs the named program to read the user's SSH configuration and to run the session's terminal. With such a value and `sshTransport` not set to `system-openssh`, the app doesn't start the program, and SSH connections fail.
* **No usable OpenSSH client, and no `sshClientPath`**: the app uses the built-in client for every connection, whatever `sshTransport` says. See **Devices without a usable client** below.
* **An `sshClientPath` program that gives no answer**: the built-in client tries the connection, whatever `sshTransport` says. See [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows).

Four of these cases pass with time. They are configuration that hasn't loaded, a record that can't be read, an `ssh.exe` that Windows wouldn't start, and an `sshClientPath` program that gave no answer. A new host first reached in such a case isn't kept on the built-in client: once the case has passed, its connections use the OpenSSH client.

A host under **Hosts already in use** moves to the OpenSSH client, or counts as new, in cases such as these. Once the OpenSSH client has connected to it, the host stays on the OpenSSH client.

* **You set `system-openssh`**: once one connection has succeeded under that setting, earlier use of the built-in client keeps no host on that client, even if you remove the setting later. Cases such as **PuTTY key files** still apply.
* **A host key that the built-in client can't check**: the user's `known_hosts` file has no plain entry for the host, and `ssh` would check its key against a certificate authority or another `known_hosts` file. The system-wide file is one such file. The host moves at its next connection.
* **A jump host**: a host that is given a jump host moves at its first connection after the user has quit and reopened Claude Desktop. Until then the built-in client dials the host without the jump host.
* **A record that is lost**: on a re-imaged PC, or once the app has reset a damaged record, every host counts as new.

Nothing that a user does to a saved connection in Claude Desktop moves its host. Removing the connection and adding it again at the same address, or editing its address, keeps the client. The same machine added under another name, address, or port counts as a new host. A user who edits their own `~/.ssh/config` or `known_hosts` file can cause the second or third case above.

While hosts stay on the built-in client:

* **Host key checks**: a host on the built-in client keeps that client's [host key check](#ssh-configuration-on-the-device), which reads the user's `known_hosts` file alone, not the system-wide one or a `RevokedHostKeys` file. To move those hosts to `ssh`'s own check, on a device with a usable OpenSSH client, set `sshTransport` to `system-openssh`.
* **Which client connected**: search `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) for `master ready for` (the OpenSSH client) or `[SSH2Connection] Connected to` (the built-in client). If both appear for one connection, the later one counts. For the reason, search for `this connection attempt uses`: the line ends with the source of the choice, such as `host_kept` for a host already in use. Two devices can use different clients for the same host.

With the device's OpenSSH client on a Windows device:

* **Repeated sign-ins**: each time Claude Desktop connects or reconnects to a host, it signs in at least twice, to run commands and to transfer files, and once more for each terminal that opens. A Windows host needs at least one more sign-in each time. On a Windows device, each sign-in is a separate `ssh` process. They stay open together, so a per-user login limit on the host has to leave room for them. Each process connects to the host by name, so a name that stands for several machines, such as a load balancer or round-robin DNS, must send all connections from one device to the same machine. Claude Desktop repeats a typed password or key passphrase itself for the other sign-ins of that connection. A host that asks for a one-time code, a push approval, or a security key touch asks again at each sign-in.
* **Key files that other accounts can read**: `ssh` ignores a private key file that any account but the user, SYSTEM, or Administrators can read. After a sign-in fails because of such a file, Claude Desktop tightens the file's access list where it can, and connects again. `ssh.log` records the list before and after.
* **Host keys that aren't on record**: where the app can show a prompt, it asks the user whether to trust the key, and records a trusted key in the user's `known_hosts` file. To distribute host keys instead, see [SSH configuration on the device](#ssh-configuration-on-the-device).
* **Saved passwords**: when the session's host asks for the account password, the sign-in dialog has a **Remember password for `<host>`** checkbox. To turn saved passwords off, set [`disableSshSavedPasswords`](https://code.claude.com/docs/en/desktop#managed-settings) to `true` in Claude Code's managed settings on the device, by the steps for `disableDesktopLocalSessions` in those settings under [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). The dialog then has no checkbox, and the app stops using passwords that it saved earlier. It doesn't delete them, and the user's settings no longer offer to forget one. Removing the connection in the app still deletes its saved password. Deliver the setting before devices start to use the OpenSSH client. Neither the Enterprise Admin Console nor a bootstrap server can deliver it.

Check what the device's OpenSSH client needs on Windows:

* **Client version**: with no [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath), a usable client prints a version that starts with `OpenSSH_for_Windows_` and is 9.4 or later. That is Microsoft OpenSSH, also called Win32-OpenSSH. Run `ssh -V` in a Command Prompt window on a device, signed in as the user. If that output is anything else, run `ssh.exe -V` in `%SystemRoot%\System32\OpenSSH` and in `%ProgramFiles%\OpenSSH`: Claude Desktop uses the first usable client that it finds, on the `PATH`, then in those two folders in that order. If you set `sshClientPath`, run that program with `-V` instead. With `sshTransport` unset or `auto`, or in Claude Desktop 3.1623 and earlier, it has to pass the same test. With `system-openssh`, it can instead be an OpenSSH client that isn't Microsoft's. Such a client has to meet the conditions in [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) or in [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user). Each section names the Claude Desktop version that it requires.
* **Devices without a usable client**: on a Windows device with no usable OpenSSH client and no `sshClientPath`, the built-in client is used, whatever `sshTransport` says. If the device can't run `ssh-keygen` either, connections fail at the host key check (see [SSH host key verification failed](#ssh-host-key-verification-failed)). Add the **OpenSSH Client** optional feature in Windows and install pending Windows updates, or install [Microsoft's newer build](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/upgrade-in-box-openssh-to-latest-openssh-release). Run the version check again, then have users quit and reopen Claude Desktop. Hosts that the device first reached without a usable client stay on the built-in client. To move them, set `sshTransport` to `system-openssh`.
* **Application control**: `ssh` shows its prompts through three helper programs that ship with Claude Desktop, `claude-ssh-askpass.exe`, `claude-ssh-broker.exe`, and `claude-ssh-proxy.exe`. Allow them in your application control policy by their publisher, Anthropic, PBC. Their folder changes with each update, and the files carry no product name or version. Allow the `ssh.exe` that the version check found, and the `ssh-keygen.exe` beside it, too. If Windows refuses to start the helpers, the app can't ask for a key passphrase, and `ssh` refuses a host whose key isn't on record. If `sshTransport` is `system-openssh`, sign-ins that need a password or a one-time code fail. Otherwise, if the app itself can't start the helper, the built-in client makes those sign-ins. See [This computer won't start Claude's SSH sign-in helper](#this-computer-won%E2%80%99t-start-claude%E2%80%99s-ssh-sign-in-helper).
* **Firewall and endpoint security**: if your endpoint security software blocks `claude-ssh-askpass.exe`, `claude-ssh-broker.exe`, or `claude-ssh-proxy.exe` after a Claude Desktop update, have it trust their publisher, `Anthropic, PBC`, rather than a path or a file hash. See [Endpoint security software](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software). Allow `ssh.exe` outbound wherever you allow Claude Desktop itself. With `sshTransport` unset or `auto` and no `sshClientPath`, the built-in client takes over where Windows refuses to start `ssh.exe`, but not where `ssh.exe` starts and can't reach the network. Each connection that the OpenSSH client makes then fails or times out, and the card points to the network or the host, not to `ssh.exe`.
* **While `ssh.exe` can't reach the network**: a host that stays on the built-in client still connects. For other hosts, set `sshTransport` to `builtin`, for Windows devices only, until you can allow `ssh.exe` (see **One value for all platforms** below). A host that the device first reaches meanwhile stays on the built-in client afterwards. The session's terminal runs `ssh.exe` with either client, so it stays blocked until then.
* **Key files**: `ssh` doesn't read a PuTTY `.ppk` key file. Unless the host stays on the built-in client because of that file (see **PuTTY key files** above), export the key in OpenSSH format, and have the user select the exported file as the connection's identity file.
* **SSH configuration files**: `ssh` reads the user's `~/.ssh/config` itself, and the connection fails if `ssh` rejects the file. In a Command Prompt window on a device, signed in as the user, run the usable client with `-G` and a host, for example `ssh -G build01.corp.example.com`. Use the client's full path if it isn't the first `ssh` on the `PATH`. `ssh` prints the host's settings if it accepts the file, and an error if it doesn't.

If you set `sshTransport`:

* **One value for all platforms**: `sshTransport` has no per-platform form. A Windows registry policy reaches Windows devices only. A value from a bootstrap server or the Enterprise Admin Console reaches the macOS and Linux devices that it serves too. The device's OpenSSH client already makes the connection there by default, so `builtin` moves them to the built-in client. To change Windows devices alone from a bootstrap server, return the key only in responses that go to them.
* **Devices with a bootstrap server**: an available [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) replaces the `sshTransport` and `sshClientPath` that device management sets in the registry, even if it leaves a key out. A response without `sshTransport` puts the device back on the default. A response without `sshClientPath` cancels your pin. Claude Desktop then chooses the client as if you had pinned nothing (see **Client version** above). Where the built-in client connects, the first `ssh` on the user's `PATH` reads the SSH configuration and runs the terminal. Return both keys in the response too. Return a Windows path only in responses that go to Windows devices. `sshClientPath` has no per-platform form either, and SSH connections fail on a macOS or Linux device that gets a Windows path.
* **Keys that a bootstrap response leaves out**: where a response leaves out `sshTransport` or `sshClientPath` and the registry sets it, Claude Desktop 4.29.0 or later writes a line to `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) each time it connects to an SSH host. The line contains `the device profile sets` and names the key.
* **Devices on the Enterprise Admin Console**: the console's configuration replaces the registry's `sshTransport` and `sshClientPath`, even where the console leaves them unset. Set them in the console too. A client that isn't Microsoft's, or a value that starts with `%LOCALAPPDATA%\`, doesn't connect when it comes from the console. The console's `sshClientPath` reaches its macOS and Linux devices too, and SSH connections fail there under a Windows path. See [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization).
* **When a change takes effect**: at each host's next connection. An open app applies a change in the registry at its next configuration check. From a bootstrap server or the Enterprise Admin Console, an open app applies a new value only if it is `builtin`, once two configuration checks in a row return it. Other values apply, at the latest, once the app has been reopened and has downloaded the configuration. A host that is connected keeps its client until the connection drops, which can take days. To move it at once on a Windows device, have the user quit and reopen Claude Desktop. After a change to the managed configuration the reopened app can fail to rejoin the engine, and a turn that still runs on the host is then cut short, as [How a remote session works](#how-a-remote-session-works) describes. With a bootstrap server, a host that connects before the reopened app has downloaded the configuration uses the registry's value. Where the registry sets none, and with the console, see **Configuration that hasn't loaded** above.
* **What `builtin` leaves on the device**: going back undoes nothing that was written while the OpenSSH client was in use. Saved passwords and new entries in the user's `known_hosts` file stay. The access list of a private key file that the app tightened stays too, and `ssh.log` recorded that list as it was before. The user's settings don't offer to forget a saved password under `builtin`, but removing the connection deletes it.

### SSH configuration on the device

Claude Desktop applies the host's entry in the user's `~/.ssh/config`. With the device's OpenSSH client, `ssh` reads the entry itself, so settings such as `ProxyJump`, certificate host keys, and GSSAPI authentication apply, and the app still connects only to the resolved hostname that passed `sshHostAllowlist`. The built-in client applies the hostname, port, user, identity file, SSH agent, and `ProxyCommand`.

* For hosts behind a bastion, configure a `ProxyJump` or `ProxyCommand`. `ProxyJump` works only when the device's OpenSSH client carries the connection. The built-in client refuses it. For the card that the user sees, see [Ask your IT administrator to set sshTransport to system-openssh](#ask-your-it-administrator-to-set-sshtransport-to-system-openssh).
* A bastion must match `sshHostAllowlist` too. See [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist).
* With the device's OpenSSH client, OpenSSH's own host key checking applies. For a host whose key isn't on record yet, where the app can show a prompt, it shows the key's fingerprint, asks the user whether to trust it, and records a trusted key in the user's `known_hosts` file, unless the user's own SSH configuration accepts new keys without asking. On some connections the app can't show a prompt, for example when it reconnects in the background. Distribute the host keys or a host certificate authority to the devices, so that each host's key is on record before users connect. `@cert-authority` entries are honored. A key that differs from the one on record for the host is refused, whatever the entry's `StrictHostKeyChecking` says, unless another setting in the SSH configuration that applies to the host turns that check off, such as `NoHostAuthenticationForLocalhost yes` for a host on a loopback address.
* With the device's OpenSSH client, you can keep the app from asking users to trust the key of a host that isn't on record yet. Distribute the host keys in the client's system-wide `known_hosts` file, such as `/etc/ssh/ssh_known_hosts`, or distribute a host certificate authority. Then set `StrictHostKeyChecking yes`, for example under `Host *`, in the client's system-wide configuration file, such as `/etc/ssh/ssh_config`, which also governs other uses of that client, such as `git` over SSH. Where the SSH configuration that applies to a host has `StrictHostKeyChecking yes`, Claude Desktop doesn't ask the user to trust such a key, and `ssh` refuses the host if it can't verify the key. A key that differs from the one on record is handled the same way with or without this setting. A user can override the setting. By OpenSSH's own rules, `ssh` reads the user's `~/.ssh/config` before the system-wide file and keeps the first value it finds for a setting, so a `StrictHostKeyChecking` line in the user's file applies in place of your system-wide line. `ssh` also accepts a key that the user adds to their own `known_hosts` file, but under `yes` a connection from a terminal doesn't record the key. A user who picks a host that `ssh` refuses sees "Couldn't connect to" followed by the host, with [SSH host key verification failed](#ssh-host-key-verification-failed) under **View details**.
* With the built-in client, the host's key must already be in the device's `~/.ssh/known_hosts` as a plain entry. The app does not prompt to accept a new key and does not evaluate `@cert-authority` entries, so have users connect once from a terminal before adding the host in the app.
* With the built-in client, an identity file protected by a passphrase is skipped, not prompted for. Load it into the SSH agent, or use an unencrypted key. With the device's OpenSSH client, the app asks for the passphrase once the host's key is verified, and skips the key if the user cancels.
* With the built-in client, a host reached through a `ProxyCommand` gets the same host key check as a host reached directly. Before Claude Desktop 2.9939.0, the built-in client skipped host key verification for such a host.
* With the built-in client, a host connects with its key unchecked when its entry sets `StrictHostKeyChecking no`, sets `UserKnownHostsFile` to `none` or `/dev/null`, and sets no `RevokedHostKeys`. The app shows no password or one-time code prompt for such a host, so it needs a key or SSH agent sign-in.
* The connection times out after 30 seconds. A larger `ConnectTimeout` in the host entry extends it, and then applies to every try.
* With the device's OpenSSH client, a route through a jump host or a `ProxyCommand` gets more time where no `ConnectTimeout` applies. When a user starts a session at the device and the first try times out, the second try has 90 seconds. On macOS and Linux devices, the time that a sign-in dialog for a `ProxyJump` host is open doesn't count, unless the session's host [allows one session per connection](#hosts-that-allow-one-session-per-connection). A jump host's push approval or security key touch counts, and so does anything that a `ProxyCommand` waits for. If a connection still times out while the user types or approves, set a `ConnectTimeout` that leaves time for it. Reconnects that Claude Desktop starts on its own may have only 30 seconds a try, so a route that is always slow still needs `ConnectTimeout`. Before Claude Desktop 4.4212.0, the second try has 30 seconds, and the dialog's time counts. Before Claude Desktop 6.6395.0, every try has 30 seconds from a Windows device, and to a host that allows one session per connection.

With either client, the connection that carries the session leaves these settings off, whatever the entry says:

* **Forwarding**: `ForwardAgent`, `ForwardX11`, `Tunnel`, `LocalForward`, `RemoteForward`, and `DynamicForward`.
* **Kerberos delegation**: `GSSAPIDelegateCredentials`. The host doesn't receive the user's Kerberos ticket over this connection, even where the entry says `GSSAPIDelegateCredentials yes`. A `ProxyJump` host is reached by a separate `ssh`, which applies the jump host's own entry.
* **Commands**: `RemoteCommand` and `LocalCommand`.

Where the session's terminal can't use that connection, and always with the built-in client, the terminal runs its own `ssh`. In Claude Desktop 4.16336.0 or later, that `ssh` leaves all of the settings above off too. Before Claude Desktop 4.16336.0, it applies the entry's forwarding, Kerberos delegation, and `LocalCommand` settings, so with `ForwardAgent yes` in the entry it forwards the user's SSH agent to the host.

### Use the OpenSSH client of Git for Windows

To have Windows devices connect with an OpenSSH client that isn't Microsoft's, such as the `ssh.exe` of Git for Windows, name the client in [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath). Unless `sshClientPath` names another client, the OpenSSH client that makes the connection on a Windows device is Microsoft's. Placing another client first on the `PATH` never lets that client make the connection. Requires Claude Desktop 3.6556.1 or later.

Name another client only on devices with one user, not on devices that several users share.

The client that you name makes the connection only if all of these conditions hold:

* **Folder**: the program is an `.exe` file under Program Files or Program Files (x86). For a program under a user's `AppData\Local` folder, see [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user).
* **Links**: with every link and junction on the path followed, the program is still under Program Files or Program Files (x86), and Windows can resolve the path. Before Claude Desktop 4.4212.0, Claude Desktop checked only the path as written, so a client that a junction places outside Program Files stops connecting when the device updates.
* **Version**: the program is OpenSSH 8.5 or later. To check, run the program with `-V` in a Command Prompt window, for example `"C:\Program Files\Git\usr\bin\ssh.exe" -V`.
* **`sshClientPath` and `sshTransport`**: `sshClientPath` holds the program's absolute path, and [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) is `system-openssh`.
* **Source of both settings**: both values come from [machine policy](https://claude.com/docs/third-party/claude-desktop/mdm.md#4-deploy-the-configuration) under `HKLM\SOFTWARE\Policies\Claude`, or from the [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) that machine policy names. Values from a user's own configuration file or from `HKCU` don't count. Neither do values from an admin-console organization that a user's own sign-in points the device to.
* **Trial start**: in each run of Claude Desktop, before the first connection, Claude Desktop starts the program without connecting. The program must accept the arguments and options that Claude Desktop passes. The `ssh.exe` of a current Git for Windows accepts them.

Before you deliver `sshClientPath` and `sshTransport`, check for these devices:

* **Devices without the program**: with no file at the path that `sshClientPath` names, every SSH connection fails, whatever the value of `sshTransport`, and Claude Desktop's built-in SSH client doesn't take over. Install the program first, or deliver both settings only to devices that have it. A device that gets neither setting connects as before.
* **Devices with a bootstrap server**: once loaded, the server's response replaces machine policy's values, even for a setting that the response leaves out. A response that leaves `sshClientPath` out cancels your choice of client, and the app then uses Microsoft's OpenSSH or the built-in client. Return both settings in the response as well as in machine policy. Return `sshClientPath` only to Windows devices, because SSH connections fail on a macOS or Linux device that gets a Windows path.

If `sshTransport` is `system-openssh` and any other condition in the list doesn't hold, connections fail with the card "Ask your IT administrator to fix the configured SSH program". Claude Desktop never runs another `ssh` in the program's place.

With `system-openssh` and a client named in `sshClientPath`, Claude Desktop's built-in client tries the connection in one case only. In that case the program's file exists, but Windows won't start the program, or the program gives no answer when Claude Desktop starts it without connecting. That case ends as soon as the program has answered once since Claude Desktop opened.

To find the condition that doesn't hold, select **View details** on the card and read the line that starts with `Claude needs:`. `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the device names the condition too. The card says less in these cases:

* **The source of both settings is what fails**: the `Claude needs:` line names only Microsoft's OpenSSH, and the reason is in `ssh.log`.
* **The path names no file**: **View details** shows no `Claude needs:` line, and `ssh.log` says only that the program is missing or can't be run. Claude Desktop 4.16336.0 or later makes one exception, a path that runs through a user's `AppData\Local` folder, which gets such a line. Before Claude Desktop 4.16336.0, the card says as little for a path that isn't absolute or isn't an `.exe` file.

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

* **The line shows `%LOCALAPPDATA%`**: Claude Desktop rejected the value. In Claude Desktop 4.16336.0 or later, the `Claude needs:` line under it names the cause. Earlier versions show no such line, and the card says that the program is missing or can't be run, even if it is there. In `ssh.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the device, the last line with `sshClientPath begins with` names the cause too.
* **The line shows a path without the variable**: in the path, `~` stands for the user's profile folder. If no line under it starts with `Claude needs:`, the user has no `.exe` file at that path. A path in another account's folder, such as `C:\Windows\System32\config\systemprofile`, means that the tool that wrote the value expanded the variable.
* **A `Claude needs:` line that asks for `sshClientPath` to start with `%LOCALAPPDATA%\`**: the value is a full path without the variable, in the registry or in the bootstrap response. Requires Claude Desktop 4.16336.0 or later.
* **A `Claude needs:` line that asks for no junction or symbolic link leading out**: a link leads out of the user's `AppData\Local` folder. Requires Claude Desktop 4.16336.0 or later. Before Claude Desktop 4.16336.0, this case and the one before it get a line that asks for Program Files, if the file is there.
* **The `ssh:` line says that `sshClientPath` is set, but could not be read**: the `Claude needs:` line under it gives the cause. It asks for a plain string (`REG_SZ`) where the registry value is an expandable string, which Claude Desktop doesn't read. It asks for a full local path where the value has a mistake, such as `..` or a second `%`. Requires Claude Desktop 4.16336.0 or later.
* **The `ssh:` line says that `sshClientPath` isn't a local absolute path**: the device runs a version before Claude Desktop 4.16336.0, which shows no `Claude needs:` line here. The causes are the same two. Before Claude Desktop 4.4212.0, every value that starts with `%LOCALAPPDATA%\` gets this line too.

With a per-user client, plan for the SSH files, prompts, and sign-ins that [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) describes, and for the following:

* **Application control**: allow the client and the `ssh-keygen.exe` beside the client in your application control policy. If your policy blocks the client, the built-in client tries the connection, and `ssh.log` says that the program gave no answer. If your policy blocks that `ssh-keygen.exe` too, the connection fails with the card "Ask your IT administrator to fix the configured SSH program".
* **Upgrades**: if the name of the client's folder contains a version number, change the value in machine policy and in the bootstrap response together with each upgrade. Prefer a folder name without a version to a junction, because through a junction Claude Desktop can stop reusing saved SSH passwords.
* **Moved or mounted profiles**: Claude Desktop looks in `AppData\Local` under the user's profile folder, even where the `LOCALAPPDATA` variable points elsewhere. It refuses a profile folder that is a UNC path, such as `\\server\profiles\user`. Where Windows mounts the profile from a profile container, test one device before you deliver the value to the others.
* **A changed or removed value**: a running Claude Desktop can keep using the client after you change or remove the value. Have users quit and reopen Claude Desktop.

## Troubleshoot

### Your organization doesn't allow this SSH connection

The `sshHostAllowlist` in effect on this device is unset, empty, or has no entry that matches the host or a jump host on the way to it. The card's details say which. The name that must match is the `HostName` that the device's `~/.ssh/config` resolves the entered host to, so an entry that lists only an alias doesn't allow the host. To find which configuration source supplies the key on a device, see [Interaction with Claude Code managed settings on the device](#interaction-with-claude-code-managed-settings-on-the-device). For a device that moved to an admin console organization, see [Devices that move to an admin console organization](#devices-that-move-to-an-admin-console-organization). The connection test, and the "Couldn't connect to" card on the New session page, report the same denial as "Your organization's settings do not allow this connection." Before Claude Desktop 2.31226.0, the card's title was "SSH isn't allowed by your organization".

For a jump host, read the warning under [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist), then add the first name in the details to the allowlist. That name is the jump host's `HostName`, and the second name is the host that the user entered.

```text theme={null}
SSH host "bastion.corp.example.com" is not allowed by your organization's managed settings. It is a jump host on the way to "build01".
```

If the next attempt names another jump host, add that one too. To find every name beforehand, see [Jump hosts and the allowlist](#jump-hosts-and-the-allowlist). Requires Claude Desktop 3.1623.0 or later.

### SSH to this device isn't available

The host resolves to the device itself (`localhost`, `127.0.0.1`, or a tunnel or port forward that ends on the device) while `allowedWorkspaceFolders` restricts workspace folders. A session over SSH to the device reaches the same disk the policy restricts, so it is refused. Connect to a different host, or use a local session unless `disableDesktopLocalSessions` turns those off. Before Claude Desktop 2.31226.0, the card's title was "SSH to this machine isn't available".

### SSH sessions can't use your model provider settings

The configured inference credential is one of the kinds listed as refused under [Inference credentials on the remote host](#inference-credentials-on-the-remote-host), or the inference endpoint is on the device itself. The card's details say which. Switch the deployment to a credential kind that works on a remote host, or point the app at an endpoint the host can reach. For a named profile that is refused, see what [Amazon Bedrock with a named profile](#amazon-bedrock-with-a-named-profile) needs. Before Claude Desktop 2.31226.0, the card's title was "Remote sessions aren't available with this inference setup".

### Couldn't start Claude Code: No AWS config found

The card's title is `Couldn't start Claude Code on <host>`, and its details start with `No AWS config found`. The deployment uses [Amazon Bedrock with a named profile](#amazon-bedrock-with-a-named-profile), and the host has neither a `config` nor a `credentials` file in the folder that holds the AWS files, or Claude Desktop can't see them there. The details name the folder and the profile. Add the profile on the host, or make the files readable for the user's account, then have the user try again. If the host should start Claude Code through a launcher, check that the host names one: with `claudeCodeProcessWrapperEnabled` on, the details say that none was found. These details require Claude Desktop 7.37095.0 or later.

### Claude Code couldn't sign in to AWS

The card's title is `Claude Code on <host> couldn't sign in to AWS`. The host has the AWS files, but Claude Code couldn't get working credentials from the profile, or AWS refused the request, for example because the profile lacks permission for Amazon Bedrock. The card's details show what the host reported. In a terminal on the host, check that the profile exists under the name in `inferenceBedrockProfile` and has that permission, and sign in again. Then have the user select **Try again**. This card requires Claude Desktop 7.37095.0 or later.

### This session needs your organization's launcher

A launcher started this session, or the session that it was made from, and now the host names no launcher or `claudeCodeProcessWrapperEnabled` is off. Claude Desktop shows this card only if a new session can use [the host's own AWS profile](#amazon-bedrock-with-a-named-profile). The user can select **New session**, and the new session signs in with the host's own AWS profile, if the host has one. To continue the old session, name the launcher on the host again and turn `claudeCodeProcessWrapperEnabled` on.

This card requires Claude Desktop 7.37095.0 or later.

### SSH host key verification failed

The host's key has changed, or it is not in the device's `~/.ssh/known_hosts` and was not trusted in the app (the built-in client never asks). Connect to the host from a terminal on the device to check and record the current key, then retry.

With the built-in client, the connection test reports this failure as "Host key changed or not trusted". With that client, connections also fail at the host key check when the app can't run `ssh-keygen`, even when the host's key is in `known_hosts`. The built-in client looks up the host's key with `ssh-keygen`, which it looks for first in the folder of the program that [`sshClientPath`](https://claude.com/docs/third-party/claude-desktop/configuration#sshclientpath) names, then on the user's `PATH`.

* **A blocked `ssh-keygen`**: where the device refuses to start the `ssh-keygen` of its OpenSSH client, for example under an application control policy, allow that `ssh-keygen` to run. Where a Windows or Linux device refuses to start the `ssh-keygen` beside the program that `sshClientPath` names, the connection fails with the card [Ask your IT administrator to fix the configured SSH program](#ask-your-it-administrator-to-fix-the-configured-ssh-program) instead of this failure. The connection test then reports "The SSH program your organization configured can't be used".
* **A Windows device with no `sshClientPath` and no `ssh-keygen.exe` on the user's `PATH`**: if the device also has no usable OpenSSH client, such as Microsoft's, the app uses the built-in client for every connection, whatever `sshTransport` says. Claude Desktop 6.6395.0 or later then runs the `ssh-keygen.exe` that Git for Windows installs in `Program Files\Git\usr\bin`. If Claude Desktop finds none or can't run it, the user sees this failure or one of the cards listed under [Ask your IT administrator to set sshTransport to system-openssh](#ask-your-it-administrator-to-set-sshtransport-to-system-openssh). Where the user sees one of those cards, the connection test reports "Host key can't be checked". Before Claude Desktop 6.6395.0, the user sees this failure whether or not the device has Git for Windows.

To check a Windows device on which connections fail, look for `ssh-keygen.exe` beside the program that `sshClientPath` names, if you set it. Then open a new Command Prompt or PowerShell window as the user who runs Claude Desktop, and run `where.exe ssh-keygen`. If neither place has `ssh-keygen.exe`, apply one of these fixes, then quit and reopen Claude Desktop:

* **Install Microsoft's OpenSSH client**: install Win32-OpenSSH 9.4 or later, then run `where.exe ssh-keygen` again to confirm that it is on the user's `PATH`. From that version, the client can also carry the connection (see [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client)).
* **Until you can install Win32-OpenSSH 9.4 or later, use another OpenSSH build**: in the configuration that the affected Windows devices receive, set `sshClientPath` to the absolute path of an `ssh.exe` that has `ssh-keygen.exe` in the same folder, such as the one in Git for Windows. On a device where that path doesn't exist, SSH connections fail. Name another client only on devices with one user, not on devices that several users share. With `sshTransport` set to `system-openssh`, that `ssh.exe` also carries the connection, and it has to meet the conditions in [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows).

With the device's OpenSSH client, if `StrictHostKeyChecking yes` applies to the host, connecting from a terminal doesn't record its key. Instead, check the key and add it to the system-wide `known_hosts` file, or give the host a certificate from your host certificate authority (see [SSH configuration on the device](#ssh-configuration-on-the-device)).

### Ask your IT administrator to set sshTransport to system-openssh

The built-in client made the connection, and the host needs the device's OpenSSH client. Where the app can name a step, the card's title gives it, and the card's text gives the cause, such as "Claude's built-in SSH library can't connect through a jump host (ProxyJump)."

* **"Ask your IT administrator to set sshTransport to system-openssh"**: the built-in client is the device's default, and the device has a usable OpenSSH client. Set [`sshTransport`](https://claude.com/docs/third-party/claude-desktop/configuration#sshtransport) to `system-openssh`. Claude Desktop 4.16336.0 or later doesn't show this title: the OpenSSH client makes the connection instead.
* **"Ask your IT administrator to change sshTransport from builtin to system-openssh"**: your configuration sets `sshTransport` to `builtin`. Change it to `system-openssh`.
* **"Ask your admin to correct the sshTransport setting"**: the app can't read the value that your configuration gives `sshTransport`, for example a misspelling, so the built-in client makes the connection. Correct the value. Requires Claude Desktop 2.37337.0 or later.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer and set sshTransport to system-openssh, then quit and reopen Claude"**: the built-in client is the device's default, and the app found no usable OpenSSH client on the device. Install the client, and set the key. Claude Desktop 4.16336.0 or later shows the next title instead.
* **"Ask your IT administrator to install Microsoft OpenSSH 9.4 or newer, then quit and reopen Claude"**: the app found no usable OpenSSH client on the device. Install the client. Before Claude Desktop 4.16336.0, this title appears only where `sshTransport` is `system-openssh`.
* **"Check your network or VPN and try again, or quit and reopen Claude"**: the device's configuration from the Enterprise Admin Console or a bootstrap server hasn't loaded, so the built-in client made the connection. Requires Claude Desktop 4.16336.0 or later.
* **"Quit and reopen Claude; if this comes back, ask your IT administrator to let Claude use the system OpenSSH client"**: the device couldn't start the OpenSSH client earlier in this run of the app (see [Host requirements](#host-requirements)).

Where the app can name no step, the card's title gives the cause, such as `<host> needs a jump host, which Claude can't use here` or `Claude can't check <host>'s key here`.

These cards require Claude Desktop 2.31226.0 or later. Before Claude Desktop 2.31226.0, the built-in client refused a `ProxyJump` host with a message that suggests `ProxyCommand`.

### Ask your IT administrator to fix the configured SSH program

The program that `sshClientPath` names is missing, can't be run, is too old, or on Windows doesn't meet the conditions for its kind. Claude Desktop never runs another `ssh` in its place. Select **View details** on the card for the program's path. On a Windows device, to find the condition, see [Use the OpenSSH client of Git for Windows](#use-the-openssh-client-of-git-for-windows) or [Use an OpenSSH client installed per user](#use-an-openssh-client-installed-per-user). With no `sshClientPath`, the card appears on a macOS or Linux device where `sshTransport` is `system-openssh` and the device can't start its own `ssh`. A Windows device in that state uses the built-in client. Where the built-in client makes the connection, the card also appears if a Windows or Linux device refuses to start the `ssh-keygen` in the folder of the program that `sshClientPath` names, for example under an application control policy. **View details** then shows a line that starts with `ssh-keygen:` and gives the blocked program's path. Allow that program to run, then have the user try again.

### This computer won't start Claude's SSH sign-in helper

Where the device's OpenSSH client makes the connection, the operating system refused to start one of the helper programs that show `ssh`'s prompts. Without them the app can't ask for a password, a one-time code, or a key passphrase, so a sign-in that needs one fails. Select **View details** on the card for the blocked program's path and, where the operating system gave one, the error code. Allow the program:

* **Windows devices**, with Claude Desktop 2.37337.0 or later: allow the helper programs as described under [Prepare Windows devices for the OpenSSH client](#prepare-windows-devices-for-the-openssh-client), then have the user try again. With Claude Desktop 4.16336.0 or later and `sshTransport` unset or `auto`, the [built-in client connects instead](#prepare-windows-devices-for-the-openssh-client) where the app itself can't start the helper. The host then stays on that client.
* **macOS and Linux devices**, with Claude Desktop 4.16336.0 or later: allow `claude-ssh-askpass` in the folder that **View details** names, then have the user try again. On these devices the built-in client never connects instead. With `spawn EACCES` on a Linux device, check too that the folder isn't mounted `noexec`.

While the fault lasts, Claude Desktop can't reconnect by itself with a saved password. It shows the card only while a user waits for the connection, for example after they start a session or send a message. On a Windows device, the card appears only for a host that accepts a password or a one-time code.

### Claude's SSH sign-in helper isn't working on this computer

On a macOS or Linux device, `claude-ssh-askpass` is missing or doesn't work, though the operating system didn't refuse to start it. Without it the app can't ask for a password, a one-time code, or a key passphrase, so a sign-in that needs one fails. Select **View details** and match the line that starts with `What failed:`:

* **`it is missing`**: reinstall Claude Desktop, then have the user try again.
* **`its test run failed`, `its test run timed out`, `its test run sent no answer`, or `its test run could not be started`**: have the user try again. If the card comes back, have them quit and reopen Claude Desktop. An update that was installed while the app was running can make that necessary. If it still comes back, reinstall the app.
* **`ssh seems unable to start it, though Claude can`**: allow `ssh` to start the helper in your application control policy. Have the user wait until then, because each try can send the host empty passwords, which can count toward an account lockout.
* **`it cannot reach Claude because ssh's stderr is redirected, for example by a wrapper script`**: look for a wrapper around `ssh`. Change the program that `sshClientPath` names, or the `ssh` first on the user's `PATH`, so that it leaves standard error untouched.

While the fault lasts, Claude Desktop can't reconnect by itself with a saved password. It shows the card only while a user waits for the connection, for example after they start a session or send a message. Requires Claude Desktop 4.16336.0 or later.

### This computer's ssh refuses a backslash or dollar sign in user names

On a macOS or Linux device where the device's OpenSSH client makes the connection, that client refuses the user name on its command line because the name has a `\` or a `$`, as in `DOMAIN\user`. Claude Desktop passes such a name to `ssh` in a configuration file that it writes, and shows this card where it can't. Select **View details** on the card and match the last line:

* **`needs the Include line in this file to use a full path`**: the system's `ssh_config`, or a file read through it, has an `Include` with a relative path. The line names the file. Write that path in full, starting with `/`.
* **`couldn't find which system ssh_config this ssh reads` or `couldn't write that file`**: have the user try again. With the second, the app couldn't write the file in a private temporary folder.
* **`the name is the jump host's`**: the card's title is "This computer's ssh refuses the jump host's user name". In the user's `~/.ssh/config`, move the name from `ProxyJump` to a `User` line in the jump host's own `Host` block.

This card requires Claude Desktop 2.37337.0 or later.

### A required sandbox isn't available

Claude Code on the host requires a sandbox that isn't available there, so it exits as it starts. The requirement comes from [`sshHostSandboxUnavailable`](#refuse-sessions-on-a-host-without-a-working-sandbox) set to `refuse` in your configuration, or from `sandbox.failIfUnavailable` in Claude Code settings on the host, in server-managed settings or a gateway's `code` settings, or in what a policy helper returns.

The card's details give Claude Code's reason, such as `dependencies are missing`. They can end with Claude Code's own hint, `Set sandbox.failIfUnavailable=false to allow unsandboxed execution`. Don't follow that hint: it switches the requirement off. Where the reason names missing dependencies on a Linux host, install the [sandbox dependencies](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) with the distribution's package manager, then have the user send a message in the session. Claude Code reports no sandbox on a Windows host, so use a macOS or Linux host.

### Setup on the host fails after SSH connects

SSH connected, but Claude Desktop couldn't place or start the remote server or the engine on the host. Select **View details** on the failure card to read the app's own message, which can end with a code in square brackets. Match the code, or the start of the message:

* **`[SFTP_UNAVAILABLE]`**: the host's SSH server refused the SFTP subsystem. Enable `Subsystem sftp` in the server's `sshd_config`, or see what a session needs under [Hosts without SFTP](#hosts-without-sftp).
* **`[SESSION_LIMIT]`**: the host's SSH server refused to open another session on the connection. If the host has to keep its `MaxSessions` limit, the device's OpenSSH client has to make the connection. See [Hosts that allow one session per connection](#hosts-that-allow-one-session-per-connection) for the version and the setting that each platform needs. Otherwise, raise `MaxSessions` in the server's `sshd_config`, for example to OpenSSH's default of 10, and reload the SSH server.
* **`[SFTP_NOT_STARTED]`**: the host's SSH server accepted the request for SFTP, but the SFTP server ended before its first answer, or text arrived in place of that answer. In a terminal on the device, run `sftp` with the same host, for example `sftp user@build01.corp.example.com`, to see what stops it. Then check the settings and files that the message names, or see what a session needs under [Hosts without SFTP](#hosts-without-sftp).
* **`[EXEC_NO_INPUT]`**: the host's SSH server ran the app's command but passed it no input, which setup and the session's own link need. In a terminal on the device, run `echo hi | ssh` with the same host and `cat`, for example `echo hi | ssh user@build01.corp.example.com cat`. It prints `hi` on a host that passes input. Have the host's administrator let commands run over SSH receive input.
* **`[ENOSPC]` or `[EDQUOT]`**: a disk is full, or a quota is used up. In a message that starts with `Couldn't prepare the deploy locally`, the disk is the device's. In any other message it is the host's, so free space in the SSH user's home directory. [Host requirements](#host-requirements) gives the space the app needs.
* **`Unsupported remote platform`**: the host's operating system or processor isn't among those under [Host requirements](#host-requirements).
* **`[CLI_NOT_RUNNABLE]`**: the remote server installed the engine, but the engine's first run didn't start or didn't exit cleanly, so the remote server removed it. One cause is a glibc older than 2.17. Run `ldd --version` on the host to check. Before Claude Desktop 2.37337.0, the message has no code and starts with `Couldn't install the Claude CLI on the remote (cli archive)`.
* **`[NO_INSTALL_RESULT]`**: the remote server's install step printed no result. A home directory mounted `noexec` is one cause, where the host's error message doesn't say `Permission denied` or `Operation not permitted`. Where it does, the code is `[SERVER_NOT_RUNNABLE]`. Before Claude Desktop 4.4212.0, a host with SFTP gets `[NO_INSTALL_RESULT]` in both cases.
* **`[SETUP_DIR_NOEXEC]`**: on a [host without SFTP](#hosts-without-sftp), the host didn't run a test program from `~/.claude/remote` in the SSH user's home directory, so the app didn't copy the remote server. A home directory mounted `noexec` and a restricted login shell are two causes. Have the host's administrator let the SSH user run programs from `~/.claude/remote`.
* **`[SERVER_NOT_RUNNABLE]`**: the remote server didn't run from `~/.claude/remote` in the SSH user's home directory, or stopped before it answered. A home directory mounted `noexec` is one cause, and security software on the host that keeps programs from running there is another. Have the host's administrator check that programs can run from that folder. Before Claude Desktop 4.4212.0, the code appears only on a [host without SFTP](#hosts-without-sftp).
* **`[DOWNLOAD_BUSY]`**: Anthropic's download server answered that it is busy, so Claude Desktop couldn't download the engine or the remote server to the device. Claude Desktop has already waited and asked again. Have the user try again in a few minutes. If the code keeps coming back, check whether a proxy on the device's network limits downloads from `downloads.claude.ai`, because a proxy can give the same answer.
* **`[DOWNLOAD_FAILED]`, or `Couldn't prepare the deploy locally` with a network code such as `[ETIMEDOUT]`**: the device couldn't download one of the programs that it puts on the host. In the message, `(server binary)` stands for the remote server and `(cli archive)` for the engine. Have the user check the device's internet connection. If your network blocks `downloads.claude.ai`, allow it. If you can't, and your SSH hosts run Linux on x64 or arm64, install Claude Desktop with the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#ssh-remote-sessions-with-the-offline-installer), which bundles the remote server and the engine for those hosts.
* **`[DOWNLOAD_GOT_WEB_PAGE]`**: a web page came back in place of the download. If the device's network has a sign-in page, have the user sign in. If a proxy answers `downloads.claude.ai` with a block page, allow that address or use the offline installer, as for `[DOWNLOAD_FAILED]`.

`[SESSION_LIMIT]` and `[SFTP_NOT_STARTED]` require Claude Desktop 2.31226.0 or later. `[SFTP_NOT_STARTED]` appears only when the device's OpenSSH client makes the connection. Their cards are titled `<host> allows too few SSH sessions per connection` and `SFTP doesn't start on <host>`.

In Claude Desktop 4.16336.0 or later, `[SESSION_LIMIT]` also appears where the built-in client makes the connection, on a device of any platform. Before Claude Desktop 4.16336.0, it appears only on macOS and Linux devices, and only when the device's OpenSSH client makes the connection.

`[CLI_NOT_RUNNABLE]` and `[EXEC_NO_INPUT]` require Claude Desktop 2.37337.0 or later. `[EXEC_NO_INPUT]` appears only where the device's OpenSSH client makes the connection. Their cards are titled `Claude Code didn't run on <host>` and `Ask <host>'s administrator to let SSH commands receive input`. From the same version, the card is titled `Couldn't copy Claude Code to <host>` where the app couldn't put its files on the host, and `Couldn't install Claude Code on <host>` where the engine's install failed, each for a cause with no card of its own.

Before Claude Desktop 4.29.0, the `[EXEC_NO_INPUT]` card is titled `<host> doesn't pass input to commands run over SSH`.

`[SETUP_DIR_NOEXEC]` and `[SERVER_NOT_RUNNABLE]` require Claude Desktop 3.1623.0 or later. Their card is titled `Ask <host>'s administrator to let Claude's server run`.

`[DOWNLOAD_BUSY]` requires Claude Desktop 4.4212.0 or later, and its card is titled `Try again in a few minutes`. Before Claude Desktop 4.4212.0, the card for `[SETUP_DIR_NOEXEC]` and `[SERVER_NOT_RUNNABLE]` is titled `Claude's server didn't run on <host>`.

`[DOWNLOAD_GOT_WEB_PAGE]` requires Claude Desktop 4.16336.0 or later, and its card is titled `Sign in to your network, or ask IT to allow the download`. From the same version, the `[DOWNLOAD_FAILED]` card is titled `Check your internet connection, or ask IT to allow the download`.

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

### Resume is missing or fails on an SSH host

Find what the user sees, on the screen or under **View details** on an error card, when they try to [resume a session that is saved on the host](#resume-a-session-that-is-saved-on-the-host):

| What the user sees | Cause | What to do |
| - | - | - |
| `/resume` is missing from the slash menu of a new SSH session. A user who types it anyway sees, for example, `Terminal sessions can only be resumed in a Local environment.` | The feature is off on this device. Its Claude Desktop version is from before the feature, or it isn't set up to send requests straight to Amazon Bedrock | Update Claude Desktop to the [version that `/resume` requires](#resume-a-session-that-is-saved-on-the-host). Then check the first condition under [Where resuming a saved session is available](#where-resuming-a-saved-session-is-available). On a device that doesn't meet it, users can run `claude --resume` in a terminal on the host |
| `/resume` is missing in an SSH session that has already started | Claude Desktop offers it in a new session, before the first message | Have the user start a new session on the host |
| `Your organization's settings don't allow resuming sessions from this host or folder.` | `sshHostAllowlist` refuses the host, `allowedWorkspaceFolders` refuses the folder, or the credential kind doesn't [work on a remote host](#inference-credentials-on-the-remote-host) | Change the key or the credential kind, or have the user pick a folder inside the list |
| `Sessions on this host can't be listed.` | The host doesn't qualify. Check first whether its managed settings lack both `"merge"` and an `allowedProviders` list. Other causes include a Windows host, a launcher that locates Claude Code itself or sets another provider, and a wider `allowedProviders` list on the host | See [Where resuming a saved session is available](#where-resuming-a-saved-session-is-available). To tell the causes apart, see [Find why resume refuses a host](#find-why-resume-refuses-a-host) |
| `Couldn't load sessions from the host.` | The connection to the host isn't up, or the host gave no usable answer. For example, a launcher was too slow to answer | Have the user select **Try again**. If the message returns and you have a launcher, see [Resume through a corporate launcher](#resume-through-a-corporate-launcher). To tell the causes apart, see [Find why resume refuses a host](#find-why-resume-refuses-a-host) |
| `Some sessions aren't listed.`, under the list or alone | The folder holds more session files than Claude Desktop goes through for one list, or some of them are too large (over 64 MiB) or too slow to check, or hold another provider's reply. The message appears alone if nothing is left to list | Have the user resume the session in a terminal on the host |
| `Couldn't resume that session.` | No reason is shown. For example, a key refuses the selection, the file is gone, or the host or the session no longer passes the checks | See [Where resuming a saved session is available](#where-resuming-a-saved-session-is-available) |
| `The host says that another user owns or can change that session's file` | For example, `sudo claude` wrote the file as root, or its mode is `0664` | Check the owner and mode of the session's file, under `~/.claude/projects` on the host |
| `Claude Code on <host> has no working credentials` | At the first message, Claude Code on the host got no working credential for Amazon Bedrock. For example, a company sign-in behind the launcher's credential has lapsed | Have the user sign in again on the host, then select **Try again** |
| `A resumed session can only use Amazon Bedrock's own address, and Claude Code was started with another address or provider.`, at a resumed session's first message. Before Claude Desktop 7.37095.0, the card is titled `Your organization doesn't allow this API key or provider` | The launcher points Amazon Bedrock requests at a proxy or gateway address. The same happens where `AWS_ENDPOINT_URL`, `AWS_ENDPOINT_URL_BEDROCK`, or `AWS_ENDPOINT_URL_BEDROCK_RUNTIME`, in the SSH user's environment on the host, names an address that isn't an Amazon Bedrock endpoint. If a new session fails too, an `allowedProviders` list in the host's managed settings lacks the provider in use | Have the launcher send resumed sessions to Amazon Bedrock's own address, or unset the variable. See [Resume through a corporate launcher](#resume-through-a-corporate-launcher). Otherwise, have the user start a new session, or resume this one in a terminal on the host. Don't widen `allowedProviders` on the host, unless a new session fails too. In that case, add the provider in use to the list, and no provider other than `bedrock` and `mantle` |
| `This session's file or folder on the host is missing or didn't pass a safety check.`, with `Claude Code wasn't started, because this session's file on the host couldn't be checked, can be changed by another user, or holds a command that would run by itself.` under **View details** | At the first message, Claude Desktop checks the session's files again, and refuses one that records a deferred tool call. It also refuses the start if the folder that the session ran in is gone, or the SSH user can't enter it. Before Claude Desktop 7.37095.0, no answer from the host to this check gives the text under **View details** too | Check that the folder that the session ran in exists on the host, and that the SSH user can enter it. Then check that the session's file exists, and its owner and mode, under `~/.claude/projects` |
| `This session can only continue on Amazon Bedrock, and that isn't possible here right now.`, with `Claude Code wasn't started, because this session can only continue on Amazon Bedrock.` under **View details** | The device, the host, or the session file no longer passes the checks | See [Where resuming a saved session is available](#where-resuming-a-saved-session-is-available) |
| `A check on the host didn't finish.`, with `Claude Code wasn't started, because a check on the host didn't finish.` under **View details** | Claude Code on the host, or the host itself, gave no usable answer | Have the user try again. If the message returns and you have a launcher, see [Resume through a corporate launcher](#resume-through-a-corporate-launcher) |

The cards in the last four rows are titled `Couldn't start Claude Code on <host>`. Before Claude Desktop 7.37095.0, a card with `Claude Code wasn't started, because` under **View details** is titled `Something went wrong`, and only that text says why. A later version can still show `Something went wrong`, for example after Claude Desktop restarts. Have the user try again to see the reason.

If the list is empty (`No Claude Code sessions found in this folder on the host.`) or lacks a session, check for these causes:

* **This Claude Desktop already has the session for this host**, in the sidebar or archived
* **The folder has many newer session files**: Claude Desktop takes the folder's 200 newest session files, skips the sessions that it already has for this host, and goes through the rest from the newest. It stops once it has 30 sessions that began in a terminal, or at 60 files, or sooner on a slow host. The user then sees `Some sessions aren't listed.`, under the list or alone. Have the user resume such a session in a terminal on the host. Before Claude Desktop 7.37095.0, it goes through the 30 newest files, and the sessions that it already has count among them.
* **The session was saved for another folder**, a subfolder included: the list uses the real path of the folder that the user picked, and includes that folder's Claude Code worktrees
* **A program started the session**: for example, `claude -p`

#### Find why resume refuses a host

To learn why a host doesn't qualify, open `main.log` in the device's [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives). Find the newest line that contains `[SSH] Whether Claude Code on <host> goes to Amazon Bedrock and is held to it:`. Claude Desktop writes such a line each time it asks Claude Code on a connected Linux or macOS host which provider it uses. The line's last word gives the result:

| The line ends in | What it means |
| - | - |
| `bound` | The host qualifies |
| `other_provider` | Claude Code on the host, started through the launcher if there is one, names a provider other than Amazon Bedrock |
| `no_list_in_force` | No provider list is in force on the host: its managed settings lack both `"parentSettingsBehavior": "merge"` and an `allowedProviders` list, or a launcher doesn't pass on every option |
| `wider_list_in_force` | The `allowedProviders` list in the host's managed settings holds more than `bedrock` and `mantle` |
| `launcher_file` | The host has a launcher that locates Claude Code itself |
| `credential_stays_here` | The credential kind doesn't [work on a remote host](#inference-credentials-on-the-remote-host), and the host's managed settings name no launcher |
| `timed_out`, `silence` | The host or the launcher took too long to answer |
| `run_failed`, `not_json`, `too_much` | `claude auth status --json` exited with an error, or printed something other than its answer |
| `launcher_not_told` | The host's managed settings can't be read, the launcher that they name can't be used, or the host gave no answer about it |
| `lost`, `no_claude_code`, `launcher_file_not_told` | The connection dropped, or the host didn't say yet which Claude Code or launcher it has. Have the user try again |

## Related

* [Code in Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/code.md)
* [`sshHostAllowlist` in the configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist)
* [Desktop and filesystem access](https://claude.com/docs/third-party/claude-desktop/local-access.md)
