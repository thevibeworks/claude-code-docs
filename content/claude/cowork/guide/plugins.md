> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install plugins

> Add packaged skills, connectors, and agents to Cowork from the plugin marketplace or a file.

A plugin is a package that extends what Claude can do in Cowork. Installing one can add skills, MCP connectors, subagents, commands, or hooks in a single step. Plugins come from the marketplace, from your organization, or from a file you upload.

A plugin you install is saved to your account, so its skills and connectors are also available in chat and in Claude Code. [Plugins](/docs/plugins/overview) covers what each surface loads; this page covers the Cowork side.

To get started, [install a plugin](#install-a-plugin) from **Customize**, or [add a Git repository as a marketplace](#use-a-git-repository-as-a-marketplace) to share plugins without publishing them.

## What a plugin can contain

A plugin can contain any combination of the following components.

| Component  | What it adds                                               |
| ---------- | ---------------------------------------------------------- |
| Skills     | Reusable instructions that teach Claude a workflow         |
| Connectors | MCP servers that give Claude access to an external service |
| Agents     | Specialized subagents Claude can delegate to               |
| Hooks      | Scripts that run at defined points in a session            |

After installing, open the plugin to see what it provides. Skills and agents appear as tabs; connectors and hooks have their own pages.

## Install a plugin

You browse, install, and upload plugins from the **Plugins** page. Open **Customize** in the sidebar, then select **Plugins**.

<Steps>
  <Step title="Browse the marketplace">
    Select **Discover** to see available plugins. The default marketplace
    is Anthropic's official catalog; you can add other marketplaces by URL.
  </Step>

  <Step title="Install">
    Select a plugin and click **Install**. Installing doesn't add or sign you in
    to any connector. If the plugin includes connectors, open its **Connectors**
    tab afterward to add or connect each one.
  </Step>

  <Step title="Review components">
    Open the installed plugin to see its skills, connectors, agents, and hooks.
    Select **Disable plugin** to turn the whole plugin off, and connect or
    disconnect each connector on its own from the **Connectors** tab.
  </Step>
</Steps>

To install from a file instead, select the upload option on the Plugins page and select the plugin package.

## Use a Git repository as a marketplace

A Git repository that contains plugin packages can serve as a marketplace, which lets you share plugins without publishing to the public catalog. For a marketplace you add yourself, repositories on GitHub, including GitHub Enterprise, are supported, and public repositories on GitLab and Bitbucket also work. To distribute plugins to everyone in a Team or Enterprise organization, an Owner syncs the repository from organization settings instead, as [Manage plugins for your organization](/docs/plugins/admin#add-your-own-plugins) describes.

<Steps>
  <Step title="Add the repository">
    On the Plugins page, select **Add marketplace** and enter the repository's
    URL. Cowork accepts the standard `https://github.com/owner/repo` form and
    the `owner/repo` shorthand for GitHub.
  </Step>

  <Step title="Install plugins from it">
    Plugins defined in the repository appear alongside plugins from other
    marketplaces. Install them the same way.
  </Step>
</Steps>

Select **Check for updates** on a marketplace to pull the latest plugins from its repository, or turn on **Sync automatically**.

For marketplaces your organization manages, see [Manage plugins for your organization](/docs/plugins/admin), or [MCP, plugins, skills, and hooks](/docs/cowork/3p/extensions) if your organization deploys Claude Desktop with its own model provider.

## Limits

The following are the default limits for plugin packages and marketplaces.

| Limit                              | Value  |
| ---------------------------------- | ------ |
| Plugin package size (uncompressed) | 200 MB |
| Files per plugin package           | 5,000  |
| Marketplace repository archive     | 512 MB |
| Plugins per marketplace            | 500    |
| Marketplaces you can add           | 25     |

The in-app skill viewer previews individual files up to 1 MB. Larger files appear in the file list as "too large to preview" but are still available to Claude at runtime.

## Plugins managed by your organization

On Team and Enterprise plans, administrators can require certain plugins for everyone in the organization. Required plugins install automatically and show **This plugin is required by your organization**; you can't remove them.

For how administrators provision plugins, see [Manage plugins for your organization](/docs/plugins/admin).

## Update and remove plugins

Cowork checks for plugin updates from the marketplace they came from. If you've edited a plugin's files locally, Cowork detects the change and warns you before an update would overwrite it.

To remove a plugin you installed, open it under **Customize > Plugins** and select **Remove**. You can't remove a plugin marked **This plugin is required by your organization**.

## Next steps

* [Plugins](/docs/plugins/overview): how plugins work across Claude products
* [Manage plugins for your organization](/docs/plugins/admin): administrator provisioning on Team and Enterprise plans
* [Submit a plugin](/docs/plugins/submit): publish your own to the marketplace
* [MCP, plugins, skills, and hooks](/docs/third-party/claude-desktop/extensions): for organizations that deploy Claude Desktop with their own model provider
