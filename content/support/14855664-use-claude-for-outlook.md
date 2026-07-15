# Use Claude for Outlook

Claude for Outlook is an add-in that integrates Claude into your Outlook inbox and calendar. It’s designed for professionals who live in email, including private equity and investment banking associates managing deal flow, in-house legal teams running counterparty negotiations, and consultants juggling client threads.

Claude for Outlook is currently in beta and available to Pro, Max, Team, and Enterprise plans.

With Claude for Outlook, you can:

- Triage your unread inbox into what needs you, what Claude can handle, and what's noise.

- Draft replies, reply-alls, and forwards in your voice, landed unsent in Outlook's compose pane.

- Summarize long threads into decisions made, open items, and who owes what, with per-email citations.

- Read .docx, .xlsx, .pptx, and .pdf attachments inline without opening them.

- Find meeting times across attendees and draft invites into Outlook's native appointment form.

- Prep for your next meeting with a one-page brief of recent threads and attached documents.

---

## Get started with Claude for Outlook

### Supported versions

- Outlook on the web

- Outlook on Windows (new Outlook and classic Outlook, Microsoft 365 subscription)

- Outlook on Mac (Microsoft 365 subscription)

### For individuals

1. Navigate to the **[Claude for Outlook listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010724?tab=Overview)**.

2. Click “Get it now” to install the add-in.

3. Open Outlook, open any email, click the Claude button in the ribbon, and sign in with your Claude account.

### For admins

**Deploy Claude for Outlook to your organization:**

1. Visit the **[Microsoft 365 Admin Center](https://admin.microsoft.com/)**.

2. Navigate to **Settings > Integrated apps > Add-ins**.

3. Search for “Claude by Anthropic for Outlook” in Microsoft AppSource.

4. Deploy the add-in to your organization or specific people.

5. Share these instructions with your team: **[Microsoft’s deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide)**.

After installation, team members can open Outlook, open any email, click the Claude button in the message ribbon, sign in with their Claude credentials, and start working with their inbox. Pin the task pane so it stays open as you move between messages.

**Important:** Claude for Outlook uses Microsoft Graph to read across your mailbox and calendar. Before users can use features that span the inbox (triage, search, find time), an IT administrator must grant admin consent for the Mail.ReadWrite, Calendars.Read, People.Read, User.Read, and offline_access delegated scopes using the admin consent URL provided in your onboarding materials. This is a one-time step per tenant.

**### Alternatively, download the manifest file to install**

For IT administrators deploying to multiple people:

**Step 1: Obtain the custom manifest**

1. Click **[this link](https://pivot.claude.ai/manifest-outlook.xml)** to download the custom manifest XML file.

2. Save this file to a secure location.

**Step 2: Access Microsoft 365 Admin Center**

1. Navigate to **<https://admin.microsoft.com>**

2. Sign in with your admin credentials.

3. Go to **Settings > Integrated apps**.

**Step 3: Upload the custom add-in**

1. Click “Upload custom apps.”

2. Select “Office Add-in.”

3. Choose “I have a manifest file on this device.”

4. Browse and select the Claude for Outlook manifest XML file.

5. Click “Upload.”

**Step 4: Assign people**

Choose your deployment scope:

- **Entire organization:** All people get access

- **Specific users:** Enter individual email addresses

- **Specific groups:** Select security groups or distribution lists

- **Just yourself:** For admin testing only

**Step 5: Deploy**

1. Review deployment settings.

2. Click “Deploy.”

3. The add-in will be available within minutes (may take up to 24 hours for full organization rollout).

**Step 6: Grant Microsoft Graph Consent**

Claude for Outlook reads mail and calendar data through Microsoft Graph, which requires a one-time tenant-wide grant from a Global Administrator. This is separate from the Integrated apps deployment above. Have a Global Admin open the below admin consent link below in a browser where they are signed in to your Microsoft 365 tenant:

<https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/People.Read%20https://graph.microsoft.com/User.Read%20offline_access&redirect_uri=https://pivot.claude.ai/auth/callback>

- The admin will see a Microsoft permissions screen listing Mail.ReadWrite, Calendars.Read, People.Read, User.Read, and offline_access

- After they click Accept, all users in the organization can use Claude for Outlook without additional Microsoft prompts. This grant takes effect immediately; only the add-in rollout in Step 5 above can take up to 24 hours.

- If this step is skipped, every user will see a “Need admin approval” message when Claude first tries to read mail or calendar data

**Step 7: Access**

- People will see Claude appear in the Outlook message ribbon when an email is open.

- First-time people will need to sign in with their Claude accounts.

- No additional installation required.

### Connect through an LLM gateway

If your organization routes API traffic through an internal LLM gateway connected to Google Cloud Vertex AI or Microsoft Azure, you can use the add-in without a Claude account. This is the same gateway pattern used by Claude Code.

For setup instructions and gateway requirements, see **[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233)**.

---

## Key features

### Triage your inbox

Ask Claude what needs your attention. Claude reads your unread mail and attachments and sorts them into three buckets: actions items for you (each with a one-line reason), items Claude can handle (scheduling asks, acknowledgments, standard-form documents, pre-drafted for your review), and noise you can archive in one click.

**Example prompts:**

- “What needs me?”

- “Draft replies for everything you can handle”

- “Archive all the calendar responses and newsletters”

### Draft replies in your voice

Tell Claude what you want to say and it drafts the reply into Outlook’s native compose pane, unsent. Tone is learned from your sent folder, so the draft matches your sentence length, sign-off, and formality register. Reply versus reply-all is chosen deliberately, and Claude warns before adding anyone who wasn’t on the thread.

**Example prompts:**

- “Reply to this and agree to the extension, push back on the fee”

- “Reply-all thanking everyone and confirming Thursday works”

- “Forward this to Dana with a two-line summary”

### Summarize long threads

Claude reads the entire conversation, including every reply and forward, and tells you what’s been decided, what’s still open, and who owes what. Every claim cites the specific email it came from, and clicking a citation opens that message in Outlook.

**Example prompts:**

- “What’s been decided and what’s still open?”

- “Who owes what on this thread?”

### Read attachments inline

Claude reads .docx, .xlsx, .pptx, and .pdf attachments on the open email without you opening them, including tracked changes inside Word files. Ask what changed in an attached LOI, what the attached deck argues, or what numbers are in the attached model.

**Example prompts:**

- “What changed in the attached LOI?”

- “Summarize the attached deck”

### Search your mailbox

Ask Claude to find a past conversation by topic, not just keywords. Results come back as clickable citations that open the source message in Outlook, so you can verify every answer against the original email.

**Example prompts:**

- “When did we last discuss the cap with Fernwood?”

- “Find the email where Dana sent the revised term sheet”

### Find time and create events

Claude checks free/busy for everyone whose calendar you can see and proposes slots that respect working hours and existing holds. The invite is drafted into Outlook’s native appointment form with attendees, subject, and agenda for you to review and send.

**Example prompts:**

- “Find 30 minutes with Dana and the Fernwood team next week”

- “Block Thursday afternoon for deep work”

### Prep for meetings

For your next event, Claude pulls the last thread with each attendee and any attached documents into a one-page brief, so you walk in knowing the open items and what each person last said.

**Example prompts:**

- “Prep me for my 2pm”

- “What’s open with Dana before our call?”

## Work across Outlook, Word, Excel, and PowerPoint

Claude for Outlook shares context with Claude for Word, Excel, and PowerPoint, so Claude can work across your open Office apps in a single conversation. For example, you can open an attached LOI in Word with the email thread already loaded as context, or pull numbers from an email into an open Excel model, without copying and pasting between apps.

For setup instructions, see **[Work across Microsoft 365 apps](https://support.claude.com/en/articles/13892150)**.

---

## Context and session management

### Auto-compaction

We **[automatically compact longer conversations](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits#h_21b66a43b4)** into new conversations to avoid running out of context.

### Chat history

Chat history is stored locally in your browser using IndexedDB. Unlike Claude, conversations aren't stored on Anthropic's servers—they're saved client-side and aren't synced across devices or browsers. You can clear all chat history from Settings at any time, and the local store is cleared when you clear your browser data. Your chat history is specific to the combination of the add-in surface, your user ID, and your organization ID—so your Excel and Outlook histories are separate, for example, but conversations carry across different workbooks within Excel (or different emails within Outlook). If you switch organizations, you'll have a separate chat history.

### Overwrite protection

To avoid accidental data loss, Claude warns you before overwriting existing data.

**Note:** Your use of Claude for Outlook is associated with your existing Claude account and is subject to the same usage limits.

---

## Current limitations

For Claude for Outlook use, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**

Enterprise organizations can route full audit telemetry from Claude for Outlook to their own OpenTelemetry (OTEL) collector for integration with a SIEM or observability platform. Learn more about **[configuring a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents)**. On Free, Pro, Max, and Team plans, observability and auditability aren't available for Claude for Outlook. Claude for Outlook doesn’t inherit custom data retention settings your organization might have set, and isn’t included in Enterprise audit logs or the Compliance API at this time.

As a beta feature, Claude for Outlook is **not recommended** for:

- Unattended sending. Claude never sends mail or invites on its own; every draft lands unsent for you to review.

- Client-facing or counterparty correspondence without reading the draft first.

- Replacing your judgment on which emails matter or how to handle a relationship.

- Mailboxes containing privileged or regulated data without appropriate organizational controls.

## Unsupported versions

- Outlook 2016 / 2019 (perpetual/volume licensed)

- Outlook on iOS

- Outlook on Android

- Exchange on-premises mailboxes (Exchange Online / Microsoft 365 only)

---

## Best practices

To use Claude for Outlook safely and effectively:

- Always review drafted replies and invites before sending, especially recipient lists.

- Verify thread summaries against the cited source emails for high-stakes conversations.

- Use appropriate Microsoft 365 permissions and conditional access policies for the add-in.

- Maintain human oversight for anything leaving your organization.

---

## Prompt injection attack risks

Be cautious with emails from external or untrusted senders. Email bodies and attachments are untrusted input and may contain instructions intended to manipulate Claude rather than you.

An important risk for those using Claude for Outlook and other AI tools that can read and act on email is prompt injection: malicious instructions hidden in an email body, signature, or attachment that try to trick the AI into taking unintended actions. For example, a seemingly routine inbound email might contain hidden text instructing Claude to forward a thread or draft a reply you didn’t ask for. Claude may interpret these instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude for Outlook can be manipulated to:

- **Extract and share sensitive information** with bad actors through web searches containing your sensitive data or file system access that exposes proprietary information.

- **Draft replies or take inbox actions that you didn't intend.**

- **Archive, move, or flag messages in ways you didn't ask for (should you allow Claude to act without reviewing**), exploiting Claude’s helpful nature to delete or alter important content.

While we continue to develop our offerings and improve safety measures to reduce these risks, you should exercise caution when using Claude for Outlook and should review every draft and inbox action when working with email from external, untrusted senders.

---

## Example use cases

### Morning inbox triage

- “What needs me this morning?”

- “Draft replies for the eight you can handle”

- “Archive all the calendar responses”

- “Flag anything from the Fernwood team for follow-up”

- “Mark everything from this distro as read”

### Deal and matter correspondence

- “Summarize this thread: what’s decided and what’s open?”

- “What changed in the attached LOI versus the version they sent last week?”

- “Reply agreeing to the extension but pushing back on the fee”

- “Open the attached model in Excel with this thread as context”

### Scheduling

- “Find 30 minutes with Dana and my associate this week”

- “Propose three slots for the Fernwood call next week”

- “Accept the 3pm and decline the conflicting 3:30”

- “Add an agenda to my Thursday team meeting”

### Meeting prep

- “Prep me for my 2pm with the Fernwood team”

- “What’s the Teams link for my next call?”

- “What’s open with each attendee before this meeting?”

- “Summarize the last three threads with Dana”

---

## Frequently asked questions

### Does Claude send email or calendar invites on my behalf?

No. Claude drafts replies and invites into Outlook’s native compose and appointment forms, and you click send. The add-in does not request the Mail.Send permission at Beta, so there is no programmatic outbound sending.

### What Microsoft Graph permissions does Claude for Outlook need?

Claude for Outlook requests Mail.ReadWrite, Calendars.Read, People.Read, User.Read, and offline_access as delegated scopes. Your IT admin grants these once via an admin consent URL; the Graph access token stays in the browser’s MSAL cache and is never sent to Anthropic.

### What happens to my chat history?

Currently, chat history isn’t saved between sessions. Each time you open the add-in, you start a fresh conversation with Claude.

### How does Claude access my mailbox?

Claude reads the email or event you have open via Office.js, and uses Microsoft Graph for anything spanning your mailbox or calendar (thread retrieval, search, free/busy, move and flag operations). Anthropic does not store a copy of your mailbox; content is fetched on demand and not persisted server-side.

### What if Claude drafts something wrong?

Every draft lands unsent in Outlook’s compose pane. Edit it, discard it, or ask Claude to try again. Nothing goes out until you click send. For inbox actions like archive or move, you can undo using Outlook’s standard undo.

### Does Claude work with shared or delegate mailboxes?

Claude can read mail in shared mailboxes you have delegate access to. Acting on a shared mailbox follows the same review-before-send flow.