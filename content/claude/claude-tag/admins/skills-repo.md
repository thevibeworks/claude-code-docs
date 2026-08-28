> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up a skills repository Claude can update

> Put your org's Claude Tag skills in a git repository with auto-sync, grant Claude write access, and Claude can open pull requests to improve its own skills from what it learns in channels.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

A **skill** is a set of instructions that teaches Claude how to use a specific tool or follow a specific process (for example, which Datadog endpoints answer which questions, or your org's incident-response runbook). Claude Tag uses the same [skills format as Claude Code](https://code.claude.com/docs/en/skills). A **plugin** bundles one or more skills together.

You can upload skills one at a time in the console, but putting them in a git repository means Claude can open pull requests to improve them from what it learns working in your channels. You review the PR; once merged, every channel picks up the update.

## Set up the skills repository

<Steps>
  <Step title="Create the repository">
    A private or internal GitHub repository, laid out as a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces): a `.claude-plugin/marketplace.json` file at the root that lists each plugin, and one folder per plugin. Each plugin bundles one or more skills. A public repository can't be selected in the next step; fork it into a private one first.
  </Step>

  <Step title="Register the repository as a plugin marketplace">
    For a github.com repository, the GitHub connector must be enabled for your organization. On the **Plugins** page at [`claude.ai/admin-settings/plugins`](https://claude.ai/admin-settings/plugins), click **Add plugins** and choose **Sync from GitHub**. Select the repository, leave **Sync automatically** on (the default), and click **Create**.

    When you click **Create**, and on every sync after that, the whole repository is downloaded as one archive, and the archive can't be larger than 512 MiB. A repository over that size, such as a large monorepo, is rejected with `Download too large (>536.9MB)` even when the plugins in it are small. Put the plugins in a smaller dedicated repository, or [upload the plugin as a zip file](#upload-a-plugin-as-a-zip-file) instead.
  </Step>

  <Step title="Grant Claude write access to the repository">
    Open an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle), go to its **Repositories** tab, and add the repository. The Claude GitHub App must already be linked to your GitHub organization; see [Configure GitHub access](/docs/claude-tag/admins/configure-github).
  </Step>

  <Step title="Attach the plugins to a scope">
    In the same bundle's **Plugins** tab, toggle on the plugins from your new marketplace; each is off until you enable it. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).
  </Step>
</Steps>

**You'll see:** the repository appears in the bundle's Repositories list, and the marketplace's plugins appear in the bundle's Plugins tab, each labeled with the marketplace name.

## How updates propagate

Once the repository is set up, Claude can propose changes and they reach channels automatically after you merge:

| Stage                     | What happens                                                                                                                         |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| Claude works in a channel | Using the skills currently attached to that scope                                                                                    |
| Claude proposes an update | Opens a pull request against the skills repository, under the Claude GitHub App identity, linked back to the thread that prompted it |
| You review and merge      | The PR is yours to approve, edit, or close, like any contributor's                                                                   |
| The marketplace syncs     | On push to the default branch, the updated plugin syncs to your organization automatically                                           |
| New threads pick it up    | The next thread in any covered channel uses the updated skill                                                                        |

Every skill change reaches channels only after a human approves the merge; Claude opens the PR, you merge it.

## Prompt Claude to propose updates

Claude won't open skill PRs unprompted. Ask in the channel when something it learned should stick:

```text wrap theme={null}
@Claude that worked. Open a PR to the skills repo so the Datadog skill includes that query pattern.
```

Or set a routine that sweeps a channel's corrections into proposed updates:

```text wrap theme={null}
@Claude every Friday, review what you got wrong in this channel this week and open one PR to the skills repo with the fixes.
```

## Why a repository instead of uploading skills

You can also upload individual skills in the console without a repository. The repository pattern is worth the setup because Claude can propose changes to it, every change goes through version control and code review, and you can attach the same skills to multiple bundles without uploading them again.

## Upload a plugin as a zip file

To upload instead, on the **Plugins** page at [`claude.ai/admin-settings/plugins`](https://claude.ai/admin-settings/plugins), click **Add plugins**, choose **Upload a file**, and upload a `.zip` or `.plugin` archive of up to 200 MB. The archive has to be a [Claude Code plugin](https://code.claude.com/docs/en/plugins), laid out in one of these ways:

* A `.claude-plugin/plugin.json` manifest at the archive root, with each skill in its own folder at `skills/<name>/SKILL.md`
* The same layout inside a single top-level folder
* For a single skill, a `SKILL.md` at the top level whose frontmatter declares the plugin's components

An archive with no manifest, with more than one `plugin.json`, or with the manifest anywhere else is rejected at upload. After upload, the plugin is in your organization's catalog but not attached anywhere. To make it available in channels, toggle it on in a bundle's **Plugins** tab or add it directly on a scope; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

## Repository context files and MCP servers

A granted repository's `CLAUDE.md` and `.claude/rules/*.md` load when Claude clones it, in the same format as Claude Code; see [What loads from a repository](/docs/claude-tag/admins/configure-github#what-loads-from-a-repository) and the [Claude Code memory docs](https://code.claude.com/docs/en/memory). A repository's `.mcp.json` is not loaded. To give Claude an MCP server, put the `.mcp.json` in a plugin, next to its `.claude-plugin/plugin.json`, and attach the plugin; the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) cover the `.mcp.json` format, and [Add a custom MCP server](/docs/claude-tag/admins/connections/custom#add-a-custom-mcp-server) covers the credential the server needs.

## What belongs in the repository

| Put in the skills repo                                        | Put in channel memory instead          |
| :------------------------------------------------------------ | :------------------------------------- |
| How to call a specific API correctly                          | This channel's preferred output format |
| A runbook that any team would reuse                           | A one-off decision this channel made   |
| Tool-specific gotchas (auth headers, pagination, rate limits) | Who owns what in this team             |

Skills in the repository reach every channel under the scope.

## Related resources

* [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins): how plugins and skills load into a scope
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): granting Claude write access to a repository
* [What Claude Tag remembers](/docs/claude-tag/users/memory): when channel memory is the right place instead
