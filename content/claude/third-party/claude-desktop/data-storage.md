> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User identity and local data

> How Claude Desktop on 3P identifies users and where it stores conversations, settings, and credentials on disk

Claude Desktop on third-party (3P) has no Anthropic account. There is no sign-in step, no cloud-stored conversation history, and no per-user state on Anthropic infrastructure. Identity and persistence are entirely local to the device.

## Identity

When the app first launches in 3P mode, it generates a random UUID and writes it (base64-encoded) to the `ant-did` file in the application-data directory. This identifier, together with the `deploymentOrganizationUuid` from your managed configuration, is what's attached to telemetry events. It is random per device and per OS-user account, and Anthropic cannot trace it back to a real device or person.

The OpenTelemetry export to your own collector is the exception: it identifies the user directly. Each exported record carries an `enduser.id` resource attribute with the user's identity and a `process.owner` attribute with the operating-system login name, so attributing activity to named users needs no collector-side correlation. See [User attribution](/docs/third-party/claude-desktop/telemetry#user-attribution) for where the identity comes from and the `endUserAttribution` key that controls it.

## Where data lives

Claude Desktop on 3P stores everything under a dedicated directory, separate from standard Claude Desktop, so the two modes can coexist on one machine without interfering.

| Platform | Application data                           | Logs                                   |
| -------- | ------------------------------------------ | -------------------------------------- |
| macOS    | `~/Library/Application Support/Claude-3p/` | `~/Library/Logs/Claude-3p/`            |
| Windows  | `%LOCALAPPDATA%\Claude-3p\`                | (under the application-data directory) |

<Note>
  On Windows, earlier Claude Desktop releases stored this data under `%APPDATA%\Claude-3p\` (the Roaming profile). On first launch after upgrading, the app moves the existing directory to `%LOCALAPPDATA%` automatically; if Roaming is redirected to a network share, conversation history and configuration are copied and large regenerable caches are re-downloaded. Update any external tooling, backup jobs, or endpoint policies that reference the old path. macOS paths are unchanged.
</Note>

Within the application-data directory:

| Path                                                         | Contents                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ant-did`                                                    | The random device identifier described above.                                                                                                                                                                                                                                                                        |
| `configLibrary/`                                             | Locally authored configuration (from the in-app configuration window). `_meta.json` records which saved configuration is applied; each is a `<id>.json` file alongside it. Ignored when a managed profile is present.                                                                                                |
| `local-agent-mode-sessions/.../cowork_account_settings.json` | User-level preferences set in the app (display name, locale, memory toggle).                                                                                                                                                                                                                                         |
| `local-agent-mode-sessions/`                                 | Cowork and Chat conversation history. One `local_<uuid>.json` file plus a working directory per session, scoped by account and organization ID. The working directory includes an `uploads/` subdirectory with copies of files attached to the conversation and an `outputs/` subdirectory for files Claude creates. |
| `local-agent-mode-sessions/.../memory/`                      | Cowork memory: a `CLAUDE.md` instructions file plus a `memory/` subdirectory of Markdown notes Claude writes about the user's preferences, projects, and feedback. See [Memory](#memory).                                                                                                                            |
| `local-agent-mode-sessions/.../spaces/<projectId>/memory/`   | Markdown memory notes for one project, used by Cowork sessions and Chat conversations inside that project. See [Memory](#memory).                                                                                                                                                                                    |
| `local-agent-mode-sessions/.../<sessionId>/audit.jsonl`      | Append-only log of session events (tool invocations, permission decisions, file operations). Each entry is HMAC-chained to the previous one so edits or deletions are detectable; the companion `.audit-key` file holds the per-session signing key, encrypted via the OS keychain.                                  |
| `claude-code-sessions/`                                      | Code conversation history, in the same per-session layout.                                                                                                                                                                                                                                                           |
| `claude-code/`, `claude-code-vm/`                            | Claude Code binary and VM workspace data for Code sessions.                                                                                                                                                                                                                                                          |
| `vm_bundles/`                                                | Cached copy of the Cowork sandbox VM bundle.                                                                                                                                                                                                                                                                         |
| `cowork_plugins/`                                            | User-installed and [org-provisioned](/docs/third-party/claude-desktop/extensions#organization-plugins-admin) plugins. Created on first plugin install.                                                                                                                                                                    |
| `IndexedDB/`, `Local Storage/`, `Session Storage/`           | Renderer-side UI state (window layout, recent folders, preferences).                                                                                                                                                                                                                                                 |

Files in this directory are written with owner-only permissions so other OS accounts on the same machine cannot read them.

The logs directory contains `main.log` (application and configuration-validation events), `cowork_vm_node.log` (sandbox VM activity), `claude.ai-web.log` (renderer events), and `mcp.log` / `mcp-server-<name>.log` (MCP connection events).

Separately from the application-data directory, Claude Desktop writes user-visible outputs (Artifacts and scheduled-task results) to `~/Claude/` in your home directory, or `~/Documents/Claude/` on legacy installs. This folder is intended for you to browse directly and is not removed when you delete the application-data directory.

## Memory

During Cowork sessions, Claude writes short Markdown files recording what it has learned about the user — working preferences, project context, and corrections — and reads them at the start of subsequent sessions. These files live under `local-agent-mode-sessions/.../memory/memory/` and never leave the device.

Users can review and delete individual entries, or pause memory for new sessions and conversations (existing files are kept but not read or updated), under **Settings → Cowork → Memory**. The same page exposes a **Global instructions** editor for the `CLAUDE.md` file that is included in every session.

Each [project](/docs/cowork/guide/projects) also keeps its own memory under `local-agent-mode-sessions/.../spaces/<projectId>/memory/`. Cowork sessions inside a project read and update the project's memory rather than the files under `local-agent-mode-sessions/.../memory/memory/`. A Chat conversation inside a project can read the project's memory but cannot change it, as described under [Chat conversations](#chat-conversations).

## Chat conversations

[Chat](/docs/third-party/claude-desktop/chat) conversations follow the same storage model as Cowork sessions: each conversation is a session state file plus a working directory under `local-agent-mode-sessions/`, in the layout described in the table above. The state file records the conversation; the working directory holds the transcript, an `uploads/` directory with copies (or hard links) of files attached to the conversation, an `outputs/` directory for files Claude creates during the conversation (its scratch space), and the same HMAC-chained `audit.jsonl` event log. Because attachments are hard-linked where the filesystem allows it, edits made to the original file while the conversation is open can be visible to the conversation. Conversation content leaves the device only as inference requests to your configured provider, as web search queries to your configured search backend, through web access your egress configuration allows, in connector tool calls permitted by your `toolPolicy` configuration and the user's approvals, and, if you have enabled [content capture](/docs/third-party/claude-desktop/telemetry#content-capture), in telemetry to your own collector.

For the questions security reviews most often ask about Chat:

* **Memory is read-only and applies only inside projects.** A Chat conversation inside a project can read that project's memory unless memory was paused when the conversation started, but cannot add to or change it. Chat conversations outside a project do not read or update memory.
* **Past chats are not searchable.** There is no index of conversation content, server-side or local (history exists only as the per-session files above), and a Chat conversation has no tools for listing or reading other sessions' transcripts. Each conversation is isolated to its own directory.
* **The advanced file analysis sandbox writes only inside the session directory.** When [advanced file analysis](/docs/third-party/claude-desktop/chat#advanced-file-analysis) is enabled, code runs in a local sandbox with no network access. The sandbox writes only to the conversation's `outputs/` directory, and reads its `uploads/` directory plus, for a conversation inside a project, that project's memory.

Deleting a conversation's session state file and working directory removes all of this; there is no other copy.

## Credentials

Inference credentials are handled according to how they're delivered:

* **Managed configuration** (for example, `inferenceGatewayApiKey`, `inferenceBedrockBearerToken`): read from the OS preference store or registry at launch and held in memory. The app also writes resolved credentials to a small set of transient, owner-only files for its own session processes, described below.
* **OAuth tokens** (in-app Google sign-in, MCP servers with `oauth: true`): stored in the application-data directory, encrypted with the operating system's secure storage (Keychain on macOS, DPAPI on Windows).
* **Credential-helper output**: held in memory for `inferenceCredentialHelperTtlSec` seconds, then discarded and re-fetched.

### Transient credential files

Parts of each session run as separate processes: the sandbox VM for Cowork sessions, and the Claude Code runtime for Code sessions. Processes that cannot receive credentials through an in-memory channel read them from short-lived files that the app writes for them. All of these files are created with owner-only permissions and are cleaned up automatically:

| Path (within the application-data directory) | Contents                                                                                                                                                                                                                                                                        | Lifecycle                                                                                                                                                                                                                                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `host-creds-<random-id>.json`                | The resolved inference credential (bearer token or API key, plus the endpoint), as environment values for background Claude Code worker processes. Written atomically with owner-only permissions (mode `0600` on macOS; per-user ACLs on Windows).                             | Rewritten on each credential refresh; deleted when the app quits; leftovers from a crash are removed at the next launch. The random path segment is regenerated when you sign out of the inference provider or its credentials are rotated, so a process holding the old path loses access. |
| `ccd-session-secrets/<session-id>/`          | File-based credentials for Code sessions: Google Cloud application default credentials for Google Cloud's Agent Platform, or AWS configuration files for Amazon Bedrock. The directory is created with owner-only permissions (mode `0700` on macOS; per-user ACLs on Windows). | Created when the session starts; removed when the session ends; the whole directory is swept before the next Code session starts and when you sign out of the inference provider.                                                                                                           |
| Per-session working directory                | For Cowork sessions, the same file-based credentials (Google Cloud's Agent Platform and Amazon Bedrock) are written into the session's working directory, which is mounted into the sandbox VM.                                                                                 | Scoped to the session; removed with the session directory.                                                                                                                                                                                                                                  |

Aside from these files, credentials delivered through managed configuration are held in memory only.

## Removing data

To fully reset a device's Claude Desktop on 3P state, delete the application-data directory above and the `~/Claude/` user-files folder. To return to standard Claude Desktop without removing data, choose the Anthropic sign-in option on the sign-in screen; to also remove the locally authored 3P configuration, delete the `configLibrary/` directory.

Conversation history exists only in this directory, so deleting it is unrecoverable.
