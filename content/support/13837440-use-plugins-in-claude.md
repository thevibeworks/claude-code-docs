# Use plugins in Claude

Plugins are available to all paid plans (Pro, Max, Team, Enterprise).

Plugins customize how Claude works for your role, team, and company. Each plugin bundles skills, connectors, and sub-agents into a single package, so you get a ready-to-go setup from your first conversation instead of configuring each piece yourself.

For a full reference on what each part of a plugin does in chat, Cowork, and Claude Code, see **[Plugins](https://claude.com/docs/plugins/overview)** in the Claude docs.

## Where you can use plugins

You can add and use plugins in chat on the web, the Chat tab in Claude Desktop, and Claude Cowork. Plugins you add are saved to your account, so they’re also available in Claude Code in your terminal when you sign in with the same account. The skills and commands bundled in a plugin work in all of these places. Hooks and sub-agents run in Cowork and Claude Code, not in chat, so they appear grayed out in chat.

Plugins can also bundle connectors, so the right services are set up for a workflow without you connecting each one. Claude connects to services like Google Drive, Gmail, Slack, DocuSign, and many more.

**Note:** In Cowork, connectors reach external services through Anthropic's cloud, not through your local network. A custom connector must point to a server that's reachable over the public internet from Anthropic's IP ranges. If your organization's servers are behind a firewall or on a private network, see **[Network requirements for custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp#h_b66e88c454)**.

### Use plugins in Claude Code

Plugins you've installed, and plugins your organization has distributed to you, sync to Claude Code when you sign in with your Claude account. This needs Claude Code v2.1.273 or later.

- Plugins sync once each time Claude Code starts.

- If you signed in on an older version, sync starts within a few hours, or right away if you run `/login` again.

- In Claude Code, a plugin runs in full on your computer, including its skills, sub-agents, hooks, and MCP servers.

- The sync is one-way. It reads from your Claude account and never changes anything in it.

- Plugins don't sync when Claude Code is signed in with an API key or runs on a cloud provider such as Amazon Bedrock.

To stop plugins from syncing, set `syncClaudeAiPlugins` to `false` in your Claude Code settings. Learn more about **[synced plugins](https://code.claude.com/docs/en/plugins-reference#synced-plugins)** in the Claude Code docs.

---

## Browse available plugins

Claude includes a growing library of plugins for common knowledge work—including sales, finance, legal, marketing, HR, engineering, design, operations, data analysis, and more. Each one comes pre-configured with the skills and connectors relevant to that function. Some plugins, like Salesforce in Claude, are built by partners and bundle a partner's own connectors and skills.

We also provide **Plugin Create**, a plugin that helps you build custom plugins from scratch.

For the full collection of Anthropic-built plugins, visit **[GitHub](https://github.com/anthropics/knowledge-work-plugins)**.

**Note:** Plugins may include local MCP servers that run on your computer with the same permissions as any other program you run. A plugin's local MCP server runs in Cowork and Claude Code, not in chat. Only install plugins from sources you trust. If your organization is on an Enterprise plan, your admin may have restricted which plugins you can install, or disabled local MCP servers entirely.

---

## Install a plugin

1. In Claude, open the **Customize** menu in the left sidebar. Customize brings your plugins, skills, and connectors together in one place.

2. Open the **Plugins** tab.

3. Open the **Discover** tab to see the available options.

4. Select the plugin you want, then click "Add."

In Cowork, open the "Cowork" tab first, then open **Customize**.

You can also upload a custom plugin file if you built one yourself. On Team and Enterprise plans, a colleague can share a plugin with you directly instead of sending you the file. See **[Use a plugin shared with you](#h_ef985546b4)** below. Plugins you add in Claude on the web or in Claude Desktop are saved to your account, not to your computer, so they follow you to chat, Cowork, and Claude Code.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2100409211/fc01614dde1a616fa31ffaa9cb04/47bacf5b-a810-45b5-a468-9769f1a58ef8?expires=1790424000&amp;signature=cb907a4638270a79820406cddefeb07767a1fd062d1f795d0cd144983342ea3d&amp;req=diEnFs1%2BlINeWPMW3nq%2BgVBR61lOupgR3i1Cn8XYmtAJlH8kidYejzXPOD4b%0AxiJ887TESjSEboZTDcW3qCct7yw%3D%0A)

If you're on the Enterprise plan and your organization has skill scanning turned on, plugins are checked for malicious content when they're installed or updated. A plugin with malicious content is blocked, and one that may carry risk shows a caution banner. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065)**.

---

## Use skills from plugins

Each plugin you add brings skills and commands you can use while working with Claude. Type "/" or click the "+" button to see the available skills from your plugins, in chat and in Cowork. In Cowork, you can also run a plugin's command by typing `/plugin-name:command`. Click any skill to see its details.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2157396844/4a790e10f5b88df770783df1d7e9/image.png?expires=1790424000&amp;signature=dc9c67094cf1df95c34ec6bd0b8df3298f3865e125f4ff386600decb5ebfcfff&amp;req=diEiEcp3m4lbXfMW3nq%2BgasPOp6KHQToIeQpIe1p%2BLb9HQmtIkQcf26oyPeR%0AIRFj8sxOf56DFbkTxy1gzI%2BQC28%3D%0A)

---

## Customize a plugin

In Cowork, you can tailor an installed plugin to better fit your workflow:

1. While viewing an installed plugin, click “Customize” in the upper right corner.

2. This opens a new Cowork task with a prompt asking Claude to customize the plugin you chose.

3. Click “Let's go” to start working with Claude to adjust the plugin's Skills and connectors to match how you work.

---

## Build your own plugin

Want to create something from scratch? The "Plugin Create" plugin walks you through the process, and you can start from any Anthropic-built template and modify it. For details on plugin structure and formatting, see the **[Plugins reference](https://code.claude.com/docs/en/plugins-reference)** in the Claude Code docs.

---

## Turn on plugin sharing for your organization

Owners and Primary Owners of Team and Enterprise organizations can turn on skill and plugin sharing for members of the organization. Plugin sharing uses the same settings and toggles as skill sharing.

To enable plugin sharing:

1. Navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Policy” tab**.**

2. To enable sharing between specific people, toggle on **Skill sharing**.

3. To enable sharing with groups, toggle on **Share with groups**. If you have custom roles, you also need to enable the **Share skills with groups** capability in the custom role.

To let users publish plugins to the organization library, use the **Publishing** setting on the same "Policy" tab. Learn more about **[letting users publish skills and plugins to your organization](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization#h_1abc45a27c)**.

---

## Share a plugin

After an Owner or Primary Owner turns on plugin sharing, you can share a plugin you uploaded or created in Customize with specific colleagues (Team and Enterprise plans) or with a group (Enterprise plans). The people you share with get your current version, and you can stop sharing at any time. Plugins you added from a marketplace can't be shared.

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

## Publish a plugin to your organization

On Team and Enterprise plans, you can submit a plugin you uploaded or created in Customize to your organization's library, so anyone in your organization can install it. Sharing gives a plugin to specific people or groups, and you keep control of it. Publishing hands it to your organization.

To publish a plugin:

1. Navigate to **[Customize > Plugins](https://claude.ai/customize/plugins)**.

2. Open the plugin you want to publish.

3. Click "Publish to org."

4. If your organization requires review, choose how you'd like the plugin offered: Available to install, Installed by default, or Required. Add release notes for the reviewer if you'd like, then submit.

If your organization requires review, an owner (or someone with permission to review requests) checks the plugin before it's published. Your choice of how it's offered is a proposal. The reviewer sees it preselected and can change it, and they also choose who gets the plugin: everyone or specific groups. You can keep using and editing your copy while you wait, and you can withdraw the submission. The plugin shows its status: pending, changes requested (with the reviewer's note), or published. You'll get an email when it's approved. If your organization doesn't require review, the plugin is published to the library and available to everyone in your organization to install. If your organization has security scanning turned on, the plugin isn't listed for others until it passes the scan, which usually takes a few minutes.

Once published, the plugin is managed by your organization. To update it, publish again. The new version goes through the same review, and everyone who uses the plugin stays on the approved version until the update is approved.

**Note:** If you don't see "Publish to org," your organization may have publishing turned off, or the plugin may not be one you created. You can't publish plugins that were shared with you or that you installed from a marketplace or your organization's library. Check with your organization owner if it's your own plugin.

## Use a plugin shared with you

When a colleague shares a plugin with you, it appears in the **Shared with you** section of the **Plugins** tab in **Customize**. It's off until you turn it on. Once it's on, its skills work the same way as any other installed plugin.

You can't edit a plugin that's been shared with you. If you want to change how it works, ask the person who built it, or build your own version. If they stop sharing the plugin or delete it, it's removed from your list automatically.

**Note:** Review a plugin shared with you before turning it on, the same as you would for any plugin from outside Anthropic. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065-get-started-with-skill-and-plugin-scanning)**.

---

## Add or remove plugin marketplaces

Anthropic provides built-in marketplaces of plugins, including a Knowledge Work marketplace that's added by default. You can add other Anthropic-built marketplaces, like Financial Services or Legal, or add one from a Git repository.

To add a marketplace:

1. Open the **Customize** menu and go to the **Plugins** tab.

2. On the **Plugins** page, click "Add," then select "Add marketplace."

3. Choose how to add it:

  - **Browse Anthropic sources:** Pick from marketplaces curated by Anthropic, such as Knowledge Work, Life Sciences, Financial Services, and Legal. Click "Add" next to the one you want, then click "Done."

  - **Add from a repository:** Enter a repository URL, or owner/repo for GitHub. Repositories on github.com work, and so do public repositories on gitlab.com and bitbucket.org.

To remove a marketplace, including the default Knowledge Work marketplace:

1. Find the marketplace in the **Plugins** section.

2. Click the menu button in the right corner and select "Remove."

---

## Organization-managed plugins

If you're on a Team or Enterprise plan, an owner can distribute plugins across your organization through plugin marketplaces, or approve plugins that users publish to the organization library These are different from plugins a colleague shares with you, which show up under **Shared with you**. Organization-managed plugins work the same as any other plugin, with a couple of differences:

- You can't edit organization-managed plugins. This keeps shared tooling consistent across your team.

- Some plugins may be installed by default or required for you. You can turn off a plugin that was installed by default if you don't need it, but required plugins can't be turned off or removed. Required plugins can't be disabled in Claude Code either.

- Available organization plugins show up on the **Discover** tab, and you can add them yourself.

On Enterprise plans, your admin may customize which plugins are available to your group. This means the plugins you see in the catalog may differ from what colleagues in other groups see. Plugins assigned to your group appear in chat, Cowork, and Claude Code sessions signed in with the same Claude account.

For guidance on setting up and managing plugins organization-wide, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-)**.