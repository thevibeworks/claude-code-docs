> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure GitHub access

> Give Claude its own GitHub identity through the Claude GitHub App. Covers linking your GitHub organization, granting repositories, and GitHub Actions.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Tip>Using GitLab instead of GitHub? See [Configure GitLab access](/docs/claude-tag/admins/configure-gitlab). GitLab uses a service-account token rather than an installed app.</Tip>

Claude Tag gives Claude its own GitHub identity, the Claude GitHub App, so pull requests it opens from a channel or a DM are authored by Claude rather than by a person. You only need GitHub access if a team will hand Claude code work: branches, pull requests, review, or CI follow-up.

You link GitHub once for your Claude organization, then choose which repositories Claude can use in each workspace and channel.

## Link your GitHub organization

<Note>
  The person who completes the link must be both an **owner of the GitHub organization** and an **Owner in your Claude organization**. If you aren't a GitHub organization owner, click the **Not the GitHub owner? Send instructions** link in the **GitHub** section of [**Organization settings > Git providers**](https://claude.ai/admin-settings/source-control). In the dialog that opens, click **Copy message** to copy a request you can send to someone who is.
</Note>

<Steps>
  <Step title="Open the Git providers page">
    Go to **Organization settings > Git providers** at [`claude.ai/admin-settings/source-control`](https://claude.ai/admin-settings/source-control). This page is shared with Claude Code; one connection serves both products. Until the Claude GitHub App is installed, you can also reach this page from Claude Tag admin settings. On the **Connectors** tab under **Claude's access**, click **Add** and select **GitHub**.
  </Step>

  <Step title="Connect GitHub">
    Beside the **GitHub** heading, click **Connect** (the button reads **Add organization** once a GitHub account is connected) and complete the GitHub authorization. After authorizing, the table in the **GitHub** section lists the GitHub accounts the Claude GitHub App is installed on. The **Type** column reads **Organization** or **Personal**. In the **Status** column, an account already linked to your Claude organization shows **Connected**, and one that still needs linking shows **Not linked**.
  </Step>

  <Step title="Link or install">
    If your organization's row reads **Not linked**, select the **Link** button next to it. If it isn't listed at all, click **Add organization** beside the **GitHub** heading and complete the install on github.com; you're returned to this page with the organization's row showing **Connected**.

    An organization can also be missing from the table because single sign-on (SSO) on GitHub hides it. A note under the table counts the organizations hidden that way. To make them appear, authorize the Claude app for those organizations on GitHub.

    * A disabled **Link** button means you can't link that account yet; the button's tooltip names the reason, such as not being an owner of that GitHub organization
    * A **Needs permissions** status means the installation has a pending request; **Review permissions** takes you to github.com to approve it
    * An **Authorize SSO** button in place of **Link** means your GitHub token isn't authorized for that organization's SSO; the button opens github.com to authorize it, and you link after returning
  </Step>
</Steps>

## Grant repository access

The remaining steps are in Claude Tag admin settings, not GitHub's settings. Granting repositories requires the **Owner** role or the [**Claude Tag Admin** permission](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) in your Claude organization. A [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can also add repositories to their own channel, limited to repositories their GitHub account is an admin of.

The GitHub page, a bundle's page, and a workspace's or channel's own page each offer the repositories the Claude GitHub App's installations reach, so you can grant a repository that no bundle holds yet. Pick repositories for each place on the GitHub page, or put them in a bundle to give a group of places the same set.

### Pick repositories for a workspace or channel

<Steps>
  <Step title="Open the GitHub page">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Connectors** tab and open **GitHub**.
  </Step>

  <Step title="Find the place">
    Under **Assign access**, find the row for where Claude should use the repositories: **Slack** for every workspace and channel, or a workspace or channel. If the place isn't listed, click **Add place**, choose it under **Where**, and click **Add**.
  </Step>

  <Step title="Pick the repositories">
    In the place's **Access** column, click **Select access**, or the repositories already picked there, and select each repository Claude should use. Selecting **Every repository in** an account also covers repositories created in it later, and asks you to confirm with **Connect all**. To attach a bundle that holds repositories instead, select it under **Bundles** in the same picker.
  </Step>

  <Step title="Save the changes">
    Click **Save changes**.
  </Step>
</Steps>

To add a repository from a workspace's or channel's own page instead, open the page from the **Channels** tab, and under **Claude's access**, click **Add**, select **Repository**, pick the repository on the **Repositories** tab, and click **Add**.

### Grant repositories through a bundle

A [bundle](/docs/claude-tag/admins/add-connections#create-a-bundle)'s places decide which channels can use the repositories in it.

<Steps>
  <Step title="Open a bundle">
    Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag). Under **Claude's access**, select the **Bundles** tab and open the bundle, or click **Add** to create one.
  </Step>

  <Step title="Add repositories">
    Under **What's in it**, click **Add** and choose **Repository**. In the dialog that opens, pick the **GitHub account** when more than one is linked, then search for a repository and select it. To grant every repository in the account's GitHub App installation, including ones added later, select the **Every repository in** option for that account. Click **Add**, and for the **Every repository in** option, confirm with **Connect all**. Before any GitHub account is linked, the dialog reads "Connect a GitHub account to your organization first."
  </Step>

  <Step title="Choose where the bundle applies">
    Under **Where it applies**, turn on the switch in the **Slack** row to apply the bundle in every workspace and channel, or in a workspace's row to apply it in that workspace. For a channel, click **Add place**, choose the channel under **Where**, and click **Add**. Then click **Save changes**.
  </Step>
</Steps>

## Verify GitHub access

* The GitHub organization shows as **Connected** in the **GitHub** section at [`claude.ai/admin-settings/source-control`](https://claude.ai/admin-settings/source-control).
* On the **Connectors** tab under **Claude's access**, select **GitHub**. Its page shows how many GitHub accounts the Claude GitHub App is installed on. Its **Access from** table lists each repository picked for a place and each repository a bundle holds. The **Set by** column reads **Here** for a repository picked for a place, or names the bundle that holds it, and **Used at** names where each one applies.
* For the end-to-end check, open a draft PR from a test channel; see [Verify the bundle is live](/docs/claude-tag/admins/attach-to-scope#verify-the-bundle-is-live).

### If Claude can't reach a repository

When Claude replies "That environment or repo isn't configured for Claude Code", or reports that GitHub returned a 403, check the two levels in order.

| Check | Where |
| :- | :- |
| The GitHub organization that owns the repository shows **Connected** in the **GitHub** section | [`claude.ai/admin-settings/source-control`](https://claude.ai/admin-settings/source-control). An installation still waiting on a GitHub organization owner shows **Needs permissions**; **Review permissions** opens the approval on github.com. |
| The repository reaches the channel | In [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag), open the channel's page from the **Channels** tab under **Claude's access**, and look for the repository in its **Claude's access** table. A repository granted in a bundle that doesn't apply to the channel isn't reachable there. |

After granting a repository, start a fresh thread in the channel and name the repository in the first message.

A `403` that names a GitHub Actions operation, such as "repository\_dispatch is not permitted for this session type.", is a different error. It says nothing about repository access; see [What Claude can do with GitHub Actions](#what-claude-can-do-with-github-actions).

## How granted repositories reach a session

Granting a repository in a bundle makes it *available* to Claude in any channel where that bundle applies. It doesn't clone the code into a session on its own. A session starts with no repositories checked out; Claude clones one when the request names it, or when someone in the thread tells it which repository to add. Tell your team to name the repository in the first message of a code task.

### What loads from a repository

When Claude clones a granted repository into a session, its Claude Code configuration loads on the next turn after the clone completes, so project context arrives without further prompting:

* `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` load as project context
* Skills in `.claude/skills/` load, so Claude can use them in the session

[Hooks](https://code.claude.com/docs/en/hooks) in a repository's `.claude/settings.json` don't run in the session. A repository's `.mcp.json` is never loaded.

Repository skills apply only in sessions that have the repository. To give a skill to every channel under a scope, add it through a [skills repository](/docs/claude-tag/admins/skills-repo).

### Install project dependencies

Every session runs in an isolated sandbox with a standard set of preinstalled tools. There are two places to add what a project needs beyond that set, such as a specific language runtime or a database client:

* **For every session in a channel**, an admin adds the install commands to the setup script of the environment the channel's sessions run on. See [Configure the environment for a scope](/docs/claude-tag/admins/customize#configure-the-environment-for-a-scope).
* **For one repository**, add the install commands to the repository's `CLAUDE.md`.

Claude follows `CLAUDE.md` as guidance when it starts work that needs it, not as an unconditional setup step. Write each install as a precondition of the work it supports, for example "install the SDK before building or running tests", so Claude runs it when a task touches that code. The sandbox is fresh for every session, so the installs repeat each time Claude works in the repository.

Prefer the standard package manager and its default registry over a vendor install script or a third-party package source. Package managers such as `apt`, `pip`, `npm`, and `dotnet` reach their default registries from the sandbox; downloads from other hosts can be blocked at the sandbox's [egress boundary](/docs/claude-tag/concepts/security-and-data#network-egress). An Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) can allow an additional host with a domain entry on a bundle; see [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential).

## What Claude can do with GitHub Actions

In a channel, Claude acts on GitHub as the Claude GitHub App, and that identity carries a fixed set of GitHub Actions permissions. No admin setting changes it, and adding `api.github.com` as a [custom connector](/docs/claude-tag/admins/connections/custom) with your own token doesn't change it either; Claude's GitHub requests always act as the Claude GitHub App.

Claude can:

* Read workflow runs, jobs, logs, and artifacts, so it follows a pull request's CI and reports the result
* Re-run a workflow run or its failed jobs, cancel a run in progress, and dispatch a `workflow_dispatch` workflow
* Delete runs, logs, or artifacts, and enable or disable a workflow
* Trigger `push` and `pull_request` workflows by pushing a branch or opening a pull request, the same way any other author does
* Edit files under `.github/workflows/` and open a pull request with the change, like any other file

Claude can't:

* Send a `repository_dispatch` event
* Approve a workflow run that's waiting on approval, or its pending deployments

A request for either is refused with a `403`; a `repository_dispatch` request returns "repository\_dispatch is not permitted for this session type." Approving a held run or a pending deployment releases a checkpoint GitHub inserted for a person, so do it from the repository's **Actions** tab on github.com.

## Require a second approval on Claude's pull requests

Claude is the author of the pull requests it opens, from a channel or a DM, so GitHub's rule against approving your own pull request applies to Claude and not to the person who asked for the change. On a branch that requires one approving review, the person who asked Claude for a change can approve and merge it alone. If you want a second person to look at Claude's work before it merges, require the second review in GitHub.

GitHub gives you two ways, both set in a branch protection rule or ruleset on each branch Claude opens pull requests against.

* **Require two approving reviews.** GitHub's built-in setting. It applies to pull requests from people too.
* **Require a status check that only Claude's pull requests must pass.** A check you build and maintain, for example a GitHub Actions workflow that fails on pull requests authored by `claude[bot]` (or by your own app's `<slug>[bot]` login on [GitHub Enterprise Server](#github-enterprise-server)) until two people have approved, and passes on pull requests people open.

With either, also turn on dismissing stale approvals when new commits are pushed, so an approval doesn't carry over to a later push. See [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [About status checks](https://docs.github.com/en/pull-requests/reference/status-checks) in GitHub's documentation.

## Scheduled work uses the same connection

Scheduled jobs use the same GitHub connection as interactive work, with nothing extra to configure. A recurring job that can't reach its repository skips that run and retries on its next schedule; after three consecutive failed runs spanning at least an hour, it disables itself. A one-time job that can't reach its repository is disabled on the first failure; the routine's page shows why.

## GitHub Enterprise

### GitHub Enterprise Cloud with data residency

Organizations on `*.ghe.com` (Enterprise Cloud with Data Residency) are registered the same way as a GitHub Enterprise Server host below.

### GitHub Enterprise Server

GitHub Enterprise Server instances are supported when reachable from the public internet. A GHES host on a private network without a public address can't be connected.

On GHES, you create the GitHub App on your own instance instead of installing Anthropic's. The setup is shared with Claude Code; follow the [Claude Code GitHub Enterprise Server guide](https://code.claude.com/docs/en/github-enterprise-server) to create and register the app. After you register the GHE host, the dialog for adding a repository to a bundle shows a **GitHub instance** picker; select your host there to grant its repositories.

Registering a GHE host with your Claude organization isn't fully self-serve. Raise it with your account team if the guide doesn't get you all the way through.

#### GitHub Enterprise Server in direct messages

In a [one-to-one direct message](/docs/claude-tag/concepts/agent-identity#direct-message-channels), Claude reaches repositories on a registered host through the sender's own GitHub Enterprise account instead of the bundle's grants. Claude adds a repository to a DM session only when both of these are true:

* The sender's GitHub Enterprise account has push access to the repository
* Your GitHub App's installation on the instance includes the repository

If the sender hasn't connected their GitHub Enterprise account on claude.ai yet, Claude replies with a link to connect it. After connecting, the sender asks Claude to add the repository again.

In channels, Claude uses the repositories granted through bundles, as it does for github.com. A person's own GitHub Enterprise connection doesn't apply in channels.

## Related resources

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): add the bundle to the workspaces and channels that need it
* [Set up routines](/docs/claude-tag/users/proactivity): the scheduled jobs that use this connection
