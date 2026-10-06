> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Per-service connection guides

> Step-by-step setup for each tool Claude Tag can connect to. Each guide covers the dedicated account to create, the credential to enter, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Each guide covers one service: how to create the credential as a dedicated identity, what to paste into the connect form, and the **Allowed websites** value. For the model behind connectors (credential types, Agent Proxy, allowed websites, bundles), see [Give Claude access](/docs/claude-tag/admins/add-connections).

<Warning>Always connect a dedicated account for Claude (for example, `claude@yourcompany.example.com`), not your personal login. Anyone in a channel where the connector applies can use it through Claude, so whatever this account can reach is available to every member of those channels. See [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service). Before you add a connector, see [where a new connector applies](/docs/claude-tag/admins/add-connections#where-a-new-connector-applies).</Warning>

| Service | Category | Guide |
| :- | :- | :- |
| Datadog | Monitoring | [Connect Datadog](/docs/claude-tag/admins/connections/datadog) |
| Sentry | Monitoring | [Connect Sentry](/docs/claude-tag/admins/connections/sentry) |
| PagerDuty | Monitoring | [Connect PagerDuty](/docs/claude-tag/admins/connections/pagerduty) |
| Linear | Issue tracking | [Connect Linear](/docs/claude-tag/admins/connections/linear) |
| Asana | Issue tracking | [Connect Asana](/docs/claude-tag/admins/connections/asana) |
| Jira and Confluence | Issue tracking | [Connect Jira and Confluence](/docs/claude-tag/admins/connections/atlassian) |
| Notion | Knowledge and docs | [Connect Notion](/docs/claude-tag/admins/connections/notion) |
| Google (Drive, Calendar, Gmail) | Knowledge and docs | [Connect Google](/docs/claude-tag/admins/connections/google) |
| HubSpot | Go-to-market | [Connect HubSpot](/docs/claude-tag/admins/connections/hubspot) |
| Salesforce | Go-to-market | [Connect Salesforce](/docs/claude-tag/admins/connections/salesforce) |
| Gong | Go-to-market | [Connect Gong](/docs/claude-tag/admins/connections/gong) |
| GitLab | Code | [Connect GitLab](/docs/claude-tag/admins/connections/gitlab) |
| BigQuery (custom) | Data warehouse | [Connect BigQuery](/docs/claude-tag/admins/connections/bigquery) |
| Snowflake | Data warehouse | [Connect Snowflake](/docs/claude-tag/admins/connections/snowflake) |
| Amplitude | Product analytics | [Connect Amplitude](/docs/claude-tag/admins/connections/amplitude) |
| Stripe | Billing | [Connect Stripe](/docs/claude-tag/admins/connections/stripe) |
| Vercel | Deployments | [Connect Vercel](/docs/claude-tag/admins/connections/vercel) |

GitHub is managed through the Claude GitHub App rather than a credential; see [Configure GitHub access](/docs/claude-tag/admins/configure-github).

Services marked (custom) aren't in the **Add a connector** list. Add them with **Custom connector** following their guide.

## Connect a service that has no guide

You can add any app that has an API as a custom connector or a custom MCP server, including services this page has no guide for. See [Connect a custom service](/docs/claude-tag/admins/connections/custom) for the credential types and form fields.

## When a connector fails after setup

If Claude says it can't reach a service you connected, start with the checks at the top of [Troubleshoot Claude Tag setup](/docs/claude-tag/admins/troubleshooting). Open the channel's page from the **Channels** tab under **Claude's access** and confirm the connector is listed in its **Claude's access** table. Then rerun the test in a new thread.

Two entries on the troubleshooting page cover connector failures directly:

* [A connection works in one channel but not another](/docs/claude-tag/admins/troubleshooting#a-connection-works-in-one-channel-but-not-another): the connector, or the bundle that holds it, likely doesn't apply to the failing channel
* [I hit an authentication error and couldn't finish this turn](/docs/claude-tag/admins/troubleshooting#i-hit-an-authentication-error-and-couldn%E2%80%99t-finish-this-turn): Claude posts that message when its own request fails an authentication check. A connected service's failing credential surfaces as a tool error inside Claude's reply instead
