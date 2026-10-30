> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User identity and local data

> How Claude Desktop on 3P identifies users and where it stores conversations, settings, and credentials on disk

Claude Desktop on third-party (3P) keeps conversations, settings, and credentials on the device. For [SSH remote sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md), the remote host also stores their conversations and receives your inference credential. When the configuration comes from MDM, a local file, or a bootstrap server, users have no Anthropic account and never sign in to Anthropic, and Anthropic holds no per-user state. When your organization manages the app from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), users sign in with a Claude account to receive their settings, and [Where your data goes](https://claude.com/docs/third-party/claude-desktop/admin-console.md#where-your-data-goes) lists what Anthropic stores in that case.

## Identity

When the app first launches in 3P mode, it generates a random UUID and writes it (base64-encoded) to the `ant-did` file in the application-data directory. When the configuration comes from MDM, a local file, or a bootstrap server, this identifier and the `deploymentOrganizationUuid` from your managed configuration are what's attached to telemetry events. The identifier is random per device and per OS-user account, and Anthropic cannot trace it back to a real device or person. In an organization managed from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), users sign in with a Claude account, so the app is not anonymous to Anthropic there, and [Where your data goes](https://claude.com/docs/third-party/claude-desktop/admin-console.md#where-your-data-goes) describes what Anthropic stores in that case.

The OpenTelemetry export to your own collector is the exception: it identifies the user directly. Each exported record carries an `enduser.id` resource attribute with the user's identity and a `process.owner` attribute with the operating-system login name, so attributing activity to named users needs no collector-side correlation. See [User attribution](https://claude.com/docs/third-party/claude-desktop/telemetry.md#user-attribution) for where the identity comes from and the `endUserAttribution` key that controls it.

## Where data lives

Claude Desktop on 3P stores everything under a dedicated directory, separate from standard Claude Desktop, so the two modes can coexist on one machine without interfering.

| Platform | Application data | Logs |
| - | - | - |
| macOS | `~/Library/Application Support/Claude-3p/` | `~/Library/Logs/Claude-3p/` |
| Windows | `%LOCALAPPDATA%\Claude-3p\` | (under the application-data directory) |
| Linux | `~/.config/Claude-3p/` | (under the application-data directory) |

> [!NOTE]
>
> On Windows, earlier Claude Desktop releases stored this data under `%APPDATA%\Claude-3p\` (the Roaming profile). On first launch after upgrading, the app moves the existing directory to `%LOCALAPPDATA%` automatically; if Roaming is redirected to a network share, conversation history and configuration are copied and large regenerable caches are re-downloaded. Update any external tooling, backup jobs, or endpoint policies that reference the old path. macOS paths are unchanged.

Within the application-data directory:

| Path | Contents |
| - | - |
| `ant-did` | The random device identifier described above. |
| `configLibrary/` | Locally authored configuration (from the in-app configuration window). `_meta.json` records which saved configuration is applied; each is a `<id>.json` file alongside it. API keys in these files are encrypted (see [Credentials](#credentials)). Ignored when a managed profile is present. |
| `local-agent-mode-sessions/.../cowork_account_settings.json` | User-level preferences set in the app, such as locale, the memory toggle, and the text entered under **Instructions for Claude** and **Global instructions**. |
| `local-agent-mode-sessions/` | Cowork and Chat conversation history. One `local_<uuid>.json` file plus a working directory per session, scoped by the `ant-did` device identifier and the organization ID, not by who is signed in to the app. The working directory includes an `uploads/` subdirectory with copies of files attached to the conversation and an `outputs/` subdirectory for files Claude creates. |
| `local-agent-mode-sessions/.../memory/` | Cowork memory: a `CLAUDE.md` instructions file plus a `memory/` subdirectory of Markdown notes Claude writes about the user's preferences, projects, and feedback. See [Memory](#memory). |
| `local-agent-mode-sessions/.../spaces/<projectId>/memory/` | Markdown memory notes for one project, used by Cowork sessions and Chat conversations inside that project. See [Memory](#memory). |
| `local-agent-mode-sessions/.../<sessionId>/audit.jsonl` | Append-only log of session events (tool invocations, permission decisions, file operations). Each entry is HMAC-chained to the previous one so edits or deletions are detectable; the companion `.audit-key` file holds the per-session signing key, encrypted via the OS keychain. |
| `claude-code-sessions/` | Code session records holding each session's working folder, settings, title, and sometimes a short summary. The conversation transcripts themselves are in Claude Code's own store at `~/.claude/projects/`, outside this directory. |
| `claude-code/`, `claude-code-vm/` | Claude Code binary and VM workspace data for Code sessions. |
| `vm_bundles/` | Cached copy of the VM workspace bundle that Cowork sessions run in, plus the data disk the app creates to hold those sessions' home directories inside the VM. |
| `cowork_plugins/` | User-installed and [org-provisioned](https://claude.com/docs/third-party/claude-desktop/extensions.md#organization-plugins-admin) plugins. Created on first plugin install. |
| `IndexedDB/`, `Local Storage/`, `Session Storage/` | Renderer-side UI state (window layout, recent folders, preferences). |

Files in this directory are written with owner-only permissions so other OS accounts on the same machine cannot read them. The app encrypts stored sign-in tokens, API keys saved from the in-app configuration window, and similar secrets with the operating system's secure storage (see [Credentials](#credentials)). It doesn't encrypt conversations, settings, or the rest of the locally applied configuration. Protection at rest for those files depends on the device's full-disk encryption, such as FileVault or BitLocker.

The logs directory contains `main.log` (application and configuration-validation events), `cowork_vm_node.log` (sandbox VM activity), `claude.ai-web.log` (renderer events), and `mcp.log` / `mcp-server-<name>.log` (MCP connection events).

Separately from the application-data directory, Claude Desktop writes user-visible outputs (Artifacts and scheduled-task results) to `~/Claude/` in your home directory, or `~/Documents/Claude/` on legacy installs. This folder is intended for you to browse directly and is not removed when you delete the application-data directory. To back up a user's data, copy every location listed under [Copy the data to the new device](#copy-the-data-to-the-new-device).

## Memory

During Cowork sessions, Claude writes short Markdown files recording what it has learned about the user — working preferences, project context, and corrections — and reads them at the start of subsequent sessions. These files live under `local-agent-mode-sessions/.../memory/memory/` and never leave the device.

Users can review and delete individual entries, or pause memory for new sessions and conversations (existing files are kept but not read or updated), under **Settings → Cowork → Memory**. The same page exposes a **Global instructions** editor for the `CLAUDE.md` file that is included in every session.

Each [project](https://claude.com/docs/cowork/guide/projects.md) also keeps its own memory under `local-agent-mode-sessions/.../spaces/<projectId>/memory/`. Cowork sessions inside a project read and update the project's memory rather than the files under `local-agent-mode-sessions/.../memory/memory/`. A Chat conversation inside a project can also read and update the project's memory, as described under [Chat conversations](#chat-conversations).

## Chat conversations

[Chat](https://claude.com/docs/third-party/claude-desktop/chat.md) conversations follow the same storage model as Cowork sessions: each conversation is a session state file plus a working directory under `local-agent-mode-sessions/`, in the layout described in the table above. The state file records the conversation; the working directory holds the transcript, an `uploads/` directory with copies (or hard links) of files attached to the conversation, an `outputs/` directory for files Claude creates during the conversation (its scratch space), and the same HMAC-chained `audit.jsonl` event log. Because attachments are hard-linked where the filesystem allows it, edits made to the original file while the conversation is open can be visible to the conversation. Conversation content leaves the device only as inference requests to your configured provider, as web search queries to your configured search backend, through web access your egress configuration allows, through [sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access), in connector tool calls permitted by your `toolPolicy` configuration and the user's approvals, and, if you have enabled [content capture](https://claude.com/docs/third-party/claude-desktop/telemetry.md#content-capture), in telemetry to your own collector.

For the questions security reviews most often ask about Chat:

* **Chat reads and updates memory only inside projects.** A Chat conversation inside a project can read and update that project's memory unless memory was paused when the conversation started. Chat conversations outside a project don't read or update memory.
* **Project folders are read-only.** A Chat conversation inside a project can read files in folders added to the project in Claude Desktop, under the conditions in [Project folders in Chat](https://claude.com/docs/third-party/claude-desktop/chat.md#project-folders-in-chat), and cannot change them.
* **Claude cannot search past chats.** Users can search their own conversations in the app, which scans the per-session files on the device on demand, but there is no index of conversation content, server-side or local (history exists only as the per-session files above), and a Chat conversation has no tools for listing or reading other sessions' transcripts. Each conversation is isolated to its own directory.
* **The advanced file analysis sandbox writes only inside the session directory.** When [advanced file analysis](https://claude.com/docs/third-party/claude-desktop/chat.md#advanced-file-analysis) is enabled, code runs in a local sandbox. Commands in it can reach the hosts in `coworkEgressAllowedHosts`, as described under [Sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access). The sandbox writes only to the conversation's `outputs/` directory, and reads its `uploads/` directory, its transcript, and its saved tool results plus, for a conversation inside a project, that project's memory. For a conversation inside a project, the sandbox can also read the folders added to the project in Claude Desktop, under the conditions in [Advanced file analysis](https://claude.com/docs/third-party/claude-desktop/chat.md#advanced-file-analysis).

Deleting a conversation's session state file and working directory removes all of this; there is no other copy.

## Credentials

Inference credentials are handled according to how they're delivered:

* **Managed configuration** (for example, `inferenceGatewayApiKey`, `inferenceBedrockBearerToken`): read from the OS preference store or registry at launch and held in memory. The app also writes resolved credentials to a small set of transient, owner-only files for its own session processes, described below.
* **API keys saved in the in-app configuration window**: stored in the `configLibrary/` files, encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows, GNOME Keyring or KWallet on Linux). Requires Claude Desktop 4.4212.0 or later, which also encrypts a key that an earlier version saved, the next time the app launches. See [Unreadable saved API keys](#unreadable-saved-api-keys).
* **OAuth tokens** (in-app Google sign-in, MCP servers with `oauth: true`): stored in the application-data directory, encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows).
* **Credential-helper output**: held in memory for `inferenceCredentialHelperTtlSec` seconds, then discarded and re-fetched.

### Transient credential files

Parts of each session run as separate processes: the sandbox VM for Cowork sessions, and the Claude Code runtime for Code sessions. Processes that cannot receive credentials through an in-memory channel read them from short-lived files that the app writes for them. All of these files are created with owner-only permissions and are cleaned up automatically:

| Path (within the application-data directory) | Contents | Lifecycle |
| - | - | - |
| `host-creds-<random-id>.json` | The resolved inference credential (plus the endpoint), as environment values for background Claude Code worker processes. The app writes it for credentials that it renews, such as a sign-in token or credential-helper output. Before Claude Desktop 4.29.0, the app also wrote it for a static API key or bearer token. Written atomically with owner-only permissions (mode `0600` on macOS; per-user ACLs on Windows). | Rewritten on each credential refresh; deleted when the app quits; leftovers from a crash are removed at the next launch. The random path segment is regenerated when you sign out of the inference provider or its credentials are rotated, so a process holding the old path loses access. |
| `ccd-session-secrets/<session-id>/` | File-based credentials for Code sessions: Google Cloud application default credentials for Google Cloud's Agent Platform, or AWS configuration files for Amazon Bedrock. The directory is created with owner-only permissions (mode `0700` on macOS; per-user ACLs on Windows). | Created when the session starts; removed when the session ends; the whole directory is swept before the next Code session starts and when you sign out of the inference provider. |
| Per-session working directory | For Cowork sessions, the same file-based credentials (Google Cloud's Agent Platform and Amazon Bedrock) are written into the session's working directory. | Scoped to the session; removed with the session directory. |

Aside from these files, credentials delivered through managed configuration are held in memory only.

### Unreadable saved API keys

An encrypted API key can be decrypted only through the secure storage of the OS user account that saved it, so a copy of the `configLibrary/` files alone can't be decrypted elsewhere. Where that account's secure storage moves with the user, for example in a Windows roaming profile that carries the user's DPAPI keys, the key also decrypts on the other device.

When Claude Desktop can't decrypt the key that its connection uses, it shows the banner **Claude can’t read your saved key** and doesn't start sessions. The saved file stays as it is.

Have the user enter the key again in the in-app configuration window, then restart the app, after any of these:

* **The data moves without its secure storage**: the application-data directory is copied or restored to another device or another OS user account
* **A Windows profile changes**: the profile is rebuilt, roams without the user's DPAPI keys, or belongs to a local account whose password an administrator reset
* **The macOS login keychain is reset**
* **The desktop environment changes on Linux**: a key saved under GNOME Keyring can't be decrypted in a KDE session, or the reverse
* **The app is rolled back**: versions earlier than Claude Desktop 4.29.0 send the encrypted text as the key, and the provider refuses it

These cases call for something else:

* **Windows profiles that don't keep the user's DPAPI keys between sign-ins**: the user has to enter the key at each sign-in, so deliver the key through managed configuration instead
* **Secure storage that isn't available as the app launches**: a restart alone is enough. For example, this happens on Linux when the app starts at login before the keyring does, and on macOS when the user dismisses the keychain prompt.
* **Devices with no secure storage that the app can use**, such as Linux without GNOME Keyring or KWallet: the key stays unencrypted, and the configuration window shows **This key is saved unencrypted on this computer.** under the key
* **Tools that read or write the `configLibrary/` files**: a tool that reads the key gets the encrypted value. A tool that writes an unencrypted key still works, and the app encrypts that key the next time it launches.

## Automatic deletion of idle sessions

By default, chats, Cowork tasks, and Code sessions stay on the device until the user deletes them. To delete them after a period without activity, set [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays), [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays), or [`codeSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#codesessionretentiondays) to a number of days from 1 to 3650. Each key covers one kind of session, and a kind you leave unset is kept until the user deletes it. Idle time counts from the session's last activity, and pinned sessions are not exempt.

With [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md) on, a conversation started from the home screen on a device that can run Cowork is a Cowork session. `coworkSessionRetentionDays` covers it along with users' other Cowork tasks, and `chatSessionRetentionDays` still covers Chat conversations. While `coworkSessionRetentionDays` is unset, neither key deletes a home-screen conversation that is a Cowork session, even if `chatSessionRetentionDays` is set. If you use `chatSessionRetentionDays`, keep it and set `coworkSessionRetentionDays` as well.

The app deletes whole sessions in the background. A chat or Cowork task is deleted with its attached files and outputs, and a Code session with its conversation. Projects, memory, and the files in a Code session's working folder stay, and Code sessions on an SSH host aren't affected. A session that is running or open on screen is skipped until a later pass. On a device that gets its configuration from a server, the app stops deleting idle sessions shortly after it loses contact with that server.

### Keep sessions for some users

> [!WARNING]
>
> `sessionRetentionHold` is deprecated. Claude Desktop stops reading it at 12:00 PM Pacific Time on December 17, 2026. From then on, the app deletes the idle sessions of the users it covers, under the periods that are set for them. Deleted sessions can't be recovered.
>
> If you use `sessionRetentionHold`, change `chatSessionRetentionDays`, `coworkSessionRetentionDays`, and `codeSessionRetentionDays` for the same users before that date, or now if it has passed, as described under [Keep sessions for some users](#keep-sessions-for-some-users). Once their devices have the change, remove `sessionRetentionHold`.

To keep some users' idle sessions from being deleted, for example under a legal hold, change `chatSessionRetentionDays`, `coworkSessionRetentionDays`, and `codeSessionRetentionDays` for those users. Make the change in the source that their devices get their configuration from:

* **[Bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) or [MDM profile](https://claude.com/docs/third-party/claude-desktop/mdm.md)**: if those users' devices use a bootstrap server, make the change in the server's response, because the app then ignores these keys in the MDM profile. Set the three keys to `3650`, the longest period, or leave them out, which keeps sessions until the user deletes them.
* **[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)**: set the three keys to `3650` in a [per-group permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies) for those users' group. Rank that policy above their other policies. If the policy leaves a key out, those users keep the period that they had.
* **[Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway)**: set the three keys to `3650` in the `desktop` block of a policy that matches only those users, and put that policy before every other policy that matches them. A user gets only the [first policy that matches them](https://code.claude.com/docs/en/claude-apps-gateway-config#managed), so copy in any other settings that they need. A policy that leaves a key out [takes the catch-all policy's value](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay).

A running app finds a change on a server at its next [configuration check](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#when-a-configuration-change-on-a-device-takes-effect) (every 10 minutes by default), and a change to an MDM profile once the profile reaches the device. It then stops deleting under the old period, without a restart. Until then, it can still delete sessions under the old period.

Other deletions continue, such as these:

* **By users**: users can delete their own sessions, for example from the sidebar or in the [**Storage** window](#how-users-free-up-disk-space)
* **By Claude Code**: [Claude Code's own cleanup](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically) deletes some of its older files, such as checkpoints and large tool outputs. If [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) set `cleanupPeriodDays`, it also deletes Code session conversations older than that number of days.

## How users free up disk space

The **Storage** window shows how much disk space Claude uses on the device. To open it, users go to **Settings > This computer > System** and click **Manage** next to **Storage**. They can also enter `/storage` in the message box in Chat, Cowork, or Code. The window requires Claude Desktop 3.6556.1 or later.

In the window, users can clean up their own inactive sessions on the device, except pinned ones:

* **Chats and Cowork tasks**: the app deletes them, including runs of scheduled tasks. It also deletes their outputs and their copies of attached files in the [application-data directory](#where-data-lives). Files outside that directory stay, such as files in `~/Claude/` or in folders that the user connected.
* **Code sessions**: the app removes their [Git worktrees](https://code.claude.com/docs/en/worktrees) and, if the user chooses, deletes the sessions with their conversations

Users can't undo these deletions.

When the disk that holds the application-data directory has less than 10 GB free, the app shows a **Low disk space** notice. Users can click **Manage storage** in the notice to open the **Storage** window.

You can't hide the **Storage** window or the **Low disk space** notice with a configuration key.

## Move a user to a new device

On devices that get their managed configuration from MDM, you can move a user to a new device by copying their data. The copy moves:

* Chats, Cowork tasks, and Code sessions
* Projects, project instructions, and memory
* Scheduled tasks, skills, and plugins
* Attached files

### What the user sets up again

Ask the user to:

* Sign in to the inference provider, if the app asks
* Enter the provider API key again, if the user saved it in the in-app configuration window (see [Unreadable saved API keys](#unreadable-saved-api-keys))
* Reconnect each connector
* Enter the environment variables for Code sessions from their original source, because the app masks saved values
* In each project they use from Chat, use **Choose a folder > Choose a different folder** to select the same folders again
* Add any keys, sign-ins, or settings that their plugins need
* Set command permissions for plugins

### Requirements for the new device

The new device needs:

* The same platform (macOS, Windows, or Linux) and CPU architecture as the old device
* The same OS user name and home-directory path. Otherwise, Code sessions, scheduled tasks, plugins, and project folders stop working.
* The managed configuration, with the same [`deploymentOrganizationUuid`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentorganizationuuid), in place before Claude Desktop launches
* The same Claude Desktop version, or a newer one

### Copy the data to the new device

> [!WARNING]
>
> The copy holds full conversations. Encrypt any intermediate copy, restrict access to it, and delete it when you're done.

1. Quit Claude Desktop on both devices. Closing its window isn't enough.
2. If the new device has an application-data directory (see [Where data lives](#where-data-lives)), delete it. This removes anything the user created in it.
3. Copy these to the same paths. On Windows, use a copy tool that supports paths longer than 260 characters.
   * The application-data directory, except these files in it, which the app creates again when it needs them:

     * `host-creds-*.json`
     * `ccd-session-secrets/`
     * `spaces-present/*/*/link-key`
     * `ccd-environment-config.json`
     * `cowork-enabled-cli-ops.json`

     If you copied any of them, quit Claude Desktop on the new device, then delete them.
   * `~/Claude/`, or `~/Documents/Claude/` on legacy installs
   * `~/.claude/` and `~/.claude.json`
   * The folders and repositories that the user's projects, scheduled tasks, and Code sessions use
4. Make the user the owner of the copied files, with read and write access. Give no other user account access to the application-data directory, `~/Claude/` or `~/Documents/Claude/`, `~/.claude/`, or `~/.claude.json`.
5. Have the user launch Claude Desktop, sign in if the app asks, and confirm that their chats, Cowork tasks, Code sessions, and projects appear. If they don't, check that the managed configuration has the old device's `deploymentOrganizationUuid` and that the user owns the copied files. Soon after launch, a scheduled task runs once if it recently missed a run.
6. Have the user [set up what the copy doesn't move](#what-the-user-sets-up-again).
7. If the old device stays in use, its enabled scheduled tasks run on both devices. Retire the old device, or turn off its scheduled tasks in Claude Desktop there. To remove the user's data from it, see [Removing data](#removing-data).

## Removing data

To fully reset a device's Claude Desktop on 3P state, delete the application-data directory above and the `~/Claude/` user-files folder. Code session transcripts are in Claude Code's store at `~/.claude/projects/`, which Claude Code in the terminal also uses, so delete them there separately if you need to remove them. For [SSH remote sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#host-requirements), transcripts are in `~/.claude/projects/` and attached files in `~/.claude/uploads/` in the SSH user's home directory on the remote host. Claude Desktop also copies those transcripts to the device, into folders in `~/.claude/projects/` whose names start with `ssh-`, so delete them in both places.

To return to standard Claude Desktop without removing data, choose the Anthropic sign-in option on the sign-in screen; to also remove the locally authored 3P configuration, delete the `configLibrary/` directory.

Except for SSH remote sessions, conversation history exists only on this device, so deleting it is unrecoverable. Deleting an SSH remote session in the app doesn't delete its transcript on the remote host.
