> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started

> Install Claude Science on macOS, Windows, or Linux, sign in with your Claude account, and run your first analysis.

Install Claude Science on your computer, sign in with your Claude account, and run your first analysis. You need a Claude Pro, Max, Team, or Enterprise plan, and on Team and Enterprise plans an Owner must [turn Claude Science on](/docs/claude-science/enable-claude-science) first. For what each plan includes and how usage works, see [Plans and usage](/docs/claude-science/overview#plans-and-usage).

## Install

<Tabs>
  <Tab title="macOS">
    Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and double-click to install. On first launch, the app sets up its runtime and starter Python and R environments, which takes a few minutes, then opens a new tab in your default browser. If no browser tab appears, click **Claude Science** in the Dock.
  </Tab>

  <Tab title="Windows">
    Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open it. It installs Claude Science for your user account, adds **Claude Science** to the Start menu and the desktop, and opens the app in its own window. The installer is signed by Anthropic, PBC. On first launch, Claude Science sets up the sandbox and downloads its app window engine (about 150 MB) from `downloads.claude.ai` before the window appears, so the first start takes longer than later ones, and a notice shows progress. The starter Python and R environments keep setting up in the background for several minutes after the window opens.

    **One-time Windows permission.** If Claude Science asks for one-time permission from Windows so that cells can run git and Command Prompt scripts and PowerShell can change folders, **Yes** lets Windows ask for approval (an administrator's password if you aren't one) and **No** leaves those features off. Python and R cells work either way, and the **Ask Windows now** button under **Settings** > **Permissions** grants the permission later.

    **Notification-area icon.** Closing the window leaves Claude Science running, with an icon in the notification area of the taskbar. Click the icon to reopen the window, or choose **Quit Claude Science** from the icon's menu to stop the app.

    **Updates.** Claude Science checks for updates in the background and shows **Update available** when one is ready; choose **Restart to update** to install it. Administrators who distribute the app themselves can turn the background check off with `[update] auto_update = false` (see [Manage Claude Science on devices](/docs/claude-science/manage-on-devices#deploy-configuration-with-device-management)). To update by hand instead, open a newer installer, which upgrades the installed copy in place and keeps your data.

    **Uninstall.** To remove the app, follow the Windows steps in [Uninstall Claude Science](#uninstall-claude-science).

    **Corporate networks.** Claude Science follows the proxy configured in Windows proxy settings and trusts corporate root certificates installed for the whole computer, so most managed PCs need no Claude Science configuration. See [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks).

    **Differences on Windows:**

    * Claude runs shell commands with PowerShell. Command Prompt scripts, git inside cells, and folder changes in PowerShell need the one-time Windows permission.
    * Only folders on local NTFS or ReFS drives can be granted, not network shares, mapped network drives, FAT or exFAT drives (many USB sticks and memory cards), or a whole drive such as `D:\`. Copy such files to a local folder or attach them in the chat.
    * [Custom connectors](/docs/claude-science/custom-connectors) that run a local command start with `npx`, `node`, `python`, or the full path of a program. Connectors launched through `npm` or a `.cmd`, `.bat`, or `.ps1` file aren't supported.
    * The **Model endpoints** section of **Settings** > **Compute** (NVIDIA BioNeMo NIM) isn't available.

    **Linux version under WSL.** To use Claude Science from a Linux environment on your Windows computer, run the Linux command-line version under Windows Subsystem for Linux (WSL 2, not WSL 1) with Ubuntu 24.04 or later. The Windows app itself doesn't need WSL. Inside the Ubuntu terminal, follow the install steps in the Linux tab, then start Claude Science with `claude-science serve --port 8765 --no-browser` and open the printed link, which starts with `http://127.0.0.1:8765`, in a Windows browser. Projects you create there stay in WSL, and the Windows app keeps its own.

    If Claude Science under WSL shows one of these errors or problems, use the matching fix:

    * `daemon already running`: Claude Science is already running. Run `claude-science url` to print a fresh link, and open it in a Windows browser.
    * `port 8765 is already in use`: another program, or another copy of Claude Science, has that port. Start with a different one, for example `--port 8080`.
    * The link stops working: check that Claude Science is still running with `claude-science status`. If it's still running, run `claude-science url` for a fresh link and open it in a Windows browser. Claude Science stops when WSL shuts down, for example after `wsl --shutdown`. Start it again by running `claude-science serve --port 8765 --no-browser` in the Ubuntu terminal.
    * An SSH host can't be added: under WSL, Claude Science reads the SSH settings in Ubuntu's `~/.ssh`, not the ones in Windows. Copy the host's entry from `C:\Users\<you>\.ssh\config`, and its key file, into Ubuntu's `~/.ssh` folder, then run `chmod 600` on them.
    * `The database is on /mnt/*`: Claude Science's data folder is on a Windows drive, which it can't use under WSL. Move the folder into your Ubuntu home folder, such as the default `~/.claude-science`, and if you set `data_dir` or `--data-dir`, point it there. If you use a folder other than the default, choose a new, empty one, because Claude Science can delete files in that folder that it didn't create.
  </Tab>

  <Tab title="Linux">
    Install the sandbox dependencies, then run the installer. The sandbox needs bubblewrap 0.8.0 or later and socat, and installing them takes administrator (root or `sudo`) access; if you don't have it, ask your system administrator to install them, or see [Run Claude Science without administrator access](/docs/claude-science/run-on-remote-linux-server#run-claude-science-without-administrator-access).

    * Ubuntu or Debian: `sudo apt-get update && sudo apt-get install -y curl bubblewrap socat`
    * Fedora or RHEL: `sudo dnf install -y curl bubblewrap socat`
    * Arch: `sudo pacman -S curl bubblewrap socat`

    Ubuntu 24.04's repositories carry a new enough bubblewrap and Ubuntu 22.04's don't; on any distribution, confirm with `bwrap --version` that the installed version is 0.8.0 or later before you start Claude Science.

    ```bash theme={null}
    curl -fsSL https://claude.ai/install-claude-science.sh | bash
    ```

    ```bash theme={null}
    claude-science serve
    ```

    First launch prints a local URL right away, then continues setting up its starter Python and R environments. To run Claude Science on a remote server and use it from your computer, see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).
  </Tab>
</Tabs>

<Note>
  Claude Science is a local application, not a website, so there's no public URL to visit. On Windows it opens in its own window, and on macOS and Linux it opens in a browser tab. Open it from the application itself: Claude Science in Applications or the Dock on macOS, the Start menu on Windows, or the `claude-science` command on Linux. On a remote server, the sign-in link reaches your browser through an SSH tunnel; see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).
</Note>

## Sign in and complete setup

When the app opens, sign in with your Claude account. On Windows, click the **Sign in on the web** button and confirm with **Continue**; the app opens claude.ai in your default browser and continues in the app window once you approve the sign-in there. No API key is required.

If you approve the sign-in in your browser but Claude Science doesn't continue (for example, on a remote server when the sign-in can't return through the SSH tunnel), sign in with a code instead:

1. Go back to the Claude Science sign-in screen and select **Paste code instead**, then **Open on web**.
2. Approve access in the browser, then copy the whole code the page shows.
3. Paste the code into Claude Science. If the sign-in doesn't continue on its own, select **Continue**.

After sign-in, a setup wizard walks you through enabling connectors and skills, setting which websites Claude can access, and choosing whether memory is on. You can change these at any time in Settings.

<Note>
  Claude Science keeps your data in a single folder in your home directory: `~/.claude-science` on macOS and Linux, and `%USERPROFILE%\.claude-science` on Windows. On Linux, the `claude-science` command itself installs to `~/.local/bin`, and on Windows the app installs to `%LOCALAPPDATA%\Programs\ClaudeScience` and adds that folder to your user PATH. Beyond that, it doesn't modify your existing conda installation, R libraries, or shell configuration. To remove Claude Science, see [Uninstall Claude Science](#uninstall-claude-science).
</Note>

## Run your first analysis

* Open the Example project, or create a new one.
* Start a conversation. Reference a folder on your computer by typing its path or using the @ picker in the composer.
* Review the folder-access card when it appears and choose whether to allow it.
* Review the code-execution card when Claude proposes running code and choose whether to allow it.
* Results appear as artifacts in the Files panel.

## Uninstall Claude Science

Uninstalling removes the application and keeps your data folder. Your projects, artifacts, and conversation history stay on your computer until you delete that folder.

<Warning>
  Deleting the data folder (`~/.claude-science`, or `%USERPROFILE%\.claude-science` on Windows) removes all your projects, artifacts, conversation history, environments, and settings, and signs you out. Copy anything you want to keep first, with **Download** on an artifact or by copying the project's folder from inside the data folder.

  Before you uninstall, check where your data is under **Settings > Storage > Data location**. If it shows a folder other than the default, the default folder still holds your environments and your sign-in, and it can also hold projects from before that location was set. To remove all your data:

  * The folder that **Data location** shows holds your current projects. Move anything else you stored there yourself out of it, then delete that folder.
  * Delete the default folder (`~/.claude-science`, or `%USERPROFILE%\.claude-science` on Windows).

  Files in the folders you granted Claude access to aren't affected unless they're inside the folder that **Data location** shows.
</Warning>

<Tabs>
  <Tab title="macOS">
    <Steps>
      <Step title="Quit Claude Science">
        In the Dock, Control-click the **Claude Science** icon and choose **Quit**. If you started Claude Science from Terminal with `claude-science serve`, also run `claude-science stop`.
      </Step>

      <Step title="Move the application to the Trash">
        In Finder, open the **Applications** folder and move **Claude Science** to the Trash. If **Claude Science** isn't there, look in the **Applications** folder inside your home folder.
      </Step>

      <Step title="Remove the Terminal command">
        The app also adds a `claude-science` command for Terminal. Remove it with `rm ~/.local/bin/claude-science`.
      </Step>
    </Steps>

    To remove your data as well, delete the `~/.claude-science` folder.
  </Tab>

  <Tab title="Windows">
    <Steps>
      <Step title="Quit Claude Science">
        Right-click the Claude Science icon in the notification area of the taskbar and choose **Quit Claude Science**. The uninstaller doesn't run while the app is running.
      </Step>

      <Step title="Uninstall the app">
        In Windows **Settings**, go to **Apps > Installed apps** and uninstall **Claude Science**, or run `claude-science uninstall` in a terminal.

        To remove the app and your data together, use `claude-science uninstall --purge` instead. It deletes the whole folder your data location points to, including anything you stored there yourself, so move those files out first.

        When your data location isn't `%USERPROFILE%\.claude-science`, `--purge` leaves that folder in place. It still holds your environments and your sign-in, and it can also hold projects from before that location was set. To remove those too, delete `%USERPROFILE%\.claude-science` yourself.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Linux">
    For the Linux version under Windows Subsystem for Linux (WSL), run these commands in the Ubuntu terminal.

    <Steps>
      <Step title="Stop Claude Science">
        ```bash theme={null}
        claude-science stop
        ```
      </Step>

      <Step title="Delete the command">
        ```bash theme={null}
        rm ~/.local/bin/claude-science
        ```

        If you installed it somewhere else, `command -v claude-science` shows where.
      </Step>
    </Steps>

    To remove your data as well, delete the `~/.claude-science` folder.
  </Tab>
</Tabs>

To reinstall, follow [Install](#install) again. Installing doesn't replace an existing data folder.

## Troubleshooting first launch

* macOS says the application isn't supported, or the app icon appears crossed out: the download page picked the build for the wrong processor. Return to the download page and choose Mac (Intel) or Mac (Apple Silicon) to match your Mac. To check which you have, open the Apple menu, choose About This Mac, and look at the Chip or Processor line.
* No browser tab appeared on macOS or Linux: on macOS, click **Claude Science** in the Dock. On Linux, copy the printed URL into a browser on the same machine, or run `claude-science url` to print a fresh one.
* On macOS, some of Claude's tools can't start and the error mentions the Xcode license, usually right after an Xcode update: macOS won't run the Python that comes with Apple's developer tools until the license is accepted. Open Xcode and agree to the license with an administrator account, or run `sudo xcodebuild -license accept` in Terminal, then ask Claude to try again.
* A Claude Science message on Windows says the app was not installed because the file could not be confirmed: the copy you opened still runs but isn't installed. Download the installer again from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open the new file. If the message persists, the PC could not verify the publisher's signature, so ask your IT team.
* The Windows app reports that it couldn't set up the app window engine: the first launch downloads that engine from `downloads.claude.ai`, and this usually means the app couldn't reach it. Check the internet connection, and on a corporate network ask IT to allow that domain (see [Network requirements](/docs/claude-science/network-requirements)).
* On Linux, the installer stops with `The download service may be unreachable, or not yet available in your region`: the installer couldn't get the latest version from `storage.googleapis.com`. Check the internet connection, and on a corporate network ask IT to allow that domain (see [Network requirements](/docs/claude-science/network-requirements#app-connections)). Claude Science is available where Anthropic offers claude.ai. See [Supported countries and regions](https://www.anthropic.com/supported-countries).
* On Linux, the shell reports `command not found` for `claude-science`: `~/.local/bin` isn't on your PATH. Add the PATH line that the installer printed to your shell profile, then open a new terminal.
* On Linux, `claude-science serve` stops with `Sandbox unavailable: bwrap not found on PATH`: bubblewrap isn't installed, or isn't on your PATH. Install bubblewrap and socat with the command for your distribution in the Linux tab of [Install](#install).
* On Linux, `claude-science serve` stops with `Sandbox unavailable: bwrap too old`: the installed bubblewrap is older than 0.8.0. Check the version with `bwrap --version`, then upgrade bubblewrap. Ubuntu 24.04's repositories carry a new enough version and Ubuntu 22.04's don't.
* On Linux, `claude-science serve` stops with `Sandbox unavailable: bwrap cannot create unprivileged user namespaces`: the kernel or an AppArmor profile blocks the sandbox from creating user namespaces. The rest of the message names the settings to check on Ubuntu, Debian, and other distributions, and changing them takes administrator (`sudo`) access.
* On Linux, an error says `socat is required for Linux sandbox networking but was not found in PATH`: socat isn't installed, or isn't on your PATH. Install socat with the command for your distribution in the Linux tab of [Install](#install).
* Projects from another computer don't appear: by design, Claude Science keeps your work on the computer where it's installed, so each computer starts with its own projects. Your earlier projects are still on the other computer. See [Use Claude Science on more than one computer](/docs/claude-science/multiple-computers).
* Projects you created under another sign-in on this computer don't appear automatically, for example, after you move from a personal plan to your organization's Team plan: your earlier projects are still in that sign-in's folder. Select the **Review** button on the banner at the top of the home screen, or select **Review** next to **Access previously saved Claude Science work on this computer** under **Settings** > **General** > **Account**, to access them. On Team and Enterprise plans, if there's no banner and the setting is grayed out, your admin controls it. See [Access work from another sign-in on your computer](/docs/claude-science/multiple-computers#access-work-from-another-sign-in-on-your-computer).
* Sign-in stops at claude.ai: your account is on the Free plan (upgrade required), the redirect couldn't return (use **Paste code instead**), or your Team or Enterprise organization hasn't [enabled Claude Science](/docs/claude-science/enable-claude-science) yet.
* After you paste a code, Claude Science says the code wasn't recognized or was issued for an earlier sign-in attempt: select **Open on web** again, approve access, and paste the whole new code. If it says `PKCE state missing or expired` instead, select **Back** and follow the steps in [Sign in and complete setup](#sign-in-and-complete-setup) again.
