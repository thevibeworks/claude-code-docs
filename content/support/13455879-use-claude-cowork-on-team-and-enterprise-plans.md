# Use Claude Cowork on Team and Enterprise plans

This article explains important limitations and considerations for Team and Enterprise organizations using Claude Cowork.

## Availability

Claude Cowork is available for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows**

  - **Windows users:** Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

---

## Admin controls

Claude Cowork is on by default, but organization owners can manually disable it.

**How to enable or disable Cowork:**

1. Log in to your Team or Enterprise organization as an Owner or Primary Owner.

2. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

3. Locate the **Cowork** toggle.

4. Toggle off to disable Cowork for all users in your organization.

**Note:** This is an organization-wide setting. On Enterprise plans, you can use groups and custom roles to enable Cowork for specific teams. See **[Access controls](#h_8465b1b558)** below.

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

Project data (tasks and memory) is stored locally on each user's computer, consistent with how other Cowork data is handled. For full details, see **[Organize your tasks with projects in Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork).**

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

Cowork activity is **not captured** in the Compliance API at this time.

### Local conversation storage

Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard **[data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** and cannot be centrally managed or exported by admins.

### Access controls

The Cowork toggle is organization-wide—either all members have access or none do. On Enterprise plans, admins who need per-team control can use **[groups and custom roles](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)** to selectively enable Cowork for specific users or teams. Team plans don't have access to these controls, so Cowork remains all-or-nothing.

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