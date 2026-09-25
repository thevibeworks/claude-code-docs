> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins

> Add plugins to Claude: what a plugin adds, where to find and install one, and where it's available across chat, Cowork, and Claude Code.

A plugin packages [skills](/docs/skills/overview), [MCP connectors](/docs/connectors/getting-started), and [commands and agents](#compare-what-each-plugin-component-adds) so you can add them to Claude as one unit. You add plugins from [**Customize > Plugins**](https://claude.ai/customize/plugins) in claude.ai or the Claude desktop app; **Customize** is the page that holds your connectors, skills, and plugins. Each plugin is saved to your account, so it's also available in Cowork and Claude Code without installing it again.

This page is for people using plugins in claude.ai, the Claude desktop app, and Cowork.

<Note>
  * If you want to build a plugin or submit one to the directory, see [Plugin structure and testing](/docs/plugins/build) and [Publish to the directory](/docs/directory/publish)
  * If you install and manage plugins from the Claude Code command line, see [Install plugins](https://code.claude.com/docs/en/plugins/install) in the Claude Code docs
  * If you have a `.mcpb` file to install into the Claude desktop app, see [Install a local connector in the desktop app](/docs/connectors/custom/add-unlisted#install-a-local-connector-in-the-desktop-app)
</Note>

To get started, [find and add a plugin](#find-and-add-a-plugin), then see [how to use it in each app](#use-a-plugin) and [where it becomes available on your account](#find-the-plugin-in-each-app).

## Install a plugin

Every way of adding a plugin to your account starts from the **Plugins** page at [**Customize > Plugins**](https://claude.ai/customize/plugins) in claude.ai or the desktop app.

### Before you add a plugin

A plugin's skills and commands are instructions Claude follows, and its connectors reach outside services with the account you connect. In Cowork and Claude Code a plugin can also run agents and hooks, which run commands on your computer when certain events happen, and a connector marked **Runs in each session** runs a program on your computer. Anthropic reviews plugins listed in the directory: every version gets automated validation and a security scan, and a person reviews a new listing before it goes live, as [Prepare for review](/docs/directory/publish#prepare-for-review) describes. That review doesn't cover a plugin you add from a marketplace URL or upload yourself, so add those only from sources you trust. On Team and Enterprise plans, an Owner controls which sources members see and whether they can add their own, as [Manage plugins for your organization](/docs/plugins/admin) covers.

### Find and add a plugin

On the **Plugins** page, you add a plugin from **Discover**, **Add > Add marketplace**, or **Add > Upload plugin**:

* **Discover**: see the plugins available to you. These are the ones in Anthropic's default marketplaces, the directory, and any your organization provides. Select one to read what it contains, then select **Add**. The directory's plugins appear on Pro, Max, Team, and Enterprise plans. On Team and Enterprise plans, an Owner chooses which Anthropic sources the organization includes, so you see the directory only if your organization keeps it
* **Add > Add marketplace**: add a [plugin marketplace](https://code.claude.com/docs/en/plugins/create-marketplace), a Git repository that contains plugins, so its plugins appear alongside the others. Enter a repository URL such as `https://github.com/your-org/your-plugins` or the `owner/repo` shorthand for GitHub. For a marketplace you add yourself, GitHub and GitHub Enterprise repositories work, and so do public GitLab and Bitbucket repositories. To add a private GitHub repository, connect your GitHub account when the dialog asks and give the Claude GitHub App access to the repository. If access is missing, the dialog says so and shows **Connect GitHub** or **Install the Claude GitHub App**. Plugins your organization distributes from its own repositories come through [organization settings](/docs/plugins/admin#add-your-own-plugins) instead
* **Add > Upload plugin**: upload a plugin you have as a folder on your computer, as a `.zip` or `.plugin` file. Zip either the plugin folder itself or its contents; both work as long as the archive holds one `.claude-plugin/plugin.json`

[Plugin feature support across platforms](/docs/plugins/platform-support#compare-installation-sync-and-admin-controls) lists the size and count limits.

### Find the plugin in each app

After you install a plugin, it's recorded on your account for the organization you're in, and you can use its components wherever you use that account:

* **Chat on the web, desktop, and mobile**: its skills, commands, and connectors are available in your conversations
* **Cowork**: its skills, commands, agents, and connectors load into your tasks the next time you start one
* **Claude Code**: it downloads as a synced plugin the next time you start a session signed in to the same account. Run `/reload-plugins` in that session to load it, or start Claude Code again. Plugins you install from the Claude Code command line stay on that machine and aren't added to your claude.ai account

### Bundled connectors

Adding a plugin doesn't add a connector to your account or sign you in to anything. To see the connectors a plugin includes, open the plugin from **Customize > Plugins** and select its **Connectors** tab. Each connector shows one of these states:

* **Connected**: the connector is already connected on your account, so there's nothing more to do
* **Not connected**: the connector is on your account, but you haven't signed in to the service yet. Connect it from this tab
* **Not added**: the connector isn't on your account yet. Add it from this tab, then connect it. On Team and Enterprise plans, an Owner adds the connector for the organization. If you can't add it yourself, ask an Owner to add it, then connect it with your own account

The plugin's skills load whether or not you connect anything. A skill that uses a connector's service can't reach that service until the connector shows **Connected**. After you add a connector, it also appears under **Customize > Connectors**. To disconnect one and keep the plugin, see [Manage installed plugins](#manage-installed-plugins).

The service a connector reaches is run by its provider, which may require its own account or paid plan.

A bundled connector marked **Runs in each session** runs on your computer rather than over the internet. It works in Claude Code and in a Cowork session that runs on your computer in the desktop app, not in chat.

### Plugins your organization installs or requires

On Team and Enterprise plans, your organization can install a plugin for you as installed by default or as required:

* **Installed by default**: the plugin is already in your list under **Customize > Plugins** without you adding it, and you can turn it off
* **Required**: the plugin is installed and always on. It's marked **This plugin is required by your organization**, and you can't turn it off or remove it

[Manage plugins for your organization](/docs/plugins/admin) covers those controls.

## Use a plugin

After you add a plugin, you use its skills and commands from the message box. To see the skills, commands, connectors, and agents a plugin contains, open it from **Customize > Plugins**, where its page lists each kind on its own tab.

You can run a plugin's skill or command in chat, Cowork, and Claude Code:

* **Chat in claude.ai or the desktop app**: describe the task, and Claude loads the plugin's skill when the task matches it. To pick one yourself:

  1. Type `/` in the message box. The menu lists your skills with the name of the plugin each one came from.
  2. Type the plugin's name, or `plugin-name:skill-name`, to narrow the list.
  3. Select the skill.

  A plugin's commands appear in the same menu as skills.
* **Cowork**: type `/plugin-name:command` to run a command, or describe the task and let Claude load the matching skill. Cowork also runs the plugin's agents
* **Claude Code**: type `/plugin-name:skill-name`. [Install and manage plugins](https://code.claude.com/docs/en/plugins/install) in the Claude Code docs covers the command line

If a skill or command uses one of the plugin's connectors, connect it first, as [Bundled connectors](#bundled-connectors) describes.

After you add a plugin, try it on a real task. If it doesn't help, turn it off with its **Disable plugin** toggle or select **Remove** from its menu, as [Manage installed plugins](#manage-installed-plugins) describes.

## Compare what each plugin component adds

A plugin can contain skills, commands, MCP connectors, and agents. Chat, Cowork, and Claude Code each load the components they support and skip the others, so one plugin can do more in Cowork than in a chat conversation.

| Component      | What it adds for you                                                                                                                                                  | Where it works            |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| Skills         | Instructions Claude follows when a task matches, such as your team's process for a weekly report. They're listed in **Customize > Skills** alongside your own skills. | Chat, Cowork, Claude Code |
| Commands       | Named actions. In Cowork and Claude Code you run one by typing `/plugin-name:command`. In chat a command loads as a skill.                                            | Chat, Cowork, Claude Code |
| MCP connectors | Access to an external tool or data source. You add or connect each one from the plugin's **Connectors** tab.                                                          | Chat, Cowork, Claude Code |
| Agents         | Specialists Claude can delegate part of a task to                                                                                                                     | Cowork, Claude Code       |

[Plugin feature support across platforms](/docs/plugins/platform-support) lists every component by app.

## Manage installed plugins

After you install a plugin, you can turn it off, remove it, disconnect its connectors, or update it from **Customize > Plugins**. Plugins that other people share with you are listed there too.

* **Turn off a plugin**: open the plugin and turn off its toggle, which is labeled **Disable plugin**. Turn the toggle on again to enable the plugin
* **Remove a plugin**: remove it from your account from its menu:
  1. Open the plugin.
  2. Open its menu.
  3. Select **Remove**.
* **Disconnect a bundled connector**: open the plugin's **Connectors** tab, or **Customize > Connectors**, and disconnect it. The plugin stays installed
* **Use a plugin someone shared with you**: a plugin that another member of your organization shares with you appears under **Shared with you** on the **Your plugins** tab, turned off. Open it and turn on its toggle to use it. It stays in your list for as long as that person shares it. To share one of your own, see [Share a plugin with specific people](/docs/plugins/share#share-a-plugin-with-specific-people)
* **Get updates**: plugins from a marketplace or the directory update from their source. After a new version syncs from the source, you get it on your account automatically, with nothing to accept. Claude Code's own marketplaces have a separate auto-update setting. To pull the latest from a marketplace you added, select **Check for updates**. For a marketplace you added yourself from github.com, you can also turn on **Sync automatically**. Marketplaces your organization syncs have their own setting, which [Sync your organization's plugins from a repository](/docs/plugins/org-sync) covers

If a plugin you added doesn't appear where you expect it, [Install plugins in Cowork](/docs/cowork/guide/plugins) covers how the desktop app loads and updates plugins, and [Synced plugins](https://code.claude.com/docs/en/plugins/loading#synced-plugins) covers Claude Code.

## Track plugin usage in your organization

On Team and Enterprise plans, a plugin's page in **Customize > Plugins** shows how much your organization uses it:

* **Adoption**: the number of people in your organization who used the plugin in the last 30 days. The count updates daily, and usage from older versions of Claude Code and the desktop app may not be counted
* **Activity**: the number of runs in the last 30 days
* **You**: the number of runs by you in the last 90 days. This one appears when you open the plugin from your own list

The plugin's **Skills** tab shows runs in the last 30 days for each skill. A skill's page in **Customize > Skills** shows the same three figures for that skill.

A plugin you made or that someone shared with you shows the organization figures only when a published copy of it is live in your organization. [Publish a plugin to your organization](/docs/plugins/share#publish-a-plugin-to-your-organization) covers publishing.

## Create your own plugin

You can make a plugin of your own from **Customize > Plugins > Add**.

* **Create with Claude**: start a conversation where Claude builds the plugin with you
* **Create a plugin**: open an editor and write its files directly

[Create a plugin with Claude](/docs/plugins/create-with-claude) covers both, and [Plugin structure and testing](/docs/plugins/build) covers building one as a folder for other people to install. On Team and Enterprise plans, you can then [share the plugin with specific people](/docs/plugins/share#share-a-plugin-with-specific-people) or [publish it to your organization](/docs/plugins/share#publish-a-plugin-to-your-organization).

You can also submit a plugin you build to Anthropic's directory, where, once it passes review, people on Pro, Max, Team, and Enterprise plans can find and add it. [Build your first plugin](/docs/plugins/quickstart) builds and tests an example plugin, and [Publish to the directory](/docs/directory/publish) covers who can submit and what review involves.

## Next steps

* [Plugin feature support across platforms](/docs/plugins/platform-support): check which of a plugin's components work in chat, Cowork, the desktop app, and Claude Code
* [Manage plugins for your organization](/docs/plugins/admin): make plugins available, installed by default, or required for members
* [Install plugins](https://code.claude.com/docs/en/plugins/install) in the Claude Code docs: install and manage plugins from the command line, including the ones synced from your account
* [Publish to the directory](/docs/directory/publish): submit a plugin to the directory, where Anthropic reviews it before it's listed
