> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect HubSpot

> Connect HubSpot to Claude Tag so it can read pipeline, deal, and contact data. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting HubSpot lets Claude pull pipeline, deal, and contact state in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the HubSpot plugin from Anthropic's plugin marketplace so Claude knows how to call the API. This connector calls HubSpot's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in HubSpot

Create a private app and select the read scopes you need (typically `crm.objects.contacts.read`, `crm.objects.companies.read`, `crm.objects.deals.read`). The private app acts as its own identity in HubSpot's audit log.

HubSpot's own guide for creating the credential is at [developers.hubspot.com](https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **HubSpot**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's private app token | The private app token from HubSpot |
| Allowed websites | `api.hubapi.com` (preset) |

If the connect form offers to include the HubSpot plugin, leave that box selected; otherwise add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

HubSpot appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/pull-deal-state): the go-to-market use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
