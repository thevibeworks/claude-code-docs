> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude for Outlook

> An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.

> [!WARNING]
>
> After the September and October 2026 Microsoft 365 updates on Windows, some
> users are missing their chat history and uploaded skills in the Claude add-in.
> Anthropic is working with Microsoft to solve this issue. In the meantime, see
> [what you and your IT team can do](https://claude.com/docs/office-agents/data-storage.md#chat-history-and-skills-missing-after-a-microsoft-365-update-on-windows).

Claude for Outlook is an add-in that brings Claude into your Outlook inbox
and calendar. It is built for professionals whose work runs through email,
including private equity and investment banking associates managing deal
flow, in-house legal teams running counterparty negotiations, and
consultants tracking multiple client threads.

> [!NOTE]
>
> Claude for Outlook is currently in beta and available to Pro, Max, Team,
> and Enterprise plans.
> It is not available on the Free plan. If you connect through a
> [third-party platform](#connect-through-a-third-party-platform), you can use
> the add-in without a Claude account.

## What you can do

With Claude for Outlook, you can:

* Triage your unread inbox into what needs you, what Claude can handle,
  and what is noise.
* Draft replies, reply-alls, and forwards, in your voice if you let Claude
  learn it, landed unsent in Outlook's compose pane.
* Summarize long threads into decisions made, open items, and who owes
  what, with per-email citations.
* Read `.docx` and `.xlsx` attachments inline without opening them.
* Find meeting times across attendees and draft invites into Outlook's
  native appointment form.
* Prep for your next meeting with a one-page brief of recent threads and
  attached documents.

## Get started with Claude for Outlook

### Supported versions

Claude for Outlook runs on the following Outlook clients.

* Outlook on the web
* Outlook on Windows, both new Outlook and classic Outlook, with a
  Microsoft 365 subscription
* Outlook on Mac with a Microsoft 365 subscription

In Outlook on the web with Chrome or Microsoft Edge at version 137 or
earlier, Claude may not be able to search your mailbox, read attachments, or
change a draft you have open. The same applies to Outlook on Windows when the
Microsoft Edge WebView2 Runtime, which Outlook uses to show add-ins, is at
version 137 or earlier. See
[Claude cannot search, read attachments, or change an open draft](#claude-cannot-search-read-attachments-or-change-an-open-draft).

The following are not supported: Outlook 2016 and 2019 perpetual or
volume-licensed editions, Outlook on iOS, Outlook on Android, and
mailboxes hosted on Exchange on-premises. Exchange Online through
Microsoft 365 is required.
Shared mailboxes and mailboxes you open as a delegate are also not
supported. Claude for Outlook searches, triages, and moves mail only in
your own mailbox.

Anthropic has not tested Claude for Outlook with Outlook 2021 or 2024
perpetual or volume-licensed editions, including Office LTSC. Microsoft
ended support for Office 2021 and Office LTSC 2021 on October 13, 2026.

Gmail, Yahoo, iCloud, IMAP, and POP accounts added to Outlook are not
supported. Microsoft states that Outlook on Windows does not support add-ins
on these accounts.

### Install for yourself

**1. Open the marketplace listing**

Go to the [Claude for Outlook listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010724?tab=Overview).

**2. Install the add-in**

Select "Get it now" to install.

**3. Open Claude in Outlook**

Open Outlook, then open or select an email. Select the Claude button
and sign in with your Claude account.

The add-in may not appear right away in desktop Outlook. If you do not see
the Claude button, restart Outlook.

The button is labeled Claude, and each Outlook client puts it in a
different place.

* **Outlook on the web and new Outlook on Windows**: open or select a
  message, select Apps on its action bar or More apps on the ribbon, then
  select Claude. To keep Claude on the ribbon and the action bar, select
  More apps on the ribbon, right-click Claude, and select Pin.
* **Classic Outlook on Windows**: set the Reading Pane to Right or Bottom
  in the View tab, because Microsoft states that add-ins are unavailable
  otherwise. Select a message, then select Claude on the Home tab of the
  ribbon. If Claude is not there, select All Apps on the ribbon, then
  select Claude. With the Simplified Ribbon, All Apps is behind the
  ellipsis button. If the message is open in its own window, look on the
  ribbon of that window.
* **Outlook on Mac**: set the Reading Pane to Right or Below in the View
  menu, because Microsoft states that add-ins are unavailable otherwise.
  Select a message, then select Claude on the toolbar. If Claude is not
  there, select the ellipsis button on the toolbar, then select Claude.

Your organization's Microsoft 365 administrator may need to let you install
store add-ins, or deploy Claude for Outlook for you. Features that
look beyond the open email, such as triage, search, and free/busy lookups,
also need a one-time approval to read your mailbox, which in some
organizations only an administrator can give. See
[Troubleshoot installation](#troubleshoot-installation).

### Remove the add-in

Where you remove Claude for Outlook depends on your Outlook client.

In Outlook on the web and Outlook on Windows, select More Apps on the
navigation bar or All Apps on the ribbon, then Add apps. On the Apps page,
select Manage your apps, find Claude, and select More options, then
Remove. Microsoft's
[Use add-ins in Outlook](https://support.microsoft.com/en-us/office/use-add-ins-in-outlook-1ee261f9-49bf-4ba6-b3e2-2ba7bcab64c8)
page gives these steps for new Outlook. In classic Outlook, the button after
All Apps is Add Apps or Get Add-ins, depending on your version or account
type. Get Add-ins opens the Add-Ins for Outlook dialog instead of the Apps
page, so remove Claude there.

In Outlook on Mac, open the
[Add-Ins for Outlook dialog](https://aka.ms/olksideload) in a browser and
remove Claude there.

If there is no option to remove it, your administrator manages the add-in.
Ask them to remove it.

### Deploy to your organization

Organization admins can deploy Claude for Outlook through the Microsoft
365 Admin Center.

**1. Open Integrated apps**

In the [Microsoft 365 Admin Center](https://admin.microsoft.com), go
to Settings, then Integrated apps.

**2. Find the add-in**

Search for "Claude for Outlook" in Microsoft AppSource.

**3. Deploy**

Deploy the add-in to your organization or to specific people. See
[Microsoft's deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins)
for assignment options.

**4. Grant Microsoft Graph consent**

Complete the [Microsoft Graph admin consent](#grant-microsoft-graph-consent)
step below so users are not prompted individually.

> [!NOTE]
>
> If your organization uses Microsoft Entra Privileged Identity
> Management (PIM) for admin roles, the Integrated apps page does not
> recognize roles activated through PIM, so deployment fails. This is a
> [known Microsoft issue](https://learn.microsoft.com/en-us/office/dev/add-ins/resources/resources-office-add-in-known-issues),
> tracking ID 11126536. To work around it, deploy from an admin account
> with the required role assigned as permanently active rather than
> PIM-eligible. See
> [Microsoft's troubleshooting guidance](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/miscellaneous/cannot-deploy-add-in-integrated-apps-menu).
> Individual users can still
> [install the add-in themselves](#install-for-yourself).

After installation, team members open Outlook, open any email, select the
Claude button, and sign in with their Claude credentials. See
[Install for yourself](#install-for-yourself) for where each Outlook client
puts the button. Pinning the task pane keeps it open as you move between
messages.

You do not need to turn on the setting that lets users access the Office
Store, which Microsoft now calls Microsoft Marketplace, to deploy Claude for
Outlook.
[Microsoft states](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center)
that the setting does not apply to Outlook add-ins. If the add-in does not
appear for people 72 hours after you deploy it from the store, deploy it
from the manifest file instead, as described in
[Install from a manifest file](#install-from-a-manifest-file).

People who install the add-in for themselves need the
[My Marketplace Apps user role](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/add-ins-for-outlook/specify-who-can-install-and-manage-add-ins)
in Exchange Online. Microsoft enables that role for everyone by default, so
check whether your organization removed it.

### Install from a manifest file

If deploying from the store does not work for your organization, an IT
administrator can deploy the add-in by uploading its manifest file directly.

**1. Download the manifest**

Download the
[Claude for Outlook manifest](https://pivot.claude.ai/manifest-outlook.xml)
and save it to a secure location.

**2. Open Integrated apps**

In the [Microsoft 365 Admin Center](https://admin.microsoft.com), go
to Settings, then Integrated apps.

**3. Upload the add-in**

Select Upload custom apps, then Office Add-in. Choose the option to
upload a manifest file from your device, select the file you downloaded,
and upload it.

**4. Assign people**

Choose your deployment scope: the entire organization, specific
people, specific groups, or just yourself for testing.

**5. Deploy**

Review the settings and select Finish deployment. The add-in can take
up to 72 hours to appear for everyone, and people may need to restart
Outlook to see it.

**6. Grant Microsoft Graph consent**

Complete the [Microsoft Graph admin consent](#grant-microsoft-graph-consent)
step below.

### Troubleshoot installation

Find your symptom below.

#### The Claude button is missing after you install

Open or select a message first, then look where your Outlook client puts
the button. [Install for yourself](#install-for-yourself) lists the place
for each client. The add-in may not appear right away in desktop Outlook,
so restart Outlook if you still do not see the button.

#### "Get it now" does nothing or returns to the same page

Add-ins are installed on a mailbox, not on a device. Sign in to the listing
page with the same Microsoft account that you use in Outlook, then select
"Get it now" again.

If the install still does not complete, your organization may restrict who
can install Outlook add-ins. In Exchange Online, the
[My Marketplace Apps user role](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/add-ins-for-outlook/specify-who-can-install-and-manage-add-ins)
controls whether people can install add-ins from the store for themselves.
Ask your Microsoft 365 administrator to assign you that role or to
[deploy Claude for Outlook to your organization](#deploy-to-your-organization).

#### You use a Gmail, Yahoo, iCloud, IMAP, or POP account in Outlook

These accounts are not supported. Claude for Outlook needs a mailbox on
Exchange Online, as described in [Supported versions](#supported-versions).

#### You use a Free Claude account

Claude for Outlook is not available on the Free plan. You can install the
add-in, but you cannot finish signing in. After you select "Connect" on the
page that opens in your browser, it says which plans include the add-in and
links to the upgrade page. The Claude pane keeps showing your sign-in code
until it expires.

To use Claude for Outlook, upgrade your plan. Then sign in again from the
Claude pane: select "Start over" if the code expired, "Continue in browser" if
your code still shows, or "Log in".

If you also belong to an organization on a Team or Enterprise plan, you do
not need to upgrade. On the page in your browser, select "Try a different
account", choose that organization, and select "Connect" again.

#### Mailbox features are unavailable

Features that look beyond the open email, such as triage, search, and
free/busy lookups, need a one-time approval to read your mailbox. If the
setup screen says "Your admin needs to approve access", select "Copy link
for your admin" and send the link to your Microsoft 365 administrator.
After they approve, select "I've been approved". See
[Grant Microsoft Graph consent](#grant-microsoft-graph-consent) for what
the administrator does.

If the setup screen says "Your admin needs to grant you access", your
organization requires each person to be assigned to Claude, and you are not
assigned yet. Select "Copy request for your admin" and send the text to your
Microsoft 365 administrator. After they assign you, select "I've been
assigned".

You do not have to wait for your administrator. Select "Continue without
mailbox access" to use Claude on the email you have open. The other features
stay off until your administrator acts.

If you already continued, select the warning button in the row with the +
button at the message box. It offers the same link or request for your
administrator, and Retry for after they act.

If the setup screen says "This Outlook client doesn't support Microsoft
Graph sign-in", approval will not help, because this Outlook client cannot
use triage, search, or free/busy lookups. Unless your organization requires a
sensitivity label check, reading and drafting on the open email still work,
so select "Continue without mailbox access" to keep going.
To use those features, update Outlook to a current Microsoft 365
subscription version, or use Outlook on the web.

If a screen titled "Can't check this email's label" says "This Outlook client
doesn't support Microsoft Graph sign-in", your organization requires a
sensitivity label check that this client cannot run. That screen has no
"Continue without mailbox access" option, and Try again will not help. To use
Claude on that email, update Outlook or use Outlook on the web.

#### The setup screen says "Couldn't connect to Microsoft Graph"

This message can mean that access to your mailbox has not been approved
yet, or that sign-in failed for another reason. Select Retry, and complete
the Microsoft sign-in if a window opens. If the window says "Need admin
approval", your Microsoft 365 administrator needs to approve access for your
organization, as described in
[Grant Microsoft Graph consent](#grant-microsoft-graph-consent). If the
screen changes to "Your admin needs to approve access" or "Your admin needs
to grant you access", follow
[Mailbox features are unavailable](#mailbox-features-are-unavailable).

If it still fails, ask your Microsoft 365 administrator whether they have
completed [Microsoft Graph consent](#grant-microsoft-graph-consent). If the
screen shows "Copy error for support", send them the copied text. To use
Claude in the meantime, select "Continue without mailbox access". Triage,
search, and free/busy lookups stay off until the connection works.

#### The Claude pane is blank or does not load

If the pane shows "Claude couldn't load Office's add-in library", your
network may be blocking `appsforoffice.microsoft.com`. Ask your IT
administrator to allow that address, then reopen the pane.

If the pane stays blank, check that your Outlook is one of the
[supported versions](#supported-versions). Outlook 2016 and 2019 perpetual
or volume-licensed editions can run add-ins in an older browser engine, and
the Claude pane may stay blank there. Update to a current Microsoft 365
subscription version of Outlook, or use Outlook on the web.

### Grant Microsoft Graph consent

Claude for Outlook reads mail and calendar data through Microsoft Graph.
This needs a one-time grant for your whole tenant, separate from the
Integrated apps deployment. A Global Administrator or a Cloud Application
Administrator can give it.

Have one of them open the following admin consent link in a
browser where they are signed in to your Microsoft 365 tenant.

```
https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/User.Read%20offline_access&redirect_uri=https://pivot.claude.ai/auth/callback
```

The administrator sees a Microsoft permissions screen listing
`Mail.ReadWrite`, `Calendars.Read`, `User.Read`, and `offline_access`.
After they select Accept, all users in the organization
can use Claude for Outlook without additional Microsoft prompts. The grant
takes effect immediately. Only the add-in rollout itself can take up to 72
hours.

If this step is skipped, people may see "Your admin needs to approve
access" or "Couldn't connect to Microsoft Graph" on the Claude setup screen.
If they try again from there, Microsoft may show its own "Need admin
approval" window.

The redirect to `pivot.claude.ai` after consent carries only the consent
outcome, never a token or authorization code. See
[Why sign-in redirects through pivot.claude.ai](https://claude.com/docs/office-agents/third-party-platforms.md#why-sign-in-redirects-through-pivot-claude-ai)
for what each redirect carries and how to verify it in a network capture.

#### Use your own Entra app instead

If your organization's policy does not permit consenting to a third-party
multi-tenant application, register a single-tenant application in the
Microsoft Entra admin center and have the add-in use it instead. The data
flow is identical; the Graph token stays in the user's Outlook client
either way. The difference is that approval and Conditional Access policy
live entirely under an application your organization owns.

**1. Register the application**

In the Entra admin center, go to App registrations and create a new
registration. Choose "Accounts in this organizational directory only".

**2. Configure authentication**

Under Authentication, add a Single-page application platform with
redirect URI `brk-multihub://pivot.claude.ai`. In Advanced settings,
set "Allow public client flows" to Yes.

**3. Add Graph permissions**

Under API permissions, add the Microsoft Graph delegated permissions
`Mail.ReadWrite`, `Calendars.Read`, `User.Read`, and `offline_access`.
Select "Grant admin consent" for your tenant.

**4. Add the client ID to the manifest**

Copy the application's client ID from the Overview page. Download the
manifest from the
[Install from a manifest file](#install-from-a-manifest-file) section
and open it in a text editor. Search for `https://pivot.claude.ai/?m=`.
At the end of every URL that starts this way, inside the quotation
marks, add `&amp;graph_client_id=YOUR_CLIENT_ID`. Lines that refer to a
URL by `resid` need no change, and neither do the icon or support
URLs. Save the file, then upload and deploy it as that section
describes.

The following example shows one edited line. The version number in your
file can differ. Type `&amp;` exactly as shown: an XML file cannot contain
`&` on its own.

```xml theme={null}
<bt:Url id="Taskpane.Url" DefaultValue="https://pivot.claude.ai/?m=outlook-1.0.0.5&amp;graph_client_id=YOUR_CLIENT_ID"/>
```

With this option, skip the admin consent link entirely. Users do not see a
Microsoft permissions prompt because your tenant has already consented to
your own application.

If you deploy through a third-party platform and generate your manifests
with the [setup wizard](https://claude.com/docs/office-agents/third-party-platforms.md#run-the-setup-wizard),
provide the client ID to the wizard as `graph_client_id` instead of
editing the file. See
[Deploy to Outlook](https://claude.com/docs/office-agents/third-party-platforms.md#deploy-to-outlook).

### Deploy in a US Government or national cloud

If your Microsoft 365 tenant is in GCC High, DoD, or 21Vianet, register
your own Entra application with `graph_client_id` as described above
(Anthropic's multi-tenant application exists only in the global cloud)
and set `graph_cloud` to the matching value:

| Tenant | `graph_cloud` |
| - | - |
| Commercial or GCC | `global` (default; may be omitted) |
| GCC High | `us-gov-high` |
| DoD | `us-gov-dod` |
| 21Vianet (China) | `china` |

For a DoD tenant, every URL in the manifest that starts with
`https://pivot.claude.ai/?m=` ends with:

```
&amp;graph_client_id=YOUR_CLIENT_ID&amp;graph_cloud=us-gov-dod
```

For GCC High and 21Vianet tenants, `graph_cloud` may be omitted: the
add-in detects those clouds at sign-in from the authority host Outlook
reports. Setting it explicitly is still recommended when your compliance
program requires the endpoints to be fixed in the reviewed manifest
rather than derived at runtime. DoD tenants share an authority host with
GCC High, so `graph_cloud=us-gov-dod` is always required for DoD.

### Connect through a third-party platform

If your organization routes API traffic through an internal LLM gateway,
Amazon Bedrock, Google Cloud Vertex AI, or Azure AI Foundry, you can use
the add-in without Claude accounts. This is the same gateway pattern used
by Claude Code.

For setup instructions and gateway requirements, see
[Use Claude for M365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms.md).

## Triage your inbox

Ask Claude what needs your attention. Claude reads your unread mail and
attachments and sorts them into three groups: action items for you, items
Claude can handle for your review, and noise you can archive in one
selection. Each action item carries a one-line reason. Items Claude can
handle, such as short acknowledgments, come with an action Claude proposes,
and Claude drafts the replies when you say so.

Prompts to try:

* "What needs me?"
* "Draft replies for everything you can handle"
* "Archive all the calendar responses and newsletters"

## Draft replies in your voice

Tell Claude what you want to say. It drafts the reply into Outlook's
native compose pane, unsent. If you say yes when Claude asks during setup,
or select "Learn my writing style" under Writing style in Settings and
confirm, Claude reads your recent sent mail once and writes a style guide, so
the draft matches your sentence length and formality register. Claude does
not read your sent mail to write the guide at any other time. It can still
read sent messages for other tasks, such as drafting a reply. To update the
guide, select the button again. To delete the style guide, Claude's
scratchpad, and what Claude learned from your edits on this device, select
"Delete what Claude
has learned about my writing" under Writing style in Settings. Claude leaves
the closing off so Outlook can append your configured signature without
duplication.
Claude chooses reply versus reply-all deliberately and warns before adding
anyone who was not on the thread.

Prompts to try:

* "Reply to this and agree to the extension, push back on the fee"
* "Reply-all thanking everyone and confirming Thursday works"
* "Forward this to Dana with a two-line summary"

## Summarize long threads

Claude reads the entire conversation, including every reply and forward,
and tells you what has been decided, what is still open, and who owes
what. Every claim cites the specific email it came from. Selecting a
citation opens that message in Outlook.

Prompts to try:

* "What's been decided and what's still open?"
* "Who owes what on this thread?"

## Read attachments inline

Claude reads `.docx` and `.xlsx` attachments on the open email without
you opening them. For `.pptx` attachments, open the deck in PowerPoint
with the thread loaded as context using
[Work across M365 apps](https://claude.com/docs/office-agents/work-across-apps.md). PDF attachments
are not currently read inline; save the file and upload it through the
sidebar instead.

Prompts to try:

* "Summarize the attached memo"
* "What's in the spreadsheet on this email?"

## Search your mailbox

Ask Claude to find a past conversation by topic. Claude searches your mailbox
by keyword, using words it picks from your request.
Results return as citations that open the source message in Outlook so
you can verify every answer against the original email.

Prompts to try:

* "When did we last discuss the cap with Fernwood?"
* "Find the email where Dana sent the revised term sheet"

## Find time and create events

Claude checks free/busy for everyone whose calendar you can see and
proposes slots that respect working hours and existing holds. The invite
is drafted into Outlook's native appointment form with attendees, subject,
and agenda for you to review and send.

To make a meeting repeat, open it for editing as the organizer and ask
Claude. This works on a new invite, a saved meeting, or a whole series.
Claude lists the pattern, dates, time, and time zone it will set and waits
for you to allow the change. Nothing is saved or sent until you click Save
or Send in Outlook. All-day events are not supported.

Prompts to try:

* "Find 30 minutes with Dana and the Fernwood team next week"
* "Block Thursday afternoon for deep work"
* "Make this weekly through the end of June"

## Prep for meetings

For your next event, Claude pulls the last thread with each attendee and
any attached documents into a one-page brief, so you walk in knowing the
open items and what each person last said.

Prompts to try:

* "Prep me for my 2pm"
* "What's open with Dana before our call?"

## Work across M365 apps

Claude for Outlook shares context with Claude for Excel, PowerPoint, and
Word, so Claude can work across your open Office apps in a single
conversation. For example, you can open an attached letter of intent in
Word with the email thread already loaded as context, or pull numbers from
an email into an open Excel model, without copying between apps.

For setup instructions, see
[Work across M365 apps](https://claude.com/docs/office-agents/work-across-apps.md).

## Model availability

When you sign in with a Claude account, you can choose from the models in the
model menu, which depend on your plan and your organization's settings. When
you connect through a
third-party platform such as Amazon Bedrock, Vertex AI, Azure AI Foundry,
or an LLM gateway, Claude for Outlook supports Claude Opus 4.7 and later
and Claude Sonnet 5 and later. Earlier model generations are not available
in Outlook on those platforms.

## How Claude accesses your mailbox

Claude reads the email or event you have open via Office.js. For anything
that spans your mailbox or calendar, including thread retrieval, search,
free/busy lookups, and move or flag operations, Claude uses Microsoft
Graph. All Graph calls run in your browser, and the Graph access token
stays in the browser's MSAL cache and is never sent to Anthropic.

The add-in never sends mail or invites. It does not request
the `Mail.Send` permission. Every draft lands unsent in Outlook's compose
or appointment form, and you click Send.

![Claude reads the open item via Office.js and uses Microsoft Graph for mailbox-wide actions; the Graph token stays in the browser.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?fit=max\&auto=format\&n=-4jzPa4NasvobarI\&q=85\&s=3760f3ba806ce4cb2f835cfa2e409eae)

Outlook mailbox access: the open item comes through Office.js, broader mailbox actions use Microsoft Graph, and the Graph token stays in the browser.

Connectors are separate from the add-in's own access. A
[connector](https://claude.com/docs/office-agents/connectors-and-skills.md), such as Microsoft 365,
can send mail, messages, or invites. Claude asks for your approval before
each connector action, unless you selected the "Always allow" button for that
connector, such as "Always allow Microsoft 365 tools", on its approval card.
Your organization can remove that button. Some actions, such as sending mail
or Teams messages through the Microsoft 365 connector, still ask every time.

Where mailbox content goes after Claude reads it depends on how you sign
in.

### When you sign in with a Claude account

Mailbox content that Claude reads becomes part of the prompt sent to
`api.anthropic.com`. Standard API retention applies: see
[Data retention and audit](#data-retention-and-audit). The add-in does not
keep a server-side copy or index of your mailbox.

### When you connect through a third-party platform

The prompt goes only to the inference endpoint you configured, such as
Amazon Bedrock, Vertex AI, Azure AI Foundry, or an LLM gateway. On Amazon
Bedrock, Vertex AI, or a gateway that routes to them, no mailbox content
reaches Anthropic. On Azure AI Foundry, Anthropic operates the Claude models
and processes prompts as an independent processor for Microsoft, as
described in
[Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).
See
[Use Claude for M365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms.md)
for configuration details. The add-in does not keep a server-side copy or
index of your mailbox.

## Chat history

Chat history is stored locally in your browser using IndexedDB. It is
not synced across devices or browsers. You can clear all chat history
from Settings at any time. The local store is also cleared when you
clear your browser data. Chat history is specific to the combination of
the add-in surface, your user ID, and your organization ID, so your
Excel and Outlook histories are separate. Reinstalling the add-in or
switching between Claude add-ins does not remove it. See
[Data storage and retention](https://claude.com/docs/office-agents/data-storage.md) for where it
sits on disk and how long it is kept.

When you sign in with a Claude account, the add-in sends your
conversations to Anthropic, including the content Claude reads from your
mailbox and calendar, and any files you attach. Clearing chat history
removes only the copy in your browser. It does not delete the messages
or attached files that Anthropic keeps.

## Data retention and audit

For Claude for Outlook use, inputs and outputs are deleted on Anthropic's
backend within 30 days of receipt or generation, except as described in
[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)

Enterprise organizations can route full audit telemetry from Claude for
Outlook to their own OpenTelemetry collector for integration with a SIEM
or observability platform. See
[Configure a custom OpenTelemetry collector](https://claude.com/docs/office-agents/enterprise-readiness.md)
for setup. On Pro, Max, and Team plans, observability and audit
export are not available. Claude for Outlook does not inherit custom
data retention settings your organization may have configured and is not
included in Enterprise audit logs. For Enterprise organizations with the
[Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api)
enabled, Claude for Outlook sessions are included in the Compliance API.
This coverage requires no additional setup: the same Compliance Access
Keys apply.

## Unsupported capabilities

Claude for Outlook does not support the following.

* Warnings when you select Send. Claude for Outlook does not use
  Outlook's Smart Alerts, so it does not check or hold a message or
  invite when you select Send. To have a draft checked, ask Claude to
  review it before you send.
* Shared mailboxes and mailboxes you open as a delegate. Claude for
  Outlook searches, triages, and moves mail only in your own mailbox.
* Mailbox-wide features without Microsoft Graph consent. Features that
  look beyond the open email or event, such as search, triage, reading a
  whole thread, free/busy lookups, and move or flag actions, need
  Microsoft Graph consent. In an organization, an administrator can grant
  it once for everyone, as described in
  [Grant Microsoft Graph consent](#grant-microsoft-graph-consent).

For the Outlook versions and mailboxes that are not supported, see
[Supported versions](#supported-versions).

## Prompt injection risks

Be cautious with email from external or untrusted senders. Email bodies
and attachments are untrusted input and may contain instructions intended
to manipulate Claude rather than you.

Prompt injection refers to malicious instructions hidden in an email
body, signature, or attachment that try to trick the AI into taking
unintended actions. For example, a routine inbound email might contain
hidden text instructing Claude to forward a thread or draft a reply you
did not ask for. Claude may interpret these instructions as legitimate
requests.

Review every draft and inbox action before accepting it, especially when
working with email from external or untrusted senders.

## Recommended use during beta

As a beta feature, Claude for Outlook is not recommended for:

* Unattended sending. The add-in never sends mail or invites; every
  draft lands unsent for your review. After you select "Always allow" for
  a connector, Claude can use it without asking, and some connectors can
  send.
* Client-facing or counterparty correspondence without reading the draft
  first.
* Replacing your judgment on which emails matter or how to handle a
  relationship.
* Mailboxes containing privileged or regulated data without appropriate
  organizational controls.

To use Claude for Outlook safely and effectively:

* Review drafted replies and invites before sending, especially recipient
  lists.
* Verify thread summaries against the cited source emails for high-stakes
  conversations.
* Apply appropriate Microsoft 365 permissions and Conditional Access
  policies for the add-in.
* Maintain human oversight for anything leaving your organization.

## Troubleshooting

### Claude cannot search, read attachments, or change an open draft

If only features that look beyond the open email, such as search, triage,
and calendar, do not work, mailbox access may not be approved yet. See
[Grant Microsoft Graph consent](#grant-microsoft-graph-consent).

If Claude also cannot read attachments on the open email or change a draft
you have open, check the causes below.

* **An older version of Chrome or Microsoft Edge in Outlook on the web**:
  at version 137 or earlier, these features may not work. Update the browser
  to the latest version, then restart it. If you cannot update it, ask your
  IT administrator.
* **An older WebView2 Runtime in Outlook on Windows**: Outlook on Windows
  shows add-ins in the Microsoft Edge WebView2 Runtime, and at version 137
  or earlier these features may not work. The runtime updates itself by
  default, separately from Outlook and Microsoft 365 updates. If it is out
  of date, your organization may manage its updates. Ask your IT
  administrator to update it to the latest version, then restart Outlook.
  See
  [Microsoft's guidance on WebView2 and Microsoft 365 Apps](https://learn.microsoft.com/en-us/deployoffice/webview2-install).
* **A content blocker**: some content blockers, such as ad blockers, have
  the same effect, even in a current browser. Turn off the content blocker,
  then reload the page or restart Outlook, and try again.
