# Connect to Microsoft 365

Connecting Microsoft 365 lets Claude search and analyze content across SharePoint, OneDrive, Outlook, and Teams in your work account. If your admin has enabled write tools, Claude can also draft and send emails, manage calendar events, and create and update files. Ask Claude for what you need, and it pulls the right information or takes the action.

The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

## Before you connect

You'll need a work Microsoft 365 account tied to a Microsoft Entra tenant. Personal Microsoft accounts (such as @outlook.com, @hotmail.com, or @live.com) can't be used. If you're not sure whether your account qualifies, check with your IT administrator.

**Important:** Before anyone in your organization can connect Microsoft 365, an admin needs to set it up. On Team and Enterprise plans, your Claude organization Owner enables Microsoft 365 for the organization. In every tenant, a Microsoft Entra Global Administrator also needs to grant a one-time consent. For details on the admin side, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-)**.

## Connect Microsoft 365

Once your admin has finished setup:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.

2. Find **Microsoft 365** in the list and click “Connect.”

3. Sign in with your Microsoft 365 credentials when prompted.

**Note:** Once you've connected Microsoft 365 to your Claude account, you can also use it on Claude for iOS and Claude for Android.

## Use Microsoft 365 with Claude

Ask Claude a question that needs information from your Microsoft 365 data. Claude detects which tools it needs and retrieves the relevant content.

### Example queries

- "Find the Q4 strategic planning document in SharePoint."

- "Summarize email conversations about the product launch."

- "What discussions happened in the Teams channel about the marketing campaign?"

- "Review meeting notes from last week's leadership sync."

- "Draft a reply to the latest email from the vendor, but don't send it."

- "Schedule a 30-minute sync with the design team next Tuesday."

### What Claude can do

**SharePoint and OneDrive**

- Search documents across SharePoint sites and libraries to locate project specifications, strategic plans, and other business documents.

- Access files stored in your OneDrive and have Claude analyze content without manually uploading them.

- Consolidate information from distributed file locations and analyze trends across multiple documents.

**Outlook email**

- Search email threads and conversations to track project status, client feedback, and team alignment.

- Access message content and metadata, filtering by date, sender, subject, and other criteria.

- Find specific information from past correspondence.

**Outlook Calendar**

- Review meeting summaries, attendee information, and content to prepare for upcoming meetings or catch up on ones you missed.

- Analyze scheduling patterns and track project decisions.

**Teams**

- Access Teams chat messages and channel discussions where you're a participant.

- Review team collaboration patterns and find decisions made across conversations.

**Write tools**

If your admin has enabled write tools for your organization, Claude can also:

- Draft, send, and organize email, including managing categories, inbox rules, and automatic replies.

- Create, update, and delete calendar events.

- Create and update files in OneDrive and SharePoint.

When Claude sends an email, it includes a message header identifying it as agent-initiated in your mail and file history. Write tools are subject to per-user limits.

**Note:** Attachments aren't currently supported in write tools—Claude can't send, forward, or draft emails with attachments.

## Manage your connection

### Turn individual tools on or off

You can selectively turn off specific tools within Microsoft 365—for example, you might keep document search on but turn off email access. To do this:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.

2. Click on “Microsoft 365.”

3. Toggle the tool on or off under **Tool permissions**.

### Turn the connector on or off per chat

You can also enable or disable Microsoft 365 in a specific conversation.

1. Click the “+” button on the lower left corner of the chat window.

2. Hover over “Connectors.”

3. Find **Microsoft 365** in the list and toggle it on or off.

### Disconnect Microsoft 365

Disconnecting removes Claude's access to your Microsoft 365 data. Reconnecting later doesn't require admin reapproval as long as your admin's consent is still active.

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.

2. Find Microsoft 365 in your connected services.

3. Click “Disconnect.”

## What Claude can access

Microsoft 365 stays under your control once connected. A few things to keep in mind:

- **Your permissions apply.** Claude can only access data you can already see in Microsoft 365. If you don't have access to a SharePoint site or aren't a member of a private Teams channel, Claude can't reach that content either.

- **On-demand only.** Claude only accesses Microsoft 365 when you ask a question that needs it. It doesn't run background searches.

- **Write tools are admin-controlled.** Claude can always search and analyze your data. Whether Claude can also take actions like sending email, updating your calendar, or creating files depends on what your admin has enabled. Claude can't post Teams messages or change Teams settings.

- **You can disconnect any time.** Use the steps above to remove Claude's access.

For the full list of permissions the integration requests, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-)** or the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-)**.

---

## Troubleshooting

### Authentication is failing

1. Confirm you're using a Microsoft 365 work account tied to a Microsoft Entra tenant. Personal Microsoft accounts (@outlook.com, @hotmail.com, @live.com) aren't supported.

2. Confirm your Microsoft 365 license is active.

3. If you're not a Microsoft Entra Global Administrator, check with your admin that tenant-wide consent has been granted for Microsoft 365. Without this, you'll see an error during authentication.

4. Your IT team may need to approve third-party app access. If your organization restricts unapproved apps, ask your admin to check organizational policies.

5. Try a different browser, or disable ad blockers and privacy extensions that might block authentication popups.

6. Clear cookies and cache and try again.

### Claude says it can't find a document I know exists

1. Verify you can access the document directly in Microsoft 365.

2. Make sure the document is in SharePoint or OneDrive, not stored locally on your machine.

3. Recently uploaded files may take time to become searchable.

4. Try specifying the SharePoint site or library name in your prompt.

5. Search by exact file name or unique keywords from the document.

### Search results are incomplete or irrelevant

- Be specific about what you're looking for.

- Specify locations, such as site names, date ranges, or document types.

- Use exact phrases for better matching.

- Break complex questions into simpler, more focused ones.

- Double-check spelling of names, projects, or technical terms.

---

## Frequently asked questions

### Can Claude modify my Microsoft 365 data?

Only if your admin has enabled write tools. When they're enabled, Claude can draft and send emails, manage calendar events, and create and update files, always within your existing Microsoft 365 permissions. When they're not enabled, the integration is read-only. Either way, Claude can't post Teams messages or change Teams settings or permissions. Attachments also aren’t supported in write tools, so Claude can’t send, forward, or draft emails with attachments.

### Does Claude search shared drives and team sites?

Yes. Claude can search any SharePoint sites and shared drives you have permission to access, including team sites, communication sites, document libraries, and shared OneDrive folders.

### How do I tell Claude to search a specific place?

Be specific in your prompts:

- *"Search the Engineering team site in SharePoint for architecture documents."*

- *"Find emails from the last week about the Q4 budget."*

- *"Show me Teams discussions with Sarah about the product roadmap."*

- *"Find PowerPoint presentations in SharePoint about sales strategy."*

### Can I point my project at a specific Sharepoint site?

No, `Sites.Selected` is not supported, so you can't scope the Microsoft 365 connector to an allowlist of specific SharePoint sites. The connector searches across all SharePoint content you already have permission to access.

### Can Claude search shared mailboxes?

Yes. Claude can search shared mailboxes you have delegate access to in Microsoft 365. This includes full access shared mailboxes and folder-level delegation, such as when you can see only the inbox of another mailbox. Search access follows your existing Microsoft 365 permissions: if you can open a shared mailbox in Outlook, Claude can search it.

### Can Claude search archived emails?

Yes. Claude can search any email you have access to in Outlook, including archived messages.

### Can Claude summarize long email threads?

Yes. Try a prompt like *"Summarize the email thread about the vendor selection process."* Claude will read the thread and provide a summary with key points and decisions.

### Why don't I see write tools?

Write tools require extra setup on the admin side: a Microsoft Entra administrator needs to consent to updated permissions, and your organization needs to enable write tools for your account. If you connected before write tools launched, ask your admin to complete both steps. For details, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951)**.

### Can Claude access private Teams channels?

Only ones you're a member of. Claude mirrors your Microsoft 365 permissions, so if you can see a private channel, Claude can search it; if you're not a member, it can't.

### What if I try to connect before my admin has set things up?

You'll see an error indicating that an administrator must grant app permissions before you can connect. Ask your organization’s Microsoft Entra Global Administrator to complete consent. If you're on a Team or Enterprise plan, your Claude organization owner also needs to enable Microsoft 365 in organization settings.