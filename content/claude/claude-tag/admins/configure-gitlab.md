> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure GitLab access

> Give Claude its own GitLab identity so it can read projects, manage issues, review merge requests, and check pipelines as a service account. Covers creating the account, scoping its access, generating a token, and adding it to a bundle.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting GitLab lets Claude read repository contents, manage issues, review and comment on merge requests, and check pipeline status from any channel under a bundle's scope, all through the GitLab API. Unlike GitHub, there is no Claude app to install in GitLab. Instead, you give Claude its own GitLab user and add that user's personal access token to an Access bundle.

A dedicated service account keeps Claude's GitLab activity attributed to a single identity you control. You decide which groups and projects it can reach by granting that account membership the same way you would for a person, and you can revoke or rescope it at any time without touching anyone else's access.

## Prerequisites

* The **Owner** role in your Claude organization to create an Access bundle.
* Permission in GitLab to create a user (or a [service account](https://docs.gitlab.com/user/profile/service_accounts/) on tiers that offer it) and to add that user to the groups or projects Claude should reach.
* An [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle) to hold the credential. Create one first if you haven't already.

## Create a dedicated GitLab account for Claude

Create a GitLab user that exists only for Claude, for example `claude@yourcompany.example.com`. On GitLab Premium or Ultimate, a [service account](https://docs.gitlab.com/user/profile/service_accounts/) is the cleanest fit because it is clearly non-human. On other tiers, a regular user works the same way; treat it as a bot seat.

Set the account's display name and avatar to whatever you want teammates to see on Claude's comments and issue activity.

## Grant the account access to your groups and projects

Add the service account as a member of each GitLab group or project Claude should work in. Granting at the group level is usually simpler than adding it to projects one at a time, and it means new projects in that group are reachable without another grant.

The role you grant determines which API calls succeed. Grant the lowest role that covers what you want Claude to do: reading code and browsing issues and merge requests needs less than creating issues, posting review comments, or acting on pipelines. See GitLab's [permissions reference](https://docs.gitlab.com/user/permissions/) for what each role allows.

## Generate a personal access token

Create a [personal access token](https://docs.gitlab.com/user/profile/personal_access_tokens/) for the account. For a GitLab.com service account, create the token from the group's service account settings or through the API; for a regular bot user, sign in as it and create the token from its profile. The token starts with `glpat-`.

| Scope      | When to grant it                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------------------ |
| `api`      | Read and write. Required for Claude to create and update issues, post comments, and act on pipelines.   |
| `read_api` | Read-only. Use this instead of `api` if you want Claude to browse and answer questions but never write. |

Set an expiry that matches your rotation policy, and store the token somewhere you can retrieve it once; GitLab shows it only at creation.

<Note>Group access tokens and project access tokens also work in the same field. The service-account approach is recommended because one token covers every group you add the account to, and the identity on comments and issues is yours to name. A group or project token is scoped to that single group or project and appears under a GitLab-generated bot name.</Note>

## Add the token to an Access bundle

<Steps>
  <Step title="Open the bundle's Credentials tab">
    At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles**, click into the bundle, and go to **Credentials**.
  </Step>

  <Step title="Connect GitLab">
    Click **Connect** next to **GitLab** and paste the token into **Personal access token**.
  </Step>

  <Step title="Attach the GitLab plugin">
    If your organization's plugin marketplace includes a GitLab plugin, add it on the bundle's **Plugins** tab so Claude knows how to call the GitLab API. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). The connection works without the plugin, which adds ready-made workflows.
  </Step>
</Steps>

The token is held by [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) and injected on every API request to your GitLab host. The model and the session sandbox never see it.

## Self-managed GitLab

Self-managed GitLab instances are supported when reachable from the public internet. In the **Connect GitLab** form, open the **Advanced** tab and add your instance's hostname under **Allowed websites**; `gitlab.com` is preset for GitLab SaaS. An instance on a private network without a public address can't be connected.

## Verify GitLab access

* GitLab is listed under the bundle's **Credentials** tab.
* In a channel under the bundle's scope, `@Claude what can you access from this channel?` returns GitLab.
* In that same channel, ask Claude to list the open issues in one of your GitLab projects. Claude returns them without prompting for credentials.

## Related resources

* [Connect GitLab](/docs/claude-tag/admins/connections/gitlab): the credential field reference and how GitLab differs from GitHub
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential and bundle reference
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): the GitHub App path, which is different
