> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure GitHub access

> Claude Tag gives Claude its own GitHub identity, so it opens pull requests as Claude. See how to link your GitHub organization, grant repositories to a bundle, what loads when a repository is cloned into a session, how to get project dependencies installed, and what Claude can do with GitHub Actions.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<div className="tm-stepbar">
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/pair-workspace">1 · Pair workspace</a>
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/add-connections">2 · Give access</a>
  <a className="tm-stepbar-seg tm-current" href="/docs/docs/claude-tag/admins/configure-github">3 · Connect GitHub</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/set-spend-limit">4 · Spend limit</a>
  <a className="tm-stepbar-seg" href="/docs/docs/claude-tag/admins/test-it">5 · See it work</a>
</div>

<Tip>Using GitLab instead of GitHub? See [Configure GitLab access](/docs/claude-tag/admins/configure-gitlab). GitLab uses a service-account token rather than an installed app.</Tip>

Claude Tag gives Claude its own GitHub identity, the Claude GitHub App, so pull requests it opens from a channel are authored by Claude rather than by a person. You only need GitHub access if a team will hand Claude code work: branches, pull requests, review, or CI follow-up.

You link GitHub once for your Claude organization, then grant repositories per Access bundle.

<Tip>If you link your GitHub organization before running [setup](/docs/claude-tag/admins/setup-overview), setup includes a step for granting repository access inline, so you don't need to return to the Repositories tab afterward.</Tip>

## Link your GitHub organization

<Note>
  The person who completes the link must be both an **owner of the GitHub organization** and an **Owner in your Claude organization**. If you aren't a GitHub organization owner, use **Copy message** under **Not a GitHub account owner?** on the GitHub settings page to send the link to someone who is.
</Note>

<Steps>
  <Step title="Open the GitHub settings page">
    Open [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github). This page is shared with Claude Code; one connection serves both products.
  </Step>

  <Step title="Connect Claude to GitHub">
    Click **Connect Claude to GitHub** and complete the GitHub authorization. After authorizing, the page shows two sections: **Connected GitHub accounts** lists organizations already linked, and **Unlinked accounts** lists organizations where the Claude GitHub App is installed but not yet linked.
  </Step>

  <Step title="Link or install">
    If your organization is under **Unlinked accounts**, click **Link** next to it. If it isn't listed at all, click **Install on another organization** and complete the install on github.com; you're returned to this page with the organization under **Connected GitHub accounts** as **Connected**.

    * A disabled **Link** button means you aren't an owner of that GitHub organization
    * A **Needs permissions** status means the installation has a pending request; **Review permissions** takes you to github.com to approve it
  </Step>
</Steps>

## Grant repository access

The remaining steps are in the Claude Tag admin page, not GitHub's settings. Repository grants live on the Access bundle; editing a bundle's Repositories tab requires the **Owner** role in your Claude organization. A [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can also add repositories to their own channel, limited to repositories their GitHub account can write to.

<Steps>
  <Step title="Open the bundle's Repositories tab">
    Open an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle) and go to its **Repositories** tab. Before any GitHub organization is linked, this tab shows a **Get started with GitHub** button that opens [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github).
  </Step>

  <Step title="Select repositories">
    Choose the repositories Claude can read from and open pull requests against. Access is per listed repository, or choose **Connect all** for the organization.
  </Step>
</Steps>

## Verify GitHub access

* The GitHub organization shows as **Connected** under **Connected GitHub accounts** at [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github).
* The granted repositories are listed in the bundle's **Repositories** tab.
* For the end-to-end check, open a draft PR from a test channel; see [Verify the bundle is live](/docs/claude-tag/admins/attach-to-scope#verify-the-bundle-is-live).

### If Claude can't reach a repository

When Claude replies "That environment or repo isn't configured for Claude Code", or reports that GitHub returned a 403, check the two levels in order.

| Check                                                                                                             | Where                                                                                                                                                                                                                                  |
| :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The GitHub organization that owns the repository shows **Connected** under **Connected GitHub accounts**          | [`claude.ai/admin-settings/github`](https://claude.ai/admin-settings/github). An installation still waiting on a GitHub organization owner shows **Needs permissions**; **Review permissions** opens the approval on github.com.       |
| The repository is listed on the bundle's **Repositories** tab, and that bundle is attached to the channel's scope | [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Access bundles** → the bundle → **Repositories**. A repository granted in one bundle isn't reachable from a channel under a different bundle. |

Repository grants apply to new threads. After changing the **Repositories** tab, start a fresh thread in the channel and name the repository in the first message.

A `403` that names a GitHub Actions operation, such as "repository\_dispatch is not permitted for this session type.", is a different error. It says nothing about repository access; see [What Claude can do with GitHub Actions](#what-claude-can-do-with-github-actions).

## How granted repositories reach a session

Granting a repository in a bundle makes it *available* to Claude in any channel under that bundle's scope. It doesn't clone the code into a session on its own. A session starts with no repositories checked out; Claude clones one when the request names it, or when someone in the thread tells it which repository to add. Tell your team to name the repository in the first message of a code task.

### What loads from a repository

When Claude clones a granted repository into a session, its Claude Code configuration loads on the next turn after the clone completes, so project context arrives without further prompting:

* `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` load as project context
* Skills in `.claude/skills/` load, so Claude can use them in the session
* The project settings in `.claude/settings.json` load, so hooks defined there run in the session as they do under Claude Code

A repository's `.mcp.json` is never loaded, and connections come only from the Access bundle.

Repository skills apply only in sessions that have the repository. To give a skill to every channel under a scope, add it through a [skills repository](/docs/claude-tag/admins/skills-repo).

### Install project dependencies

Every session runs in an isolated sandbox with a standard set of preinstalled tools. The sandbox is the same for every repository; there is no setup script or custom image to configure. If a project needs something the standard set doesn't include, such as a specific language runtime or a database client, add the install commands to the repository's `CLAUDE.md`.

Claude follows `CLAUDE.md` as guidance when it starts work that needs it, not as an unconditional setup step. Write each install as a precondition of the work it supports, for example "install the SDK before building or running tests", so Claude runs it when a task touches that code. The sandbox is fresh for every session, so the installs repeat each time Claude works in the repository.

Prefer the standard package manager and its default registry over a vendor install script or a third-party package source. Package managers such as `apt`, `pip`, `npm`, and `dotnet` reach their default registries from the sandbox; downloads from other hosts can be blocked at the sandbox's [egress boundary](/docs/claude-tag/concepts/security-and-data#network-egress). An Owner can allow an additional host on the bundle's Domains tab; see [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential).

## What Claude can do with GitHub Actions

In a channel, Claude acts on GitHub as the Claude GitHub App, and that identity carries a fixed set of GitHub Actions permissions. No admin setting changes it, and adding `api.github.com` as a [custom connection](/docs/claude-tag/admins/connections/custom) with your own token doesn't change it either; Claude's GitHub requests always act as the Claude GitHub App.

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

## Scheduled work uses the same connection

Scheduled jobs use the same GitHub connection as interactive work, with nothing extra to configure. A recurring job that can't reach its repository skips that run and retries on its next schedule; after three consecutive failed runs spanning at least an hour, it disables itself. A one-time job that can't reach its repository is disabled on the first failure; the routine's page shows why.

## GitHub Enterprise

### GitHub Enterprise Cloud with data residency

Organizations on `*.ghe.com` (Enterprise Cloud with Data Residency) are registered the same way as a GitHub Enterprise Server host below.

### GitHub Enterprise Server

GitHub Enterprise Server instances are supported when reachable from the public internet. A GHES host on a private network without a public address can't be connected.

On GHES, you create the GitHub App on your own instance instead of installing Anthropic's. The setup is shared with Claude Code; follow the [Claude Code GitHub Enterprise Server guide](https://code.claude.com/docs/en/github-enterprise-server) to create and register the app. After registering the GHE host, a host picker appears on the bundle's **Repositories** tab; select your host there to grant its repositories.

Registering a GHE host with your Claude organization isn't fully self-serve. Raise it with your account team if the guide doesn't get you all the way through.

## Related resources

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): bind the bundle to the workspaces and channels that need it
* [Set up routines](/docs/claude-tag/users/proactivity): the scheduled jobs that use this connection
