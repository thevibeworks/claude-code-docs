Title: MCP connectors

URL Source: https://support.claude.com/en/articles/14503689-mcp-connectors

Markdown Content:
MCP connectors let Claude connect to your organization’s tools, data sources, and services. Claude can search your documents, read your email, or call external APIs on your behalf, all without leaving the chat.

## How MCP connectors differ in Claude for Government

**Claude for Government runs the first FedRAMP High authorized MCP implementation.**The MCP framework, the infrastructure that registers, authenticates, and executes Anthropic-provided connectors, operates entirely within the Claude for Government authorized boundary. Because the authorization covers MCP as a feature, new Anthropic-provided and customer-provided connectors can be added without additional FedRAMP audits of Claude for Government itself, as long as the connectors meet your agency's data-handling requirements.

**The connector catalog is curated.** Only connectors approved for the government environment appear in the Admin Settings directory, so some commercial Claude connectors are not available.

## Browse available connectors

Organizations can also register their own MCP servers for internal systems, custom tools, or approved third-party services. See **[Custom Connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)**.

## Enable a connector for your organization

Connectors are enabled org-wide from Admin Settings. Once enabled, individual users in your organization can connect their own accounts.

## Connect your account to a connector

After your org admin enables a connector, it appears in your personal settings.

## Security and privacy

### How authentication works

Connectors use delegated, per-user OAuth wherever possible. When you connect a tool, Claude inherits your permissions in that tool and can only see and do what you can already see and do. There are no service accounts with elevated access.

### Where your credentials are stored

OAuth tokens are encrypted at rest and stored entirely within the Claude for Government FedRAMP High boundary. Tokens are scoped to the individual user who authenticated and are never shared between users. Anthropic does not receive standing access to your connected tenants.

### What stays inside the boundary

The MCPservice, token storage, and all connector-execution audit logging stay inside the FedRAMP High authorized environment. Each tool invocation follows the path:

User → Claude (in boundary) → MCP service(in boundary) → connected service

Whether the **connected service** sits inside or outside the boundary depends on the connector. The catalog description for each connector states this explicitly. For example, the Microsoft 365 connector calls Microsoft Graph within your tenant; the Web Search connector calls a third-party search API outside the boundary under a zero-data-retention agreement.

## Frequently asked questions

### Does enabling a connector give Anthropic access to our data?

No. Connectors use per-user delegated OAuth. Data flows between the in-boundary MCP proxy and the connected service using the individual user's credentials. Anthropic does not receive standing access to your tenant.

### If we add a new connector, do we need to update our ATO?

Adding a connector does not change Claude for Government's FedRAMP authorization—MCP was authorized as a feature. Whether your agency's own ATO requires an update depends on the data the connector handles and your internal authorization process.

### Can we restrict which users in our org can use a connector?

Connectors are enabled at the organization level. Once enabled, any user in the org can connect their individual account. Per-user or per-group connector gating is not currently available.

### Can Claude take write actions—send emails, create files—through connectors?

It depends on the connector: admins should review all connector permissions before adding them. Custom connectors can expose write tools if your MCP server implements them; see the security guidance in Custom Connectors before enabling write scopes.

* * *

Related Articles

[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)[Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)[MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)[MCP: Web Search](https://support.claude.com/en/articles/14503775-mcp-web-search)
