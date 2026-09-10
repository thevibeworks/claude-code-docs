> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started

> Install Claude Science on macOS, Windows, or Linux, sign in with your Claude account, and run your first analysis.

## Install

<Tabs>
  <Tab title="macOS">
    Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and double-click to install. On first launch, the app sets up its runtime and starter Python and R environments, which takes a few minutes, then opens a new tab in your default browser. If no browser tab appears, choose Open from the menu bar icon.
  </Tab>

  <Tab title="Windows">
    Download the installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open it. It installs Claude Science for your user account without administrator rights, adds **Claude Science** to the Start menu and the desktop, and opens the app in its own window. The first launch sets up the sandbox and downloads the app window engine (about 150 MB) before the window appears, so it takes longer than later launches, and the starter Python and R environments keep setting up in the background. For requirements, updates, and uninstalling, see [Run on Windows](/docs/claude-science/run-on-windows).
  </Tab>

  <Tab title="Linux">
    Install the sandbox dependencies, then run the installer. The sandbox needs bubblewrap 0.8.0 or later and socat, and installing them takes administrator (`sudo`) access; if you don't have it, ask your system administrator to install them.

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
  Claude Science is a local application, not a website, so there's no public URL to visit. On Windows it opens in its own window, and on macOS and Linux it opens in a browser tab. Open it from the application itself: the menu bar icon on macOS, the Start menu on Windows, or the `claude-science` command on Linux. On a remote server, the sign-in link reaches your browser through an SSH tunnel; see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server).
</Note>

## Sign in and complete setup

When the app opens, sign in with your Claude account. On Windows, the app opens claude.ai in your default browser for this and continues in the app window once you approve the sign-in. If the sign-in redirect can't return to the app (for example, through an SSH tunnel), use the **Paste code instead** option on the sign-in screen. No API key is required.

After sign-in, a setup wizard walks you through enabling connectors and skills, setting which websites Claude can access, and choosing whether memory is on. You can change these at any time in Settings.

<Note>
  Claude Science keeps your data in a single folder in your home directory: `~/.claude-science` on macOS and Linux, and `%USERPROFILE%\.claude-science` on Windows. On Linux, the `claude-science` command itself installs to `~/.local/bin`, and on Windows the app installs to `%LOCALAPPDATA%\Programs\ClaudeScience` and adds that folder to your user PATH. Beyond that, it doesn't modify your existing conda installation, R libraries, or shell configuration.
</Note>

<Warning>
  Deleting the data folder removes all projects, artifacts, and conversation history. Deleting the folder and the application removes Claude Science entirely; on Windows, [uninstall the app](/docs/claude-science/run-on-windows#uninstall) from **Settings** > **Apps** > **Installed apps**.
</Warning>

## Run your first analysis

* Open the Example project, or create a new one.
* Start a conversation. Reference a folder on your computer by typing its path or using the @ picker in the composer.
* Review the folder-access card when it appears and choose whether to allow it.
* Review the code-execution card when Claude proposes running code and choose whether to allow it.
* Results appear as artifacts in the Files panel.

## Troubleshooting first launch

* macOS says the application isn't supported, or the app icon appears crossed out: the download page picked the build for the wrong processor. Return to the download page and choose Mac (Intel) or Mac (Apple Silicon) to match your Mac. To check which you have, open the Apple menu, choose About This Mac, and look at the Chip or Processor line.
* No browser tab appeared on macOS or Linux: on macOS, choose Open from the menu bar icon. On Linux, copy the printed URL into a browser on the same machine, or run `claude-science url` to print a fresh one.
* A Claude Science message on Windows says the app was not installed because the file could not be confirmed: download the installer again from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open the new file. If the message persists, the PC could not verify the publisher's signature, so ask your IT team.
* The Windows app reports that it couldn't set up the app window engine: the first launch downloads that engine from `downloads.claude.ai`, and this usually means the app couldn't reach it. Check the internet connection, and on a corporate network ask IT to allow that domain (see [Network requirements](/docs/claude-science/network-requirements)).
* On Windows, environment builds or other features fail and the PC doesn't have the Microsoft Visual C++ Redistributable (x64): install the latest supported x64 version from [Microsoft's download page](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist), then quit Claude Science from its notification-area icon and open it again.
* Linux refuses to start: a sandbox dependency is missing (install bubblewrap and socat as shown in the Install section), too old, or blocked. Check your bubblewrap version with `bwrap --version`, then match the error message to its fix in the [Linux troubleshooting table](/docs/claude-science/run-on-remote-linux-server#troubleshooting).
* Projects from another computer don't appear: by design, Claude Science keeps your work on the computer where it's installed, so each computer starts with its own projects. Your earlier projects are still on the other computer. See [Use Claude Science on more than one computer](/docs/claude-science/multiple-computers).
* Sign-in stops at claude.ai: your account is on the Free plan (upgrade required), the redirect couldn't return (use Paste a code), or your Team or Enterprise organization hasn't [enabled Claude Science](/docs/claude-science/enable-claude-science) yet.
