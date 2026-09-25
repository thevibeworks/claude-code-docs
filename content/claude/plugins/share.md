> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Share a plugin with teammates

> Share a plugin you made with specific people in your Team or Enterprise organization, or publish it to your organization's library.

On a Team or Enterprise plan, you can get a [plugin](/docs/plugins/overview) you made to other people in your organization. You share it with specific people yourself, or you publish it to your organization's library, where an Owner decides who can find and install it.

This page is for someone on a Team or Enterprise plan who created or uploaded a plugin, for example with [Create a plugin with Claude](/docs/plugins/create-with-claude).

<Note>
  * If you're an Owner reviewing what members publish, see [Manage plugins for your organization](/docs/plugins/admin)
  * If you want a wider audience than your organization, see [Plugin structure and testing](/docs/plugins/build) and [Publish to the directory](/docs/directory/publish)
</Note>

To give the plugin to people you name, go to [Share a plugin with specific people](#share-a-plugin-with-specific-people). To reach the whole organization, go to [Publish a plugin to your organization](#publish-a-plugin-to-your-organization).

## Share a plugin with specific people

On a Team or Enterprise plan, you can give a plugin you created or uploaded to specific people in your organization yourself. You don't need an Owner, and nothing is published or reviewed.

### Choose how to distribute a plugin

You can get the plugin to specific people, to your organization's library, to someone outside your organization, or to a wider audience:

* **Share**: specific people in your organization get the plugin from you directly
* **Publish to org**: the plugin goes to your organization's library, where an Owner decides who can find and install it. See [Publish a plugin to your organization](#publish-a-plugin-to-your-organization)
* **The plugin file**: someone in another organization or on a personal plan adds the `.plugin` file or a zip of the plugin with **Add > Upload plugin**. It becomes a separate plugin on their account
* **A marketplace or the directory**: for a wider audience, put the plugin in a Git repository as a folder, as [Plugin structure and testing](/docs/plugins/build) describes, then share it through [your own marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) or [the directory](/docs/directory/publish)

### Share the plugin

Sharing gives the people you name your plugin in their **Customize > Plugins** list, turned off until they turn it on. To share with specific people:

<Steps>
  <Step title="Open the plugin and select Share">
    Go to [**Customize > Plugins**](https://claude.ai/customize/plugins) in claude.ai or the desktop app and open the plugin. Select **Share** at the top of its page. The plugin's menu in your **Your plugins** list has the same **Share** item.
  </Step>

  <Step title="Add people">
    Add each person by name or email address, then confirm the share.
  </Step>
</Steps>

### What the people you share with get

**Share** reaches only members of your organization, and the people you share with can use the plugin but not change it:

* **Who you can share with**: members of the organization you're in. If you enter the email address of someone who isn't a member yet, they're invited to join your organization first, where your organization lets members send invitations. On Enterprise, where an Owner has turned on **Share with groups**, you can also add a user group. To reach someone in another organization or on a personal plan, send them the plugin file instead. **Share** has no option for the whole organization. To reach everyone, [publish the plugin to your organization](#publish-a-plugin-to-your-organization)
* **What they see**: a notice in claude.ai that you shared the plugin, and the plugin listed under **Shared with you** on the **Your plugins** tab of **Customize > Plugins**. It's turned off until they turn it on
* **What they do**: open the plugin and turn on its toggle. When the plugin includes something that runs on their computer, such as a local MCP server or a hook, Claude asks them to confirm first
* **What they can change**: nothing in the plugin. They can view it, turn it on or off, and use it. It stays in their list for as long as you share it
* **Your later edits**: people who turned the plugin on get your new version wherever they use Claude, including chat on the web
* **Connectors**: your connector sign-ins aren't shared. Each person adds or connects the plugin's connectors with their own account, as [Bundled connectors](/docs/plugins/overview#bundled-connectors) describes
* **The link**: **Copy link** in the share dialog copies a link to the plugin's page. Only people you've shared the plugin with can open it

### Stop sharing a plugin

When you stop sharing a plugin with someone, the plugin stops loading for them. To stop sharing, select **Share** again and remove the person from the list of people with access.

### If you can't share a plugin

**Share** appears only on a plugin you created or uploaded yourself, not on one you added from a marketplace or that your organization provides. On your own plugin, these are the cases where you can't share:

* **The share dialog says "Direct sharing is turned off for your organization"**: an Owner turned off **Skill sharing**, the setting that covers both skills and plugins. Ask an Owner to turn it on in [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy). Until then you can open **Share** to remove people, but you can't add anyone
* **Share is missing and Skills is turned off for your organization**: ask an Owner to turn on **Skills** on the same **Policy** tab
* **Share is missing and your organization's security scan blocked the plugin**: a blocked plugin can't be shared
* **You're on a personal plan**: sharing with specific people needs a Team or Enterprise plan. **Share** either offers an upgrade to a Team plan or doesn't appear

## Publish a plugin to your organization

Publishing puts your plugin in your organization's library, where an Owner decides who can find and install it. It's available on Team and Enterprise plans, and whether you can do it depends on the **Publishing** setting an Owner has chosen for your organization.

Sharing reaches only the people you name and needs no approval. Publishing can reach the whole organization, and under the **Requires review** setting it waits for an Owner to approve it.

To publish, open the plugin from **Customize > Plugins** and select **Publish to org** at the top of its page. This is what happens next under each **Publishing** setting:

* **Requires review**: you submit the plugin for review and propose how it installs for members: **Available to install**, **Installed by default**, or **Required**. The version you submit is frozen, so edits you make afterward aren't part of the request. The reviewer sees your proposal and can change it before approving. An Owner approves or denies it in [**Organization settings > Plugins & skills > Requests**](https://claude.ai/admin-settings/skills?tab=requests), and you can't approve your own submission. You get the decision by email, with the reviewer's reason if it's denied
* **Open**: the plugin is published without review. Where your organization scans what members publish, it goes live after the security scan passes
* **Off**: your organization doesn't accept plugins from members, and **Publish to org** doesn't appear on your plugin

On a Team plan, the **Publishing** setting is **Open** unless an Owner has changed it. [Review plugins that members publish](/docs/plugins/admin#review-plugins-that-members-publish) lists the default for each plan.

You see the result on the plugin's own page, which shows whether the submission is waiting for review, denied, or published:

* **While it's waiting**: you can withdraw it from the plugin's page
* **If it's denied**: the page shows the date and the reviewer's reason, and **Publish to org** is available again so that you can revise the plugin and submit a new request
* **After a version is published**: later edits reach your organization only when you publish again

## Next steps

* [Create a plugin with Claude](/docs/plugins/create-with-claude): make a plugin in claude.ai or the desktop app with Claude's help
* [Manage plugins for your organization](/docs/plugins/admin): if you're an Owner, turn sharing and publishing on or off for members
* [Plugin structure and testing](/docs/plugins/build): write the plugin as a folder for a marketplace or the directory
