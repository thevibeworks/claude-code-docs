> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Datadog

> Connect Datadog to Claude Tag so it can query metrics, logs, and monitors. Covers the dedicated account to create, the API key fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Datadog lets Claude query metrics, logs, and monitors during debugging in any channel where the connector is on. Claude connects with its own credential, not a person's.

Pair this connector with the Datadog plugin from Anthropic's plugin marketplace so Claude knows how to call the API. This connector calls Datadog's HTTP API. It isn't an MCP server or a member's personal claude.ai connector.

## Create the credential in Datadog

Create an API key under a service account in Datadog. Also create an Application key under the same service account. The Application key carries the read scopes, so restrict it to read-only roles. The form doesn't require the Application key, but reading metrics, monitors, and dashboards does.

Datadog's own guide for creating the credential is at [docs.datadoghq.com](https://docs.datadoghq.com/account_management/api-app-keys/).

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select the Datadog entry for your Datadog account's site. Datadog has a separate API host per site, and a key only works against its own.

| Entry | Site and API host |
| :- | :- |
| **Datadog** | US1, `api.datadoghq.com`, Datadog's default site |
| **Datadog (US3)** | US3, `api.us3.datadoghq.com` |
| **Datadog (US5)** | US5, `api.us5.datadoghq.com` |
| **Datadog (EU)** | EU, `api.datadoghq.eu` |
| **Datadog (AP1)** | AP1, `api.ap1.datadoghq.com` |
| **Datadog (AP2)** | AP2, `api.ap2.datadoghq.com` |
| **Datadog (US1-FED)** | US1-FED, `api.ddog-gov.com` |

Every entry asks for the same fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's API key | The API key from Datadog |
| Claude's application key | The Application key from Datadog. Optional in the form; add it so Claude can read metrics, monitors, and dashboards |
| Allowed websites | The entry's API host (preset) |

If the connect form offers to include the Datadog plugin, leave that box selected; otherwise add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

The connector is created with path prefixes that cover Datadog's read and query routes: metric, log, trace, and RUM queries, monitors, downtimes, dashboards, SLOs, notebooks, events, hosts, service definitions, and incident search. It doesn't cover Datadog's key, user, integration, or log-configuration management routes, so Claude can't call those through it. To narrow the connector further, for example to `GET` only, or to allow another route, go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click your Datadog connector, open the menu on the credential's row in the **Access from** table, and click **Edit**. See [Restrict by path or method](/docs/claude-tag/admins/add-connections#restrict-by-path-or-method).

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Datadog appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
