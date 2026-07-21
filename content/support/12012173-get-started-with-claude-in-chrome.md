# Get started with Claude in Chrome

Claude in Chrome is available for all paid plans (Pro, Max, Team, and Enterprise). It's generally available in Claude Cowork and Claude Code, and in beta in the Chrome browser.

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites alongside you. You can launch Claude in Chrome tasks from the side panel in your Chrome browser, or through Claude Cowork or Claude Code.

**Important:** Claude in Chrome allows Claude to interact directly with websites on your behalf. Claude in Chrome is now enhanced with our safety classifiers but is still risky. Please review **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)** before use.

## Where you can use Claude in Chrome

### Claude Code integration

Claude Code and the Chrome extension now work together for a build-test-verify workflow:

- Build with Claude Code in your terminal, then deploy to a URL Claude can reach.

- Test and verify in the browser with the Chrome extension.

- Debug issues using console logs—Claude can read errors, network requests, and DOM state directly.

This integration is especially useful for design verification (comparing Figma mocks to built output), live debugging, and automated testing.

### Control browser actions from Claude Desktop (Chat, Claude Cowork, and Claude Code)

When you start a chat, task, or session in Claude Cowork that touches a website, Claude can open the browser directly in Chrome and do the work, clicking, typing, and filling out forms the way a person would. You can let Claude handle work in the browser without switching windows.

Follow these steps to enable the Claude in Chrome connector in your desktop app:

1. Click your initials in the lower left corner, then select “Settings.”

2. Navigate to “Connectors.”

3. Find **Claude in Chrome** in the list and click “Configure.”

4. Toggle the connector on, then download and install the extension if you haven’t already.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1892696502/a23969725f631e99b9e4c47ec6e9/89803b8f-4f3c-4983-8b4d-63aec687ea1a?expires=1784609100&amp;signature=0d8ef8786b3e9247173488f5e90e1772195ab2cb36e4f4128cba4c431f27a5b8&amp;req=dSguFM93m4RfW%2FMW1HO4zdOezI9a6Lp4hnw73Y7ib%2Be2yU75SAloDAepfWn%2B%0A4PYTm1C%2BMTa3P%2FraVts%3D%0A)

Completing these steps will add Claude in Chrome to the “Connectors” drop-down on your chats with Claude. This is disabled by default, so you’ll need to enable it manually for each conversation.

### Chat with Claude in the browser side panel

Open the Claude side panel to work with Claude right next to the page you're on. Claude sees what's on the page and can act on it—reading, clicking, typing, navigating, and filling forms—so you can get help without leaving your browser window.

The side panel is a good fit for in-the-moment browsing tasks:

- Summarize or compare what's open across your tabs.

- Pull details off a page into a note, doc, or form.

- Walk through a task on a site step by step while you watch.

To open the side panel, click the Claude icon in your Chrome toolbar. It stays visible while you browse. If you haven't installed the extension yet, see **[Installing Claude in Chrome](#h_e0aabae2db)** below.

## Model selection

Claude in Chrome is available on all public models.

---

## Installing Claude in Chrome

1. Open a Google Chrome browser window.

  1. **Note:** Claude in Chrome is not supported on other Chromium-based web browsers or mobile devices.

2. Visit the **[Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)** to find Claude in Chrome.

3. Click "Add to Chrome" to install the extension.

4. Sign in with your Claude account credentials when prompted.

5. Pin the extension by clicking the puzzle piece icon, then the thumbtack next to "Claude."

6. Grant the necessary permissions to enable Claude to interact with your browser.

The Claude icon will appear in your Chrome toolbar. Click it to open Claude in a side panel that stays visible while you browse.

---

## Permissions required to install Claude in Chrome

You will need to grant Claude in Chrome the following permissions to install and use the extension:

| **Permission**                      | **Why Claude Needs This**                                                                                                                                              |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sidePanel                           | This lets Claude appear as a panel on the side of your browser, so you can chat with Claude while browsing any website.                                                |
| storage                             | This lets Claude save your preferences so they're still there when you close and reopen your browser.                                                                  |
| scripting                           | This lets Claude read text on webpages so it can help you with tasks.                                                                                                  |
| debugger                            | This is what allows Claude to actually control your browser – clicking buttons, typing text, and taking screenshots – when you ask it to complete tasks for you.       |
| tabGroups                           | This lets Claude organize tabs it opens into a separate group with a different color, so you can easily tell which tabs Claude is using versus your personal browsing. |
| tabs                                | This lets Claude open, close, and switch between browser tabs when completing tasks for you.                                                                           |
| alarms                              | This lets Claude run scheduled tasks at specific times you choose – like checking something on a website at a set time every day.                                      |
| notifications                       | This lets Claude send you a notification on your computer when it finishes a task or needs you to take action.                                                         |
| system.display                      | This lets Claude know the size of your screen so it can accurately click in the right places when automating tasks.                                                    |
| webNavigation                       | This lets Claude intervene if it detects that you are on a high-risk website.                                                                                          |
| declarativeNetRequestWithHostAccess | This lets the extension identify itself to Anthropic's servers, helping us understand how the browser extension is being used and troubleshoot any issues.             |
| offscreen                           | This lets Claude play notification sounds in the background when your attention is needed.                                                                             |
| nativeMessaging                     | This will let the extension seamlessly integrate with other Anthropic products on your computer like Claude Desktop or Claude Code once we enable that capability.     |
| downloads                           | This lets Claude download files from websites and open them when you ask it to save or work with files as part of an automated workflow.                               |
| unlimitedStorage                    | This lets Claude store more data locally (like complex instructions for a detailed workflow) beyond the normal limits that Chrome sets for extensions.                 |

Refer to the **[Google Chrome Permissions documentation](https://developer.chrome.com/docs/extensions/reference/permissions-list)** for more information.

## Core capabilities

### Record a workflow

Teach Claude a workflow by recording the steps yourself, and Claude learns to repeat them. This is useful for repetitive browser tasks that follow the same pattern each time. To record a workflow:

1. Click the record icon in the extension panel.

2. Perform the steps you want Claude to learn.

3. Stop recording when finished.

4. Save the workflow as a shortcut for future use.

### Console logs

Claude can now read browser console output, including errors, network requests, and DOM state. This helps developers identify and debug issues without leaving the browser.

### Scheduled tasks

Set recurring browser tasks to run automatically on your schedule. Set it once and Claude handles it from there—daily, weekly, monthly, or annually. You can schedule your Claude in Chrome shortcuts to run automatically by clicking the clock icon in the upper right corner of the extension panel.

### Multi-tab functionality

Claude can manage multiple browser tabs simultaneously. Drag tabs into Claude's designated tab group to enable Claude to view and interact with all grouped tabs at once—eliminating the need to manually switch between tabs to compile information.

### Enhanced site navigation

Claude has built-in knowledge of how to navigate popular platforms including Slack, Google Calendar, Gmail, Google Docs, and GitHub. Simple commands like "schedule a meeting" or "update the doc" work without detailed step-by-step instructions. We're continuously expanding Claude's site-specific capabilities.

### Sign in with 1Password

When a task requires signing in, Claude can request the login from 1Password instead of stopping at the login page. You approve each request with biometrics, and 1Password fills the credential directly so Claude never sees your password or one-time code. 1Password for Claude is in beta on macOS. Learn more in **[Get started with 1Password for Claude](https://support.claude.com/en/articles/15936181)**.

### Background workflows

Claude handles complex, multi-step workflows and keeps working even when you switch tabs (as long as Chrome is open). Enable notifications to receive alerts when Claude requires permission or completes a task, allowing you to focus on other work while Claude processes tasks in the background.

### Visual context sharing

Share visual information directly with Claude by uploading images or capturing screenshots of specific screen regions. Point Claude to the exact button, field, or detail—much faster than describing complex layouts in words.

### Image uploads

Give Claude an image and tell it where to upload, whether it's an expense report, form attachment, or picture upload.

### Shortcuts

Save your best-working prompts as shortcuts and reuse these proven workflows instantly:

1. After crafting a prompt that works well, save it as a shortcut.

2. Access your saved shortcuts by typing "/" in the chat.

3. Select your shortcut to instantly apply the same instructions.

4. Edit or delete shortcuts through the extension settings.

You can also schedule shortcuts to automate recurring tasks.

### Contextual suggestions

Get prompt suggestions and helpful tips based on the website you're visiting, so you always have a starting point with Claude.

---

## For Team and Enterprise users

If you're using Claude in Chrome on a Team or Enterprise plan, your admin may have configured settings that affect your experience:

- **Extension availability:** Your admin controls whether the extension is enabled for your organization.

- **Site access:** Your admin can restrict which websites Claude is allowed to access using allowlists and blocklists.

If you're unable to install or use the extension, contact your organization's admin. For admin documentation, see **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls)**.

---

## Next steps

- **[Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)**: Learn how to control what Claude can access and do within the extension.

- **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)**: Understand risks and best practices.

- **[Claude in Chrome troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)**: Get help with common issues.

- **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls)**: For Team and Enterprise admins managing the extension for their organization.