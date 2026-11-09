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

Claude Desktop on 3P keeps its application data and logs in directories of its own, separate from those of standard Claude Desktop. A few locations in the user's home directory are outside these directories, and [standard Claude Desktop uses them too](#data-shared-with-standard-claude-desktop).

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
| `local-agent-mode-sessions/.../<sessionId>/audit.jsonl` | Log of one Cowork session or Chat conversation. It holds the full text of prompts, Claude's responses, and tool inputs and results. See [Session audit log](#session-audit-log). |
| `claude-code-sessions/` | Code session records holding each session's working folder, settings, title, and sometimes a short summary. The conversation transcripts themselves are in Claude Code's own store at `~/.claude/projects/`, outside this directory. |
| `claude-code/`, `claude-code-vm/` | Claude Code binary and VM workspace data for Code sessions. |
| `vm_bundles/` | Cached copy of the VM workspace bundle that Cowork sessions run in, plus the data disk the app creates to hold those sessions' home directories inside the VM. |
| `cowork_plugins/` | User-installed and [org-provisioned](https://claude.com/docs/third-party/claude-desktop/extensions.md#organization-plugins-admin) plugins. Created on first plugin install. |
| `plugin-mcp-auth/`, `connectors/*/plugin-mcp/` | On Windows and Linux, the `.credentials.json` file that holds the user's sign-ins to plugin servers, made outside **Code**. See [Credentials](#credentials). |
| `IndexedDB/`, `Local Storage/`, `Session Storage/` | Renderer-side UI state (window layout, recent folders, preferences). |

Other standard OS accounts on the same machine can't read the files in this directory, but administrators can. On macOS and Linux, the app creates the directory with owner-only permissions. On Windows, the directory takes the permissions of the user's profile.

The app doesn't encrypt conversations, settings, or the locally applied configuration other than its API keys. On Windows and Linux, it also doesn't encrypt the user's sign-ins to plugin servers or secret plugin settings entered in **Code**. Protection at rest for those files depends on the device's full-disk encryption, such as FileVault or BitLocker. The app encrypts some credentials with the operating system's secure storage, such as API keys saved from the in-app configuration window and the OAuth tokens of managed MCP servers (see [Credentials](#credentials)).

The logs directory contains `main.log` (application and configuration-validation events), `ssh.log` (SSH connection events), `cowork_vm_node.log` (sandbox VM activity), `claude.ai-web.log` (renderer events), and `mcp.log` / `mcp-server-<name>.log` (MCP connection events).

Separately from the application-data directory, Claude Desktop writes user-visible outputs (Artifacts and scheduled-task results) to `~/Claude/` in your home directory, or `~/Documents/Claude/` on legacy installs. This folder is intended for you to browse directly and is not removed when you delete the application-data directory. To back up a user's data, copy every location listed under [Copy the data to the new device](#copy-the-data-to-the-new-device).

### Data shared with standard Claude Desktop

Unless you [restrict a device to one deployment mode](https://claude.com/docs/third-party/claude-desktop/mdm.md#restrict-a-device-to-one-deployment-mode), a user can switch, in the same OS user account, between Claude Desktop on 3P and standard Claude Desktop, where users sign in to claude.ai. On a device where you haven't turned on the [migration to Claude Enterprise](https://claude.com/docs/third-party/claude-desktop/move-to-claude-enterprise.md), the two modes handle the user's data as follows:

* **Chats, Cowork tasks, projects, and memory**: standard Claude Desktop doesn't show, import, or upload those stored in the 3P [application-data directory](#where-data-lives). It reads and writes some settings files in that directory, such as the user's choice of mode. It also reads the Code session records in `claude-code-sessions/`, so that it doesn't list those sessions or delete their folders.
* **Code sessions**: each mode lists only its own, but **Code** in both modes and Claude Code in the terminal keep their transcripts in the same folder, `~/.claude/`. Each mode reads the transcripts there to count usage, and the figures that standard Claude Desktop shows for `/stats` in **Code** include sessions from both modes and the terminal. Claude Code in the terminal can resume a session from either mode, and then sends the earlier conversation to the provider that the terminal uses.
* **Claude Code setup**: `~/.claude/` and `~/.claude.json` also hold Claude Code's setup, such as skills, plugins, hooks, permission rules, trusted folders, and MCP servers, shared by **Code** in both modes and Claude Code in the terminal. Sign-ins to MCP servers made in **Code** are in [Claude Code's own credential store](https://code.claude.com/docs/en/authentication#credential-management), which they share too.
* **Connectors**: standard Claude Desktop doesn't load the connectors, plugins, or extensions that users added outside **Code**. From your [`managedMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) entries, it loads only a built-in Microsoft 365 connector set in the device's managed profile.
* **Connector sign-ins**: on a device configured by MDM, a local file, or a bootstrap server, switching modes leaves [connector sign-ins](#credentials) made outside **Code** in place and doesn't revoke them. Standard Claude Desktop doesn't use them, and Claude Desktop on 3P uses them again when the user switches back.
* **Files in `~/Claude/`**: by default, both modes write Artifacts, scheduled tasks, and project files here, and each lists only its own. To give Claude Desktop on 3P a folder of its own, have the user go to **Settings > Cowork** and click **Change** next to **Cowork files**. The app copies everything in the current folder, the other mode's files included, to the new location and leaves the old folder in place.

With the migration on, standard Claude Desktop also copies what [What is migrated](https://claude.com/docs/third-party/claude-desktop/move-to-claude-enterprise.md#what-is-migrated) lists, and `~/.claude/`, `~/.claude.json`, and `~/Claude/` are still shared.

No configuration key moves these three locations. They are in the user's home directory, so each OS user account has its own.

A [diagnostic report](https://claude.com/docs/third-party/claude-desktop/installation.md#troubleshooting), or the `.zip` file from **Help > Troubleshooting > Show Logs in Finder** (**Show Logs in File Explorer** on Windows), includes app log lines from both modes, whichever mode the user creates it in.

### Session audit log

As a Cowork session or Chat conversation runs on the device, the app writes an `audit.jsonl` file in the session's working directory, under `local-agent-mode-sessions/` in the [application-data directory](#where-data-lives). The file holds the conversation's content. The session's transcript, under the same directory, holds it too. The app appends the full text of:

* The user's prompts
* Claude's responses
* Tool inputs and results, such as the text of a file that Claude reads or writes

The file also records any thinking text that Claude returns, permission decisions, and session details such as the model and token usage. Code sessions don't write this file.

The app handles the file as follows:

* **Protection**: the file isn't encrypted, so protection at rest depends on the device's full-disk encryption
* **Transfer**: the app doesn't send the file off the device
* **Deletion**: the app deletes the file with its session. By default, a session stays until the user deletes it, as described under [Automatic deletion of idle sessions](#automatic-deletion-of-idle-sessions).
* **Configuration**: no configuration key, including [`otlpContentCapture`](https://claude.com/docs/third-party/claude-desktop/telemetry#content-capture), turns the file off or changes what it records
* **Signing**: when the app has a signing key for the session, in the `.audit-key` file beside the log, each entry carries a keyed hash (HMAC) linked to the signed entries before it. Otherwise, entries are unsigned. The app doesn't check these hashes, and they don't reveal entries removed from the end of the file.

To retain an audit trail, use the [OpenTelemetry export](https://claude.com/docs/third-party/claude-desktop/telemetry.md#sending-telemetry-to-your-own-collector) to your own collector.

## Memory

During Cowork sessions, Claude writes short Markdown files recording what it has learned about the user (working preferences, project context, and corrections) and reads them at the start of subsequent sessions. In a scheduled Cowork task outside a project, Claude can read these files but doesn't save to them: it lists the notes with their one-line descriptions and chooses which to open. These files live under `local-agent-mode-sessions/.../memory/memory/`. The app doesn't sync them to a server. The files themselves leave the device if the user [exports them](#turn-on-export-and-import) or you copy them. What Claude reads from them becomes part of the session, so it goes to your configured inference provider with the rest of the conversation.

Where sessions run on the device, users find the memory controls in these places:

* **Pause memory**: users go to **Settings > General** and turn off the **Use memory in sessions** toggle to pause memory for new sessions and conversations (existing files are kept but not read or updated)
* **Review and delete notes**: where your configuration allows Cowork and the device can run it, users go to **Settings > General** and scroll to the **Memory** heading. Users can review and delete individual notes there.
* **Edit global instructions**: where your configuration allows Cowork, users go to **Settings > Cowork** and click **Edit** next to **Global instructions** to change the `CLAUDE.md` file that is included in every session

### Project memory

Each [project](https://claude.com/docs/cowork/guide/projects.md) keeps its own memory under `local-agent-mode-sessions/.../spaces/<projectId>/memory/`. Cowork sessions inside a project, scheduled tasks included, read and update the project's memory rather than the files under `local-agent-mode-sessions/.../memory/memory/`. A Chat conversation inside a project can also read and update the project's memory, as described under [Chat conversations](#chat-conversations).

To review a project's memory files, users go to **Projects**, open the project, and look under the **Memory** heading. Users click a file to read it, or right-click it and select **Copy path** to get its location on the device.

## Chat conversations

[Chat](https://claude.com/docs/third-party/claude-desktop/chat.md) conversations follow the same storage model as Cowork sessions: each conversation is a session state file plus a working directory under `local-agent-mode-sessions/`, in the layout described under [Where data lives](#where-data-lives). The state file records the conversation; the working directory holds the transcript, an `uploads/` directory with copies (or hard links) of files attached to the conversation, an `outputs/` directory for files Claude creates during the conversation (its scratch space), and the [session audit log](#session-audit-log). Because attachments are hard-linked where the filesystem allows it, edits made to the original file while the conversation is open can be visible to the conversation. Conversation content leaves the device only as inference requests to your configured provider, as web search queries to your configured search backend, through web access your egress configuration allows, through [sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access), in connector tool calls permitted by your `toolPolicy` configuration and the user's approvals, in telemetry to your own collector if you have enabled [content capture](https://claude.com/docs/third-party/claude-desktop/telemetry.md#content-capture), in the zip files that users export if you have [turned on export](#turn-on-export-and-import), and in any copy that you make.

For the questions security reviews most often ask about Chat:

* **Chat reads and updates memory only inside projects.** A Chat conversation inside a project can read and update that project's memory unless memory was paused when the conversation started. Chat conversations outside a project don't read or update memory.
* **Project folders are read-only.** A Chat conversation inside a project can read files in folders added to the project in Claude Desktop, under the conditions in [Project folders in Chat](https://claude.com/docs/third-party/claude-desktop/chat.md#project-folders-in-chat), and cannot change them.
* **Claude cannot search past chats.** Users can search their own conversations in the app, which scans the per-session files on the device on demand, but there is no index of conversation content, server-side or local (history exists only as the per-session files above), and a Chat conversation has no tools for listing or reading other sessions' transcripts. Each conversation is isolated to its own directory.
* **The advanced file analysis sandbox writes only inside the session directory.** When [advanced file analysis](https://claude.com/docs/third-party/claude-desktop/chat.md#advanced-file-analysis) is enabled, code runs in a local sandbox. Commands in it can reach the hosts in `coworkEgressAllowedHosts`, as described under [Sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access). The sandbox writes only to the conversation's `outputs/` directory, and reads its `uploads/` directory, its transcript, and its saved tool results plus, for a conversation inside a project, that project's memory. For a conversation inside a project, the sandbox can also read the folders added to the project in Claude Desktop, under the conditions in [Advanced file analysis](https://claude.com/docs/third-party/claude-desktop/chat.md#advanced-file-analysis).

Deleting a conversation's session state file and working directory removes all of this.

## Credentials

Credentials are handled according to how they're delivered:

* **Managed configuration** (for example, `inferenceGatewayApiKey`, `inferenceBedrockBearerToken`): read from the OS preference store or registry at launch and held in memory. The app also writes resolved credentials to a small set of transient, owner-only files for its own session processes, described below.
* **API keys saved in the in-app configuration window**: stored in the `configLibrary/` files, encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows, GNOME Keyring or KWallet on Linux). Requires Claude Desktop 4.4212.0 or later, which also encrypts a key that an earlier version saved, at the next launch where secure storage is available. See [Unreadable saved API keys](#unreadable-saved-api-keys).
* **OAuth tokens** (in-app Google sign-in, MCP servers with `oauth: true` in `managedMcpServers` or in an `org-plugins/` plugin): stored in the application-data directory, encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows).
* **[Sign-ins to plugin servers](https://claude.com/docs/third-party/claude-desktop/extensions.md#sign-in-to-a-plugin-server)**: the OAuth tokens from a sign-in outside **Code** are stored as follows, and any program that runs under the user's OS account can read them:

  * **Windows and Linux**: an unencrypted `.credentials.json` file under `plugin-mcp-auth/` or `connectors/*/plugin-mcp/` in the application-data directory
  * **macOS**: the login keychain, or that file if the keychain rejects the write

  The tokens from a sign-in in **Code** are in [Claude Code's own credential store](https://code.claude.com/docs/en/authentication#credential-management).
* **Secret plugin settings**: a plugin can ask the user for a value that it marks as sensitive, such as an API key. A value entered in **Code** is in [Claude Code's own credential store](https://code.claude.com/docs/en/authentication#credential-management):
  * **Linux, and Windows by default**: an unencrypted file
  * **macOS**: the login keychain, or that file if the keychain rejects the write
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

When Claude Desktop can't decrypt the key that its connection uses, it shows the banner **Claude can’t read your saved key** and doesn't start sessions. Connectors set in the same saved configuration aren't listed or started until the app can decrypt the key. The saved file stays as it is.

Have the user enter the key again in the in-app configuration window, then restart the app, after any of these:

* **The data moves without its secure storage**: the application-data directory is copied or restored to another device or another OS user account
* **A Windows profile changes**: the profile is rebuilt, roams without the user's DPAPI keys, or belongs to a local account whose password an administrator reset
* **The macOS login keychain is reset**
* **The desktop environment changes on Linux**: a key saved under GNOME Keyring can't be decrypted in a KDE session, or the reverse
* **The app is rolled back**: versions earlier than Claude Desktop 4.29.0 send the encrypted text as the key, and the provider refuses it

These cases call for something else:

* **Windows profiles that don't keep the user's DPAPI keys between sign-ins**: the user has to enter the key at each sign-in, so deliver the key through managed configuration instead
* **Secure storage that isn't available as the app launches**: have the user restart the app once secure storage is available. They don't need to enter the key again. For example, on Linux the app can start at login before the keyring does.
* **A macOS keychain that the app can't access as it launches**: this happens, for example, when the user dismisses the keychain prompt. Have the user restart the app, and enter their password or click **Allow** if macOS asks. If the banner stays, have the user enter the key again.
* **A key entered again while secure storage isn't available**: the app saves the key unencrypted and uses it after a restart. At the next launch where secure storage is available, the app encrypts the key, so a later launch without secure storage shows the banner again.
* **Devices with no secure storage that the app can use**, such as Linux without GNOME Keyring or KWallet: the key stays unencrypted, and the configuration window shows **This key is saved unencrypted on this computer.** under the key
* **Tools that read or write the `configLibrary/` files**: a tool that reads the key gets the encrypted value. A tool that writes an unencrypted key still works, and the app encrypts that key at the next launch where secure storage is available.

## Automatic deletion of idle sessions

By default, chats, Cowork tasks, and Code sessions stay on the device until the user deletes them. To delete them after a period without activity, set [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays), [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays), or [`codeSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#codesessionretentiondays) to a number of days from 1 to 3650. Each key covers one kind of session, and a kind you leave unset is kept until the user deletes it. Idle time counts from the session's last activity, and pinned sessions are not exempt.

With [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md) on, a conversation started from the home screen on a device that can run Cowork is a Cowork session. `coworkSessionRetentionDays` covers it along with users' other Cowork tasks, and `chatSessionRetentionDays` still covers Chat conversations. While `coworkSessionRetentionDays` is unset, neither key deletes a home-screen conversation that is a Cowork session, even if `chatSessionRetentionDays` is set. If you use `chatSessionRetentionDays`, keep it and set `coworkSessionRetentionDays` as well.

The app deletes whole sessions in the background:

* **Chats**: the app deletes a chat, its copies of attached files, its outputs, and the live artifacts (interactive pages) that Claude created in the chat. The live artifacts of chats deleted before Claude Desktop 4.16336.0 stay on the device.
* **Cowork tasks**: the app deletes a task, its copies of attached files, and its outputs. The task's live artifacts stay. A home-screen conversation that is a Cowork session is deleted the same way, and its live artifacts stay.
* **Code sessions**: the app deletes a session and its conversation. It also removes the session's [Git worktree](https://code.claude.com/docs/en/worktrees), except in some cases, such as when the worktree has uncommitted changes or the session is pinned. Other files in the session's working folder stay, and Code sessions on an SSH host or in WSL aren't affected.

Projects and memory stay. A session that is running or open on screen is skipped until a later pass. On a device that gets its configuration from a server, the app stops deleting idle sessions shortly after it loses contact with that server.

### Keep sessions for some users

> [!WARNING]
>
> `sessionRetentionHold` is deprecated. Claude Desktop stops reading it at 12:00 PM Pacific Time on December 17, 2026. From then on, the app deletes the idle sessions of the users it covers, under the periods that are set for them. Deleted sessions can't be recovered.
>
> If you use `sessionRetentionHold`:
>
> 1. Change `chatSessionRetentionDays`, `coworkSessionRetentionDays`, and `codeSessionRetentionDays` for the same users before that date, or now if it has passed, as described under [Keep sessions for some users](#keep-sessions-for-some-users).
> 2. If the hold is in the catch-all policy (`match: {}`) of a Claude apps gateway, it also covers the users of every other policy that leaves `sessionRetentionHold` out. If it is in the organization-wide settings of the Enterprise Admin Console, it also covers the users of every per-group permission policy that leaves it out. In either case, set all three keys to `3650` where the hold is and in every policy that sets any of the three keys. You don't need to add a policy or change the order of your policies.
> 3. Once the change has reached the devices of every user that the hold covers, remove `sessionRetentionHold`.

To keep some users' idle sessions from being deleted, for example under a legal hold, change `chatSessionRetentionDays`, `coworkSessionRetentionDays`, and `codeSessionRetentionDays` for those users. Make the change in the source that their devices get their configuration from:

* **[Bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) or [MDM profile](https://claude.com/docs/third-party/claude-desktop/mdm.md)**: if those users' devices use a bootstrap server, make the change in the server's response, because the app then ignores these keys in the MDM profile. Set the three keys to `3650`, the longest period, or leave them out, which keeps sessions until the user deletes them.
* **[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)**: set the three keys to `3650` in a [per-group permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies) for those users' group. Rank that policy above their other policies. If the policy leaves a key out, those users keep the period that they had. To keep every user's sessions, set the three keys to `3650` in the organization-wide settings and in every per-group permission policy that sets any of them.
* **[Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway)**: set all three keys to `3650` in the `desktop` block of a policy that matches only those users, and put that policy before every other policy that matches them. If this policy leaves one of the keys out, those users can [get a shorter period for it from a policy listed after it](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay), such as the catch-all policy. By default, the gateway applies only the [first policy that matches a user](https://code.claude.com/docs/en/claude-apps-gateway-config#managed), and takes any setting that policy leaves out from the catch-all policy. Copy into this policy any other settings that those users need. To keep every user's sessions, set all three keys to `3650` in the catch-all policy, keep it last, and set them to `3650` in every other policy that sets any of the three keys.

A running app finds a change on a server at its next [configuration check](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#when-a-configuration-change-on-a-device-takes-effect) (every 10 minutes by default), and a change to an MDM profile once the profile reaches the device. It then stops deleting under the old period, without a restart. Until then, it can still delete sessions under the old period.

Other deletions continue, such as these:

* **By users**: users can delete their own sessions, for example from the sidebar or in the [**Storage** window](#how-users-free-up-disk-space)
* **By Claude Code**: [Claude Code's own cleanup](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically) deletes some of its older files, such as checkpoints and large tool outputs. If [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings) set `cleanupPeriodDays`, it also deletes Code session conversations older than that number of days.

## How users free up disk space

The **Storage** window shows how much disk space Claude uses on the device. To open it, users go to **Settings > This computer > System** and click **Manage** next to **Storage**. They can also enter `/storage` in the message box in Chat, Cowork, or Code. The window requires Claude Desktop 3.6556.1 or later.

In the window, users can clean up their own inactive sessions on the device, except pinned ones:

* **Chats and Cowork tasks**: the app deletes them, including runs of scheduled tasks. It also deletes their outputs and their copies of attached files in the [application-data directory](#where-data-lives). For a chat, the app also deletes the live artifacts (interactive pages) that Claude created in the chat. Other files stay, such as the live artifacts of a Cowork task or of a [home-screen conversation that is a Cowork session](https://claude.com/docs/third-party/claude-desktop/unified-claude.md), the rest of `~/Claude/`, and files in folders that the user connected. The live artifacts of chats deleted before Claude Desktop 4.16336.0 stay too.
* **Code sessions**: the app removes their [Git worktrees](https://code.claude.com/docs/en/worktrees) that have no uncommitted changes, except those it can't safely remove, such as a worktree that another session uses. It removes worktrees with uncommitted changes only if the user selects the **Also remove** checkbox, and then those changes are lost. If the user chooses, the app also deletes the sessions with their conversations, but not a session whose worktree stays.

Users can't undo these deletions.

When the disk that holds the application-data directory has less than 10 GB free, the app shows a **Low disk space** notice. Users can click **Manage storage** in the notice to open the **Storage** window.

You can't hide the **Storage** window or the **Low disk space** notice with a configuration key.

## Move a user to a new device

You can move a user's Claude Desktop data to a new device with an export or a copy:

* **Export and import**: you [turn on two settings](#turn-on-export-and-import). The user exports their data to a zip file on the old device and imports it on the new device.
* **[Copy the data](#copy-the-data-to-the-new-device)**: on devices that get their configuration from MDM or from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), you copy the user's [application-data directory](#where-data-lives) and related folders to the same paths on the new device

### When to use an export or a copy

Both ways need the same platform (macOS, Windows, or Linux) on both devices. A copy moves more data.

Copy the data if:

* **The user's Cowork projects and scheduled tasks use many folders.** After an import, the user adds each folder again.
* **On Windows, the user's Code sessions or Code scheduled tasks use folders on a mapped network drive.** An import leaves out those sessions and tasks.
* **Your policies don't let users save their conversations and files to a zip file**
* **Claude Desktop doesn't open on the old device**, so the user can't start an export
* **You set `allowedOrganizationUuids`** under [`claudeAiImport`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport), which turns off import from a file
* **The export dialog says that the export is over the import limit of 20 GB or 5,000,000 files**

Use an export and import if:

* **The new device has a different OS user name or home-directory path.** A copy needs the same user name and path.
* **The user already works on the new device.** An import adds to their data, and a copy replaces it.

### Turn on export and import

Both settings are off by default.

* **Managed configuration**: set [`claudeAiImport`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) to `{"enabled": true, "exportEnabled": true}`, along with any fields you already set in it
* **[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md)**: go to the **Capabilities** page and turn on the **Enable import** and **Enable export** switches under **Claude.ai data import**. To turn them on for some users, use a [per-group permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies).

Both devices need Claude Desktop 4.23118.0 or later, the same platform, and [the same organization](#requirements-for-the-new-device). Earlier versions export only sessions, their output files, and project names.

If a setting is already on, it applies to [the additional data](#what-can-leave-and-enter-a-device) as soon as a user's app [updates](https://claude.com/docs/third-party/claude-desktop/installation.md#updates) to 4.23118.0 or later. With `enabled`, users can import that data. With `exportEnabled` too, users can export it. To stop either one, turn off that setting.

For the user's steps and the full list of data that moves, see [Move your data to another device](https://claude.com/docs/third-party/claude-desktop/import.md#move-your-data-to-another-device).

### What can leave and enter a device

`exportEnabled` works only when `enabled` is on.

* **`exportEnabled`**: users can export their data to a zip file anywhere they can save files. The file contains sessions with attached and output files, projects, the files of each project whose folder is in the default location (`~/Claude/Projects`), memory, scheduled tasks, saved skills, uploaded plugins, some app preferences, and the commands, arguments, and environment variable names of local MCP servers. It also lists the paths of the other folders that projects use, and of the folders and files that scheduled tasks use. If you set `allowedOrganizationUuids`, it contains only sessions, their files, and project names and instructions.
* **`enabled`**: users can import an export file from another device, a claude.ai data export, and earlier sessions on the device. Claude Desktop can't verify who made an export file, so it asks the user to confirm that the file is their own. If the user doesn't confirm, only the sessions are imported, with the projects and attached files that they use.

After the user confirms:

* **Memory**: Claude uses it right away, including when scheduled tasks run. Paused memory is in the file but isn't imported.
* **App preferences**: those that the user hasn't set on the new device apply right away
* **Project instructions**: Claude uses them after the user accepts them
* **Project files**: the import copies them into a new folder for each project
* **Folders**: the import doesn't connect any to a project or a Cowork task. A Code session or a Code scheduled task keeps its folder only if the new device trusts that folder. The last screen lists the folders that the user's projects and scheduled tasks used.
* **Uploaded plugins, saved skills, and scheduled tasks**: they stay off until the user turns them on. Setting [`userPluginUploadsEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#userpluginuploadsenabled), [`skillCreationEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#skillcreationenabled), or [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled) to `false` keeps that kind of data out of the import.
* **Local MCP servers**: for each import, a second dialog lists up to five servers with their full commands and environment variables. Claude Desktop tries to start the servers that the user adds right away. Blocks that the user set on tools on the old device don't apply, because tool permissions aren't imported. The app writes no values of these servers' environment variables into an export. Until the user enters the values, a server might not work, or might run without a limit that the user set in a variable. Setting [`isLocalDevMcpEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled) to `false` keeps local MCP servers out of the export and the import.

> [!WARNING]
>
> The zip file isn't encrypted. Sessions, project files, memory, scheduled tasks, skills, plugins, and the arguments of local MCP servers are copied as they are, with any passwords or API keys written in them. Sign-ins, connector tokens, saved provider API keys, and the values of environment variables for the local MCP servers that users added stay on the old device. Tell users to import only their own exports, to keep the file private, and to delete every copy when they no longer need it.

The old device keeps its data until you [remove it](#removing-data).

### What a copy moves

On devices that get their configuration from MDM or from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), you can move a user to a new device by copying their data. The copy moves:

* Chats, Cowork tasks, and Code sessions
* Projects, project instructions, and memory
* Scheduled tasks, skills, and plugins
* Attached files
* Local MCP server settings and app preferences

### What the user sets up again

After a copy, ask the user to:

* Sign in to the inference provider, if the app asks
* Enter the provider API key again, if the user saved it in the in-app configuration window (see [Unreadable saved API keys](#unreadable-saved-api-keys))
* Reconnect each connector
* Enter the environment variables for Code sessions from their original source, because the app masks saved values
* In each project they use from Chat, use **Choose a folder > Choose a different folder** to select the same folders again
* Add any keys, sign-ins, or settings that their plugins need
* Set command permissions for plugins

### Requirements for the new device

For a copy, the new device needs:

* The same platform (macOS, Windows, or Linux) and CPU architecture as the old device
* The same OS user name and home-directory path. Otherwise, Code sessions, scheduled tasks, plugins, and project folders stop working.
* The same organization as the old device:
  * **MDM**: the managed configuration, with the same [`deploymentOrganizationUuid`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentorganizationuuid), in place before Claude Desktop launches
  * **Enterprise Admin Console**: no managed configuration to deploy. When the app asks the user to sign in to Claude, they use the same account and organization as on the old device.
* Anything on the device that your configuration relies on for credentials, set up as on the old device. For example, a [credential helper](https://claude.com/docs/third-party/claude-desktop/credential-helper.md) or other helper script, an [AWS named profile](https://claude.com/docs/third-party/claude-desktop/bedrock.md#named-profile), or a [Google Cloud credentials file](https://claude.com/docs/third-party/claude-desktop/vertex.md#credentials-file).
* The same Claude Desktop version, or a newer one

### Copy the data to the new device

> [!WARNING]
>
> The copy holds full conversations. Encrypt any intermediate copy, restrict access to it, and delete it when you're done.

1. Quit Claude Desktop on both devices, without signing out. Closing its window isn't enough.
2. If the new device has an application-data directory (see [Where data lives](#where-data-lives)), delete it. This removes anything the user created in it.
3. Copy these to the same paths. On Windows, use a copy tool that supports paths longer than 260 characters.
   * The application-data directory, except these files in it, which the app creates again when it needs them:

     * `host-creds-*.json`
     * `ccd-session-secrets/`
     * `spaces-present/*/*/link-key`
     * `ccd-environment-config.json`
     * `cowork-enabled-cli-ops.json`

     Also leave out `plugin-mcp-auth/` and `connectors/*/plugin-mcp/`, which on Windows and Linux hold the user's sign-ins to plugin servers. The user signs in to those servers again on the new device.

     If you copied any of these files or folders, quit Claude Desktop on the new device, then delete them.
   * The user's Cowork files folder: `~/Claude/`, or `~/Documents/Claude/` on legacy installs. If the user changed it, note the folder shown under **Cowork files** in **Settings > Cowork** on the old device before step 1, and copy that folder instead.
   * `~/.claude/` and `~/.claude.json`
   * The folders and repositories that the user's projects, scheduled tasks, and Code sessions use
4. Make the user the owner of the copied files, with read and write access. Give no other user account access to the application-data directory, the user's Cowork files folder, `~/.claude/`, or `~/.claude.json`.
5. Have the user launch Claude Desktop, sign in if the app asks, and confirm that their chats, Cowork tasks, Code sessions, and projects appear. If any are missing, check that:
   * The user owns the copied files
   * The [`ant-did`](#identity) file in the application-data directory has the same contents as on the old device. If it doesn't, start again from step 1.
   * With MDM, the managed configuration has the old device's `deploymentOrganizationUuid`
   * With the Enterprise Admin Console, the account menu at the bottom of the sidebar shows the same organization as on the old device. If it shows another name, look for a managed profile that [keeps the device off the admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile). If you find one, remove it, then have the user relaunch Claude Desktop and sign in. Otherwise, have the user choose your organization from the account menu and sign in.
6. Have the user [set up what the copy doesn't move](#what-the-user-sets-up-again).
7. Soon after launch on the new device, a scheduled task runs once if it recently missed a run. If the old device stays in use, its enabled scheduled tasks run on both devices. Retire the old device, or turn off its scheduled tasks in Claude Desktop there. To remove the user's data from it, see [Removing data](#removing-data).

## Removing data

To fully reset a device's Claude Desktop on 3P state, delete the application-data directory above and the `~/Claude/` user-files folder. Code session transcripts are in Claude Code's store at `~/.claude/projects/`, which Claude Code in the terminal also uses, so delete them there separately if you need to remove them. For [SSH remote sessions](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#host-requirements), transcripts are in `~/.claude/projects/` and attached files in `~/.claude/uploads/` in the SSH user's home directory on the remote host. Claude Desktop also copies those transcripts to the device, into folders in `~/.claude/projects/` whose names start with `ssh-`, so delete them in both places.

On a device that also runs standard Claude Desktop, `~/Claude/` and `~/.claude/` hold that mode's files too, so deleting them deletes those as well. See [Data shared with standard Claude Desktop](#data-shared-with-standard-claude-desktop).

> [!NOTE]
>
> On macOS, the user's sign-ins to plugin servers, made outside **Code**, stay in the login keychain after you delete the application-data directory. To end them, have the user [disconnect each server](https://claude.com/docs/third-party/claude-desktop/extensions.md#sign-in-to-a-plugin-server) first, or revoke them at the server's authorization server.

To return to standard Claude Desktop without removing data, choose the Anthropic sign-in option on the sign-in screen; to also remove the locally authored 3P configuration, delete the `configLibrary/` directory.

Except for SSH remote sessions and any export or copy that was made, conversation history exists only on this device, so deleting it is unrecoverable. Deleting an SSH remote session in the app doesn't delete its transcript on the remote host.
