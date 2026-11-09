> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows fleet checklist

> Windows device, MSIX installer, application control, and virtualization checks to make before you deploy Claude Desktop for Claude for Government.

> **Who this is for:** IT administrators and desktop engineering teams who are preparing a Windows fleet for Claude Desktop connected to Claude for Government.

Use this checklist to confirm what your devices and policies need before you push Claude Desktop to a Windows fleet. Several items concern the virtual machine that Claude Desktop runs on each device for Cowork, the agentic workspace in Claude Desktop, and for Advanced file analysis in Chat. When every item is in place, follow [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md) to deliver the managed settings and the app.

## Device requirements

* **Windows version and architecture.** See the Claude Desktop [system requirements](https://claude.com/docs/third-party/claude-desktop/installation.md#system-requirements). Devices in Windows S mode cannot run Claude Desktop.
* **Memory and disk.** Plan for at least 8 GB of memory and about 20 GB of free space on the drive that holds `%LOCALAPPDATA%`. Cowork keeps its workspace there. Cowork still starts on a device with less memory, but tasks run slowly.

## Installer and packaging

* **Use the `.msix` package.** Cowork is available only when Claude Desktop is installed from the `.msix` package. The legacy `.exe` installer gives you Claude Desktop without Cowork. See [Install the app](https://claude.com/docs/third-party/claude-desktop/installation.md#install-the-app).
* **Install machine-wide.** Have your management system (for example Intune or Configuration Manager) provision the package for all users from the system account, or provision it from an elevated PowerShell session with `Add-AppxProvisionedPackage` or the equivalent DISM command. The package registers a Windows service that Cowork uses, so an install run by a standard user fails, and installing it yourself requires a local administrator. The [Windows deployment guide](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows) covers downloading and distributing the package.
* **Allow trusted app installation.** Make sure Windows policy allows trusted app packages to install from outside the Microsoft Store. If your security baseline configures **Allow all trusted apps to install** (the `ApplicationManagement/AllowAllTrustedApps` policy), set it to enabled. Windows Developer Mode is not required.
* **Intune scripts.** For Intune, Anthropic publishes [install and detection scripts](https://downloads.claude.ai/releases/enterprise/intune/Claude-Intune-README.md) that deploy the `.msix` as a Win32 app, so that Intune keeps reporting the app as installed after the app updates itself.
* **Offline installer.** For networks that cannot reach `downloads.claude.ai`, deploy the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation), which includes the components that the app otherwise downloads from that host, as listed under [Network access](https://claude.com/docs/government/deploy-desktop/configure.md#network-access). On a device that already has the standard package, follow [Replace the standard package with the offline package on Windows](https://claude.com/docs/third-party/claude-desktop/installation.md#replace-the-standard-package-with-the-offline-package-on-windows). To keep devices on those networks from updating themselves, see [Automatic updates](https://claude.com/docs/government/deploy-desktop/configure.md#automatic-updates).
* **Nothing else to pre-install.** The `.msix` package is self-contained, with no separate runtimes or frameworks to install first.
* **Software intake.** The package is MSIX rather than MSI or EXE. If your software intake process names MSI or EXE packages specifically, confirm that it accepts MSIX. An MSIX package installs without prompts when your management system deploys it and takes no vendor-specific switches.
* **Git for Windows.** Code sessions that use a Git worktree need it, and so do [hooks written for Bash](https://claude.com/docs/third-party/claude-desktop/extensions.md#hooks-on-windows-devices-without-git-for-windows). Claude Desktop versions earlier than 2.9939.2 need it for every Code session. On those versions, install Git on the devices whose users will work in Code, or turn **Code in Claude Desktop** off under [Product availability](https://claude.com/docs/government/config/settings.md#product-availability) so that users are not prompted to install Git.

## Application control rules

If you enforce application control with AppLocker or App Control for Business (formerly Windows Defender Application Control), allow Claude Desktop by publisher or by package family name rather than by path, and let the rule match any version, so that it keeps matching as the app updates.

| Identifier | Value |
| - | - |
| Package name | `Claude` |
| Package family name | `Claude_pzs8sxrjxfjjc` |
| Publisher display name | Anthropic, PBC |

These values identify the `.msix` package from the download site and the offline installer, and they do not change between versions or architectures.

Claude Desktop runs Chat conversations, Cowork tasks, and Code sessions through an agent helper named `claude.exe`, a separate executable signed by Anthropic. With the standard installer, the app downloads the helper and places it under each user's profile rather than inside the package. The helper runs during conversations, tasks, and Code sessions and connects to your Claude for Government host. If AppLocker executable rules, App Control for Business, or endpoint security software with path-based rules apply on your devices, allow the helper by publisher too, as described under [Endpoint security software](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software).

## Cowork virtualization

Cowork runs the shell commands that Claude issues inside a dedicated virtual machine that the app manages on each device, and Advanced file analysis in Chat uses the same virtual machine. Users install nothing for this, but each device must be able to start the virtual machine. The [Cowork readiness check](https://claude.com/docs/third-party/claude-desktop/installation.md#check-device-readiness) verifies most of these requirements on a device without installing anything or signing in.

* **Virtual Machine Platform.** Enable the **Virtual Machine Platform** optional Windows feature (`VirtualMachinePlatform`) on every device before rollout, for example by running `Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart` from an elevated PowerShell session, then restart the device so that the feature takes effect. Without the feature, users who have Cowork or Advanced file analysis in Chat see an **Additional setup needed** card. Its **Enable** button asks Windows to run PowerShell as an administrator, which a standard user cannot approve.
* **Hardware virtualization.** Turn on hardware virtualization in each device's firmware (Intel VT-x or AMD-V on x64 devices).
* **Service logon right.** If your security baseline manages the **Log on as a service** right through Group Policy or MDM, include the built-in `NT VIRTUAL MACHINE\Virtual Machines` group (SID `S-1-5-83-0`), and keep it out of **Deny log on as a service**. To check a device and change the policy, follow [Windows security policy blocks the Cowork workspace](https://claude.com/docs/third-party/claude-desktop/installation.md#windows-security-policy-blocks-the-cowork-workspace) in the Claude Desktop documentation.
* **Uncompressed application data.** Leave `%LOCALAPPDATA%\Claude-3p` out of NTFS compression and Encrypting File System (EFS) policies, which can keep the virtual machine from starting.
* **Virtual desktops.** On virtual desktop infrastructure, the Windows desktops themselves run as virtual machines, so the app's virtual machine can start only where the hosting platform exposes nested virtualization to them. Run the readiness check on one desktop in each pool, and make Cowork and Advanced file analysis in Chat available to virtual desktop users only where the check passes.

### If some devices are not ready for Cowork

You can deploy Claude Desktop to devices that do not yet meet the [Cowork virtualization](#cowork-virtualization) requirements. First, have a tenant administrator or organization owner set **Claude Desktop home** to **Chat only** under [Product availability](https://claude.com/docs/government/config/settings.md#product-availability) for the devices' users, for example through a [directory group](https://claude.com/docs/government/config/overview.md#group-specific-settings). With **Chat only** in effect, those users keep Chat (without Advanced file analysis), Code is unaffected, and the app does not download or start the virtual machine. Claude Desktop 2.2553.0 or later also does not show them the **Additional setup needed** card. Claude Desktop versions earlier than 1.30096.1 can still show Cowork and download and try to start the virtual machine, but do not run Cowork tasks. Reset **Claude Desktop home** once those devices meet the requirements.

## Configuration, network, and accounts

Confirm the remaining prerequisites on [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md): the registry values under [Windows](https://claude.com/docs/government/deploy-desktop/configure.md#windows), the hosts under [Network access](https://claude.com/docs/government/deploy-desktop/configure.md#network-access), and the user accounts under [Before you begin](https://claude.com/docs/government/deploy-desktop/configure.md#before-you-begin).
