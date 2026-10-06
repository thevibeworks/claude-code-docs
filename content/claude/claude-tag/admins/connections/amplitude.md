> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Amplitude

> Connect Amplitude to Claude Tag with a project API key and secret key, or by signing in with Amplitude, so Claude can answer product-analytics questions.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Amplitude lets Claude answer product-analytics questions, such as funnel and retention numbers, event segmentation, a user's recent activity, and cohort sizes, in any channel where the connector is on. Claude connects with its own credential, not a person's.

You can connect with a project API key and secret key, which you can limit to read requests, or by signing in as an Amplitude user, which gives Claude Amplitude's MCP tools for creating and editing content as well as reading it.

For the API key route, pair the connector with a plugin that covers Amplitude so Claude knows how to call the REST API. Add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab. A member's own Amplitude connector on claude.ai is separate from this connector and applies in one-to-one DMs. Claude can also [use that connector in a channel](/docs/claude-tag/concepts/personal-connectors) for that member's own tasks, after the member allows it.

## Choose an API key or Amplitude sign-in

When you select **Amplitude** in the **Add a connector** dialog, the dialog shows two routes under **How Claude authenticates**: **Paste an API key**, selected to start, and **Sign in to Amplitude as Claude**. Select a route and click **Continue to Amplitude** to open the connect form for that route.

| Route | What Claude can do | Amplitude data center | What you need |
| :- | :- | :- | :- |
| **API key and secret key** (**Paste an API key**) | Run analytics queries, such as event segmentation, funnels, and retention, through Amplitude's [Dashboard REST API](https://amplitude.com/docs/apis/analytics/dashboard-rest). The setup steps restrict the key pair to read requests. | US or EU | A project API key and a secret key generated for this connector |
| **Amplitude sign-in** (**Sign in to Amplitude as Claude**) | Work with charts, dashboards, cohorts, and experiments through Amplitude's MCP tools, which can create and edit content as well as read it. Claude acts in Amplitude with the signed-in user's roles and project access. | US | A dedicated Amplitude user to sign in as |

Use the API key route when Claude should be limited to read requests. Also use the API key route when Amplitude hosts your organization's data in its EU data center (you sign in to Amplitude at `app.eu.amplitude.com` rather than `app.amplitude.com`), because the **Sign in to Amplitude as Claude** option connects to the MCP server for Amplitude's US data center, `https://mcp.amplitude.com/mcp`. Choose Amplitude sign-in when Claude should also build or change content in Amplitude, such as creating a chart or updating a dashboard.

With either route, Claude can use the connector in every channel where it's on. The form says the sign-in option uses Amplitude's MCP connector because Claude reaches Amplitude through Amplitude's hosted MCP server. The result is still a connector Claude holds for your organization, not a personal claude.ai connector.

## Get the API key and secret key from Amplitude

The API key route uses two keys from one Amplitude project: the project's API key and a secret key. The connector sends them with HTTP Basic authentication, the API key as the username and the secret key as the password. Keys belong to a single project, so each credential reaches one project's data, and an organization with several Amplitude projects needs a key pair and a credential for each.

You need the Manager or Admin role in Amplitude to generate keys. Generate a secret key dedicated to this connector and give it a name that identifies Claude, so you can rotate or revoke it without affecting the keys your other tools use. Amplitude shows the secret key's value only once and can't display it again, so copy it as soon as it appears; if you lose it, generate a new secret key.

An Amplitude key pair has no read-only option, and the same pair can also call Amplitude's write and user-deletion endpoints. In the next section you restrict the credential to `GET` requests, so the key pair authenticates read requests only. Read access still covers everything those APIs return for the project, including raw event export and individual users' event streams, so turn the connector on only in channels whose members may see that data.

Amplitude's own guide for creating the keys is at [amplitude.com](https://amplitude.com/docs/admin/account-management/manage-your-api-keys-and-secret-keys).

## Add the connector with an API key

A saved credential works with every HTTP method wherever the connector is on, and the first Amplitude credential added on the **Connectors** tab is on in every workspace and channel as soon as you save it. To restrict the key pair before any channel can use it, add Amplitude to a new bundle, which applies nowhere until you add places to it.

<Steps>
  <Step title="Create a bundle for Amplitude">
    Go to [**Organization settings > Claude Tag > Bundles**](https://claude.ai/admin-settings/claude-tag?access=presets), click **Add**, enter a name such as `Amplitude`, and click **Create**. The bundle's page opens.
  </Step>

  <Step title="Open the Amplitude form">
    Under **What's in it**, click **Add**, select **Connector**, and select **Amplitude**. Leave **Paste an API key** selected and click **Continue to Amplitude**. The connect form opens.
  </Step>

  <Step title="Enter the key pair">
    With **Use an API token** selected, fill in these fields.

    | Field | Value |
    | :- | :- |
    | Claude's API key | The project's API key from Amplitude |
    | Claude's secret key | The secret key you generated for this connector |
    | Allowed websites | `amplitude.com` (preset) |

    If Amplitude hosts your organization's data in its EU data center (you sign in to Amplitude at `app.eu.amplitude.com` rather than `app.amplitude.com`), replace the host with `analytics.eu.amplitude.com`.

    Click **Connect** to save the connector.
  </Step>

  <Step title="Restrict the credential to read requests">
    The credential is created with the `/api/` path prefix, which covers Amplitude's REST APIs and keeps the key pair off the rest of `amplitude.com`. Add the method restriction yourself: under **What's in it**, open the menu on the Amplitude row and click **Edit**. In the **Edit connection** dialog, clear **All methods** under **Methods**, select `GET`, and click **Save**.

    With the restriction in place, the Agent Proxy attaches the key pair only to `GET` requests under `/api/`. A request outside that restriction, such as a write or a user-deletion call, doesn't match the credential. Agent Proxy never attaches the key pair to it, so the request can't authenticate to Amplitude.
  </Step>

  <Step title="Choose where the bundle applies">
    Under **Where it applies**, click **Add place**, choose a workspace or channel under **Where**, and click **Add**. The bundle applies there and in every channel beneath it. Click **Save changes** to save the places.
  </Step>
</Steps>

Amplitude rate-limits these APIs per project, with a cap on concurrent requests and an hourly budget in which queries that span more days or segments cost more. Claude's queries draw on the same budget as your project's other API clients. If Claude reports that Amplitude returned a rate-limit error (HTTP 429), narrow the date range, drop a group-by, or ask again later. Amplitude's [Dashboard REST API documentation](https://amplitude.com/docs/apis/analytics/dashboard-rest) lists the current limits.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Add the connector with Amplitude sign-in

<Warning>Sign in as a dedicated Amplitude user created for this connector (for example, `claude@yourcompany.example.com`), not with your own account. Anyone in a channel where the connector is on can ask Claude to use it, so everything that user can reach in Amplitude is available to every member of those channels. Because Amplitude's MCP tools can create and edit charts, dashboards, and cohorts as well as read them, give the user the most limited role that covers what the channels need in each project, such as Viewer. A dedicated user also limits Claude to the projects you add that user to and keeps Claude's activity in Amplitude traceable to one account.</Warning>

This route connects to the MCP server for Amplitude's US data center. If you sign in to Amplitude at `app.eu.amplitude.com`, Amplitude hosts your organization's data in its EU data center, so use the [API key route](#add-the-connector-with-an-api-key) instead.

<Steps>
  <Step title="Open the Amplitude form">
    Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Amplitude**. Select **Sign in to Amplitude as Claude** and click **Continue to Amplitude**. The connect form opens.
  </Step>

  <Step title="Sign in as the dedicated user">
    The **Sign in to Amplitude as Claude** option shows the MCP server the sign-in grants access to, `https://mcp.amplitude.com/mcp`, and the form sets the connector's allowed host to that server for you.

    The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you sign in.

    Click **Sign in with Amplitude** at the bottom of the form. A sign-in window opens. If your browser blocks pop-ups, allow them for claude.ai and click **Sign in with Amplitude** again. Sign in to Amplitude as the dedicated user and approve access. When the sign-in completes and the window closes, the connector is saved and Amplitude's connector page opens, with the new credential marked **New**.
  </Step>
</Steps>

Amplitude decides what the signed-in user can read and change, and that user's roles and project access apply to every request Claude makes through this connector. The `GET` restriction described for the API key route applies only to that route's key pair. If the sign-in succeeds but Claude reports that Amplitude denied a request, check the dedicated user's role and project access in Amplitude. See [Amplitude MCP](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) for what Amplitude's MCP server can do.

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude can you reach Amplitude? List a few of our event types.
```

With either route, Claude replies with event types from Amplitude once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use Amplitude by name.

## Related resources

* [Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions): the question-to-chart pattern in a Slack thread, shown there with a data warehouse
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
* [Connect a custom service](/docs/claude-tag/admins/connections/custom): for Amplitude APIs the **Amplitude** entry doesn't cover, such as the User Profile API, which lives on `profile-api.amplitude.com` and authenticates with a different header
* Amplitude's [API authentication](https://amplitude.com/docs/apis/authentication), [API key and secret key management](https://amplitude.com/docs/admin/account-management/manage-your-api-keys-and-secret-keys), and [Amplitude MCP](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) documentation
