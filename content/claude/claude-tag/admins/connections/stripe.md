> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Stripe

> Connect Stripe to Claude Tag so it can answer billing and subscription questions. Covers the dedicated account to create, the key fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Stripe lets Claude answer billing and subscription questions from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

Pair this connection with the Stripe plugin from Anthropic's plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

## Create the credential in Stripe

Use a restricted key with read-only resource permissions, not your account's full secret key. Consider connecting test mode first.

Stripe's own guide for creating the credential is at [docs.stripe.com](https://docs.stripe.com/keys).

## Add the connection to a bundle

In the bundle, click **Connect** next to **Stripe**.

| Field               | Value                                                                         |
| :------------------ | :---------------------------------------------------------------------------- |
| Claude's secret key | The secret key from Stripe                                                    |
| Allowed websites    | `api.stripe.com` (preset). To add a different host, use the **Advanced** tab. |

The field labeled Claude's secret key accepts a restricted key; the label is the field name, not a key-type constraint.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Stripe appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
