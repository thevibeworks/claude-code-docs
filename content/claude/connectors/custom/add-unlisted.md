> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a connector that isn't in the directory

> Connect Claude to an MCP server that isn't in the Connectors Directory, by its URL or as a local desktop extension.

You can connect Claude to a [Model Context Protocol (MCP)](/docs/connectors/building/mcp) server that isn't listed in the [Connectors Directory](/docs/connectors/directory). You add a remote server by its URL as a custom connector. In Claude Desktop, you can also use a desktop extension, which runs the server on your own computer.

This page is for people adding a connector to their own Claude and for Team and Enterprise Owners adding one for their organization.

<Note>
  * If you want a service that's already in the directory, see the [Connectors Directory](/docs/connectors/directory) and connect it from there
  * If you're building the server yourself, see [Build an MCP server for Claude](/docs/connectors/building/index)
  * If your server runs inside your private network, see [MCP tunnels](/docs/connectors/mcp-tunnels/overview)
</Note>

If you have a server URL, go to [Add a connector by URL](#add-a-connector-by-url). If you have a desktop extension, go to [Install a local connector in the desktop app](#install-a-local-connector-in-the-desktop-app).

## Choose a URL or a local install

A connector by URL suits internet-hosted services and public APIs. A desktop extension suits access to local files or tools, sensitive enterprise data, and work that needs offline capability.

| You have                       | Use                                                                                           | Works in                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| The URL of a remote MCP server | [Add a connector by URL](#add-a-connector-by-url)                                             | Free, Pro, Max, Team, and Enterprise plans     |
| A desktop extension            | [Install a local connector in the desktop app](#install-a-local-connector-in-the-desktop-app) | The Claude desktop app, signed in to claude.ai |

## Add a connector by URL

You can add any third-party connector as a custom connector as long as you have the URL of its remote MCP server. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.

<Warning>
  Custom connectors allow connections to unverified services. Claude can access and perform actions within these services, so review [Security and privacy](#security-and-privacy) before you add one.
</Warning>

### On a Team or Enterprise plan

An Owner adds the connector for the organization. On Enterprise plans, a member whose custom role includes managing the organization's libraries can add it too. If you're a member without one of those roles, you can't add a custom connector yourself, so ask an Owner to add it.

#### Add the connector for the organization

Adding the connector in organization settings makes it appear under [**Customize > Connectors**](https://claude.ai/customize/connectors) for members, with the **Custom** label. To add it:

<Steps>
  <Step title="Open organization connectors">
    Go to [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors).
  </Step>

  <Step title="Add a custom connector">
    Select **Add**, then **Custom**. If Claude asks for the connector type, choose **Web**.
  </Step>

  <Step title="Enter the server URL">
    Enter the remote MCP server URL.
  </Step>

  <Step title="Enter OAuth credentials if needed">
    Optionally, enter an OAuth client ID and secret. See [Choose authentication settings](#choose-authentication-settings).
  </Step>

  <Step title="Add the connector">
    Click **Add**.
  </Step>
</Steps>

#### Connect as a member

Once an Owner has added the connector, each member connects to it with their own account:

<Steps>
  <Step title="Open Customize > Connectors">
    Go to **Customize > Connectors**.
  </Step>

  <Step title="Find the custom connector">
    Find the connector with the **Custom** label.
  </Step>

  <Step title="Connect">
    Click **Connect** to authenticate.
  </Step>
</Steps>

### On a Free, Pro, or Max plan

You add custom connectors to your own account. On the Free plan, you can add one custom connector.

<Steps>
  <Step title="Open Customize > Connectors">
    Go to **Customize > Connectors**.
  </Step>

  <Step title="Add a custom connector">
    Click **Add custom connector**.
  </Step>

  <Step title="Enter the server URL">
    Enter the remote MCP server URL.
  </Step>

  <Step title="Enter OAuth credentials if needed">
    Optionally, enter OAuth credentials. See [Choose authentication settings](#choose-authentication-settings).
  </Step>

  <Step title="Add the connector">
    Click **Add**.
  </Step>
</Steps>

### Choose authentication settings

The layout of the **Add custom connector** dialog varies by organization. If yours shows a name, a URL, and **Advanced settings** on one screen, enter the OAuth client ID and secret under **Advanced settings**. If yours has two steps, it asks you to choose among the settings in this section.

For **MCP server URL**, enter the HTTPS address where the server accepts MCP requests, for example `https://mcp.example.com/mcp`.

For **Authentication**, choose how people connect to the server:

* **Sign in now**: each user signs in through the server's OAuth flow before using the connector
* **Sign in when needed**: Claude connects without credentials and prompts users to sign in when the server asks
* **No sign-in**: anyone with access to the server URL can use the connector. If the server uses an API key, choose **No sign-in** and add the key under **Request headers**. Claude stores the key as the connector's credential

For **OAuth client**, choose how Claude identifies itself to the server's authorization server. You see this setting unless you chose **No sign-in**.

* **Use Claude's published identity**: the recommended option. The server reads Claude's client details from a Client ID Metadata Document that Anthropic hosts. You set nothing up, and the server must support this method
* **Register automatically**: Claude registers OAuth clients with the server as users connect, using Dynamic Client Registration. This works with most servers and adds client registrations over time
* **Use your own OAuth client**: enter a client ID you registered with the server. Leave the secret blank unless your authorization server requires one. See [Authentication for connectors](/docs/connectors/building/authentication)

For **Request headers**, add fixed credentials such as API keys that Claude sends on every request. See [Authenticate with request headers](#authenticate-with-request-headers).

Change **Advanced > Transport** only if the server's documentation says to. A URL ending in `/sse` selects the older SSE transport.

### Authenticate with request headers

<Note>
  Request header authentication is in beta and available to a limited set of organizations. If you don't see the **Request headers** section in the **Add custom connector** dialog, your organization doesn't have access yet.
</Note>

If your MCP server authenticates with an API key, bearer token, or other fixed credential instead of OAuth, configure it in the **Request headers** section of the **Add custom connector** dialog. Claude stores each header value securely, doesn't show it again after you save, and sends it on every request to your server.

Request headers suit services where everyone in your organization shares one credential, such as an internal tool or a service account. If each person needs to sign in with their own account, use OAuth instead.

You can also use request headers in addition to OAuth, including OAuth with your own pre-registered client credentials. Claude sends the headers on every request alongside the OAuth bearer token. Use this to verify where a request came from, to pass additional client metadata, or to work with tunnels and gateways that need their own routing header. On an OAuth connection you can't configure `Authorization` as a request header, because OAuth uses that header.

#### Add a request header

A request header holds a fixed credential, such as an API key, that Claude stores and sends on every request to your server. To add one:

<Steps>
  <Step title="Open Request headers">
    In the **Add custom connector** dialog, open **Request headers**.
  </Step>

  <Step title="Choose the header name">
    Select a header name from the list, or choose **Custom header** to enter a different name. The list offers standard authentication and routing header names such as `authorization`, `x-api-key`, and `x-auth-token`, which every connector can use.
  </Step>

  <Step title="Enter the value">
    Enter the header value exactly as your server expects to receive it.
  </Step>

  <Step title="Mark it required or optional">
    Choose whether the header is **Required**. When a required header has no stored value at connection time, the connection fails. When an optional header has no value, Claude omits it from the request.
  </Step>

  <Step title="Add more headers and save">
    Repeat for any additional headers your server needs, then click **Add**. You can add up to four headers.
  </Step>
</Steps>

Anthropic reviews and approves each custom header name before Claude sends it to a third-party server. This review prevents connector configuration from being used to send arbitrary header names. If you enter a header name that isn't approved, Claude rejects the save with an error. To request approval for a custom header name, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support).

#### Enter the full header value

Claude sends the value exactly as you enter it. It doesn't add an authentication scheme or any other prefix. For an `Authorization` header, include the scheme in the value, as this table shows.

| You enter           | Claude sends                       |
| ------------------- | ---------------------------------- |
| `Bearer your-token` | `Authorization: Bearer your-token` |
| `your-token`        | `Authorization: your-token`        |

Most servers that use bearer tokens reject a value without the `Bearer ` scheme. If your server's documentation shows `Authorization: Bearer YOUR_TOKEN`, enter `Bearer ` followed by your token, including the space. The same applies to Basic authentication, where you enter `Basic ` followed by the base64-encoded credentials.

### Turn connectors on or off in a chat

You can turn each connector on or off for a single conversation. Click the **+** button in your chat interface and select **Connectors**, then turn each connector on or off for that conversation.

### Edit or remove a connector

You can edit a connector's name or URL, or remove the connector:

<Steps>
  <Step title="Open your connectors">
    Go to **Customize > Connectors**. If you're a Team or Enterprise Owner, go to **Organization settings > Connectors** instead.
  </Step>

  <Step title="Remove or open the menu">
    Click **Remove**, or select the three-dot menu.
  </Step>

  <Step title="Follow the prompts">
    Follow the prompts.
  </Step>
</Steps>

You can't change authentication settings after you add a connector. That covers OAuth credentials and request headers. To change them, remove the connector and add it again with the new details. Members then need to reconnect.

## Install a local connector in the desktop app

A desktop extension is a local MCP server packaged with MCPB (MCP Bundles) that runs on your device inside Claude Desktop. Use one when Claude needs local tools without an internet dependency, or a custom integration with an internal tool.

You can install a desktop extension in the Claude desktop app when you're signed in to claude.ai. Your organization can turn extensions off or limit which ones you can install. When extensions are turned off, **Extensions** doesn't appear in settings.

To install an extension you have as a `.mcpb` file:

<Steps>
  <Step title="Open Settings > Extensions">
    In the Claude desktop app, go to **Settings > Extensions**.
  </Step>

  <Step title="Drag in the file">
    Drag the `.mcpb` file onto the page. Claude opens a preview of the extension.
  </Step>

  <Step title="Install">
    Select **Install**, then confirm.
  </Step>
</Steps>

The extension then appears in the list on the **Extensions** page.

### Get a desktop extension from your organization

On Team and Enterprise plans, your organization can build its own desktop extensions and package them with MCPB. It deploys them through enterprise software management and controls which extensions you can install.

### Build and package a desktop extension

If you're authoring the extension, follow [Build a desktop extension with MCPB](/docs/connectors/building/mcpb) and the [MCPB documentation](https://github.com/modelcontextprotocol/mcpb). You build your MCP server, bundle it with MCPB, test it locally, and then deploy it to your organization.

## Security and privacy

Some connectors in the directory are verified by Anthropic and others are community connectors, as [connector verification](/docs/connectors/verification) explains. A connector you add yourself connects Claude to an unverified service.

### Connectors you add by URL

A remote MCP server gives Claude tools that can read data from applications, create, modify, or delete data, and take actions on your behalf. Before you connect to one, take these precautions:

* Only connect to servers from trusted organizations
* Carefully review requested permission scopes during authentication
* Be aware of prompt injection risks. Claude has built-in protections
* Monitor for unexpected changes in tool behavior

While you use the connector, take these precautions:

* Monitor Claude's actions for unintended effects
* Review tool approval requests carefully
* Only click **Always allow** for trusted servers
* Turn off connectors you aren't using with the toggles in the **Connectors** item of the chat **+** menu
* Block individual tools you don't need under **Customize > Connectors** by selecting the connector and setting the tool's permission to **Blocked**

### Desktop extensions

A desktop extension runs locally with your user permissions:

* It can access only what you can access
* It transmits no data unless the extension is explicitly designed to
* Enterprise organizations get full audit capability
* Administrators can revoke it

### Report a malicious server

Report malicious MCP servers to [Anthropic's Bug Bounty Program](https://www.anthropic.com/responsible-disclosure-policy).

## Next steps

* [Build an MCP server for Claude](/docs/connectors/building/index): build your own remote MCP server for any tool
* [Connector verification](/docs/connectors/verification): which directory connectors Anthropic verifies and which are community connectors
* [MCP in Claude Code](https://code.claude.com/docs/en/mcp-quickstart): add the same server to Claude Code from the command line
