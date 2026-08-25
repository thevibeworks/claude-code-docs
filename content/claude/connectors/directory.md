> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors directory

> Browse verified and community MCP integrations for Claude

The Connectors Directory is a catalog of [MCP](/docs/connectors/building/mcp) servers that work across all Claude products — Claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Cowork.

The directory contains both verified connectors and community connectors. Verified connectors have been tested by Anthropic for quality and compatibility and met the Software Directory Policy requirements at the time of review, though verification is not a security audit. Anthropic screens community connectors before listing but does not review them in depth. The label reflects the level of review each connector received, not how it works: once connected, a community connector has the same capabilities and access as any connector you grant. See [connector verification](/docs/connectors/verification) to learn what each label means.

<Note>
  All connectors in the directory are subject to the [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) and the [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms).
</Note>

## How the directory works

* The same catalog serves Claude.ai, Cowork, Desktop, mobile, and Claude Code.
* Directory connectors are eligible for **Suggested Connectors**—in-chat recommendations when relevant to the user's task. Every directory entry is included automatically.
* Ranking is usage-based, similar to other app stores.
* No domain-ownership proof (DNS or `.well-known`) is required—that requirement applies only to the open MCP Registry, not the Anthropic Directory.
* The help-docs link shown in the in-product connector setup flow is not partner-customizable.

Directory connectors and custom connectors run on the same infrastructure—see [directory vs custom](/docs/connectors/building/directory-vs-custom).

## Browsing the directory

Access the Connectors Directory through:

* **[Customize > Connectors](https://claude.ai/customize/connectors)** in claude.ai
* **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** for Team/Enterprise admins

## Requesting a connector on a Team plan

On Claude Team plans, members who do not have permission to enable connectors see a **Request** button on each directory connector instead of a connect action. Selecting **Request** sends the connector to your organization's admins for review. The button changes to **Requested** while the request is pending.

If you are a Team admin with permission to manage connectors, member requests appear in two places:

* **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** shows a **Requested by your team** section above the connector list.
* **[Organization settings > Notifications](https://claude.ai/admin-settings/notifications)** lists each requested connector on the **Requests** tab, and the **Notifications** item in the admin sidebar shows a count badge while requests are pending.

From either location you can enable the connector for your organization or dismiss the request. Claude shows the requesting member the outcome the next time they open the connectors directory.

## When a connector's endpoint changes

Occasionally a provider updates the endpoint URL behind its directory listing, for example moving a server from `https://mcp.example.com/sse` to `https://mcp.example.com/mcp`. This is a routine change on the provider's side. Here is what you may notice in Claude:

* **Your existing connection keeps working.** Connectors you added before the change keep using the endpoint they were installed with, and your authentication is unaffected.
* **It appears as a custom connector.** Because your connector no longer matches the updated directory listing, it shows under "Custom" in [Customize > Connectors](https://claude.ai/customize/connectors) instead of as a named directory connector.
* **The directory listing shows as not installed.** Adding the connector from the directory again without removing the original gives you two connections: your original one and a new one on the updated endpoint.

To move to the new endpoint, remove the connector and re-add it from the directory. Claude prompts you to authenticate with the service again.

## Submitting to the directory

Organizations can submit their MCP servers for review and inclusion in the directory:

1. Review the [submission guidelines](/docs/connectors/building/submission)
2. Ensure your server meets security and compatibility standards
3. Submit through the [submission portal](https://claude.ai/admin-settings/directory/submissions/new) in Claude.ai admin settings

Submitting requires a Team or Enterprise organization and directory management access (organization Owners by default); see [Before you start](/docs/connectors/building/submission#before-you-start). After publication, the same dashboard shows your server's health and usage; see [Managing your listing](/docs/connectors/building/managing-your-listing).

## Related topics

<Card title="Build a connector" icon="code" href="/docs/connectors/building/index">
  Create your own MCP server.
</Card>
