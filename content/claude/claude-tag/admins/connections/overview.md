> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Per-service connection guides

> Step-by-step setup for each tool Claude Tag can connect to. Each guide covers the dedicated account to create, the credential to enter, and the URL to allow.

> [!NOTE]
>
> Claude Tag is in public beta. Features and behavior described here may change before general availability.

Each guide covers one service: how to create the credential as a dedicated identity, what to paste into the connect form, and the **Allowed websites** value. For the model behind connectors (credential types, Agent Proxy, allowed websites, bundles), see [Give Claude access](https://claude.com/docs/claude-tag/admins/add-connections.md).

> [!WARNING]
>
> Always connect a dedicated account for Claude (for example, `claude@yourcompany.example.com`), not your personal login. Anyone in a channel where the connector applies can use it through Claude, so whatever this account can reach is available to every member of those channels. See [Create a dedicated account per service](https://claude.com/docs/claude-tag/admins/add-connections.md#create-a-dedicated-account-per-service). Before you add a connector, see [where a new connector applies](https://claude.com/docs/claude-tag/admins/add-connections.md#where-a-new-connector-applies).

| Service | Category | Guide |
| :- | :- | :- |
| Datadog | Monitoring | [Connect Datadog](https://claude.com/docs/claude-tag/admins/connections/datadog.md) |
| Sentry | Monitoring | [Connect Sentry](https://claude.com/docs/claude-tag/admins/connections/sentry.md) |
| PagerDuty | Monitoring | [Connect PagerDuty](https://claude.com/docs/claude-tag/admins/connections/pagerduty.md) |
| Linear | Issue tracking | [Connect Linear](https://claude.com/docs/claude-tag/admins/connections/linear.md) |
| Asana | Issue tracking | [Connect Asana](https://claude.com/docs/claude-tag/admins/connections/asana.md) |
| Jira and Confluence | Issue tracking | [Connect Jira and Confluence](https://claude.com/docs/claude-tag/admins/connections/atlassian.md) |
| Notion | Knowledge and docs | [Connect Notion](https://claude.com/docs/claude-tag/admins/connections/notion.md) |
| Google (Drive, Calendar, Gmail) | Knowledge and docs | [Connect Google](https://claude.com/docs/claude-tag/admins/connections/google.md) |
| HubSpot | Go-to-market | [Connect HubSpot](https://claude.com/docs/claude-tag/admins/connections/hubspot.md) |
| Salesforce | Go-to-market | [Connect Salesforce](https://claude.com/docs/claude-tag/admins/connections/salesforce.md) |
| Gong | Go-to-market | [Connect Gong](https://claude.com/docs/claude-tag/admins/connections/gong.md) |
| GitLab | Code | [Connect GitLab](https://claude.com/docs/claude-tag/admins/connections/gitlab.md) |
| BigQuery (custom) | Data warehouse | [Connect BigQuery](https://claude.com/docs/claude-tag/admins/connections/bigquery.md) |
| Snowflake | Data warehouse | [Connect Snowflake](https://claude.com/docs/claude-tag/admins/connections/snowflake.md) |
| Amplitude | Product analytics | [Connect Amplitude](https://claude.com/docs/claude-tag/admins/connections/amplitude.md) |
| Stripe | Billing | [Connect Stripe](https://claude.com/docs/claude-tag/admins/connections/stripe.md) |
| Vercel | Deployments | [Connect Vercel](https://claude.com/docs/claude-tag/admins/connections/vercel.md) |

GitHub is managed through the Claude GitHub App rather than a credential; see [Configure GitHub access](https://claude.com/docs/claude-tag/admins/configure-github.md).

Services marked (custom) aren't in the **Add a connector** list. Add them with **Custom connector** following their guide.

## Connect a service that has no guide

You can add any app that has an API as a custom connector or a custom MCP server, including services this page has no guide for. See [Connect a custom service](https://claude.com/docs/claude-tag/admins/connections/custom.md) for the credential types and form fields.

## When a connector fails after setup

If Claude says it can't reach a service you connected, start with the checks at the top of [Troubleshoot Claude Tag setup](https://claude.com/docs/claude-tag/admins/troubleshooting.md). Open the channel's page from the **Channels** tab under **Claude's access** and confirm the connector is listed in its **Claude's access** table. Then rerun the test in a new thread.

Two entries on the troubleshooting page cover connector failures directly:

* [A connection works in one channel but not another](https://claude.com/docs/claude-tag/admins/troubleshooting.md#a-connection-works-in-one-channel-but-not-another): the connector, or the bundle that holds it, likely doesn't apply to the failing channel
* [I hit an authentication error and couldn't finish this turn](https://claude.com/docs/claude-tag/admins/troubleshooting.md#i-hit-an-authentication-error-and-couldn%E2%80%99t-finish-this-turn): Claude posts that message when its own request fails an authentication check. A connected service's failing credential surfaces as a tool error inside Claude's reply instead
