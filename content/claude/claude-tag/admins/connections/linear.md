> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Linear

> Connect Linear to Claude Tag so it can file tickets and post status updates. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Linear lets Claude file tickets and post status updates from a thread in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the Linear plugin from Anthropic's plugin marketplace so Claude knows how to call the API. This connector calls Linear's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in Linear

Create a personal API key from a dedicated Linear seat for Claude, not your own account, so its activity shows under that seat in Linear's audit log.

Scope the key to specific Linear teams when you create it; the only place to limit which projects Claude can write to is in Linear itself. The key starts with `lin_api_`.

Linear's own guide for creating the credential is at [linear.app](https://linear.app/developers/graphql#personal-api-keys).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Linear**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's API key | The API key from Linear |
| Allowed websites | `api.linear.app` (preset) |

If the connect form offers to include the Linear plugin, leave that box selected; otherwise add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Linear appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/create-artifacts): the issue tracking use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
