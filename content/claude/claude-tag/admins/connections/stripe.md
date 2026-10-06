> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Stripe

> Connect Stripe to Claude Tag so it can answer billing and subscription questions. Covers the dedicated account to create, the key fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Stripe lets Claude answer billing and subscription questions in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the Stripe plugin from Anthropic's plugin marketplace so Claude knows how to call the API. Add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. This connector calls Stripe's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in Stripe

Use a restricted key with read-only resource permissions, not your account's full secret key. Consider connecting test mode first.

Stripe's own guide for creating the credential is at [docs.stripe.com](https://docs.stripe.com/keys).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Stripe**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's secret key | The secret key from Stripe |
| Allowed websites | `api.stripe.com` (preset) |

The field labeled Claude's secret key accepts a restricted key; the label is the field name, not a key-type constraint.

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Stripe appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
