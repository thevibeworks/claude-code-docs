# MCP: Individual connectors

Your organization can register its own MCP servers in Claude for Government, letting Claude connect to internal systems, custom tools, or third-party services you've approved for your environment.

**Custom connectors work the same way in Claude for Government as in Claude Enterprise.** The prerequisites, the registration flow, and the behavior once enabled are identical. For full setup instructions, see **[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**. This page covers only what's different.

For general guidance on building and deploying MCP servers, see **[modelcontextprotocol.io](https://modelcontextprotocol.io/)** and the **[commercial connector guide](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**.

## How custom connectors differ for Claude for Government

**Adding a connector does not trigger a new FedRAMP review**

MCP was authorized as a **feature** in Claude for Government's FedRAMP High package. The infrastructure that registers, authenticates, and executes your connector—including encrypted token storage, per-user OAuth, and audit logging—is already covered. You can add new custom connectors without re-engaging Anthropic's FedRAMP audit process.

**Important:** This applies to Claude for Government's authorization only. Your agency's own ATO process may still require you to evaluate the MCP server and any backing services it reaches before enabling them. Anthropic does not review, authorize, or assume responsibility for customer-registered MCP servers or the external systems they call.

## Register custom connectors

Navigate to **claude.fedstart.com/admin-settings/connectors** as an **Owner** or **Primary Owner**. The rest of the flow matches the **[commercial guide](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**.

Once added, the connector appears in your users' settings exactly as Anthropic-provided connectors do.

## Know where the FedRAMP boundary sits

When a user invokes a tool from your custom connector:

User → Claude → MCP proxy → Your MCP server → Your backing service

└──── inside FedRAMP High ────┘ └─your responsibility─┘

Claude, the MCP proxy, and all OAuth token storage stay inside the FedRAMP High authorized environment. Whether your MCP server and its backing service sit inside or outside that boundary is under your control and yours to evaluate against the data classifications your users will handle.

**Prefer FedRAMP-authorized backing services.** If your connector talks to a SaaS product, check whether that product has a government-cloud offering—Atlassian Government Cloud, Salesforce Government Cloud, ServiceNow GCC—and point the connector there rather than at the commercial endpoint.