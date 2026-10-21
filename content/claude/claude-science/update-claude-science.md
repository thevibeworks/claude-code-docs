> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Claude Science

> Install the latest version of Claude Science on Mac, Windows, or Linux, and get past an Update required message or an update that fails.

Your projects, conversations, and artifacts stay in your data folder. Updating stops running sessions, so afterward select **Resume** in any session that shows it above the message box.

## Update from the app

1. Select **Update now** in the **Update required** box, or **Restart to update** on the "Update available" notice. With neither, select **Check for updates** under **Settings > General > About**, then **Restart to update**.
2. If sessions are still running, select **Stop & restart**, which stops them.
3. Leave Claude Science open while it downloads and restarts.

## A Mac app in its own window

If **Update now** shows an error in red:

1. Quit Claude Science with Command-Q, which stops running sessions. Closing the window isn't enough.
2. Wait ten seconds, open Claude Science from your **Applications** folder, and send a message.
3. If the **Update required** box comes back, choose **Claude Science > Check for App Updates…** in the menu bar. When the window says "Ready to update", select **Restart to update**.

> [!WARNING]
>
> Download Claude Science again only if that window says "install the newest Claude Science app over this one", or if Claude Science won't open and says "This copy of Claude Science can't be opened". Then [install Claude Science again](#install-claude-science-again). The download is the app that opens in a browser tab, not the app you have.

## From a terminal or on a server

Run these commands in a terminal on the computer where Claude Science runs. The second one stops running sessions.

```bash theme={null}
claude-science update
claude-science stop
```

If `claude-science stop` says "Not killing pid", press Ctrl-C in the terminal where Claude Science is running, or restart the computer. If it tells you to remove a file, don't. Then start Claude Science the way you usually do, and open the new link that it prints.

## Install Claude Science again

On a Mac where Claude Science opens in its own window, do this only if [the steps for that Mac](#a-mac-app-in-its-own-window) sent you here, and [get help](#if-the-update-still-fails) if they didn't. Installing again doesn't replace your data folder. If your projects don't appear afterward, don't delete any folders, and get help.

1. Quit Claude Science. On a Mac, Control-click **Claude Science** in the Dock and choose **Quit**. On Windows, right-click its icon in the notification area of the taskbar and choose **Quit Claude Science**.
2. Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open it. On a Mac, choose **Install**.

On Linux, run this installer in a terminal instead, then run `claude-science stop` and start Claude Science again:

```bash theme={null}
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

## If the update still fails

* **Claude Science still asks you to update**: on a Mac where Claude Science opens in its own window, quit it with Command-Q, wait ten seconds, then open it from your **Applications** folder. Anywhere else, run `claude-science stop` in a terminal (on a Mac or Linux, if the command isn't found, type `~/.local/bin/claude-science stop`), quit Claude Science if you're on a Mac, then open it again. If `claude-science stop` says "Not killing pid", follow [the terminal steps](#from-a-terminal-or-on-a-server).
* **The message says "restart aborted"**: follow [restart aborted](/docs/claude-science/troubleshooting#restart-aborted).
* **Anything else**: on a Mac where Claude Science opens in its own window, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) with your version and the exact words you see. Anywhere else, [install Claude Science again](#install-claude-science-again), and contact support if that doesn't work.
