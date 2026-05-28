Title: Get started with Claude in Chrome

URL Source: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

Markdown Content:
Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites alongside you. Claude works directly in the side panel while you browse, seeing what you see and taking actions when you ask.

## What's new

After months of testing, Claude in Chrome is now available in beta to users on all paid plans (Pro, Max, Team, and Enterprise).

### Claude Code integration

Claude Code and the Chrome extension now work together for a build-test-verify workflow:

This integration is especially useful for design verification (comparing Figma mocks to built output), live debugging, and automated testing.

### Control browser actions from Claude Desktop

Start a task in Claude Desktop and let it handle work in the browser without switching windows. Follow these steps to enable the Claude in Chrome connector in your desktop app:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/1892696502/a23969725f631e99b9e4c47ec6e9/89803b8f-4f3c-4983-8b4d-63aec687ea1a?expires=1779963300&signature=c288e855493ba9b6a76ed4a448212b818804126ce93558426bfc5ed9a7e61b29&req=dSguFM93m4RfW%2FMW1HO4zdOew4JV7rB6hnw73Y7ib%2BdVQWEiLiPZBdA6pcSA%0AUxAA5B8osrO9vqQc2Kk%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1892696502/a23969725f631e99b9e4c47ec6e9/89803b8f-4f3c-4983-8b4d-63aec687ea1a?expires=1779963300&signature=c288e855493ba9b6a76ed4a448212b818804126ce93558426bfc5ed9a7e61b29&req=dSguFM93m4RfW%2FMW1HO4zdOew4JV7rB6hnw73Y7ib%2BdVQWEiLiPZBdA6pcSA%0AUxAA5B8osrO9vqQc2Kk%3D%0A)

Completing these steps will add Claude in Chrome to the “Connectors” drop-down on your chats with Claude. This is disabled by default, so you’ll need to enable it manually for each conversation.

### Record a workflow

Teach Claude a workflow by recording the steps yourself, and Claude learns to repeat them. This is useful for repetitive browser tasks that follow the same pattern each time. To record a workflow:

### Console logs

Claude can now read browser console output, including errors, network requests, and DOM state. This helps developers identify and debug issues without leaving the browser.

### Scheduled tasks

Set recurring browser tasks to run automatically on your schedule. Set it once and Claude handles it from there—daily, weekly, monthly, or annually. You can schedule your Claude in Chrome shortcuts to run automatically by clicking the clock icon in the upper right corner of the extension panel.

### Follow Claude’s plan

Use “Ask before acting” to have Claude create a plan for your approval, then let it execute the entire workflow independently within those approved boundaries. Aside from **[certain high-risk actions](https://support.claude.com/en/articles/12902446-claude-for-chrome-permissions-guide#h_b7ded56289)**, Claude won't ask for permission until it's done or encounters something outside the plan. Learn more about this permission mode in our **[Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)**.

## Model selection

**Pro plans:** Claude in Chrome is currently limited to Haiku 4.5.

**Max, Team, and Enterprise plans:** Choose the model that best fits your task.

Switch between models anytime based on what you need.

## Installing Claude in Chrome

The Claude icon will appear in your Chrome toolbar. Click it to open Claude in a side panel that stays visible while you browse.

## Permissions required to install Claude in Chrome

You will need to grant Claude in Chrome the following permissions to install and use the extension:

**Permission****Why Claude Needs This**
sidePanel This lets Claude appear as a panel on the side of your browser, so you can chat with Claude while browsing any website.
storage This lets Claude save your preferences so they're still there when you close and reopen your browser.
scripting This lets Claude read text on webpages so it can help you with tasks.
debugger This is what allows Claude to actually control your browser – clicking buttons, typing text, and taking screenshots – when you ask it to complete tasks for you.
tabGroups This lets Claude organize tabs it opens into a separate group with a different color, so you can easily tell which tabs Claude is using versus your personal browsing.
tabs This lets Claude open, close, and switch between browser tabs when completing tasks for you.
alarms This lets Claude run scheduled tasks at specific times you choose – like checking something on a website at a set time every day.
notifications This lets Claude send you a notification on your computer when it finishes a task or needs you to take action.
system.display This lets Claude know the size of your screen so it can accurately click in the right places when automating tasks.
webNavigation This lets Claude intervene if it detects that you are on a high-risk website.
declarativeNetRequestWithHostAccess This lets the extension identify itself to Anthropic's servers, helping us understand how the browser extension is being used and troubleshoot any issues.
offscreen This lets Claude play notification sounds in the background when your attention is needed.
nativeMessaging This will let the extension seamlessly integrate with other Anthropic products on your computer like Claude Desktop or Claude Code once we enable that capability.
downloads This lets Claude download files from websites and open them when you ask it to save or work with files as part of an automated workflow.
unlimitedStorage This lets Claude store more data locally (like complex instructions for a detailed workflow) beyond the normal limits that Chrome sets for extensions.

## Core capabilities

### Multi-tab functionality

Claude can manage multiple browser tabs simultaneously. Drag tabs into Claude's designated tab group to enable Claude to view and interact with all grouped tabs at once—eliminating the need to manually switch between tabs to compile information.

### Enhanced site navigation

Claude has built-in knowledge of how to navigate popular platforms including Slack, Google Calendar, Gmail, Google Docs, and GitHub. Simple commands like "schedule a meeting" or "update the doc" work without detailed step-by-step instructions. We're continuously expanding Claude's site-specific capabilities.

### Background workflows

Claude handles complex, multi-step workflows and keeps working even when you switch tabs (as long as Chrome is open). Enable notifications to receive alerts when Claude requires permission or completes a task, allowing you to focus on other work while Claude processes tasks in the background.

### Visual context sharing

Share visual information directly with Claude by uploading images or capturing screenshots of specific screen regions. Point Claude to the exact button, field, or detail—much faster than describing complex layouts in words.

### Image uploads

Give Claude an image and tell it where to upload, whether it's an expense report, form attachment, or picture upload.

### Shortcuts

Save your best-working prompts as shortcuts and reuse these proven workflows instantly:

You can also schedule shortcuts to automate recurring tasks.

### Contextual suggestions

Get prompt suggestions and helpful tips based on the website you're visiting, so you always have a starting point with Claude.

## For Team and Enterprise users

If you're using Claude in Chrome on a Team or Enterprise plan, your admin may have configured settings that affect your experience:

If you're unable to install or use the extension, contact your organization's admin. For admin documentation, see **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls)**.

## Next steps

* * *

Related Articles

[Claude in Chrome Troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)[Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
