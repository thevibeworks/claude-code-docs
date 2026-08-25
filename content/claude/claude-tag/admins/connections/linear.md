> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Linear

> Connect Linear to Claude Tag so it can file tickets and post status updates. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Linear lets Claude file tickets and post status updates from a thread from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

Pair this connection with the Linear plugin from Anthropic's plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

## Create the credential in Linear

Create a personal API key from a dedicated Linear seat for Claude, not your own account, so its activity shows under that seat in Linear's audit log.

Scope the key to specific Linear teams when you create it; the only place to limit which projects Claude can write to is in Linear itself. The key starts with `lin_api_`.

Linear's own guide for creating the credential is at [linear.app](https://linear.app/developers/graphql#personal-api-keys).

## Add the connection to a bundle

In the bundle, click **Connect** next to **Linear**.

| Field            | Value                   |
| :--------------- | :---------------------- |
| Claude's API key | The API key from Linear |
| Allowed websites | `api.linear.app`        |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Linear appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/create-artifacts): the issue tracking use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
