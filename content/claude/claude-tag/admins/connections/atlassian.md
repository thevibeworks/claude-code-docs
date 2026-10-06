> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Jira and Confluence

> Connect Atlassian Cloud to Claude Tag so it can read and update Jira issues and search Confluence pages.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Atlassian Cloud lets Claude read and search Confluence pages and read, comment on, and update Jira issues in any channel where the connector is on. One credential covers both products on the same Atlassian site.

This connector calls the Jira and Confluence HTTP APIs. It isn't an MCP server or a member's personal claude.ai connector. Pair it with plugins that cover Jira and Confluence so Claude knows how to call the API. Add them on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab.

## Create the credential in Atlassian

Create a dedicated Atlassian account for Claude (for example `claude@yourcompany.example.com`) and add it to the Jira projects and Confluence spaces it should reach. The connector can read whatever this account can read, so a dedicated account keeps Claude's reach to exactly what you grant it.

Sign in as that account and create an API token at [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens). Atlassian shows the token once; store it somewhere you can retrieve it. Atlassian API tokens expire, with a maximum lifetime of one year, so plan to create a new token and rotate the connector's credential before the old one lapses.

<Note>Create the API token without scopes. Atlassian accepts tokens with scopes, including service account tokens, only at its `api.atlassian.com` gateway, not at your site's hostname, so the **Jira & Confluence** entry can't use them.</Note>

If your organization requires tokens with scopes, see [Connect a token with scopes through the Atlassian gateway](#connect-a-token-with-scopes-through-the-atlassian-gateway).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Jira & Confluence**. Leave **Paste an API key** selected and click **Continue to Jira & Confluence**.

In the connect form, with **Use an API token** selected, enter the dedicated account's email address, the API token from Atlassian, and your own site's hostname, such as `your-domain.atlassian.net`. Claude sends the token only to that site. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

<Note>Atlassian Data Center (self-hosted) isn't covered by the **Jira & Confluence** entry because it authenticates with a personal access token sent as a Bearer header. Add a Data Center instance as a [custom connector](/docs/claude-tag/admins/connections/custom) with the **Bearer** credential type and your instance's hostname under **Allowed websites**. The instance must be reachable from the public internet.</Note>

## Connect a token with scopes through the Atlassian gateway

If your organization requires tokens with scopes, connect through the gateway instead of the **Jira & Confluence** entry. Add the gateway connector inside a new bundle. A new bundle applies nowhere until you add places to it, so you can limit the token to your site's paths before any channel can use it.

<Steps>
  <Step title="Create a bundle for the gateway">
    Go to [**Organization settings > Claude Tag > Bundles**](https://claude.ai/admin-settings/claude-tag?access=presets), click **Add**, enter a name such as `Atlassian gateway`, and click **Create**. The bundle's page opens.
  </Step>

  <Step title="Add the gateway connector">
    Under **What's in it**, click **Add**, select **Connector**, and select **Custom connector**. In the [custom connector](/docs/claude-tag/admins/connections/custom) form, enter a **Name**, choose the **Basic** credential type, enter the dedicated account's email as the **Username** and the API token as the **Password**, and enter `api.atlassian.com` under **Allowed websites**. Click **Connect** to save the connector.
  </Step>

  <Step title="Limit the credential to your site's paths">
    Under **What's in it**, open the menu on the new connector's row and click **Edit**. In the **Edit connection** dialog, add `/ex/jira/<cloud-id>/` and `/ex/confluence/<cloud-id>/` under **Path prefixes**, then click **Save**. The cloud ID in a gateway request's path chooses which Atlassian site the request reaches.
  </Step>

  <Step title="Choose where the bundle applies">
    Under **Where it applies**, click **Add place**, choose a workspace or channel under **Where**, and click **Add**. Click **Save changes** to save the places.
  </Step>
</Steps>

Atlassian documents [tokens with scopes](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/), [service account tokens](https://support.atlassian.com/user-management/docs/manage-api-tokens-for-service-accounts/), and [how to find your site's cloud ID](https://support.atlassian.com/jira/kb/retrieve-my-atlassian-sites-cloud-id/).

## Verify the connection

In a channel where the connector is on, in a new thread, ask Claude to fetch one issue or page by key or URL. The call lands under the dedicated account in Atlassian's audit log.

```text wrap theme={null}
@Claude can you read PROJ-123 from Jira?
```

New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [Custom connector](/docs/claude-tag/admins/connections/custom): for a setup the **Jira & Confluence** entry doesn't cover, such as a self-hosted Data Center instance
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full connection model and how to scope a dedicated account
