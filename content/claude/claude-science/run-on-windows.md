> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run on Windows

> Install Claude Science on a Windows PC: requirements, what the installer does, first launch and sign-in, updates, where data lives, and how to uninstall.

Claude Science runs on Windows as a desktop app in its own window. It installs for your user account without administrator rights, and Claude's code runs in a sandbox built on Windows' own app isolation rather than on WSL, Hyper-V, or Docker.

## Requirements

* Windows 11, 64-bit (x64).
* The Microsoft Visual C++ Redistributable (x64), which some Claude Science features depend on. Most PCs already have it. If yours doesn't, install the latest supported x64 version from [Microsoft's download page](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist).
* Free disk space for the app and its analysis environments, as listed under [Claude Science requirements](/docs/claude-science/overview#requirements).
* An internet connection on first launch, to download the app window engine (the component that displays the window, about 150 MB) from `downloads.claude.ai`.
* A Claude account on a Pro, Max, Team, or Enterprise plan.

## Install

Download the Windows installer from [claude.com/product/claude-science](https://claude.com/product/claude-science) and open it. It needs no administrator approval. It installs Claude Science for your user account under `%LOCALAPPDATA%\Programs\ClaudeScience`, adds **Claude Science** to the Start menu and the desktop, puts the `claude-science` command on your PATH, lists the app under **Settings** > **Apps** > **Installed apps**, and opens it. The installer is signed by Anthropic, PBC.

If a Claude Science message says the app was not installed because the file could not be confirmed as the published copy, the copy you opened still runs but isn't installed. Download the installer again and open the new file, and if the message persists, ask your IT team, because the PC could not verify the publisher's signature.

## First launch and sign-in

On first launch, Claude Science sets up the sandbox and downloads its app window engine from `downloads.claude.ai` before the window appears, so the first start takes longer than later ones, and a notice shows progress. The starter Python and R environments keep setting up in the background for several minutes after the window opens.

To sign in, click the **Sign in on the web** button and confirm with **Continue**. Claude Science opens claude.ai in your default browser and continues once you approve the sign-in there; if the browser can't hand the sign-in back, choose the **Paste code instead** option. Then complete the setup wizard as described in [Get started](/docs/claude-science/get-started#sign-in-and-complete-setup).

If Claude Science asks for one-time permission from Windows so that cells can run git and Command Prompt scripts and PowerShell can change folders, **Yes** lets Windows ask for approval (an administrator's password if you aren't one) and **No** leaves those features off. Python and R cells work either way, and the **Ask Windows now** button under **Settings** > **Permissions** grants the permission later.

Closing the window leaves Claude Science running, with an icon in the notification area of the taskbar. Click the icon to reopen the window, or choose **Quit Claude Science** from the icon's menu to stop the app.

## Updates

Claude Science checks for updates in the background and shows **Update available** when one is ready; choose **Restart to update** to install it. Administrators who distribute the app themselves can turn the background check off with `[update] auto_update = false` (see [Manage Claude Science on devices](/docs/claude-science/manage-on-devices#deploy-configuration-with-device-management)). To update by hand instead, open a newer installer, which upgrades the installed copy in place and keeps your data.

## Where Claude Science stores data

Your projects, conversations, artifacts, analysis environments, logs, and `config.toml` live in the data folder, `%USERPROFILE%\.claude-science`, and **Settings** > **Storage** > **Data location** shows the folder in use. The program lives in `%LOCALAPPDATA%\Programs\ClaudeScience`, and launch logs and app state in `%LOCALAPPDATA%\ClaudeScience`.

## Uninstall

Quit Claude Science from its notification-area icon first, because the uninstaller refuses to run while the app is running. Then uninstall **Claude Science** from **Settings** > **Apps** > **Installed apps**, or run `claude-science uninstall` in a terminal. Either way your data is kept. To remove the data as well, run `claude-science uninstall --purge` in a terminal instead.

## Corporate networks

Claude Science follows the proxy configured in Windows proxy settings and trusts corporate root certificates installed for the whole computer, so most managed PCs need no Claude Science configuration. Networks that allow only listed domains must allow `downloads.claude.ai` in addition to the domains every install needs. See [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks) and [Network requirements](/docs/claude-science/network-requirements).

## Differences on Windows

* Claude runs shell commands with PowerShell. Command Prompt scripts, git inside cells, and folder changes in PowerShell need the [one-time Windows permission](#first-launch-and-sign-in).
* Only folders on local NTFS or ReFS drives can be granted, not network shares, mapped network drives, FAT or exFAT drives (many USB sticks and memory cards), or a whole drive such as `D:\`. Copy such files to a local folder or attach them in the chat.
* [Custom connectors](/docs/claude-science/custom-connectors) that run a local command start with `npx`, `node`, `python`, or the full path of a program. Connectors launched through `npm` or a `.cmd`, `.bat`, or `.ps1` file aren't supported.
* The **Model endpoints** section of **Settings** > **Compute** (NVIDIA BioNeMo NIM) isn't available.

## The Linux version under WSL

The Linux command-line version of Claude Science also runs under Windows Subsystem for Linux (WSL 2) with Ubuntu 24.04 or later. Inside the Ubuntu terminal, follow the Linux steps in [Get started](/docs/claude-science/get-started#install), start Claude Science with `claude-science serve --port 8765 --no-browser`, and open the printed link in a Windows browser.
