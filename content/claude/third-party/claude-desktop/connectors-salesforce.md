> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Salesforce

> Give Claude access to your Salesforce org through Salesforce's plugin and hosted MCP server, set up in the Enterprise Admin Console or your managed configuration with an OAuth client that a Salesforce admin creates.

The Salesforce plugin and Salesforce's hosted MCP server let Claude work with your organization's Salesforce records. The plugin's marketplace is one of the preconfigured [plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin) Claude Desktop offers.

## Set up Salesforce

<Steps>
  <Step title="Prepare your Salesforce org">
    In Salesforce Setup, turn on **Enable MCP Service**, then create an External Client App for Claude Desktop with these OAuth settings:

    * The callback URL `http://127.0.0.1:53280/callback`
    * The OAuth scopes `mcp_api` and `refresh_token`
    * Proof Key for Code Exchange (PKCE) required
    * Access tokens issued as JSON Web Tokens (JWTs)
    * An OAuth policy that lets users self-authorize

    Copy the app's **Consumer Key**, which is its client ID. With PKCE, Claude Desktop needs no client secret.
  </Step>

  <Step title="Add the Salesforce marketplace">
    **In the Enterprise Admin Console.** Go to [claude.ai](https://claude.ai) → **Organization settings** and open the **Plugins** page under **Desktop 3P**. Under **Plugin marketplaces**, click **Add** and choose **Salesforce** under **From partners**. The new entry has **Source** set to **GitHub**, **Repository** set to `salesforce/salesforce-skills`, and **Ref** set to `claude-prod`, the branch Salesforce publishes its releases to. Leave **Installation** empty and click **Save changes**.

    **With MDM or a bootstrap server.** Add this entry to the [`allowedPluginMarketplaces`](/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces) key of your managed configuration or bootstrap response:

    ```json theme={null}
    {
      "source": "github",
      "repo": "salesforce/salesforce-skills",
      "ref": "claude-prod"
    }
    ```

    Either way the marketplace stays **available**, and each user installs the plugin once, as described in step 4. To install the plugin on every device without user action instead, set the ref to a full 40-character commit SHA and the installation preference to `auto_install`. [Marketplace installation preferences](/docs/third-party/claude-desktop/extensions#marketplace-installation-preferences) explains why the SHA is required, and [Roll out marketplace updates](/docs/third-party/claude-desktop/extensions#roll-out-marketplace-updates) explains how to move to a newer release.
  </Step>

  <Step title="Add the Salesforce MCP server">
    **In the Enterprise Admin Console.** Go to [claude.ai](https://claude.ai) → **Organization settings** and open the **Connectors** page under **Desktop 3P**. Under **Managed MCP servers**, click **Add → Blank**, fill in the entry as below, and click **Save changes**. [Set up sign-in for managed MCP servers](/docs/third-party/claude-desktop/mcp-sign-in) explains each **OAuth** field, and users' apps pick up console changes as described under [Configuration updates](/docs/third-party/claude-desktop/admin-console#configuration-updates).

    | Field                    | Value                                                              |
    | ------------------------ | ------------------------------------------------------------------ |
    | **Name**                 | `salesforce-h360`                                                  |
    | **Transport**            | **Streamable HTTP**                                                |
    | **URL**                  | `https://api.salesforce.com/platform/mcp/v1/platform/headless-360` |
    | **OAuth**                | **Bring your own client**                                          |
    | **Client ID**            | The Consumer Key from step 1                                       |
    | **Authorization server** | `["https://login.salesforce.com"]`                                 |

    **With MDM or a bootstrap server.** Add this entry to the [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) key of your managed configuration or bootstrap response:

    ```json theme={null}
    {
      "name": "salesforce-h360",
      "transport": "http",
      "url": "https://api.salesforce.com/platform/mcp/v1/platform/headless-360",
      "oauth": {
        "clientId": "YOUR_CONSUMER_KEY",
        "authorizationServer": ["https://login.salesforce.com"]
      }
    }
    ```

    Keep the name exactly as shown. The Salesforce plugin defines an MCP server with this name, and Claude Desktop matches your entry to it by name and connects it with your client ID. Without the entry, users get the plugin's skills but not its Salesforce tools.

    Enter exactly one URL as the authorization server. To send users to your org's My Domain login page instead of the shared Salesforce login page, enter that URL, for example `["https://yourorg.my.salesforce.com"]`.

    For a Salesforce sandbox org, create the External Client App in the sandbox and enter the sandbox's login URL as the authorization server, for example `["https://test.salesforce.com"]`. Set the URL to `https://api.salesforce.com/platform/mcp/v1/sandbox/platform/headless-360`.

    Devices need git installed to fetch the marketplace, and outbound HTTPS access to `github.com`, `api.salesforce.com`, and your Salesforce login host.
  </Step>

  <Step title="Have users install the plugin and connect">
    Each user opens **Customize → Plugins** in Claude Desktop and clicks **Discover**, which opens the **Directory**. On its **Organization** tab the user selects your marketplace's tab and clicks the **+** button on the Salesforce plugin to install it. The user then opens **Customize → Connectors**, clicks **Connect** next to **salesforce-h360**, and signs in to Salesforce in the browser.
  </Step>
</Steps>
