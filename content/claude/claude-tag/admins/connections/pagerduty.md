> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect PagerDuty

> Connect PagerDuty to Claude Tag so it can read incidents and on-call schedules. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting PagerDuty lets Claude read incidents and on-call schedules during incident work in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the PagerDuty plugin from Anthropic's plugin marketplace so Claude knows how to call the API. This connector calls PagerDuty's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in PagerDuty

Generate a general-access read-only API key. A read-write key lets Claude acknowledge and resolve incidents. If you use one, [turn the connector on only in a private incident channel](/docs/claude-tag/admins/add-connections#add-a-connection).

Creating a general-access key requires the PagerDuty Admin or Account Owner role; non-admins only see User Token keys, which also work but inherit that user's permissions.

PagerDuty's own guide for creating the credential is at [support.pagerduty.com](https://support.pagerduty.com/main/docs/api-access-keys#generate-a-general-access-rest-api-key).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **PagerDuty**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's API key | The api key from PagerDuty |
| Allowed websites | `api.pagerduty.com` (preset) |

PagerDuty accounts on the EU service region use `api.eu.pagerduty.com` instead.

If the connect form offers to include the PagerDuty plugin, leave that box selected; otherwise add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

PagerDuty appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
