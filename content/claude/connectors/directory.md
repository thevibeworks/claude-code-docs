> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors directory

> Browse verified and community MCP connectors in the Connectors Directory, one catalog for claude.ai, Claude Desktop, mobile, Claude Code, and Cowork

The Connectors Directory is a catalog of [MCP](/docs/connectors/building/mcp) servers that work across all Claude products: claude.ai, Claude Desktop, Claude Mobile, Claude Code, and Cowork.

The directory contains both verified connectors and community connectors. Verification isn't a security audit. [Connector verification](/docs/connectors/verification) explains what each label means.

<Note>
  All connectors in the directory are subject to the [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) and the [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms).
</Note>

## Understand how the directory works

* The same catalog serves claude.ai, Cowork, Desktop, mobile, and Claude Code
* Directory connectors are eligible for **Suggested Connectors**, which are in-chat recommendations shown when relevant to the user's task. Every directory entry is included automatically
* Ranking is usage-based, similar to other app stores
* No domain-ownership proof (DNS or `.well-known`) is required. That requirement applies only to the open MCP Registry, not the Anthropic Directory
* The help-docs link shown in the in-product connector setup flow is not partner-customizable

Directory connectors and custom connectors run on the same infrastructure. See [directory vs custom](/docs/connectors/building/directory-vs-custom).

## Browse the directory

Access the Connectors Directory through:

* **[Customize > Connectors](https://claude.ai/customize/connectors)** in claude.ai
* **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** for Team and Enterprise Owners

On Team and Enterprise plans, an Owner adds a connector for the organization, and members then connect with their own account. On Enterprise plans, a member whose custom role includes managing the organization's libraries can add one too.

## Request a connector on a Team plan

On Claude Team plans, members who do not have permission to enable connectors see a **Request** button on each directory connector instead of a connect action. Selecting **Request** sends the request to your organization's Owners. The button changes to **Requested** while the request is pending.

If you are an Owner on a Team plan, member requests appear in two places:

* **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** shows a **Requested by your team** section above the connector list
* **[Organization settings > Notifications](https://claude.ai/admin-settings/notifications)** lists each requested connector on the **Requests** tab, and the **Notifications** item in the admin sidebar shows a count badge while requests are pending

From either location you can enable the connector for your organization or dismiss the request. Claude shows the requesting member the outcome the next time they open the connectors directory.

## Recognize when a connector's endpoint changes

Occasionally a provider updates the endpoint URL behind its directory listing, for example moving a server from `https://mcp.example.com/sse` to `https://mcp.example.com/mcp`. This is a routine change on the provider's side. Here is what you may notice in Claude:

* **Your existing connection keeps working.** Connectors you added before the change keep using the endpoint they were installed with, and your authentication is unaffected
* **It appears as a custom connector.** Because your connector no longer matches the updated directory listing, it shows under **Custom** in **[Customize > Connectors](https://claude.ai/customize/connectors)** instead of as a named directory connector
* **The directory listing shows as not installed.** Adding the connector from the directory again without removing the original gives you two connections: your original one and a new one on the updated endpoint

To move to the new endpoint, remove the connector and re-add it from the directory. Claude prompts you to authenticate with the service again.

## Submit to the directory

Organizations can submit their MCP servers for review and inclusion in the directory:

<Steps>
  <Step title="Review the submission guidelines">
    Review the [submission guidelines](/docs/connectors/building/submission).
  </Step>

  <Step title="Meet the standards">
    Ensure your server meets security and compatibility standards.
  </Step>

  <Step title="Submit in the developer portal">
    Submit through the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage).
  </Step>
</Steps>

Anyone on a paid Claude plan can submit, and on Team and Enterprise an Owner submits; see [who can submit to the directory](/docs/directory/publish#confirm-you-can-submit-to-the-directory) for the role and organization requirements. After publication, the same dashboard shows your server's health and usage; see [Manage your directory listing](/docs/connectors/building/managing-your-listing).

## Next steps

* [Connector verification](/docs/connectors/verification): what the Verified and Community labels mean
* [Get started with connectors](/docs/connectors/getting-started): set up a connector and use it in conversations
* [Build an MCP server for Claude](/docs/connectors/building/index): create your own MCP server
