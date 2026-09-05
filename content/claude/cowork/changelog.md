> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Release notes for Claude Desktop

<Update label="v1.46388.4" description="2026-09-05">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.46388.3" description="2026-09-04">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * Added support for attaching your home folder, Windows Documents, AppData, the macOS Library folder, and whole drives; Claude's own configuration and session data inside them stay off-limits, as do certain credential and shell-startup locations (for example SSH keys, AWS and Google Cloud credentials, and bash, zsh and PowerShell profile files).

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.46388.2" description="2026-09-04">
  **General**

  * No user-facing changes.

  **Code**

  * Fixed Code sessions started in a git worktree failing to initialize on Windows.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.46388.1" description="2026-09-04">
  **General**

  * Removed the "Mark as unread" action for chats.
  * Fixed links between artifacts and shared-artifact links clicked inside the app opening in the browser or losing their share key; they now open in place, and a teammate without access sees the request-access screen instead of "not available".
  * Fixed memory use on macOS growing steadily while working with files, which could end with the system reporting it had run out of application memory.
  * Fixed new messages being queued instead of sent after reopening a chat whose last message had no reply yet.
  * Fixed removing a file from the message box after stopping or losing a reply sometimes deleting that file from the message you had already sent, which made "Try again" on it fail.
  * Fixed side chat, the slash-command picker, usage insights, and other quick actions failing silently on machines where an organization deploys a Claude Code `managed-mcp.json`.
  * Fixed the dictation microphone button disappearing from the chat composer once a message had text, an attached file, or a quoted reply.

  **Code**

  * Added a queue for messages sent while your 5-hour usage limit is reached: they wait above the composer instead of failing, and you can edit, cancel, or send them when you're ready.
  * Added keep-awake while Claude works: the computer no longer idle-sleeps while Claude is working in the Code tab, with a "Keep computer awake while Claude works" setting (and a "Keep awake on battery power" option) under Settings > Claude Code, a "Keep computer awake for this session" item in the session menu, and a one-time notice after a long task.
  * Removed the Summary transcript view from the session's Transcript view menu; sessions that had it selected open in the Normal view.
  * Fixed Extra high and Max effort on Claude Opus 5 quietly running at High when thinking was turned off in your Claude Code settings; those efforts now run with thinking on for the session.
  * Fixed organization-managed settings not loading, and Remote Control not connecting automatically, for some users until they signed out and back in.
  * Fixed sessions failing to open: a "Couldn't load this" message now recovers on its own instead of needing a manual reload, sessions no longer show "No messages yet" on Windows hosts that use FSLogix or similar profile containers, and a transcript that can't be read shows the reason with a Retry button.
  * Fixed SSH sessions being restarted after some reconnects, which could leave duplicate Claude Code processes on the remote machine, and fixed messages held for an unreachable host: they are retried after an app restart, and when the host comes back needing your password or an unlocked SSH agent the app asks you instead of marking the message "needs you".
  * Fixed switching models in a session: a switch refused with a "plugin hooks could not be loaded" error now restarts that session's Claude Code on the model you picked, the model picker no longer shows a model Claude Code refused, and Remote Control sessions no longer offer models the connected Claude Code version can't run.
  * Fixed switching models staying blocked for the rest of the session when an organization-managed plugin's marketplace or a plugin hook failed to load.
  * Fixed the remembered folder sometimes getting mixed up with a remote machine's path, which made every local session launch fail with "working directory no longer exists".

  **Cowork**

  * Added automatic re-runs (after 5, 15, and 30 minutes) for a scheduled task that could not reach the model at all, for example right after the computer wakes behind a VPN.
  * Fixed Record a skill opening an unresponsive chooser window on Windows.
  * Fixed saving a skill Claude proposes in a conversation: a name that matches one of your skills now offers to update that skill instead of failing with "Try again", and when saving is blocked until you sign in again the Save skill button opens the sign-in prompt instead of a generic error.
  * Fixed scheduled tasks and other automatic ways of starting a session choosing a model the installed app version can't run, which made every turn fail.
  * Fixed the row under the composer (Add folder, permission mode, model) disappearing after switching a session to automatic approvals.

  **3P**

  * Added `blockReadsOutsideWorkingDirectories`: restricts Code sessions to reading files inside the session folder and `allowedWorkspaceFolders`; file tools refuse reads elsewhere, and sandboxed shell commands lose access to the home directory.
  * Added `configRecheckIntervalMinutes`: how often a running app re-checks its managed configuration for changes, from 2 to 30 minutes; unset means 10 minutes, where the app previously checked every 30. A served value applies without a restart, and the key can also be set from device management.
  * Added `disableBypassPermissionsMode`: removes bypass permissions mode from Code sessions and Cowork tasks, so Claude always follows the configured permission policy.
  * Added `sshClientPath` (beta): the absolute path of the OpenSSH program the app runs for SSH sessions; when unset, the app uses the first `ssh` on the user's PATH.
  * Added an Edit button to your most recent message in Cowork and Chat sessions, so you can revise and resend it, and fixed "Restart conversation from here" doing nothing in Chat sessions.
  * Added the restart prompt, escalating to a required restart after `relaunchEnforcementHours`, when device-managed configuration (the managed plist, Windows policy registry, or Linux managed-settings file) changes while the app is running; previously only configuration changes served from a customer bootstrap endpoint prompted one.
  * (breaking) Changed `relaunchEnforcementHours`: in served configuration the key moved from `bootstrap.relaunchEnforcementHours` to `lifecycle.relaunchEnforcementHours`; this release no longer reads the old path and earlier versions do not read the new one, so move the value under `lifecycle` (the flat-format and device-management key name is unchanged); the key can now also be set from device management; and the default window before a required restart is now 24 hours instead of 1. A device-management profile that sets any app-behavior key takes precedence over a served value for this key, so such a profile should set it too.
  * (breaking) Changed how unreadable Claude Code managed settings are handled: if a device's `managed-settings.json` file, a drop-in, the device-management plist, or the Windows policy registry value cannot be parsed, Claude Code now refuses to start and names the source, so sessions on that device will not start until that file or value is fixed or removed; previously they ran without those settings. Check that these sources parse on managed devices before rolling out this version.
  * Changed `allowedPluginMarketplaces` entries set to `auto_install` or `required` without a pinned commit SHA (or without `manifestSha256` for a `url` source) to show as available with a configuration warning, instead of being removed from the marketplace list.
  * Changed Claude Code's `allowedMcpServers` setting (in its `managed-settings.json`, not the managed-configuration schema) to govern only servers users add themselves: a server from a `managed-mcp.json` file that the allowlist used to filter out now loads, and `deniedMcpServers` is the way to keep it off.
  * Fixed chat search returning no results; searching finds chats by title and message content again.
  * Fixed deployments without cloud features, or with the Cowork tab turned off, showing controls that could not work there, including Remote Control, automatic pull requests, the Cloud and Slack session filters, Add marketplace, and Cowork slash commands.
  * Fixed organization plugins staying installed for users after an administrator removed the plugin's folder from the system `org-plugins` directory.
  * Fixed remote MCP connectors whose `headersHelper` mints the credential continuing to fail for up to several minutes after the server rejected an expired credential; the helper now re-runs immediately and the rejected request is retried once.
</Update>

<Update label="v1.44121.4" description="2026-09-02">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Added support in Chat for skills from organization-provided plugins, and Chat-only users can now see and manage those plugins under Customize, matching Cowork and Code.
  * Fixed advanced file analysis in Chat failing with "Workspace unavailable" for users whose organization enables `chatAdvancedFileAnalysisEnabled` but turns Cowork off with `coworkTabEnabled: false`.
  * Fixed managed OAuth connectors showing a connection error instead of prompting to sign in when the app starts without a usable sign-in (expired with no refresh token, or never signed in on this machine), including servers added by URL alone, where Connect could fail instead of opening the sign-in page.
  * Fixed organization-configured URL plugin marketplaces failing to install or load plugins with "marketplace entry path does not stay inside the marketplace directory".
</Update>

<Update label="v1.44121.2" description="2026-09-02">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * Fixed sessions on Windows being unable to run commands or fetch web pages. This reverts the 1.44121.1 fix for sessions failing to start on Windows for accounts with many saved artifacts, scheduled tasks, or connected folders.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.44121.1" description="2026-09-02">
  **General**

  * Added Claude to the "Open with" menu for common work files, including spreadsheets, PDFs, Word and PowerPoint documents, text files, and images, on macOS and on Windows (Microsoft Store and MSIX installs).
  * Fixed a crash at launch when the app's settings file couldn't be read.
  * Fixed a new chat's first message being dropped when you had to sign in again or verify this device; the chat now asks for that step in a dialog over your message.
  * Fixed an issue where an invalid settings file could cause all app settings to be reset.
  * Fixed Claude not finding files attached in Cowork and Chat, including pasted files and a re-attached file with the same name; attachments that can't be read now say so instead of being dropped silently.
  * Fixed scheduled tasks failing with an error after a permission approval.
  * Fixed the app reloading endlessly when it keeps crashing right after loading; it now stops and shows what to do next.

  **Code**

  * Added a Split View submenu to the View menu for opening a new session beside or below the current one, and side panes (diff, terminal, plan, preview, and others) can now open in a window of their own.
  * Added Claude Code output styles: an "Output style" submenu in the session menu and a `/output-style` command for viewing and switching styles, a "New style…" option that drafts a custom style from a plain-language description, and a default style setting in Settings › Claude Code.
  * Changed the Files pane to open files as tabs beside a collapsible file tree, with single-click preview tabs, multi-select, richer right-click menus, and inline previews for PDF, Word, Excel, and PowerPoint files.
  * Fixed `/rewind` appearing undone when returning to a session after navigating away, which could also cause the next message to silently drop recent conversation history.
  * Fixed Code sessions repeatedly failing to start after a corrupt Claude Code download on macOS, failing to start on Linux arm64, and SSH and WSL session setup failing on slow connections; the one-time install now shows progress and can fall back to uploading Claude Code from your computer.
  * Fixed sessions failing to start on macOS 12 (Monterey).
  * Fixed sessions getting stuck on "responding" when a message was queued near the end of a turn.

  **Cowork**

  * Changed live artifact sharing to follow your organization's Artifacts setting and sharing policies: members no longer see sharing options their organization has turned off, and already-shared artifacts keep Copy link and Unshare.
  * Changed updating a skill from a file card or skill proposal to apply in one step with an Undo toast instead of a confirmation dialog; where a confirmation still appears, its Update button is the pre-selected action.
  * Changed what happens when web fetch isn't available for your organization: Claude now says so instead of retrying and reporting failed fetches.
  * Fixed a crash when previewing an image file that is empty or actually contains text.
  * Fixed a message with an attachment that couldn't be read or was too large failing to send over and over with no explanation; Claude now marks the attachment with the problem, says what to do, and offers Retry where it can help.
  * Fixed sessions failing to start on Windows for accounts with many saved artifacts, scheduled tasks, or connected folders.
  * Fixed sessions that run Claude Code directly on the device failing to start for organizations that set `disableSideloadFlags` in Claude Code's managed settings (`managed-settings.json`, an MDM profile, or the registry); in those sessions Claude Code loads none of the desktop's plugins, so their commands, agents, and hooks are unavailable.
  * Fixed the session page reloading after you connect a connector that signs in through the browser.

  **3P**

  * Added `claudeAiImport.automatic3pImport` (beta): when `true` and `deploymentOrganizationUuid` is set, the app copies this computer's earlier third-party sessions stored before an organization ID was configured into that organization's session store, once per device and in the background, independently of `claudeAiImport.enabled`; a copy interrupted when the app quits resumes on the next launch.
  * Added `egressProxyUrl` and `egressProxyPacUrl`: route the app's and the agent's traffic through a corporate HTTP proxy, or let a PAC file choose the proxy per request, instead of following the operating system's proxy settings; on macOS and Windows, Cowork's workspace follows the pinned proxy too. Both keys are read from device management or the local configuration file only, and the PAC file wins when both are set.
  * Added `inferenceStreamIdleTimeoutSec`: how many extra seconds (300 to 1800, default 300) Chat, Cowork, and Code sessions wait for model output on a streaming response that is sending only keep-alive pings, for gateways that send keep-alives while the upstream model is silent. Gateway provider only.
  * Added a Duplicates step to the import wizard when an imported Project has the same name as one you already have, with the option to merge the imported sessions into your Project and remove the duplicate; the Projects page offers the same merge.
  * Added conversation titles to the OpenTelemetry export: a `desktop_session_title_set` event carries each Cowork and Code session's title plus the Claude Code session ID to join on, sent when `otlpDesktopLogLevel` is `info` or lower; the title text is included only when `otlpContentCapture` includes `userPrompts`.
  * Added installing and updating plugins from admin-configured marketplaces on devices where Cowork isn't available, from the Code tab or the Cowork tab.
  * Added local scheduled tasks to the Code tab, including the `/schedule` command and the Scheduled page, matching what Cowork already offered.
  * Added the ability to attach files in SSH Code sessions.
  * (breaking) Changed the Usage page cost estimate to require `inferenceModelPricingEnabled`; `inferenceModelPricingMultiplier` and `inferenceModelPricing` now refine the estimate only while it is on and no longer turn it on by themselves.
  * Changed `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` set in the `env` block of Claude Code's managed settings (`managed-settings.json` or your organization's server-managed Claude Code settings) to apply to Chat, Cowork, and Code sessions even when the computer has a system proxy configured.
  * Changed `isClaudeCodeForDesktopEnabled`: when it is `false`, the app no longer starts Code sessions even if asked directly, Preview no longer scans projects for a dev server, and the computer is no longer offered for Remote Control; a Code session requested anyway shows "Code sessions are turned off by your organization" instead of a retry prompt.
  * Fixed Bedrock and Bedrock Mantle sessions being cut off by network idle timeouts during long thinking phases on Opus 4.7 and later models.
  * Fixed Code tab sessions not prompting to re-authenticate when the deployment's credentials had expired; they now show the same sign-in prompt as Cowork. Also fixed Live Artifact `askClaude()` calls and the Code tab's "Detect dev server" failing on deployments that use SSO, credential helpers, Vertex, or Bedrock SSO.
  * Fixed managed MCP connector sign-in staying permanently stuck when the identity provider no longer recognizes the OAuth client the app registered; the app now registers a new client automatically.
  * Fixed MCP servers provided by plugins not connecting in Code and Cowork sessions when `managedMcpServers` is configured; in that case, with `isLocalDevMcpEnabled` set to `false`, plugins' remote MCP servers connect and their local (stdio) ones stay blocked.
  * Fixed plugins distributed as a zip whose top level is a single component folder (for example `skills/` or `commands/`) installing with no skills, commands, or agents.
  * Fixed the `allowedWorkspaceFolders` policy not always being applied to Code sessions over SSH.
  * Fixed the Code tab home's usage stats reporting a favorite model, per-model breakdown, and activity from other Claude Code history on the same machine instead of this deployment's own sessions.
</Update>

<Update label="v1.40609.1" description="2026-08-30">
  **General**

  * Updated the bundled Claude Code CLI to version 2.1.255.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.40609.0" description="2026-08-27">
  **General**

  * Fixed Claude sometimes being unable to read or search a page in the built-in browser just after opening it or while it was still loading, and browser screenshots and interactions timing out or stalling on Windows and Linux while the browser pane was closed or another page was selected.
  * Fixed the app failing to launch when one of its settings files had become corrupted, and settings files sometimes being left corrupt after an unexpected shutdown or power loss on Windows.
  * Fixed the Share dialog: "Keep private" now takes effect immediately, and sharing a chat while offline shows an error instead of waiting indefinitely.
  * Fixed typing with an IME (Japanese, Chinese, or Korean): confirming or cancelling a conversion with Enter, Escape, or a digit key no longer sends half-composed text, discards typed drafts, denies tool approvals, rejects plans, or stops Claude's response in Code sessions, and no longer commits or discards text in the browser pane's address field.
  * Fixed scheduled tasks that run on this computer occasionally being marked as skipped without running; a run the app fails to pick up is now retried a few minutes later.

  **Code**

  * Added side-task suggestions in cloud sessions: Claude can suggest follow-up tasks that you start on your machine, in the cloud, or in the same session with one click.
  * Added `/resume`: search the Claude Code sessions started from your terminal on this computer and continue one in the app on the same transcript.
  * Added a view of the session's MCP servers: type `/mcp` in a local session to see the servers from `.mcp.json`, `~/.claude.json`, plugins, and your claude.ai connectors, with live status and Connect, Reconnect, and Re-authenticate actions.
  * Fixed "Import Claude Code CLI sessions" (Help > Troubleshooting): it again finds Code sessions whose sidebar entries were lost after a reinstall or repair, no longer rewrites a session file that a running Claude Code process is still using, and saves a backup of the original transcript when importing removes its thinking blocks.
  * Fixed inline plan comments being silently lost when left after a plan was approved; the Plan pane now accepts comments in Plan mode or while Claude is asking you to approve the plan, and says when commenting opens otherwise.
  * Fixed SSH sessions losing messages that were waiting to be sent when the remote host became unreachable or the app was quit, updated, or restarted; they are now kept and delivered automatically at the next connection, and Claude Code is restarted on the host when needed.
  * Improved SSH session reconnects: high-latency links no longer drop their own connection, a network change mid-stream is noticed within seconds, an unreachable host is no longer re-dialed every few seconds in the background, and the session shows the specific connection error with a Try again button instead of a generic message or an indefinite "Reconnecting…".

  **Cowork**

  * Fixed files dropped onto the composer together with a folder being discarded; they now attach alongside the folder.
  * Fixed shell commands that use plugin or skill file paths failing with "No such file or directory".
  * Fixed the app running out of memory after many scheduled task runs.
  * Fixed the Cowork readiness check appearing to hang for minutes when a network-redirected profile folder is unreachable, and reporting a computer as unsupported because of an encrypted leftover folder from an uninstalled Claude version.
  * Fixed organization plugins failing to install or update on some Windows Store installs.
  * Fixed a message that starts with a typed, pasted, or app-filled slash command for one of your enabled skills failing with "Unknown skill" in an existing task; it now sends.

  **3P**

  * Added `relaunchEnforcementHours` (served configuration only): when a served configuration change needs a restart, it sets how many hours (0 to 336) users may keep running on the previous configuration; at the deadline Claude shows a restart dialog and restarts on its own after 2 minutes of inactivity. Unset means 1 hour.
  * Added `sshHostAllowlist` (beta): admins can turn on SSH remote sessions in the Code tab by listing the hosts users may connect to (`["*"]` allows any host). Unset keeps SSH sessions off unless a Claude Code managed-settings file on the device already allows hosts; an explicit `[]` keeps them off even then when the configuration is admin-delivered (device management or trusted remote delivery), while on a self-configured install the device allowlist still applies. Works with a gateway, Claude API key, or Foundry, and with Bedrock and Vertex when they use token-based credentials; file-based credential kinds are refused at session start with a message naming the kind.
  * Added an estimated-cost view to the Usage page chart: when the organization has turned on cost estimates, the chart can switch between tokens and estimated cost per day (per week at 90 days), and days with turns that have no estimate show as gaps rather than \$0.
  * Added an in-app warning when the organization's configuration uses a deprecated field: each user sees a dismissible notice from September 10, 2026 and once more in the 24 hours before the field stops being accepted, with a Details dialog naming each field, its replacement, the cut-off date and what changes then, plus a Copy report button that puts a plain-text summary for administrators on the clipboard. The new `disableConfigDeprecationWarnings` key hides the first showing; the final 24-hour reminder still appears. The warning also appears on standard deployments whose device-management profile uses one of these fields.
  * Added Anthropic's Cowork and Claude Code plugin marketplaces as prefilled entries in the Setup window's `allowedPluginMarketplaces` Add menu.
  * (breaking) Deprecated a set of older managed-configuration spellings, each accepted until October 7, 2026, 12:00 PM Pacific Time, with an in-app warning from September 10, 2026: `inferenceGatewayHeaders` (use `inferenceCustomHeaders`), `trustBootstrapLocalExec` (use `trustBootstrapDelivery`), `enduserAttribution` (use `endUserAttribution`), `inferenceGatewayAuthScheme` values `sso` (use `inferenceCredentialKind: "interactive"`) and `auto` (remove the key; `bearer` is the default), `isDxtEnabled` (use `isDesktopExtensionEnabled`) and `isDxtSignatureRequired` (use `isDesktopExtensionSignatureRequired`), header maps written as strings or lists in `inferenceCustomHeaders`, `otlpHeaders`, `otlpResourceAttributes` and `bootstrapHeaders` (use a JSON object), the `orgPluginSettings` record form (use the array form), the `ask-session` tool-permission value in `builtinToolPolicy`, `managedMcpServers[].toolPolicy` and `orgPluginSettings[].tools[].permission` (use `ask`), and in `managedMcpServers` entries the `scopes` list (use `scope`), `transport: "builtin"` (remove it), `authorityHost` (use `azureCloud: "us-gov-high"` for a GCC High tenant), `source` (remove it), `oauth` written as a number or string (use `true` or an `oauth` object), `oauth.scopes` or a list-valued `oauth.scope` (use `oauth.scope` as one space-separated string), and entries other than a built-in server with no `transport` (add `transport: "http"`, `"sse"` or `"stdio"`; a built-in Microsoft 365 or GitHub entry takes no `transport`). After the cut-off a renamed key's old name falls back to its fail-closed value or default, and an invalid `managedMcpServers` or `orgPluginSettings` entry makes that connector or tool policy unavailable until it is rewritten.
  * Changed `inferenceVertexProjectId` and `inferenceVertexWorkforceUserProject`: a value delivered by a bootstrap URL the user configured themselves (in Settings or a local configuration file) now asks that user to approve it before it takes effect, and declining quits the app. Because the project ID is required, each such Vertex install prompts once after updating. Values delivered through device management, or by a bootstrap URL that device management set or that `trustBootstrapDelivery: true` covers, are unchanged and never prompt. Both keys must now match the Google Cloud project format.
  * Changed `toolSearchEnabled` on gateway deployments to enable tool search alone; other experimental Claude Code betas stay suppressed.
  * Changed how a managed-configuration value the app cannot read is handled: it now engages the restriction it belongs to instead of being ignored. Restriction keys such as `disabledBuiltinTools`, `builtinToolPolicy`, `coworkTabEnabled` and `disableBundledSkills` fall back to their restrictive value, an unreadable `managedMcpServers` keeps Code sessions restricted to managed MCP servers, an unreadable `isDesktopExtensionEnabled` or `isDesktopExtensionSignatureRequired` disables extensions or requires signed extensions, and a tool-permission value the app does not recognize is applied as the most restrictive setting (`ask` for a built-in tool, `blocked` for a plugin-delivered tool) and reported as a configuration error. `allowedPluginMarketplaces`, the built-in GitHub MCP preset and `otlpTracesEnabled` are no longer marked Beta.
  * Changed the Setup window's configuration exports and the published bootstrap JSON schema to write `orgPluginSettings` in its array form; the app still accepts the older record form until October 7, 2026. Desktop versions before 1.15200.0 read only the record form and do not enforce plugin tool locks given the array, so update the fleet past 1.15200.0 before deploying an exported configuration that uses it.
  * Changed the Vertex AI credential kind for Google sign-in to `inferenceCredentialKind: "interactive"`, matching other providers; `oauth` keeps working until October 7, 2026 (12:00 PM Pacific Time). If you deliver configuration as nested JSON (a self-hosted bootstrap server or a Setup JSON export), keep `oauth` until the whole fleet is on this release or later, because an older desktop drops the Google client ID from a nested `interactive` credential and Vertex sign-in stops working; flat MDM keys, .mobileconfig and .reg files are unaffected. Until October 7, 2026 a Vertex configuration that sets `interactive` together with `inferenceVertexWorkforceAudience` and no `inferenceVertexOAuthClientId` is still read as Workforce Identity; after that it means Google sign-in, so set `workforce` explicitly if that is the intent.
  * Improved Cowork reliability when the workspace is slow to start or has been idle, and made switching back to a recently opened Code tab session faster.
  * Fixed importing sessions from a previous Claude Desktop install: imported Cowork sessions keep their Project and its `~/Claude/Projects/<Name>` folder instead of getting a new empty one, an interrupted import now appears in Import history and its sessions are no longer imported twice on the next run, and the import wizard no longer re-creates a Project you had deleted (an imported Project that duplicates an existing name gets a "(1)" suffix).
  * Fixed the Code tab's plugin directory and Customize > Plugins not listing plugins from marketplaces configured with `allowedPluginMarketplaces`; an admin-configured marketplace is now managed as the organization's in both tabs.
</Update>

<Update label="v1.37937.3" description="2026-08-26">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.37937.2" description="2026-08-26">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.37937.1" description="2026-08-25">
  **General**

  * Updated the bundled Claude Code CLI to version 2.1.246.

  **Code**

  * Fixed remote MCP servers never recovering after a dropped connection; they now reconnect automatically or report as failed.
  * Fixed signing in to some MCP servers, such as Linear, failing with an "Invalid redirect URI" error.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Added support for the `inferenceModelPricing` rates and the `inferenceModelPricingMultiplier` discount in the Usage page's cost estimate; in 1.37937.0 the estimate always used Anthropic list price.
</Update>

<Update label="v1.37937.0" description="2026-08-25">
  **General**

  * Added support for legacy Word .doc files, which now open like .docx, and Excel .xlsx and .xls spreadsheets, which now attach as text where they used to be refused.
  * Removed sharing of chat artifacts for members of organizations whose admin has turned Artifacts off; links already shared keep working.
  * Fixed chat refusing new messages after the weekly Cowork limit was used up.
  * Fixed scheduled tasks set to run on both a day of the month and a weekday (for example "the 1st and every Monday") only running when the two coincided; they now run on either day, as their schedule description says.
  * Fixed several chat reliability issues: queued messages could disappear or send on their own, a send retried during a service overload could add repeated copies of a message, reopening a chat before the reply arrived could show a false "message wasn't sent" error, and a single failed response could show two error messages.
  * Fixed the app sometimes signing you out right after an automatic update.

  **Code**

  * Improved SSH session reliability: fixed connections failing when the configured identity file is a public key (common with 1Password setups), messages sent while the host reconnects are delivered once it is back, a Claude Code upload to the host now rides out a brief network pause, idle sessions no longer show a false "Lost connection" card, reconnecting can ask for a password or one-time code when needed, and a reconnect no longer reports lost output unless it truly could not be recovered.
  * Fixed all saved SSH connections disappearing when one stored connection entry was invalid.
  * Fixed background cleanup of old session worktrees on Windows sometimes also deleting the contents of folders that NTFS junctions inside the worktree pointed to, such as the main checkout's `node_modules`.
  * Fixed removing a claude.ai import run resetting uncommitted work in a session you had started from that import; the session's files are now kept on disk.
  * Fixed sessions failing to start for organizations using the `disableSideloadFlags` setting in Claude Code's `managed-settings.json`; sessions now start without the desktop's bundled skills and plugins instead.
  * Fixed very high memory use, and a blank or unresponsive window, when opening or reconnecting sessions with very large transcripts or many subagents.

  **Cowork**

  * Added dictation in the Claude in Chrome side panel; allow the microphone once in the extension's settings.
  * Fixed "upload failed" errors when staging Google Drive and other cloud-synced files that are not downloaded on your Mac yet; they now download automatically, and clearer messages explain when the sync app needs to be started.
  * Fixed a Rename, Delete, or Move dialog left open in a task's header staying open when you switched to another task and acting on the task you switched to; it now closes on switch.
  * Fixed only the last file staying attached when several files opened with Claude each needed confirmation.
  * Fixed restored Cowork tabs showing a "Try again" error when the app restarted before sessions finished loading, such as right after an update.
  * Fixed the tasks and files panel staying open as an empty pane after a restart.

  **3P**

  * Added `mcpToolTimeoutSec`, which sets how long an MCP tool call may run before it times out. Defaults to 180 seconds.
  * Added `organizationInstructions`: organization-wide instructions appended to Claude's system prompt in Chat, Cowork, and Code sessions (up to 3,000 characters); settable via device management, a local configuration file, or the bootstrap response. They are guidance the model follows, not an enforced control.
  * Added `skipWebFetchPreflight`. When enabled, Code sessions no longer contact api.anthropic.com before fetching a web page, which fixes page fetches failing on networks that block that host. Off by default.
  * Added `userPluginMarketplacesEnabled` and `userPluginUploadsEnabled`, which control whether members can add their own plugin marketplaces and upload their own plugins; when off, the add options are hidden and adds are refused. Unset keys change nothing.
  * Added Code tab features already available in the standard app: the Files panel with Show in Files, emoji autocomplete and inline prompt suggestions in the composer, interactive MCP app widgets in the conversation, and letting Claude read output from the integrated terminal panel.
  * Added cost estimates to the Usage page: `inferenceModelPricingEnabled` shows an estimated cost alongside token counts, priced at Anthropic list price; `inferenceModelPricing` supplies per-model rates and `inferenceModelPricingMultiplier` scales every estimate (a number between 0 and 1). The two rate keys take effect from 1.37937.1; in 1.37937.0 estimates use list price. Off by default.
  * Added suggestions for plugins and skills from your organization's own library in chat.
  * Added support for plugin marketplace credential helpers that return a username or `authtype=Bearer`, so marketplaces hosted on Bitbucket Data Center or behind GitLab deploy tokens can authenticate.
  * Added the `disableDesktopLocalSessions` setting to Claude Code's `managed-settings.json`, which turns off Code sessions that run on the device itself so the Code tab offers only remote environments such as SSH; the environment menu shows Local greyed out with a "Disabled by your organization" explanation.
  * Changed `allowedPluginMarketplaces` (beta): a `url` marketplace hosted on the bootstrap server's own origin can now use `credentialKind: "inferenceCredential"` and is fetched with the same sign-in the app already uses for its bootstrap configuration.
  * Changed `builtinToolPolicy` to accept argument-scoped Claude Code permission rules such as `Bash(curl *)` in addition to bare tool names; `WebSearch` and `WebFetch` entries stay bare tool names, and entries that are not usable rules are rejected with a configuration error.
  * Changed gateway device-code sign-in to show the signed-in account's email, when the gateway returns one, instead of the computer's login name.
  * Changed the Code tab's file pane and git panel to follow the administrator's `allowedWorkspaceFolders` setting.
  * Fixed Bedrock sessions behind a proxy that strips the response content type silently re-running every request without streaming, which billed each request twice.
  * Fixed Cowork scheduled tasks running on the 200K-context model when the 1M-context row or "Default model" was selected in the task form; the form now labels the 1M row.
  * Fixed the built-in Microsoft 365 connector publishing an invalid schema for updating a calendar event's end time.
  * Fixed the Microsoft 365 local connector on Windows failing for users with more than one Microsoft work account on the PC. The Reconnect card now opens the Windows account picker and the chosen account is remembered; users of this connector will be asked to reconnect once after this update.
  * Fixed the model picker showing a duplicate, mislabeled 1M-context row when `inferenceModels` lists a model both with and without the `[1m]` suffix.
</Update>

<Update label="v1.34493.1" description="2026-08-21">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Fixed prompt caching not being applied in sessions that use an inference gateway or custom endpoint.
</Update>

<Update label="v1.34493.0" description="2026-08-20">
  **General**

  * Fixed a startup freeze on Macs that keep applications in iCloud Drive with Optimize Mac Storage turned on.
  * Fixed scheduled task problems: "every N days/months" schedules ran on the wrong days (existing tasks move to the correct days on their next run), re-enabling a task or editing its schedule immediately started a catch-up run for a time slot that passed while it was off, and manually run tasks sometimes did not record when they last ran.
  * Fixed the app crashing when signing in with Touch ID on macOS; Touch ID passkey sign-in is temporarily unavailable.
  * Fixed the app quitting on macOS when the disk was full or when stopping dictation.

  **Code**

  * Fixed archiving an SSH session discarding uncommitted or unmerged work in its remote worktree; the worktree is now kept, and unarchiving recreates it if it is missing so the session can pick up where it left off.
  * Fixed session history no longer updating or appearing lost on macOS for sessions in folders whose names contain accented, Korean, or Japanese characters.
  * Fixed sessions you hadn't opened for 30 days or more losing their conversation history even though the app was in regular use.
  * Fixed SSH connections on slow or unstable networks failing on the first attempt and needing a manual retry.
  * Fixed SSH sessions losing a task that was still running when the app reconnected after an app update.
  * Fixed the side chat answering once and then failing with an authentication error for the rest of a long session.

  **Cowork**

  * Fixed conversations failing to open when a message contained a very long run of bracketed text, a very long line starting with an unclosed `[`, or a very long run of `>` characters.
  * Fixed message ratings and "Send feedback" links sometimes appearing when your organization has product feedback turned off.
  * Fixed sessions failing to start on managed Macs where the app's temporary directory is not writable.

  **3P**

  * Changed gateway device-code sign-in to refresh silently when the gateway also issues a refresh token, instead of prompting you to sign in again each time the access token expires.
  * Fixed an ended gateway device-code sign-in going unnoticed while the app was idle; the app now notices at its next periodic configuration check or shortly after the computer wakes from sleep and asks you to sign in again, and the Setup window says "Session expired" instead of "Denied".
  * Fixed Cowork file previews showing "Preview unavailable" until the app was restarted once a preview pane had been closed for a few minutes.
</Update>

<Update label="v1.32885.1" description="2026-08-18">
  **General**

  * Added message queueing during Research: a message sent while a Research run is in progress is queued and sent when the report is ready.
  * Fixed 1Password credential requests failing when Claude in Chrome is signed in from more than one browser profile.
  * Fixed a crash on Windows when installing an update while a background update check was still running, and fixed update installs repeatedly failing after a newer update replaced one already staged.
  * Fixed a message sent immediately after stopping a reply sometimes being put back into the input box instead of sending.
  * Fixed reloading or reopening a temporary chat rebuilding the page a moment after it loads, which could discard text typed early.
  * Fixed the computer-use permission prompts in Cowork and Claude Code sessions accepting a keyboard shortcut aimed at the message box or another surface, and added a brief delay so a send keystroke that lands just as the prompt appears cannot approve it.

  **Code**

  * Fixed automatic continuation after a rate limit firing into the imported-session confirmation prompt or a stale sign-in state, and it now waits out the server's limit reset and sends a clearer continuation message.
  * Fixed inline bash commands being silently captured as input by a previous command still waiting for a response, such as an interactive login; a stuck command is now noted in the transcript and cleared before the next command runs.
  * Fixed messages sent from one session to another sometimes being silently dropped, which left the sending session showing a thinking state for many minutes.
  * Fixed slow session starts for people with MCP servers configured in `~/.claude.json`.
  * Fixed the Code tab wrongly asking you to install Git on Macs that have Apple's Command Line Tools but not Xcode.
  * Fixed worktree sessions failing with a "path contains control characters" error when a `WorktreeCreate` hook prints status output before the path.

  **Cowork**

  * Fixed an occasional "Something went wrong" error when a session's question card from Claude changed to a new set of questions.
  * Fixed Claude sometimes reporting a file as saved when it had been written to a temporary location you could not open.
  * Fixed Cowork failing to start on Intel Macs.

  **3P**

  * Added `bootstrapHeaders` and `bootstrapHeadersHelper` for authenticating the bootstrap configuration fetch with a service-account credential, the supported replacement for embedding `user:password@` in `bootstrapUrl` (rejected since 1.32352.0): `bootstrapHeaders` is a set of static headers sent on every fetch, and `bootstrapHeadersHelper` is the absolute path of an executable that prints headers as JSON, for a rotating token; helper output is merged over the static headers. When either is set and no `bootstrapOidc` provider is configured, the headers count as sufficient authentication for the fetch and no per-user sign-in is required for it; a per-user sign-in bearer, when also present, still wins on `Authorization`. Header values are masked in diagnostics, and both keys are accepted only from device management or a local configuration file.
  * Added the option to sign in to claude.ai directly from the import wizard to fetch your data export, with no manual zip download needed.
  * Changed new Cowork sessions to store Claude Code transcripts under a short fixed folder name, now that the bundled Claude Code (2.1.234) supports it, further shortening file paths on Windows; existing sessions are unchanged.
  * Changed organization plugin delivery: when the organization plugins endpoint is removed from your configuration, the plugins it had installed are removed from members' devices, as already happens for a removed plugin marketplace.
  * Fixed admin-configured plugin marketplaces and organization plugins not re-syncing until the next periodic refresh after signing in or after a delayed configuration fetch applied.
</Update>

<Update label="v1.32352.1" description="2026-08-18">
  **General**

  * Fixed a rare Windows startup failure where the first window could fail to initialize on a fresh install.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.32352.0" description="2026-08-17">
  **General**

  * Fixed Windows updates sometimes leaving the app half installed, with later updates failing too.
  * Fixed the app staying on "Couldn't connect to Claude" when a network proxy blocked its first connection; it now keeps retrying for a few minutes and again when you return to the window.
  * Fixed the composer staying disabled after a usage-limit notice when your organization has extra usage turned off or not set up; sending works again once your admin turns it on.
  * Fixed settings and connector links in chat doing nothing, or opening your web browser, when clicked in the app; they now open the app's own settings.
  * Fixed text typed on the new chat page sometimes disappearing when turning on incognito.
  * Fixed the chat showing an error screen instead of the conversation when Claude created or linked a file whose name contains a percent sign.

  **Code**

  * Changed auto-continue after the 5-hour usage limit to be on by default: sessions left open resume when the limit resets. Uncheck "Auto-continue when limits reset" in the limit banner to turn it off for your account.
  * Fixed sessions sometimes hanging after resume, either showing "The session stopped responding" after the first message or never starting when a file system or MCP server stalled.
  * Fixed undo (Cmd+Z, or Ctrl+Z on Windows and Linux) in the message composer sometimes failing with an error and then no longer working.
  * Fixed a brand-new cloud session losing its first message when you navigated away within a few seconds of sending it.
  * Fixed sessions started right after the app opened sometimes running in a more permissive mode than your saved permission mode.
  * Fixed Remote Control sessions staying stuck at "connecting" after you completed the sign-in or device-check prompt, and file links not opening when the session was viewed from another computer.

  **Cowork**

  * Removed the "Allow all browser actions" option from Claude in Chrome permission cards; allow each website instead. The switch in Settings is unchanged.
  * Fixed the workspace startup error suggesting a restart or reinstall when the computer was low on disk space; it now asks you to free up space and retry.
  * Fixed a tool call hanging for a full minute when its local MCP server crashed mid-call; it now fails right away.
  * Fixed computer use on macOS refusing every click after you had taken a screenshot or while a screen recording was running.
  * Fixed the approval mode still showing "Skip all approvals" when your organization's policy had blocked it; switching back to "Manually approve" now asks again before Claude fetches web pages it visited while approvals were off.
  * Fixed the activity panel button doing nothing while a file was open beside the chat; it now closes the file and shows the panel.

  **3P**

  * **Breaking:** Managed-config URL settings now reject values that embed credentials (`https://user:password@host…`). Configurations that relied on this fail to load until the credentials are removed; use `bootstrapHeaders` / `bootstrapHeadersHelper` (available from 1.32885.1) to send authentication instead.
  * Added `claudeAiImport.exportEnabled`. With it and `claudeAiImport.enabled` both `true`, users can export this computer's chats, Cowork tasks, and Code sessions from Settings > Import & export as a zip that another install can import. Off by default.
  * Added a `url` source for `allowedPluginMarketplaces` (beta): a hosted `marketplace.json` that delivers plugins as zip archives over HTTPS, with no git on the device. Set `manifestSha256` to pin the exact manifest; it is required for automatically installed plugins.
  * Added `inferenceCredential` as a `credentialKind` for `allowedPluginMarketplaces` (beta): a `url` marketplace hosted on your inference gateway is fetched with the same credential the app already uses for inference.
  * Changed `coworkEgressAllowedHosts`: a `:port` suffix now also applies to shell commands and package installs in Cowork sessions, which previously could not reach a port-scoped host at all.
  * Changed settings from a locally configured (not device-managed) bootstrap URL that need user approval to apply all or nothing: nothing takes effect until the user chooses Allow; Quit closes the app and asks again next launch.
  * Changed a served configuration with an invalid connection value to report that field by name and keep the organization's other settings in force; a non-Anthropic model entry is now skipped with a warning instead of invalidating the whole configuration.
  * Changed admin-configured plugin marketplaces (`allowedPluginMarketplaces`, beta), including automatically installed and required plugins, to apply to Code sessions as well as Cowork.
  * Changed new Cowork sessions to use much shorter folder names on disk so file paths are less likely to exceed Windows path-length limits; existing sessions keep their folders, and tooling that matches the `local_` prefix should also match the new names.
  * Fixed Settings > Import & export saying import isn't enabled on deployments that provision the sign-in import without setting `claudeAiImport.enabled`; that key now governs only file and earlier-session import, the import prompt, and session export.
  * Fixed the Setup window accepting a mis-typed inference region, Azure AI Foundry resource name, blank Vertex AI project ID, or non-Anthropic model ID that was only rejected later on the device; these are now flagged before saving.
  * Fixed imported project instructions arriving as a loose file instead of the project's editable Instructions; they are now shown for review on the project page and apply once you accept them.
</Update>

<Update label="v1.30096.5" description="2026-08-14">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.30096.1" description="2026-08-13">
  **General**

  * Fixed Find (Cmd+F) doing nothing the first time it was pressed after launch.
  * Fixed right-to-left text in the composer scrambling around embedded left-to-right words; code blocks stay left-to-right.
  * Fixed the Artifacts entry missing from the sidebar on Windows machines that can't run local Cowork; it now opens the Artifacts gallery.
  * Fixed macOS asking for notification permission as soon as the app launched, instead of when the first notification is about to appear.
  * Fixed the app crashing at launch, or on a system theme change, on some Linux installs (most often repackaged builds); it now falls back to a default tray icon.

  **Code**

  * Added Rewind to cloud sessions (message menu, Esc Esc, or `/rewind`), and fixed rewound-away messages reappearing when a rewound cloud or Remote Control session was reopened.
  * Fixed an interrupted Claude Code download (for example, after a crash or power loss mid-install) leaving Code sessions on that computer unable to start, most often on Windows.
  * Fixed an unanswered permission or plan-approval prompt in a cloud session sometimes being treated as approved after the session's environment disconnected.
  * Fixed cloud sessions marked as needing input sometimes opening without the question or approval prompt.
  * Fixed Remote Control sessions sometimes never connecting when opened while idle, staying off your other devices after a stop or interruption until turned back on by hand, and looking idle instead of reporting that the host computer is offline.
  * Fixed copy and paste problems: transcript text pasted into rich-text apps lost the spaces around inline code, bold, and italics and mangled code blocks, and Cmd+C after selecting text in the Plan view copied nothing.

  **Cowork**

  * Fixed the earlier conversation being discarded when you chose Go back after a failed task resume, or edited a message right after the app restarted.
  * Fixed memory saves failing when the Claude Code `managed-settings.json` policy sets `allowManagedPermissionRulesOnly`.
  * Fixed Cowork on Windows failing on every launch with "VM service not running" after its background service had stopped; the service is now restarted automatically, and otherwise the error explains that restarting the computer restores it.
  * Fixed Cowork sometimes pulling you back to the bottom of a task after you had scrolled up, for example when a sub-agent step finished.

  **3P**

  * Added `otlpAuthMode` and `otlpHeadersHelper`, two ways to authenticate telemetry exports without static `otlpHeaders`: set `otlpAuthMode` to `inference-credential` to reuse the signed-in user's inference token, or point `otlpHeadersHelper` at an executable that prints the collector headers as JSON.
  * Added an optional `inferenceGatewayOidc.resource` subfield that sends an RFC 8707 resource indicator on gateway sign-in and token refresh, for identity providers that audience-restrict access tokens.
  * Changed `inferenceBedrockBaseUrl` and `inferenceVertexBaseUrl`: only affects users who entered the bootstrap server URL themselves (in Settings or a local config file). Those users are now asked once to allow a Bedrock or Vertex endpoint that server delivers before it takes effect, the same prompt `inferenceGatewayBaseUrl` already shows. Managed deployments (bootstrap URL set by device management, or `trustBootstrapDelivery: true`) see no change.
  * Changed `claudeAiImport`: an imported session now asks the user to confirm once (Trust and resume) before Claude continues it for the first time; this also applies to sessions imported before this update.
  * Fixed a single malformed `allowedPluginMarketplaces` (beta) entry disabling every configured marketplace; the entry is now skipped and reported.
  * Fixed sending messages failing when a bootstrap server turned Cowork off (`coworkTabEnabled` set to `false`); the home screen now opens directly into Chat.
  * Fixed OpenTelemetry exports being rejected when the configured gateway also serves as the telemetry collector endpoint.
</Update>

<Update label="v1.28929.0" description="2026-08-11">
  **General**

  * Added the standard macOS full-screen keyboard shortcut, with an Enter Full Screen and Exit Full Screen item in the View menu.
  * Fixed a startup error on some Linux systems, most often repackaged or containerized installs, that left the app without a tray icon and recurred on every system theme change.
  * Fixed commands in the built-in terminal failing with error -1743 when controlling other apps on macOS, instead of showing the Automation permission prompt.
  * Fixed sign-in on macOS repeatedly failing with "Failed to login, it may have been cancelled"; Claude now opens the sign-in page in your default browser when the system sign-in sheet is unavailable.
  * Fixed some Windows installs (MSIX packages and enterprise-managed roaming profiles) failing to save chat history, settings, and scheduled tasks, and Cowork failing to start with "Download failed" after an app update.
  * Fixed the app's memory use growing without bound during long-running sessions.

  **Code**

  * Removed the ability for scheduled-task runs and other unattended sessions to start dev servers in the Browser preview; other sessions now approve each distinct dev server command once rather than on every start.
  * Fixed app settings, and the app's record of session worktrees, being discarded when those files had been re-saved with a UTF-8 byte-order mark by an external editor.
  * Fixed forked sessions starting from the original base branch instead of the parent session's current branch.
  * Fixed importing Claude Code CLI sessions changing the order of existing sessions in `claude --resume`.
  * Fixed sessions failing to resume, reporting their conversation history as missing, after Claude had moved the session into a worktree.
  * Fixed file uploads through Claude in Chrome from a Code session failing with "Invalid arguments for tool file\_upload".

  **Cowork**

  * Fixed a follow-up message sent while Claude was still writing a reply sometimes being dropped, with the reply cut off.

  **3P**

  * Added history import. When `claudeAiImport.enabled` is `true`, users can bring a Claude.ai data export, Cowork, Code, and Chat sessions from other Claude installs on the same computer or from an app data folder they choose, and terminal Claude Code sessions into the app from Settings > Import. `claudeAiImport.bannerBehavior` controls an optional banner on new tasks that offers it: `off` (default), `detect` (only when earlier sessions are found on the computer), or `show` (everyone, until dismissed or imported).
  * Added `modelPrefer1mContext`. When `true`, a user who has not yet chosen a model starts on the 1M-context variant of the default model whenever the deployment marks or reports that model as 1M-capable, including auto-discovered models. Saved selections are never changed. Defaults to `false`.
  * Added the gateway address, `inferenceGatewayBaseUrl`, to the one-time bootstrap consent prompt. When a bootstrap server delivers it and the bootstrap URL was not set through device management, each user is asked once at launch to allow the address, and again if it later changes; the app does not connect to the gateway until they choose Allow. Existing installs prompt the first time they start this version. Set `trustBootstrapDelivery` to `true` in your device-management profile or local configuration file to accept it for everyone in advance.
  * Changed the Code tab to be hidden entirely, rather than shown greyed out, when an administrator has disabled Code.
  * Fixed a session opened in a new window on Windows having no title bar, window controls, or drag area.
  * Fixed stored sign-ins being lost when the system keychain was temporarily locked.
  * Fixed the Chat tab ignoring `toolSearchEnabled`, which sent every connector's tool definitions with each request and could exceed the context window when many connectors were configured; Chat now loads them on demand when the key is `true`, as Cowork and Code do.
  * Fixed the credential-expired notice and the session error banners in Cowork and Code offering no way to sign in again when the credential comes from a helper script (`inferenceCredentialHelper`); they now show "Sign in again", which re-runs the helper.
  * Fixed the model picker reverting to the standard-context variant in new sessions, after relaunch, and when switching between Chat and Cowork once the 1M-context variant had been chosen.
</Update>

<Update label="v1.26832.0" description="2026-08-06">
  **General**

  * Added a "Start a new project" option to the "Add to project" menu, which opens the create-project dialog.
  * Added Esc as a way to end voice mode in the chat composer.
  * Added the ability to add suggested skills in local sessions, and plugins from your personal marketplaces, directly from their suggestion cards.
  * Fixed Claude Desktop on Linux entering a crash-and-relaunch loop that consumed heavy processor time when automatic session restore ran into persistent graphics failures.
  * Fixed starting a chat inside a project showing a blank screen until the response finished, and leaving the chat without its project name or title.
  * Fixed the scheduled-task prompt editor not being announced to screen readers as a labeled multiline text box.

  **Code**

  * Added session-window restore: Claude Code session windows that were open when you quit now reopen the next time you launch the app.
  * Changed permission-mode picks so they apply to the folder where you made them instead of becoming a machine-wide default.
  * Removed the "Always allow" option when approving dev server starts in the Browser preview; each new server start now asks, and a server that has crashed asks again instead of restarting silently.
  * Fixed "Try again" on session-error cards sometimes doing nothing, and a failed send's retry card and prompt text now survive an app relaunch.
  * Fixed leftover session workspaces building up on disk until new sessions could fail with a disk-space error.
  * Fixed repository pickers in project settings and scheduled tasks timing out or omitting repositories in large organizations; they now load quickly, can search every repository, and can load more results.

  **Cowork**

  * Added a ⋮ menu to scheduled tasks in the sidebar, including Mark as unread for the latest run.
  * Added a confirmation before a link in a live artifact opens in your browser, with a per-site "Don't ask again" option.

  **3P**

  * Added `updateViaUpdatesHost`. Set it to `true` to read the update feed from `releases.claude.com`, a host that serves only the desktop update check and carries no model API, so networks that block `api.anthropic.com` can still receive updates. Installer downloads continue to come from `downloads.claude.ai`. Defaults to `false`.
  * Added an access mode to each `allowedWorkspaceFolders` entry. Set `mode` to `ro` to let Claude read and search a folder without changing it: in Cowork, writes are blocked and Claude is directed to put modified copies in the session outputs folder. In the Code tab this covers Claude's file tools only; Bash in the Code tab and SSH sessions do not yet enforce it. Entries without `mode` stay read-write, so existing configurations are unchanged.
  * Added optional `:port` suffixes to `coworkEgressAllowedHosts` entries, for example `internal.corp.com:8443` or `*.corp.com:8443`, restricting that entry to the named port. This applies to the sandbox's web fetch now, and to shell egress once the updated virtual machine image ships; on the Code tab, a port-scoped entry is treated as its bare host (any port). Entries without a port keep allowing any port, and an invalid entry is dropped on its own with a warning in the logs.
  * Added settings that decide where users sign in for inference to the one-time bootstrap consent prompt: the Azure AI Foundry Entra tenant and client, Bedrock IAM Identity Center, the Vertex OAuth client and workforce identity, and gateway OIDC. Set `trustBootstrapDelivery` to `true` in your device-management profile to accept these for everyone in advance.
  * Added the merged Chat and Cowork home as the default. The "New" button starts a chat or a task from one composer, and the sidebar shows Home, which lists chats and tasks together, alongside Code.
  * Changed the `trustBootstrapLocalExec` key name to `trustBootstrapDelivery`, reflecting that it now covers sign-in targets as well as helper scripts and connectors. The previous name continues to work in existing profiles.
  * Fixed chats started inside a Project not picking up the Project's Instructions and Context links, including reading the files linked there.
  * Fixed Code sessions on a custom gateway endpoint ending with an idle-timeout error while the gateway was still sending keep-alive responses.
  * Fixed Code tab sessions on gateway and direct API key deployments still sending nonessential traffic to `api.anthropic.com` after an administrator turned off nonessential telemetry.
  * Fixed model selections provided by your deployment being overridden by an out-of-date Claude Code `managed-settings.json` left on the device.
  * Fixed the published `bootstrap-config-v2.schema.json` describing flat keys instead of the nested shape the app's own configuration export uses.
</Update>

<Update label="v1.25927.0" description="2026-08-04">
  **General**

  * Added a chevron next to the composer's microphone button that switches between dictation and voice mode and keeps your choice; clicking the microphone now starts dictation right away.
  * Fixed `⌘K` (or `Ctrl+K` on Windows and Linux) search missing results from tool output and archived sessions.
  * Fixed a crash on macOS during passkey and Touch ID prompts when the system language is German, Spanish, French, Hindi, Indonesian, Italian, Japanese, or Korean.
  * Fixed automatic and menu-triggered update restarts interrupting an in-progress Claude Code or Cowork task.
  * Fixed the app being left with no usable window: a failure during startup now shows an error dialog and records the details to a file, and a window the system shut down under low memory reloads instead of staying blank.

  **Code**

  * Added automatic resume for sessions interrupted when your computer goes to sleep. A banner with a manual Continue button appears only when resuming isn't safe, and you can continue the session in the cloud instead.
  * Added capture and annotation for the page the Browser pane is showing, including external sites, so you can mark up what you see and attach the image to chat.
  * Fixed a crash while using the in-app browser on pages with heavy console or network activity.
  * Fixed messages sent while Claude was working disappearing from a session after it was reloaded from disk.
  * Fixed sessions sometimes becoming permanently unopenable, showing "No messages yet" while their conversation history was still on disk.
  * Fixed starting a session and swapping repositories stalling in organizations with very large repository lists: the pickers now load repositories page by page, find the rest as you type, say when more are available by searching, and report a failed search instead of showing empty results.

  **Cowork**

  * Added pasted and attached images to the session's uploads folder, so Claude can open and edit the actual file.
  * Fixed "Allow for this task" not appearing for connector tools when your organization has turned off persistent "Always allow".
  * Fixed documents showing an internal file id instead of their title, including in export filenames and approval prompts.
  * Fixed long-running workspace shell commands, such as large database queries, being cut off too early.
  * Fixed scheduled task problems: a cron expression using `7` for Sunday never ran, stalled runs kept running in the background until the app was restarted, and "Allow for all scheduled runs" appeared on prompts where the choice could not be saved, so the task asked again on every run.

  **3P**

  * Added Projects for organizing Chat conversations: create a project, start a chat inside it, or move existing chats in. Projects stays available even when your administrator has turned the Cowork tab off.
  * Added `inferenceGatewayOidcAuthFlow` and `inferenceVertexWorkforceAuthFlow`, which choose whether identity-provider sign-in for gateway and Vertex workforce-identity credentials runs in the system browser (the default) or through the operating system's Microsoft account broker on Windows and macOS, so sign-in can satisfy Conditional Access policies that require a managed device.
  * Added `managedMcpServers[].oauth.authFlow`, which lets a managed connector sign in through the operating system's Microsoft Entra account broker on Windows and macOS, so Conditional Access policies that require a managed device no longer block it. Devices without a broker keep using browser sign-in.
  * Added `skillCreationEnabled`, which controls whether users can create and upload their own skills. It defaults to on; setting it to `false` hides the creation and upload surfaces and turns off Claude's skill-creation tools. It appears in the Setup window under workspace restrictions.
  * Added `trustBootstrapLocalExec`. Each user is now asked once for consent when the bootstrap configuration includes settings that run local commands, such as credential helpers and local connectors. Set this key to `true` to accept them for everyone in advance. It defaults to `false` and is accepted only from MDM or a local configuration file.
  * Added a built-in GitHub connector to `managedMcpServers`: set `server` to `github` and supply your own GitHub OAuth app client ID with the device flow enabled. The new `host`, `toolsets`, and `readOnly` subfields point the connector at a GitHub Enterprise Server instance, choose which toolsets load, and offer read tools only. The connector is also configurable from the Setup window.
  * Added support for mounting Windows mapped network drives into the Cowork sandbox, so shell commands and document processing can work with files on network drives, and fixed adding a mapped network-drive folder mid-session being rejected with a message to use the folder picker.
  * (breaking) Changed the nested v2 bootstrap response: `deploymentDisplayName` and `deploymentDisplaySubtitle` now sit under `appearance`, and `endUserAttribution` and `userContentRendererUrl` under `workspace`. The flat MDM key names are unchanged.
  * Changed `managedMcpServers` and `microsoftAuthBroker` to be supported on standard deployments as well, so an administrator can enable the built-in Microsoft 365 connector by adding it to `managedMcpServers` through MDM. It stays off unless configured.
  * Changed where several keys can be delivered from: `claudeAiImport`, `deploymentDisplayName`, and `deploymentDisplaySubtitle` now accept values from MDM and a local configuration file as well as a bootstrap server, and `disableDeepLinkRegistration`, `microsoftAuthBroker`, `userContentRendererUrl`, `inferenceFoundryTenantId`, `inferenceFoundryClientId`, `inferenceCredentialHelper` (with its TTL, timeout, and silent-refresh keys), `inferenceBedrockProfile`, `inferenceBedrockAwsDir`, `inferenceBedrockAwsCliPath`, and `inferenceVertexCredentialsFile` can now be delivered by a bootstrap server. The keys that name a local executable go through the consent prompt above.
  * Deprecated `organizationPluginsUrl` and removed it from the configuration reference. The key is still honored, but organization plugins are better configured with `allowedPluginMarketplaces`.
  * Updated `enduserAttribution` to the corrected spelling `endUserAttribution`. The previous spelling is still accepted and now records a configuration warning.
  * Fixed connector sign-in recovery: connectors no longer ask you to sign in again after a slow startup when the credentials are still valid, and the GitHub connector shows its Reconnect card on the next tool call after its token is revoked on github.com instead of staying stuck.
  * Fixed tasks failing with "Couldn't start this task" for the rest of the session when the app launched while the network or the sign-in credential was unavailable.
  * Fixed the app losing administrator-enabled features, such as the Chat tab, for the rest of the session when the organization's configuration server was unreachable at launch. It now retries in the background and recovers.
  * Fixed the home composer and sidebar still offering Cowork when an administrator has turned the Cowork tab off; Cowork is now hidden instead of greyed out, while Chat and Projects remain available.
</Update>

<Update label="v1.24012.11" description="2026-08-03">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Fixed sessions started while configured MCP servers were still connecting having no connector tools until a new conversation was started.
  * Fixed the Microsoft 365 connector not appearing after first-time sign-in until the app was restarted.
</Update>

<Update label="v1.24012.9" description="2026-07-24">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * Fixed plugin hooks silently doing nothing on Windows.

  **3P**

  * Added the `mcpPersistentAlwaysAllowEnabled` managed configuration key, letting admins disable the persistent "Always allow" approvals for MCP tools while keeping session-scoped approvals available.
  * Added the five-level effort selector for Claude Opus 5 in the model picker. Extended thinking is always on for Opus 5.
</Update>

<Update label="v1.24012.0" description="2026-07-21">
  **General**

  * Added an option to keep custom plugin marketplaces up to date automatically, and fixed a marketplace refresh reporting success before the sync ran and re-adding an existing marketplace not refreshing its contents.
  * Improved keyboard and screen reader support across the app: settings tabs and share-visibility choices respond to arrow keys, dialogs announce meaningful titles, decorative graphics no longer clutter screen reader output, and the find bar, search fields, and pane resize handles show a visible focus outline and announce their size.
  * Fixed failed uploads being reported as corrupted or unsupported files, and retries showing a "Server is busy" message for unrelated errors.
  * Fixed safety-block notices suggesting you switch models when no alternative model was available for that topic.
  * Fixed the app failing to launch when its settings file or logs folder was corrupted, and saved sessions disappearing after a relaunch when one session's stored data was invalid.
  * Fixed the app window resizing abruptly and losing its saved size and position when signing in or out; it now animates smoothly in place.

  **Code**

  * Added iOS Simulator support: Claude Code can build your iOS app, launch the simulator, and verify the result without leaving the session.
  * Added iOS Simulator and Android Emulator buttons to the session titlebar when the agent launches an app on a device, so the pane is one click to reopen.
  * Added Pause Project, which pauses a project's coordinator and new session spawning from settings and shows a Resume banner above the composer.
  * Added screenshot annotation in the composer: click a staged image, open the pencil, and draw with pen, shapes, text, and colors before sending.
  * Improved how large sessions open: the newest messages paint first while older history loads in the background.
  * Fixed Code sessions affecting the wrong files: background worktree cleanup could switch or reset the main repository checkout when a worktree folder was only partially removed, and new sessions could copy uncommitted files from the original folder.
  * Fixed session list problems: finished sessions still showing as running, deleted sessions reappearing as empty "Session not found on disk" entries after an update, archived sessions still appearing active on claude.ai and other devices, and sessions started from claude.ai missing Rename, Archive, and Delete in the sidebar menu.
  * Fixed the app freezing when Claude Code updated its configuration file during concurrent use, and web pages in the Browser pane freezing the app with alert and confirm dialogs.

  **Cowork**

  * Added /usage and /cost to Cowork tasks: an inline card shows your plan limits and the session's usage without sending anything to the model.
  * Improved background computer use so it types faster and no longer leaves menus stuck open on screen.
  * Updated folder access prompts for cloud Cowork tasks to note that files Claude uses leave your device and are processed on Anthropic's servers.
  * Fixed changes to Instructions for Claude sometimes not applying to new sessions, and edits reverting to an earlier version while a session was running, including after an app restart.
  * Fixed Cowork workspace problems: the Windows workspace failing to start when its virtual disk files were compressed, a backgrounded shell command leaving a session stuck reporting "already running", and bash commands failing when several subtasks ran them at once.
  * Fixed the message input staying stuck in a sending state when a folder access dialog went unanswered.

  **3P**

  * Added `deploymentDisplayName` and `deploymentDisplaySubtitle` to customize the deployment name and an optional subtitle shown in the account menu and sidebar.
  * Added `enduserAttribution`, which shows the signed-in user's identity in the sidebar, account menu, and Code tab, and includes it as the OpenTelemetry `enduser.id` attribute on telemetry sent to your configured collector. Administrators can turn it off, and an existing static `enduser.id` is kept.
  * Added `oauth.authorizationUrl` and `oauth.tokenUrl` to managed MCP servers for identity providers that do not serve a discovery document, and `oauth.additionalRedirectReferrerHosts` to allow sign-in callbacks from hosts other than the authorization URL's.
  * Added `userContentRendererUrl`, which sets the HTTPS origin that renders artifact and file previews; leave it unset to use the default Anthropic-hosted renderer.
  * Added a `broker` option to `inferenceFoundryAuthFlow` that signs in to Azure AI Foundry through the operating system's native account broker on Windows or Company Portal on macOS, so sign-in can satisfy Conditional Access policies that require a compliant device. Windows and macOS only.
  * Added a Usage page in Settings for custom deployments, showing token usage across Chat, Cowork, and Code.
  * Added Microsoft 365 Teams tools (send to a chat, channel, or thread; create a chat; @mention people) and formatted-body support for Outlook reply drafts.
  * Added the 1M context option in the model picker for gateway-discovered models that report the capability in `/v1/models`, without requiring an `inferenceModels` entry.
  * Changed telemetry on bootstrap-server deployments to default to disabled until the server explicitly enables it (previously only FedRAMP hosts), and added the ability to disable error and usage reporting through bootstrap configuration.
  * Fixed managed MCP connectors: a server that requires authentication now opens a sign-in window even when its configuration does not explicitly enable OAuth, and an `oauth` entry with sign-in fields but a missing or empty `clientId` is now rejected at load with a clear error instead of silently attempting automatic registration.
  * Fixed managed MCP tool policies that block all tools by default with per-tool exceptions denying the excepted tools in Claude Code sessions.
  * Fixed sessions, skills, and plugins intermittently disappearing after sign-in or configuration changes.
  * Fixed the Claude.ai sign-in option being hidden on deployments configured with a bootstrap URL; it is now hidden only when the administrator explicitly disables the deployment mode chooser.
  * Fixed the bundled Microsoft 365 connector showing only an opaque tool error when its sign-in expired; it now shows an inline Reconnect card.
  * Fixed the token-cap setup fields so the maximum tokens per window and the token cap window hours are required together; setting only one previously produced a cap that enforced nothing.
</Update>

<Update label="v1.22209.3" description="2026-07-19">
  **General**

  * Fixed sessions on Windows failing on every turn with a "Socket is closed" error when traffic passed through a corporate proxy that inspects encrypted connections, by updating the bundled Claude Code CLI to 2.1.215. Interrupted responses now retry on a fresh connection instead of ending the turn.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.22209.0" description="2026-07-16">
  **General**

  * Improved responsiveness while artifacts generate, so typing and scrolling stay smooth during generation.
  * Improved the "Add to project" menu to show only projects you can move into, with your own projects listed first.
  * Fixed rare freezes when a transcript contained very large whitespace-padded messages or tool output.
  * Fixed tool errors blaming an organization policy when a site was actually blocked by your own site permissions or settings.

  **Code**

  * Added controls for project owners to remove members from a shared project and copy an invite link from the members dialog.
  * Added per-row actions to queued messages (Edit in composer, Send now, and Remove), with right-click support.
  * Fixed a new session sometimes taking over the directory another session was still working in.
  * Fixed Code sessions hanging at startup when skill syncing was slow, and tools on your shell `PATH` staying undetected when shell environment detection timed out at startup.
  * Fixed freezes, a stuck "loading earlier messages" spinner, and blank rendering when scrolling back through very large session transcripts or when a running task's output grew very large.
  * Fixed the New session button, `⌘N` (or `Ctrl+N` on Windows and Linux), and the project header "+" discarding an unsent composer draft.

  **Cowork**

  * Improved writing drafts to consistently appear as preview cards before being staged in a connected app such as Slack.
  * Fixed documents Claude creates not reliably opening in the editor.
  * Fixed files edited by Claude sometimes reading back stale or truncated content on Windows.
  * Fixed the chat window freezing and not updating while Claude uses your computer.
  * Fixed the document editor sometimes attributing your own typing to Claude while autosaving.
  * Fixed working documents disappearing from the Documents panel after a temporary disk error.

  **3P**

  * Added `disableBrowserExternalNavigation`, which admins can set to `true` in Claude Code's `managed-settings.json` to keep the Code tab's Browser pane limited to localhost for both users and Claude. Local dev servers and file previews are unaffected.
  * Added `otlpTracesEnabled` (beta), which also exports OpenTelemetry traces from Cowork tasks and Code sessions to your configured collector.
  * Updated the allowed workspace folders policy to also apply to Code sessions on SSH hosts, evaluated against the folders on the remote host.
  * Fixed enforcement of the managed Auto mode opt-out.
  * Fixed plugins being treated as required by your organization when their marketplace name merely resolved under a required marketplace entry; only the exact entry a name resolves to now applies, so affected plugins can be uninstalled again.
  * Fixed saving a skill created in chat failing; skills now save to the app's local skill storage.
  * Fixed tools without a configured `toolPolicy` offering only Allow once and Deny; they now show the full set of approval options (Allow for this task, Allow for all tasks) and the prompt-injection warning. Explicit `ask` policies still prompt on every call.
</Update>

<Update label="v1.21459.3" description="2026-07-16">
  **General**

  * Fixed installed extensions failing to load and showing an endless loading state.

  **Code**

  * No user-facing changes.

  **Cowork**

  * Fixed a status indicator that stayed on after a conversation finished.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.21459.0" description="2026-07-14">
  **General**

  * Changed the web-fetch permission prompt to default to "Allow all for this website" when that grant is available; "Allow once" stays the default otherwise, and pressing Enter always answers "Allow once".
  * Updated the embedded Claude Code engine to the latest version.
  * Fixed a crash on launch when Claude's worktree bookkeeping file couldn't be read or written.
  * Fixed brief app freezes when opening terminals or switching sessions on Windows, and when the @ mention menu refreshed the list of open windows.
  * Fixed scheduled tasks and routines: editing a routine no longer deletes its one-time schedule, "Run now" no longer silently does nothing until the app restarts, and you can now rename routines and scheduled tasks from the edit dialog.
  * Fixed session exports that could produce an archive without the transcript; the transcript is now always included as `transcript.jsonl`, and the export shows a clear error when it can't be included.
  * Fixed the "Sign in again" prompt not appearing when a background session was blocked for session freshness, including while the desktop was idle.

  **Code**

  * Added a browser-style address bar to the preview pane, and a clear message, with the option to open the site in your browser, when a page can't be displayed instead of showing a blank page.
  * Added the ability to pin artifacts from the gallery or the artifact viewer, and to filter the gallery to your pinned artifacts.
  * Improved SSH session connection handling: messages no longer hang after the computer wakes from sleep, sessions recover from repeated disconnects, and a reconnecting indicator appears while the connection is restored.
  * Fixed `permissions.defaultMode` in Claude Code settings being ignored for new sessions after a per-folder permission mode had been chosen.
  * Fixed branch switches on large repositories failing after an uncommitted-changes stash timed out, and restored your stashed changes when a switch fails.
  * Fixed several session reliability problems: a session could get stuck showing "running" and queue new messages forever, a just-started session could disappear from the sidebar or show "session could not be found" during startup, and streamed responses could break or show a literal "undefined".

  **Cowork**

  * Added a live word count and a copy button to each document bar above the composer.
  * Changed Markdown files Claude delivers to open in the document editor instead of a plain-text preview, without flashing the old viewer first.
  * Changed the composer to keep the standard Send button while a response is running: it appears when you type, and sending mid-response queues your message instead of showing a separate Queue button.
  * Fixed Claude's mid-task replies not appearing in the conversation; they now show under a collapsed "Working notes" row.
  * Fixed screenshots from connected browsers and computer use not being saved to the task folder.
  * Fixed text typed in one conversation appearing in other conversations' composers when switching between sessions.

  **3P**

  * Added `envHelper` and `envHelperTtlSec` subfields to `managedMcpServers`, letting a managed stdio server load environment variables from an admin-provided helper executable.
  * Added an All tab to organization plugins that browses and searches every configured marketplace at once, and labeled plugins with their source marketplace so they can be filtered when more than one is configured.
  * Added support for the `eu` and `us` multi-region Vertex AI endpoints, required for the newest models with EU and US data residency.
  * Added the `disableFeatureDiscovery` key, which hides unprompted feature announcements such as the post-update "What's new" nudge and new-feature tips. Release notes remain available from the menu.
  * Fixed remote MCP connectors whose `headersHelper` mints short-lived credentials failing one token-lifetime after connecting: the helper now re-runs before expiry and the refreshed headers are applied to the live connection. The new `headersHelperRefreshBufferSec` subfield of `managedMcpServers` tunes how far ahead of expiry the refresh runs.
  * Added the `prefer1m` subfield to `inferenceModels`, which makes a model's 1M-context variant the default picker selection when paired with `supports1m`.
  * Added the `toolSearchEnabled` key. When enabled, Code and Cowork sessions load MCP tool schemas on demand instead of placing every schema in context up front, which helps when many configured tools would otherwise crowd the context window. Requires an inference endpoint that forwards `anthropic-beta` request headers.
  * Bootstrap-delivered model configuration is now forwarded to Claude Code sessions in third-party deployments.
  * Changed the projects environment picker to respect an organization policy that hides Anthropic-managed environments.
  * Removed the Beta designation from the `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` keys; the Chat tab and advanced file analysis are now generally available. Availability is unchanged, and both remain opt-in.
  * Fixed a bug affecting third-party plugins installed from external sources (GitHub, URL, or npm).
</Update>

<Update label="v1.20186.9" description="2026-07-14">
  **General**

  * Fixed an issue where permission prompts and in-session questions could silently stop appearing after an input-handling error — if Claude asked a question or requested permission and the prompt never showed up, this release fixes that. (Updates the bundled Claude Code CLI to 2.1.209.)
</Update>

<Update label="v1.20186.0" description="2026-07-09">
  **General**

  * Fixed `claude://` deep links being ignored when opening one launched the app from a closed state, including on Windows and Linux.
  * Fixed device attestation failing on Windows when sending several messages at once.
  * Fixed garbled tool summaries in the transcript: descriptions that don't start with a recognized verb (for example "Final verification") now appear as written instead of being mis-conjugated.
  * Fixed skill proposal and skill-file cards failing to save with "Couldn't save this skill" when a skill of that name already exists; they now offer "Update skill" and a replace confirmation.
  * Fixed the app forgetting your last-used tab (for example Code) after an update or re-login.
  * Fixed the menu bar usage menu showing an empty progress bar for extra usage when the spend cap is unlimited.

  **Code**

  * Added a Troubleshooting option to import Claude Code CLI sessions found on this computer into the session list.
  * Fixed a typed `<channel-message>` turn rendering as a spoofable "Message from `{server}`" card instead of as your own text.
  * Fixed cross-session messages going missing in the transcript: messages from another session no longer disappear when they arrive in the same turn as other content or when their envelope can't be fully parsed.
  * Fixed file links to files outside the working directory, including reports Claude writes to its scratchpad, showing "This file is outside the working directory" instead of opening.
  * Fixed the context window indicator and token count staying at the pre-compaction value after compacting a conversation.

  **Cowork**

  * Fixed admin-configured plugin marketplace sync failing behind corporate proxies on macOS.
  * Fixed plugin connectors sometimes missing from the Connectors list and tool permission prompts when they were slow to start.
  * Fixed skills saved in a remote session sometimes still returning "Unknown command" right after saving.
  * Fixed the "Run this task while your Mac sleeps" setting turning itself off after an app update.

  **3P**

  * Added `*` wildcard matching for managed MCP `toolPolicy` keys; partial wildcard keys such as `"outlook_*"` in existing configurations now take effect, including any `allow` wildcards, which pre-approve the tools they match. Exact keys and the standalone `"*"` key behave as before.
  * Added support for exporting Cowork task telemetry over `otlpProtocol: grpc` on macOS and Linux when no network proxy is configured.
  * Fixed Azure AI Foundry sessions failing with an authentication error on every message after interactive Microsoft Entra ID sign-in.
  * Fixed gateway-SSO bootstrap dropping cross-origin `managedMcpServers` entries, so admin-provisioned third-party connectors reach the app under device-code sign-in.
  * Fixed MCP connectors failing to connect through gateways that optionally request a TLS client certificate, even though the connection test passed.
  * Fixed sign-in timing out with identity providers (such as PingFederate) that redirect via a rendered page after authentication.
  * Fixed third-party settings ignoring managed configuration: the Claude Code pane now follows `isClaudeCodeForDesktopEnabled`, the Developer tab hides when `isLocalDevMcpEnabled` is off, and the Capabilities and Voice settings no longer appear.
</Update>

<Update label="v1.19367.0" description="2026-07-07">
  **General**

  * Added automatic updates on Linux through the Anthropic apt repository, so new versions arrive with `apt upgrade` (and unattended upgrades where enabled).
  * Added the ability to archive or delete the current chat, project, task, or coding session directly from the command palette (`⌘K`, or `Ctrl+K` on Windows and Linux).
  * Fixed bank payment-verification (3DS) pages not loading during checkout.
  * Fixed MCP connectors in artifacts being silently dropped; approving a connector now reliably grants its tools to the artifact, and a previously stuck approval heals itself the next time you approve.
  * Fixed repeated crashes on Linux caused by unstable graphics acceleration; the app now turns acceleration off automatically and tells you.
  * Fixed the app becoming unresponsive when a session folder is on a slow or disconnected network drive.

  **Code**

  * Added descriptive branch names for local Code sessions, derived from your first message, in place of the random adjective-noun names.
  * Changed the default transcript and composer width to a narrower, more readable column; a width you already chose in Settings → Appearance is preserved.
  * Fixed "Open in Finder", "Open in editor", and "Attach to chat" doing nothing, or using the wrong path, for files in the diff panel when the session folder differs from the repo folder.
  * Fixed freezes and stalls: while restoring a large number of sessions at startup, while builds or file syncs churned files inside a watched folder, and while the diff panel refreshed during a response.
  * Fixed newly trusted folders sometimes failing to start a session with a "workspace is not trusted" error.
  * Fixed security-key and phone sign-ins not completing in preview tabs.

  **Cowork**

  * Added a copyright-access notice in the session timeline when Claude in Chrome first operates on certain news publisher sites.
  * Added keyboard access to the preview pane: Tab reaches a "Preview page" control, Enter moves focus into the loaded page, and `F6` (or `Ctrl+F6`) moves it back out.
  * Fixed Cowork offering terminal access, and showing an impossible fix suggestion, on devices whose operating system cannot provide the virtualization its isolated environment needs (such as ChromeOS), where every command immediately failed.

  **3P**

  * Added `inferenceFoundryAuthFlow` to choose how interactive Microsoft Entra ID sign-in for Azure AI Foundry runs: `device-code` (the default, which shows a code to enter at `microsoft.com/devicelogin`) or `browser`, which opens the system browser for an authorization-code (PKCE) sign-in.
  * Added `microsoftAuthBroker`; set it to `disabled` to force browser-based Microsoft 365 sign-in instead of the native Company Portal or Windows account broker.
  * Added a "session expires soon" warning for Bedrock SSO and AWS-profile sign-in so you can re-authenticate before hitting an error.
  * Added a `startupTimeoutSec` option for managed local (stdio) MCP servers and raised the default startup timeout from 10 to 120 seconds, fixing connection failures when a server command downloads packages on first run (for example `uvx` or `npx`).
  * Added support for background agents: long-running tasks now stay signed in after your identity provider's access token expires.
  * Added the ability for administrators to grant Microsoft 365 write scopes (send mail; edit calendars and files; send Teams chat; mailbox settings) through managed configuration.
  * (breaking) Changed the default for Desktop Extensions (`.dxt` and `.mcpb`): they no longer load unless you set `isDesktopExtensionEnabled` to `true` in managed configuration. Previously they loaded by default and only the install UI was blocked.
  * Updated `allowedPluginMarketplaces` (beta) so it can be delivered per-user through the bootstrap server; a response that omits the key leaves MDM-provisioned marketplaces in place.
  * Fixed a one-time loss of sign-ins on some managed Windows machines after app data moved to a new location.
  * Fixed AWS credentials not reaching the Code tab's terminal for Amazon Bedrock configurations that use IAM Identity Center.
  * Fixed bundled Microsoft 365 and other MCP connectors failing to connect on networks with corporate TLS inspection (custom root CA).
  * Fixed connection tests reporting false failures: the test now runs MCP helper scripts and checks managed configurations exactly as saved, and uses the same Azure AI Foundry endpoint that sessions use.
  * Fixed managed MCP connectors failing with a credential-storage error when the server allows anonymous access.
  * Fixed the Microsoft 365 connector failing to sign in on Macs enrolled with Microsoft Company Portal.
  * Fixed the setup form incorrectly showing "Blocked address" for internal MCP or OAuth servers on IPv6 enterprise networks.
</Update>

<Update label="v1.18286.2" description="2026-07-07">
  **General**

  * Updated the embedded Claude Code engine to the latest version.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.18286.0" description="2026-07-02">
  **General**

  * Fixed `apt update` failing on Linux after uninstalling a Claude that was installed from the apt repository.
  * Fixed being asked to sign in repeatedly after a session expired while you were using the app; your in-progress message draft now returns when you sign back in within 10 minutes, and signing out still clears it.
  * Fixed being unable to disable, delete, or uninstall plugins from GitHub-connected marketplaces, or to remove those marketplaces.
  * Fixed pressing Enter not sending your message when an @mention had no matching results.
  * Fixed remote SSH sessions getting stuck in a reconnect loop on very large messages, being lost when the computer woke from sleep mid-reconnect, and occasionally sending the same input twice after reconnecting.
  * Fixed setup on Windows getting stuck retrying a download when the download folder was locked or inaccessible.
  * Fixed the file-open spinner on Linux staying up after the download completed.

  **Code**

  * Added a "Choose folder" option to recover a session whose working folder is missing: the conversation forks into the folder you pick and the stuck session is archived.
  * Added a "Switch organization" option on the "session not found" page so you can reopen a session link under the right organization.
  * Added drag-to-reorder for queued messages, and Steer now works for messages that include images.
  * Improved the Code tab's live preview: it now reports honest connection and loading status (including when a page arrives but never finishes loading, or a server overloads itself with requests), adds browser-style Back, Forward, and Reload/Stop controls, and lets you close other preview tabs.
  * Fixed background tasks and workflows continuing to show as running after they finished, the session restarted, or the session was stopped.
  * Fixed Remote Control sessions spinning forever with no error after you sent a message when the hosting computer was no longer connected.
  * Fixed the sidebar project + button opening an empty prompt (or pointing at github.com) for GitHub Enterprise repositories.

  **Cowork**

  * Added click-to-zoom and drag-to-pan to the fullscreen image viewer.
  * Fixed Computer Use teach mode where the Next and Exit buttons sometimes stopped responding until you switched apps and back, and cleared up teach-mode visuals so the screen-edge glow no longer flickers and the status indicator no longer sticks after you exit a guide.
  * Fixed dictation dropping back to the text box when started from the mic button in existing sessions.
  * Fixed document tools in cloud sessions acting on your local files instead of the session's files.

  **3P**

  * Added a usage breakdown by model family, source attribution, and usage tips to the `/usage` card.
  * Removed automatic addition of Anthropic's default plugin marketplace on third-party deployments, and removed the `disableDefaultPlugins` managed configuration key (which had no effect there). Provision marketplaces via `allowedPluginMarketplaces` (beta).
</Update>

<Update label="v1.17377.2" description="2026-07-01">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Added Claude Fable 5 to the model picker for organizations with access.
</Update>

<Update label="v1.17377.1" description="2026-06-30">
  **General**

  * Added Linux support: Claude Desktop is now available for Debian and Ubuntu on x64 and arm64, installable as a .deb package.
  * Updated the plugin Directory to show admin-configured marketplaces under the Organization tab and refresh them automatically when the source repository updates.
  * Fixed plugin and skill downloads stalling for several minutes on a dead connection before retrying; stalled downloads now retry sooner.
  * Fixed prompt and tool-detail content missing from OpenTelemetry exports for standard deployments that have not set an explicit content-capture policy; third-party deployments are unchanged.
  * Changed zoom in and out to use smaller steps for finer control.

  **Code**

  * Added an integrated terminal pane and inline image previews in the transcript for SSH sessions.
  * Added step-by-step progress and a Stop button while a session's worktree is being set up, so a long checkout on a large repository can be cancelled.
  * Added a right-click menu in the Terminal pane with Copy, Paste, and Attach selection as context.
  * Updated the transcript to mask API keys and tokens by default; click the eye icon to reveal them.
  * Fixed folder access and cross-session requests being rejected after you approved them when permission mode was Auto or Bypass permissions.
  * Fixed failed mid-turn message sends (for example, while offline) dropping your text instead of returning it to the input.
  * Fixed new session worktrees branching from the currently checked-out branch instead of the repository's default branch, and archived sessions leaving their worktree folders on disk.

  **Cowork**

  * Fixed a crash when resuming sessions with malformed remote connector data on disk.
  * Fixed the workspace download restarting from zero after a network interruption; it now resumes from where it left off and retries automatically.
  * Fixed folder and file names containing a dollar sign being misread, which broke file references.
  * Fixed dictation immediately dropping back to the text input in existing sessions.
  * Fixed an error caused by Claude trying to read a document creation skill that was not available.
  * Fixed clicking a built-in workflow (such as `deep-research`) in the activity panel's Skills section showing an empty drawer instead of its name and source.

  **3P**

  * Added the `allowedPluginMarketplaces` managed configuration key. Configured git repositories appear under the Directory's Organization tab.
  * Added an optional `omitOfflineAccess` subfield to the `inferenceVertexWorkforceOidc` configuration. Enable it when an identity provider rejects the `offline_access` scope; the app then prompts for sign-in each time the identity provider token expires instead of refreshing silently.
  * Added managed configuration support on Linux: administrators can provision settings in a root-owned `/etc/claude-desktop/managed-settings.json`, validated against the same schema as the macOS and Windows sources.
  * Fixed claude.ai sign-in never completing on Windows when an enterprise inference provider is configured.
  * Fixed subagents failing with an invalid model error on third-party inference providers.
  * Fixed `inferenceModels[].supports1m` being ignored, restoring the 1M-context option in the model picker for Bedrock, Vertex, Foundry, and gateway providers.
  * Fixed the Microsoft 365 connector showing an unexpected admin-consent prompt after updating on tenants with restrictive consent policies when the connector's Access setting was blank. Also updated the bundled connector with tools to read the signed-in user's profile and draft reply-all emails.
  * Improved expired sign-in handling for third-party inference providers and connectors: a sign-in prompt now appears whichever credential type expired, connector authentication errors are shown in Settings and inline in chat with a Reconnect action, and background Code sessions stay signed in across a credential refresh.
  * Fixed several connector reliability issues: connectors silently stopping mid-session after an OAuth refresh failed instead of prompting to reconnect, connectors configured with both OAuth sign-in and custom headers failing to connect, and admin-configured connectors not appearing in a session until they were signed in.
</Update>

<Update label="v1.15962.2" description="2026-06-30">
  **General**

  * Updated the embedded Claude Code engine to the latest version.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * No user-facing changes.
</Update>

<Update label="v1.15962.1" description="2026-06-26">
  **General**

  * No user-facing changes.

  **Code**

  * No user-facing changes.

  **Cowork**

  * No user-facing changes.

  **3P**

  * Fixed locally-configured stdio MCP servers being refused in third-party deployments that don't use MDM.
  * Fixed third-party MCP connectors disconnecting on every app restart when the OAuth provider returns a non-standard refresh response.
  * Fixed Microsoft 365 brokered sign-in failing with "No reply address provided" on managed Macs.
</Update>

<Update label="v1.15962.0" description="2026-06-25">
  **General**

  * Fixed a crash on launch caused by an unusually large saved session.
  * Fixed the conversation jumping and the Progress panel flashing when opening a completed task.
  * Improved keyboard navigation: a message's action buttons are now a single Tab stop, with arrow keys to move between them.

  **Code**

  * Fixed high background CPU usage when several Code sessions were open in the same large repository.
  * Fixed people without a Claude Code seat being sent to the marketing site from `/code`; they now see an in-app organization switcher.
  * Added support for custom cron expressions when scheduling local routines.
  * Added "Open in VS Code", "Open in Cursor", and similar actions to the file panel, file tree, plan panel, titlebar, and sidebar in SSH sessions.
  * Fixed attachment cards for files that exist only inside a session doing nothing when clicked; they now open in the File pane, lightbox, Preview pane, or Files browser.
  * Added a "Load more" button to the All sessions list for people with many sessions.

  **Cowork**

  * Fixed workspace setup repeatedly failing with the same checksum error after a corrupted download, until the cache was cleared.
  * Fixed Cowork sessions losing their project after restarting the app.
  * Added a one-time prompt before Claude runs a dynamic workflow, explaining what workflows do.
  * Improved the time it takes to start a session.

  **3P**

  * Added a managed `websearch` built-in tool so self-hosted deployments can search the web. Admins configure Brave, Tavily, Exa, or a custom endpoint in managed config, and it is available in both the Cowork and Code tabs.
  * Added an `otlpContentCapture` managed setting that lets admins opt in to sending specific categories of unredacted content — user prompts, assistant responses, tool inputs, tool outputs, and raw API request/response bodies — to their OTLP collector.
  * Updated the Microsoft 365 built-in connector's `scope` field to accept `MailboxSettings.Read`.
  * Fixed managed connectors that lost their connection staying broken with failing tool calls; they now reconnect automatically on the next tool call, including from newly started conversations, and show a message if reconnecting fails.
  * Fixed Microsoft 365 connector sign-in failing on Windows because of a broker error.
  * Fixed a sign-in loop when your organization's gateway denies access; the app now shows "Access denied" and points you to your administrator.
  * Fixed the selected model reverting after restarting the app and resuming a session.
  * Added a `disableBundledSkills` managed config key that turns off Claude Code's bundled skills and workflows (such as `deep-research`) on that device.
</Update>

<Update label="v1.15200.0" description="2026-06-23">
  **General**

  * No user-facing changes.

  **Code**

  * Added an inline card for multiple-choice questions from Claude, so you can pick an option and step through each question before your choices are sent as a single reply.
  * Fixed the app crashing shortly after opening the Code tab when local session history files are very large.
  * Fixed the integrated terminal eventually failing to open new shells after the app had been running for several days on macOS.
  * Fixed forked sessions not carrying over pull requests from the original conversation, and pull request rows staying marked as closed after being reopened on GitHub.
  * Fixed the @-mention dropdown, side-chat panel, and plan-comment popover rendering, resizing, and dismissing in the wrong window when a session is opened in its own window.
  * Fixed an extra tab opening in the system browser when navigating with the Artifacts pane open.

  **Cowork**

  * Added the ability to delete Cowork sessions from the sidebar, recents, and Spaces views.

  **3P**

  * Published the v2 bootstrap-response JSON schema (nested format). The v1 flat schema remains supported.
  * Removed support for installing connector extensions from local `.mcpb` and `.dxt` files.
  * Fixed the Setup panel being locked when only the auto-update policy was deployed via MDM.
  * Fixed connectors configured by your organization not appearing until restart after first sign-in.
  * Fixed the model picker dropping to "Default model" mid-session when a gateway's model-list response was temporarily degraded.
</Update>

<Update label="v1.14271.0" description="2026-06-18">
  **General**

  * Fixed the app prompting you to sign in again every day when your claude.ai session was more than a day old.
  * Fixed Claude Design links in chat navigating the app in place instead of opening Claude Design.
  * Fixed the app showing a blank window when a network proxy redirects the connection to Claude.

  **Code**

  * Changed routines to count against your regular usage limits instead of a separate daily included-run limit, and removed the included-runs indicator.
  * Updated the model picker to show restricted models as non-selectable with an explanatory badge, and to reflect your organization's allowed default model.
  * Fixed HTML and SVG file previews showing black text on a dark background in dark mode.
  * Fixed menus and popovers opening behind the preview panel.

  **Cowork**

  * Fixed Claude in Chrome file uploads failing for files in the session's shared folders and outputs.
  * Fixed scheduled tasks leaving earlier processes running after each scheduled run.
  * Fixed Windows file paths showing garbled characters in the folder access approval card, and reduced unnecessary folder access denials when allowed workspace folders are configured.

  **3P**

  * (breaking) Changed the `chatCodeExecutionEnabled` managed configuration key to `chatAdvancedFileAnalysisEnabled`. It still lets Claude analyze attached files such as spreadsheets and presentations by running code in a sandbox scoped to the session's attachments, and remains off by default. Update any managed configuration that sets the old key.
  * Deprecated the `betaFeaturesEnabled` managed configuration key; use the per-feature keys `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` instead. The Beta label in the Setup window is now informational only, and the Beta label has been removed from the built-in Microsoft 365 connector presets.
  * Added the `inferenceSessionLifetimeSec` managed configuration key. Set it to your identity provider's session lifetime to show users a re-authenticate reminder before their sign-in expires.
  * Added `~` and environment variable expansion (such as `%APPDATA%` and `%OneDriveCommercial%`) to the `allowedWorkspaceFolders` setting, so folder paths can vary per user.
  * Added a per-folder pre-select option to `allowedWorkspaceFolders` so an administrator-configured folder can appear as a ready chip when users start a new task, and removed the "Create workspace folder?" prompt for administrator-configured folders.
</Update>

<Update label="v1.13576.0" description="2026-06-16">
  **General**

  * Improved find-in-page to search the entire session transcript instead of only the text scrolled into view, and the find bar now reliably takes keyboard focus when opened.
  * Added a unified Artifacts view that lists your chat, Code, and Cowork artifacts in one searchable place, with a "New artifact" menu and a "Filter by" control to narrow the list by source.
  * Fixed keyboard shortcut conflicts failing silently. Assigning a shortcut already held by another app now tells you and keeps your previous shortcut working, and Quick Entry registration errors now appear in Settings.
  * Fixed the first-run notification explaining that Claude keeps running in the notification area never appearing on Windows.

  **Code**

  * Added running dev servers to the Background tasks panel, with stop and open-preview actions.
  * Improved the Code file viewer: images, video, and audio now play inline instead of showing as text, and Markdown, CSV, and image files refresh automatically when Claude edits them.
  * Updated the model picker. The three headline models appear at the top level with older models and context-size variants under "More models", each model shows a capability description, and currently-unavailable models appear disabled instead of failing when selected.
  * Updated the in-session artifact panel: switch between a session's published artifacts from the title dropdown, see when an artifact was last updated, copy a share link, and open, share, or delete the artifact from the overflow menu.
  * Changed the Code sessions tab from "Projects" to "All sessions". It now lists your non-project sessions alongside project sessions and adds a multi-select Environment filter.
  * Fixed pull request status checks. Failures now show a small warning indicator on the branch row instead of repeated error popups, the "status couldn't be checked" warning appears less often and can always be dismissed, and only GitHub CLI sign-in problems still raise a notification.

  **Cowork**

  * Fixed corrupt plugin downloads crashing or hanging the app.
  * Fixed skills sometimes staying on an older version after being edited until toggled off and on.

  **3P**

  * Added the Chat tab as a beta feature controlled by the `chatTabEnabled` managed configuration key. The separate `chatCodeExecutionEnabled` key lets Claude analyze attachments and create files such as spreadsheets and presentations by running code in an isolated sandbox scoped to the session's attachments, and is off by default.
  * Added the `betaFeaturesEnabled` managed configuration key. Setting it to false disables every beta feature in the deployment, including the Chat tab.
  * Added Bedrock Mantle as an inference provider option. It reuses the existing `inferenceBedrockRegion` and `inferenceBedrockBaseUrl` managed configuration keys and authenticates with a bearer token or a credential helper.
  * Added `anthropicFamilyTier` and `isFamilyDefault` to managed `inferenceModels` entries. Tag each configured model with the Claude tier it stands in for so tier shortcuts like opus and sonnet resolve to your configured model IDs instead of the canonical names your provider may not route.
  * Added the `inferenceBedrockAwsCliPath` managed configuration key to set the AWS CLI's absolute path. This fixes aws sso login failing when the app is launched from Finder on macOS and the CLI is not on the default search path.
  * Fixed Google Workspace connectors never starting their OAuth sign-in. The MCP client identifier the app sends to connected servers is now `claude-desktop-3p`, changed from `custom3p-desktop`, so update any MCP server allowlists or log filters that match the old value.
  * Fixed the managed Tool policy `*` entry being ignored. It now applies as the default for any tool not listed by name.
  * Fixed organization plugins sometimes not opening from the Directory right after launch or update.
  * Fixed several connection and sign-in issues: Bedrock sessions now prompt to sign in again after AWS IAM Identity Center expires instead of failing with repeated credential errors, remote MCP connectors no longer stay Connected after a non-refreshable access token expires, the connection test now passes against gateways that optionally request a TLS client certificate, signing in after signing out no longer needs a double click, and sign-in recovery no longer uses stale configuration after a server-side update or leaves the model picker empty until restart.
</Update>

<Update label="v1.12603.1" description="2026-06-11">
  **General**

  * Added Find Next and Find Previous keyboard shortcuts to in-app search.
  * Fixed preview panes stealing keyboard focus from the chat input when they reloaded or navigated.
  * Fixed sessions failing to start after your sign-in expired — the app now prompts you to sign in again.

  **Code**

  * Added the Files panel to remote and SSH sessions — search the session's files and open them in the viewer — plus a Show in Files button in the file viewer.
  * Added a running-tasks button to the activity indicator that opens the Tasks panel, and Bash rows in the Background tasks panel now open to show their output, including a live tail while the command runs.
  * Fixed SSH sessions: forking no longer opens an empty conversation, and connections no longer fail with "Failed to upload file" errors on remotes first set up by early-2026 versions of the app.
  * Fixed renaming a session while its title was still generating — the generated title no longer overwrites the name you set.
  * Fixed the Pull Requests view showing "No open pull requests" when GitHub isn't connected — it now prompts you to connect.
  * Added model-picker memory — the picker now remembers your last model choice.

  **Cowork**

  * Fixed scheduled tasks firing many duplicate runs at once when the computer wakes from sleep.
  * Fixed remote sessions re-prompting for access to folders you had already trusted.
  * Fixed plugins becoming corrupted when they synced while you switched accounts.

  **3P**

  * Added the built-in Microsoft 365 connector — admins can configure it from the Setup window's server presets. Users sign in through their browser, and Claude can search and read Microsoft 365 mail, calendar, OneDrive, and SharePoint. It requests read-only access by default; admins can grant additional read scopes, such as Teams channel messages and meeting transcripts, with the managed server entry's scope setting.
  * Deprecated the "sso" value for the inferenceGatewayAuthScheme managed configuration key in favor of inferenceCredentialKind "interactive" — existing configurations keep working and log a deprecation warning.
  * Added the inferenceVertexOAuthLoginHint managed configuration key to pre-fill the Google account chooser when signing in to Vertex AI, so users in organizations federated to a third-party identity provider land on the right account automatically.
</Update>

<Update label="v1.11847.5" description="2026-06-09">
  **General**

  * Fixed Clear Cache and Restart signing you out instead of just clearing caches.
  * Fixed mouse back and forward buttons not navigating on macOS for mice managed by driver software like Logitech Options+, and added trackpad swipe navigation.
  * Fixed organization plugins sometimes failing to open right after app launch, and the plugin directory now offers Install again after an uninstall.
  * Fixed connector, Chrome extension, and plugin toggles in the composer's "+" menu not responding when you click directly on the switch.
  * Fixed an issue where signing in could leave the app unable to start sessions until it was restarted.
  * Fixed shell-exported custom request headers not reaching Claude Code sessions.

  **Code**

  * Fixed Claude losing its coding instructions, file-link formatting, and worktree context after a session resumed from idle.
  * Fixed the preview pane sometimes connecting to an unrelated dev server that was already using the configured port, and it now reopens the dev server you last picked for each project.
  * Improved responsiveness in Code sessions: smoother streaming of long code blocks, quicker side-panel shortcuts, and less delay opening cloud sessions with many screenshots.
  * Fixed popovers, dialogs, and the rewind picker not appearing — and typed characters jumping to the end of the composer — when a Code session is opened in its own window.
  * Fixed the slash-command menu opening behind the side chat panel.
  * Fixed the source-branch picker showing nothing for SSH sessions with worktree enabled.

  **Cowork**

  * Added a "Free Up Cowork Disk Space" option under Help > Troubleshooting, and Cowork now cleans up caches and old temporary files automatically when its workspace disk runs low.
  * Improved the read/unread toggle on sidebar sessions: it now works on the currently open session, has a larger click target, and shows a tooltip describing what a click will do.

  **3P**

  * Added support for the Fable model family, and for Mythos where your organization has access.
  * Fixed sign-in failing with external identity providers that reject the offline\_access scope — admins can now disable the automatic append.
</Update>

<Update label="v1.11187.4" description="2026-06-05">
  **General**

  * Fixed reinstalling Claude on Windows failing after an uninstall when IT had installed it for all users.
  * Fixed the app not starting automatically at login on Windows.
  * Added a banner when an update fails to install, instead of failing silently.
  * Fixed built-in connectors staying disconnected after a crash — existing sessions now reconnect them automatically, and disconnecting a built-in connector now signs it out and keeps it disconnected across restarts.

  **Code**

  * Added math rendering for inline and block expressions in Claude Code transcripts.
  * Added Ultracode to the effort slider, which selects the highest effort level and turns on dynamic workflows for the session.
  * Added drag-to-reorder and A→Z sorting for projects in the Claude Code sidebar.
  * Added triple-click to select a whole code block, plus right-click menu actions to copy a code block or inline code, in Claude Code transcripts.
  * Fixed resuming Code sessions when the working folder had moved or been deleted — sessions saved with a \~ path no longer show as missing or re-prompt for trust, and a deleted remote folder now reports clearly and offers a Fork session button instead of retrying in a loop.

  **Cowork**

  * Added a low-disk-space warning before Cowork downloads the files it needs to run.
  * Added in-session effort and thinking controls for local Cowork projects.
  * Updated the New project folder picker to default to your Claude data folder (\~/Claude/Projects) instead of \~/Documents.
  * Fixed Claude reporting that a skill was updated when the change was never saved to your account.
  * Fixed the /schedule command in Cowork showing as unavailable.

  **3P**

  * Fixed managed connectors and SSO sign-in requesting broader OAuth scopes than the administrator configured.
  * Fixed three Bedrock sign-in and session issues: SSO sign-in failing behind corporate proxies that intercept secure traffic, expired SSO tokens prompting a new sign-in every hour instead of refreshing automatically, and resumed sessions failing on their first message.
</Update>
