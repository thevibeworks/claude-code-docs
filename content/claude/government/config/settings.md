> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Available settings

> Config page settings in Claude for Government, such as session timeouts, network and folder access, tool approvals, connectors, plugins, telemetry, and updates.

> **Who this is for:** Tenant administrators and organization owners who set product behavior for the people they manage.

Find each setting on the **Config** page in the admin portal under its category in that page's sidebar. Each setting can be set at both the tenant and organization level unless noted otherwise. To set a value for a directory group, see [Group-specific settings](/docs/government/config/overview#group-specific-settings). For how the levels combine, what locking does, when a change reaches members, and how to compare and preview, see [How Config works](/docs/government/config/overview).

Where **Applies to** gives a version, earlier versions ignore the setting. The **Config** page can show settings that are not listed here.

## Product availability

These switches control which Claude products and features are available to members.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Claude Desktop** | Makes Claude Desktop available. | On | Claude Desktop |
| **Claude Desktop home** | Chooses what members see in Claude Desktop: **Standard**, **Simple**, **Chat only**, or **Off**. **Separate settings** leaves it to the Chat, file analysis, and Cowork switches. | **Separate settings** | Claude Desktop 1.52386.0 or later |
| **Chat in Claude Desktop** | Lets members chat with Claude in Claude Desktop, for quick questions and drafting. Without Chat, members cannot open their existing chats. | On | Claude Desktop |
| **Advanced file analysis in Chat** | Lets Claude run code in a sandbox for data analysis in Chat. Only takes effect where **Shell commands** and **Chat in Claude Desktop** are both on. Without this setting, Claude cannot read Word, Excel, or PowerPoint files that members attach in Chat. | On | Claude Desktop |
| **Cowork in Claude Desktop** | Lets members give Claude longer tasks, such as research, analysis, and drafting documents, which it works through on its own in Claude Desktop. Without Cowork, members cannot continue their Cowork tasks. | On | Claude Desktop |
| **Code in Claude Desktop** | Lets members use Claude Code inside Claude Desktop to write and run code. Without Code, members cannot open their existing Code sessions. | On | Claude Desktop |
| **Scheduled tasks** | Lets members set up [tasks that Claude runs on a schedule](/docs/third-party/claude-desktop/configuration#scheduledtasksenabled). Turning it off also turns off scheduling in Claude Code, such as `/loop`. | On | Claude Desktop 2.110.0 or later, Claude Code |
| **Claude Code** | Makes the [Claude Code command-line tool](/docs/government/deploy-claude-code/configure) available. | Off | Claude Code |
| **Claude for Microsoft 365** | Makes [Claude for Microsoft 365](/docs/government/deploy-microsoft-365/configure), the add-in for Excel, Word, and PowerPoint, available. | Off | Claude for Microsoft 365 |

Turning off **Claude Desktop**, **Claude Code**, or **Claude for Microsoft 365** stops the members the setting applies to from using that application. An organization cannot turn on a product that the tenant has turned off. These switches turn applications off, not accounts, and are not a security boundary: to cut one member off from everything at once, deactivate their account (see [Deactivated users](/docs/government/org-admin/users#deactivated-users)).

The **Claude Desktop home** row appears once your agency has access to it, and it then holds the Chat, Advanced file analysis, and Cowork switches. A choice other than **Separate settings** overrides those switches, unless a level above has locked one. If you choose **Off**, keep Code turned on, or Claude Desktop has nothing to open. Under **Separate settings**, if Chat, Cowork, and Code are all turned off, Claude Desktop keeps Cowork on.

## Sessions and access

These settings cover session limits, the network hosts and folders Claude Desktop may use, and Claude for Microsoft 365 features.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Session idle timeout** | How long a member can stay inactive before being signed out, from 15 to 5,760 minutes (96 hours). Organizations and groups can only set a shorter timeout than the tenant. | 1,440 minutes (24 hours) | All products |
| **Maximum session length** | The longest a member can stay signed in, even while active, before they have to sign in again, from 60 to 525,600 minutes (365 days). Each level can set or shorten the maximum but not lengthen it past what the level above allows. | No maximum | All products |
| [**Allowed network hosts**](#allowed-network-hosts) | A list of hostnames that tools in Claude Desktop may reach, for example to install packages or fetch web pages. | **Claude connection only** | Claude Desktop |
| **IPv6 in the sandbox** | Lets tools in the sandbox [reach IPv6-only hosts](/docs/third-party/claude-desktop/configuration#coworkvmipv6enabled) through the computer's own IPv6 connection. **Allowed network hosts** still applies. | Off | Claude Desktop 1.52386.0 or later on macOS and Windows |
| [**Allowed workspace folders**](#allowed-workspace-folders) | Which folders members can pick as a project folder in Claude Desktop. | **Any folder** | Claude Desktop |
| **Block reads outside workspace folders** | Stops Claude's file tools in Code sessions in Claude Desktop from reading files outside the session's project folder and any folders listed in **Allowed workspace folders**. Its effect on the shell commands Claude runs [differs by operating system](/docs/third-party/claude-desktop/code#applied-as-managed-policy). | Off | Claude Desktop 1.46388.1 or later |
| **Attach files to chat**, on the **Microsoft 365 features** card | Lets members attach files to chat by picking, dragging, or pasting them. | On | Claude for Microsoft 365 |
| **Accept all edits**, on the **Microsoft 365 features** card | Lets members switch to **Accept all edits**, where Claude makes most edits to the open file without asking. Turning it off also turns off **Skip all permissions**. | On | Claude for Microsoft 365 |
| **File access rules (Microsoft 365)** | Rules that block Claude on files with chosen Microsoft sensitivity labels, or block attaching them. A rule can **Block** matching files or **Allow only matching files**. If the add-in cannot read a file's label, the file counts as blocked for every feature that has a rule covering it. | None | Claude for Microsoft 365 |
| **Request headers (Claude for Microsoft 365)** | Extra headers Claude for Microsoft 365 sends with each request to Claude. Each member's add-in receives them. Headers are hidden after you save them. | None | Claude for Microsoft 365 |

**Maximum session length** always counts from when the member originally signed in, so a session that is already older than the new maximum ends when it [picks up the change](/docs/government/config/overview#when-changes-take-effect) and the member is prompted to sign in again. Your identity provider decides whether that sign-in asks the member to authenticate again or passes them straight through.

### Allowed network hosts

The list covers [web fetch and shell commands](/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) in Chat and Cowork, and the [sandboxed shell commands](/docs/government/security/security-and-data-handling#code-in-claude-desktop) of Code sessions on macOS and Linux. Web search, connectors, and the app's own connections do not use this list.

Entries are hostnames or wildcard patterns such as `*.example.com`, and match by name, not by the address a name resolves to.

### Allowed workspace folders

Check **Block all workspace folders** to allow none, in which case Claude can still work in Chat and Cowork in folders it creates inside its own sandbox. Subfolders of a listed folder are included. The setting does not stop the shell commands Claude runs in a Code session from reading files elsewhere on the device, and [Code in Claude Desktop](/docs/government/security/security-and-data-handling#code-in-claude-desktop) describes what confines those commands on each operating system.

* **Windows and Mac**: a list with only Windows entries leaves Mac users with no allowed folder, so include a Mac path as well, or one that starts with `~`, which stands for each member's home folder on both Windows and Mac.
* **Synced folders**: on Windows, `~/Documents` refers to the local Documents folder in the user profile, not one redirected to OneDrive. For that one, use [a variable](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) such as `%OneDriveCommercial%` or `%OneDrive%`. For Code sessions and other work that creates many files, consider listing a local folder that is not synced, such as `~/ClaudeWork`.

## Claude Code

Claude for Government delivers these settings to the command-line tool after a member signs in, and in Claude Desktop 2.9939.2 or later they can also reach Code sessions. While Claude Code is in [early access](/docs/government/deploy-claude-code/configure), the section appears once your agency has access.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Blocked shell commands** | Command names, such as `curl` or `ssh`, that Claude Code applies as [deny rules](https://code.claude.com/docs/en/permissions#bash) for its Bash and PowerShell tools. | None blocked | Claude Code |
| **Managed hooks** | [Hooks](https://code.claude.com/docs/en/hooks) that run in every member's Claude Code sessions, such as a command that writes an audit record after each tool use. | None | Claude Code |
| **Member-added hooks** | Whether hooks and custom status lines that members set up in their own or their projects' settings run as well. Managed hooks still run, and in Claude Desktop so do hooks inside plugins. | **Blocked** | Claude Code |
| **Plugin sources** | Where members can install Claude Code plugins from, one of **None**, **Approved sources only** with an **Approved plugin sources** list, or **Any source** with a **Blocked plugin sources** list. | **None** | Claude Code |
| **Sideloaded plugins** | Whether members can load plugins, agents, or connector files with a command-line flag. | **Blocked** | Claude Code command-line tool |
| **Minimum Claude Code version** | Claude Code below this version does not start and tells the member to update. | No minimum | Claude Code |
| **Maximum Claude Code version** | Claude Code above this version does not start. | No maximum | Claude Code |
| **Opening from the browser** | Whether Claude Code sets itself up to open from links in web pages and editors, with a prompt filled in. | **Blocked** | Claude Code |
| **Shell command sandbox** | Lets you turn off [Claude Code's sandbox](/docs/government/security/security-and-data-handling#code-in-claude-desktop) for workspaces where it cannot start, such as containers. | **Claude Code default**, which leaves that to Claude Code's own settings | Claude Code |

Two switches under [Integrations](#integrations) narrow **Any source**: while **Let members add plugin marketplaces** is off, members install only from the **Approved plugin sources** list, and while **Let members add their own plugins** is off, they cannot add a source of their own from a file or folder on their machine.

Settings in other categories govern Claude Code too, such as **Scheduled tasks** under [Product availability](#product-availability) and **Member-added connectors** under [Integrations](#integrations).

## Claude behavior

This setting shapes how Claude responds.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Organization instructions** | Instructions Claude follows for everyone in your organization, in every product. | None | All products |

Organization instructions guide how Claude responds, and they are not an enforced restriction. Members do not see the instructions in their applications. Instructions set at the organization level replace the tenant's instructions for that organization rather than adding to them. A change takes effect from each member's next message.

## Appearance

These settings change what members see in Claude Desktop.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Claude Desktop banner** | A persistent banner shown at the top of Claude Desktop. | Off | Claude Desktop |
| **Show the Claude for Government Web import banner** | Shows a banner on Claude Desktop's home screen inviting members to [import their conversations and projects from Claude for Government Web](/docs/government/desktop/import). Members see the banner only in organizations where Anthropic has enabled the import. | Off | Claude Desktop 2.9939.2 or later |

The system-use notification shown at sign-in is separate from the **Claude Desktop banner**. It is fixed text and cannot be edited.

## Integrations

The tool and connector cards and related settings cover connectors, plugins, and the tools Claude can use.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Web search** | Lets Claude search the web. Turning it on asks you to acknowledge a short description of [how search works](/docs/government/security/security-and-data-handling#web-search-and-web-fetch). | Off | Claude Desktop, Claude Code |
| **Require approval for each search** | Asks the member to approve every search before it runs. When this is off, each member chooses whether to approve each search or allow searches automatically. | On | Claude Desktop, Claude Code |
| **Microsoft 365** | The Microsoft 365 connector, which is separate from the Claude for Microsoft 365 add-in, lets members reach [your agency's Microsoft 365 content](/docs/government/connectors/microsoft-365), including SharePoint, OneDrive, Outlook, and Teams, from Claude Desktop. Each member signs in with their own Microsoft account. | Off until you enter a **Tenant ID** and **Client ID** | Claude Desktop |
| **Connectors** | [Connectors](/docs/government/connectors/overview) that let Claude reach your systems. Each is defined once and applied to the products you choose. | None | All products |
| **Member-added connectors**, on the **Connectors** card | Which other connectors members can use in Claude Code, beyond web search and the ones you add: **None**, **Only these**, or **Any connector**. | **None** | Claude Code, Claude Desktop 2.2553.0 or later |
| **Blocked connectors**, under **Any connector** | Connectors that Claude Code does not connect. Entries by server URL also block plugins' servers in Claude Desktop. An entry by **Server name** matches [the name a connector is given](https://code.claude.com/docs/en/managed-mcp#how-servername-entries-match), not the server it reaches. | None | Claude Code, Claude Desktop 2.16120.0 or later |
| **Plugins** | [Plugin packages](/docs/government/config/plugins-and-connectors) you upload and deliver to members in Claude Desktop. | None | Claude Desktop |
| **Let members add plugin marketplaces** | Lets members add plugin marketplaces and install plugins from them. While it is off, it also narrows [**Plugin sources**](#plugin-sources) in Claude Code. Marketplaces that members added earlier are hidden while it is off, which needs Claude Desktop 2.16120.0 or later. | Off | Claude Desktop, Claude Code |
| **Let members add their own plugins** | Lets members upload plugin files or have Claude create a plugin for them. While it is off, it also narrows [**Plugin sources**](#plugin-sources) in Claude Code. Plugins that members uploaded or created earlier stay installed. | Off | Claude Desktop, Claude Code |
| **Let members add their own connectors** | Lets members add connectors of their own in Claude Desktop, as local MCP servers under **Settings**, then **Developer**. While the switch is off, Claude Desktop ignores connectors that members already added under **Developer**. | Off | Claude Desktop |
| **Let members create skills** | Lets members [create or upload skills](/docs/third-party/claude-desktop/configuration#skillcreationenabled) of their own. Skills that members already made keep working. | On | Claude Desktop, Claude for Microsoft 365 |
| **Web fetch** | Lets Claude fetch web pages. See [**Allowed network hosts**](#allowed-network-hosts). | On | Claude Desktop, Claude Code |
| **Require approval for each fetch** | Asks the member to approve every page fetch before it runs. When this is off, fetches in Chat and Cowork run without asking, and Code sessions follow [Claude Code's usual permission rules](https://code.claude.com/docs/en/permissions). | Off | Claude Desktop, Claude Code |
| **Shell commands** | Lets Claude run shell commands during tasks. Turning this off also turns off **Advanced file analysis in Chat**. | On | Claude Desktop, Claude Code |
| **Require approval for each command** | In Claude Desktop, asks the member to approve every shell command before it runs. When this is off, commands [can run without asking](/docs/government/security/security-and-data-handling#approvals-and-auto-mode). | Off | Claude Desktop, Claude Code |
| **Terminal panel tools** | Lets Claude run commands in the Code tab's Terminal panel in Claude Desktop. These commands [run as the user outside of Claude's sandbox](/docs/government/security/security-and-data-handling#code-in-claude-desktop). Turning off **Shell commands** turns these tools off as well. | On | Claude Desktop |
| **Bypass-permissions mode** | Whether members can use the mode that skips permission prompts: bypass-permissions mode in Claude Code, **Skip all permissions** in Claude for Microsoft 365. | **Blocked** | Claude Code, Claude for Microsoft 365 |
| **Auto mode** | Whether members can switch to [Auto mode](https://code.claude.com/docs/en/permission-modes). [Approvals and Auto mode](/docs/government/security/security-and-data-handling#approvals-and-auto-mode) says which sessions start in it. | **Blocked** | Claude Code, Claude Desktop |

* **Member-added connectors**: in Claude Desktop it also governs connectors delivered inside plugins. A plugin's connector can connect only under **Any connector** or when listed under **Only these**.
* **Member-added connectors**, **Bypass-permissions mode**, and **Auto mode**: these take effect once your agency has the [**Claude Code**](#claude-code) section. In Claude for Microsoft 365, **Bypass-permissions mode** instead takes effect once your agency has the [**Microsoft 365 features**](#microsoft-365-features) card.

## Compliance and telemetry

These settings cover usage telemetry export to your own collector and Claude Desktop updates.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| [**Telemetry endpoint**](#telemetry-endpoint) | The base address of your [OpenTelemetry](https://opentelemetry.io/) collector, such as `https://otel-collector.example.gov:4318`. Each product adds its own paths and sends its telemetry directly from members' devices, so the collector must be reachable from their networks. | Empty, which turns telemetry off | All products |
| **Telemetry headers** | Headers each product sends with every telemetry request, such as an Authorization header carrying your collector's token. Each member's app receives these headers and sends its telemetry directly, so use a credential that can only send data to your collector. | None | All products |
| **Telemetry content capture** | [Content](/docs/third-party/claude-desktop/telemetry#content-capture) each product adds to the telemetry it sends to your collector: **Prompts**, **Claude's responses**, **Tool inputs**, **Tool results**, and **Full requests and responses**. Captured content goes only to your collector and is never sent to Anthropic. | No content captured | All products |
| **Application event level (Claude Desktop)** | How much of [Claude Desktop's own event log](/docs/third-party/claude-desktop/configuration#otlpdesktoploglevel) is sent to your collector, in addition to usage telemetry: **Off**, **Errors only**, **Warnings and errors**, **Informational**, or **Debug**. | **Errors only** | Claude Desktop |
| **Telemetry resource attributes** | Labels added to every telemetry record each product sends, such as your agency or environment name, so your collector can tell where each record comes from. | Not set | All products |
| **Telemetry traces** (beta) | Adds [traces](/docs/third-party/claude-desktop/telemetry#traces-beta), so that the events of one request can be followed together. Traces carry message and tool content only for the categories selected in **Telemetry content capture**. | Off | All products; Claude Desktop 1.22209.0 or later |
| **Block automatic updates** | Stops Claude Desktop from downloading and installing updates automatically. Turn this on only if your organization distributes Claude Desktop updates itself. For devices where no member is signed in, and for Linux, see [Automatic updates](/docs/government/deploy-desktop/configure#automatic-updates). | Off | Claude Desktop on macOS and Windows |
| **Restart deadline for updates** | How long a member can put off restarting Claude Desktop to install a downloaded update, from 1 to 72 hours. | [Claude Desktop's default](/docs/third-party/claude-desktop/configuration#autoupdaterenforcementhours) | Claude Desktop |
| **Restart deadline for configuration changes** | How long a member can put off restarting Claude Desktop after the app detects a configuration change, from 0 to 336 hours (14 days). | [Claude Desktop's default](/docs/third-party/claude-desktop/configuration#relaunchenforcementhours) | Claude Desktop |

* **Telemetry headers**: the headers you enter replace all of the saved ones when you save, so enter every header again when you add or change one.
* **Telemetry content capture**: **Tool results** adds tool output only while **Telemetry traces** is on. **Full requests and responses** can carry tool output with traces on or off.
* **Application event level (Claude Desktop)**: at **Informational** and **Debug**, the application events also include each conversation's title, and the title text is sent only when **Prompts** is selected in **Telemetry content capture**.
* **Telemetry resource attributes**: a list set at an organization or group replaces the inherited list, so repeat any attributes that should still apply.

### Telemetry endpoint

Once a member has signed in and the app has loaded their configuration from Claude for Government, it takes its telemetry settings from that configuration alone and ignores any set on the device itself. Claude Desktop keeps working when the collector refuses requests or cannot be reached, and members see no error. For what the collector must accept, and how to confirm that telemetry is arriving, see [Collector endpoint and headers](/docs/third-party/claude-desktop/telemetry#collector-endpoint-and-headers). For Claude for Microsoft 365, the collector must also accept [cross-origin requests from your Claude for Government host](/docs/government/deploy-microsoft-365/configure#before-you-begin).

Each record [identifies the member](/docs/third-party/claude-desktop/telemetry#user-attribution). See what [Claude Desktop](/docs/cowork/monitoring#events), [Claude for Microsoft 365](/docs/office-agents/opentelemetry#what-the-collector-receives), and [Claude Code](https://code.claude.com/docs/en/monitoring-usage) send.

## Admin Console

Only tenant administrators can change **Let organizations manage their own seat tiers** and **Compliance API**, which are read-only for organization owners.

| Setting | What it does | Default | Applies to |
| - | - | - | - |
| **Let organizations manage their own seat tiers** | Lets organization owners create and edit self-managed seat tiers on the [Tiers](/docs/government/org-admin/seat-tiers) page, in addition to the Anthropic-managed ones. When it is off, the **Reset usage limits** action on the [Users](/docs/government/org-admin/users) page is also unavailable. | On | Admin Console |
| **Compliance API** | Controls whether the [Compliance API](/docs/government/org-admin/compliance-api) is available. When this is off, requests are refused and existing keys stay listed so you can revoke them. | On | Admin Console |
| **Organization Analytics connector** | Makes the Organization Analytics connector available to organization owners in Claude Desktop. When this is off, requests to it are refused. | Off | Claude Desktop |
