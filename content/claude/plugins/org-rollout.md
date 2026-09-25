> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Roll out a plugin to your whole organization

> Get your organization's plugin to members in claude.ai and Cowork and to developers in Claude Code by using organization settings and managed settings together.

You can get your organization's own plugin to every member two ways, and each reaches different people:

* **Organization settings on claude.ai**: members get the plugin on their accounts, where chat and Cowork use it. Plugins you add this way stay private to your organization
* **Claude Code managed settings**: Claude Code installs the plugin on developers' machines

This page is for the person rolling out a plugin their organization built, on a Team or Enterprise plan.

<Note>
  * If you want to list a plugin publicly, see [Publish to the directory](/docs/directory/publish)
  * If you haven't built the plugin yet, see [Build your first plugin](/docs/plugins/quickstart) and [Plugin structure and testing](/docs/plugins/build)
</Note>

## Choose a rollout route

The table compares organization settings on claude.ai with Claude Code managed settings on who receives the plugin and what each route asks of you.

|                           | Organization settings on claude.ai                                                                                 | Claude Code managed settings                                                                                                    |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| Who receives the plugin   | Members, on their claude.ai account: in chat, in Cowork, and in Claude Code sessions that sync from that account   | Claude Code on every machine that receives the settings                                                                         |
| Where you set it up       | [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory)              | Server-managed settings, an MDM policy, or a `managed-settings.json` file                                                       |
| What you set              | An availability for each plugin, such as **Installed by default** or **Required**                                  | `extraKnownMarketplaces` to register your marketplace and `enabledPlugins` to install plugins from it                           |
| Access to your repository | Members need none. Organization sync reads the repository through your organization's GitHub or GitLab connection. | Each machine fetches the marketplace itself. For a private Git repository, it uses the Git credentials already on that machine. |
| Which components load     | Depends on the surface. See [Plugin feature support across platforms](/docs/plugins/platform-support).                  | Every component                                                                                                                 |
| Full setup steps          | [Manage plugins for your organization](/docs/plugins/admin)                                                             | [Manage Claude Code plugins for your organization](https://code.claude.com/docs/en/plugins/org) in the Claude Code docs         |

A plugin on a member's account reaches Claude Code as a synced plugin in Cowork and in terminal sessions where the member signs in with their claude.ai account on Claude Code v2.1.273 or later. [Plugins synced from claude.ai](https://code.claude.com/docs/en/plugins/loading#synced-plugins) has the sign-in and timing rules. For developers whose terminal sessions don't sync from a claude.ai account, use managed settings.

## Roll out through both routes

Use both routes when the plugin is for people in chat and Cowork and also for developers whose Claude Code sessions don't sync from a claude.ai account.

<Steps>
  <Step title="Lay out the repository as a marketplace">
    Put the plugin in a Git repository with a `.claude-plugin/marketplace.json` that lists it. You use the same repository for both routes. [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) in the Claude Code docs covers the format.
  </Step>

  <Step title="Check the repository against the organization sync rules">
    Organization sync is stricter than Claude Code about the repository's visibility and about which plugin source types it accepts, and it rejects a plugin with a top-level `bin/` directory. Check [the plugin sources that organization sync accepts](/docs/plugins/org-sync#plugin-sources-that-organization-sync-accepts) before you continue.
  </Step>

  <Step title="Sync the repository from organization settings">
    In [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory), add the repository as [Add your own plugins](/docs/plugins/admin#add-your-own-plugins) describes, then [set each plugin's availability](/docs/plugins/admin#set-availability).
  </Step>

  <Step title="Register the same marketplace in managed settings">
    Set `extraKnownMarketplaces` and `enabledPlugins` as [Pre-install and require plugins](https://code.claude.com/docs/en/plugins/org#pre-install-and-require-plugins) describes. To limit developers to your marketplace, see [Restrict what users can install](https://code.claude.com/docs/en/plugins/org#restrict-what-users-can-install).
  </Step>

  <Step title="Confirm on each surface">
    * **In claude.ai**: as a member, open [**Customize > Plugins**](https://claude.ai/customize/plugins) and check that the plugin appears there
    * **On a developer's machine**: start Claude Code and run `/plugin`, which lists the marketplace and the plugin
  </Step>
</Steps>

### If a developer has the plugin from both routes

A developer can end up with the plugin from both routes. Claude Code loads one plugin per name. It loads the copy that managed settings install and reports the synced copy as not loaded, as [Name conflicts](https://code.claude.com/docs/en/plugins/loading#name-conflicts) describes.

## Build one repository for both audiences

One plugin folder can serve both audiences, because each surface skips the components it doesn't load. Hooks and agents load in Cowork and Claude Code and not in chat, and a local MCP server doesn't run in chat. Check each component you include against [Plugin feature support across platforms](/docs/plugins/platform-support) before you promise a behavior to people who only use chat.

## Update a plugin you've rolled out

You release an update by pushing to the repository. How the update reaches people depends on the route.

### Update through organization settings

Organization sync reads the repository's default branch, and members get the new version after the marketplace syncs. It syncs when an Owner selects **Re-sync** or, with **Sync automatically** on, when someone pushes to the default branch. Nothing syncs on a schedule. Tags aren't read, so a tag by itself releases nothing.

**Re-sync** syncs the marketplace now, so members get the version on the default branch without waiting for a push. To re-sync:

<Steps>
  <Step title="Open the Marketplaces tab">
    Go to [**Organization settings > Plugins & skills > Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces).
  </Step>

  <Step title="Re-sync the marketplace">
    Open the menu in the marketplace's row and select **Re-sync**.
  </Step>

  <Step title="Retry if you synced recently">
    If you see **You synced recently**, wait the number of seconds the message gives, then select **Re-sync** again.
  </Step>
</Steps>

### Update through managed settings

Claude Code refreshes a marketplace and updates the plugins installed from it when auto-update is on for that marketplace. [Set update policy](https://code.claude.com/docs/en/plugins/org#set-update-policy) covers turning it on for your fleet.

If your `plugin.json` sets `version`, raise it with every release, because Claude Code compares it to decide whether an installed plugin has an update.

## Next steps

* [Sync your organization's plugins from a repository](/docs/plugins/org-sync): check your repository and plugin sources against the rules organization sync enforces
* [Manage plugins for your organization](/docs/plugins/admin): set availability for everyone or for user groups, and control what members can add themselves
* [Manage Claude Code plugins for your organization](https://code.claude.com/docs/en/plugins/org): set the managed-settings keys and deliver them to developers' machines
