> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot Claude Science

> Fix errors you see while using Claude Science: being signed out, capacity retries, Agent Failed, environment setup, connectors, git, dictation, and updates.

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
* To retry the environments that failed, select **Retry builds**. For the one ending in `-mcp`, which runs the connectors on your computer, restart Claude Science instead.
* If an environment is marked "Blocked until rebuilt" and the details say package files changed, you can keep its packages: undo the change, if you made one, and restart Claude Science. If it's still blocked a few minutes later, close the sessions that use it and select **Retry builds**. It's rebuilt with only its default packages, so install any others again. Claude Science first tries to save the environment's package list in `~/.claude-science/rebuilt-environments` (`%USERPROFILE%\.claude-science\rebuilt-environments` on Windows). Install only packages you know, because code that ran in the environment can add names to the list.

If the notice reads "Analysis is unavailable" instead, no Python or R code can run until Claude Science restarts. Fix the cause the notice names, then quit and reopen Claude Science. Closing the window or browser tab leaves Claude Science running, so quit it this way:

* **macOS**: Control-click **Claude Science** in the Dock and choose **Quit**.
* **Windows**: right-click its icon in the notification area of the taskbar and choose **Quit Claude Science**.
* **Started from a terminal with `claude-science serve`**: run `claude-science stop` in a terminal.

### failed to load 5 times in a row — automatic retries are paused

This message appears in **Settings > Connectors** on a Featured connector marked **Failed** (hold the pointer over **Failed**) and on the connector's own page. The connector runs on your computer and failed to start five times in a row, so Claude Science stopped trying. Turn the connector off and on again in **Settings > Connectors**, or restart Claude Science.

## Files in granted folders

Code that Claude runs can read but not change granted folders, even with **Read & write**. On Windows, it can change files and folders there whose own permissions let it, such as some that you moved or restored there (see [Sandbox](https://claude.com/docs/claude-science/core-concepts.md#sandbox)). Before version 0.1.73, it could write in **Read & write** folders.

### Claude's code can't write in a granted folder

The error can include `Read-only file system` on Linux, `Operation not permitted` on a Mac, or `Access is denied`, `Access to the path`, or `Permission denied` on Windows. Asking for access again doesn't change it. Your local-command connectors can't write there either, with exceptions on Windows (see [Sandbox](https://claude.com/docs/claude-science/core-concepts.md#sandbox)).

* **To get a result into the folder**: ask Claude to save it there. It saves finished files such as CSVs, PNGs, SVGs, PDFs, and notebooks by itself. In a **Read-only** folder, a card first asks you to choose **Read & write**. Claude makes the file in the session's workspace folder, inside the folder **Settings > Storage > Data location** shows, then copies it to your folder, so a large result needs free space in both. Before a large run, check **Available on disk** in **Settings > Storage > Disk usage**.
* **To get source code into the folder**, such as a `.py` or `.R` file: ask Claude to save it there. In [auto mode](https://claude.com/docs/claude-science/auto-mode.md), it saves most source code without asking. Otherwise, a card asks first, and nothing is saved if nobody answers within 10 minutes. **Allow in this repo** or **Allow in this folder** lets Claude save most source code there without asking until the session ends or Claude Science restarts.
* **For a file Claude doesn't save by itself**, such as a shell script or a JSON, `.zip`, or `.rds` file: tell Claude in a message to put it in the folder. If Claude keeps it as an artifact instead, tell it again. A card asks first and shows the file's text, except for an archive, a saved object, or a JSON file over about 65,000 characters. After three such cards, or one you decline or don't answer, Claude can't show another until your next message.
* **If such a file is too large for a card**: ask Claude to keep it as a downloadable artifact. The limits are about 65,000 characters of text, and 2 GiB for archives, saved objects, and most JSON files. Claude can save a refused long JSON file as CSV or `.jsonl` instead.
* **Other binary files Claude doesn't save by itself, such as `.xls`, `.psd`, or `.whl`**: ask Claude to keep them as downloadable [artifacts](https://claude.com/docs/claude-science/artifacts.md), which aren't cleared when the session ends.
* **To get a many-file result into the folder**, such as a Zarr store or genome index: tell Claude in a message to put it there as one archive, such as a `.tar` file. If Claude keeps it as an artifact instead, tell it again. A card asks first. The card can't show what's inside, and Claude can't unpack the archive there, so do that yourself in a terminal outside Claude Science. List it with `tar -tvf`, move it to a new, empty folder, and run `tar -xf` there, because unpacking replaces files with the same names. Saved file by file, the result can be incomplete, because Claude doesn't save some kinds of file.
* **On a Mac or Linux, Claude can't change some files**, such as executable or read-only ones, or another user's. Ask it to save under another name.
* **If a save is refused because the file is open in another program**: close it there, such as in LibreOffice, Excel, or Word, and ask again. If it isn't open anywhere, delete the hidden lock file beside it, whose name starts with `.~lock.` or `~$`, or have Claude save under another name. For a database with a `-wal`, `.wal`, `-shm`, or `-journal` file beside it, have Claude use another name.
* **On Windows, some saves are refused**: for example, over a file with its own permissions or one open in another program. Claude can't change a read-only file either. Download Claude's version from the session, or ask it to save under another name.
* **To build, or to run a tool that writes beside its input**: ask Claude to copy the needed files to the session's [temporary](#a-file-that-claude-made-is-gone) workspace folder and work there. Do this before a long script run that writes into your granted folder, because the script fails at its first write there and can lose in-memory results.
* **To commit changes**: see [Git in granted folders](#git-in-granted-folders).
* **To add packages to an environment there**: see [Environments in granted folders](https://claude.com/docs/claude-science/tools-and-environments.md#environments-in-granted-folders).
* **To open a SQLite database that won't open there**: ask Claude to copy it and its `-wal` file to the workspace folder. Claude can't replace one in your folder, so have it save changed `.sqlite` or `.duckdb` files under new names.

### A file with `.kept-` in its name

If the chat says a file was replaced and its old version kept, or you find a file such as `data.csv.kept-1a2b3c4d`, the new version has your file's name, and the old one is beside it, with `.kept-` in its name.

Claude Science keeps the old version when another program may be writing your file, when the disk with Claude Science's data folder has less than about 1 GB free and the old version takes up little of the room left on your file's disk, or in a few other cases. With so little room on that folder's disk, check that the new version is complete before removing the old one. On most network drives and Windows drives in WSL, it does this whenever Claude saves over your version, because it can't tell whether another program is writing.

A program that was writing goes on writing to the old version, so close that program before combining the two. Remove old versions yourself when you no longer need them. Until you do, a program that reads every file in your folder, such as a Parquet dataset reader, can take an old version for data without an error. A `.gitignore` line such as `*.csv` doesn't cover them, so add the line `*.kept-*` to keep `git add .` from adding them.

### Nothing saves into granted folders

On a Mac, the notice "Claude can't save files into folders you share with it, and some of its tools won't run, until Apple's Command Line Tools are installed" appears when the tools are missing or broken. Until they work, Claude can't save or change anything in granted folders. You or an administrator can install them in Terminal:

```bash theme={null}
xcode-select --install
```

Claude Science needs no restart. Until the tools are installed, ask Claude to keep a result as an [artifact](https://claude.com/docs/claude-science/artifacts.md), and download it. If a message mentions the Xcode license instead, see [Troubleshooting first launch](https://claude.com/docs/claude-science/get-started.md#troubleshooting-first-launch).

On Linux, the same happens without the notice if `/usr/bin/python3` is missing or older than Python 3.8. Install a newer Python 3 with your distribution's package manager, and check `/usr/bin/python3 --version` in a terminal.

### A file that Claude made is gone

Claude Science clears files Claude didn't save into your folder or as an [artifact](https://claude.com/docs/claude-science/artifacts.md). They're in a workspace folder: the session's, cleared about 12 hours after Claude's last reply, even if the session is still open, or a [delegated track](https://claude.com/docs/claude-science/core-concepts.md#delegation)'s own, cleared about 6 hours after the track ends.

From version 0.1.73, a workspace folder is kept up to 7 days after that reply or the track's end if a program is still writing a file in it. At most 50 folders are kept that long too if Claude saved or tried to save into your folders, ran code naming a **Read & write** folder, or asked for **Read & write** access, even if you declined. On a nearly full disk, that can be fewer, or none. If Claude Science's data folder is on a network drive, as on many clusters, only a program still writing from the same computer counts.

If Claude Science isn't running when the time is up, it clears the folder at its next start. To keep a file, have Claude save it as an artifact.

## Git in granted folders

The messages in this section appear when Claude runs git in the sandbox on a Mac or Linux. On Windows, git commands that write in a granted folder fail too, without these messages and with exceptions (see [Sandbox](https://claude.com/docs/claude-science/core-concepts.md#sandbox)).

### Git can't write here: .git is read-only in the sandbox

Code that Claude runs can't change git repositories in granted folders (see [Files in granted folders](#files-in-granted-folders)). Write commands such as `git add`, `git commit`, `git checkout`, `git fetch`, `git pull`, `git config`, `git init`, and `git clone` fail.

`git log` still runs. `git status` and `git diff` do too, but some things can stop them or make them list changes nobody made, such as Git LFS files ("clean filter 'lfs' failed") and, on Linux, a checked-out submodule in a **Read & write** folder ("not a git repository") or a credential file git tracks, such as `.env` or `.npmrc` ("unsupported file type" from `git diff`).

None of this changes your files.

Don't run git yourself in a repository Claude made, because git outside the sandbox would run its hooks and settings. Check any `git config` command from Claude first, because a setting such as `core.hooksPath` points your git at programs that run outside the sandbox.

* **To commit changes**: run git yourself in a terminal outside Claude Science. In a **Read-only** folder, ask Claude for a diff, read it all, then `git apply` it at the repository's top. Look closely at scripts, build files, git hooks, and CI settings, which later run outside the sandbox.
* **To get Git LFS contents**: run `git lfs checkout` or `git lfs pull` yourself in a terminal outside Claude Science. When Claude runs them in a granted folder, they don't bring in the real contents.
* **To have Claude commit**: have it make a repository in the session's [workspace folder](https://claude.com/docs/claude-science/core-concepts.md#projects-and-sessions) or clone one there from its `https://` address. That folder is [temporary](#a-file-that-claude-made-is-gone), so before it's cleared, have Claude [push to GitHub](#git-and-github) or save the files you want.
* **After a `git push` from a granted folder**: check the server before pushing again. See [Git and GitHub](#git-and-github).

### transport 'file' not allowed

Git run by Claude can't clone, fetch, pull, or push between local folders. Have Claude use the repository's `https://` address or copy only the files it needs.

`uv` stops with "transport 'file' not allowed" when installing from a git address, even `https://`, because it clones from its cache. Have Claude clone the repository into the session's [workspace folder](https://claude.com/docs/claude-science/core-concepts.md#projects-and-sessions) and install from there.

## Git and GitHub

The messages in this section appear when Claude runs git in the sandbox on a Mac or Linux.

### SSH is off inside Claude Science’s sandbox

By design, SSH is off in the [sandbox](https://claude.com/docs/claude-science/core-concepts.md#sandbox). For `github.com`, Claude can push over HTTPS with a GitHub token you save. With the token, a `git@github.com:` remote works as it is. If your organization [manages the network allowlist](https://claude.com/docs/claude-science/admin-controls.md#network-allowlist), ask an admin to check that the [GitHub domains](https://claude.com/docs/claude-science/network-requirements.md#package-management-domains) are on.

Check these limits before you push:

* **A host other than `github.com`**: Claude Science has no built-in sign-in for it
* **A Git LFS repository**: Claude's commits can store LFS files as ordinary files, and a push from the sandbox may not upload them
* **A granted folder**: Claude can push existing commits but can't make new ones. See [Git in granted folders](#git-in-granted-folders).
* **On Linux**: folders such as `.devcontainer` look empty in the sandbox, so git shows their files as deleted. Don't commit those deletions.

For a `github.com` repository that doesn't use Git LFS, follow these steps:

1. Go to **Settings > Credentials**, select **Connect** next to **GitHub**, paste a personal access token that can write to the repository, and select **Save**. To limit the token to one repository, use a [fine-grained token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for it alone, with **Contents** set to **Read and write**. If the button says **Disconnect**, a token is already saved.

2. Ask Claude:

   ```text Prompt wrap theme={null}
   Push my commits with a shell command in the default python environment, using my saved GitHub credential.
   ```

3. Select **Allow for this conversation** on the **Run a shell command?** [permission card](https://claude.com/docs/claude-science/core-concepts.md#permission-cards) if it appears, then on the **Credentials** card.

   By default, the approval lasts for the conversation, and Claude's commands there can use the token without another **Credentials** card. With auto mode on or off, a **Run a shell command?** card can still appear if [Claude Science's check](https://claude.com/docs/claude-science/auto-mode.md#what-auto-mode-checks) is unsure about a command that can use the token. Allowing it runs that one command, and the check still reviews the next such command, even after **Allow for this conversation**. To revoke the approval, go to **Settings > Permissions**, hold the pointer over each **GitHub** row under **Credentials**, and select **Revoke** (the ×).

Check GitHub for your commits, because git can print an error even when the push worked.

These steps also apply to `could not read Username for 'https://github.com'`, and to the `/bin/false` error git printed before Claude Science 0.1.61.

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
