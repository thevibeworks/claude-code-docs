> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin feature support across platforms

> Look up which plugin components and install paths work in claude.ai chat, Cowork, and Claude Code, and why a plugin behaves differently on each.

You can install the same plugin folder everywhere you use Claude, but chat, Cowork, and Claude Code each load a different subset of what the folder can contain. A surface skips a component it doesn't load, so a plugin can look complete in one place and partial in another.

This page is for anyone checking a component or behavior before relying on it, whether you're installing a plugin, building one, or submitting one to the directory.

<Note>
  * If you want to install and manage plugins, see [Plugins](/docs/plugins/overview)
  * If you're building a plugin, see [Plugin structure and testing](/docs/plugins/build)
  * If you run Claude Desktop on your own model provider, see its [Feature matrix](/docs/third-party/claude-desktop/feature-matrix) for feature availability
  * If you want to know where MCP Apps render, see [Add interactive UI with MCP Apps](/docs/connectors/building/mcp-apps/getting-started)
</Note>

## Compare component support by app

The tables on this page use these column names:

* **Chat**: conversations in claude.ai on the web, in the Claude desktop app, and in the mobile apps
* **Cowork**: Cowork tasks in the desktop app
* **Claude Code**: the terminal, the IDE extensions, and the desktop app's Code tab

A component marked "Ignored" is skipped on that surface, and a component marked "Can't be installed" makes that surface refuse the whole plugin.

| Component                                                             | Chat                                                                              | Cowork                                                                            | Claude Code                       | Notes                                                                                       |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------- | :------------------------------------------------------------------------------------------ |
| Skills (`skills/<name>/SKILL.md`)                                     | Loads                                                                             | Loads                                                                             | Loads                             | [Create custom skills](/docs/skills/how-to)                                                      |
| Commands (`commands/*.md`)                                            | Loads as a skill; Claude applies it when it fits                                  | Loads; you run it by typing `/plugin-name:command`                                | Loads                             |                                                                                             |
| Agents (`agents/*.md`)                                                | Ignored                                                                           | Loads                                                                             | Loads                             |                                                                                             |
| Hooks (`hooks/hooks.json`)                                            | Ignored                                                                           | Loads                                                                             | Loads                             | [Hooks](https://code.claude.com/docs/en/plugins/components#hooks) in the Claude Code docs   |
| Remote MCP server, `http` or `sse` with a fixed URL                   | Listed on the plugin's **Connectors** tab; works once you add or connect it there | Loads; connect it from the plugin's **Connectors** tab                            | Loads                             | [Bundle a connector with its skill](/docs/plugins/build#bundle-an-mcp-connector-with-its-skill)  |
| Local MCP server, a command the app starts, including `.mcpb` bundles | Ignored                                                                           | Loads when the Cowork session runs on your computer                               | Loads                             | On the web, the plugin's **Connectors** tab marks it **Runs in each session**               |
| MCP server that references `${user_config.*}` values                  | Ignored when the URL contains the reference                                       | Ignored when a referenced option has no default; Cowork doesn't prompt for values | Loads; prompts you for the values | [User configuration](https://code.claude.com/docs/en/plugins/components#user-configuration) |
| Executables in a top-level `bin/` directory                           | Can't be installed                                                                | Can't be installed                                                                | Loads                             |                                                                                             |
| LSP servers, output styles, themes, `settings`                        | Ignored                                                                           | Ignored                                                                           | Loads                             | [Plugin components](https://code.claude.com/docs/en/plugins/components)                     |

When you submit a plugin to the directory, the portal derives the surfaces it supports from these same rules and shows them to you before you submit.

## Compare installation, sync, and admin controls

Chat and Cowork read plugins from your claude.ai account, and Claude Code reads them from the machine it runs on.

|                                          | Chat and Cowork                                                                                                                                                                                                                  | Claude Code                                                                                             | Notes                                                                                                                                                |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Where you add plugins                    | [**Customize > Plugins**](https://claude.ai/customize/plugins) in claude.ai or the desktop app                                                                                                                                   | `/plugin` in a session, or `claude plugin install`                                                      | [Plugins](/docs/plugins/overview), [Install plugins](https://code.claude.com/docs/en/plugins/install)                                                     |
| What an install is attached to           | Your account, for the organization you're in                                                                                                                                                                                     | The machine, at user, project, or local scope                                                           |                                                                                                                                                      |
| Which way installs travel                | A plugin you install on your account also appears in Claude Code as a synced plugin at the next session start                                                                                                                    | A plugin you install from the command line stays on that machine and isn't added to your account        | [Synced plugins](https://code.claude.com/docs/en/plugins/loading#synced-plugins)                                                                     |
| Hosts for a marketplace you add yourself | GitHub and GitHub Enterprise repositories, and public GitLab and Bitbucket repositories                                                                                                                                          | Any Git repository, GitHub shorthand, URL, or local path                                                | Repositories your organization syncs to distribute plugins follow [different rules](/docs/plugins/org-sync#plugin-sources-that-organization-sync-accepts) |
| Marketplace and plugin limits            | Up to 25 marketplaces that you add yourself, counted for your account in each organization. Each plugin can contain up to 5,000 files and 200 MB, and 200 MB is also the largest file that **Upload plugin** accepts.            | No account limits apply; installs are per machine                                                       |                                                                                                                                                      |
| Install from a file                      | **Add > Upload plugin** with a zip of the folder                                                                                                                                                                                 | `claude --plugin-dir <path>` for one session                                                            | [Plugin structure and testing](/docs/plugins/build#test-the-plugin-on-each-surface)                                                                       |
| Browse the directory                     | **Discover** in **Customize > Plugins**, on Pro, Max, Team, and Enterprise plans. On Team and Enterprise plans, an Owner can [remove the directory as a source](/docs/plugins/admin#manage-synced-marketplaces) for the organization. | Not in `/plugin`; a plugin added from the directory on claude.ai reaches Claude Code as a synced plugin | [Publish to the directory](/docs/directory/publish)                                                                                                       |
| Organization controls                    | An Owner sets each plugin to **Not available**, **Available to install**, **Installed by default**, or **Required**                                                                                                              | In managed settings, an admin allowlists or blocks marketplaces and force-installs plugins              | [Manage plugins for your organization](/docs/plugins/admin), and the [Claude Code equivalent](https://code.claude.com/docs/en/plugins/org)                |

## Related resources

* [Plugin structure and testing](/docs/plugins/build): lay out the plugin folder and write the manifest that all three surfaces load
* [Plugin components](https://code.claude.com/docs/en/plugins/components) in the Claude Code docs: look up every component type, including the Claude Code-only ones
* [Manage plugins for your organization](/docs/plugins/admin): as an Owner, set each plugin's availability for members
