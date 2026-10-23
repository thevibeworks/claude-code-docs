# Use Claude Cowork on Team and Enterprise plans

This article explains important limitations and considerations for Team and Enterprise organizations using Claude Cowork.

## Availability

Claude Cowork is available on paid plans (Pro, Max, Team, and Enterprise):

- **Claude Desktop for macOS, Windows, and Linux (beta):** All paid plans. Download or update at **claude.com/download**.

- **Web and Claude Mobile:** Pro, Max, and Team plans (in beta on Team), and Enterprise plans when an owner enables it.

- **Claude in Chrome side panel:** All paid plans. On Enterprise plans, an owner needs to enable Claude in Chrome and Cowork in the cloud. See **[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173)**.

The new Claude experience, which combines chat and Cowork, is rolling out to Pro and Max plans. On Team plans (in beta) and Enterprise plans, it's available where **Chat and Cowork unified** is turned on. Organizations that haven't turned it on keep chat and Cowork as separate options, so this article still applies. Enterprise owners can learn more in **[Set up and manage the new unified Claude experience for your Enterprise organization](https://support.claude.com/en/articles/17444462)**.

---

## Where Cowork runs

On Team and Enterprise plans, Cowork sessions can run in two places:

- **Sessions in the cloud:** Running Cowork in the cloud lets members run tasks on Anthropic's infrastructure instead of their own machines. This means work continues across desktop, web, and mobile and scheduled tasks run when the laptop closes and no device is online.

- **Local sessions:** Claude's work runs on the user’s computer, with code in an isolated virtual machine.

## Admin controls

Claude Cowork is on by default, but organization owners can manually disable it. In organizations that have enabled HIPAA, Cowork is off by default. An Owner can turn on Cowork in **Organization settings > Cowork**.

### Enable or disable Cowork

1. Log in to your Team or Enterprise organization as an Owner or Primary Owner.

2. Navigate to **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)**.

3. Locate the **Enable for your organization** toggle under **Cowork**.

4. Toggle off to disable Cowork for all users in your organization.

This toggle controls whether Cowork is available at all. Whether sessions can run in the cloud is a separate control.

**Note:** This is an organization-wide setting. On Enterprise plans, you can use groups and custom roles to enable Cowork for specific teams. See **[Access controls](#h_8465b1b558)** below.

### Enable or disable sessions in the cloud

For Team and Enterprise plans, there's a separate organization-wide toggle in **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)** under "Run Cowork in the cloud."

- **Team plans:** on by default. An owner can turn it off any time from the "Run Cowork in the cloud" toggle.

- **Enterprise plans:** off by default. An owner turns on "Run Cowork in the cloud," then grants the Cowork in the cloud capability to a group with custom roles. See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**. With the HIPAA configuration applied to Claude Code (local mode) and Cowork (local mode), Cowork in the cloud isn't available, and no setting turns it on.

### Enable or disable the built-in browser

Claude can use the web in Cowork in two ways: a browser built into the Claude Desktop app, or your users' own Chrome browser through the Claude in Chrome extension. You can enable one, both, or neither.

- **Built-in browser:** Controlled from **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)**. On Team plans, it's on by default. Team owners can turn it off anytime. On Enterprise plans, it's on by default unless you've turned it off. In organizations that have enabled HIPAA, the built-in browser stays off until an Owner turns it on in **Organization settings > Cowork**. With the **[HIPAA configuration applied to Claude Code (local mode) and Cowork (local mode)](https://support.claude.com/en/articles/17318731)**, the built-in browser isn't available, and no setting turns it on. When it's off, users can't open the built-in browser and Claude can't use it.

- **Claude in Chrome:** Controlled from **[Organization settings > Claude in Chrome](https://claude.ai/admin-settings/browser-extension)**, and users' browsers still need the extension deployed or installed. See **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128)**.

Both run the same safety layers: a blocklist for high-risk sites and safety checks on every action. The built-in browser needs the Claude Desktop app open and online; Claude in Chrome needs the extension installed in the user's browser. Browser traffic comes from the user's machine, where the desktop app runs. To site operators it looks like traffic from that device, even when the session is steered from web or mobile.

Learn more in **[Use the built-in browser in Claude Cowork](https://support.claude.com/en/articles/16607400)**.

### Auto mode availability

Two organization settings in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** control "Automatically approve" mode in Cowork:

- **Allow "Automatically approve" mode** controls whether members can use the mode. This setting is on by default, so the mode is available to your members unless you turn it off. When it's off, "Automatically approve" doesn't appear in your members' mode selector.

- **Start new tasks in "Automatically approve" mode** controls whether new Cowork tasks start in that mode. It’s on by default on Pro, Max, and Team plans, and off by default on Enterprise plans. Turn it off to keep "Manually approve" as the default.

Members can switch modes within any session.

Learn more about how the modes differ in **[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork#h_e1353133dd)**.

### Connector tool approvals

The organization setting **Allow "Always allow" for connector tools** in **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)** (under **Permissions**) controls whether members can skip per-task approval for write-capable connector tools in Cowork. This setting is off by default.

When the setting is off:

- The "Allow for all tasks" option appears grayed out in Cowork's approval dialog, even when your organization-wide tool policies allow these tools.

- Previously saved always-allow preferences for write tools aren't honored. Members approve these tools per task until the setting is turned on.

Read-only tools are exempt only when the connector annotates them as read-only. Most custom connectors don't annotate their tools, so every tool on those connectors is gated.

On Enterprise plans, this setting works alongside custom role grants, and the most restrictive layer wins. Role grants can't override it. For the full layering model, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_979e558d00)**.

### Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

For details on what members can do with plugins, see **[Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

---

## Projects

Projects in Cowork let users organize tasks into dedicated workspaces with their own files, links, instructions, and memory. Projects are available to all Cowork users. There are no separate admin controls for projects, so owners cannot restrict project creation at the organization level at this time.

Projects are available wherever members use Cowork. Projects tied to a local folder support Cowork sessions on desktop only. For local sessions, project data is stored on the user's computer; for sessions in the cloud, projects are saved with the member's Claude account. For full details, see **[Organize your tasks with projects in Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork).**

---

## Manage plugins for your organization

Owners can create plugin marketplaces to distribute curated plugins across their organization. This gives you control over which plugins users see and use in chat, Cowork, and Claude Code (for users who sign in to Claude Code with their Claude account).

- **Installed by default** — Automatically added for everyone in your organization. Members can turn it off if they choose.

- **Available to install** — Appears on the **Discover** tab for members to add on their own.

- **Required** — Automatically installed for all members. Members can’t turn it off or remove it.

- **Not available** — Hidden from members. Useful for staging or deprecating plugins.

On Enterprise plans, admins can also override these preferences for specific groups—for example, auto-installing a plugin for one team while hiding it from everyone else. For details, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

---

## Company branding

Cowork now surfaces your organization's branding, including a redesigned home screen tailored to your team. Team and Enterprise owners can configure branding within **Organization settings**.

---

## Security, compliance, and monitoring

**Note:** For the most up-to-date and extensive guide see **[Cowork security best practices](https://trust.anthropic.com/resources?s=uukz8hyx7jmdmo80lys36s&name=claude-cowork-security-best-practices)**.

**Important:** On a HIPAA-ready Enterprise plan, after the Primary Owner applies the HIPAA configuration to Claude Code (local mode) and Cowork (local mode), your Business Associate Agreement (BAA) covers Cowork sessions in Claude Desktop. Without that configuration, Cowork is available but not covered under your BAA. With that configuration applied, Cowork in the cloud isn't available. See **[Use Claude Code (local mode) and Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731)**.

### Monitoring

**Compliance API**

Cowork sessions via Claude, Claude Desktop, and Claude Mobile are captured in the Compliance API. Learn more about **[retrieving remote sessions in the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)**.

**Local conversation storage**

For local sessions, Cowork stores conversation history on users' computers. This data is not subject to Anthropic's standard **[data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**, and admins cannot centrally manage or delete it. Claude Enterprise admins can retrieve this content through the Compliance API. Deletion endpoints for local sessions aren't available yet. In organizations that have enabled HIPAA and turned on the Compliance API, Anthropic captures Cowork sessions that run on members' computers, so that your organization can retrieve them through the Compliance API. The Compliance API returns sessions from the most recent 30 days. If your organization's retention period is shorter than 30 days, the Compliance API returns sessions from that period.

For sessions in the cloud, sessions and files are saved to the member's Claude account.

**OpenTelemetry**

Team and Enterprise owners can stream Cowork events to your SIEM and observability tools through OpenTelemetry. This gives security teams visibility into tool calls, file access, human approval decisions, and more. It doesn't replace audit logging for compliance purposes.

For setup, supported events, and security considerations, see **[Monitor Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-cowork-activity-with-opentelemetry)**. You can also refer to **[Monitoring](https://claude.com/docs/cowork/monitoring)** in our Claude Docs.

### Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. We've implemented safety measures including model training and content classifiers, but the risk of prompt injection attacks is non-zero.

Users should:

- Avoid granting access to files with sensitive information

- Monitor Claude for suspicious actions

- Limit browser and web access to trusted sources

- Report suspicious behavior immediately

### Network access

Cowork respects your organization's current network egress permissions. Before enabling Cowork, review your network access settings in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** under **Code execution**.

Network settings are applied when a new Cowork session is created. If you change the network access mode or add domains to the allowlist during an active conversation, those changes won't take effect in that session. Start a new conversation for the updated settings to apply.

Network egress permissions don't apply to the web fetch or **[web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)** tools, or to MCPs, including Claude in Chrome. Web fetch runs server-side and is limited to search results and URLs you've shared. Team and Enterprise owners can turn off web search for Cowork and Chat in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**, and Claude in Chrome in **[Organization settings > Claude in Chrome](https://claude.ai/admin-settings/browser-extension)**.