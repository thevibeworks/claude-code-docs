> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors

> Add Model Context Protocol servers for your own systems, choose which Claude products receive each one, and set which of their tools are available to members.

> **Who this is for:** Tenant administrators and organization owners who want Claude to reach their agency's own systems (for example, an internal search service or a ticketing tool) from Claude Desktop and other Claude products.

Use this page to add Model Context Protocol servers for your own systems, choose which Claude products receive each one, and set which of their tools are available to members.

A **connector** is a link between Claude and an external service. The service runs a Model Context Protocol (MCP) server, which is a standard way for a service to publish a set of tools that Claude can call. You add the server once here, and Claude for Government delivers it to the products you select.

## The Connectors card

The **Connectors** card appears on your [tenant](/docs/government/tenant-admin/configuration) or [organization](/docs/government/org-admin/configuration) Config page alongside the built-in connector cards, and on the Config page for each [directory group](/docs/government/config/overview#group-specific-settings). It lists the connectors added at the level you are viewing and the connectors that level inherits, with each one's name, address, the products it applies to, and a summary of how many of its tools are allowed. Click **Add connector** to open the wizard, or click the edit icon next to a connector added at this level to change it.

An inherited connector has a badge that says where it comes from, such as **Inherited from your tenant** or **Inherited from your organization**, in place of the edit and remove controls. To change an inherited connector for the members at your level, click **Add connector** and create one with the same name. The inherited connector's details and stored secret are not copied, so you enter the server address and authentication again. Your entry then replaces the inherited one in the list and takes priority over it, as described under [Who receives a connector](#who-receives-a-connector).

## Who receives a connector

Who receives a connector depends on where you add it:

* On the tenant Config page, it reaches the members of every organization in the tenant.
* On an organization's Config page, it reaches every member of that organization.
* On the Config page for a [directory group](/docs/government/config/overview#group-specific-settings), it reaches that group's members: in every organization when you open the group from the tenant Config page (a tenant-wide group setting), or only in one organization when you open the group from that organization's Config page (an organization group setting).

In every case it is delivered only to the products you select, with the tool policy you set.

When the same connector name is added at more than one level, each member receives only the entry from the most specific level that applies to them: the organization's group settings first, then the organization, then the tenant-wide group settings, then the tenant. That entry replaces the others as a whole, including its address, authentication, products, and tool policy. You cannot remove a connector inherited from a level above, but you can stop it from reaching the members at your level by adding one with the same name and selecting no products under **Apply to**.

A connector added for a group does not always reach every member of the group. Someone who belongs to more than one directory group receives group settings, connectors included, from only one of them: their [highest-priority group](/docs/government/config/overview#when-someone-belongs-to-more-than-one-group) that has any configuration. Adding a group's first connector or deleting its last one can therefore change which group, and so which group settings, apply to some members. The group's Config page shows a note when this could happen. To check which group applies to a particular member, use the person lookup described under [Comparing settings across levels](/docs/government/config/overview#comparing-settings-across-levels).

## Adding a connector

The **Add connector** button opens a three-step wizard.

### Step 1: Server

Enter the details of the MCP server.

* **Name** is a short identifier for the connector. It must be lowercase letters, digits, hyphens, or underscores.
* **Server URL** is the address of the server's MCP endpoint. It must begin with `https://`.
* **Transport** selects how Claude talks to the server. Choose HTTP or SSE to match what your server supports.
* **Authentication** selects how Claude proves who it is to the server. **None** sends no credentials. **Header (shared secret)** sends a fixed header (for example, an authorization token) with every request; the value is stored securely and shown as `••••` after you save. **OAuth (members sign in)** has each member sign in on first use, and their tokens stay on their own machine. **OAuth (pre-registered app)** also has each member sign in, through an app you register with the server's sign-in provider ahead of time.

For **OAuth (pre-registered app)**, enter the **Client ID** your provider issued when you registered the app. A single-tenant Microsoft Entra app also needs its **Tenant ID** and the **Scope** the app requests. Enter the scope that your server's own API expects (for example, an `api://` scope for an app registered in your tenant), because Microsoft Graph scopes such as `Mail.Read` would give the connector's server access to members' Microsoft 365 data. Neither OAuth option stores a secret.

When you choose either OAuth option, a confirmation checkbox appears on the final step asking you to confirm that the server address is exactly the one you intend, because members are sent to a sign-in page that the server chooses. When sign-in happens somewhere other than the server itself, for example when you set a tenant ID for a Microsoft Entra app, the checkbox names both that sign-in address and the server address.

### Step 2: Discover tools

This step tries to list the tools the server offers so that you can set policy on the next step. Discovery runs from your own browser and is best-effort; many servers cannot be reached this way (for example, because they require authentication or are on a private network), and you can always add tools by name on the next step instead.

Click **Discover tools** to run the probe. If the server answers, the tools it advertises are listed. If the server asks for sign-in, a **Sign in to discover** option appears: confirm the sign-in host, sign in through the popup, and the probe runs again with that one-time credential. The credential is used once in your browser for this probe and is never stored; it is separate from the **Authentication** choice on the Server step, which controls how members authenticate later.

The **Sign in to discover** option does not appear when you choose **OAuth (pre-registered app)**, because this probe does not sign in with the app you registered. Add the tools by name on the next step.

### Step 3: Policy & scope

Choose which products receive this connector and which of its tools are available.

Under **Apply to**, tick the products that should receive this connector: Claude Desktop and Microsoft 365. A connector with no products ticked is saved but delivered nowhere, which is a way to pause it. A connector that uses OAuth cannot be applied to Microsoft 365, because per-user sign-in is not available there. A connector with any tool switched off in the table below also cannot be applied to Microsoft 365, and the checkbox is disabled with a **needs every tool on** note until every tool is on.

Under **Tool policy**, the table lists the tools found during discovery with an on/off switch for each. **Refresh tools** probes the server again and fills in any tools that are new since you last looked, keeping the switches you have already set. **Add tool** lets you type a tool name by hand when discovery could not reach the server.

On Claude Desktop, a tool you switch off is blocked, a tool you switch on is available and each member still approves its use, and a tool that is not listed at all is left to the member to enable or disable. You cannot apply this connector to Microsoft 365 while any tool in this table is switched off. If you are editing a connector that already applies to Microsoft 365 and you switch a tool off, a warning tells you that saving will remove it from Microsoft 365.

Click **Save** to create the connector. It appears in the **Connectors** card and is delivered to the products you ticked.

## Editing and removing a connector

Click the edit icon next to a connector in the card to open the same wizard with its current values filled in. Changing the authentication method clears any stored secret and the app details saved for **OAuth (pre-registered app)**. Click the remove button next to a connector to delete it; it is withdrawn from every product at the next refresh. If you delete a connector that takes priority over an inherited connector with the same name, the inherited connector applies again from that refresh.
