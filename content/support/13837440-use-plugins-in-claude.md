# Use plugins in Claude

Plugins are available to all paid plans (Pro, Max, Team, Enterprise).

Plugins customize how Claude works for your role, team, and company. Each plugin bundles skills, connectors, and sub-agents into a single package, so you get a ready-to-go setup from your first conversation instead of configuring each piece yourself.

## Where you can use plugins

You can install and use plugins in chat on the web, the Chat tab in Claude Desktop, and Claude Cowork. The skills bundled in a plugin work across all three. Hooks and sub-agents run only in Cowork, so they appear grayed out in chat.

Plugins can also bundle connectors, so the right services are set up for a workflow without you connecting each one. Claude connects to services like Google Drive, Gmail, Slack, DocuSign, and many more.

**Note:** In Cowork, connectors reach external services through Anthropic's cloud, not through your local network. A custom connector must point to a server that's reachable over the public internet from Anthropic's IP ranges. If your organization's servers are behind a firewall or on a private network, see **[Network requirements for custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp#h_b66e88c454)**.

---

## Browse available plugins

Claude includes a growing library of plugins for common knowledge work—including sales, finance, legal, marketing, HR, engineering, design, operations, data analysis, and more. Each one comes pre-configured with the skills and connectors relevant to that function.

We also provide **Plugin Create**, a plugin that helps you build custom plugins from scratch.

For the full collection of Anthropic-built plugins, visit **[GitHub](https://github.com/anthropics/knowledge-work-plugins)**.

**Note:** Plugins may include local MCP servers that run on your computer with the same permissions as any other program you run. Only install plugins from sources you trust. If your organization is on an Enterprise plan, your admin may have restricted which plugins you can install, or disabled local MCP servers entirely.

---

## Install a plugin

1. In Claude, open the **Customize** menu in the left sidebar. Customize brings your plugins, skills, and connectors together in one place.

2. Open the **Plugins** tab.

3. Click "Browse plugins" to see the available options.

4. Click "Install" on the plugin you want.

In Cowork, open the "Cowork" tab first, then open **Customize**.

You can also upload a custom plugin file if you built one yourself. On Team and Enterprise plans, a colleague can share a plugin with you directly instead of sending you the file. See **[Use a plugin shared with you](#h_ef985546b4)** below. On Claude Desktop and in Cowork, plugins you add yourself are saved locally to your computer.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2100409211/fc01614dde1a616fa31ffaa9cb04/47bacf5b-a810-45b5-a468-9769f1a58ef8?expires=1788674400&amp;signature=bd6f516b99c1ee0a2c5d4bb040cc9ae0255114641135193335f3dc36870509b9&amp;req=diEnFs1%2BlINeWPMW3nq%2BgVBR61lPspoU3ilCn8XYmtC5uDZwJDOPmveFyMgA%0AtmuzlkXKMrKrRP8J4L6D5hAiAjk%3D%0A)

If you're on the Enterprise plan and your organization has skill scanning turned on, plugins are checked for malicious content when they're installed or updated. A plugin with malicious content is blocked, and one that may carry risk shows a caution banner. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065)**.

---

## Use skills from plugins

Each plugin you install adds skills you can use while working with Claude. Type "/" or click the "+" button to see the available skills from your installed plugins, in chat and in Cowork. Click any skill to see its details.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2157396844/4a790e10f5b88df770783df1d7e9/image.png?expires=1788674400&amp;signature=63e0720a7cebba4473d80d5978264bd67a037bc94af2baf9886a07314d0049ba&amp;req=diEiEcp3m4lbXfMW3nq%2BgasPOp6LFQbtIeApIe1p%2BLZEH2XVMBx94Cg0HKYP%0As05Q7zqmfxIo15rNnDY2Sr93vNQ%3D%0A)

---

## Customize a plugin

In Cowork, you can tailor an installed plugin to better fit your workflow:

1. While viewing an installed plugin, click “Customize” in the upper right corner.

2. This opens a new Cowork task with a prompt asking Claude to customize the plugin you chose.

3. Click “Let's go” to start working with Claude to adjust the plugin's Skills and connectors to match how you work.

---

## Build your own plugin

Want to create something from scratch? The "Plugin Create" plugin walks you through the process, and you can start from any Anthropic-built template and modify it. For details on plugin structure and formatting, see the **[Plugins reference](https://code.claude.com/docs/en/plugins-reference)** in our Claude Code docs.

---

## Turn on plugin sharing for your organization

Owners and Primary Owners of Team and Enterprise organizations can turn on skill and plugin sharing for members of the organization. Plugin sharing uses the same settings and toggles as skill sharing.

To enable plugin sharing:

1. Navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills).**

2. Click the "Policy" tab.

3. To enable sharing between specific people, toggle on **Skill sharing**.

4. To enable sharing with groups, toggle on **Share with groups**. If you have custom roles, you also need to enable the **Share skills with groups** capability in the custom role.

---

## Share a plugin

After an Owner or Primary Owner turns on plugin sharing, you can share a plugin you uploaded or created in Customize with specific colleagues (Team and Enterprise plans) or with a group (Enterprise plans). The people you share with get your current version, and you can stop sharing at any time. Plugins you installed from a marketplace, and plugins saved locally in Claude Desktop or Cowork, can't be shared.

**Note:** If you don't see the option to share, check with your organization owner.

To share a plugin:

1. Navigate to **[Customize > Plugins](https://claude.ai/new#settings/customize-plugins)**.

2. Find the plugin you created.

3. Click the three-dot menu "..." next to it, then select "Share."

4. Choose who to share with:

  1. **Specific people:** Enter names or emails to share directly. Sharing creates a link that opens the item for anyone it's shared with. The plugin appears in the **Shared with you** section of each recipient's Plugins tab, grayed out until they enable it, and shows your name as the owner.

  2. **A group (Enterprise plans only):** Share with a group your organization has already set up. The plugin appears in every group member's Plugins tab under **Shared with you**, grayed out until they enable it. Requires the **Share with groups** toggle.

5. Click "Share."

The plugin appears in each recipient's **Shared with you** section, labeled with your name, and stays off until they turn it on. Shared plugins are view-only. Recipients can enable and use the plugin, but they can't edit the contents. If you update the plugin later, recipients automatically get the updated version at next use. You can remove someone's access at any time, and access is removed automatically if they leave the organization.

To copy a link to a shared plugin, click "Copy link" in the Share dialog. The link opens the plugin for people you've already shared it with; anyone else sees a message that it isn't available.

## Stop sharing a plugin

1. Click the "..." button next to the plugin, then select "Share."

2. Click the "x" next to the person or group you want to remove.

The plugin is removed from their list right away. Deleting a plugin removes it for everyone you shared it with, and anything shared with a member is removed automatically when they leave your organization.

## Use a plugin shared with you

When a colleague shares a plugin with you, it appears in the **Shared with you** section of the **Plugins** tab in **Customize**. It's off until you turn it on. Once it's on, its skills work the same way as any other installed plugin.

You can't edit a plugin that's been shared with you. If you want to change how it works, ask the person who built it, or build your own version. If they stop sharing the plugin or delete it, it's removed from your list automatically.

**Note:** Review a plugin shared with you before turning it on, the same as you would for any plugin from outside Anthropic. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065-get-started-with-skill-and-plugin-scanning)**.

---

## Add or remove plugin marketplaces

Anthropic provides built-in marketplaces of plugins, including a Knowledge Work marketplace that's added by default. You can add other Anthropic-built marketplaces, like Financial Services or Legal, or add one from a GitHub repository.

To add a marketplace:

1. Open the **Customize** menu and go to the **Plugins** tab.

2. In the **Personal plugins** section, click the "+" button, then select "Add marketplace."

3. Choose how to add it:

  - **Browse Anthropic sources:** Pick from marketplaces curated by Anthropic, such as Knowledge Work, Life Sciences, Financial Services, and Legal. Click "Add" next to the one you want, then click "Done."

  - **Add from a repository:** Sync a marketplace from a GitHub repository or git URL.

To remove a marketplace, including the default Knowledge Work marketplace:

1. Find the marketplace in the **Plugins** section.

2. Click the menu button in the right corner and select "Remove."

---

## Organization-managed plugins

If you're on a Team or Enterprise plan, an owner can distribute plugins across your organization through plugin marketplaces. These are different from plugins a colleague shares with you, which show up under **Shared with you**. Organization-managed plugins work the same as any other plugin, with a couple of differences:

- You can't edit organization-managed plugins. This keeps shared tooling consistent across your team.

- Some plugins may be auto-installed or required for you. You can uninstall auto-installed plugins if you don't need them, but required plugins can't be removed.

- Available organization plugins show up when you browse the plugin catalog, and you can install them yourself.

On Enterprise plans, your admin may customize which plugins are available to your group. This means the plugins you see in the catalog may differ from what colleagues in other groups see. Plugins assigned to your group appear in chat as well as Cowork.

For guidance on setting up and managing plugins organization-wide, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-)**.