> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish to the directory

> Submit a plugin or MCP connector to Anthropic's directory: the two submission kinds, who can submit, what review involves, and where to start.

The directory is Anthropic's catalog of plugins and connectors that people browse inside Claude, on the [**Customize**](https://claude.ai/customize) page in claude.ai and the desktop app. A listing reaches people in claude.ai on the web, the desktop and mobile apps, and Cowork, and a plugin they add is also available in their Claude Code sessions.

This page is for developers who have built a plugin, or the MCP server behind one, and want it listed. Anyone on a paid Claude plan can submit, there's no partner program to apply to first, and Anthropic checks each submission before it's listed.

<Note>
  * If you're still deciding what goes in your plugin, see [Decide what to include in your plugin](/docs/connectors/building/what-to-build)
  * If you want to build a small example plugin and submit it, see [Build your first plugin](/docs/plugins/quickstart)
  * If you want to share a plugin without a public listing, use [your own marketplace](https://code.claude.com/docs/en/plugins/publish) for Claude Code or [roll it out to your whole organization](/docs/plugins/org-rollout)
  * If you came here from [Claude Marketplace](https://claude.com/marketplace), the website where you browse plugins, connectors, partner products, and service partners, you're in the right place: there's no separate Claude Marketplace submission, and you submit to the directory instead
</Note>

If you're ready to submit, open the [developer portal](https://claude.ai/directory/manage) or jump to [Start a submission in the developer portal](#start-a-submission-in-the-developer-portal).

## Before you submit to the directory

A directory listing is either a plugin bundle or an MCP connector.

### Submit your plugin, and your MCP server as a connector

A plugin bundle is the main thing you submit: one listing that packages whatever the plugin contains, whether that's skills, an MCP connector reference, commands, agents, or any combination. If you also run the remote MCP server that plugin points at, you submit the server as its own MCP connector too. When you start a submission, the developer portal asks which kind you're submitting:

|                     | Plugin bundle                                                                   | MCP connector                                                       |
| :------------------ | :------------------------------------------------------------------------------ | :------------------------------------------------------------------ |
| What it is          | A plugin folder with skills, commands, agents, hooks, and MCP server references | One remote MCP server that people connect to reach your app or data |
| Where it comes from | A GitHub repository, which must be public before the listing goes live          | The server's URL, with no repository needed                         |
| How it's listed     | As a plugin with all of its components                                          | As a connector people connect to from the directory                 |

If you have a remote MCP server, always submit it as an MCP connector, even when a plugin you're submitting already references it. Submitting the server as a connector gives your organization the connector's listing, its dashboard, and the option to pair it with your plugin:

* **The connector's listing**: you edit its details and its authentication configuration
* **The connector's dashboard**: it shows the server's health and usage by tool, which a plugin's **Usage** tab doesn't break out
* **Pairing with your plugin**: when the connector and a plugin bundle that references it are submitted from the same organization, you can pair the two listings

For your own product, make two submissions: the server as an MCP connector, then the plugin bundle whose skills teach Claude how to use it. Point the bundle's MCP server configuration at the same URL, so people who have both see one set of tools rather than two.

Desktop extension listings in the directory are deprecated, and the directory no longer accepts local MCP servers packaged as desktop extensions (MCPB). To distribute a local MCP server through the directory, include it in a plugin bundle. [Compare component support by app](/docs/plugins/platform-support#compare-component-support-by-app) shows where a plugin's local servers run.

Skills aren't a submission type on their own. Put them in a bundle.

### What a listing gets you

A directory listing gives you:

* **One listing across Claude's apps**: people find it in claude.ai on the web, the desktop and mobile apps, and Cowork, and a plugin they add is also available in their Claude Code sessions
* **One developer portal for the whole life of a listing**: at [claude.ai/directory/manage](https://claude.ai/directory/manage) you submit, follow each submission's status, publish new versions, see usage, and change or delist the listing. [Track your directory submission](/docs/directory/submission-status) explains each status
* **Updates without resubmitting**: after the first submission, you keep the listing current by merging to the tracked branch as you normally release. The directory picks up each commit, scans it, and once it's published serves it to the people who have your plugin. [Update a published plugin](/docs/plugins/submit#update-a-published-plugin) covers the steps
* **Usage figures**: a published plugin's **Usage** tab shows installs, versions, how often each skill and MCP server runs, and error rates. A listed connector has a dashboard with server health and usage by tool. [Track published plugin usage](/docs/connectors/building/after-publishing#track-published-plugin-usage) and [Manage your directory listing](/docs/connectors/building/managing-your-listing) cover each

### Confirm you can submit to the directory

You submit from a claude.ai account, and the listing belongs to the organization you submit from. Before you start, confirm each of these:

* **Plan**: Pro, Max, Team, or Enterprise. Free accounts can't submit
* **Role**: on Pro and Max, you submit from your own account and there's no role to check. On Team and Enterprise, an Owner can submit. On Enterprise, an Owner can also grant the **Directory** permission to other members through a custom role under [**Organization settings > Roles**](https://claude.ai/admin-settings/roles). If you don't have one of those roles, ask an Owner
* **Which organization**: for a plugin bundle, the first organization to submit a given repository folder holds that listing, and the portal refuses a second organization's submission of the same one. Submit from the organization that should own the listing long term

### Move an earlier submission to the developer portal

A listing you submitted before the developer portal existed stays as it is. Move it to the portal to get what the portal adds:

* New versions that the directory scans and, once they're published, serves to the people who have your plugin
* A status for each submission
* Usage figures for a published plugin

The earlier Claude Console form for plugin submissions is no longer supported. To move a submission you made through it, open [**Plugin submissions**](https://platform.claude.com/plugins/submissions) in the Claude Console:

* **A submission with a Withdraw button**: select **Withdraw**. Then submit the plugin again at [claude.ai/directory/manage](https://claude.ai/directory/manage) from a claude.ai account
* **A submission with no Withdraw button**: email `directory@anthropic.com` to have it moved to the developer portal instead of starting a new submission there. If you already saved a draft in the developer portal for the same repository and folder, [delete the draft](/docs/plugins/submit#withdraw-or-delist-a-plugin) first

Until the Console submission is withdrawn or moved, the portal can refuse **Submit for review** for the same repository and folder with **Already submitted by another organization**.

### Prepare for review

Anthropic checks every submission before it's listed, and checks a plugin bundle again with each new version.

* **Plugin bundles**: every version gets automated validation and a security scan, and a person reviews a new listing before it goes live. The [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) lists what validation checks
* **MCP connectors**: every submission is scanned automatically for policy compliance and, by default, listed as a Community connector. Anthropic may escalate a listing to Verified review, in which a reviewer tests each tool against the [connector pre-submission checklist](/docs/connectors/building/review-criteria)

Every listing is subject to the [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) and [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).

There's no separate application for the **Verified** label or for where in the directory a listing is placed. Anthropic decides both during review, and [Connector verification](/docs/connectors/verification#list-your-own-connector) explains how a listing becomes Verified and what each label means to people installing it.

Review time isn't fixed. Your submission's current state shows in the portal, and [Track your directory submission](/docs/directory/submission-status) explains what each status in the portal means and who acts next.

## Start a submission in the developer portal

You submit and maintain listings in the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage).

To start a submission:

<Steps>
  <Step title="Select Submit new">
    In the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage), select **Submit new**.
  </Step>

  <Step title="Choose the submission type">
    Under **What would you like to submit?**, choose **Plugin bundle** or **MCP connector**.
  </Step>

  <Step title="Follow the checklist and submit pages">
    Work through the checklist and submit pages for that kind:

    * [Plugin pre-submission checklist](/docs/plugins/pre-submission-checklist), then [Submit a plugin](/docs/plugins/submit): for a plugin bundle
    * [Connector pre-submission checklist](/docs/connectors/building/review-criteria), then [Submit a connector](/docs/connectors/building/submission): for an MCP connector
  </Step>
</Steps>

## Next steps

These pages cover building and submitting a first plugin and, once a listing is published, maintaining it from the same portal:

* [Build your first plugin](/docs/plugins/quickstart): build a small example plugin and submit it to the directory
* [Track your submission](/docs/directory/submission-status): check what your submission's status means and who acts next
* [After publishing](/docs/connectors/building/after-publishing): update your server or plugin, and delist
* [Track published plugin usage](/docs/connectors/building/after-publishing#track-published-plugin-usage): see installs, versions, runs, and error rates on the plugin's **Usage** tab
* [Manage your directory listing](/docs/connectors/building/managing-your-listing): for an MCP connector, check health and usage metrics and edit the listing
