> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Claude Science

> Fix errors you see while using Claude Science: being signed out, capacity retries, Agent Failed, environment setup, connectors, dictation, and updates.

This page covers error messages that Claude Science shows while you work. Other problems have their own troubleshooting sections:

* Installing and signing in for the first time: [Troubleshooting first launch](https://claude.com/docs/claude-science/get-started.md#troubleshooting-first-launch).
* Running Claude Science on a Linux server: the troubleshooting table on [Run on a remote Linux server](https://claude.com/docs/claude-science/run-on-remote-linux-server.md#troubleshooting).
* Proxies, TLS inspection, and package mirrors: [Troubleshooting corporate network errors](https://claude.com/docs/claude-science/corporate-networks.md#troubleshooting-corporate-network-errors).
* A session that pauses at a usage limit: [When you reach a usage limit](https://claude.com/docs/claude-science/overview.md#when-you-reach-a-usage-limit).

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

Claude is busy or is limiting your requests, and Claude Science is retrying. Claude Science keeps retrying on its own, and once a retry goes through, Claude's reply starts again. Select **Check service status** to see whether there's an incident. To stop waiting, select the stop button in the composer. If your plan's usage limit runs out while Claude Science is retrying, the session pauses instead, as described in [When you reach a usage limit](https://claude.com/docs/claude-science/overview.md#when-you-reach-a-usage-limit).

These other retry messages can appear in the same place:

* "Claude is temporarily unavailable — retrying" means Claude returned a server error and Claude Science is retrying. This message also has a **Check service status** link.
* "Connection issue — retrying" means Claude Science couldn't reach Claude and is retrying. Check your internet connection.

### Agent Failed

An "Agent Failed" box ends a reply when Claude Science hits an error it has no specific explanation for. The box shows the error's own text, and the line under it can show an HTTP status and a request ID. If the box's text is one of the messages on this page, such as "No credentials available for Anthropic API", follow that section instead. If the box says your version "is older than the minimum supported version", see [Update Claude Science](https://claude.com/docs/claude-science/update-claude-science.md). To get help, contact [Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) and include the request ID.

## Python, R, and connectors

Claude Science sets up Python and R environments on your computer so Claude can run code, and it starts the Featured connectors that run on your computer. The messages in this section appear when an environment can't be set up or one of those connectors can't start.

### Environments failed

A notice such as "2 environments failed" means Claude Science couldn't set up one or more of the environments Claude uses to run code, and it names them. Select **Details** to see each environment's status and, for any that failed, the error.

* If setup failed because of your organization's network, the dialog that **Details** opens links to settings for a package mirror, a CA bundle, or mirror credentials. When you save any of these settings, Claude Science retries the failed setups automatically. See also [Troubleshooting corporate network errors](https://claude.com/docs/claude-science/corporate-networks.md#troubleshooting-corporate-network-errors).
* To retry the environments that failed, select **Retry builds**.

If the notice reads "Analysis is unavailable" instead, no Python or R code can run until Claude Science restarts. Fix the cause the notice names, then quit and reopen Claude Science. Closing the window or browser tab leaves Claude Science running, so quit it this way:

* **macOS**: Control-click **Claude Science** in the Dock and choose **Quit**.
* **Windows**: right-click its icon in the notification area of the taskbar and choose **Quit Claude Science**.
* **Started from a terminal with `claude-science serve`**: run `claude-science stop` in a terminal.

### failed to load 5 times in a row — automatic retries are paused

This message appears in **Settings > Connectors** on a Featured connector marked **Failed** (hold the pointer over **Failed**) and on the connector's own page. The connector runs on your computer and failed to start five times in a row, so Claude Science stopped trying. Turn the connector off and on again in **Settings > Connectors**, or restart Claude Science.

## Dictation

You can dictate a message with the microphone button in the composer instead of typing it. The messages in this section appear on the microphone button when dictation can't start.

### Microphone access is blocked

The microphone button in the composer shows a slash, and holding the pointer over it shows this message. Allow the microphone in your system's privacy settings. If Claude Science is open in a browser tab, also allow the microphone in the browser's site settings. Then select the microphone button again.

For the steps, see the help for [Chrome](https://support.google.com/chrome/answer/2693767), [Safari](https://support.apple.com/guide/safari/customize-settings-per-website-ibrw7f78f7fe/mac), [macOS](https://support.apple.com/guide/mac-help/control-access-to-the-microphone-on-mac-mchla1b1e1fe/mac), and [Windows and Microsoft Edge](https://support.microsoft.com/en-us/windows/privacy/windows-camera-microphone-and-privacy).

If holding the pointer over the microphone button shows "No microphone was found." instead, check that a microphone is connected and that your system's privacy settings allow access to it.

## Updates

If Claude Science asks you to update, see [Update Claude Science](https://claude.com/docs/claude-science/update-claude-science.md).

Claude Science shows updates and their errors in these places:

* **In a browser tab and in the Windows app**: an "Update available" notice appears when an update is ready. If installing the update fails, that notice shows the error.
* **In its own window on a Mac**: the **Updates** window shows the update and any error. Open it with **Claude Science > Check for App Updates…** in the menu bar.

### cannot reach the public release endpoint

Claude Science couldn't reach the update server. Check your internet connection, then select **Restart to update** on the "Update available" notice to try again, or run `claude-science update` again. On a corporate network, see [Network requirements](https://claude.com/docs/claude-science/network-requirements.md#app-connections) for the domains Claude Science connects to.

### restart aborted

On the "Update available" notice, this means the new version was downloaded but didn't start. On a Mac or Linux, if the message says "restart aborted" and you started Claude Science from a terminal, follow [the terminal steps](https://claude.com/docs/claude-science/update-claude-science.md#from-a-terminal-or-on-a-server). Otherwise, if Claude Science is still running, it's the version you had, and you can try again: select **Check for updates** under **Settings > General > About**, then select **Restart to update** there. On Windows, if trying again fails, leave Claude Science open and follow [the Windows steps](https://claude.com/docs/claude-science/update-claude-science.md#if-the-update-still-fails). If Claude Science has stopped, start it again.

In version 0.1.67 and later, the notice can show one of these two sentences, with the new version's error on a **Reason** line when there is one:

* "Update failed: the new version couldn't start. You're still on version …" (Linux only) means Claude Science went back to the version you had.
* "The update is installed, but the restart failed. The next start will run the new version." means the new version is in place but didn't start; the steps for "restart aborted" still apply.

### Not updated; the current version still works

On Linux, the "Update available" notice shows these words on its **Reason** line when the new version checked your computer before it was installed and couldn't confirm that it would start there. Claude Science keeps running the version you had. The rest of the line says what the new version needs. If it names bubblewrap or socat, version 0.1.71 and later run both only from system folders or a copy you've approved. Install them with the command for your distribution in the Linux tab of [Install](https://claude.com/docs/claude-science/get-started.md#install). Without administrator access, [get a copy of your own](https://claude.com/docs/claude-science/run-on-remote-linux-server.md#approve-your-own-copy-of-bubblewrap-or-socat) first, then run the install command from that tab again: it keeps the version you have and prints the steps to approve that copy.

### Couldn't check for updates

On a Mac where Claude Science opens in its own window, the **Updates** window shows this message when Claude Science couldn't get update information from Anthropic's update server. The same steps apply when it says "Couldn't download the update":

* If the window says to check your internet connection, check it, then select **Try again**.
* If you cancelled a request from macOS for an administrator's password, select **Try again**.
* Otherwise, such as when it says "Updates aren't available right now", wait a few minutes, then select **Try again**.
* On a corporate network, ask your IT team to allow `storage.googleapis.com` (see [Proxy and certificates for updates in the Mac app window](https://claude.com/docs/claude-science/corporate-networks.md#proxy-and-certificates-for-updates-in-the-mac-app-window)).

### not approved

On Linux, version 0.1.71 can refuse to start after you type `claude-science update` if your bubblewrap or socat isn't in `/usr/bin`, `/usr/local/bin`, or `/bin`. That includes copies from conda, pixi, a cluster module, or your home folder. The refusal includes "Sandbox unavailable:". The `claude-science sandbox approve` command that it suggests then says "not approved", for example if your copy needs a library "which this system does not have".

To go back to version 0.1.70, run this command in a terminal on the computer where Claude Science runs. The flag is safe only in this command, because version 0.1.70 stores sessions the same way as version 0.1.71:

```bash theme={null}
claude-science update --to f866abff --accept-layout-downgrade
```

When it prints "Updated" and `f866abff`, start Claude Science again.

Claude Science then offers 0.1.71 again. Don't type `claude-science update` until you've approved copies that work. [Updating from the app](https://claude.com/docs/claude-science/update-claude-science.md#update-from-the-app) or with the Linux command under [Install Claude Science again](https://claude.com/docs/claude-science/update-claude-science.md#install-claude-science-again) is safe, because you keep your version if the new one can't start.

Instead of going back, run the commands for your case in a terminal, type `y` at "Approve? \[y/N]", and start Claude Science again. If only one of the two tools is your own copy, give only that tool's option, `--bwrap` or `--socat`. If you installed the tools with `pixi global install`, approve pixi's real programs, because its launchers in `~/.pixi/bin`, which `command -v bwrap socat` shows, can't be approved:

```bash theme={null}
claude-science sandbox approve --bwrap ~/.pixi/envs/bubblewrap/bin/bwrap --socat ~/.pixi/envs/socat/bin/socat
```

If those paths don't exist, `ls ~/.pixi/envs/*/bin/bwrap ~/.pixi/envs/*/bin/socat` shows where pixi put the programs.

If you have conda and a network connection, install both tools into a folder of their own and approve those copies:

```bash theme={null}
conda create -y --copy --override-channels -p ~/claude-science-tools -c conda-forge bubblewrap socat
claude-science sandbox approve --bwrap ~/claude-science-tools/bin/bwrap --socat ~/claude-science-tools/bin/socat
```

On 0.1.70, which has no `sandbox approve`, these approve commands don't work. Run the `conda create` line if you use conda, then the Linux install command. In the approval steps that it prints, give the paths of copies that work, such as `~/claude-science-tools/bin/bwrap` and `~/claude-science-tools/bin/socat` or pixi's real programs, not what `command -v bwrap socat` shows, which would be refused. If you have neither conda nor pixi, stay on 0.1.70 and ask your administrator to install bubblewrap 0.8.0 or later and socat in `/usr/local/bin`.

### Not using the data folder that config.toml names

Version 0.1.71 and later check a data folder named `claude-science-data`, with or without capital letters on a Mac or Windows, each time they start. When Claude Science won't use the folder, it shows this message and a reason. After an update fails, the "Update available" notice, or `claude-science update` in a terminal, shows "downloaded binary failed to launch", then the start of this message. On the notice, it's on the **Reason** line. On a Mac where Claude Science opens in its own window, the page says "the app's Claude Science didn't finish starting", and under **details** the message says "Not using the folder `--adopt-install` names". Your data stays in the folder, and if an update failed, you're still on the version you had.

If the reason is "This install did not create it", Claude Science doesn't recognize the folder, for example because you moved it, restored it from a backup, or copied it from another of your computers, or because the folder's name has capital letters. The fixes for this reason make Claude Science accept the files in the folder as its own, without checking where they came from. Files that someone else put there could approve actions or run programs on your computer, so use these fixes only for a folder that you know is yours. If other people can change files in the folder or in the folder that holds it, or the folder came with a project or download that someone else supplied, ask your IT team first. Don't remove the entry that the message names, which can hold your work or your settings.

* **If your update failed and Claude Science still works**: quit Claude Science the way [Environments failed](#environments-failed) describes, because closing its window or tab leaves it running. If the folder's name has capital letters, rename it to `claude-science-data` and end the `data_dir` line of [config.toml](https://claude.com/docs/claude-science/configuration-file-reference.md) with that same name. Then open Claude Science again and update again. If Claude Science opens with none of your work, the `data_dir` line doesn't match the folder's name. Quit, correct the line, and open it again. Your work is still in the folder. If Claude Science won't start, use whichever of the other two fixes fits your computer.
* **On a Mac where Claude Science opens in its own window**: quit Claude Science, then run this command in Terminal as it's written, with its quotation marks and without `sudo`:

  ```bash theme={null}
  "/Applications/Claude Science.app/Contents/Resources/bin/claude-science" serve --no-browser --trust-here-data
  ```

  If Terminal says there's no such file, put `$HOME` in front of `/Applications` and run the command again. When a line that starts with `[daemon] listening on 127.0.0.1:` appears, press Control-C and wait for the prompt to come back. Then open Claude Science from your **Applications** folder.
* **Anywhere else, if Claude Science won't start**: run `claude-science serve --trust-here-data` once, without `sudo`, in a terminal on the computer where Claude Science runs. On a Mac or Linux, if the terminal says the command isn't found, type `~/.local/bin/claude-science serve --trust-here-data` instead. Wait until Claude Science opens with your work or, on a computer with no browser, until a line that starts with `[daemon] listening on 127.0.0.1:` appears. Then press Control-C in that terminal, and open Claude Science as usual.

If two computers that don't share a home folder use the folder, each fix on one makes the other refuse it, so give each computer a folder of its own. Quit Claude Science on both, copy the folder onto one of them, keeping its name `claude-science-data`, and put the copy's whole path on the `data_dir` line of [config.toml](https://claude.com/docs/claude-science/configuration-file-reference.md) on that computer. If Claude Science then won't start on one of them, use the fix that fits that computer once more. From then on, each computer keeps its own work (see [Use Claude Science on more than one computer](https://claude.com/docs/claude-science/multiple-computers.md)).

If the message gives another reason, or none of those causes explains yours, ask your IT team, and don't remove what the message names.

If you have no one to ask, quit Claude Science, make a new, empty folder in your home folder, and put its whole path on the `data_dir` line of [config.toml](https://claude.com/docs/claude-science/configuration-file-reference.md). Claude Science then starts with none of your earlier work, and the old folder stays as it is. If an update failed, update again. Don't copy the old folder's files into the new one.
