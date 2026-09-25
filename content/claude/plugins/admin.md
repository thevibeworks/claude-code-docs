> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage plugins for your organization

> Control which plugins members of your Team or Enterprise organization can use in claude.ai and Cowork: see what you have, add your own, and set availability.

Owners of a Team or Enterprise organization decide which plugins members can use in claude.ai and Cowork from [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills). You set each plugin's availability: hidden, available for members to install, installed for everyone, or required. You can also add your organization's own plugins from a GitHub or GitLab repository or a zip file.

This page is for Owners, and for Enterprise members whose role includes managing the organization's plugins.

<Note>
  * If you set plugin policy for the Claude Code command line, see [managed settings](https://code.claude.com/docs/en/plugins/org) in the Claude Code docs
  * If you want one plugin to reach members in claude.ai and Cowork and developers in the Claude Code command line, and need to decide between this page and managed settings, or use the two together, see [Roll out a plugin to your whole organization](/docs/plugins/org-rollout)
  * If you run Claude Desktop on your own model provider, see [MCP, plugins, skills, and hooks](/docs/third-party/claude-desktop/extensions)
</Note>

To start, go to [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory). From there you can [review what your organization has](#review-your-organization%E2%80%99s-inventory), [set each plugin's availability](#set-availability), or [add your organization's own plugins](#add-your-own-plugins).

## Find your organization's plugin settings

[**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory) is available on Team and Enterprise plans to Owners and Primary Owners. On Enterprise, it's also available to members whose custom role includes viewing or managing the organization's libraries. That permission is the **Libraries** row in the roles editor at **Organization settings > Roles**. The role labeled **Admin** in your members list doesn't include this page. With a role that only views libraries, you see the page without the **Add** menu and without the availability settings.

The **Plugins & skills** page has these tabs: **Inventory**, **Marketplaces**, **Organization skills**, **Requests**, and **Policy**.

### Inventory

The [**Inventory**](https://claude.ai/admin-settings/skills?tab=inventory) tab lists every plugin and skill in your organization and who can use each one. This is where you [review what you have](#review-your-organization%E2%80%99s-inventory), [set availability](#set-availability), and [add your own plugins](#add-your-own-plugins).

### Marketplaces

The [**Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces) tab lists the repositories and catalogs your organization's plugins come from, with the sync status of each one. This is where you [re-sync a marketplace, turn on automatic sync, or remove a source](#manage-synced-marketplaces).

### Organization skills

The **Organization skills** tab holds skills your organization uploaded that haven't moved into the **Inventory** tab yet. It appears only while your organization has some.

### Requests

The [**Requests**](https://claude.ai/admin-settings/skills?tab=requests) tab lists plugins and skills that members have asked to publish to your organization. This is where you [approve or deny them](#review-plugins-that-members-publish).

### Policy

The [**Policy**](https://claude.ai/admin-settings/skills?tab=policy) tab holds the switches for what members can do themselves: [create and add their own](#control-what-members-add-themselves), [share with each other](#let-members-share-plugins-with-each-other), and [publish to the organization](#review-plugins-that-members-publish). It also holds the **Skills and plugins scanning** switch, which turns on the security scan whose result the **Inventory** tab shows, and the switch that [turns plugins and skills off for everyone](#turn-plugins-and-skills-off-for-everyone).

## Review your organization's inventory

The [**Inventory**](https://claude.ai/admin-settings/skills?tab=inventory) tab lists every skill and plugin your organization governs in one table. The table includes what your organization uploaded or syncs from a marketplace, plugins from Anthropic's catalogs, which are Anthropic's default marketplaces, and what members created for themselves or shared.

Each row has these columns. Read across a row to see where an item came from and who has it:

* **Name**: the item's name, marked **Skill** or **Plugin**
* **Source**: the marketplace or repository the item comes from, or **Member** for an item a member created
* **Security scan**: the result of the item's security scan. You see this column when **Skills and plugins scanning** is on in the [**Policy**](https://claude.ai/admin-settings/skills?tab=policy) tab. Otherwise the column is **Version**
* **Capabilities**: the connectors and tools the item uses
* **Audience**: who can use the item, such as everyone or specific groups
* **Users (30d)**: how many people in your organization used the item in the last 30 days

Use the controls above the table to narrow it to the items you're looking for:

* **Search by name**: find an item by its name
* **Source**: show items from your organization's marketplaces, from Anthropic, or from members
* **Audience**: show items by who can use them
* **Add filter**: filter by **Type** to show only skills or only plugins, or by **Author** to show one person's items
* **Sort**: order the table by **Newest**, **Name A–Z**, or **Most users**

### Open an item's page

Select a row to open the item's page. For an item your organization uploaded or syncs, the page has these sections:

* **Distribution**: the item's availability and any group settings. These are the settings that [Set availability](#set-availability) and [Limit to user groups on Enterprise](#limit-to-user-groups-on-enterprise) describe
* **Connectors & tools**: what the item connects to
* **Version history**: each version with its date, who added it, and how it arrived, such as a GitHub push or an upload. To see what changed, open a version's menu and select **Compare with current**

When the item's security scan warns, fails, or couldn't run, a notice on the page gives the result and the reason. To run the scan again, open the menu on the item's page and select **Retry scan**.

To add a version of an item your organization uploaded, open the item's menu and select **Upload new version**. To remove an item your organization owns, use the delete option in the same menu.

For an item a member created for themselves, the page shows who created it, who they've shared it with, any request to publish it, and its scan status. It doesn't show the item's version history.

### Roll back to an earlier version

For an item your organization uploads, you can make any earlier version the one members get:

<Steps>
  <Step title="Open the item's page">
    On the [**Inventory**](https://claude.ai/admin-settings/skills?tab=inventory) tab, select the item's row to open its page.
  </Step>

  <Step title="Go to Version history">
    Go to **Version history**. The version members get now is marked **Current**.
  </Step>

  <Step title="Compare the earlier version">
    To see what an earlier version changes, open that version's menu and select **Compare with current**.
  </Step>

  <Step title="Revert to the version">
    Open the menu of the version you want, select **Revert to this version**, and confirm.
  </Step>
</Steps>

Members then get that version, and **Current** moves to it. Reverting deletes nothing, so every version stays in the list. To go forward again, open a newer version's menu and select **Make this the current version**.

Reverting isn't available for an item synced from a repository. Fix the plugin in the repository and push to the default branch. Then select **Re-sync** on the marketplace in the [**Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces) tab, as [Update through organization settings](/docs/plugins/org-rollout#update-through-organization-settings) describes.

While the repository is being fixed, you can [set the plugin's availability](#set-availability) to **Not available**. Members stop seeing the plugin and Claude stops loading it for them, including members who had it installed. On Enterprise, a group's own **Group access…** setting replaces the organization-wide one for that group's members, as [Limit to user groups on Enterprise](#limit-to-user-groups-on-enterprise) explains. Set any group that has one for this plugin to **Not available** as well. Set the availability back when the fix has synced. Don't use **Delete source** on the marketplace for this, because it permanently deletes every plugin in that marketplace for every member.

## Control which plugins members get

You set a plugin's availability, add your own plugins, manage synced marketplaces, decide what members can add, share, and publish, and set availability for user groups, all from the tabs of **Plugins & skills**.

### Set availability

A plugin's availability decides whether members can see the plugin, install it if they want it, get it installed automatically, or must keep it on. In the plugin's row menu, this setting is labeled **Default access**. To set it:

<Steps>
  <Step title="Open the Inventory tab">
    Go to [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory) and stay on the **Inventory** tab.
  </Step>

  <Step title="Open the plugin's menu">
    Open the menu at the end of the plugin's row.
  </Step>

  <Step title="Select Default access">
    Select **Default access**.
  </Step>

  <Step title="Choose a value">
    Choose **Not available**, **Available to install**, **Installed by default**, or **Required**.
  </Step>
</Steps>

The product shows the availability setting under other labels too: **Distribution** on the item's page, **Audience** in the table, and **Group access…** for a user group.

Each availability value decides what members see and whether they can remove the plugin:

| Setting                  | What members see                                                                               | Can members remove it                      |
| :----------------------- | :--------------------------------------------------------------------------------------------- | :----------------------------------------- |
| **Not available**        | Nothing; the plugin is hidden from **Customize > Plugins** and can't be installed              | Not applicable                             |
| **Available to install** | The plugin appears under **Discover** and members install it if they want it                   | Yes                                        |
| **Installed by default** | The plugin is already installed for every member                                               | Members can turn it off                    |
| **Required**             | The plugin is installed and always on, marked **This plugin is required by your organization** | No; members can't turn it off or remove it |

Availability doesn't add a plugin's bundled connectors. If a plugin you install by default or require includes a connector, an Owner also adds that connector in [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors), and members then connect it with their own account.

You can set availability for plugins your organization owns and for plugins from Anthropic's catalogs. An item a member created for themselves has no availability setting.

In Claude Code sessions that sync the member's account plugins, a required plugin stays on as well. [Choose a rollout route](/docs/plugins/org-rollout#choose-a-rollout-route) says which sessions sync, and [Control which synced plugins load](https://code.claude.com/docs/en/plugins/loading#control-which-synced-plugins-load) in the Claude Code docs covers what the member sees there.

### Add your own plugins

Adding a plugin or skill of your own puts it on the **Inventory** tab, private to your organization, where you then [set its availability](#set-availability) for members. To add one:

<Steps>
  <Step title="Open Plugins & skills">
    Go to [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory).
  </Step>

  <Step title="Select Add and choose the source">
    Select **Add**, then choose where the plugin or skill comes from. The menu groups these items under **Skills** and **Plugins**:

    * **Upload a skill** or **Create a skill**: one skill for your organization
    * **Upload a plugin**: a plugin zip
    * **Create a plugin**: a plugin you write in the browser
    * **Sync from GitHub** or **Sync from GitLab**: a [plugin marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) repository that contains your plugins
    * **Add marketplace**: another source of plugins, such as one of Anthropic's catalogs
  </Step>
</Steps>

A marketplace you add appears on the **Marketplaces** tab, and its plugins appear on the **Inventory** tab. Adding plugins here doesn't publish them anywhere.

[Sync your organization's plugins from a repository](/docs/plugins/org-sync) covers the repository requirements for syncing, the GitLab setup, and how members receive the plugins without needing access to the repository themselves.

### Manage synced marketplaces

The [**Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces) tab lists each marketplace your organization's plugins come from, with its sync status and its number of items. Select a marketplace to open its page, where these controls decide when it syncs and what availability its plugins start with:

* **Re-sync**: sync the marketplace now. A marketplace syncs when you select **Re-sync** or, with **Sync automatically** on, when someone pushes to the repository's default branch. Nothing syncs on a schedule. **Re-sync** is also in the marketplace's row menu on the **Marketplaces** tab
* **Sync automatically**: start a sync when someone pushes to the repository's default branch. It's in the **Sync** section, and it requires a webhook on the repository
* **Default access**: the availability for every plugin from this marketplace that doesn't have its own setting, including plugins added to it later. It's in the **Default settings** section. For Anthropic's directory, the choices are **Not available** and **Available to install** only

If a sync fails, the marketplace's page shows the date and the reason, with a **View affected items** link.

#### Remove one of Anthropic's sources

You can remove a catalog source, such as Anthropic's directory or a partner catalog, so that members no longer see plugins from it:

<Steps>
  <Step title="Open the Marketplaces tab">
    Open the [**Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces) tab.
  </Step>

  <Step title="Find the catalog's row">
    Find the row that shows **Catalog** under its name. Its **Sync** column reads **Managed by Anthropic**, or **Managed by** the partner's name for a partner catalog.
  </Step>

  <Step title="Remove it from the organization">
    Open the menu at the end of the row and select **Remove from organization**.
  </Step>

  <Step title="Confirm">
    In **Remove source**, select **Remove**.
  </Step>
</Steps>

To add the source back, select **Add**, then **Add marketplace**, then **Browse Anthropic sources**, and select **Add** next to the source.

### Control what members add themselves

Members can add plugins of their own from **Customize > Plugins > Add**: a marketplace by URL, an uploaded file, **Create a plugin**, or **Create with Claude**. The setting that lets members create skills also controls those options.

Go to [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy) and turn **User-created skills** on or off. When **User-created skills** is off, members can't upload or create skills, and the plugin options don't appear in their **Add** menu.

For the Claude Code command line, the counterpart is managed settings. [Restrict what users can install](https://code.claude.com/docs/en/plugins/org#restrict-what-users-can-install) in the Claude Code docs covers those keys.

### Turn plugins and skills off for everyone

You can turn plugins and skills off for your whole organization. This also stops Claude Code from loading the plugins it syncs from members' claude.ai accounts.

<Steps>
  <Step title="Open the Policy tab">
    Go to [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy).
  </Step>

  <Step title="Turn off Skills">
    Turn off **Skills**.
  </Step>
</Steps>

Members then see **Skills must be enabled in order to use plugins.** on **Customize > Plugins**, and they can't add or use plugins there. The organization's own skills are off as well.

To stop the sync into Claude Code and leave plugins on in claude.ai and Cowork, set `syncClaudeAiPlugins` to `false` in Claude Code managed settings instead. [Control which synced plugins load](https://code.claude.com/docs/en/plugins/loading#control-which-synced-plugins-load) in the Claude Code docs covers that setting.

### Let members share plugins with each other

Members can share a plugin they made with specific people without involving you. In [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy), **Skill sharing** controls whether members can share skills and plugins they made with specific people in your organization. On Enterprise, **Share with groups** lets them share with user groups as well. [Share a plugin with specific people](/docs/plugins/share#share-a-plugin-with-specific-people) covers what members and recipients see.

### Stop sharing by a member who left

When someone leaves your organization, the items they shared keep working for the people they shared them with. The **Inventory** tab shows a notice with the number of former members who still share items. To end that sharing:

<Steps>
  <Step title="Open the review">
    On the [**Inventory**](https://claude.ai/admin-settings/skills?tab=inventory) tab, select **Review** in the notice.
  </Step>

  <Step title="Stop sharing">
    Select **Stop sharing** for an item, or stop sharing all of one former member's items at once.
  </Step>

  <Step title="Confirm">
    Confirm. Everyone the item is shared with loses access right away.
  </Step>
</Steps>

You can also open a former member's item from the table. Its page has an **Owner has left** section with **Stop sharing** and **Delete**.

### Review plugins that members publish

Members on Team and Enterprise plans can publish a plugin they made to your organization's library with **Publish to org** on the plugin's page. You decide whether that's allowed and whether each request waits for your approval. [Publish a plugin to your organization](/docs/plugins/share#publish-a-plugin-to-your-organization) covers the member's side.

#### Set the publishing policy

The **Publishing** setting decides whether members can publish to your organization and whether each request waits for review. Set it in [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy). Owners and Primary Owners can change it. The same setting covers skills and plugins, and it has these values:

| Publishing          | What members can do                                                                                                                          |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **Requires review** | Submit a plugin for review. Nothing reaches other members until a reviewer approves the request.                                             |
| **Open**            | Publish without review. Where your organization scans what members publish, the plugin goes live after the security scan passes.             |
| **Off**             | Nothing. **Publish to org** doesn't appear for members, and requests that were already waiting are hidden until you turn publishing back on. |

If nobody in your organization has chosen a **Publishing** value, your plan's default applies:

* **Team**: **Open**
* **Enterprise**: **Off**. On October 2, 2026, the Enterprise default becomes **Requires review**. To keep a different value, choose it before then

#### Review a request

Under **Requires review**, nothing reaches other members until a reviewer approves the request. To approve or deny a request, you need to be an Owner or Primary Owner. On Enterprise, a member whose custom role includes managing the organization's libraries can review requests too.

Requests to publish wait in [**Organization settings > Plugins & skills > Requests**](https://claude.ai/admin-settings/skills?tab=requests). You can't review a request you submitted yourself. A pending request that looks similar to other items in your organization is tagged **Possible duplicate**, and its review page lists up to three similar items, each with a **Compare** link.

To review a request:

<Steps>
  <Step title="Open the request">
    Open the request to see what the member submitted.
  </Step>

  <Step title="Approve or deny">
    Select **Approve** or **Deny**.
  </Step>

  <Step title="Set availability or give a reason">
    If you approve, choose the plugin's availability, as [Set availability](#set-availability) describes.

    If you deny, enter a reason, which the member receives by email and sees on their plugin's page. A denial closes that request, and the member can revise the plugin and submit a new one.
  </Step>
</Steps>

A plugin that a member published appears on the **Inventory** tab with your organization's other plugins. You [set its availability](#set-availability) there, and you can delete it from its menu.

### Limit to user groups on Enterprise

On Enterprise plans, you can give a user group its own availability for a plugin. For example, one team gets a plugin installed by default while the rest of the organization doesn't see it.

User groups are the ones listed at **Organization settings > Groups**. They sync from your identity provider through SCIM, or you add one there with **Add group**. If your organization has no groups, the picker shows **No groups in this organization.**

To set availability for a group, you need to be an Owner or Primary Owner, or hold a custom role with **Libraries** set to **Can manage** and **Identity & Access** set to **Can view**. Then:

<Steps>
  <Step title="Open the Inventory tab">
    Go to [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory) and stay on the **Inventory** tab.
  </Step>

  <Step title="Open the plugin's menu">
    Open the menu at the end of the plugin's row. **Default access** is the availability for the whole organization.
  </Step>

  <Step title="Select Group access">
    Select **Group access…**.
  </Step>

  <Step title="Choose the group and its availability">
    Choose a group and the availability for it.
  </Step>
</Steps>

When a member falls under more than one setting for a plugin, these rules decide which one applies:

* **Group over organization**: the setting you choose for a group replaces the organization-wide setting for that group's members, even when the group's setting is stricter. A member who is only in a group set to **Not available** doesn't get a plugin that's **Required** organization-wide. You can also set a group to **Installed by default** or **Required** for a plugin that's **Not available** organization-wide
* **Several groups**: when a member is in several groups with different settings for a plugin, the most permissive setting applies, in this order: **Required**, **Installed by default**, **Available to install**, **Not available**

On a Team plan, which has no group setting, you can pilot a plugin with a few people before everyone gets it: with [**User-created skills**](#control-what-members-add-themselves) on, upload the plugin to your own account from [**Customize > Plugins**](https://claude.ai/customize/plugins) with **Add > Upload plugin**, and [share it with specific people](/docs/plugins/share#share-a-plugin-with-specific-people). When the pilot is done, add it for the organization and set its availability.

## Track usage in your organization

Members on Team and Enterprise plans see usage figures on a plugin's or skill's own page, as [how a plugin is used in your organization](/docs/plugins/overview#track-plugin-usage-in-your-organization) describes. The [**Inventory**](https://claude.ai/admin-settings/skills?tab=inventory) tab adds one view across all of them. To find which items people use, read the **Users (30d)** column or sort by **Most users**:

* **Users (30d)**: the number of distinct people in your organization who used the item in the last 30 days. A dash means there's no data for the item, not that nobody used it
* **Most users**: a **Sort** option that puts the most-used items first

Select an item to open its page, which shows **Users (30d)** and **Activity (30d)**, the number of times the item was used in the last 30 days. These are the same figures members see on the item's page in **Customize**.

The **Inventory** tab has no export.

## Related organization controls

You control connectors, Claude Code policy, monitoring, and directory submissions separately from plugin availability, and directory review is described with the submission pages:

* [Roll out a plugin to your whole organization](/docs/plugins/org-rollout): reach members in claude.ai and Cowork and developers in the Claude Code command line with one plugin
* [Manage Claude Code plugins for your organization](https://code.claude.com/docs/en/plugins/org): allowlist marketplaces, force-install plugins, and turn account sync on or off for the command line with managed settings
* [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors): choose which connectors members can add, including a plugin's bundled connectors
* [Monitoring](/docs/cowork/monitoring): export members' Cowork activity to your OpenTelemetry collector
* [Prepare for review](/docs/directory/publish#prepare-for-review): how Anthropic checks plugins listed in the directory, with automated validation and a security scan on every version and a person reviewing each new listing, for when you're deciding whether to keep the directory as a source
* [Publish to the directory](/docs/directory/publish): submit a plugin for a public listing through the developer portal, which the **Directory** item in organization settings opens for members with permission to submit
