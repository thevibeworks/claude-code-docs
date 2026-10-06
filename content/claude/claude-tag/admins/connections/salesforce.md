> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Salesforce

> Connect Salesforce to Claude Tag so it can read and update CRM records. Covers the connected app to create, the client credential fields, and the host to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Salesforce lets Claude read accounts, contacts, opportunities, and cases (and write, if you grant it) in any channel where the connector is on. Claude connects with its own credential, not a person's. The connector uses the OAuth 2.0 client credentials flow.

## Create the credential in Salesforce

Create a connected app (or External Client App) with the client credentials flow enabled, and set a dedicated integration user as the app's run-as user. Salesforce's guide is [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_client_credentials_flow.htm\&type=5).

You'll need from Salesforce:

* The app's **Consumer Key** (the client ID), from its **Settings** tab
* The app's **Consumer Secret** (the client secret)
* Your org's My Domain host (for example `yourcompany.my.salesforce.com`)

Assign the integration user a Permission Set scoped to the objects and fields Claude should reach. Read-only is the recommended starting point.

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Salesforce**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Client ID | The app's Consumer Key |
| Client secret | The app's Consumer Secret |
| Token URL | Your org's token endpoint, `https://yourcompany.my.salesforce.com/services/oauth2/token` |
| Scopes (optional) | On the **Advanced** tab. Leave empty unless your app requires specific scopes |
| Allowed websites | Your org's host, for example `yourcompany.my.salesforce.com` |

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. The **Allowed websites** field shows an example host that can't resolve. Enter your org's host there, then click **Connect** to save the connector.

To change the host later, go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Salesforce**, open the menu on the credential's row in the **Access from** table, and click **Edit**. In the **Edit connection** dialog, the **Allowed websites** setting is labeled **Allowed hosts**. Change the host there and click **Save**.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude list the five most recently modified Opportunities in Salesforce.
```

Check the integration user's login history in Salesforce Setup to confirm the call landed under that user.

## Related resources

* [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state): what this connection adds
