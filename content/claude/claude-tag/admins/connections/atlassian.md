> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Jira and Confluence

> Connect Atlassian Cloud to Claude Tag so it can read and update Jira issues and search Confluence pages.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Atlassian Cloud lets Claude read and search Confluence pages and read, comment on, and update Jira issues from any channel under the bundle's scope. One credential covers both products on the same Atlassian site.

This is an HTTP API connection, not an MCP server or a personal claude.ai connector. Pair it with a plugin that covers Jira and Confluence so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

## Create the credential in Atlassian

Create a dedicated Atlassian account for Claude (for example `claude@yourcompany.example.com`) and add it to the Jira projects and Confluence spaces it should reach. The connection can read whatever this account can read, so a dedicated account keeps Claude's reach to exactly what you grant it.

Sign in as that account and create an API token at [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens). Atlassian shows the token once; store it somewhere you can retrieve it. Atlassian API tokens expire, with a maximum lifetime of one year, so plan to create a new token and update the connection before the old one lapses.

<Note>Create the API token without scopes. Atlassian accepts tokens with scopes, including service account tokens, only at its `api.atlassian.com` gateway, not at your site's hostname, so the preset can't use them.</Note>

If your organization requires tokens with scopes, connect through the gateway instead of the preset. Add a [custom connection](/docs/claude-tag/admins/connections/custom) with the **Basic** credential type, the dedicated account's email and token, and `api.atlassian.com` under **Allowed websites**. Then [restrict the connection](/docs/claude-tag/admins/add-connections#restrict-by-path-or-method) to the path prefixes `/ex/jira/<cloud-id>/` and `/ex/confluence/<cloud-id>/`, because the cloud ID in a gateway request's path chooses which Atlassian site the request reaches. Atlassian documents [tokens with scopes](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/), [service account tokens](https://support.atlassian.com/user-management/docs/manage-api-tokens-for-service-accounts/), and [how to find your site's cloud ID](https://support.atlassian.com/jira/kb/retrieve-my-atlassian-sites-cloud-id/).

## Add the connection to a bundle

On the bundle's **Credentials** tab, click **Connect** next to **Jira & Confluence**.

The form asks for the dedicated account's email address and the API token from Atlassian. In the host field, replace the prefilled `*.atlassian.net` with your own site's hostname, such as `your-domain.atlassian.net`. The form rejects the wildcard because it would let the credential reach any Atlassian site, not just yours.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

<Note>Atlassian Data Center (self-hosted) isn't covered by the preset because it authenticates with a personal access token sent as a Bearer header. Add a Data Center instance as a [custom connection](/docs/claude-tag/admins/connections/custom) with the **Bearer** credential type and your instance's hostname under **Allowed websites**. The instance must be reachable from the public internet.</Note>

## Verify the connection

In a channel under the bundle's scope, in a new thread, ask Claude to fetch one issue or page by key or URL. The call lands under the dedicated account in Atlassian's audit log.

```text wrap theme={null}
@Claude can you read PROJ-123 from Jira?
```

New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [Custom connection](/docs/claude-tag/admins/connections/custom): for a setup the preset doesn't cover, such as a self-hosted Data Center instance
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connection model and how to scope a dedicated account
