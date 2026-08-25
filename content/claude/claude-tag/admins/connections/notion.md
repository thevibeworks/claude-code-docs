> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Notion

> Connect Notion to Claude Tag so it can read and search your Notion workspace. Covers the dedicated account to create, the token fields, and the URL to allow.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Notion lets Claude ground answers in your Notion workspace from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

Pair this connection with the Notion plugin from Anthropic's plugin marketplace so Claude knows how to call the API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). This is an HTTP API connection, not an MCP server or a personal claude.ai connector.

## Create the credential in Notion

Create an internal integration in Notion and share the specific pages or databases Claude should read with that integration. Nothing is reachable until shared.

Notion's own guide for creating the credential is at [developers.notion.com](https://developers.notion.com/docs/create-a-notion-integration).

## Add the connection to a bundle

In the bundle, click **Connect** next to **Notion**.

| Field                       | Value                                       |
| :-------------------------- | :------------------------------------------ |
| Claude's integration secret | The internal integration secret from Notion |
| Allowed websites            | `api.notion.com`                            |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Notion appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/find-answers): the knowledge and docs use cases
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
