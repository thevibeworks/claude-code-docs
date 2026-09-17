> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Google Cloud

> Give Claude access to BigQuery and Google's other remote MCP servers with an OAuth client from your own Google Cloud project, set up in the Enterprise Admin Console.

When Claude Desktop is deployed on third-party inference, Claude can work with your organization's BigQuery and other Google data through Google's remote MCP servers, for example the BigQuery server at `https://bigquery.googleapis.com/mcp`. The device talks to Google directly: users' Google tokens stay on the device, and no Google data passes through Anthropic's infrastructure.

## How the connection works

Google's remote MCP servers don't support dynamic client registration, and Google's token endpoint requires the client secret even for a client of the **Desktop app** type. You create one Desktop-app OAuth client in your Google Cloud project, enter its client ID and client secret in the server's entry, and each user signs in with their own Google account. Google doesn't treat a Desktop-app client secret as confidential, so the Enterprise Admin Console stores it with the entry, as described under [Where the client secret goes](/docs/third-party/claude-desktop/mcp-sign-in#where-the-client-secret-goes). That page also explains each **OAuth** field.

## Set up the BigQuery server

<Steps>
  <Step title="Prepare the Google Cloud project">
    In the Google Cloud project that holds your BigQuery data, enable the BigQuery MCP server and grant each user the **MCP Tool User** role (`roles/mcp.toolUser`) together with the BigQuery roles their queries need. Google's [Use the BigQuery MCP server](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp) guide covers both.
  </Step>

  <Step title="Create a Desktop-app OAuth client in Google Cloud">
    If the project has no OAuth consent screen, configure one first in the Google Cloud Console under **APIs & Services → OAuth consent screen**. Choose the **Internal** user type when all users are in your Google Workspace organization. With **External**, add every user as a test user while the app is in testing, or Google blocks their sign-in.

    Then open **APIs & Services → Credentials**, choose **Create credentials → OAuth client ID**, and select **Desktop app** as the application type. When Google shows the new client, copy its **Client ID** (ends in `.apps.googleusercontent.com`) and **Client secret** (begins with `GOCSPX-`). You don't add redirect URIs, because Desktop-app clients accept loopback redirects automatically.
  </Step>

  <Step title="Add the server in the Enterprise Admin Console">
    In the Enterprise Admin Console ([claude.ai](https://claude.ai) → **Organization settings**), open the **Connectors** page under **Desktop 3P**. Under **Managed MCP servers**, click **Add → Blank** and fill in the entry:

    | Field                    | Value                                 |
    | ------------------------ | ------------------------------------- |
    | **Name**                 | `BigQuery`                            |
    | **Transport**            | **Streamable HTTP**                   |
    | **URL**                  | `https://bigquery.googleapis.com/mcp` |
    | **OAuth**                | **Bring your own client**             |
    | **Client ID**            | The client ID from step 2             |
    | **Client secret**        | The client secret from step 2         |
    | **Authorization server** | `["https://accounts.google.com"]`     |

    <Frame caption="A BigQuery entry on the Connectors page with OAuth set to Bring your own client.">
      <img src="https://mintcdn.com/claude-ai/l0HgWAJ4dDJ1-I-u/images/third-party/admin-console-managed-mcp-oauth.png?fit=max&auto=format&n=l0HgWAJ4dDJ1-I-u&q=85&s=efa91a216efb8f99c1e4aefc0ed5b16a" alt="Managed MCP server entry named BigQuery in the Enterprise Admin Console, with Transport set to Streamable HTTP, the BigQuery MCP URL, OAuth set to Bring your own client, and the Client ID, Client secret, and Authorization server fields filled in." width="1952" height="1705" data-path="images/third-party/admin-console-managed-mcp-oauth.png" />
    </Frame>

    Click **Save changes**. Users' apps pick up the new entry as described under [Configuration updates](/docs/third-party/claude-desktop/admin-console#configuration-updates). Devices need outbound HTTPS access to `bigquery.googleapis.com`, `accounts.google.com`, and `oauth2.googleapis.com`.

    If you manage configuration through MDM or a bootstrap server instead, the equivalent [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) entry is:

    ```json theme={null}
    {
      "name": "BigQuery",
      "transport": "http",
      "url": "https://bigquery.googleapis.com/mcp",
      "oauth": {
        "clientId": "CLIENT_ID.apps.googleusercontent.com",
        "clientSecret": "GOCSPX-YOUR_CLIENT_SECRET",
        "authorizationServer": ["https://accounts.google.com"]
      }
    }
    ```
  </Step>

  <Step title="Have users connect">
    Each user opens **Customize → Connectors** in Claude Desktop, clicks **Connect** next to **BigQuery**, and approves Google's consent screen in the browser. Claude Desktop asks Google for offline access automatically, so the token refreshes in the background without another sign-in.
  </Step>
</Steps>

## Other Google servers

Google's other remote MCP servers take the same **Client ID**, **Client secret**, and **Authorization server** values. For the [Google Workspace servers](https://developers.google.com/workspace/guides/configure-mcp-servers) (Gmail, Drive, Calendar, Docs, Sheets, Slides, and Chat), that guide lists each server's URL and prerequisites, including a Google Cloud project enrolled in Google's [Workspace Developer Preview Program](https://developers.google.com/workspace/preview).

## Troubleshoot sign-in errors

These messages appear in `main.log` in the [logs directory](/docs/third-party/claude-desktop/data-storage#where-data-lives) on the user's device.

| Message                                                       | Cause                                                                                          | Fix                                                                                                                                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_secret is missing` after the browser sign-in succeeds | The entry has no **Client secret**                                                             | Enter the secret of the client named in **Client ID**, with **Authorization server** set to `["https://accounts.google.com"]`                                |
| `invalid_client`                                              | The secret doesn't belong to the client named in **Client ID**, or was deleted in Google Cloud | In **APIs & Services → Credentials**, add a new secret to that client and update **Client secret** in the server's entry. Users then click **Connect** again |
