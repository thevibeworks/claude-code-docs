> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Datadog

> Connect Datadog to Claude Tag so it can query metrics, logs, and monitors. Covers the dedicated account to create, the API key fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Datadog lets Claude query metrics, logs, and monitors during debugging from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

Pair this connection with the Datadog plugin from Anthropic's plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

## Create the credential in Datadog

Create an API key under a service account in Datadog. Also create an Application key under the same service account. The Application key carries the read scopes, so restrict it to read-only roles. The form doesn't require the Application key, but reading metrics, monitors, and dashboards does.

Datadog's own guide for creating the credential is at [docs.datadoghq.com](https://docs.datadoghq.com/account_management/api-app-keys/).

## Add the connection to a bundle

In the bundle, click **Connect** next to Datadog. The picker has three Datadog entries, one per site. Pick the one that matches your Datadog account's site.

| Picker entry      | Site                                        |
| :---------------- | :------------------------------------------ |
| **Datadog**       | US1 (`api.datadoghq.com`), the default site |
| **Datadog (US5)** | US5 (`api.us5.datadoghq.com`)               |
| **Datadog (EU)**  | EU (`api.datadoghq.eu`)                     |

The form asks for the same fields in all three.

| Field                    | Value                                                                                                               |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------ |
| Claude's API key         | The API key from Datadog                                                                                            |
| Claude's application key | The Application key from Datadog. Optional in the form; add it so Claude can read metrics, monitors, and dashboards |
| Allowed websites         | Prefilled by the preset; override for other sites (see below)                                                       |

Datadog has a separate API host per site, and a key only works against its own. If your account is on a site without a picker entry, pick any Datadog entry and override Allowed websites with your site's API host: `api.us3.datadoghq.com`, `api.ap1.datadoghq.com`, or `api.ddog-gov.com`. To change the host later, open the **⋮** menu on this connection in the bundle's Credentials tab and choose **Edit**.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Datadog appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/watch-monitors): the monitoring use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
