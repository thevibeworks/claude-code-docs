# Set up browser use in Claude Cowork for Team and Enterprise plans

Claude can use the web in Claude Cowork in two ways: a browser built into the Claude Desktop app, or your users' own Chrome browser through the Claude in Chrome extension. This article explains the difference, how to enable each one for your organization, and what your users see when both are on.

Browser controls for Cowork are available on Team and Enterprise plans. The built-in browser is rolling out gradually this week and works in the Claude Desktop app on macOS, Windows, and Linux (beta). The **Built-in browser** setting may not appear in Organization settings until the rollout reaches your organization. When the desktop app is online, the built-in browser is also available in Cowork on web or mobile.

## Two ways for Claude to use the web

- **Built-in browser.** Claude works in its own browser, which opens in the Claude side panel inside the Cowork desktop app. There's nothing to install. It's separate from users' own browsers, so Claude doesn't see their logins unless they choose to import them. It requires the desktop app to be open and online.

- **Claude in Chrome.** Claude works in the user's own Chrome browser through the Claude in Chrome extension, on the page they're already on, with the accounts they're already signed in to. Your users' browsers need the extension deployed or installed. Cowork sessions on web and mobile can also use Claude in Chrome when it's the user's preferred browser.

Both run the same safety layers: per-site permission prompts before Claude acts on a new site, a blocklist for high-risk sites, and safety checks on every action. Learn more in **[Use the built-in browser in Claude Cowork](https://support.claude.com/en/articles/16607400)** and **[Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428)**.

You can enable one, both, or neither.

## Enable or disable the built-in browser

- **Team plans:** On by default as it rolls out.

- **Enterprise plans:** Off by default at launch. Starting September 10, 2026, it turns on by default unless you've turned it off.

To turn the built-in browser on or off for your organization:

1. Sign in to Claude as an Owner or Primary Owner.

2. Navigate to **[Organization settings > Cowork](https://claude.ai/admin-settings/cowork)**.

3. Find **Built-in browser** and turn it on or off.

When the built-in browser is off, users can't open it and Claude can't use it. This setting doesn't affect Claude in Chrome or the browser in Claude Code.

**Note:** On Enterprise plans, users aren't notified automatically when you turn the built-in browser on. You may want to communicate availability through your internal channels.

## Enable or disable Claude in Chrome

Claude in Chrome is managed separately, in **[Organization settings > Claude in Chrome](https://claude.ai/admin-settings/browser-extension)**. It's on by default on Team plans. On Enterprise plans, it's off by default; starting September 10, 2026, it turns on by default unless you've already disabled it. Site allowlists and blocklists you configure there apply when Claude works in the extension. For setup, deployment, and pilot guidance, see **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128)**.

## When both are enabled

If your organization has both the built-in browser and Claude in Chrome turned on, each user chooses which one Claude uses with the **Preferred browser** toggle in **[Settings > Cowork](https://claude.ai/settings/cowork)**. Users who already use Claude in Chrome keep it as their preferred browser. Users who don't have the extension get the built-in browser.

Claude uses the preferred browser for web tasks. If the preferred browser isn't available when a task needs one:

- If the user asked Claude to use a browser generally, Claude tells them their preferred browser is offline and continues with the other one.

- If the user asked for a specific browser by name, Claude tells them it's unavailable and asks before using the other one.

The preferred browser setting also applies to Cowork sessions on web and mobile. A session started on web or mobile uses the built-in browser when it's the user's preference and the desktop app is open and online. If Claude in Chrome is the preference, the session uses the extension. For web and mobile sessions to use Claude in Chrome, they must be connected to a desktop, but the app doesn't have to be open.