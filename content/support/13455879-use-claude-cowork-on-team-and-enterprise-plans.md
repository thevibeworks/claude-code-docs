# Use Claude Cowork on Team and Enterprise plans

This article explains important limitations and considerations for Team and Enterprise organizations using Claude Cowork.

## Availability

Claude Cowork is available for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows**

  - **Windows users:** Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

- **Web**, at claude.ai

- **Claude Mobile**, in the latest version of Claude for iOS and Claude for Android

Starting August 3, 2026, Claude Cowork is in beta on web and mobile for Team and Enterprise plans. On web and mobile, Claude Cowork sessions run in Anthropic's cloud.

---

## Where Cowork runs

During the beta, Cowork sessions can run in two places:

- **Sessions in the cloud (beta starting August 3, 2026):** Running Cowork in the cloud lets members run tasks on Anthropic's infrastructure instead of their own machines. This means work continues across desktop, web, and mobile and scheduled tasks run when the laptop closes and no device is online.

- **Local sessions:** Claude's work runs on the user’s computer, with code in an isolated virtual machine.

## Admin controls

Claude Cowork is on by default, but organization owners can manually disable it.

### Enable or disable Cowork

1. Log in to your Team or Enterprise organization as an Owner or Primary Owner.

2. Navigate to **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)**.

3. Locate the **Enable for your organization** toggle under **Cowork**.

4. Toggle off to disable Cowork for all users in your organization.

This toggle controls whether Cowork is available at all. Whether sessions can run in the cloud is a separate control.

**Note:** This is an organization-wide setting. On Enterprise plans, you can use groups and custom roles to enable Cowork for specific teams. See **[Access controls](#h_8465b1b558)** below.

### **Enable or disable sessions in the cloud**

For Team and Enterprise plans, there's a separate organization-wide toggle in **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)** under "Run Cowork in the cloud."

- **Team plans:** on by default. An owner can turn it off any time from the "Run Cowork in the cloud" toggle.

- **Enterprise plans:** off by default. An owner turns on "Run Cowork in the cloud," then grants the Cowork in the cloud capability to a group with custom roles. See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

### Connector tool approvals

The organization setting **Allow "Always allow" for connector tools** in **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)** (under **Permissions**) controls whether members can skip per-task approval for write-capable connector tools in Cowork. This setting is off by default.

When the setting is off:

- The "Allow for all tasks" option appears grayed out in Cowork's approval dialog, even when your organization-wide tool policies allow these tools.

- Previously saved always-allow preferences for write tools aren't honored. Members approve these tools per task until the setting is turned on.

Read-only tools are exempt only when the connector annotates them as read-only. Most custom connectors don't annotate their tools, so every tool on those connectors is gated.

On Enterprise plans, this setting works alongside custom role grants, and the most restrictive layer wins. Role grants can't override it. For the full layering model, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_979e558d00)**.

### Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

For details on what members can do with plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

---

## Projects

Projects in Cowork let users organize tasks into dedicated workspaces with their own files, links, instructions, and memory. Projects are available to all Cowork users. There are no separate admin controls for projects, so owners cannot restrict project creation at the organization level at this time.

Projects are available wherever members use Cowork. Projects tied to a local folder support Cowork sessions on desktop only. For local sessions, project data is stored on the user's computer; for sessions in the cloud, projects are saved with the member's Claude account. For full details, see **[Organize your tasks with projects in Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork).**

---

## Manage plugins for your organization

Owners can create plugin marketplaces to distribute curated plugins across their organization. This gives you control over which plugins your team members see and use in Cowork.

- **Installed by default** — Automatically added for everyone in your organization. Members can uninstall if they choose.

- **Available** — Appears in the plugin catalog for members to install on their own.

- **Required** — Automatically installed for all members. Members cannot uninstall it.

- **Not available** — Hidden from the catalog. Useful for staging or deprecating plugins.

On Enterprise plans, admins can also override these preferences for specific groups—for example, auto-installing a plugin for one team while hiding it from everyone else. For details, see **[Manage Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

---

## Company branding

Cowork now surfaces your organization's branding, including a redesigned home screen tailored to your team. Team and Enterprise owners can configure branding within **Organization settings**.

---

## Compliance and monitoring

Team and Enterprise owners can stream Cowork events to your SIEM and observability tools through OpenTelemetry. This gives security teams visibility into tool calls, file access, human approval decisions, and more—though it doesn't replace audit logging for compliance purposes. For setup, supported events, and security considerations, see **[Monitor Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-cowork-activity-with-opentelemetry).**

You can also refer to **[Monitoring](https://claude.com/docs/cowork/monitoring)** in our Claude Docs for more information.

Cowork via mobile and web is captured in the Compliance API. Learn more about **[retrieving remote sessions in the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)**.

### Local conversation storage

For local sessions, Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard **[data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** and cannot be centrally managed or exported by admins.
​
For sessions in the cloud, your sessions and files are saved to your Claude account.

### Access controls

The Cowork toggle is organization-wide—either all members have access or none do. On Enterprise plans, admins who need per-team control can use **[groups and custom roles](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)** to selectively enable Cowork or grant the "Run Cowork in the cloud" capability to specific users or teams. Team plans don't have access to these controls, so Cowork remains all-or-nothing.

Within Cowork, admins have more granular control over plugins. You can set per-plugin installation preferences to control which plugins are auto-installed, available for self-service, or hidden from your organization's catalog. On Enterprise plans, these preferences can also be customized per group. See **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)** for details.

---

## Security considerations

### Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. While we've implemented safety measures including model training and content classifiers, the risk of prompt injection attacks is non-zero.

Users should:

- Avoid granting access to files with sensitive information

- Monitor Claude for suspicious actions

- Limit browser and web access to trusted sources

- Report suspicious behavior immediately

For detailed guidance, see **[Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)**.

### Network access

Cowork respects your organization's current network egress permissions. Review your network access settings in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** under **Code execution** before enabling Cowork.

Network settings are applied when a new Cowork session is created. If you change the network access mode or add domains to the allowlist while a conversation is already active, those changes will not take effect in that session. Start a new conversation for the updated settings to apply.

**Important:** Network egress permissions don't apply to the web fetch or **[web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)** tools or MCPs, including Claude in Chrome. Web fetch runs server-side and is limited to search results and URLs you've shared. Team or Enterprise plan owners can turn off web search for Cowork and Chat in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**, or Claude in Chrome via **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension)**.