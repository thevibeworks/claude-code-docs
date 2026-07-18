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

You can also upload a custom plugin file if you built one yourself or received one from a colleague. On Claude Desktop and in Cowork, plugins you add yourself are saved locally to your computer.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2100409211/fc01614dde1a616fa31ffaa9cb04/47bacf5b-a810-45b5-a468-9769f1a58ef8?expires=1784394900&amp;signature=46539f646d7b56ac3fdd4da42ca21f78314ea2ec89324cac1f07887cd3d28d2f&amp;req=diEnFs1%2BlINeWPMW1HO4zZF3IhHeOvFcxakFVfq5WwyiHm%2Fms%2FdU4m9DGX1K%0AWGWwTB1L566ARQzPMHQ%3D%0A)

---

## Use skills from plugins

Each plugin you install adds skills you can use while working with Claude. Type "/" or click the "+" button to see the available skills from your installed plugins, in chat and in Cowork. Click any skill to see its details.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2157396844/4a790e10f5b88df770783df1d7e9/image.png?expires=1784394900&amp;signature=41c7e9b0fae71067c0c5d2b822b4754604e9efe2d1d22d7ba8ba7591f9ab93d2&amp;req=diEiEcp3m4lbXfMW1HO4zf4NBPL%2FikSdmKUxugP2BQvOGjFETuTRZecOiwRg%0AZpFgnXkqLGW9QWq2TqQ%3D%0A)

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

If you're on a Team or Enterprise plan, an owner can distribute plugins across your organization through plugin marketplaces. These work the same as any other plugin, with a couple of differences:

- You can't edit organization-managed plugins. This keeps shared tooling consistent across your team.

- Some plugins may be auto-installed or required for you. You can uninstall auto-installed plugins if you don't need them, but required plugins can't be removed.

- Available organization plugins show up when you browse the plugin catalog, and you can install them yourself.

On Enterprise plans, your admin may customize which plugins are available to your group. This means the plugins you see in the catalog may differ from what colleagues in other groups see. Plugins assigned to your group appear in chat as well as Cowork.

For guidance on setting up and managing plugins organization-wide, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-)**.