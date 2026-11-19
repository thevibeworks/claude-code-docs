# Let Claude use your computer in Cowork

Claude can now use your computer to complete tasks in Claude Cowork and Claude Code (refer to our **[Claude Code Docs](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer)** for more information about this). When computer use is enabled and Claude doesn't have a connector or tool for what you need, it may navigate to your screen directly—clicking, typing, and opening apps just like you would. It can work in your browser, open files, and use your apps automatically, with no setup required other than enablement.

## Availability

Computer use is available for Pro, Max, and Ultra plans in Cowork and Claude Code in the Claude Desktop application for both macOS and Windows. On Team and Enterprise plans, computer use is in beta and works only in the new Claude experience, once an owner turns it on for your organization. This is rolling out to organizations gradually. See **Computer use on Team and Enterprise plans** below.

On some Pro, Max, and Ultra accounts, the **Enable computer use** toggle is already on. You'll still be asked to confirm the first time Claude asks to use an app. You can turn it off in **Settings**. See **Get started with computer use** below.

This capability comes with risks—review **[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)** before using it.

The new Claude experience, which combines chat and Cowork, is rolling out to Pro, Max, and Ultra plans. On Team plans (in beta) and Enterprise plans, it's available where **Chat and Cowork unified** is turned on. If your message box no longer shows "Chat" and "Cowork" options, you have the new experience, and some steps in this article may look different. Learn more in **[Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823)**.

---

## How computer use works with Cowork

In Cowork, Claude uses the most precise tool first. When you assign a task, Claude follows this order:

1. **Connectors.** If a connector is available—like Gmail, Google Drive, Microsoft 365, or Slack—Claude uses it. This is the fastest and most reliable path.

2. **Browser.** When there isn't a connector for the tool you need, Claude may work on your task in the browser built into the Claude Desktop app, or in your own Chrome browser through Claude in Chrome if that's your preferred browser. Learn more in **[Use the built-in browser in Claude Cowork](https://support.claude.com/en/articles/16607400)**.

3. **Screen interaction.** Claude uses computer use to interact directly with your screen: clicking, typing, and navigating your desktop apps.

Claude typically prioritizes the fastest method. For example, pulling messages through your Slack connection takes seconds, but navigating Slack through your screen takes much longer and is more error-prone.

---

## What you can do

Computer use lets Claude work with the apps and files on your machine. For example:

- Pull together a competitive analysis using local files and connected tools, then compile it into a formatted report.

- Open your phone simulator, interact with the app you developed, and find UX issues.

- Navigate apps that don’t have connectors—like an internal dashboard or a specialized tool your team uses.

If your work involves a physical machine, Claude keeps working while you step away. Your computer just needs to be on.

On macOS (version 15 or later), Claude works in background windows, so you can keep using your computer while it runs. Claude doesn't take over your pointer or keyboard, and it generally waits if you're in the middle of typing. Claude asks for your permission the first time a task needs the full screen in each session before taking over.

**Note:** Working in the background is the default on macOS 15 or later. If you'd rather have Claude take over the screen while it works, go to the **Computer use** section in **Settings > Capabilities** (or, if it isn't there, **Settings > System**, under **This computer**) and set **How Claude uses the apps you allow** to "Full control."

---

## Permissions and access

Claude asks for your permission before accessing each application. You’ll see a prompt and must approve before Claude can interact with that app. After that, Claude can keep using the app in that session without asking again, and you can stop Claude at any time. Some apps are off-limits by default.

If the **Enable computer use** toggle is on, Claude can list and search the apps installed on your computer, and sometimes see which ones are open, so that it can ask you for the right app. On some Pro, Max, and Ultra accounts, the toggle is on by default. On those accounts, Claude can do this until you turn the toggle off, even if you never turned it on yourself.

Seeing which apps you have doesn't let Claude see your screen or use those apps. Before Claude uses computer use for the first time, you'll be asked to confirm that you want it on. You'll also need to approve each app before Claude can use it.

To stop computer use from showing Claude which apps are installed or open, turn off the **Enable computer use** toggle in **Settings** (see **Get started with computer use** below), then quit and reopen Claude Desktop.

Computer use isn't limited to the folders you've connected. Through the apps you approve, Claude can open, change, or delete files outside those folders. **[Cowork's deletion protection](https://support.claude.com/en/articles/13364135)** doesn't cover computer use.

What Claude can do through computer use in an app you approve depends on the type of app:

- **Browsers, and many investment, trading, and crypto apps:** Claude can see them, but can't click or type in them.

- **Terminals and code editors:** Claude can click and scroll, but can't type. A click can still run code in these apps.

- **Most other apps:** Claude has full access.

Some apps, such as music, video streaming, and e-book apps, are off limits. You can also block apps yourself.

Claude is also trained and instructed to avoid high-risk actions, such as trading stocks or crypto, or typing passwords and card numbers. It's also trained and instructed to check with you about actions your request doesn't clearly cover, such as sending a message or submitting a form. It’s trained and instructed to treat what it sees on screen as information, not instructions, and to tell you if content tries to steer it.

In "Automatically approve" mode only, an automated check also reviews Claude's actions before they run.

These safeguards aren't perfect, and Claude may occasionally act outside these boundaries.

---

## Safeguarding personal data

When Claude uses computer use, Claude takes screenshots of your computer to understand how to navigate the screen and the apps to which you’ve given permission. This means Claude can see any information visible on your screen or those apps, including personal data, sensitive documents, or private information belonging to you or others. The automated check that reviews Claude's actions can also see the latest screenshot, and Anthropic can keep a copy of it in its record of the check.

Be mindful of what's visible when using Claude, especially on apps containing confidential information. Close files or apps with sensitive information before using computer use.

### Claude is trained to avoid

- Trading stocks, crypto, or other investments

- Inputting sensitive data

These guardrails are part of how Claude is trained and instructed, but they aren't absolute. Don't rely on them as a substitute for blocking access to sensitive apps.

### Recommendations

- Do not give computer use permission access to sensitive apps (such as banking, healthcare, government).

- Start with simple tasks like research or organizing rather than complex multi-step workflows.

- Make sure your prompts are specific and carefully tailored to avoid Claude doing things you didn't intend.

### What to avoid

We strongly advise against using computer use to manage or take actions on sensitive information including but not limited to:

- Managing financial accounts or investments

- Handling legal documents or contracts

- Processing medical or health information

- Interacting with apps containing personal information of others

### Memory

Cowork in the cloud shares the memory you use in chat, so Claude can start from what it already knows about how you work. By default, Claude doesn't save topics some people consider sensitive, such as health information, unless you turn on **Include sensitive topics in memory** in **Settings > Your Claude** (or **Settings > Memory** in the older Settings layout). Some information is never saved, including government ID numbers, criminal history, financial account numbers, and immigration status. You can view, edit, and delete what Claude remembers at any time. Learn more about **[Claude's memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#h_82126ebcc9)**.

---

## Safety

Computer use has no sandbox between Claude and your applications. Claude interacts directly with your desktop, and apps—clicking, typing, and navigating your screen. We've built safeguards for this:

- **Per-app permissions.** Claude asks before accessing each application, and there are many investment, trading, and crypto apps that Claude can view, but not click or type in.

- **App blocklist.** Prevent Claude from accessing certain apps by adding them to a blocklist. Any requests from Claude to use blocked applications will be automatically denied.

- **Action review.** Our system scans for signs of prompt injection when Claude uses your computer, and Claude will ask permission before accessing new applications. You can stop Claude at any point. But this capability is still early, and attacks are constantly evolving—stay cautious.

That said, computer use is a new capability, and the threats it guards against are constantly evolving. Claude makes mistakes, and no safeguards are perfect. Start with apps you trust and monitor Claude’s work—especially early on. Note that actions taken in one app can impact other apps. For example, clicking a link in your email app might open it in Chrome, even if you haven’t explicitly granted Claude permission to use Chrome (we can prevent Claude from seeing the Chrome window but can’t stop the link from opening). We don't recommend for use on apps with sensitive data relating to your healthcare, finances, or other personal records.

For detailed safety guidance, see **[Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)**.

---

## Current limitations

Keep the following in mind:

- Your desktop must be active. Your computer needs to be awake and the Claude Desktop app needs to be open for computer use to work.

- Complex tasks sometimes need a second try. Computer use works well for many tasks, but may struggle with complex multi-step workflows.

- Screen interaction is slower than connectors. When Claude works through your screen instead of a direct integration, tasks take longer. Where possible, connect the tools you use most.

- Available for Pro, Max, and Ultra plans. On Team and Enterprise plans, it's available only in the new Claude experience, once an owner turns it on.

---

## Computer use on Team and Enterprise plans

On Team and Enterprise plans, computer use is in beta and off until an owner of your organization turns it on. This is rolling out to organizations gradually.

Computer use works only in the new Claude experience in Claude Desktop, Claude on the web, and Claude Mobile, where there's no separate "Cowork" option. It doesn't work in tasks started with the "Cowork" option, or in Claude Code. Owners can learn more in **[Set up computer use for Team and Enterprise plans](https://support.claude.com/en/articles/18483812-set-up-computer-use-for-team-and-enterprise-plans)**.

You need to open the latest version of Claude Desktop on the computer Claude will use. Turn on **Enable computer use** there, if it isn't already on.

Using it from Claude on the web or Claude Mobile also needs your organization's **Computer access** setting to be on, and the chat must be connected to the computer you want Claude to use. If you're asked which computer to use, choose that computer. In Claude on the web, you can also choose it under "+" > "Devices."

If you can't turn on computer use, hover over the grayed-out toggle to see why:

- **"Computer use isn’t available for your organization."** It hasn't reached your organization yet, or your organization can't have it. If an owner has turned it on, check again in about an hour.

- **"Computer use is off for your organization."** Ask an owner to turn it on. If they just did, check again soon.

- **"Computer use is off for your organization. You can turn it on in Organization settings → Capabilities."** You can turn it on yourself.

- **"Computer use is off for your role. Ask your admin for access."** None of your custom roles include it. Ask whoever manages roles in your organization to give you access.

- **"Computer use needs the new Claude experience, which isn’t on for your account."** Ask an owner, or whoever manages roles in your organization, to give you access.

- **"Your organization has turned on computer use, but this app can’t use it yet. Check again in a little while, and make sure Claude is up to date."** Update Claude Desktop from the **[Claude downloads page](https://claude.com/download)**.

- **"Computer use is disabled by your organization’s policy."** Your organization's compliance setup doesn't allow it, and no setting turns it on.

- **"Your organization has turned off computer use on this computer. Ask your IT administrator for access."** Your organization's IT team controls this. Follow the message.

- **"Couldn’t check whether computer use is allowed on this computer. Quit and reopen Claude to try again. If it’s still off, ask your IT administrator."** Your organization's IT team controls this. Follow the message.

- **"Computer use requires macOS 14 or later."** Update macOS.

If Claude says that your organization blocked an app, or that an app isn't on your organization's list, an owner has most likely limited which apps Claude can use. Ask an owner.

---

## Get started with computer use

To start using computer use:

1. Make sure you have the latest version of Claude Desktop. Download or update at claude.com/download.

2. Open the desktop app and go to **Settings > Capabilities**. If there's no **Computer use** section there, go to **Settings > System**, under **This computer**.

3. Find the **Enable computer use** toggle and turn it on if it isn't already. To turn computer use off, turn this toggle off.

4. Open chat, Cowork, or Claude Code in the desktop app and start a session. On Team and Enterprise plans, start a chat in the new Claude experience instead.

5. Ask Claude to do something that involves an app on your computer. Claude will ask for permission to access the app before proceeding.

If something doesn’t work as expected, use the in-app feedback button or reach out to <usersafety@anthropic.com>.