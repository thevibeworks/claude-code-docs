> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Snowflake

> Connect Snowflake to Claude Tag so it can run read-only queries on your warehouse. Covers the dedicated user to create, the access token field, and the host to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Snowflake lets Claude run queries against your warehouse in any channel where the connector is on. Claude connects with its own credential, not a person's.

This connector calls Snowflake's HTTP API, and it's separate from members' personal claude.ai connectors.

## Create the credential in Snowflake

Create a dedicated Snowflake user for the agent with a read-only role scoped to the databases and schemas Claude should query. In Snowsight (Snowflake's web interface), under **Governance & security** and then **Users & roles**, generate a programmatic access token for that user. Tokens expire after 15 days by default, so plan to rotate the credential.

Snowflake's guide for programmatic access tokens is at [docs.snowflake.com](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens). The connector authenticates with this token; key-pair authentication isn't supported.

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Snowflake**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Claude's programmatic access token | The programmatic access token from Snowflake |
| Allowed websites | Your account's host, for example `yourorg-youraccount.snowflakecomputing.com` |

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. The **Allowed websites** field shows `*.snowflakecomputing.com` only as a hint, and a wildcard under `snowflakecomputing.com` can't be saved. Enter your account's host there, then click **Connect** to save the connector.

To change the host later, go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Snowflake**, open the menu on the credential's row in the **Access from** table, and click **Edit**. In the **Edit connection** dialog, the **Allowed websites** setting is labeled **Allowed hosts**. Change the host there and click **Save**.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Snowflake appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/answer-data-questions): warehouse questions answered with charts in the thread
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
