# Use Claude in Google Docs, Sheets, and Slides

Claude for Google Workspace adds a Claude sidebar to Google Docs, Google Sheets, and Google Slides. Claude reads the file you have open and edits it directly, so you can draft, analyze, restructure, and restyle without copying content back and forth.

Claude for Google Workspace is available in beta for Pro, Max, Team, and Enterprise plans. You also need a Google account that is allowed to install Google Workspace Marketplace apps.

With Claude for Google Workspace, you can:

- Ask questions about the document, spreadsheet, or deck you have open and get answers that cite where they came from.

- Have Claude make the edits for you, in place, with every change visible in version history.

- Build spreadsheet models, write and fix formulas, and clean up data in Sheets.

- Draft, rewrite, and restructure long documents in Docs.

- Create new slides or tighten and restyle existing ones in Slides.

- Use the connectors your organization has already set up in Claude, from inside the sidebar.

This is different from the **[Google Workspace connectors](https://support.claude.com/en/articles/10166901)** in Claude, which let Claude search and reference your Drive, Gmail, and Calendar while you chat at claude.ai. The extension works the other way around: Claude comes to the file you’re already in.

## Quick start

If your organization already allows Marketplace apps, this takes about two minutes.

1. Install Claude from the **[Google Workspace Marketplace listing](https://workspace.google.com/marketplace/app/claude/12459801340)** and click "Install.” If an admin has already installed it for you, skip this step.

2. Open any file in Google Docs, Sheets, or Slides and go to Extensions > Claude > “Open Claude":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2707281468/abc0497defca04936c9a4b97d147/8b17d05f-3fb1-4e49-8d1f-65364ac3f496?expires=1791271800&amp;signature=54f1b1c94ad04510bc9d367fd6a6ea7e83eeb7a919b722fa1bc6f9c2ddb0b73b&amp;req=dicnEct2nIVZUfMW1HO4zRwmJT1uU%2BVHaAKM49NdBLPzox%2Fel8zYuzG69fJl%0A%2BArh%0A)

3. The first time, Google asks you to allow two permissions. Review them and click "Allow":

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2707282342/f583a396098ff16e3cbd156d4a2a/112c6459-79c6-4fbb-9bc0-748fda6f592f?expires=1791271800&amp;signature=ef53819ffc67a59c31718ea386944ed9a31cd7152c6ab18e6f4723f367eff3bc&amp;req=dicnEct2n4JbW%2FMW1HO4zeKY3p0Ehw%2F4eBfHlrCfDWf3Na6Mf4Z9kVIfZwdu%0AGW78%0A)

4. Sign in with your Claude account in the sidebar, and optionally enable your connectors.

5. Then ask Claude something about the file. Try "Summarize this document in five bullets" or "What does column F calculate?"

If the install button is greyed out or you see "This application is not allowed by your administrator,” your Google Workspace admin needs to allow or install Claude first. See **[Install for your organization](#h_2118c53c4b)** below.

## Install Claude for Google Workspace

There are two ways to install: for yourself, or for your whole organization. Which one you can use depends on your Google Workspace admin's Marketplace settings, not on your Claude plan.

### Install for yourself

1. Open the **[Claude listing](https://workspace.google.com/marketplace/app/claude/12459801340)** in the Google Workspace Marketplace.

2. Click "Install,” choose the Google account you use for Docs, Sheets, and Slides, and click "Continue.”

3. Review the permissions and click "Allow.”

4. Reload any Docs, Sheets, or Slides files you already have open. Claude now appears under the Extensions menu in all three.

One install covers Docs, Sheets, and Slides. You do not install three separate extensions.

### Install for your organization

Google Workspace super administrators can install Claude for everyone, or for specific groups or organizational units, so users don't have to install it themselves.

1. Open the **[Claude listing](https://workspace.google.com/marketplace/app/claude/12459801340)** while signed in as a super admin.

2. Click "Admin install,” then "Continue.”

3. Choose "Everyone at your organization,” or "Certain groups or organizational units," and pick who should get Claude.

4. Review the data access and terms, tick the agreement box, and click "Finish.”

5. Ask users to reload any open files. Claude appears under **Extensions** without any action on their part.

To remove Claude later, go to the Google Admin console, Apps, Google Workspace Marketplace apps, Apps list, select “Claude,” and click "Uninstall app.” Removal takes effect for all users the next time they reload a file.

### If your organization blocks Marketplace apps

Many organizations block Marketplace installs by default. An admin has two options in the Google Admin console under Apps, Google Workspace Marketplace apps, Settings:

- **Allowlist Claude** so users can install it themselves: set Marketplace access to "Allow users to install and run only allowlisted apps,” then add Claude to the allowlist under Apps list, Allowlist app.

- **Admin install it** using the steps above. Admin install works even while user installs are blocked.

Users who try to install a blocked app see “This application is not allowed by your administrator.” That message comes from Google, not Claude, and only a Workspace admin can clear it.

## What you can ask Claude to do

Claude works best when you tell it the outcome you want and let it figure out the steps. You can select text, cells, or a slide first to point Claude at a specific part of the file.

### In Google Docs

- "Rewrite the executive summary so it leads with the recommendation and fits in one paragraph."

- "This brief is 14 pages. Cut it to 6 without losing any of the numbered requirements."

- "Turn the notes under 'Next steps' into a table with owner, action, and due date."

- "Check this contract for defined terms that are used but never defined."

- "Make every heading sentence case and fix the numbering in section 4."

### In Google Sheets

- "Walk me through how the total in H42 is calculated and flag anything hardcoded."

- "Build a three-statement model on a new tab from the assumptions in 'Inputs'."

- "Column D has dates in three different formats. Normalize them to YYYY-MM-DD."

- "Find why the VLOOKUP in the Summary tab returns #N/A for some rows and fix it."

- "Add a sensitivity table for price and volume, plus a chart of revenue by quarter."

### In Google Slides

- "Draft a five-slide project update from the bullet points in the speaker notes on slide 1."

- "Slide 7 is a wall of text. Split it into two slides and keep the deck's styling."

- "Make the titles across the deck parallel and under eight words each."

- "Add a bar chart of the regional numbers on slide 4, matching the deck's colors."

- "Restyle this deck to use the fonts and colors from the title slide."

Claude can also answer questions without editing anything: "What changed between the Q2 and Q3 tabs?" or "Which slides mention pricing?"

## How Claude works in your file

### Claude reads the file you have open, and only that file

When you send a message, Claude reads the relevant parts of the open file, plus whatever you have selected. Apart from content from any connectors you turn on, it cannot see other files in your Drive, your email, or your calendar. If you need Claude to use content from somewhere else, paste it into the chat or attach a file.

### Edits happen in place, as you

Claude makes changes directly in the document, spreadsheet, or deck. Google records them under your name, so they appear in File, Version history like any edit you make yourself. To undo something Claude did, use Undo for the last change or restore an earlier version from version history.

## You choose how much Claude asks first

The mode selector at the bottom of the sidebar has two settings:

| **Mode**                   | **What happens**                                                                                                                                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ask before edits (default) | Claude shows you what it is about to do, in plain language, and waits for you to click “Allow.”                                                                                     |
| Accept all edits           | Claude makes ordinary content edits without stopping. It still pauses for approval on anything that touches links, external images, web addresses, or someone's access to the file. |

In Google Docs, you also prompt Claude to propose text changes as cards you accept or reject one at a time, similar to suggestions.

### Some actions always need your approval, and some are never allowed

Regardless of mode, Claude stops and asks before it inserts an image from a web address, adds a link, or removes anyone's access. These show a "Security review" label and there is no "always allow" option for them.

Claude cannot share the file, give anyone access, or change who owns it. It also cannot create menus or scheduled automations, or load arbitrary web pages into your file. These requests are refused even if you ask.

### What else is in the sidebar

- **Model picker.** Choose the Claude model for the conversation.

- **Connectors.** Connectors your organization has enabled in Claude appear in the + menu. Add new ones at claude.ai, not in the sidebar.

- **Files and images.** Attach reference files (up to 20 per message, 30 MB per document, 10 MB per image) for Claude to read alongside the open file.

- **Web search.** Toggle “Search the web” when you want Claude to look things up. Off by default.

- **Chat history.** Conversations are saved per file in your browser and come back when you reopen Claude in that file. They do not sync across devices or browsers, and a copy of the file starts fresh.

---

## Current limitations

Claude for Google Workspace is in beta. These are the limits people ask about most. Several are deliberate, because the permissions that would lift them would also widen what the extension can access.

### All three apps

- Works only on the file it’s opened in. Claude can’t open, create, or copy other files in Drive, and can’t export the file as a PDF or download.

- Keep the sidebar open while Claude is working. Closing it stops the current task.

- Use Chrome, Edge, or Safari. Firefox is not supported in this beta; the sidebar loads but actions do not complete.

- Voice dictation is not available in the sidebar.

- A single long operation can run for up to six minutes before Google stops it. For very large jobs, ask Claude to work in stages.

- "Work across apps" (handing a task between Excel, Word, and PowerPoint) is a Microsoft 365 feature and is not available in Google Workspace.

### Google Docs

- Claude cannot read, reply to, or resolve comments. Paste a comment into the chat if you want Claude to act on it.

- Claude cannot accept or reject existing suggestions, and its own edits land as direct edits, not suggestions. Use "Ask before edits" if you want to review each change first.

- Claude cannot create, rename, or reorder document tabs. It can read and edit the content of every tab.

### Google Sheets

- Connected Sheets tabs (live BigQuery data) cannot be read or edited. Use Data, Data connectors, Extract to pull the rows into a regular tab first.

- Claude cannot create triggers, custom menus, or scheduled refreshes.

### Google Slides

- Charts Claude creates are inserted as images, not linked Sheets charts, so they do not update when numbers change. Ask Claude to regenerate the chart instead.

- Claude cannot refresh an existing linked chart. Click “Update” on the chart yourself after changing the source sheet.

- Claude cannot insert images from a web address without your approval each time.

---

## Security, privacy, and admin controls

Claude sees only the file you have open, plus any connectors you turn on, your content is handled under your existing Claude terms and is not used for training, and Google Workspace admins control who has the extension.

### Permissions Claude asks Google for

Claude requests two Google permissions, the minimum needed to show a sidebar and edit the file it is opened in. It does not request access to Drive, Gmail, Calendar, your contacts, or the ability to make network requests from your file.

| **Permission Google shows you**                                                                       | **Why Claude needs it**                                                                                                  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Display and run third-party web content in prompts and sidebars inside Google applications            | Shows the Claude sidebar inside Docs, Sheets, and Slides                                                                 |
| View and manage documents, spreadsheets, or presentations that this application has been installed in | Lets Claude read and edit the one file you opened it in. Google enforces this: the extension cannot open any other file. |

### How your data is handled

- Content from the open file, your messages, and any files you attach are sent to Claude to generate a response. For Team and Enterprise plans, this is governed by your organization's Commercial Terms and Data Processing Addendum. For Pro and Max it is governed by the Consumer Terms and Privacy Policy.

- Anthropic does not use this content to train its models. Use of data received from Google Workspace APIs adheres to the **[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy)**, including the Limited Use requirements.

- Inputs and outputs are deleted from Anthropic's systems within 30 days, except as described in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) The extension does not inherit custom data retention settings your organization may have set.**

- Chat history is stored locally in your browser, per file and is not synced across devices. Clear it from Settings in the sidebar.

### Enterprise security controls

How the standard Claude Enterprise controls apply to the Google Workspace extension today:

- **Third-party inference (Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway):** Not supported in this beta. The extension requires a Claude account sign-in. Claude for Microsoft 365 supports these platforms; the Google Workspace extension does not yet.

- **Zero Data Retention (ZDR):** Not available. Standard retention applies as described above. Because third-party inference is not supported, there is no zero-retention deployment path for the extension today.

- **HIPAA-ready organizations:** Not covered. Do not use the extension with protected health information.

### Admin controls

- **Google Workspace admins** decide who can install or use Claude through Marketplace allowlisting and admin install, scoped to the whole domain, groups, or organizational units. Uninstalling from the Admin console removes it for everyone.

- **Claude admins** control which connectors, skills, and models are available to members. The sidebar inherits those settings from your Claude organization.

- **Users sign in with their Claude account**, including SSO if your organization uses it. API keys and cloud-provider sign-in are not supported in the Google extension.

### Prompt injection

Files can contain instructions written by someone else, sometimes hidden in white text or tiny fonts. Claude treats document content as data rather than commands, labels hidden text it finds, and is designed not to follow a document's instruction to share the file, fetch a link, or contact anyone. You should still review Claude's proposed actions before approving them, especially in files you received from outside your organization.

---

## Troubleshooting

### Claude doesn't appear in the Extensions menu

Extensions only appear in files opened after the install, so if Claude isn’t appearing in the menu, reload the file. If it’s still missing, check that you are signed in to Google with the account Claude was installed for, then ask your Google Workspace admin to confirm Claude is installed or allowlisted for you. Tip: press Alt+/ (Option+/ on Mac) and type "Claude" to find the menu item quickly.

### "This application is not allowed by your administrator"

Your Google Workspace organization blocks Marketplace apps that are not allowlisted. This is a Google setting. Ask your Workspace admin to allowlist Claude or admin-install it. See If your organization blocks Marketplace apps.

### "Claude for Google Workspace needs a Claude account"

You previously signed in to a Claude add-in with an API key, Amazon Bedrock, Google Vertex AI, or a gateway. The Google extension supports Claude account sign-in only.

### The sidebar opens but nothing happens when I send a message

This can be caused by using Firefox or a browser with strict tracking protection that blocks the sidebar from talking to the document. Switch to Chrome, Edge, or Safari. If you are already on one of those, reload the file and reopen Claude.

### "This document's Claude add-in script is out of date"

Google is still serving an older version of the extension to this file. Reload the file and reopen Claude. If it persists for more than a few minutes, try again later.

### "Exceeded maximum execution time" or a task stops partway

Google limits a single extension operation to six minutes. Ask Claude to continue, or break the request into smaller steps, for example one tab or ten slides at a time.

### Claude says it can't read a tab in Sheets

The tab is a Connected Sheet backed by BigQuery. Use Data, Data connectors, Extract to copy the rows into a regular tab, then ask again.

### My conversation disappeared

Chat history is saved in your browser per file. It will not be there in a different browser, in a private window, after clearing site data, or in a copy of the file made with File, Make a copy.

---

## Frequently asked questions

### Do I need to install Claude separately for Docs, Sheets, and Slides?

No. One install from the Marketplace adds Claude to all three.

### Can Claude see my other files in Google Drive

Not by default. Google restricts the extension to the single file it is opened in. However, if you have the Google Drive MCP connected, Claude can use that to see other files. This is off by default.

### Can other people in the file see my conversation with Claude?

No. The conversation lives in your browser. Collaborators see Claude's edits in the file and in version history, attributed to you, but not your chat.

### Does Claude keep working if I close the sidebar or the tab?

No. Keep the sidebar open until Claude finishes. You can switch to other browser tabs while it works.

### How do I undo something Claude did?

Use Undo for the most recent change, or File, Version history, See version history to restore an earlier version. Every Claude edit is a normal edit in the file's history.

### Which Claude models can I use?

The same models available to your plan in Claude. Pick one from the model selector at the bottom of the sidebar.

### Is this the same as Claude in Chrome or the Google Drive connector?

No. Claude in Chrome works across web pages in your browser; the Google Workspace connectors let Claude search your Drive, Gmail, and Calendar from claude.ai. This extension puts Claude inside a specific Docs, Sheets, or Slides file and lets it edit that file.

### I use Microsoft 365 as well. Is there an equivalent?

Yes. See **[Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)**.