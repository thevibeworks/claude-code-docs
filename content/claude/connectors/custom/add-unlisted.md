> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a connector that isn't in the directory

> Connect Claude to an MCP server that isn't in the Connectors Directory, by its URL or as a local desktop extension.

You can connect Claude to a [Model Context Protocol (MCP)](https://claude.com/docs/connectors/building/mcp.md) server that isn't listed in the [Connectors Directory](https://claude.com/docs/connectors/directory.md). You add a remote server by its URL as a custom connector. In Claude Desktop, you can also use a desktop extension, which runs the server on your own computer.

This page is for people adding a connector to their own Claude and for Team and Enterprise Owners adding one for their organization.

> [!NOTE]
>
> * If you want a service that's already in the directory, see the [Connectors Directory](https://claude.com/docs/connectors/directory.md) and connect it from there
> * If you're building the server yourself, see [Build an MCP server for Claude](https://claude.com/docs/connectors/building/index.md)
> * If your server runs inside your private network, see [MCP tunnels](https://claude.com/docs/connectors/mcp-tunnels/overview)

If you have a server URL, go to [Add a connector by URL](#add-a-connector-by-url). If you have a desktop extension, go to [Install a local connector in the desktop app](#install-a-local-connector-in-the-desktop-app).

## Choose a URL or a local install

A connector by URL suits internet-hosted services and public APIs. A desktop extension suits access to local files or tools, sensitive enterprise data, and work that needs offline capability.

| You have | Use | Works in |
| - | - | - |
| The URL of a remote MCP server | [Add a connector by URL](#add-a-connector-by-url) | Free, Pro, Max, Team, and Enterprise plans |
| A desktop extension | [Install a local connector in the desktop app](#install-a-local-connector-in-the-desktop-app) | The Claude desktop app, signed in to claude.ai |

## Add a connector by URL

You can add any third-party connector as a custom connector as long as you have the URL of its remote MCP server. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.

> [!WARNING]
>
> Custom connectors allow connections to unverified services. Claude can access and perform actions within these services, so review [Security and privacy](#security-and-privacy) before you add one.

### On a Team or Enterprise plan

An Owner adds the connector for the organization. On Enterprise plans, a member whose custom role includes managing the organization's libraries can add it too. If you're a member without one of those roles, you can't add a custom connector yourself, so ask an Owner to add it.

#### Add the connector for the organization

Adding the connector in organization settings makes it appear under [**Customize > Connectors**](https://claude.ai/customize/connectors) for members, with the **Custom** label. To add it:

**1. Open organization connectors**

Go to [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors).

**2. Add a custom connector**

Select **Add**, then **Custom**. If Claude asks for the connector type, choose **Web**.

**3. Enter the server URL**

Enter the remote MCP server URL.

**4. Enter OAuth credentials if needed**

Optionally, enter an OAuth client ID and secret. See [Choose authentication settings](#choose-authentication-settings).

**5. Add the connector**

Click **Add**.

#### Connect as a member

Once an Owner has added the connector, each member connects to it with their own account:

**1. Open Customize > Connectors**

Go to **Customize > Connectors**.

**2. Find the custom connector**

Find the connector with the **Custom** label.

**3. Connect**

Click **Connect** to authenticate.

### On a Free, Pro, or Max plan

You add custom connectors to your own account. On the Free plan, you can add one custom connector.

**1. Open Customize > Connectors**

Go to **Customize > Connectors**.

**2. Add a custom connector**

Click **Add custom connector**.

**3. Enter the server URL**

Enter the remote MCP server URL.

**4. Enter OAuth credentials if needed**

Optionally, enter OAuth credentials. See [Choose authentication settings](#choose-authentication-settings).

**5. Add the connector**

Click **Add**.

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
* **Use your own OAuth client**: enter a client ID you registered with the server. Leave the secret blank unless your authorization server requires one. See [Authentication for connectors](https://claude.com/docs/connectors/building/authentication.md)

For **Request headers**, add fixed credentials such as API keys that Claude sends on every request. See [Authenticate with request headers](#authenticate-with-request-headers).

Change **Advanced > Transport** only if the server's documentation says to. A URL ending in `/sse` selects the older SSE transport.

### Authenticate with request headers

> [!NOTE]
>
> Request header authentication is in beta and available to a limited set of organizations. If you don't see the **Request headers** section in the **Add custom connector** dialog, your organization doesn't have access yet.

If your MCP server authenticates with an API key, bearer token, or other fixed credential instead of OAuth, configure it in the **Request headers** section of the **Add custom connector** dialog. Claude stores each header value securely, doesn't show it again after you save, and sends it on every request to your server.

Request headers suit services where everyone in your organization shares one credential, such as an internal tool or a service account. If each person needs to sign in with their own account, use OAuth instead.

You can also use request headers in addition to OAuth, including OAuth with your own pre-registered client credentials. Claude sends the headers on every request alongside the OAuth bearer token. Use this to verify where a request came from, to pass additional client metadata, or to work with tunnels and gateways that need their own routing header. On an OAuth connection you can't configure `Authorization` as a request header, because OAuth uses that header.

#### Add a request header

A request header holds a fixed credential, such as an API key, that Claude stores and sends on every request to your server. To add one:

**1. Open Request headers**

In the **Add custom connector** dialog, open **Request headers**.

**2. Choose the header name**

Select a header name from the list, or choose **Custom header** to enter a different name. The list offers standard authentication and routing header names such as `authorization`, `x-api-key`, and `x-auth-token`, which every connector can use.

**3. Enter the value**

Enter the header value exactly as your server expects to receive it.

**4. Mark it required or optional**

Choose whether the header is **Required**. When a required header has no stored value at connection time, the connection fails. When an optional header has no value, Claude omits it from the request.

**5. Add more headers and save**

Repeat for any additional headers your server needs, then click **Add**. You can add up to four headers.

Anthropic reviews and approves each custom header name before Claude sends it to a third-party server. This review prevents connector configuration from being used to send arbitrary header names. If you enter a header name that isn't approved, Claude rejects the save with an error. To request approval for a custom header name, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support).

#### Enter the full header value

Claude sends the value exactly as you enter it. It doesn't add an authentication scheme or any other prefix. For an `Authorization` header, include the scheme in the value, as this table shows.

| You enter | Claude sends |
| - | - |
| `Bearer your-token` | `Authorization: Bearer your-token` |
| `your-token` | `Authorization: your-token` |

Most servers that use bearer tokens reject a value without the `Bearer ` scheme. If your server's documentation shows `Authorization: Bearer YOUR_TOKEN`, enter `Bearer ` followed by your token, including the space. The same applies to Basic authentication, where you enter `Basic ` followed by the base64-encoded credentials.

### Turn connectors on or off in a chat

You can turn each connector on or off for a single conversation. Click the **+** button in your chat interface and select **Connectors**, then turn each connector on or off for that conversation.

### Edit or remove a connector

You can edit a connector's name or URL, or remove the connector:

**1. Open your connectors**

Go to **Customize > Connectors**. If you're a Team or Enterprise Owner, go to **Organization settings > Connectors** instead.

**2. Remove or open the menu**

Click **Remove**, or select the three-dot menu.

**3. Follow the prompts**

Follow the prompts.

You can't change authentication settings after you add a connector. That covers OAuth credentials and request headers. To change them, remove the connector and add it again with the new details. Members then need to reconnect.

## Install a local connector in the desktop app

A desktop extension is a local MCP server packaged with MCPB (MCP Bundles) that runs on your device inside Claude Desktop. Use one when Claude needs local tools without an internet dependency, or a custom integration with an internal tool.

You can install a desktop extension in the Claude desktop app when you're signed in to claude.ai. Your organization can turn extensions off or limit which ones you can install. When extensions are turned off, **Extensions** doesn't appear in settings.

To install an extension you have as a `.mcpb` file:

**1. Open Settings > Extensions**

In the Claude desktop app, go to **Settings > Extensions**.

**2. Drag in the file**

Drag the `.mcpb` file onto the page. Claude opens a preview of the extension.

**3. Install**

Select **Install**, then confirm.

The extension then appears in the list on the **Extensions** page.

### Get a desktop extension from your organization

On Team and Enterprise plans, your organization can build its own desktop extensions and package them with MCPB. It deploys them through enterprise software management and controls which extensions you can install.

### Build and package a desktop extension

If you're authoring the extension, follow [Build a desktop extension with MCPB](https://claude.com/docs/connectors/building/mcpb.md) and the [MCPB documentation](https://github.com/modelcontextprotocol/mcpb). You build your MCP server, bundle it with MCPB, test it locally, and then deploy it to your organization.

## Security and privacy

Some connectors in the directory are verified by Anthropic and others are community connectors, as [connector verification](https://claude.com/docs/connectors/verification.md) explains. A connector you add yourself connects Claude to an unverified service.

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

* [Build an MCP server for Claude](https://claude.com/docs/connectors/building/index.md): build your own remote MCP server for any tool
* [Connector verification](https://claude.com/docs/connectors/verification.md): which directory connectors Anthropic verifies and which are community connectors
* [MCP in Claude Code](https://code.claude.com/docs/en/mcp-quickstart): add the same server to Claude Code from the command line
