# Use Claude Cowork on web, desktop, and mobile

Claude Cowork is available on desktop, web, mobile, and in the Claude in Chrome side panel. Your sessions and files live with your Claude account and go where you go, on any device. This article explains how to start a Cowork session and what's available on each surface.

Claude Cowork is in beta on web and mobile for Pro, Max, and Team plans, and on Enterprise plans where an admin has enabled it. Cowork is also available in the Claude in Chrome side panel on Max and Team plans, on Pro plans as it rolls out, and on Enterprise plans where an admin has enabled it. See **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls#h_bdb63199e1)** for enablement steps.

---

## Start a Cowork session

On desktop, web, and mobile, chat and Cowork share one home, so you start both from the same place. Find the message box, select "Cowork" in the bottom left corner, then describe your task. To go back to a regular conversation, select "Chat."

The Chrome side panel works differently. Opening the side panel starts a Cowork session directly, with no selector to switch between chat and Cowork.

- **Web:** Go to **[claude.ai](https://claude.ai)** and find the “Home” tab.

- **Mobile:** Open the latest version of Claude for iOS or Claude for Android. If you don't see the Cowork option in the message box, update the app.

- **Desktop:** Open the latest version of the Claude Desktop app. If you don't see the Cowork option in the message box, update the app. Desktop is the full Cowork experience, where Claude can also use your local files and browser.

- **Chrome:** Click the Claude icon in your Chrome toolbar to open the side panel. The side panel starts a Cowork session, so there's no need to select "Cowork" first.

---

## How Cowork in the cloud works

When using Cowork in the cloud, Claude's work runs on Anthropic's servers instead of your computer, and your sessions and files are saved to your Claude account. This changes what Cowork can do:

- Work continues in the background. Close your laptop and Claude keeps going.

- Scheduled tasks run with no device online.

- The same sessions and files are available on desktop, web, and mobile.

- Sessions run in the cloud on every surface.

For details on how cloud and local sessions are isolated and what each can access, see **[Claude Cowork architecture overview](https://support.claude.com/en/articles/14479288)**. For safety guidance, see **[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135)**.

---

## What's available on each surface

Cowork in the cloud is in beta, and some features aren’t available yet. Here's what you can use on each surface today:

| **Feature**                                 | **Desktop** | **Web** | **Mobile** |
| ------------------------------------------- | ----------- | ------- | ---------- |
| Start, steer, and review tasks              | ✅           | ✅       | ✅          |
| Resume a session started on another surface | ✅           | ✅       | ✅          |
| Connectors                                  | ✅           | ✅       | ✅          |
| Skills and plugins                          | ✅           | ✅       | ✅          |
| Preview files Claude creates                | ✅           | ✅       | ✅          |
| Scheduled tasks                             | ✅           | ✅       | ✅          |
| Projects                                    | ✅           | ✅       | ✅          |
| Live artifacts                              | ✅           |         |            |
| Local file access                           | ✅           | ✅\*     | ✅\*        |
| Browser use                                 | ✅           | ✅\*     | ✅\*        |
| Computer use                                | ✅           | ✅\*     | ✅\*        |

A few notes on the table:

- *Local file access, local connectors, browser use, and computer use from web and mobile work through the Claude Desktop app. A cloud session can read and write files in folders you've connected on your computer only while the desktop app is open on that computer. If the app is closed, the session keeps running but can't reach your local files.

- Projects are available on every surface. From a project you can start a chat or a Cowork session, and Claude uses the project's knowledge as context. Projects tied to a local folder support Cowork sessions on desktop only, and Cowork won't change a project's contents, so add anything you want to keep to the project yourself. For more information, see **[Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274)** and **[Use live artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249)**.

- Live artifacts are available on the desktop app only. For more information, see **[Use live artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249)**.

- Local connectors and plugins that include local MCP servers work through the desktop app only.

- Scheduled tasks run in the cloud, so they no longer need your computer to be awake. For more information, see **[Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387)**.

- Computer use is a research preview for Pro and Max plans. For more information, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542)**.

## What requires the desktop app

Some capabilities reach things on your computer, so they need the Claude Desktop app open on your machine, even when your session runs in the cloud:

- **Local file access.** Claude reads and writes files in folders you've connected on your computer. A session in the cloud reaches these files only while the desktop app is open, only for folders you've connected, and with the permissions you've already set.

- **Local connectors.** This includes plugins using those connectors.

- **Browser use.** Claude works in your browser through Claude in Chrome. In the Chrome side panel, Claude can read the tab you're on without the desktop app. Claude driving your browser as part of a task still needs the desktop app open.

- **Computer use.** Claude clicks, types, and navigates your screen directly.

## Move between surfaces

When using Cowork in the cloud, sessions follow your account, so you can switch surfaces mid-task:

1. Start a task on any surface.

2. Open the same session from another surface to check progress, answer Claude's questions, or redirect the work.

3. Pick up the finished output wherever you are.

For example, start a task in the Chrome side panel while you're looking at a dashboard, then pick it up on desktop to work with the downloaded files.

When Claude finishes a task or needs your input, you'll get a notification on your phone. To get started, see **[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190)**.