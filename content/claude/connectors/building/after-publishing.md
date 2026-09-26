> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage your listing after publishing

> Update your MCP server, plugin, and directory listing after publication, keep your listing URL stable, and delist when you need to.

Once your connector or plugin is listed in the directory, you keep it current from the same developer portal you submitted from, at [claude.ai/directory/manage](https://claude.ai/directory/manage).

This page is for the developer who owns a published listing.

<Note>
  If your submission isn't live yet, see [Track your directory submission](/docs/directory/submission-status), which explains what each status in the portal means and who acts next.
</Note>

You can [update what you've published](#update-a-published-connector-or-plugin), [track how a published plugin is used](#track-published-plugin-usage), [share your listing's permanent URL](#directory-listing-urls-are-permanent), or [delist](#delist-a-connector-or-plugin).

## Update a published connector or plugin

You don't resubmit to Anthropic to change a listed MCP server's tools or a listed plugin's files.

### MCP server changes

To add, change, or remove tools, deploy the change to your server. The tool names shown on your directory listing are part of the listing details, so update them with a [listing edit](/docs/connectors/building/managing-your-listing#edit-your-listing), which a reviewer approves.

### Plugin changes

To update a listed plugin, push to the branch or tag the directory tracks for it. The directory picks up the new commit, runs the same validation and security scan as your first submission, and shows the result as a new version on the plugin's page in the portal. If you set `version` in `plugin.json`, raise it with each release, because installed copies use it to tell that an update exists.

A version that doesn't pass, or that is held for a reviewer, doesn't take your listing down: the directory keeps serving the last published version until a newer one is published. [Submit a plugin](/docs/plugins/submit#update-a-published-plugin) covers how the directory finds new commits, how to have GitHub notify it on push, and how to change the tracked branch or tag.

### Listing details

For a connector, edit your description, categories, icon, and other listing details from the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage). See [Manage your directory listing](/docs/connectors/building/managing-your-listing) for what you can edit directly and which changes require review.

A plugin listing's name and short description come from `plugin.json` and the README of the version that's live. To change them, edit those files and publish a new version, as [Plugin changes](#plugin-changes) describes. If an Anthropic reviewer edited either field during review, the listing keeps the reviewer's text. From the plugin's **Settings** tab in the developer portal, you can change which surfaces the plugin is listed on, your contact email, and your answer on whether the plugin collects or transmits user data.

## Track published plugin usage

A published plugin's page in the developer portal has a **Usage** tab. The portal is open to the people who [can submit](/docs/directory/publish#confirm-you-can-submit-to-the-directory). Use it to see how many accounts install and use the plugin, which version they're on, and whether the plugin loads and its MCP servers respond without errors.

The **Usage** tab covers a period you choose, up to 90 days, and you can export the figures as CSV. It shows these groups of figures:

* **Reach**: installs, active accounts, and retention, with installs broken out by surface and by where the install came from, such as the **Discover** tab
* **Versions**: the share of accounts on each version
* **Components**: how often each skill, command, agent, hook, and MCP server is used
* **Quality**: load errors by Claude Code version, and tool calls, error rate, and latency for each MCP server
* **Directory funnel**: listing views, install clicks, and installs

Figures are computed once a day in UTC, and the tab shows the date the data runs through. Until usage is recorded for your plugin, the tab is marked **Preview** and shows sample numbers.

For a connector, [Manage your directory listing](/docs/connectors/building/managing-your-listing#server-health-and-usage-metrics) covers the health badge and usage metrics.

## Directory listing URLs are permanent

Your directory slug is fixed after publication. It determines your connector's permanent listing URL:

```text theme={null}
https://claude.ai/directory/connectors/SLUG
```

Share the listing URL from your own documentation or a **Connect to Claude** button to send users directly to your listing. You can change display names via the dashboard, but you can't change the URL slug.

## Delist a connector or plugin

You delist a plugin from the developer portal and a connector by email:

* **To remove a plugin listing:** open the plugin in the developer portal and select **Delist plugin** from the plugin's menu or its **Settings** tab
* **To bring a plugin listing back:** select **Relist plugin** on the **Settings** tab, which asks the directory to restore the listing
* **To remove a connector from the directory:** email `mcp-review@anthropic.com`

## Next steps

* [Manage your directory listing](/docs/connectors/building/managing-your-listing): for a connector, check submission status and health and usage metrics, and edit the listing
* [Connector verification](/docs/connectors/verification#list-your-own-connector): see how a listing becomes Verified and what each label means to people installing it
