> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Available settings

> Reference for the product settings on the Config page in Claude for Government, including session timeout, maximum session length, organization instructions, telemetry, automatic updates, Claude Desktop banner, product availability, and the tool and connector cards.

> **Who this is for:** Tenant administrators and organization owners who set product behavior for the people they manage.

This page describes the settings on the **Config** page in the admin portal. Each setting is written once here and can be set at both the tenant and organization level unless noted otherwise. For how the levels combine, what locking does, and how to compare and preview, see [How Config works](/docs/government/config/overview).

## Settings list

### Session idle timeout

Controls how long a member can stay inactive before being signed out. The value must be a whole number of minutes from 15 to 5,760 (96 hours), and the default is 1,440 minutes (24 hours) until your tenant sets a value. This is a restriction, so organizations and groups can only set a shorter timeout than the tenant.

### Maximum session length

Controls how long a member can stay signed in before they have to sign in again, even if they are active the whole time. The value must be a whole number of minutes from 60 to 525,600 (365 days), and by default there is no maximum. The maximum is an absolute limit on a session's lifetime that is independent of the session idle timeout, and a session ends as soon as it reaches either limit. This is a restriction, so each level can set or shorten the maximum but not lengthen it past what the level above allows, and the value that takes effect is always the shortest one in the chain.

A shorter maximum, or a new maximum where there was none before, also applies to members who are already signed in. Open sessions pick up the change while the member is active rather than instantly, so allow up to one session idle timeout period (24 hours by default) for it to reach everyone who is currently signed in. Any session that has not picked it up by then has already expired from inactivity. The maximum always counts from when the member originally signed in, so a session that is already older than the new maximum ends when it picks up the change and the member is prompted to sign in again. A longer maximum, or removing the maximum set at your level by clearing the value or resetting the setting, applies only at each member's next sign-in. Sessions that are already open keep the limit they already have, and raising or removing the maximum does not restore sessions that a shorter value has already shortened or ended.

When a session ends because it reached the maximum, the member signs in again, just as they do after the idle timeout. Your identity provider decides whether that sign-in asks the member to authenticate again (for example with a password, a multi-factor prompt, or a PIV card) or passes them straight through, according to its own session and re-authentication policy. Examples of that policy are the sign-in frequency control in Microsoft Entra Conditional Access and authentication policies in Okta. If you want members to authenticate again when they sign back in after reaching the maximum, set your identity provider's re-authentication interval to no longer than the maximum session length.

### Let organizations manage their own seat tiers

Controls whether organization owners may create and edit self-managed seat tiers on the [Tiers](/docs/government/org-admin/seat-tiers) page, in addition to the Anthropic-managed ones. Only tenant administrators can change this setting; it is always read-only at the organization level, and organization owners cannot grant themselves the capability. When it is off, the **New seat tier** button and the edit and delete controls on the Tiers page are hidden, and the **Reset usage limits** action on the [Users](/docs/government/org-admin/users) page is also unavailable.

<Note>
  **Set at the tenant level only.** This setting is read-only for organization owners.
</Note>

### Compliance API

Controls whether the [Compliance API](/docs/government/org-admin/compliance-api) is available. When it is off, organization owners cannot create new keys and every request to the API returns an error, including requests made with keys that were valid before. Listing and revoking existing keys remains available even when this is off, so that a disabled organization can still revoke an exposed key.

<Note>
  **Set at the tenant level only.** This setting is read-only for organization owners.
</Note>

### Organization instructions

Instructions that Claude follows for everyone in your organization, in every product: Claude Desktop (Chat, Cowork, and Code), the Claude Code command-line tool, and Claude for Microsoft 365. Use them for rules that should apply to every conversation, such as compliance requirements, data handling, or formatting standards. Enter the instructions as plain text.

A change takes effect from each member's next message, including in conversations that are already open, and needs no application update or restart. Members do not see the instructions in their applications. Instructions set at the organization level replace the tenant's instructions for that organization rather than adding to them, so repeat anything from the tenant level that should still apply. A tenant administrator who wants the same instructions in every organization can set them at the tenant level and [lock](/docs/government/config/overview#locks) the setting.

Organization instructions guide how Claude responds, and they are not an enforced restriction. To restrict what Claude can do, for example which network hosts it can reach, use **Allowed network hosts** and the other settings on this page.

<Note>
  **Set at the tenant and organization levels only.** This setting cannot be set for a group.
</Note>

### Telemetry endpoint (Claude Desktop)

The base address of the collector where Claude Desktop sends usage telemetry using the [OpenTelemetry](https://opentelemetry.io/) protocol (OTLP), for example `https://otel-collector.example.gov:4318`. Claude Desktop appends the OTLP request paths `/v1/logs` and `/v1/metrics` itself, so enter the address without those suffixes. Leaving the value empty disables telemetry.

The value must begin with `https://` and may include a port and a path prefix. Its host must be a hostname or a private-network address, and a public IP address is refused. A matching **Telemetry endpoint (Claude for Microsoft 365)** setting covers that product.

Point this address at a receiver that accepts OTLP over HTTP in both its protobuf and JSON encodings. An [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) does this by default and conventionally listens for OTLP over HTTP on port 4318. If your logging or SIEM platform accepts only its own HTTP ingestion format, run an OpenTelemetry Collector that receives OTLP and forwards to that platform, and enter the collector's address here.

Claude Desktop on each member's device connects to this address itself rather than through the Claude for Government service. The collector must therefore be reachable from your members' networks and must present a TLS certificate that their operating system trusts.

Members pick up a new or changed endpoint the next time they start Claude Desktop. From then on your collector receives OpenTelemetry logs and metrics for each member's activity under three `service.name` values:

* `cowork` for Chat and Cowork activity
* `claude-code-desktop` for Code sessions
* `claude-desktop` for error events from the application itself

Each conversation turn produces events such as `user_prompt`, `api_request`, and `tool_result` that record the model, token counts, durations, and tool names. Every record also carries the member's operating-system login name as the `enduser.id` and `process.owner` resource attributes. Message text, file contents, and tool output are not included. See the [event reference in Monitoring](/docs/cowork/monitoring#events) for each event's attributes.

Claude Desktop keeps working when the collector refuses requests or cannot be reached, and members see no error. To confirm telemetry is arriving, check your collector's own request logs or metrics for requests to `/v1/logs` after a member has restarted Claude Desktop and sent a message.

### Telemetry headers (Claude Desktop)

Headers that Claude Desktop sends with every telemetry request, typically the credential your collector requires. Leave the setting empty if your collector does not require one. Because the value may contain a secret, it is never displayed after you save it; you see only that it is set.

Write each header as `Name=value`, for example `Authorization=Bearer <token>`. To send more than one header, separate them with commas, as in `Authorization=Bearer <token>,X-Tenant=agency`. Because the comma is the separator, a header value itself cannot contain one. Spaces and `=` characters within a value are fine.

### Block automatic updates

Stops Claude Desktop from downloading and installing updates automatically. It is off by default, so Claude Desktop keeps itself updated. Turn it on only if your agency distributes Claude Desktop updates itself, and [lock](/docs/government/config/overview#locks) it if the levels below yours should not be able to turn updates back on.

Claude Desktop applies this setting once a member has signed in and the app has loaded their configuration from Claude for Government. With that configuration loaded, the app follows this setting even when it is off, so a `disableAutoUpdates` value in the device's configuration profile does not stop a signed-in member's app from updating. When the app starts without a signed-in member, for example on a newly deployed device or when a member has to sign in again because their session expired, it follows the profile value instead, if one is set. To make sure devices never update themselves, turn this setting on and also have your IT administrators set `disableAutoUpdates` in the profile, as described under [Automatic updates](/docs/government/deploy-desktop/configure#automatic-updates) on the Connect Claude Desktop to Claude for Government page.

### Restart deadline for updates

How long a member can put off restarting Claude Desktop to install an update that the app has downloaded, as a whole number of hours from 1 to 72. When the deadline passes, the app restarts to install the update without waiting for the computer to be idle. Leave the value empty to allow 72 hours, after which the app restarts only once the computer is idle. While **Block automatic updates** is on, this setting has no effect, because the app downloads no updates.

<Note>
  Members who are running Claude Desktop when you change **Block automatic updates** or **Restart deadline for updates** may need to restart the app to pick up the change.
</Note>

### Claude Desktop banner

A persistent banner shown at the top of Claude Desktop. You can set the text, colors, and an optional link, and preview the result as you edit. Banner text may be up to 200 characters, leading and trailing spaces are rejected, colors must be valid hex codes, and the link (if set) must begin with `https://`. An empty banner is valid and simply hides it.

The system-use notification shown at sign-in is separate from this banner. It is fixed text and cannot be edited. Use the Claude Desktop banner setting if you need a configurable message inside the application.

### Product availability

A group of separate switches that control which Claude products and features are available to members. Each switch appears as its own row: **Claude Desktop**, **Chat in Claude Desktop**, **Advanced file analysis in Chat**, **Cowork in Claude Desktop**, **Code in Claude Desktop**, **Claude Code**, and **Claude for Microsoft 365**. All are on by default.

Turning off one of the three product switches (**Claude Desktop**, **Claude Code**, or **Claude for Microsoft 365**) makes Claude for Government stop serving that application your organization's configuration. From then on, Claude Desktop and the Claude for Microsoft 365 add-in are refused the organization's configuration when they request it, and Claude Code that is signed in to Claude for Government exits when it next starts (or right after sign-in) with a message that it couldn't load settings from the cloud gateway. Claude Code that is already running is not cut off and keeps working until it is next started. The product switches are not an access control on the Claude for Government service itself. What a member can reach is governed by their account, their [seat tier](/docs/government/org-admin/seat-tiers), and your agency's device and network management. To cut a member off at once, deactivate their account, after which they cannot sign in and requests from their existing sign-ins are refused (see [Deactivated users](/docs/government/org-admin/users#deactivated-users)). Turning off one of the other four switches removes that feature from Claude Desktop, as described below.

The **Chat in Claude Desktop**, **Cowork in Claude Desktop**, and **Code in Claude Desktop** switches each make one part of the app available to members. Chat is for simple conversations, Cowork is for longer tasks that Claude works through on its own in a local workspace folder, and Code is for software development. The **Claude Code** switch is separate and applies to the standalone Claude Code command-line tool.

When Chat and Cowork are both available, Claude Desktop presents them together as **Home** in its sidebar, next to **Code**. From Home, a member chooses **Chat** or **Cowork** in the message box, and the sidebar lists their chats and tasks together.

Turning a switch off also changes this layout. For example, with **Chat in Claude Desktop** off, the sidebar shows **Cowork** in place of Home and the message box offers no choice, and with **Cowork in Claude Desktop** off, the message box offers Chat only. If Chat, Cowork, and Code are all turned off, Claude Desktop keeps Cowork on. There is no setting that chooses what Claude Desktop opens to, or whether the message box starts on Chat or Cowork.

<Note>
  This layout applies to Claude Desktop 1.26832.0 and later. Earlier versions show **Chat**, **Cowork**, and **Code** as three separate tabs, controlled by the same switches.
</Note>

### Allowed network hosts

A list of hostnames that tools in Claude Desktop may reach, for example to install packages or fetch web pages. This covers the tools Claude uses during Cowork tasks, web fetch in Chat, and the sandboxed shell commands of Code sessions on macOS. For how the list applies to Code sessions on each operating system, see [Code in Claude Desktop](/docs/government/security/security-and-data-handling#code-in-claude-desktop). The connection to Claude is always allowed and does not need to be listed. An empty list shows as **Claude connection only**. Use **Add package registries** to add npm, PyPI, GitHub, crates.io, and other common registries so that Claude can install libraries; hosts added this way appear together as a single **Package registries** pill with a count.

Entries are hostnames or wildcard patterns such as `*.example.com`, which matches subdomains at any depth but not `example.com` itself, so list both if you need both. The list does not accept IP addresses or ports, and unless you allow all traffic with a `*` entry, the tools this list covers cannot reach a destination by its IP address. Web search, connectors, and the app's own connections, such as sign-in, updates, and telemetry export, do not use this list. Web fetch refuses localhost and private-network addresses regardless of what the list contains. Because entries match by name, a hostname you list is reachable even when it resolves inside your network, so treat the list as one layer alongside your own network controls.

### Allowed workspace folders

Controls which folders members can pick as a project folder in Claude Desktop, and where Claude can read and write files. Leave it unset to allow any folder. Add folder paths to limit members to those locations, or check **Block all workspace folders** to allow none, in which case Claude can still work in Chat and Cowork in folders it creates inside its own sandbox. A Code session starts only in a folder this setting permits, and [Code in Claude Desktop](/docs/government/security/security-and-data-handling#code-in-claude-desktop) describes how the setting applies to Code sessions on each operating system. You can list Windows and Mac paths together, and each device uses only the paths for its platform. An unset value shows as **Any folder** and an empty list shows as **No folders**.

Write each entry as an absolute path. A path can start with `~`, which stands for each member's home folder on both Windows and Mac; write these with forward slashes, for example `~/ClaudeWork`, and they resolve on both platforms. A path can also use one of the per-user variables `%OneDrive%`, `%OneDriveCommercial%`, `%OneDriveConsumer%`, `%APPDATA%`, `%LOCALAPPDATA%`, and `%USERNAME%`. A device ignores an entry whose variable it does not define, so a list with only Windows entries leaves Mac users with no allowed folder. Include a `~` path or a Mac path as well. Subfolders of a listed folder are included, Claude Desktop creates a listed folder that does not exist yet when a member opens the folder picker, and the picker opens in one of the listed folders.

If your agency redirects Desktop and Documents to OneDrive or another sync client, consider listing a local folder that is not synced, such as `~/ClaudeWork`, for Code sessions and other work that creates many files or scripts. Keep synced folders for documents and finished work. To point at the synced Documents folder on Windows, use `%OneDriveCommercial%` or `%OneDrive%`, for example `%OneDriveCommercial%\Documents\ClaudeOutput`, because `~/Documents` refers to the local Documents folder in the user profile, not the redirected one. What the sync client uploads, including whether it skips particular file types, is controlled by your sync client's policies rather than by Claude for Government.

## Tool and connector cards

Alongside the settings list, the Config page shows cards for the built-in tools (Web search, Web fetch, and Shell commands), the built-in connector (Microsoft 365), a **Connectors** card for the ones you add yourself, and a **Plugins** card for plugin packages you upload. A connector is an integration that lets Claude reach an external service on a user's behalf.

The **Web search** card controls whether Claude can search the web in Claude Desktop. It is off by default. When you turn it on you are shown a short description of how search works and asked to acknowledge it before the setting is saved. A **Require approval for each search** sub-setting sits below the toggle and becomes available once web search is on; it is on by default, and turning it off lets each member choose whether to approve every search or allow searches to run automatically.

Once you turn web search on, each member's Claude Desktop picks it up the next time the app starts and shows it in the message box's **+** menu, under **Connectors**, as a **Web Search** switch that the member can turn off for themselves. If one member has no **Web Search** switch after restarting Claude Desktop while others do, select [**Compare config across levels**](/docs/government/config/overview#comparing-settings-across-levels) at the top of the Config page and type the member's name into the search box to check whether another level, such as a [directory group](/docs/government/config/overview#group-specific-settings), turns web search off for them. If every level shows web search on, check whether that member's network is blocking it, as described in the troubleshooting table in [Connect Claude Desktop to Claude for Government](/docs/government/deploy-desktop/configure#troubleshooting).

The **Web fetch** card controls whether Claude can fetch web pages in Claude Desktop. It is on by default, and fetches are subject to the Allowed network hosts list above. A **Require approval for each fetch** sub-setting sits below the toggle. Turning it on asks the member to approve every page fetch before it runs; when it is off (the default), each member chooses whether to approve fetches or allow them automatically.

The **Shell commands** card controls whether Claude can run shell commands during tasks in Claude Desktop. It is on by default, and turning it off also turns off Advanced file analysis in Chat. A **Require approval for each command** sub-setting sits below the toggle. Turning it on asks the member to approve every shell command before it runs; when it is off (the default), each member chooses whether to approve commands or allow them automatically. Chat always asks before each command regardless of this setting.

The **Microsoft 365** card lets members reach your agency's Microsoft 365 content, including SharePoint, OneDrive, Outlook, and Teams, from Claude Desktop. Each member signs in with their own Microsoft account. Enter the **Tenant ID** and **Client ID** from an application you register in Microsoft Entra, choose the **Azure cloud** your Microsoft tenant is in, and select which Microsoft Graph permissions to allow under **Access**. The connector is off while Tenant ID and Client ID are both blank. See [Set up the Microsoft 365 connector](/docs/government/connectors/microsoft-365) for the full walkthrough.

The **Connectors** card lists the Model Context Protocol servers you have added for your own systems. Each connector is defined once and applied to the products you choose. See the [Connectors](/docs/government/connectors/overview) page for how to add and manage them.

The **Plugins** card lets you upload plugin packages and deliver them to members in Claude Desktop. A plugin bundles skills, slash commands, and sub-agents for Claude Desktop, and can also carry hooks and declare connectors; see [Manage plugins and connectors](/docs/government/config/plugins-and-connectors) for how each component behaves in Claude for Government and the [Plugins overview](/docs/plugins/overview) for what a plugin can contain. Plugins are delivered only to Claude Desktop.

Click **Add plugins** and drop a `.zip` file. The file can be a single plugin package or a whole marketplace archive, for example the **Download ZIP** of a GitHub repository that holds several plugins. A preview shows each plugin's name, version, and description, and marks any plugin that declares components that can run code on the member's machine, for example hooks or an MCP server. In Claude for Government, a plugin's hooks run on the member's machine at defined points during a session; a plugin's declared local MCP server is disabled and does not run. For those plugins, you confirm that you trust the package before it is added. See [Plugins that run code](/docs/government/config/plugins-and-connectors#plugins-that-run-code) for what the marker means and how these components behave in Claude for Government.

Each plugin you add appears as a row with an **Auto-install** or **Members choose** control. **Auto-install** installs the plugin for every member automatically, and **Members choose** makes it available for members to install themselves. Click the remove icon to queue a plugin for removal. Changes you make in these rows are staged: nothing is applied until you click **Save changes**, and **Discard** clears the pending changes. Plugins you add through the **Add plugins** dialog take effect as soon as you confirm them in that dialog. Removing a plugin stops delivering it, and members who already installed it keep their copy until they remove it themselves.

At the organization level, plugins the tenant has added appear under a **From levels above** heading with an **Inherited from your tenant** badge. You can see them there but cannot change or remove them. Upload a plugin with the same name at your organization level to take priority over one.

<Tip>
  The Claude for Government deployment may include additional settings that are not listed above. Any extra setting follows the same chain, status badges, and edit and reset behavior.
</Tip>
