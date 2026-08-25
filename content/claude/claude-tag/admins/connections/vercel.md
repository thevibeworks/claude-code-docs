> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Vercel

> Connect Vercel to Claude Tag so it can check deployment status and logs. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Vercel lets Claude check deployment status and logs from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

Pair this connection with the Vercel plugin from Anthropic's plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

## Create the credential in Vercel

Create the token from a dedicated team member seat, scoped to the team rather than your personal account.

Vercel's own guide for creating the credential is at [vercel.com](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token).

## Add the connection to a bundle

In the bundle, click **Connect** next to **Vercel**.

| Field                 | Value                        |
| :-------------------- | :--------------------------- |
| Claude's access token | The access token from Vercel |
| Allowed websites      | `api.vercel.com`             |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Vercel appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
