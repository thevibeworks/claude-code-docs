# Install an artifact as an app

You can install an artifact that Claude makes for you as an app on your Mac or Windows computer. It gets its own window and icon, opens like any other app, and can even interact with the operating system the way any other app might. It enables users to build and share custom apps. This article explains how to build, install, open, and uninstall apps, and how their permissions work.

Installing artifacts as apps is rolling out in beta on Free, Pro, Max, Ultra, Team, and Enterprise plans. You need Claude for Mac or Claude for Windows, version 6.28899.0 or later.

On Team plans, it's on by default, but the highest permission tier, full access to the computer, is off by default until an admin enables it. On Enterprise plans, the entire feature is off until an owner turns it on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans)**.

## How it works

An installed app shows your artifact in a window of its own. It's still the same artifact: when you or another editor changes it, the app changes too. To open an app, you need to be online and signed in to Claude Desktop.

An app can use Claude and your connectors the same way the artifact does. In addition, when you explicitly allow it, installed artifacts can interact with the operating system. This lets them run programs, read files, send notifications, or add macOS menu bar items, depending on what you allow. Learn more about **[artifacts and how to use them](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)**.

**Note:** "Add to Dock," "Add browser shortcut," and "Add to Home Screen" in your browser only add a shortcut. They don't have the desktop features described here.

## Build an app

Describe the app you want in a chat. For example:

- "Make a Pomodoro timer that lives in my menu bar."

- "Make a small Mac app that reminds me to stretch every hour."

- "Make a Windows app that renames the photos in a folder by date."

## Install an app

To install an artifact as an app:

1. Open the artifact in the main Claude Desktop window.

2. Open the artifact's title menu, or right-click the artifact.

3. Select "Install as app."

4. Select "Install" to confirm.

You can also find **Install as app** under **Share**. Artifacts can also build their own install button, if asked to do so. Claude asks you to confirm installation no matter which path you take.

If you don't see "Install as app," update Claude Desktop. On macOS, go to **Claude > Check for Updates**. On Windows, go to **Help > Check for Updates** under the menu button (☰). On Team and Enterprise plans, ask an owner if it's turned on. Some kinds of artifacts can't be installed. See **Current limitations** below.

## Open an app

To open an installed app:

- **macOS:** Open it from the **Claude Apps** folder inside the Applications folder in your home folder. To keep one in the Dock, right-click its icon and select **Options > Keep in Dock**. You can also find your apps in macOS Spotlight and the Apps launcher.

- **Windows:** Open it from the Start menu (**Claude Apps** folder) or from the shortcut on your desktop.

- **In Claude Desktop:** Select "Open installed app" on the artifact, or go to **File > Apps**, select the app, and select "Open." On Windows, **File** is under the menu button (☰).

An app with a menu bar item or system tray icon keeps running after you close its window. To stop it on macOS, quit it from the Dock, or press Cmd+Q while it's the active app. On Windows, select "Exit" in its tray icon's menu.

## Permissions

An app has to ask before it uses any of these features. You answer each request with "Allow" or "Don't allow."

| **Permission**                                      | **What the app can do**                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notifications                                       | Show notifications while you use other apps                                                                                                                       |
| Keyboard shortcuts                                  | Respond to key combinations while you use other apps                                                                                                              |
| Float over other windows                            | Draw content above other windows, and read where the mouse cursor is on your screens                                                                              |
| Menu bar item (macOS) or system tray icon (Windows) | Show an item there while the app is open                                                                                                                          |
| Full access to this computer                        | Run programs and read, change, or delete your files without asking each time. Also covers the permissions above, unless you or your organization turned them off. |

An "Allow" covers one version of the app. After any update, including your own edits, Claude asks again. A "Don't allow" stays until you change it. If an app loads code from another site, that code can change without a new request.

If an app comes from outside your organization, or Claude can't tell who made it, the request shows a warning.

### Full access

**Warning:** An app with full access can run any program and read, change, or delete your files. Only allow it if you trust everyone who wrote the app. Anthropic doesn't review apps before you install them.

- Claude generally doesn't allow apps to request full access if someone outside your organization wrote part of the app or Claude can't confirm who made it.

- On Free, Pro, Max, and Ultra plans, "outside your organization" means any user other than you.

### Change or take back a permission

To change or take back a permission:

- **macOS:** With the app open, click the app's name in the menu bar and select "Permissions."

- **Windows:** Right-click the app's title bar (or press Alt+Space) and select "Permissions."

- **In Claude Desktop:** While the app is open, go to **File > Apps**, select the app, and select "Permissions."

Turning off full access can reload or close the app, so save your work first. It stops the programs the app started, except any that separated themselves from the app. It doesn't undo changes the app already made.

If you lose access to an app, for example because its owner stops sharing it with you, the programs it started stop too. This can take up to about 20 minutes. It can take longer while Claude can't check, such as when it's offline, signed out, or using another organization.

To report an app, select "Report Artifact" in the same menu as "Permissions," if it's available.

## Uninstall an app

To uninstall an app:

1. Go to **File > Apps** in Claude Desktop.

2. Select the app.

3. Select "Uninstall."

On macOS, the app moves to the Trash. On Windows, its shortcuts are removed. If you kept the app in the Dock or pinned it to the taskbar or Start, remove it there too.

Uninstalling removes the permissions you allowed, it doesn't delete the artifact. If the artifact is deleted, taken down, or no longer shared with you, Claude usually offers to uninstall the app when you open it.

## Usage limits

Building an app, and any requests an app makes to Claude, count toward your plan's usage limits. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**.

## Current limitations

Installing artifacts as apps is in beta. At launch:

- **Platforms:** Apps aren't available on Linux, web, or mobile.

- **Templates:** Artifacts made from a template, such as Docs, Slides, or Sheets, can't be installed. Neither can legacy artifacts or live artifacts from Claude Cowork.

- **HIPAA:** Apps aren't available to organizations with HIPAA-ready configurations.

- **Education:** Full access isn't available in Claude for Teachers or to K-12 organizations. Installing apps may also be off or unavailable.

- **Zero data retention (ZDR):** In organizations with zero data retention for Claude Code, you can install apps once an owner turns on **Artifacts** and **Install as app**. These apps aren't covered by zero data retention.

- **Computer use:** On macOS, Claude can see an installed app when it uses your computer, but can't click or type in it.