> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Claude Science

> Fix errors you see while using Claude Science: being signed out, capacity retries, Agent Failed, environment setup, connectors, dictation, and updates.

This page covers error messages that Claude Science shows while you work. Other problems have their own troubleshooting sections:

* Installing and signing in for the first time: [Troubleshooting first launch](/docs/claude-science/get-started#troubleshooting-first-launch).
* Running Claude Science on a Linux server: the troubleshooting table on [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server#troubleshooting).
* Proxies, TLS inspection, and package mirrors: [Troubleshooting corporate network errors](/docs/claude-science/corporate-networks#troubleshooting-corporate-network-errors).
* A session that pauses at a usage limit: [When you reach a usage limit](/docs/claude-science/overview#when-you-reach-a-usage-limit).

## Sign-in and replies

The messages in this section appear in a conversation, in place of Claude's reply or under it.

### No credentials available for Anthropic API

Claude Science can't use your Claude sign-in right now, so it can't send your message. Your sign-in may have ended, or a network or server problem may have stopped Claude Science from renewing it automatically.

* If a "You've been signed out" notice appears, select **Sign in** on it, then send your message again.
* If the whole window shows "You've been signed out." instead, follow the step that page names to continue.
* If neither appears, wait a moment and send your message again.
* If the error comes back, sign out and sign in again. Signing out stops any sessions that are still running. Open the account menu (the gear icon at the bottom of the sidebar inside a project, or the account icon at the top right of the home screen), choose **Sign out**, and confirm with **Sign out**. Then sign in and send your message again.

If you see "Your Claude session is no longer valid. Please sign out and sign in again." instead, sign out and sign in again the same way.

Your sign-in lasts a limited time. In the last three days before it expires, Claude Science shows a notice that says when it expires. Select **Sign in again** on that notice to renew your sign-in before it ends.

### Claude is at capacity — retrying

Claude is busy or is limiting your requests, and Claude Science is retrying. Claude Science keeps retrying on its own, and once a retry goes through, Claude's reply starts again. Select **Check service status** to see whether there's an incident. To stop waiting, select the stop button in the composer. If your plan's usage limit runs out while Claude Science is retrying, the session pauses instead, as described in [When you reach a usage limit](/docs/claude-science/overview#when-you-reach-a-usage-limit).

These other retry messages can appear in the same place:

* "Claude is temporarily unavailable — retrying" means Claude returned a server error and Claude Science is retrying. This message also has a **Check service status** link.
* "Connection issue — retrying" means Claude Science couldn't reach Claude and is retrying. Check your internet connection.

### Agent Failed

An "Agent Failed" box ends a reply when Claude Science hits an error it has no specific explanation for. The box shows the error's own text, and the line under it can show an HTTP status and a request ID. If the box's text is one of the messages on this page, such as "No credentials available for Anthropic API", follow that section instead. To get help, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) and include the request ID.

## Python, R, and connectors

Claude Science sets up Python and R environments on your computer so Claude can run code, and it starts the Featured connectors that run on your computer. The messages in this section appear when an environment can't be set up or one of those connectors can't start.

### Environments failed

A notice such as "2 environments failed" means Claude Science couldn't set up one or more of the environments Claude uses to run code, and it names them. Select **Details** to see each environment's status and, for any that failed, the error.

* If setup failed because of your organization's network, the dialog that **Details** opens links to settings for a package mirror, a CA bundle, or mirror credentials. When you save any of these settings, Claude Science retries the failed setups automatically. See also [Troubleshooting corporate network errors](/docs/claude-science/corporate-networks#troubleshooting-corporate-network-errors).
* To retry the environments that failed, select **Retry builds**.

If the notice reads "Analysis is unavailable" instead, no Python or R code can run until Claude Science restarts. Fix the cause the notice names, then quit and reopen Claude Science. On Windows, closing the window leaves Claude Science running, so right-click its icon in the notification area of the taskbar and choose **Quit Claude Science**.

### failed to load 5 times in a row — automatic retries are paused

This message appears in **Settings > Connectors** on a Featured connector marked **Failed** (hold the pointer over **Failed**) and on the connector's own page. The connector runs on your computer and failed to start five times in a row, so Claude Science stopped trying. Turn the connector off and on again in **Settings > Connectors**, or restart Claude Science.

## Dictation

You can dictate a message with the microphone button in the composer instead of typing it. The messages in this section appear on the microphone button when dictation can't start.

### Microphone access is blocked

The microphone button in the composer shows a slash, and holding the pointer over it shows this message. Allow the microphone in your system's privacy settings. If Claude Science is open in a browser tab, also allow the microphone in the browser's site settings. Then select the microphone button again.

For the steps, see the help for [Chrome](https://support.google.com/chrome/answer/2693767), [Safari](https://support.apple.com/guide/safari/customize-settings-per-website-ibrw7f78f7fe/mac), [macOS](https://support.apple.com/guide/mac-help/control-access-to-the-microphone-on-mac-mchla1b1e1fe/mac), and [Windows and Microsoft Edge](https://support.microsoft.com/en-us/windows/privacy/windows-camera-microphone-and-privacy).

If holding the pointer over the microphone button shows "No microphone was found." instead, check that a microphone is connected and that your system's privacy settings allow access to it.

## Updates

When an update is ready, Claude Science shows an "Update available" notice. If installing the update fails, that notice shows the error.

### cannot reach the public release endpoint

Claude Science couldn't reach the update server. Check your internet connection, then select **Restart to update** on the "Update available" notice to try again, or run `claude-science update` again. On a corporate network, see [Network requirements](/docs/claude-science/network-requirements#app-connections) for the domains Claude Science connects to.
