> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Amplitude

> Connect Amplitude to Claude Tag with a project API key and secret key, or by signing in with Amplitude, so Claude can answer product-analytics questions.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting Amplitude lets Claude answer product-analytics questions, such as funnel and retention numbers, event segmentation, a user's recent activity, and cohort sizes, from any channel under the bundle's scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.

You can connect with a project API key and secret key, which you can limit to read requests, or by signing in as an Amplitude user, which gives Claude Amplitude's MCP tools for creating and editing content as well as reading it.

For the API key route, pair the connection with a plugin that covers Amplitude so Claude knows how to call the REST API; see [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins). A member's own Amplitude connector on claude.ai is separate from this connection and applies in DMs. Claude can also [use that connector in a channel](/docs/claude-tag/concepts/personal-connectors) for that member's own tasks, after the member allows it.

## Choose an API key or Amplitude sign-in

On a bundle's **Credentials** tab, clicking **Connect** next to **Amplitude** opens a form that offers two ways to connect: **Sign in with Amplitude**, selected by default, and **Use an API token** below it.

| Route                                              | What Claude can do                                                                                                                                                                                                                     | Amplitude data center | What you need                                                    |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- | :--------------------------------------------------------------- |
| **API key and secret key** (**Use an API token**)  | Run analytics queries, such as event segmentation, funnels, and retention, through Amplitude's [Dashboard REST API](https://amplitude.com/docs/apis/analytics/dashboard-rest). The setup steps restrict the key pair to read requests. | US or EU              | A project API key and a secret key generated for this connection |
| **Amplitude sign-in** (**Sign in with Amplitude**) | Work with charts, dashboards, cohorts, and experiments through Amplitude's MCP tools, which can create and edit content as well as read it. Claude acts in Amplitude with the signed-in user's roles and project access.               | US                    | A dedicated Amplitude user to sign in as                         |

Use the API key route when Claude should be limited to read requests. Also use the API key route when Amplitude hosts your organization's data in its EU data center (you sign in to Amplitude at `app.eu.amplitude.com` rather than `app.amplitude.com`), because the **Sign in with Amplitude** option connects to the MCP server for Amplitude's US data center, `https://mcp.amplitude.com/mcp`. Choose Amplitude sign-in when Claude should also build or change content in Amplitude, such as creating a chart or updating a dashboard.

With either route, Claude can use the connection in every channel under the bundle's scope. The form calls the sign-in option an MCP connector because Claude reaches Amplitude through Amplitude's hosted MCP server, and the result is still a connection in the bundle, not a personal claude.ai connector.

## Get the API key and secret key from Amplitude

The API key route uses two keys from one Amplitude project: the project's API key and a secret key. The connection sends them with HTTP Basic authentication, the API key as the username and the secret key as the password. Keys belong to a single project, so each connection reaches one project's data, and an organization with several Amplitude projects needs a key pair and a connection for each.

You need the Manager or Admin role in Amplitude to generate keys. Generate a secret key dedicated to this connection and give it a name that identifies Claude, so you can rotate or revoke it without affecting the keys your other tools use. Amplitude shows the secret key's value only once and can't display it again, so copy it as soon as it appears; if you lose it, generate a new secret key.

An Amplitude key pair has no read-only option, and the same pair can also call Amplitude's write and user-deletion endpoints. In the next section you restrict the connection to `GET` requests, so the key pair authenticates read requests only. Read access still covers everything those APIs return for the project, including raw event export and individual users' event streams, so scope the bundle to channels whose members may see that data.

Amplitude's own guide for creating the keys is at [amplitude.com](https://amplitude.com/docs/admin/account-management/manage-your-api-keys-and-secret-keys).

## Add the connection with an API key

A saved connection is live with every HTTP method in any channel under the bundle's scope. Add the connection to a bundle that isn't attached to a scope yet, and attach the bundle after you finish the restriction step below.

<Steps>
  <Step title="Open the Amplitude form">
    On the bundle's **Credentials** tab, click **Connect** next to **Amplitude**.
  </Step>

  <Step title="Enter the key pair">
    Select **Use an API token**, then fill in the two fields.

    | Field               | Value                                            |
    | :------------------ | :----------------------------------------------- |
    | Claude's API key    | The project's API key from Amplitude             |
    | Claude's secret key | The secret key you generated for this connection |

    The host is prefilled as `amplitude.com`. If Amplitude hosts your organization's data in its EU data center (you sign in to Amplitude at `app.eu.amplitude.com` rather than `app.amplitude.com`), replace the host with `analytics.eu.amplitude.com`.

    Click **Connect** to save the connection.
  </Step>

  <Step title="Restrict the connection to read requests">
    The connection is created with the `/api/` path prefix, which covers Amplitude's REST APIs and keeps the key pair off the rest of `amplitude.com`. Add the method restriction yourself: select **Edit** on the connection's row, then in the **Edit connection** dialog clear **All methods** under **Methods** and select `GET`. See [Restrict by path or method](/docs/claude-tag/admins/add-connections#restrict-by-path-or-method).

    With the restriction in place, the Agent Proxy attaches the key pair only to `GET` requests under `/api/`. A request outside that restriction, such as a write or a user-deletion call, doesn't match the connection. Agent Proxy never attaches the key pair to it, so the request can't authenticate to Amplitude.
  </Step>
</Steps>

Amplitude rate-limits these APIs per project, with a cap on concurrent requests and an hourly budget in which queries that span more days or segments cost more. Claude's queries draw on the same budget as your project's other API clients. If Claude reports that Amplitude returned a rate-limit error (HTTP 429), narrow the date range, drop a group-by, or ask again later. Amplitude's [Dashboard REST API documentation](https://amplitude.com/docs/apis/analytics/dashboard-rest) lists the current limits.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Add the connection with Amplitude sign-in

<Warning>Sign in as a dedicated Amplitude user created for this connection (for example, `claude@yourcompany.example.com`), not with your own account. Anyone in a channel under the bundle's scope can ask Claude to use the connection, so everything that user can reach in Amplitude is available to every member of those channels. Because Amplitude's MCP tools can create and edit charts, dashboards, and cohorts as well as read them, give the user the most limited role that covers what the channels need in each project, such as Viewer. A dedicated user also limits Claude to the projects you add that user to and keeps Claude's activity in Amplitude traceable to one account.</Warning>

This route connects to the MCP server for Amplitude's US data center. If you sign in to Amplitude at `app.eu.amplitude.com`, Amplitude hosts your organization's data in its EU data center, so use the [API key route](#add-the-connection-with-an-api-key) instead.

<Steps>
  <Step title="Open the Amplitude form">
    On the bundle's **Credentials** tab, click **Connect** next to **Amplitude**.
  </Step>

  <Step title="Sign in as the dedicated user">
    Leave **Sign in with Amplitude** selected. The **Sign in with Amplitude** option shows the MCP server the sign-in grants access to, `https://mcp.amplitude.com/mcp`, and the form sets the connection's allowed host to that server for you.

    Click **Sign in with Amplitude** at the bottom of the form. A sign-in window opens. If your browser blocks pop-ups, allow them for claude.ai and click **Sign in with Amplitude** again. Sign in to Amplitude as the dedicated user and approve access. When the sign-in completes and the window closes, the connection is saved to the bundle and appears on its **Credentials** tab.
  </Step>
</Steps>

Amplitude decides what the signed-in user can read and change, and that user's roles and project access apply to every request Claude makes through this connection. The `GET` restriction described for the API key route applies only to that route's key pair. If the sign-in succeeds but Claude reports that Amplitude denied a request, check the dedicated user's role and project access in Amplitude. See [Amplitude MCP](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) for what Amplitude's MCP server can do.

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude can you reach Amplitude? List a few of our event types.
```

With either route, Claude replies with event types from Amplitude once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use Amplitude by name.

## Related resources

* [Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions): the question-to-chart pattern in a Slack thread, shown there with a data warehouse
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
* [Connect a custom service](/docs/claude-tag/admins/connections/custom): for Amplitude APIs the preset doesn't cover, such as the User Profile API, which lives on `profile-api.amplitude.com` and authenticates with a different header
* Amplitude's [API authentication](https://amplitude.com/docs/apis/authentication), [API key and secret key management](https://amplitude.com/docs/admin/account-management/manage-your-api-keys-and-secret-keys), and [Amplitude MCP](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) documentation
