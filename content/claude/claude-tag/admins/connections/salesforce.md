> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Salesforce

> Connect Salesforce to Claude Tag so it can read and update CRM records. Covers the connected app to create, the client credential fields, and the host to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Salesforce lets Claude read accounts, contacts, opportunities, and cases (and write, if you grant it) from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person. The connection uses the OAuth 2.0 client credentials flow.

## Create the credential in Salesforce

Create a connected app (or External Client App) with the client credentials flow enabled, and set a dedicated integration user as the app's run-as user. Salesforce's guide is [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_client_credentials_flow.htm\&type=5).

You'll need from Salesforce:

* The app's **Consumer Key** (the client ID), from its **Settings** tab
* The app's **Consumer Secret** (the client secret)
* Your org's My Domain host (for example `yourcompany.my.salesforce.com`)

Assign the integration user a Permission Set scoped to the objects and fields Claude should reach. Read-only is the recommended starting point.

## Add the connection to a bundle

In the bundle, click **Connect** next to **Salesforce**.

| Field             | Value                                                                                    |
| :---------------- | :--------------------------------------------------------------------------------------- |
| Client ID         | The app's Consumer Key                                                                   |
| Client secret     | The app's Consumer Secret                                                                |
| Token URL         | Your org's token endpoint, `https://yourcompany.my.salesforce.com/services/oauth2/token` |
| Scopes (optional) | Leave empty unless your app requires specific scopes                                     |
| Allowed websites  | Your org's host, for example `yourcompany.my.salesforce.com`                             |

The preset prefills Allowed websites with an example host that cannot resolve. Replace it with your org's host before saving, or every request fails. To change the host later, open the **⋮** menu on this connection in the bundle's Credentials tab and choose **Edit**.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude list the five most recently modified Opportunities in Salesforce.
```

Check the integration user's login history in Salesforce Setup to confirm the call landed under that user.

## Related resources

* [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state): what this connection adds
