> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Asana

> Connect Asana to Claude Tag so it can file tasks and read project status. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Asana lets Claude file tasks and pull project status in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the Asana plugin from Anthropic's plugin marketplace so Claude knows how to call the API. This connector calls Asana's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in Asana

On every Asana plan, create the personal access token from a dedicated Asana seat for Claude, and give that seat access to only the projects and teams Claude needs. Per Asana's guidance, avoid service account tokens, which carry organization-wide access.

Asana's own guide for creating the credential is at [developers.asana.com](https://developers.asana.com/docs/personal-access-token).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Asana**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's personal access token | The personal access token from Asana |
| Allowed websites | `app.asana.com` (preset) |

If the connect form offers to include the Asana plugin, leave that box selected; otherwise add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Asana appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/track-projects): the issue tracking use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
