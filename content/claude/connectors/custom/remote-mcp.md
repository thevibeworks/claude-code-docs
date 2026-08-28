> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Third party connectors with remote MCP

> Connect Claude to your tools using the Model Context Protocol

Custom connectors enable you to link Claude directly to your essential tools and data sources using the Model Context Protocol (MCP).

## What are third party connectors?

Custom connectors allow Claude to operate within your preferred software and leverage comprehensive context from your external tools.

You can:

* Connect Claude to existing remote MCP servers
* Build your own remote MCP servers for any tool

### Finding connectors

Browse the [Connectors Directory](/docs/connectors/directory) to discover third-party MCP servers that are ready to use across all Claude products. Some are verified by Anthropic and others are community connectors; see [connector verification](/docs/connectors/verification).

## Adding custom connectors

You can manually add any third-party connector to Claude as long as you have the URL of that remote MCP server.

<Warning>
  **Security Notice**: Custom connectors allow connections to unverified services. Claude can access and perform actions within these services, so review security considerations carefully.
</Warning>

### For Team and Enterprise plans

**Owners must:**

1. Navigate to **Organization settings > Connectors**
2. Select **Add**, then **Custom**. If Claude asks for the connector type, choose **Web**.
3. Enter the remote MCP server URL
4. Optionally configure OAuth Client ID/Secret in Advanced settings
5. Click "Add"

If your Add custom connector dialog has two steps, see [The Add custom connector dialog, field by field](#the-add-custom-connector-dialog-field-by-field).

**Members then:**

1. Go to **Customize > Connectors**
2. Find the connector with "Custom" label
3. Click "Connect" to authenticate

### For Free, Pro, and Max plans

1. Navigate to **Customize > Connectors**
2. Click "Add custom connector"
3. Enter the remote MCP server URL
4. Optionally configure OAuth credentials
5. Click "Add"

If your Add custom connector dialog has two steps, see [The Add custom connector dialog, field by field](#the-add-custom-connector-dialog-field-by-field).

### Enabling connectors in chat

Use the "+" button in your chat interface to access "Connectors," where you can enable/disable connectors per conversation.

## The Add custom connector dialog, field by field

<Note>
  The two-step dialog described here is rolling out gradually. If your dialog shows a name, URL, and Advanced settings on one screen, your organization has the earlier version; the steps above still apply.
</Note>

**Name**: the display name shown in the connectors list.

**Remote MCP server URL**: the HTTPS address where the server accepts MCP requests, for example `https://mcp.example.com/mcp`. After you continue, Claude checks the URL and pre-fills the authentication settings it detects, marked "Detected."

**Authentication**: how people connect to the server.

* **Always required**: each user signs in through the server's OAuth flow before using it.
* **Required when the server asks**: Claude connects without credentials and prompts users to sign in when the server asks.
* **None**: no sign-in. Anyone with access to the server URL can use the connector. If the server uses an API key, choose None and add the key under **Request headers**; Claude stores it as the connector's credential.

**OAuth client** (shown unless you chose None): how Claude identifies itself to the server's authorization server.

* **Use Anthropic's hosted client metadata** (recommended): the server reads Claude's client details from a URL Anthropic hosts (Client ID Metadata Document). Nothing to set up; the server must support it.
* **No client ID — register one automatically**: Claude registers OAuth clients with the server as users connect (Dynamic Client Registration). Works with most servers, but adds client registrations over time.
* **Use your own OAuth client**: enter a client ID you registered with the server. Leave the secret blank unless your authorization server requires one. See [Authentication for connectors](/docs/connectors/building/authentication).

**Request headers**: fixed credentials such as API keys, sent on every request. See [Authenticating with request headers](#authenticating-with-request-headers).

**Advanced > Transport**: set from the URL automatically; a URL ending in `/sse` selects the older SSE transport. Change it only if the server's documentation says to.

## Authenticating with request headers

<Note>
  Request header authentication is in beta and available to a limited set of organizations. If you don't see the **Request headers** section in the Add custom connector dialog, your organization doesn't have access yet.
</Note>

If your MCP server authenticates with an API key, bearer token, or other fixed credential instead of OAuth, you can configure it in the **Request headers** section of the Add custom connector dialog. Claude stores each header value securely, does not show it again after you save, and sends it on every request to your server.

Request headers suit services where everyone in your organization shares one credential, such as an internal tool or a service account. If each person needs to sign in with their own account, use OAuth instead.

You can also use request headers in addition to OAuth, including OAuth with your own pre-registered client credentials. Headers configured on an OAuth connection are sent on every request alongside the OAuth bearer token. This is useful for verifying where a request came from, passing additional client metadata, or working with tunnels and gateways that need their own routing header. The one exception is `Authorization`: OAuth owns that header, so it cannot be configured as a request header on an OAuth connection.

### Adding a request header

1. In the Add custom connector dialog, open **Request headers**.
2. Select a header name from the list, or choose **Custom header** to enter a different name. The list offers standard authentication and routing header names such as `authorization`, `x-api-key`, and `x-auth-token`, which every connector can use. Anthropic reviews and approves each custom header name before Claude will send it to a third-party server, which prevents connector configuration from being used to send arbitrary header names. If you enter a header name that isn't approved, Claude rejects the save with an error. To request approval for a custom header name, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support).
3. Enter the header value exactly as your server expects to receive it.
4. Choose whether the header is **Required**. When a required header has no stored value at connection time, the connection fails. When an optional header has no value, Claude simply omits it from the request.
5. Repeat for any additional headers your server needs (you can add up to four), then click **Add**.

### Enter the full header value

Claude sends the value exactly as you enter it. It does not add an authentication scheme or any other prefix.

For an `Authorization` header, include the scheme in the value:

| You enter           | Claude sends                       |
| ------------------- | ---------------------------------- |
| `Bearer your-token` | `Authorization: Bearer your-token` |
| `your-token`        | `Authorization: your-token`        |

Most servers that use bearer tokens reject the second form. If your server's documentation shows `Authorization: Bearer YOUR_TOKEN`, enter `Bearer ` followed by your token, including the space. The same applies to Basic authentication: enter `Basic ` followed by the base64-encoded credentials.

## Managing connectors

To edit a connector's name or URL, or to remove a connector:

1. Go to **Customize > Connectors** (Team and Enterprise owners: **Admin settings > Connectors**)
2. Click "Remove" or select the three-dot menu
3. Follow the prompts

Authentication settings (OAuth credentials and request headers) can't be changed after a connector is added. To change them, remove the connector and add it again with the new details. Members will need to reconnect.

## Security and privacy

### Best practices

* Only connect to servers from trusted organizations
* Carefully review requested permission scopes during authentication
* Be aware of prompt injection risks; Claude has built-in protections
* Monitor for unexpected changes in tool behavior

### Tool actions

Remote MCP servers enable Claude to invoke tools that can:

* Read data from applications
* Create, modify, or delete data
* Take actions on your behalf

**Usage guidelines:**

* Monitor Claude's actions for unintended effects
* Review tool approval requests carefully
* Only click "Always allow" for trusted servers
* Turn off connectors you aren't using with the toggles in the chat "+" menu's **Connectors** item
* Block individual tools you don't need under **Customize > Connectors** by selecting the connector and setting the tool's permission to **Blocked**

## Reporting issues

Report malicious MCP servers to [Anthropic's Bug Bounty Program](https://www.anthropic.com/responsible-disclosure-policy).

## Related topics

<Columns cols={2}>
  <Card title="Building Connectors" icon="hammer" href="/docs/connectors/building/">
    Learn to build your own MCP servers.
  </Card>

  <Card title="Connectors Directory" icon="book" href="/docs/connectors/directory">
    Browse pre-built connectors.
  </Card>

  <Card title="MCP Overview" icon="plug" href="/docs/connectors/building/mcp">
    Understand the Model Context Protocol.
  </Card>

  <Card title="Desktop Extensions" icon="desktop" href="/docs/connectors/custom/desktop-extensions">
    Deploy enterprise-grade MCP servers.
  </Card>

  <Card title="MCP in Claude Code" icon="terminal" href="https://code.claude.com/docs/en/mcp-quickstart">
    Add the same server to Claude Code from the command line.
  </Card>
</Columns>
