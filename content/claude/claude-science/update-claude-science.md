> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Claude Science

> Install the latest version of Claude Science on Mac, Windows, or Linux, and get past an Update required message or an update that fails.

Your projects, conversations, and artifacts stay in your data folder. Updating stops running sessions, so afterward select **Resume** in any session that shows it above the message box.

## Update from the app

1. Select **Update now** in the **Update required** box, or **Restart to update** on the "Update available" notice at the lower right of the window. With neither, select **Check for updates** under **Settings > General > About**, then **Restart to update**.
2. If sessions are still running, select **Stop & restart**, which stops them.
3. Leave Claude Science open while it downloads and restarts, which can take several minutes. If it says "Restart timed out", or nothing changes for an hour, start Claude Science the way you usually do. On Windows, don't quit Claude Science first.

## A Mac app in its own window

If **Update now** shows an error in red:

1. Choose **Claude Science > Check for App Updates…** in the menu bar at the top of the screen. If you don't see that menu, click the Claude Science window first.
2. Wait while the window that opens checks and downloads, then select **Restart to update**. If sessions are running, select **Stop session and restart** or **Stop sessions and restart** instead. If macOS asks for an administrator's password and you don't have one, ask your IT team.
3. Send a message. If the **Update required** box comes back, do steps 1 and 2 once more.

If you can't find the menu, leave Claude Science open for ten minutes. Then quit with Command-Q, which stops running sessions (closing the window isn't enough), wait ten seconds, and open Claude Science from your **Applications** folder.

> [!WARNING]
>
> Download Claude Science again only if the window from step 2 says "install the newest Claude Science app over this one", or if Claude Science won't open and says "This copy of Claude Science can't be opened". Then [install Claude Science again](#install-claude-science-again). The download is the app that opens in a browser tab, not the app you have.

## From a terminal or on a server

Run these commands in a terminal on the computer where Claude Science runs. The second one stops running sessions. On Linux, if `command -v bwrap` or `command -v socat` prints a path that isn't in `/usr/bin`, `/usr/local/bin`, or `/bin`, [update from the app](#update-from-the-app) or [install Claude Science again](#install-claude-science-again) instead, and see [not approved](https://claude.com/docs/claude-science/troubleshooting.md#not-approved).

```bash theme={null}
claude-science update
claude-science stop
```

If `claude-science stop` says "Not killing pid", press Ctrl-C in the terminal where Claude Science is running, or restart the computer. If it tells you to remove a file, don't. Then start Claude Science the way you usually do, and open the new link that it prints.

## Install Claude Science again

On a Mac where Claude Science opens in its own window, do this only if [the steps for that Mac](#a-mac-app-in-its-own-window) sent you here, and [get help](#if-the-update-still-fails) if they didn't. On Windows, if an update said "restart aborted" or "The update is installed", follow [the Windows steps](#if-the-update-still-fails) first. Installing again doesn't replace your data folder. If your projects don't appear afterward, don't delete any folders, and get help.

1. Quit Claude Science. On a Mac, Control-click **Claude Science** in the Dock and choose **Quit**. On Windows, right-click its icon in the notification area of the taskbar and choose **Quit Claude Science**.
2. Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open it. On a Mac, choose **Install**.

On Linux, run this installer in a terminal instead, then run `claude-science stop` and start Claude Science again:

```bash theme={null}
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

## If the update still fails

* **On Windows, an update said "restart aborted" or "The update is installed"**: don't quit Claude Science or run `claude-science stop`, and don't shut down or restart your PC, or sign out of Windows. Letting your PC sleep doesn't close Claude Science. If security software is blocking the new version, Claude Science might not open again. Select **Update now** or **Restart to update** again after a few minutes. If it still fails, ask your IT team whether security software is blocking Claude Science, and send them [Where the app stores data](https://claude.com/docs/claude-science/manage-on-devices.md#where-the-app-stores-data). If you don't have an IT team, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support).
* **Claude Science still asks you to update**: on Windows, if an update said "restart aborted" or "The update is installed", follow the entry above instead. On a Mac where Claude Science opens in its own window, quit it with Command-Q, wait ten seconds, then open it from your **Applications** folder. Anywhere else, run `claude-science stop` in a terminal (on a Mac or Linux, if the command isn't found, type `~/.local/bin/claude-science stop`), quit Claude Science if you're on a Mac, then open it again. If `claude-science stop` says "Not killing pid", follow [the terminal steps](#from-a-terminal-or-on-a-server).
* **The message says "restart aborted" or "The update is installed"**: on a Mac or Linux, if you started Claude Science from a terminal, follow [the terminal steps](#from-a-terminal-or-on-a-server). Otherwise, follow [restart aborted](https://claude.com/docs/claude-science/troubleshooting.md#restart-aborted).
* **The message says "the new version couldn't start"**: you're still on the version you had. Updating again, even from a terminal, gets the same version until a newer one is released, so contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) with the exact words you see.
* **On Linux, version 0.1.71 won't start after you typed `claude-science update`**: see [not approved](https://claude.com/docs/claude-science/troubleshooting.md#not-approved) before you try 0.1.71 again. To go back to version 0.1.70, run this command in a terminal on the computer where Claude Science runs, then start Claude Science again (the flag is safe only in this command):
  ```bash theme={null}
  claude-science update --to f866abff --accept-layout-downgrade
  ```
* **Anything else**: on a Mac where Claude Science opens in its own window, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) with your version and the exact words you see. Anywhere else, [install Claude Science again](#install-claude-science-again), and contact support if that doesn't work.
