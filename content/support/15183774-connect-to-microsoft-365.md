Title: Connect to Microsoft 365

URL Source: https://support.claude.com/en/articles/15183774-connect-to-microsoft-365

Markdown Content:
Connecting Microsoft 365 lets Claude search and analyze content across SharePoint, OneDrive, Outlook, and Teams in your work account. Ask a question that needs information from your work data, and Claude pulls what it needs to answer.

## Before you connect

You'll need a work Microsoft 365 account tied to a Microsoft Entra tenant. Personal Microsoft accounts (such as @outlook.com, @hotmail.com, or @live.com) can't be used. If you're not sure whether your account qualifies, check with your IT administrator.

## Connect Microsoft 365

Once your admin has finished setup:

## Use Microsoft 365 with Claude

Ask Claude a question that needs information from your Microsoft 365 data. Claude detects which tools it needs and retrieves the relevant content.

### Example queries

### What Claude can do

**SharePoint and OneDrive**

**Outlook email**

**Outlook Calendar**

**Teams**

## Manage your connection

### Turn individual tools on or off

You can selectively turn off specific tools within Microsoft 365—for example, you might keep document search on but turn off email access. To do this:

### Turn the connector on or off per chat

You can also enable or disable Microsoft 365 in a specific conversation.

### Disconnect Microsoft 365

Disconnecting removes Claude's access to your Microsoft 365 data. Reconnecting later doesn't require admin reapproval as long as your admin's consent is still active.

## What Claude can access

Microsoft 365 stays under your control once connected. A few things to keep in mind:

## Troubleshooting

### Authentication is failing

### Claude says it can't find a document I know exists

### Search results are incomplete or irrelevant

## Frequently asked questions

### Can Claude modify my Microsoft 365 data?

No. The integration is read-only. Claude can search and analyze your data but can't:

### Does Claude search shared drives and team sites?

Yes. Claude can search any SharePoint sites and shared drives you have permission to access, including team sites, communication sites, document libraries, and shared OneDrive folders.

### How do I tell Claude to search a specific place?

Be specific in your prompts:

### Can I point my project at a specific Sharepoint site?

No, `Sites.Selected` is not supported, so you can't scope the Microsoft 365 connector to an allowlist of specific SharePoint sites. The connector searches across all SharePoint content you already have permission to access.

### Can Claude search shared mailboxes?

Yes. Claude can search shared mailboxes you have delegate access to in Microsoft 365. This includes full access shared mailboxes and folder-level delegation, such as when you can see only the inbox of another mailbox. Access is read-only and follows your existing Microsoft 365 permissions: if you can open a shared mailbox in Outlook, Claude can search it.

### Can Claude search archived emails?

Yes. Claude can search any email you have access to in Outlook, including archived messages.

### Can Claude summarize long email threads?

Yes. Try a prompt like _"Summarize the email thread about the vendor selection process."_ Claude will read the thread and provide a summary with key points and decisions.

### Can Claude access private Teams channels?

Only ones you're a member of. Claude mirrors your Microsoft 365 permissions, so if you can see a private channel, Claude can search it; if you're not a member, it can't.

### What if I try to connect before my admin has set things up?

You'll see an error indicating that an administrator must grant app permissions before you can connect. Ask your organization’s Microsoft Entra Global Administrator to complete consent. If you're on a Team or Enterprise plan, your Claude organization owner also needs to enable Microsoft 365 in organization settings.

* * *

Related Articles

[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)[Work across Microsoft 365 apps](https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
