> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect GitLab

> Connect GitLab to Claude Tag so it can read code, manage issues, comment on merge requests, and check pipelines through the GitLab API. Covers token permissions, self-managed hostnames, and how it differs from GitHub.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting GitLab lets Claude read and search projects, manage issues, comment on merge requests, and check pipeline status, all through the GitLab REST API. The connector holds a single access token.

<Tip>This page is the credential field reference. The full setup walkthrough, including creating a dedicated GitLab service account for Claude and scoping its group access, is at [Configure GitLab access](/docs/claude-tag/admins/configure-gitlab).</Tip>

If your plugin marketplace includes a GitLab plugin, pair it with this connector so Claude knows how to call the API. Add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The connector works without it.

## Add the connector

<Steps>
  <Step title="Create the token in GitLab">
    A personal access token from a [dedicated service account](/docs/claude-tag/admins/configure-gitlab#create-a-dedicated-gitlab-account-for-claude) is recommended, so one identity covers every group you add it to. Project and group access tokens also work if you only need a single project or group. Grant the `api` scope for read and write, or `read_api` for read-only. The token starts with `glpat-`.
  </Step>

  <Step title="Add the connector">
    Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, select **GitLab**, and paste the token. For self-managed GitLab, switch to the form's **Advanced** tab and add your instance's hostname under **Allowed websites**. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.
  </Step>
</Steps>

**You'll see:** GitLab on the **Connectors** tab, and `@Claude what can you access from this channel?` returns it in a new thread in any channel where the connector is on. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

| Field | Value |
| :- | :- |
| Claude’s personal access token | The token from GitLab, starting with `glpat-`. Project and group access tokens work here too. |
| Allowed websites | `gitlab.com` (preset) |

GitLab's own guide for creating tokens is at [docs.gitlab.com](https://docs.gitlab.com/api/rest/authentication/).

## How GitLab differs from GitHub

| | GitLab | GitHub |
| :- | :- | :- |
| Auth | A service account's personal access token | The Claude GitHub App, [installed separately](/docs/claude-tag/admins/configure-github) |
| Referencing a project in a thread | Give Claude the full project URL; it reads it through the API | Typing `owner/repo` in the message auto-attaches it |
| Self-managed | Your hostname under **Advanced > Allowed websites** | [GitHub Enterprise setup](/docs/claude-tag/admins/configure-github#github-enterprise) |
| Handing back changes | Manages issues and comments on merge requests through the API | [Draft pull requests](/docs/claude-tag/users/use-cases/work-with-github) authored by the Claude GitHub App |

The connector is API-only. The token authenticates GitLab API requests, not git, so Claude gets a 401 error when it tries to clone a private project or push to any project over HTTPS, even with the connector in place. To clone a repository into the session workspace, connect it through [GitHub](/docs/claude-tag/admins/configure-github) instead.

The token is auto-injected on every API request to your GitLab host. The model and the sandbox are not given the key; see [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Related resources

* [Configure GitHub access](/docs/claude-tag/admins/configure-github): the GitHub App path, which is different
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
