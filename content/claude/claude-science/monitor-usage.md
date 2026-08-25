> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor Claude Science usage

> Claude Science usage counts against each member's standard weekly quota and uses the same seat as the rest of claude.ai.

Claude Science usage counts against each member's standard weekly quota and uses the same seat as the rest of claude.ai. You can track adoption in Analytics and through the Admin API.

## Analytics

Open Analytics from the user menu and select the Claude Science tab to see adoption and session metrics for this product. To see spend, or to compare active members across products, select Claude Science in the product filter on the Overview tab.

The Monitor usage link in Organization settings > Claude Science opens Analytics.

## Admin API

The Claude Enterprise Admin API (Enterprise plans only) returns Claude Science usage alongside your other products.

Per-member metrics (GET /v1/organizations/analytics/users, science\_metrics object):

| Field                       | Description                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| distinct\_session\_count    | Number of distinct Claude Science sessions. Null on aggregated rows where a distinct count can't be computed. |
| message\_count              | Number of messages sent in Claude Science sessions.                                                           |
| delegation\_count           | Number of delegations (handoffs to a specialized agent) in Claude Science sessions.                           |
| remote\_compute\_job\_count | Number of remote compute jobs launched from Claude Science sessions.                                          |
| skills\_used\_count         | Total number of skill invocations in Claude Science sessions.                                                 |

See the Admin API reference for authentication and the full schema.
