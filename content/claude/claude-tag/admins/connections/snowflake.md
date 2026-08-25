> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Snowflake

> Connect Snowflake to Claude Tag so it can run read-only queries on your warehouse. Covers the dedicated user to create, the access token field, and the host to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Snowflake lets Claude run queries against your warehouse from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

This is an HTTP API connection, not a personal claude.ai connector.

## Create the credential in Snowflake

Create a dedicated Snowflake user for the agent with a read-only role scoped to the databases and schemas Claude should query. In Snowsight (Snowflake's web interface), under **Governance & security** and then **Users & roles**, generate a programmatic access token for that user. Tokens expire after 15 days by default, so plan to rotate the credential.

Snowflake's guide for programmatic access tokens is at [docs.snowflake.com](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens). The connection authenticates with this token; key-pair authentication is not currently supported.

## Add the connection to a bundle

In the bundle, click **Connect** next to **Snowflake**.

| Field                              | Value                                                                         |
| :--------------------------------- | :---------------------------------------------------------------------------- |
| Claude's programmatic access token | The programmatic access token from Snowflake                                  |
| Allowed websites                   | Your account's host, for example `yourorg-youraccount.snowflakecomputing.com` |

The preset prefills Allowed websites with an example host that cannot resolve. Replace it with your account's host before saving, or every request fails. To change the host later, open the **⋮** menu on this connection in the bundle's Credentials tab and choose **Edit**.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Snowflake appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/answer-data-questions): warehouse questions answered with charts in the thread
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
