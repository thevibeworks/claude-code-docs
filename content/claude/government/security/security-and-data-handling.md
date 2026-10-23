> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security and data handling

> Answers for agency security review: sandbox isolation, network egress and required domains, approvals, connector credentials, telemetry, and where data is stored.

> **Who this is for:** Security, compliance, and IT reviewers who are assessing Claude for Government for their agency, and administrators who need to explain the product's runtime behavior.

The answers on this page address the security and data-handling questions that come up most often during agency security review, for the [Claude Desktop application](#claude-desktop) and for the standalone [Claude Code command-line tool](#claude-code-command-line-tool), each in its own section. Each answer states what is specific to Claude for Government (the FedRAMP High boundary, the defaults Anthropic applies for government tenants, and the relevant admin portal control), then links to the product documentation for the underlying mechanism. For assurance materials such as the security architecture overview, SOC 2 report, and penetration testing summary, request access through the [Anthropic Trust Center](https://trust.anthropic.com).

## Claude Desktop

The sections below cover the Claude Desktop application, which offers three ways to work with Claude: **Chat** for simple conversations, **Cowork** for longer tasks with a local workspace folder, and **Code** for software development. For the admin portal and the Compliance API, see the [Organization administration](https://claude.com/docs/government/org-admin/overview.md) and [Tenant administration](https://claude.com/docs/government/tenant-admin/overview.md) sections.

### Sandbox and isolation

In Cowork, and for the file-analysis steps in Chat, the Claude Desktop application runs shell commands and model-written code inside a dedicated local virtual machine. In Claude for Government, this sandbox is always the execution path for the code and shell commands that Claude runs in Chat and Cowork. Code sessions run on the workstation itself rather than in the virtual machine, as described under [Code in Claude Desktop](#code-in-claude-desktop). For the detailed threat model and isolation design, request the security architecture overview through the [Anthropic Trust Center](https://trust.anthropic.com).

> **What does the sandbox isolate, and what runs outside it?**
>
> The sandbox virtual machine runs the shell commands and model-written code of Cowork sessions and of the file-analysis steps in Chat. The agent loop, built-in file tools, web fetch, and the connector client run in the Claude Desktop application on the user's device and are governed by separate controls: per-action approval prompts, administrator-set per-tool policies, and the network egress allowlist applied when each tool runs. Code sessions also run outside the virtual machine, as described under [Code in Claude Desktop](#code-in-claude-desktop). For a deeper description of the layered controls inside and outside the virtual machine, see the security architecture overview available through the [Anthropic Trust Center](https://trust.anthropic.com).

> **What can shell commands in the sandbox reach?**
>
> Shell commands that Claude runs in the sandbox work on the folders the user has attached, a scratch area, and read-only reference material bundled by the application (such as skill and plugin directories). Shell commands cannot work on the rest of the user's files. In Cowork, Claude can ask the user to add a specific folder during the session, and the user approves or declines that request; see [Approvals and Auto mode](#approvals-and-auto-mode). Administrators can restrict which local folders users may attach with **Allowed workspace folders** on the [Config](https://claude.com/docs/government/config/settings.md#allowed-workspace-folders) page. The desktop client then refuses folders outside that list in the workspace picker, in requests Claude makes during a session, and in Claude's file tools. In Cowork, Claude's file tools may read and write in the listed folders. See [Desktop and filesystem access](https://claude.com/docs/third-party/claude-desktop/local-access.md) for how folder scoping is enforced.

> **How are attached folders made available to the sandbox?**
>
> When a user attaches a local folder to a Cowork session, the entire folder is made available to that session's sandbox as a filesystem mount, so changes Claude makes are written directly to the folder on disk. A mapped network drive on Windows is an exception: Claude's host-side file tools can read, write, and search it, but shell commands in the sandbox can reach it only if the drive was mapped and reachable when the sandbox started (see [Network drives on Windows](https://claude.com/docs/third-party/claude-desktop/local-access.md#network-drives-on-windows)). Files the user attaches individually to a conversation are copied or hard-linked into a per-conversation uploads directory and mounted read-only; where the filesystem hard-links, edits to the original file while the conversation is open can be visible to it. The allowed-folders setting is a policy control enforced by the desktop application. See [Desktop and filesystem access](https://claude.com/docs/third-party/claude-desktop/local-access.md).

> **Which file types need the sandbox in Chat?**
>
> Some attachment types, such as Excel and PowerPoint, need a conversion step that runs inside the sandbox. Enabling **Advanced file analysis in Chat** under **Product availability** on the [Config](https://claude.com/docs/government/config/settings.md#product-availability) page lets Claude run code against attachments in a sandbox, including that conversion. You do not need to make Cowork available to get this capability. See [Chat in Claude Desktop](https://claude.com/docs/third-party/claude-desktop/chat.md) for how Chat handles file attachments.

### Code in Claude Desktop

Code sessions use Claude Code built into the desktop application and run on the user's workstation itself, not in the virtual machine. The shell commands Claude runs during a Code session execute on the workstation's own operating system under the user's own account.

On macOS and Linux, those shell commands run inside an operating-system-level sandbox that the application builds from your organization's **Allowed network hosts** and **Allowed workspace folders** settings on the [Config](https://claude.com/docs/government/config/settings.md#allowed-network-hosts) page. The sandbox is in place whenever either setting restricts access, which the default configuration does. Inside the sandbox, a command can create or change files only in the session's folder, the other folders **Allowed workspace folders** permits, and temporary locations. Unless [**Block reads outside workspace folders**](https://claude.com/docs/government/config/settings.md#block-reads-outside-workspace-folders) is on, it can read any file on the device that the user's account can open. By default it runs without asking the user first. A user can exempt specific commands from this sandbox in a Claude Code settings file, and an exempted command runs outside the sandbox under the permission mode the user selects for the session.

Claude can also type commands into the Code tab's terminal, which is the user's own shell (PowerShell on Windows). The app asks the user to approve each of those commands by default, and they run as the user, outside any sandbox. Administrators can turn these terminal tools off with the **Terminal panel tools** card on the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page. The [**Blocked shell commands**](https://claude.com/docs/government/config/settings.md#claude-code) list does not block commands Claude types into the terminal, but the **Require approval for each command** sub-setting on the **Shell commands** card applies to them in every permission mode.

On Linux, the sandbox requires the `bubblewrap` and `socat` packages, so install both on each workstation as described under [Set up Linux and WSL2](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2) in the Claude Code documentation. If either package is missing, shell commands run outside the sandbox as they do on Windows.

On macOS and Linux, the sandbox also blocks connections to local Unix sockets. A command that talks to a local agent through a socket, such as git signing a commit with a key held in an SSH agent or a hardware-backed key manager, cannot reach that agent from inside the sandbox. On macOS, a user who needs such a command to work can list the agent's socket path under `sandbox.network.allowUnixSockets` in their Claude Code settings file, which keeps the command inside the sandbox. Every sandboxed command in that user's Code sessions can then ask the agent to sign or authenticate, so this is appropriate only for an agent that asks the user to approve each use, for example with Touch ID, and not for an agent that signs without prompting.

On Linux, the sandbox ignores `sandbox.network.allowUnixSockets` and has no exception for individual sockets. See [Sandbox settings](https://code.claude.com/docs/en/settings-reference#sandbox-settings) in the Claude Code documentation.

Exempting git commands such as `git commit` with `sandbox.excludedCommands` is not a safe way around the socket restriction. A sandboxed command can still change files that git runs during a commit, such as hook scripts kept in the working tree, and an exempted `git commit` would then run that code outside the sandbox. On macOS, git also cannot reach remotes over SSH from inside the sandbox, so a user who needs to push can use an HTTPS remote whose host is on the **Allowed network hosts** list, or push from a terminal outside the Code session.

In container-based Linux environments, such as cloud development workspaces, the sandbox can fail to start, and shell commands in Code sessions then fail with a `bwrap` error. To run Code sessions there, turn off the **Shell command sandbox** switch under **Advanced settings** in the **Claude Code** section of the [Config](https://claude.com/docs/government/config/settings.md) page, at the level that applies to the members who work in those environments, such as a [directory group](https://claude.com/docs/government/config/overview.md#group-specific-settings).

The **Shell command sandbox** switch applies to those members on every device they use, not only in the container workspaces. It reaches their Code sessions where your organization's [Claude Code settings](https://claude.com/docs/government/config/settings.md#claude-code) do. Shell commands in those Code sessions then run without the sandbox, under the permission mode the user selects for the session, as they do on Windows, and the **Allowed network hosts** and **Allowed workspace folders** settings no longer confine what those commands can reach or change. The switch also turns the sandbox off in those members' sessions in the Claude Code command-line tool.

On Windows, there is no operating-system-level sandbox for Code sessions. Shell commands run directly on the device under the permission mode the user selects for the session and under your agency's own endpoint and network controls. The **Allowed network hosts** and **Allowed workspace folders** settings do not confine what those commands can reach, read, or change.

On every operating system, the application starts a Code session only in a folder that **Allowed workspace folders** permits when that setting is configured, and Claude's file reading and editing tools then work only inside the permitted folders. Administrators can also require a prompt on every shell command, in every permission mode, with the **Require approval for each command** sub-setting on the **Shell commands** card of the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page.

Code sessions in Claude for Government run on the local workstation by default. SSH remote sessions are off unless your agency allows specific hosts in Claude Code's managed settings on the device; see [Interaction with Claude Code managed settings on the device](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#interaction-with-claude-code-managed-settings-on-the-device). On Windows, Code sessions inside a Windows Subsystem for Linux (WSL) distribution are not available.

Commands that belong to Claude Code's terminal interface, such as `/sandbox`, are not part of Code sessions in the desktop application. See [how your configuration reaches Code sessions](https://claude.com/docs/third-party/claude-desktop/code.md). If your agency also deploys Claude Code's own managed settings to the same devices:

* **Where your organization's [Claude Code settings](https://claude.com/docs/government/config/settings.md#claude-code) reach Code sessions**: Claude Code uses them instead of the Claude Code policy in those managed settings, such as hooks and permission rules, apart from the [keys Claude Code reads from every admin source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source). The restrictions Claude Desktop [applies as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy) also apply. Where they conflict with your organization's settings, such as on whether the sandbox is on, your organization's value wins, though some of Claude Desktop's restrictions stay on whatever your organization sets. Claude Desktop itself still reads some keys from those managed settings, such as the [SSH host allowlist](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#interaction-with-claude-code-managed-settings-on-the-device).
* **Where they don't**: whether the restrictions Claude Desktop [applies as managed policy](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy), the sandbox included, still apply beside those managed settings depends on their `parentSettingsBehavior`. With `"merge"`, those restrictions also apply. Where they conflict with those managed settings, such as on whether the sandbox is on, the managed settings' value wins, though some of Claude Desktop's restrictions stay on whatever those managed settings set. [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) explains each value.

### Network egress, required domains, and proxies

The desktop application follows the operating system's proxy settings, and a single allowlist controls outbound network access from Claude's tools. You manage the allowlist with the **Allowed network hosts** setting on the [Config](https://claude.com/docs/government/config/settings.md#allowed-network-hosts) page.

> **What does the egress allowlist control?**
>
> The allowlist governs outbound network access from the shell commands and package installs of Cowork sessions, which run in the sandbox virtual machine, from the sandboxed shell commands of Code sessions on macOS and Linux (see [Code in Claude Desktop](#code-in-claude-desktop)), and from the host-side web fetch tool. It does not govern web search (which routes through the Claude for Government service) or connector traffic (covered under [Connectors](#connectors) below). When the list is empty or unset, the only hosts reachable from those tools are the Claude for Government service address and, if you have set a **Telemetry endpoint** on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-endpoint) page, that collector's host, which the application adds to the allowlist automatically. Package installs and page fetches to any other host fail. The list accepts exact hostnames, wildcard patterns such as `*.example.com`, or `*` to allow all outbound traffic. See [Web search and web fetch](https://claude.com/docs/third-party/claude-desktop/web-tools.md) for the full allowlist semantics.

> **Which domains does Claude Desktop need to reach?**
>
> For configuration and model inference, the application reaches the Claude for Government service hostname provided to your agency during onboarding. Sign-in happens in the user's default browser, which must reach that same hostname, the Claude for Government sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider. See the network prerequisites in [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md#before-you-begin). Claude for Government does not publish IP addresses for its service and sign-in hosts, so allow both by hostname on port 443. The [IP addresses](https://platform.claude.com/docs/en/api/ip-addresses) page in the Claude API documentation covers the Claude API, not the Claude for Government hosts. Anthropic-bound telemetry endpoints are not contacted in Claude for Government. Allow `downloads.claude.ai` for the agent helper that runs Chat, Cowork, and Code sessions and for the sandbox virtual machine image, which the app fetches at session start when it does not already have them (not required if your agency uses the offline installer variant that bundles both). The app also reaches the hosts listed under Non-essential services in [Required egress paths](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths). If traffic is blocked, the app will run without icons, previews, and widgets. For automatic application updates, the required hosts depend on how your agency distributes the client; see the network-requirements table in [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md) and confirm the update hosts for your deployment before finalizing your allowlist.

> **Can administrators control when Claude Desktop updates?**
>
> Yes. An agency that distributes Claude Desktop updates itself, for example to keep devices on an assessed version until the next one is approved, turns on **Block automatic updates** on the [Config](https://claude.com/docs/government/config/settings.md#block-automatic-updates) page and also blocks automatic updates in each device's managed configuration, as described under [Automatic updates](https://claude.com/docs/government/deploy-desktop/configure.md#automatic-updates). With both in place, the application neither downloads nor installs updates on its own. An agency that leaves automatic updates on can use **Restart deadline for updates** on the [Config](https://claude.com/docs/government/config/settings.md#restart-deadline-for-updates) page to set how long members may postpone the restart that installs a downloaded update.

> **Does Claude for Government depend on claude.ai or anthropic.com?**
>
> Sign-in, configuration, and model inference do not. Configuration and model inference go through the dedicated Claude for Government service hostname, and sign-in goes through that hostname, the separate Claude for Government sign-in service, and your agency's identity provider, none of which are under either domain. Blocking `*.claude.ai` and `*.anthropic.com` leaves sign-in and inference working. Blocking `*.claude.ai` also blocks `downloads.claude.ai`, which prevents Chat conversations, Cowork tasks, and Code sessions from starting on devices installed with the standard installer unless the app has already downloaded the components they need from that host. App updates often change one or both of those components, and the sandbox virtual machine that runs shell commands in Cowork and Advanced file analysis in Chat then cannot start until the app has downloaded the new versions from that host. Devices installed with the offline installer variant, which includes those components, are not affected. Automatic application updates use hosts under these domains, so an agency that blocks these domains distributes updates itself, as described under [Automatic updates](https://claude.com/docs/government/deploy-desktop/configure.md#automatic-updates).

> **Does blocking claude.ai affect Claude for Government?**
>
> Blocking `claude.ai` does not affect sign-in or inference; neither uses any host under that domain. A personal Claude account cannot sign in to Claude for Government, and a Claude for Government account cannot sign in to `claude.ai`, so there is no shared sign-in surface to restrict. If you allow automatic application updates, keep the update hosts listed in the network-requirements table reachable.

> **Is web fetch always checked against the allowlist?**
>
> Yes. Every web page fetch is checked against your egress allowlist before the request is made, and redirects are re-checked against the allowlist on each hop. See [Web search and web fetch](https://claude.com/docs/third-party/claude-desktop/web-tools.md). Do not rely on this allowlist alone to restrict access to your private network; see **Allowed network hosts** on the [Config](https://claude.com/docs/government/config/settings.md#allowed-network-hosts) page.

> **Can all traffic route through a single proxy?**
>
> Yes, with a caveat for Linux. The desktop application follows the operating system's proxy settings, including PAC URLs, and so does the Cowork sandbox on macOS and Windows. On Linux, no proxy settings reach the Cowork sandbox, and its commands connect directly. See [Network proxy](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#traffic-that-bypasses-the-app-proxy) for the traffic that bypasses the proxy.
>
> TLS inspection at your proxy should work; validate this in your environment before rollout. Web search requests pass through your proxy to the Claude for Government service, and the service's onward call to the search provider originates from inside the FedRAMP High boundary.

### Approvals and Auto mode

By default, Claude for Government prompts the user for connector actions, for each web search, and, in Cowork, when Claude asks to add another folder to the session. In Chat and Cowork, Claude's file tools do not write outside the attached folders, the session's working folder, [memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory), and the folders listed in [**Allowed workspace folders**](https://claude.com/docs/government/config/settings.md#allowed-workspace-folders). In Cowork, shell commands run without a prompt because they run inside the sandbox virtual machine. Web page fetches run without a prompt in both Chat and Cowork and are checked against the [egress allowlist](#network-egress-required-domains-and-proxies). Administrators can require a prompt on every shell command or fetch with the **Require approval for each command** and **Require approval for each fetch** sub-settings on the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page. In Chat on Claude Desktop versions earlier than 2.110.0, every shell command prompts regardless. By default, members cannot switch to Auto mode. When an administrator sets the **Auto mode** setting to **Allowed** on the [Config](https://claude.com/docs/government/config/settings.md#bypass-permissions-mode-and-auto-mode) page, Claude Desktop offers it in Cowork and in Code sessions, and members can switch the Claude Code command-line tool to it. New Code sessions in Claude Desktop 2.9939.2 or later and new interactive sessions in the Claude Code command-line tool 2.1.283 or later then start in it on models that support Auto mode, unless another mode is chosen. Cowork does not offer a bypass-permissions mode.

> **Can write and send actions be gated behind approval?**
>
> Yes. Connector actions prompt the user by default. For each connector an administrator adds, the administrator can switch individual tools on or off under **Tool policy**. A tool that is on stays available and each user approves every use. A tool that is off is blocked. Users cannot loosen these settings.
>
> Tools that are not listed in a connector's **Tool policy**, including tools the server adds later, stay under each user's control. The Microsoft 365 connector always asks for approval before write actions such as sending mail, changing calendar events, or posting Teams messages, and no Claude for Government setting removes that prompt. The **Microsoft 365** card has no per-tool setting, and the connector's read tools follow each user's own approval choices. On the built-in **Web search**, **Web fetch**, and **Shell commands** cards of the Config page, administrators can require approval for every use or turn the tool off. See [Tool and connector cards](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) and [Connectors](https://claude.com/docs/government/connectors/overview.md) for the available settings.

> **Can Auto mode be disabled when a sensitive connector is attached?**
>
> Not for one connector alone. Auto mode is available only while an administrator has the **Auto mode** setting at **Allowed** on the [Config](https://claude.com/docs/government/config/settings.md#bypass-permissions-mode-and-auto-mode) page, as described above, and setting it back to **Blocked** withdraws it again. To limit a sensitive connector while Auto mode is allowed, switch the connector's tools off under **Tool policy** on the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page.

> **Can individual shell commands be allowlisted enterprise-wide?**
>
> Not in Chat or Cowork. Administrators can turn the built-in **Web search**, **Web fetch**, and **Shell commands** tools on or off, or require approval on every use, but cannot allowlist individual commands within those tools. In Chat, an approval for a shell command covers that one command, with no standing approval. For analyses that take many steps, Cowork runs shell commands in the sandbox without prompting; you make Cowork available to members under **Product availability** on the [Config](https://claude.com/docs/government/config/settings.md#product-availability) page. In Code sessions, the [Claude Code](https://claude.com/docs/government/config/settings.md#claude-code) section has no list of allowed commands. Permission rules in a Claude Code managed-settings file on the device can allow individual commands, but they apply in Code sessions only where your organization's Claude Code settings don't reach them, as [Code in Claude Desktop](#code-in-claude-desktop) describes.

> **Can users suppress approval prompts with an Always allow choice?**
>
> For most tools, users who see an approval prompt can choose **Always allow**, which suppresses that prompt for them going forward. Administrators can remove that option on the Config page. Turning on the **Require approval for each search**, **Require approval for each fetch**, or **Require approval for each command** sub-setting on the **Web search**, **Web fetch**, or **Shell commands** card forces a fresh prompt on every use of that tool. A connector tool that an administrator has switched on under **Tool policy** also prompts on each use, without an **Always allow** choice. The Microsoft 365 connector's read tools keep each user's own choice, and its write actions never offer **Always allow**. The create-artifact prompt is an exception: it offers no standing approval. See [Tool and connector cards](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) and [Connectors](https://claude.com/docs/government/connectors/overview.md) for the available settings.

### Connectors

In Claude for Government, connectors fall into three main categories: built-in tools (Web search, Web fetch, Shell commands, and Terminal panel tools), the built-in Microsoft 365 connector, and connectors an administrator adds on the Connectors card of the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page.

> **Where do connectors run, and where are tokens stored?**
>
> Connectors are called from the desktop application, outside the sandbox. The built-in Microsoft 365 connector and administrator-added connectors call their endpoints directly from the user's device, through the system proxy where one is configured. OAuth tokens for both are stored encrypted on each user's device using operating system encryption (macOS Keychain on Mac, DPAPI on Windows). For administrator-added connectors, the bearer header entered on the Config page is delivered to each user's desktop.
>
> A plugin package can include skills, slash commands, sub-agents, and hooks, which run on the member's machine. The Config page asks the administrator to confirm trust before adding a plugin that declares components that can run code on the member's machine, for example hooks or an MCP server. When an administrator adds a plugin on the Config page, Claude Desktop can run a local MCP server that the plugin declares on the member's machine, or connect to a remote one. Administrators distribute plugins to members on the Config page with a per-plugin choice of automatic installation or member opt-in. The **Let members add their own connectors** switch on the Config page controls whether end users can add local MCP servers of their own in Claude Desktop, under **Settings**, then **Developer**. It is off by default, as described under [Let members add their own connectors](https://claude.com/docs/government/config/settings.md#let-members-add-their-own-connectors). The **Let members add plugin marketplaces** and **Let members add their own plugins** switches on the Config page control whether end users can add plugin marketplaces or plugins of their own in Claude Desktop. Both are off by default, as described under [Member-added plugins and marketplaces](https://claude.com/docs/government/config/settings.md#member-added-plugins-and-marketplaces).
>
> A user-added plugin's skills, slash commands, sub-agents, and hooks run on that user's machine, and any connector it declares does not become available as an organization connector. Hook commands and local MCP servers run as programs under the user's own account, outside both the [sandbox virtual machine](#sandbox-and-isolation) and the [Code session sandbox](#code-in-claude-desktop). See [Connectors](https://claude.com/docs/government/connectors/overview.md) and the Plugins card under [Tool and connector cards](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards).

> **Do connectors follow the sandbox egress allowlist?**
>
> No. The built-in Microsoft 365 connector calls Microsoft Graph directly from the user's device; see the [Microsoft 365 connector](https://claude.com/docs/government/connectors/microsoft-365.md) page. Administrator-added connectors connect directly from the user's device to the address configured for that connector. Both pass through the system proxy where one is configured. Web search is a built-in tool rather than a connector and routes through the Claude for Government service; see [Web search and web fetch](#web-search-and-web-fetch) below.

> **Can artifacts be blocked from calling connectors?**
>
> Artifacts follow the same tool settings as Claude's direct connector calls: a connector tool that an administrator has switched off is refused, and a tool that requires approval on every use never runs from an artifact without the user's approval of that call. There is no single switch to disable artifact-to-connector calls while keeping connectors available to Claude directly.

### Telemetry and logging

In Claude for Government, Anthropic-bound error and usage telemetry is always disabled. The OpenTelemetry export to your own collector is a separate setting and sends data only to the endpoint you configure.

> **Is there an inline DLP or inspection point?**
>
> No. Claude for Government does not include an inline content-inspection or DLP gate. The available inspection points are your own network proxy, which sees the traffic routed through it, and the desktop's OpenTelemetry export, which sends tool-call metadata (tool name, connector, outcome, duration, and approval status) to your collector for after-the-fact review. You set the OpenTelemetry endpoint with **Telemetry endpoint** on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-endpoint) page. The **Telemetry content capture** setting on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-content-capture) page adds prompt, response, and tool content to the export for the categories you select, and nothing is selected by default. See [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md).

> **What is logged for connector actions and outbound requests?**
>
> Chat and Cowork sessions write a local audit log to the user's disk recording tool invocations, permission decisions, and file operations; that log never leaves the device. The desktop can also export OpenTelemetry events to a collector you specify: tool name, connector, outcome, duration, and approval status are sent. Prompt text, Claude's responses, and tool inputs and results are included only for the categories you select in the **Telemetry content capture** setting on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-content-capture) page. See [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md) for what the export can include. Server-side, the [Compliance API](https://claude.com/docs/government/org-admin/compliance-api.md) records identity and configuration events but never tool calls or conversation content.

### Data storage and retention

In Claude for Government, conversation content stays on the user's device. If you select content categories in the **Telemetry content capture** setting on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-content-capture) page, Claude Desktop also sends the selected prompt, response, and tool content to your own OpenTelemetry collector, and never to Anthropic. Model requests are proxied through the Claude for Government service to the model endpoint inside the FedRAMP High boundary, and the service records only per-request metadata, not content.

> **Can Anthropic view conversations?**
>
> No. Chat transcripts are stored on the user's workstation, and the Claude for Government service does not log request or response bodies. Inference requests pass through the service to the model endpoint but are not retained. If you select content categories in the **Telemetry content capture** setting on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-content-capture) page, Claude Desktop also sends the selected content to your own OpenTelemetry collector, and never to Anthropic. See [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md) for where conversation content is stored.

> **Where on the device is conversation content stored?**
>
> Conversation content lives under the owner-only application data directory (`%LOCALAPPDATA%\Claude-3p` on Windows, `~/Library/Application Support/Claude-3p` on macOS, `~/.config/Claude-3p` on Linux). Code session transcripts live in Claude Code's own folder in the user's home directory (`~/.claude/projects`). The application does not encrypt these files itself, so encryption at rest depends on the workstation's full-disk encryption, such as BitLocker, FileVault, or LUKS. The operating system encryption that protects connector credentials, described under [Connectors](#connectors), does not apply to conversation content. User-visible outputs such as artifacts are written separately to the user files directory (default `~/Claude`). See [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md) for the full list of what each location holds.

> **Is local history kept separate for each organization?**
>
> No. Claude Desktop keeps conversation history in the application data directory of the operating system account in use on the device, and it does not divide that history by the Claude for Government organization or tenant the user signs in to. A user who is moved to another organization, or who signs in to a second tenant from the same operating system account, sees the same conversations and projects as before. Each operating system account's application data directory is written with owner-only permissions, so other accounts on the device cannot read it, and [Removing data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#removing-data) describes how to clear it. In the folder layout that [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md) describes, Claude for Government uses a single fixed organization ID. The Claude Desktop [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md#deploymentorganizationuuid) lists a `deploymentOrganizationUuid` key that separates local data by organization in other deployments. That key does not apply to Claude for Government, so leave it out of your [configuration profile](https://claude.com/docs/government/deploy-desktop/configure.md#deploy-to-your-fleet).

> **Where are files added to a project stored, and are they indexed?**
>
> A project in Claude for Government is stored in the application data directory on the user's own device, together with any instructions, links, and folder references the user adds to it. Files added to a project stay on the user's local disk; there is no service-side project store, and files are not vectorized or indexed. Claude reads them directly from disk on demand with its file tools. A new Cowork session in the project does not reuse what an earlier session read, so Claude reads the files it needs again. The project's [memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory) carries short notes between sessions, such as preferences and decisions, not the contents of the files. Content Claude reads from those files is handled like the rest of the conversation: inference requests pass through the Claude for Government service to the model endpoint but are not retained. See [Desktop and filesystem access](https://claude.com/docs/third-party/claude-desktop/local-access.md).

> **Can the local data location be changed for backup or sync?**
>
> No. The location is fixed to the per-user application data directory, and the application avoids the roaming profile because the sandbox image cache can be large. Chat history exists only on the device that created it, so back up the application data directory through your endpoint management tools if you need to preserve it. Artifacts and project folders are separate locations on the same device; see the question above. See [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md) for the folder layout.

### Web search and web fetch

> **How does web search reach the internet?**
>
> Web search is operated by Anthropic inside the Claude for Government FedRAMP High boundary, and the search provider's API is the one case where traffic egresses that boundary. Before search is enabled, an administrator must acknowledge a disclosure covering this data flow when enabling the **Web search** card on the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page. By default, users approve each query before it is sent, and Claude transforms it into a generic, de-identified search request and shows the user the exact text. Anthropic has a zero-data-retention agreement with the search provider. The [Web search and web fetch](https://claude.com/docs/third-party/claude-desktop/web-tools.md) page covers how web search is configured in other Claude Desktop deployments; the Claude for Government search path described here is specific to this deployment.

> **How do administrators enable web search?**
>
> Web search is built in and does not require obtaining a separate connector. An organization owner opens the [Config](https://claude.com/docs/government/config/settings.md#tool-and-connector-cards) page, finds the **Web search** card, turns it on, and acknowledges the data-flow notice. The **Require approval for each search** setting is on by default.

> **Why does Chat's web fetch fail with an empty allowlist?**
>
> Chat includes a web fetch tool, and every fetch is checked against the same egress allowlist that governs Cowork. With the allowlist empty or unset, a fetch to anything other than the Claude for Government service address (or, when configured, the **Telemetry endpoint** collector host) returns an error. Add hosts to **Allowed network hosts** on the [Config](https://claude.com/docs/government/config/settings.md#allowed-network-hosts) page to let Chat fetch from them, or turn off the **Web fetch** card on the same page if you prefer Claude not to see the tool. See [Web search and web fetch](https://claude.com/docs/third-party/claude-desktop/web-tools.md).

### Chat and Cowork differences

> **Are projects available in both Chat and Cowork?**
>
> Yes. Chat and Cowork share one list of projects, and users can start a Chat conversation or a Cowork session inside a project. A project in Claude for Government is stored only on the user's device. There is no service-side project store, and projects are not shared between users. Cowork sessions in a project use the same execution model as the rest of Cowork. Chat conversations in a project can read the project's [memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory). See [Data storage and retention](#data-storage-and-retention) for where project contents are stored.

> **Are artifacts available in Chat?**
>
> Yes. Artifacts are available in both Chat and Cowork. Claude creates an artifact by calling a tool when the output suits an interactive view, and the artifact opens in a side panel next to the conversation. Artifacts do not depend on the sandbox, so they remain available in Chat even when **Advanced file analysis** is disabled.

> **Where do files that Claude creates go?**
>
> In Chat and Cowork, Claude creates files on the user's device in places such as these:
>
> * A folder the user attached to a Cowork task.
> * The working folder that each task or conversation has inside the [application data directory](#data-storage-and-retention).
> * For artifacts, the user files directory (default `~/Claude`).
>
> Files that Claude saves in a working folder appear in the conversation as file cards that the user can open or show in Finder or File Explorer and copy from there. Code sessions work directly in the folder the user opened, as described under [Code in Claude Desktop](#code-in-claude-desktop).
>
> In Cowork, Claude's file tools change files in an attached folder in place, so the changes appear there immediately. A user who wants results in a particular folder attaches that folder to the task and asks Claude to save the files there. Shell commands run inside the sandbox virtual machine, and on the device they can write only to the attached folders and the task's working folder. A file that a command writes anywhere else in the virtual machine, for example under `/tmp`, does not appear in any folder on the device. See [Chat in Claude Desktop](https://claude.com/docs/third-party/claude-desktop/chat.md) for what a Chat conversation can reach, and [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md) for the folder layout.

## Claude Code command-line tool

The answers below cover the standalone Claude Code command-line tool when it signs in through Claude for Government, as [Connect Claude Code to Claude for Government](https://claude.com/docs/government/deploy-claude-code/configure.md) describes. The Claude Desktop answers above cover Code sessions inside Claude Desktop.

> **Which domains does Claude Code need to reach?**
>
> The Claude for Government gateway address in the managed settings from [Connect Claude Code to Claude for Government](https://claude.com/docs/government/deploy-claude-code/configure.md#the-managed-settings), over HTTPS on port 443, for sign-in, organization settings, and model inference. Sign-in finishes in the user's browser, which needs the Claude for Government host, its sign-in service, and your agency's identity provider, as for Claude Desktop. Claude Code also reaches, from the user's device, the address of each connector an administrator applies to **Claude Code** on the **Connectors** card, and that connector's sign-in service when it uses OAuth. The managed settings from [Connect Claude Code to Claude for Government](https://claude.com/docs/government/deploy-claude-code/configure.md#before-sign-in) turn off Claude Code's background connections before sign-in (release notes, update checks, and the official plugin marketplace).

> **Does Claude Code send telemetry to Anthropic?**
>
> No. The managed settings in [Connect Claude Code to Claude for Government](https://claude.com/docs/government/deploy-claude-code/configure.md#the-managed-settings) turn off Claude Code's usage telemetry and error reporting to Anthropic from the first launch, and the organization's settings keep them off after sign-in.

## More information

Assurance materials including the security architecture overview, SOC 2 Type 2 report, and penetration testing summary are available on request through the [Anthropic Trust Center](https://trust.anthropic.com).
