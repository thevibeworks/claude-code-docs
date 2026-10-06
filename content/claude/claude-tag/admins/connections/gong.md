> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Gong

> Connect Gong to Claude Tag so it can pull call summaries and deal context. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Gong lets Claude pull call summaries and deal context in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the Gong plugin from Anthropic's plugin marketplace so Claude knows how to call the API. Add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. This connector calls Gong's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in Gong

A Gong technical admin generates the access key and secret; the key is tied to the admin who created it, so use a dedicated admin account where possible.

The credential type is HTTP Basic; both the access key and the access key secret are required.

Gong's own guide for creating the credential is at [help.gong.io](https://help.gong.io/docs/receive-access-to-the-api).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Gong**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's access key | The access key from Gong |
| Claude's access key secret | The access key secret from Gong |
| Allowed websites | `api.gong.io` (preset) |

Gong assigns each company its own API base URL, like `us-46459.api.gong.io`. Copy yours from **Company Settings > Ecosystem > API** in Gong, then switch to the connect form's **Advanced** tab and enter it under **Allowed websites**.

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Gong appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/pull-deal-state): the go-to-market use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
