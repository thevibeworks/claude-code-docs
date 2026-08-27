# Use the built-in browser in Claude Cowork

Claude Cowork has a browser built into the Claude Desktop app. This article explains how the built-in browser works, how it differs from Claude in Chrome, and how to choose which one Claude uses.

The built-in browser is rolling out gradually this week to Cowork in Claude Desktop for macOS, Windows, and Linux (beta) on Pro, Max, and Team plans, and on Enterprise plans where an owner has enabled it. If you don't see it yet, check back in a few days. When the desktop app is online, the built-in browser is also available in Cowork on web or mobile.

## How the built-in browser works

When a Cowork task involves a website, a browser opens in the side panel next to your task. Claude opens sites, reads pages, clicks, types, and fills forms while you watch, with no need to switch windows. Links in the task transcript open in the same panel.

The built-in browser has the same browsing capabilities as Claude in Chrome. It doesn't rely on your own browser and works regardless of which browser you normally use.

The built-in browser lives in the desktop app, so Claude Desktop needs to be open and online for Claude to use it, even though your Cowork session runs in the cloud. If you start a task on desktop, you can keep steering it from Claude on the web or Claude Mobile as long as the desktop app stays open.

## Sign in to sites

The first time the built-in browser opens, you’ll see the option to "Stay signed in to your sites by importing cookies from your browser." Click the “Import cookies” button to import saved logins from your browser in one step. Import works site by site, so you choose which logins to bring over. Banking, email, and single sign-on sites stay unchecked by default.

Importing saved logins is available from Chrome, Edge, and Firefox on macOS, and from Firefox on Windows and Linux (beta). Import isn't available from Safari.

You can also sign in to sites as you go, and Claude remembers your logins across Cowork sessions so you don't have to sign in again.

## What Claude can see

The built-in browser is separate from your own browser. Claude doesn't see your saved logins unless you choose to import them.

**Note:** Anything you sign in to inside the built-in browser is available to Claude in future Cowork sessions on that computer. Be deliberate about which sites you sign in to, especially sites that handle money or personal information.

## Built-in browser or Claude in Chrome

Cowork can use the web in two ways:

- **Built-in browser.** Claude works in its own browser in the side panel. Nothing to install, and it doesn't touch your tabs or logins. Use it when you want to hand off the web part of a task and keep working.

- **Claude in Chrome.** Claude works in your own Chrome browser through the Claude in Chrome extension, on the page you're already on, with the accounts you're already signed in to. Use it when the work is on a page in front of you. Learn more in **[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173)**.

If you already use Claude in Chrome, it stays your default for web tasks in Cowork. If you don't have the extension, or you're new to browser use in Cowork, Claude uses the built-in browser once it's available to you.

## Change which browser Claude uses

You can switch the default at any time:

1. Open the Claude Desktop app and go to **Settings > Cowork**.

2. Under **Preferred browser**, choose “Built-in browser” or “Chrome (Claude in Chrome)”.

Claude uses your preferred browser for web tasks unless you ask it to use the other one.

If you choose the built-in browser as your preferred browser, tasks started on web or mobile use the browser in your desktop app as long as the app is open and online. If your preferred browser is Claude in Chrome, tasks on web or mobile use the extension directly; your session needs to be connected to a desktop, but the app doesn't have to be open.

If your preferred browser isn't available, Claude tells you and continues with the other one. If you ask for a specific browser by name and it isn't available, Claude tells you and asks before using the other one.

---

## Safety

The built-in browser runs the same safeguards as Claude in Chrome:

- Claude asks for your permission before acting on a site for the first time.

- High-risk sites are blocked.

- Every action runs through safety checks that compare what Claude is doing with what you asked for.

Any AI agent that acts in a browser can be targeted by prompt injection, where instructions hidden in a webpage try to redirect Claude. These safeguards reduce that risk but can't remove it. Start with sites you trust, stay close to tasks with real consequences, and stop the task if something looks off.

Learn more in **[Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428)** and **[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135)**.

**Important:** We strongly advise against using the built-in browser or Claude in Chrome to manage or take actions involving sensitive information, such as financial accounts, medical information, or other people's personal data.

---

## On Team and Enterprise plans

Your organization's owner controls whether the built-in browser and Claude in Chrome are available. If you don't see the built-in browser, or the **Preferred browser** setting is missing an option, contact your admin. For admin documentation, see **[Set up browser use in Claude Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/16635803)**.