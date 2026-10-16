> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat in Claude Desktop on 3P

> What Chat can and cannot do in Claude Desktop on 3P, and how to configure it

<Note>
  When [Unified Claude](/docs/third-party/claude-desktop/unified-claude) is on, a message sent from the home screen starts a Cowork session on a device that can run Cowork.
</Note>

Chat in Claude Desktop on third-party (3P) is a conversational surface for quick questions and drafting. Unlike [Cowork](/docs/cowork/overview) and [Code](/docs/third-party/claude-desktop/code), which run agentic sessions with access to folders you grant and a code-execution environment, a Chat conversation runs with a deliberately small tool surface: it can search and fetch the web under your admin configuration, read files attached to the conversation, read and update the project's memory and read the files in the project's folders when the conversation is inside a project, write files into a scratch space of its own, and use skills from the plugins you provision, and nothing else on the machine. Chat is off by default and is enabled with a single configuration key.

Chat conversations run against your configured inference provider, and their history is stored on the user's device. See [User identity and local data](/docs/third-party/claude-desktop/data-storage#chat-conversations) for exactly what is written where and what can leave the device.

## What a Chat conversation can reach

| Capability | Scope |
| - | - |
| Web search | Same options and rules as Cowork and Code sessions; depends on your provider or a configured search server. See [Web search](/docs/third-party/claude-desktop/web-tools#web-search). |
| Web fetch | Runs in the app on the device, never inside a sandbox. Every fetch is checked against `coworkEgressAllowedHosts`; with no allowlist configured, fetch is disabled. See [Web fetch](/docs/third-party/claude-desktop/web-tools#web-fetch). |
| Attached files | Read-only access to files the user attaches to the conversation. Each attachment is copied or hard-linked into the conversation's local uploads directory. |
| Project memory | For a conversation inside a project, that project's [memory](/docs/third-party/claude-desktop/data-storage#memory): Claude can read, add to, and update the notes that Chat conversations and Cowork sessions in that project share. Not used if memory was paused when the conversation started, or for conversations outside a project. |
| Project folders | For a conversation inside a project, read-only access to folders added to the project in Claude Desktop. Claude can list and read files in them. See [Project folders in Chat](#project-folders-in-chat). |
| Scratch directory | A per-conversation working directory where Claude can create and edit files (documents, data files, HTML artifacts) and offer them to the user for download or preview. |
| Managed MCP servers | The servers you provision via [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) are available in Chat with the same approval model as Cowork sessions: a tool's `toolPolicy` of `"allow"` pre-approves it, `"blocked"` blocks it, and `"ask"` requires user approval on every call. A tool with no policy asks the user, who can allow it once or grant standing approval, as in Cowork. |
| Clarifying questions | Claude can present multiple-choice questions to the user (the `AskUserQuestion` tool). |
| Plugin skills and hooks | Skills from the plugins you provision through [organization plugins](/docs/third-party/claude-desktop/extensions#organization-plugins-admin) or [plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin) are available in Chat, including as slash commands. Hooks from those plugins also run in Chat conversations as they do in Cowork sessions, as described under [Plugin hooks](/docs/third-party/claude-desktop/extensions#plugin-hooks). Plugin sub-agents do not run in Chat, and a skill that runs scripts needs [advanced file analysis](#advanced-file-analysis). Plugin skills require Claude Desktop 1.44121.4 or later, and plugin hooks run in Chat on Claude Desktop 1.52386.0 or later. |
| Code execution | Off by default. When you enable [advanced file analysis](#advanced-file-analysis), Claude can additionally run code in a local sandbox against attached files and, inside a project, files in the project's folders. See [Sandbox network access](#sandbox-network-access). |

`disabledBuiltinTools` and `builtinToolPolicy` apply in Chat the same way they do in Cowork and Code sessions. For example, adding `"WebFetch"` removes web fetch from Chat conversations too.

### Project folders in Chat

For a conversation inside a project, Claude can list and read files in folders added to the project in Claude Desktop, and can't change them.

* **Folders the user adds.** To have Claude read a folder, the user adds it to the project in Claude Desktop and starts a new conversation. For a folder that an [import](/docs/third-party/claude-desktop/import) put on the project, or that was on the project before Chat could read folders, the user adds it to the project again.
* **Folders you allow.** If you set [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), the list also limits which of a project's folders Claude reads.

## What a Chat conversation cannot do

Apart from reading [the folders added to a project](#project-folders-in-chat), in a Chat conversation Claude cannot:

* **Read or write the filesystem** beyond the conversation's own uploads and scratch directories, its own transcript and saved tool results (read-only), and, inside a project, the project's memory. The tool for requesting folder access is removed, and the app refuses folder grants to a Chat conversation even when requested through internal interfaces.
* **Run code on the host.** There is no shell access. With advanced file analysis off (the default), the sandbox VM is never started for Chat; with it on, code runs only inside the sandbox described under [Advanced file analysis](#advanced-file-analysis), never on the host itself.
* **Run in auto mode.** Chat conversations always run in the default permission mode. Auto mode and other reduced-supervision modes are rejected for Chat regardless of `autoModeEnabled`.
* **Create or run scheduled tasks**, or list the ones that exist.
* **Escalate into an agentic session.** The tools that launch Code sessions or dispatch background agent tasks are removed. When a request needs capabilities Chat doesn't have, Claude says so and suggests starting the task in Cowork instead.
* **Read other conversations.** The tools that list sessions or read other sessions' transcripts are removed, so a Chat conversation cannot search or quote your other chats, Cowork sessions, or Code sessions.

These restrictions are enforced in the app's main process, not just hidden in the UI.

## Advanced file analysis

By default, Chat can read attached files only in the formats Claude understands natively. Setting `chatAdvancedFileAnalysisEnabled` to `true` lets Claude also run code against attachments and, inside a project, against files in [the project's folders](#project-folders-in-chat). This is useful for spreadsheets, PowerPoint files, and other formats that need parsing, and for inline data analysis on attached data.

The execution environment is intentionally narrower than the Cowork sandbox:

* Code runs in the same isolated local VM that Cowork uses. For Chat, the VM starts only when analysis is coming: on the first analysis call, or at the start of a turn with files attached.
* Commands in the sandbox can reach the hosts in `coworkEgressAllowedHosts`. See [Sandbox network access](#sandbox-network-access).
* The only conversation data the sandbox sees is the conversation's attached files (read-only), its scratch directory (writable), its own transcript and saved tool results, such as connector results (read-only), and, for a conversation inside a project, that project's memory (read-only), plus read-only reference material bundled by the app. The sandbox sees no user folders except, for a conversation inside a project, [the project's folders](#project-folders-in-chat) (read-only), and no other sessions' working directories or transcripts.
* The sandbox doesn't see project folders in a conversation that starts while a rule for `"Read"`, `"Grep"`, or `"Glob"` is set in `disabledBuiltinTools`, in `builtinToolPolicy` with a value other than `"allow"`, or as a deny or ask rule in Claude Code's own managed settings on the device. See [`chatAdvancedFileAnalysisEnabled`](/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled) for more cases.
* Each command runs independently; results land in the scratch directory, where Claude can offer them to the user as downloads or artifacts.

The data flow end to end: an attached file is copied into the conversation's local uploads directory, mounted read-only into the sandbox when analysis runs, and any outputs are written to the conversation's scratch directory on local disk. File content leaves the device only as conversation context sent to your configured inference provider, in web search queries to your configured search backend, through web fetches your egress allowlist permits, through [sandbox network access](#sandbox-network-access), in a connector tool call permitted by your `toolPolicy` configuration and the user's approvals, or, if you have enabled [content capture](/docs/third-party/claude-desktop/telemetry#content-capture), in telemetry to your own collector.

<Note>
  Advanced file analysis uses the same shell tool as Cowork's sandbox, so adding `"Bash"` to `disabledBuiltinTools` disables it even when `chatAdvancedFileAnalysisEnabled` is `true`. Running it requires the sandbox VM bundle, which the app downloads from Anthropic unless you deployed the offline installer (see [required egress paths](/docs/third-party/claude-desktop/telemetry#required-egress-paths)).
</Note>

### Sandbox network access

Commands that Claude runs in the advanced file analysis sandbox can reach the hosts in [`coworkEgressAllowedHosts`](/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts). A command-line tool that a [plugin](/docs/third-party/claude-desktop/extensions#controlling-user-extensions) adds to the sandbox can also reach the hosts that its plugin declares. Those hosts don't need to be in the list. If the list is unset or empty, no host is allowed for other commands.

* **Other hosts.** A web request to any other host gets a `403 Forbidden` response with the header `X-Proxy-Error: blocked-by-allowlist`. `pip install` reports this as `Tunnel connection failed: 403 Forbidden`.
* **Package installs.** Package managers contact their default index, so list its hosts. For pip, list `pypi.org` and `files.pythonhosted.org`. To install from a private mirror, list its host. The command must name the mirror, for example with pip's `--index-url`.

<Warning>
  By default, commands in the sandbox run without an approval prompt. A command can upload anything the sandbox can read to a listed host, and can run what it downloads from one. [Web fetch](/docs/third-party/claude-desktop/web-tools#web-fetch) in Chat uses the same list, so a host you list for web fetch is also open to sandbox commands. With `"*"` in the list, network filtering in the sandbox is off, so commands can reach any host.

  * **To have Claude ask before each command**, set `"Bash"` to `"ask"` in [`builtinToolPolicy`](/docs/third-party/claude-desktop/configuration#builtintoolpolicy). That policy also applies to Cowork and Code sessions.
  * **To keep web fetch but turn off sandbox commands**, set [`chatAdvancedFileAnalysisEnabled`](#configuration) to `false`.
</Warning>

<Note>
  Sandbox network access requires Claude Desktop 2.42304.0 or later. On earlier versions, requests to listed hosts get a `403 Forbidden` response. After a device updates, commands can reach the listed hosts with no change to your configuration, in existing conversations too. If Claude says in an existing conversation that the sandbox has no network access, ask the user to start a new conversation.
</Note>

## Configuration

| Key | Default | Effect |
| - | - | - |
| [`chatTabEnabled`](/docs/third-party/claude-desktop/configuration#chattabenabled) | off | Makes Chat available. Chat is opt-in: it appears in the app only when this key is explicitly `true`. |
| [`chatAdvancedFileAnalysisEnabled`](/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled) | off | Allows code execution in the sandbox described under [Advanced file analysis](#advanced-file-analysis), on attached files and, inside a project, on files in the project's folders. Has no effect unless Chat is enabled. |

While the `desktopHome` key for [Unified Claude](/docs/third-party/claude-desktop/unified-claude#how-unified-claude-interacts-with-chat-and-cowork-settings) has a value, Claude Desktop ignores `chatTabEnabled`, `chatAdvancedFileAnalysisEnabled`, and `coworkTabEnabled`.

When `chatTabEnabled` is `true`, Claude Desktop presents Chat and Cowork together as **Home** in its sidebar, next to **Code**. From Home, the user chooses **Chat** or **Cowork** in the message box, and the sidebar lists chats and tasks together. When the key is unset or `false`, the sidebar shows **Cowork** in place of Home and the message box offers no choice. If [`coworkTabEnabled`](/docs/third-party/claude-desktop/configuration#coworktabenabled) is `false` while Chat is enabled, the message box offers Chat only.

<Note>
  This layout applies to Claude Desktop 1.26832.0 and later. Earlier versions show **Chat** (when enabled), **Cowork**, and **Code** as separate tabs, controlled by the same keys.
</Note>

Enforcement of `chatTabEnabled` happens in the app's main process: when the key is unset or `false`, Chat does not appear in the app, and the app additionally refuses to start or continue a Chat conversation, including conversations created before an admin turned the key off.

The rule that at least one surface must stay enabled counts Chat only when `chatTabEnabled` is explicitly `true`: a configuration that disables Cowork and Code without enabling Chat re-enables Cowork with a validation warning, rather than leaving users with an empty app. With `chatTabEnabled` set to `true`, a chat-only configuration is valid.

## Where Chat data lives

Chat conversations are stored on the local device, in the same per-session layout as Cowork sessions: conversation history, attachment copies, scratch outputs, and a tamper-evident audit log, all under the application-data directory. Nothing is synced to a server, and there is no server-side index of past conversations. See [Chat conversations](/docs/third-party/claude-desktop/data-storage#chat-conversations) on the data-storage page for the breakdown.
