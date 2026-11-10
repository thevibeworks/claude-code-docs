# Connect to Microsoft 365

Connecting Microsoft 365 lets Claude search, analyze, and act on your Outlook email, calendar, and your OneDrive files, plus SharePoint and Teams with a work or school account. Ask Claude for what you need, and it pulls the right information or takes the action.

The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Ultra, Team, and Enterprise. You can connect a personal Microsoft account on Free, Pro, Max, and Ultra plans.

You can connect one Microsoft account at a time. Go to the section for your account:

- **[Work or school account](#h_0fa7577f04)**

- **[Personal account](#h_cffabf2c6c)**

The sections after those two apply to both account types.

## Work or school account

Your company or school gives you this account, which is tied to a Microsoft Entra tenant. It connects SharePoint, OneDrive, Outlook, and Teams. If your admin has enabled write tools, Claude can also draft and send emails, manage calendar events, create and update files, and send Teams messages. If you're not sure whether your account qualifies, check with your IT administrator.

### Before you connect

Before anyone in your organization can connect, an admin needs to set up Microsoft 365. On Team and Enterprise plans, your Claude organization Owner or Primary Owner enables Microsoft 365 for the organization. In every tenant, a Microsoft Entra Global Administrator also needs to grant a one-time consent. For details on the admin side, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)**.

### Connect your account

Once your admin has finished setup:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.

2. Find **Microsoft 365** in the list and click “Add.”

3. Choose “Work or school account,” if you're asked.

4. Sign in with that account when prompted.

**Note:** Once you've connected Microsoft 365 to your Claude account, you can also use it on Claude for iOS and Claude for Android.

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

- Create, update, and delete calendar events, and send invitations to attendees.

- Create and update files in OneDrive and SharePoint.

- Send a Teams chat message, post or reply in a channel, or start a new chat.

When Claude sends an email, it includes a message header identifying it as agent-initiated. Teams messages, file writes, and calendar writes aren't currently tagged. Write tools are subject to per-user limits.

**Note:** Attachments aren't currently supported in write tools. Claude can't send, forward, or draft emails with attachments.

**Note:** On Team and Enterprise plans, your admin can set each Teams write tool separately. If your organization added the Microsoft 365 connector before the Teams write tools launched in September 2026, these tools may be blocked by default until your admin turns them on.

In chat and Cowork, Claude asks you to confirm each time before it sends a chat message or posts or replies in a channel, unless your admin has set the Teams tool for that action to **Always allow** on or after November 9, 2026, or your organization added the Microsoft 365 connector for the first time after November 9, 2026. In those cases, Claude asks by default, and you can choose **Always allow** for the tool if your admin allows it. If you chose **Always allow** for the tool in the past, that earlier choice can take effect right away, so Claude can stop asking you.

On or after December 9, 2026, you can choose **Always allow** for any of these tools your admin sets to **Always allow**.

These exceptions don't apply in organizations that have enabled HIPAA. On Free, Pro, Max, and Ultra plans, Claude asks by default, and you can choose **Always allow** for these tools, as for any other tool. "Automatically approve" mode and scheduled tasks are different: if your admin sets one of these tools to **Always allow**, Claude may use it without asking anyone first. This applies in "Automatically approve" mode and in some scheduled tasks, such as a cloud scheduled task set to "Automatically approve" or a Claude Code routine.

Claude can always search and analyze your data. Your admin decides whether Claude can also take actions like sending email, updating your calendar, creating files, or sending Teams messages. Claude can't change Teams settings or permissions.

For the full list of permissions the integration requests, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)** or the[**Microsoft 365 connector security guide**](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide).

### Disconnect your account

Disconnecting removes Claude's access to your Microsoft 365 data. Reconnecting later doesn't require admin reapproval as long as your admin's consent is still active.

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.

2. Find Microsoft 365 in your connected services.

3. Click “Disconnect.”

### Fix authentication issues

- Confirm you chose “Work or school account,” or sign in with a work or school account if you weren't asked which account to connect. A work or school account can't sign in through “Personal account.”

- Confirm your Microsoft 365 license is active.

- If you're not a Microsoft Entra Global Administrator, check with your admin that tenant-wide consent has been granted for Microsoft 365. Without this, you'll see an error during authentication.

- Your IT team may need to approve third-party app access. If your organization restricts unapproved apps, ask your admin to check organizational policies.

- Try a different browser, or disable ad blockers and privacy extensions that might block authentication popups.

- Clear cookies and cache and try again.

### Frequently asked questions

**Can Claude modify my Microsoft 365 data?**

Only if your admin has enabled write tools. When they're enabled, Claude can draft and send emails, manage calendar events, create and update files, and send Teams messages (a chat message, a post or reply in a channel, or a new chat), always within your existing Microsoft 365 permissions. When they're not enabled, the integration is read-only. Either way, Claude can't change Teams settings or permissions. Attachments also aren't supported in write tools, so Claude can't send, forward, or draft emails with attachments.

**Does Claude search shared drives and team sites?**

Yes. Claude can search any SharePoint sites and shared drives you have permission to access, including team sites, communication sites, document libraries, and shared OneDrive folders.

**Can I point my project at a specific Sharepoint site?**

No, `Sites.Selected` is not supported, so you can't scope the Microsoft 365 connector to an allowlist of specific SharePoint sites. The connector searches across all SharePoint content you already have permission to access.

**Can Claude search shared mailboxes?**

Yes. Claude can search shared mailboxes you have delegate access to in Microsoft 365. This includes full access shared mailboxes and folder-level delegation, such as when you can see only the inbox of another mailbox. Search access follows your existing Microsoft 365 permissions: if you can open a shared mailbox in Outlook, Claude can search it.

**Why don't I see write tools?**

Write tools require extra setup on the admin side: a Microsoft Entra administrator needs to consent to updated permissions, and your organization needs to enable write tools for your account. If you connected before write tools, or the Teams write tools, launched, ask your admin to complete both steps. On or after December 9, 2026, write tools that are still blocked by default will be turned on and set to **Needs approval**, unless your admin has set them, or the whole connector, to **Blocked**. For details, see **[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)**.

**Why does Claude ask me to confirm before it sends or changes something?**

By default, in chat and Cowork, Claude asks you to confirm each time it sends or forwards an email, sends a Teams message, creates, changes, deletes, or responds to a calendar event, or sets an automatic reply. On Free, Pro, Max, and Ultra plans, you can choose **Always allow** for any of these tools, and Claude will then use it without asking you each time.

On Team and Enterprise plans, Claude asks each time for these tools, unless your admin has set that tool to **Always allow** on or after November 9, 2026, or your organization added the Microsoft 365 connector for the first time after November 9, 2026. In those cases, you can choose **Always allow** for the tool if your admin allows it. If you chose **Always allow** for the tool in the past, that earlier choice can take effect right away, so Claude can stop asking you. These exceptions don't apply in organizations that have enabled HIPAA.

"Automatically approve" mode and scheduled tasks are different: if your admin sets one of these tools to Always allow, Claude may use it without asking anyone first. This applies in "Automatically approve" mode and in some scheduled tasks, such as a cloud scheduled task set to "Automatically approve" or a Claude Code routine.

**Can Claude access private Teams channels?**

Only ones you're a member of. Claude mirrors your Microsoft 365 permissions, so if you can see a private channel, Claude can search it; if you're not a member, it can't.

**What if I try to connect before my admin has set things up?**

You'll see an error indicating that an administrator must grant app permissions before you can connect. Ask your organization’s Microsoft Entra Global Administrator to complete consent. If you're on a Team or Enterprise plan, your Claude organization owner also needs to enable Microsoft 365 in organization settings.

---

## Personal account

On Free, Pro, Max, and Ultra plans, you can connect a personal Microsoft account, such as an Outlook.com, Hotmail, Live, or MSN account. It connects Outlook and OneDrive, and Claude can also draft and send emails, manage calendar events, and create and update files. You don't need an admin to set it up. Team and Enterprise plans aren’t shown this option.

### Connect your account

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.

2. Find **Microsoft 365** in the list and click “Connect.”

3. Choose “Personal account.”

4. Sign in with that account when prompted.

**Note:** Choose a personal account in Claude on the web. Once you've connected Microsoft 365 to your Claude account, you can also use it on Claude for iOS and Claude for Android.

### What Claude can do

**OneDrive**

- Access files stored in your OneDrive and have Claude analyze content without manually uploading them.

- Consolidate information from distributed file locations and analyze trends across multiple documents.

**Outlook email**

- Search email threads and conversations to track project status, client feedback, and team alignment.

- Access message content and metadata, filtering by date, sender, subject, and other criteria.

- Find specific information from past correspondence.

**Outlook Calendar**

- Review attendee information and content to prepare for upcoming meetings or catch up on ones you missed.

- Analyze scheduling patterns and track project decisions.

**Write tools**

Write tools are included. Claude can always search and analyze your data, and when you ask, it can also:

- Draft, send, and organize email, including managing categories and moving messages to Deleted Items.

- Create, update, and delete calendar events, and send invitations to attendees.

- Create, update, rename, move, and delete files in OneDrive (deleted files go to the recycle bin).

In chat, Claude asks before it sends, creates, changes, moves, or deletes anything. Searching and reading run without asking. You can change each tool under **Tool permissions**.

Emails Claude sends, forwards, or drafts include a header identifying the emails as agent-initiated. Drafts Claude didn’t create and calendar invitations aren’t tagged. Write tools are subject to per-user limits.

**Note:** Attachments aren't currently supported in write tools, so Claude can't send, forward, or draft emails with attachments.

A personal account doesn't include SharePoint, Teams, meeting summaries, inbox rules, automatic replies, shared mailboxes or calendars, or finding times when other people are free. Claude searches your own OneDrive, including shared items you've added to it.

For the full list of permissions a personal account requests, see **[Personal Microsoft accounts](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide#h_66d5bff0e6)** in the security guide.

### Disconnect your account

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.

2. Find Microsoft 365 in your connected services.

3. Click “Disconnect.”

Disconnecting removes Claude's access, and Claude no longer reads or changes anything in that Microsoft account. The permission you gave Claude stays active in your Microsoft account until you remove it there. Learn more about **[managing apps that have permissions for your Microsoft account](https://account.microsoft.com/privacy/app-access)** (Microsoft sign-in required).

### Fix authentication issues

- Confirm you chose “Personal account.” A personal account can't sign in through “Work or school account.” If you weren't asked which account to connect, Microsoft 365 may already be connected. To switch accounts, disconnect and connect again.

- Try a different browser, or disable ad blockers and privacy extensions that might block authentication popups.

- Clear cookies and cache and try again.

### Frequently asked questions

**Can Claude modify my Microsoft 365 data?**

Only through write tools, which are on unless you turn them off under **Tool permissions**. Attachments aren't supported in write tools, so Claude can't send, forward, or draft emails with attachments.

**Does Claude search shared drives and team sites?**

No. Claude searches your own OneDrive, including shared items you've added to it.

**Why don't I see write tools?**

Check that the tools are on under **Tool permissions**.

---

## Use Microsoft 365 with Claude

Ask Claude a question that needs information from your Microsoft 365 data. Claude detects which tools it needs and retrieves the relevant content.

Example queries:

- "Find the Q4 strategic planning document in SharePoint."

- "Summarize email conversations about the product launch."

- "What discussions happened in the Teams channel about the marketing campaign?"

- "Review meeting notes from last week's leadership sync."

- "Draft a reply to the latest email from the vendor, but don't send it."

- "Schedule a 30-minute sync with the design team next Tuesday."

- "Post a summary of this thread in the #project-updates channel in Teams."

Examples that name SharePoint or Teams need a work or school account.

---

## Supported file types

When reading files from SharePoint and OneDrive, Claude can open these formats:

- **Word, Excel, and PowerPoint**, including older .doc, .xls, and .ppt files

- **PDF**

- **Plain-text files**: .txt, .md, .csv, .tsv, .json, .xml, .html, .htm, and .log

Files in any other format can't be read. They still appear in search results because they're ordinary files in your libraries, but when Claude tries to open one, you'll see a "mime type '...' is not allowed" error.

**Note:** OneNote isn't supported. With a work or school account, notebooks show up in search results, but read attempts return a "mime type 'application/msonenote' is not allowed" error. To bring OneNote content into Claude, export pages or sections to Word or PDF in the same library.

---

## Manage your connection

### Turn individual tools on or off

You can selectively turn off specific tools within Microsoft 365. For example, you might keep document search on but turn off email access. To do this:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.

2. Click on “Microsoft 365.”

3. Toggle the tool on or off under **Tool permissions**.

### Turn the connector on or off per chat

You can also enable or disable Microsoft 365 in a specific conversation.

1. Click the “+” button on the lower left corner of the chat window.

2. Hover over “Connectors.”

3. Find **Microsoft 365** in the list and toggle it on or off.

### Switch accounts

On Free, Pro, Max, and Ultra plans, to switch between a work or school account and a personal account, disconnect and connect again.

---

## What Claude can access

Microsoft 365 stays under your control once connected. A few things to keep in mind:

- **Your permissions apply.** Claude can only access data you can already see in Microsoft 365. If you don't have access to a SharePoint site or aren't a member of a private Teams channel, Claude can't reach that content either.

- **On your request.** Claude accesses Microsoft 365 when you ask, or when a scheduled task you set up needs it.

- **You can disconnect any time.** Use the steps for your account to remove Claude's access.

---

## Troubleshooting

### Claude says it can't find a document I know exists

1. Verify you can access the document directly in Microsoft 365.

2. Make sure the document is in SharePoint or OneDrive, not stored locally on your machine.

3. Recently uploaded files may take time to become searchable.

4. With a work or school account, try specifying the SharePoint site or library name in your prompt.

5. Search by exact file name or unique keywords from the document.

6. If SharePoint’s own search finds a file but Claude doesn’t, ask your Microsoft 365 admin to see **[Claude doesn’t find files that SharePoint search finds](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector#h_cfbc8cb240)**.

### Search results are incomplete or irrelevant

- Be specific about what you're looking for.

- Specify locations, such as site names, date ranges, or document types.

- Use exact phrases for better matching.

- Break complex questions into simpler, more focused ones.

- Double-check spelling of names, projects, or technical terms.

---

## Frequently asked questions

### How do I tell Claude to search a specific place?

Be specific in your prompts:

- *"Search the Engineering team site in SharePoint for architecture documents."*

- *"Find emails from the last week about the Q4 budget."*

- *"Show me Teams discussions with Sarah about the product roadmap."*

- *"Find PowerPoint presentations in SharePoint about sales strategy."*

Prompts that name SharePoint or Teams need a work or school account.

### Why can't Claude read OneNote notebooks?

OneNote isn't currently a supported file type. With a work or school account, notebooks show up in SharePoint search results because they're ordinary files in your libraries, but Claude can't open them, so read attempts return a "mime type 'application/msonenote' is not allowed" error. To work with OneNote content in Claude, export pages or sections to Word or PDF. For the full list of formats Claude can read, see **[Supported file types](#h_90f0c97f12)** above.

### Can Claude search archived emails?

Yes, but only if they're in your primary mailbox. Claude can search every folder in your primary Outlook mailbox, including its Archive folder. Claude doesn't search the separate Online Archive mailbox (also called the In-Place Archive), so messages that a retention policy has moved there won't appear in results. To work with one of those messages, move it back into a folder in your primary mailbox, or open it in Outlook and paste the content into your chat.

### Can Claude summarize long email threads?

Yes. Try a prompt like *"Summarize the email thread about the vendor selection process."* Claude will read the thread and provide a summary with key points and decisions.