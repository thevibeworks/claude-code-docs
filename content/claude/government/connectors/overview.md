> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors

> Connectors let tenant administrators and organization owners add their agency's MCP servers: who gets them, authentication, OAuth redirect URIs, tool policy.

> **Who this is for:** Tenant administrators and organization owners who want Claude to reach their agency's own systems (for example, an internal search service or a ticketing tool) from Claude Desktop and other Claude products.

Use this page to add Model Context Protocol (MCP) servers for your own systems, choose which Claude products receive each one, and set which of their tools are available to members.

A **connector** is a link between Claude and an external service. The service, your agency's own or a vendor's, runs an MCP server, which is a standard way for a service to publish a set of tools that Claude can call. You add the server once here, and Claude for Government delivers it to the products you select.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **The Microsoft 365 connector**: see [Set up the Microsoft 365 connector](https://claude.com/docs/government/connectors/microsoft-365.md)
> * **Plugins**: see [Manage plugins and connectors](https://claude.com/docs/government/config/plugins-and-connectors.md)

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-07-connectors-and-plugins.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=43f78d15928eea46d27229f8dbc04db6" aria-label="Video walkthrough: Connectors and plugins" />

Video: Connectors and plugins (2 min 8 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#connectors-and-plugins)

## Who receives a connector

To see or add connectors, go to **Settings > Config** and open the **Connectors** card, under **Integrations**. A connector reaches the people whose settings you are editing when you add it: everyone in the [tenant](https://claude.com/docs/government/tenant-admin/configuration.md), everyone in an [organization](https://claude.com/docs/government/org-admin/configuration.md), or the members of one directory group, as described under [Group-specific settings](https://claude.com/docs/government/config/overview.md#group-specific-settings). In every case it is delivered only to the products you select, with the tool policy you set.

A connector added for a group does not always reach every member of the group. Only one group's settings, connectors included, apply to each person, as described under [When someone belongs to more than one group](https://claude.com/docs/government/config/overview.md#when-someone-belongs-to-more-than-one-group).

When the same connector name is added at more than one level, each member receives only the entry from the [most specific level](https://claude.com/docs/government/config/overview.md#how-settings-are-applied) that applies to them. That entry replaces the others as a whole, including its address, authentication, products, and tool policy.

### Change or stop an inherited connector

Unless a level above has [locked](https://claude.com/docs/government/config/overview.md#locks) the **Connectors** card, you can change an inherited connector for the members at your level: click **Add connector** and create one with the same name. The inherited connector's details and stored secret are not copied, so you enter the server address, authentication, and tool policy again. You cannot remove a connector inherited from a level above, but in the same way you can stop it from reaching the members at your level: add one with the same name and select no products under **Apply to**.

## Adding a connector

Go to **Settings > Config**, open the **Connectors** card, and click **Add connector**. On the tenant Config page, you first choose whether organizations **May set their own value** or **Must use this value**, which stops organizations and groups from adding connectors or replacing yours.

### Server address and authentication

* **Name** is a short identifier for the connector. It must be letters a to z in either case, digits, hyphens, or underscores. Claude Desktop shows members [the name](https://claude.com/docs/third-party/claude-desktop/configuration.md#managedmcpservers) with the capital letters you type. If you add a connector with a name already used at your level, even with different capital letters, the new connector replaces that one, tool policy included.
* **Server URL** is the address of the server's MCP endpoint. It must begin with `https://`. Enter the address the server answers on, not one that redirects to it. Claude Desktop [connects to it directly from each member's device](https://claude.com/docs/government/security/security-and-data-handling.md#connectors), so the server, and its sign-in provider if it uses OAuth, must be reachable from those devices. You do not need to ask Anthropic to allow either address.
* **Transport** selects how Claude talks to the server. Choose HTTP or SSE to match what your server supports.
* **Authentication** selects how Claude proves who it is to the server:
  * **None** is for a server that needs no sign-in: it sends no credentials. If the server asks for sign-in anyway, Claude Desktop [lets each member sign in](https://claude.com/docs/third-party/claude-desktop/extensions.md#oauth-sign-in).
  * **Header (shared secret)** sends a fixed header (for example, an authorization token) with every request; the value is stored securely and shown as `••••` after you save, and each member's app receives it.
  * **OAuth (members sign in)** has each member sign in on first use, and their tokens stay on their own machine. Choose it when the server's sign-in provider lets apps register themselves (dynamic client registration).
  * **OAuth (pre-registered app)** also has each member sign in, through an app you register with the server's sign-in provider ahead of time. Choose it when the provider has you create an app and copy its client ID.

Neither OAuth option stores a secret. If the server's sign-in provider requires a client secret, members can't connect to that server.

When you choose either OAuth option, a confirmation checkbox appears on the final step asking you to confirm that the server address is exactly the one you intend, because members are sent to a sign-in page that the server chooses. When sign-in happens somewhere other than the server itself, for example when you set a tenant ID for a Microsoft Entra app, the checkbox names both that sign-in address and the server address.

### Register an app for sign-in

For **OAuth (pre-registered app)**, add Claude Desktop's [redirect URI](https://claude.com/docs/third-party/claude-desktop/extensions.md#oauth-sign-in), `http://127.0.0.1:53280/callback`, to the app's registration with your sign-in provider. If the registration uses another port or `localhost`, set **Callback port** or **Callback host** in the wizard to match. Have the app's client ID ready, and for a single-tenant Microsoft Entra app its tenant ID and scope as well.

For the Claude Code command-line tool, set **Callback port** to the port you registered for Claude Desktop. Also add `http://localhost:PORT/callback`, with that port, to the registration. A connector with a tenant ID is not delivered to the command-line tool.

Enter the scope that your server's own API expects (for example, an `api://` scope for an app registered in your tenant), because Microsoft Graph scopes such as `Mail.Read` would give the connector's server access to members' Microsoft 365 data.

### Tool discovery

The wizard tries to list the tools the server offers, so that you can set policy on them. Discovery runs from your own browser and is best-effort; many servers cannot be reached this way (for example, because they require authentication or are on a private network), and you can always add tools by name on the next step instead.

Discovery can ask you to sign in to the server. The credential is used once in your browser for this probe and is never stored; it is separate from the **Authentication** choice on the Server step, which controls how members authenticate later.

### Products and tool policy

Under **Apply to**, tick the products that should receive this connector. **Microsoft 365** is the [Claude for Microsoft 365 add-in](https://claude.com/docs/government/deploy-microsoft-365/configure.md#before-you-begin), which cannot receive a connector that uses OAuth or that has any tool switched off.

Under **Tool policy**, switch each of the server's tools on or off, or leave it unlisted. On Claude Desktop, that tool policy shapes what members experience:

* A tool you switch off is blocked, so Claude cannot use it.
* A tool you switch on is available and asks the member on every use, and members are not offered a lasting approval for it. Its permission control is locked, and hovering over it shows **Permission set by your admin**.
* A tool you do not list is left to the member to turn on or off, and its approval prompts follow the member's own choices, which can include lasting approval. To return a listed tool to each member's control, remove its row.

A saved connector reaches members as described under [When changes take effect](https://claude.com/docs/government/config/overview.md#when-changes-take-effect).

### Connection to server failed

If **Connect** in Claude Desktop shows "Connection to server failed. You can try again.", check first that the device can reach the server's address, that the app you registered lists the redirect URI, and that no other program is using the callback port. When the provider doesn't list the redirect URI, its own error page opens in the member's browser. In the other two cases the member's [`main.log`](https://claude.com/docs/government/deploy-desktop/configure#troubleshooting) records the reason. [How OAuth sign-in works](https://claude.com/docs/third-party/claude-desktop/extensions.md#how-oauth-sign-in-works) lists other causes.

## Editing and removing a connector

To change a connector, edit it on the **Connectors** card. Changing the authentication method clears any stored secret and the app details saved for **OAuth (pre-registered app)**.

Click the remove button next to a connector to delete it; it is withdrawn from every product [when the change takes effect](https://claude.com/docs/government/config/overview.md#when-changes-take-effect). If you delete a connector that takes priority over an inherited connector with the same name, the inherited connector applies again.
