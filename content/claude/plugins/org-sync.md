> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sync your organization's plugins from a repository

> Distribute your organization's plugins from a GitHub or GitLab repository through organization settings, including repository requirements and GitLab setup.

You can distribute your organization's own plugins by syncing a Git repository that holds them from [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory). Members then find those plugins under **Customize > Plugins** with the availability you set.

This page is for the Owner who adds the repository and for the engineer who maintains it. It covers the requirements the repository and its plugin entries must meet for the sync to accept them.

<Note>
  * If you're choosing who gets each plugin once the repository syncs, see [Manage plugins for your organization](/docs/plugins/admin#set-availability)
  * If you're writing the `marketplace.json` file, see [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) in the Claude Code docs
</Note>

To get started, check [how organization sync gets access to your repository](#give-organization-sync-access-to-your-repository) for your Git host, then check your `marketplace.json` against [the plugin sources that organization sync accepts](#plugin-sources-that-organization-sync-accepts).

## Give organization sync access to your repository

Members don't need access to the repository themselves, and their Git credentials aren't involved. Organization sync reads the marketplace repository's default branch through your organization's GitHub or GitLab connection on claude.ai, whichever matches the repository's host:

* **github.com**: the Claude GitHub App, which you install during [Sync a marketplace from github.com](#sync-a-marketplace-from-github-com)
* **Your GitHub Enterprise Server host**: your organization's [GitHub Enterprise App](https://code.claude.com/docs/en/github-enterprise-server#admin-setup)
* **gitlab.com or your self-managed GitLab instance**: the access token in your organization's [GitLab configuration](#sync-a-gitlab-hosted-marketplace) for that host

### Sync a marketplace from github.com

When you sync a marketplace from github.com, organization sync reads the repository through the Claude GitHub App, and you choose the availability its plugins start with as you add it. To sync a marketplace from a private or internal repository on github.com:

<Steps>
  <Step title="Open Plugins & skills">
    Go to [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory).
  </Step>

  <Step title="Select Sync from GitHub">
    Select **Add**, then **Sync from GitHub**.
  </Step>

  <Step title="Connect to GitHub">
    If the dialog shows **Connect to GitHub**, select it and authorize. GitHub returns you to the dialog.
  </Step>

  <Step title="Choose the repository">
    Search for the repository or enter it as `owner/repo`. The list shows private and internal repositories.
  </Step>

  <Step title="Install the Claude GitHub App if needed">
    If the repository isn't in the list, select **Install the Claude GitHub App** under **Repository missing?**, grant the app access to the repository on GitHub, and return to the dialog.
  </Step>

  <Step title="Leave automatic sync on">
    Leave **Sync automatically** on to sync each time someone pushes to the default branch. Claude creates the webhook on the repository for you.
  </Step>

  <Step title="Choose the default access">
    Choose the **Default access** for the plugins in this marketplace.
  </Step>

  <Step title="Create the marketplace">
    Select **Create**.
  </Step>
</Steps>

The marketplace's page opens, and **Last synced** shows **Syncing...** until the first sync finishes. If the dialog says **The Claude GitHub App is not installed on** the repository, grant the Claude GitHub App access to the repository on GitHub and try again.

To turn on automatic sync later, open the marketplace from the [**Marketplaces**](https://claude.ai/admin-settings/skills?tab=marketplaces) tab and turn on **Sync automatically**. If it shows **No webhook yet**, select **Configure webhook**, then **Enable webhook**.

### Sync a GitLab-hosted marketplace

Syncing a marketplace from GitLab needs a GitLab configuration for the host first, which holds the access token that organization sync reads the repository with. To sync a marketplace from gitlab.com or a self-managed GitLab instance:

<Steps>
  <Step title="Add a GitLab configuration">
    As an [Owner](https://code.claude.com/docs/en/server-managed-settings#access-control), add a GitLab configuration for that host at [**Organization settings > Claude Code**](https://claude.ai/admin-settings/claude-code). GitLab configurations are in public beta and apply only to plugin marketplace sync.
  </Step>

  <Step title="Sync from GitLab">
    In [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory), select **Add**, then **Sync from GitLab**, as [Add your own plugins](/docs/plugins/admin#add-your-own-plugins) describes. When you add it, enter the project's HTTPS URL, such as `https://gitlab.example.com/platform/claude-plugins`.
  </Step>
</Steps>

Organization sync reads the project's default branch. If you turn on **Sync automatically**, only pushes to the default branch start a sync.

## Plugin sources that organization sync accepts

The repository you sync is a [plugin marketplace](https://code.claude.com/docs/en/plugins/create-marketplace): it has a `.claude-plugin/marketplace.json` file that lists your plugins and the location of each one. On a Team or Enterprise plan, organization sync applies these rules to the marketplace repository and to each plugin source the marketplace lists:

* **Marketplace repository**: on github.com and gitlab.com, the marketplace repository must be private or internal
* **Plugin source types**: each plugin source must be of type `github`, `url`, or `git-subdir`, or a [relative path](https://code.claude.com/docs/en/plugins/marketplace-reference#relative-path-plugin-source) that starts with `./`. If you list a plugin by bare name under `metadata.pluginRoot`, organization sync rejects it as an unsupported source. Write the path out instead, such as `./plugins/deploy-tools`
* **Private plugin sources**: a plugin source can be private when it's one of the following:
  * A github.com source that shares the marketplace repository's owner
  * A source on your organization's GitHub Enterprise host with the GitHub Enterprise App installed on the repository
  * A `url` or `git-subdir` source on the same GitLab host as the marketplace repository. On gitlab.com, the source must also be under the same top-level group or user namespace as the marketplace repository
* **Public plugin sources**: any other plugin source must be a public repository on github.com, gitlab.com, or bitbucket.org, which organization sync fetches without credentials. Organization sync rejects plugin sources on hosts these rules don't cover

To include private plugins, place the plugin folders inside the marketplace repository and reference them with a relative path. Organization sync packages each plugin during distribution, so members never need access to a separate source repository. For example, this `marketplace.json` plugin entry references a plugin you committed at `plugins/deploy-tools` in the marketplace repository:

```json theme={null}
{
  "name": "deploy-tools",
  "source": "./plugins/deploy-tools"
}
```

### Keep executables out of the top-level bin directory

Don't include a top-level `bin/` directory in any plugin you distribute through organization settings. claude.ai rejects a plugin that has one, whether the plugin arrives by marketplace sync or by direct upload in [**Organization settings > Plugins & skills**](https://claude.ai/admin-settings/skills?tab=inventory). The error message starts with `Plugin contains a top-level bin/ directory`. On marketplace sync, organization sync rejects that plugin and syncs the rest of the marketplace.

Keep executables in another directory, such as `scripts/`, and reference them as `${CLAUDE_PLUGIN_ROOT}/scripts/<name>` from your [skills, hooks, or MCP server configs](https://code.claude.com/docs/en/plugins/manifest-reference#environment-variables).

## Next steps

* [Manage plugins for your organization](/docs/plugins/admin#set-availability): set each synced plugin to available, installed by default, or required
* [Roll out a plugin to your whole organization](/docs/plugins/org-rollout): reach members in claude.ai and Cowork and developers in the Claude Code command line with one plugin
* [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) in the Claude Code docs: write the `marketplace.json` file that lists your plugins
