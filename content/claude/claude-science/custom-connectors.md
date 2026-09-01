> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom connectors

> Add any Model Context Protocol (MCP) server as a Remote (HTTPS web server) or Local command (program on your computer).

In **Settings > Connectors** > **Add connector**, choose **Remote** or **Local command** and enter a **Name** (lowercase letters, digits, hyphens). For **Remote**, enter the server URL; **Advanced settings** covers transport (**SSE** or **Streamable HTTP**), OAuth client settings, and the **Headers helper command**. For **Local command**, enter the command; **Advanced settings** covers arguments and environment variables. **Browse Connectors Directory** opens the public directory.

Remote servers that need login take you through the provider's sign-in page.

On Team and Enterprise plans, you can add and use custom connectors only if your organization allows them. When it doesn't, the **Remote** and **Local command** options under **Add connector** are grayed with a note that custom connectors are disabled by your admin. Custom connectors you added earlier stay listed and grayed, Claude can't use them, and they work again if your organization turns custom connectors back on. See [Custom connectors](/docs/claude-science/admin-controls#custom-connectors) in the admin controls.

Every tool from a custom connector starts at **Ask each time**. On the connector's page, set individual tools to **Always allow** or **Block** under **Tools**, or turn on Skip approvals for the whole connector.

<Warning>
  Skip approvals disables the per-call card for every tool on that connector. Only use connectors from developers you trust.
</Warning>

Local-command connectors run inside the sandbox with the same network limits as Claude's code and a per-connector writable directory. Environment variables for local connectors are saved unencrypted in a configuration file readable by your account only; don't put high-value secrets there.
