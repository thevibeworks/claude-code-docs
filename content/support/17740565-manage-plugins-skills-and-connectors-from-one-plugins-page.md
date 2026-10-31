# Manage plugins, skills, and connectors from one Plugins page

Plugins, skills, and connectors are coming together in one Plugins experience. This article explains what's changing, which accounts are affected, and what you need to do. Most organizations don't need to do anything.

This change reaches Enterprise plans on November 30, 2026. Free, Pro, Max, Ultra, and Team plans start rolling out on October 29.

## What's changing

You'll find, add, and manage plugins, skills, and connectors from one place. In the sidebar, what was previously **Customize** becomes **Plugins**, and one Plugins page replaces the separate Skills, Connectors, and Plugins tabs in Claude.

### For users

- **New name:** **Customize** now reads **Plugins** in the sidebar, the chat menu, and settings.

- **Your plugins first:** **Your plugins** appear above the plugins you can browse. It includes plugins from your organization and plugins shared with you.

- **Quick filters:** You can narrow the list to skills or connectors. Each card shows which type it is.

- **One detail page:** Plugins and connectors open on the same page layout.

- **Directory labels:** Public plugins show **Verified** or **Community**.

- **Skills work as plugins:** To use a skill, click the “+” button or type “/” in chat. You can still share skills.

Your existing connectors, skills, and plugins stay installed. Removing a plugin that packages skills and a connector doesn't disconnect its connector, so you'll need to disconnect it separately.

### For admins

- **Your controls:** Most existing controls stay in place, with the changes below. Plugin and connector controls stay mostly separate in Organization settings.

- **Plugins and connectors keep separate pages:** In Organization settings, Plugins & skills and Connectors become one Plugins group, with separate pages for plugins, connectors, policy, marketplaces, and requests.

- **Skills disabled setting:** Starting November 30, if Skills are disabled for your organization, plugins are also blocked in the Claude Desktop app. This matches how Claude web and Claude Code work today.

## Which accounts are affected

The timing depends on your plan.

| **Plan**                              | **When the change reaches you**                                            |
| ------------------------------------- | -------------------------------------------------------------------------- |
| Free, Pro, Max, Ultra, and Team plans | Rolling out gradually starting October 29, generally available November 9. |
| Enterprise plan                       | On by default starting November 30                                         |

The Skills-off rule applies to Team and Enterprise plans starting November 30.

## What you need to do

Most users don't need to do anything. You will continue to be able to use your existing connectors, skills, and plugins that are already installed on your account.

Admins of organizations with Skills turned off need to turn on Skills before November 30 to keep plugins in Claude Desktop.

### If you're a user

No action is needed. To find what you've already added:

1. Click **Plugins** in the sidebar.

2. Open **Your plugins > Show all**.

3. Use the quick filters to show plugins that only contain skills or connectors.

### If you're an admin on a Team or Enterprise plan

No action is needed if Skills are enabled for your organization.

If Skills are disabled for your organization, Plugins will stop working in Claude Desktop with this update given that Skills will become packaged into Plugins. Before November 30, choose whether to keep Plugins working on Claude Desktop:

- **To keep plugins available:** Turn on Skills.

  - **Note:** This will be renamed to **Plugins** on November 30.

- **To block plugins:** Leave Skills off. Plugins stop working in Claude Cowork and the Code tab starting November 30.

To enable Plugins, you'll need to be an owner:

1. Go to **Organization settings > Library > Policy**. Turn on **Cloud code execution and file creation** if it's off. Plugins require it.

2. Turn on **Skills**.

  - **Note:** This will be renamed to **Plugins** on November 30.

**Important:** If your organization uses the HIPAA configuration, your BAA doesn't cover connectors, plugins, or skills, including after an owner turns them on. Keep protected health information (PHI) out of them.