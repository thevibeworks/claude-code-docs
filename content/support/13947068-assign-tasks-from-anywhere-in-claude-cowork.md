# Assign tasks from anywhere in Claude Cowork

Claude Cowork gives you one continuous conversation with Claude that you can reach from your phone or your desktop. With Dispatch, you can message Claude from your phone and have it work on your desktop computer, using your local files, connectors, plugins, and apps, then come back to the finished work.

Dispatch runs your tasks on your desktop, so your computer needs to be awake and the Claude Desktop app open while Claude works. This is different from a cloud session, which runs on Anthropic's servers and keeps working even when your computer is off. For where Cowork runs on each surface, see **[Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349)**.

This capability is available in beta for Pro and Max plans on Claude Cowork. It requires both the Claude Desktop app and the Claude mobile app.

---

## Requirements

To use this capability, you need:

- The most recent version of the **Claude Desktop app** installed and running on your computer (macOS, Windows x64, or Linux). Your computer must be awake and the app must be open for Claude to work on tasks. Download or update at **[claude.com/download](http://claude.com/download)**.

- The most recent version of the **Claude mobile app** installed on your phone. Existing mobile app users will need to update to the latest version before using this capability.

- **A Pro or Max plan**.

- **An active internet connection** on both devices.

---

## How it works

Instead of starting a new session for each task, you have a single persistent thread with Claude. This thread doesn't reset. Claude retains context from previous tasks, so you can pick up where you left off.

Message Claude from your phone on the way to work, then follow up from your desktop when you sit down. It's the same conversation, same context, wherever you reach it.

When you assign a task, Claude figures out what kind of work is needed and spins up the right session. Development tasks run in Claude Code; knowledge work runs in Cowork. These sessions appear in their respective sidebars. You can click into any session for details, or wait for the result in the thread.

Claude messages you the outcome (a spreadsheet, a memo, a comparison table, a pull request) rather than showing you every step of the process. You'll get a push notification on your phone when a task is done or when Claude needs your go-ahead.

---

## Get started

Follow these steps to get started:

1. Download or update Claude Desktop.

2. Download or update Claude for iOS or Android.

3. Open Cowork on either your phone or your desktop.

4. Click “Dispatch” on the left side panel.

5. You’ll land on a page describing the functionality. Click “Get started”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2169954086/419674f781edb2977b93cce062b4/93b1893c-d79a-4eb6-b2f1-2fe3e043bd90?expires=1784291400&amp;signature=5f36ee1cefbb0999fbf7d1b12c14962b982ab11341cbd227de18ab567d129c42&amp;req=diEhH8B7mYFXX%2FMW1HO4zSZP0paJHA%2F7B32drIe5EDlo9XrqMBAhM5ier77z%0AQaX8%0A)

6. On the next screen, you can give Claude access to your files and keep your computer awake by toggling those on:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2169955082/de4053ee0eab8fcb9263584bb171/d39b77da-1a69-4682-9fdb-7ed488f236b0?expires=1784291400&amp;signature=023298fe8bb0ba9f7d83e30cb5a1fbe7b4709d92ca3741260bd2146d6ed41fcb&amp;req=diEhH8B7mIFXW%2FMW1HO4zaZWs96aVAAaepuGRb1rD3JSUvVxZoOkcAmrfo8j%0ALu3H%0A)

7. Click “Finish setup.”

8. Start messaging Claude within the “Dispatch” section.

After completing these steps, your continuous conversation with Claude syncs across both surfaces automatically.

---

## What you can do

From your phone, you can hand Claude tasks that use everything on your desktop, including things you can't open on your phone. For example:

- Ask Claude to pull data from a local spreadsheet and compile a summary report.

- Have Claude search your Slack messages and email, then draft a briefing document.

- Request a formatted presentation built from files in your Google Drive.

- Tell Claude to organize or process files in a specific folder on your computer.

Claude uses the same connectors, plugins, and file access you've already configured in Cowork. You don't need to set anything up separately for mobile.

### Retrieve files and outputs

When Claude finishes a task that produces a file, you can access it directly from mobile or find it on your desktop at the location Claude specifies.

### Memory

Claude remembers what you've worked on and learns how you work. Context carries across sessions, so you don't have to re-explain your preferences, your projects, or how you like things done.

You control what Claude remembers. You can view, edit, and delete your memory at any time.

### Scheduled tasks and routines

You can set up tasks that Claude runs automatically on a schedule. Tell Claude once to check your email every morning, pull your metrics every week, or compile a Friday report, and it handles it from there without being asked again.

For more on setting up and managing scheduled tasks, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

### Computer use

Claude can use the apps on your computer to complete tasks you assign through Dispatch. If you ask Claude to update a spreadsheet in Excel, navigate an internal dashboard, or run your dev tools, Claude can work directly with those apps on your desktop.

For details on how computer use works, permissions, and safety guidance, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-computer-use-safety)**.

**Note:** Computer use isn't available in the Linux beta. On a Linux desktop, Dispatch still works with your files, connectors, and plugins, but it can't drive desktop apps through computer use.

---

## Safety considerations

From your phone, you can now access everything on your desktop through Claude—including files, connectors, any plugins you've installed, and your apps through computer use.

Giving a mobile AI agent remote control of a desktop AI agent creates a chain where instructions from your phone can trigger real actions on your computer: reading, moving, or deleting local files, interacting with connected services, controlling your browser, and using your desktop apps. This is powerful, but it also means mistakes (or malicious content the model encounters along the way) can have real consequences. A manipulated instruction, an unexpected command, or a phishing link opened in your browser could cascade into actions that are difficult or impossible to undo.

Before enabling this, make sure you:

- Trust every app and service in the chain

- Understand what files and accounts are accessible

- Know how to quickly disconnect or revoke access

Only connect these agents if you're comfortable with what they *could* do, not just what you intend them to do.

For additional safety guidance, see **[Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)**.

---

## Current limitations

The following limitations apply:

- **Your desktop must be active.** Dispatch works with the local files and apps on your desktop computer, so your computer needs to be awake and the Claude Desktop app open while Claude works. If you want Claude to keep working while your computer is off, start a cloud session instead. See **[Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349)**.

- **Computer use has different safety properties than other Cowork tools.** Claude clicks, types, and navigates your screen directly rather than going through connectors or permission-gated file access. For details, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-computer-use-safety)**.

- **One continuous thread.** There's no way to start a new thread or manage multiple threads. All messages live in a single conversation.

- **On Linux, tasks that rely on computer use aren't available**, since computer use isn't part of the Linux beta. File, connector, and plugin tasks work as normal.