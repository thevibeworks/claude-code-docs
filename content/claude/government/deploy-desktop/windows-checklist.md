> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows fleet checklist

> Device, installer, virtualization, policy, network, and account prerequisites to confirm before deploying Claude Desktop across a Windows fleet for Claude for Government.

> **Who this is for:** IT administrators and desktop engineering teams who are preparing a Windows fleet for Claude Desktop connected to Claude for Government.

Use this checklist to confirm what your devices, policies, network, and user accounts need before you push Claude Desktop to a Windows fleet. Several items concern the virtual machine that Claude Desktop runs on each device for Cowork, the agentic workspace in Claude Desktop, and for Advanced file analysis in Chat. When every item is in place, follow [Connect Claude Desktop to Claude for Government](/docs/government/deploy-desktop/configure) to deliver the managed setting and the app.

## Device requirements

* **Windows version and architecture.** Devices need Windows 10 version 2004 (build 19041) or later, including Windows 11, on x64 or Arm64 hardware. See the Claude Desktop [system requirements](/docs/third-party/claude-desktop/installation#system-requirements). Devices in Windows S mode cannot run Cowork.
* **Memory and disk.** Plan for at least 8 GB of memory and about 20 GB of free space on the drive that holds `%LOCALAPPDATA%`. Cowork keeps its workspace there after downloading it the first time a user starts a task. Cowork still starts on a device with less memory, but tasks run slowly.

## Installer and packaging

* **Use the `.msix` package.** Cowork is available only when Claude Desktop is installed from the `.msix` package. The legacy `.exe` installer gives you Claude Desktop without Cowork. See [Install the app](/docs/third-party/claude-desktop/installation#install-the-app).
* **Install machine-wide.** Have your management system (for example Intune or Configuration Manager) provision the package for all users from the system account, or provision it from an elevated PowerShell session with `Add-AppxProvisionedPackage` or the equivalent DISM command. The package registers a Windows service that Cowork uses, so an install run by a standard user fails, and installing by hand requires a local administrator. The [Windows deployment guide](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows) covers downloading and distributing the package.
* **Allow trusted app installation.** Make sure Windows policy allows trusted app packages to install from outside the Microsoft Store. If your security baseline configures **Allow all trusted apps to install** (the `ApplicationManagement/AllowAllTrustedApps` policy), set it to enabled. Windows Developer Mode is not required.
* **Intune scripts.** For Intune, Anthropic publishes [install and detection scripts](https://downloads.claude.ai/releases/enterprise/intune/Claude-Intune-README.md) that deploy the `.msix` as a Win32 app, so that Intune keeps reporting the app as installed after the app updates itself.
* **Offline installer.** For networks that cannot reach `downloads.claude.ai`, deploy the [offline installer](/docs/third-party/claude-desktop/installation#offline-installation), which includes the components that Cowork and Code otherwise download from that host.
* **Nothing else to pre-install.** The `.msix` package is self-contained, with no separate runtimes or frameworks to install first. Git for Windows is needed only on devices whose users will work in Code; see [Before you begin](/docs/government/deploy-desktop/configure#before-you-begin).
* **Software intake.** The package is MSIX rather than MSI or EXE, and Intune, Configuration Manager, and PowerShell deploy MSIX natively. If your software intake process names MSI or EXE packages specifically, confirm that it accepts MSIX. An MSIX package installs without prompts when your management system deploys it and takes no vendor-specific switches.

## Application control rules

If you enforce application control with AppLocker or App Control for Business (formerly Windows Defender Application Control), allow Claude Desktop by publisher or by package family name rather than by path, and let the rule match any version, so that it keeps matching as the app updates.

| Identifier             | Value                  |
| ---------------------- | ---------------------- |
| Package name           | `Claude`               |
| Package family name    | `Claude_pzs8sxrjxfjjc` |
| Publisher display name | Anthropic, PBC         |

These values identify the `.msix` package from the download site and the offline installer, and they do not change between versions or architectures.

Cowork also runs an agent helper, a separate executable signed by Anthropic that the app places under each user's profile rather than inside the package. If AppLocker executable rules or endpoint security software with path-based rules apply on your devices, allow the helper by publisher too, as described under [Endpoint security software](/docs/third-party/claude-desktop/installation#endpoint-security-software).

## Cowork virtualization

Cowork runs the shell commands that Claude issues inside a dedicated virtual machine that the app manages on each device, and Advanced file analysis in Chat uses the same virtual machine. Users install nothing for this, but each device must be able to start the virtual machine. The [Cowork readiness check](/docs/third-party/claude-desktop/installation#check-device-readiness) is a small program that verifies most of the requirements below on a device without installing anything or signing in. Run it on one device of each hardware model, and resolve what it reports before the broad rollout.

* **Virtual Machine Platform.** Enable the **Virtual Machine Platform** optional Windows feature (`VirtualMachinePlatform`) on every device before rollout, for example by running `Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart` from an elevated PowerShell session, then restart the device so that the feature takes effect. Turning the feature on requires administrator rights, so a standard user cannot enable it later.
* **Hardware virtualization.** Turn on hardware virtualization in each device's firmware (Intel VT-x or AMD-V on x64 devices).
* **Service logon right.** The virtual machine runs under an account in the built-in `NT VIRTUAL MACHINE\Virtual Machines` group (SID `S-1-5-83-0`), the same group that Hyper-V and WSL 2 use, so a fleet where either of those works already meets this requirement. You only need to act if your security baseline manages the **Log on as a service** right through Group Policy. In that case, include this group, and keep it out of **Deny log on as a service**.
* **Uncompressed application data.** Leave `%LOCALAPPDATA%\Claude-3p` out of NTFS compression and Encrypting File System (EFS) policies, because the virtual machine's disk cannot start from a compressed or EFS-encrypted folder.
* **Virtual desktops.** On virtual desktop infrastructure, the Windows desktops themselves run as virtual machines, so Cowork can start only where the hosting platform exposes nested virtualization to them. Run the readiness check on one desktop in each pool, and make Cowork available to virtual desktop users only where it passes.

On a device that does not meet these requirements, Chat still works apart from Advanced file analysis, and Cowork reports that it is unavailable. If a device meets them and Cowork still fails to start, check whether endpoint security software is blocking the Cowork agent helper, as described under [Application control rules](#application-control-rules).

## Configuration values

* **Two registry values.** Push the two values described under [Windows](/docs/government/deploy-desktop/configure#windows) as machine policy under `HKLM\SOFTWARE\Policies\Claude`: the required `bootstrapUrl` and the recommended `disableDeploymentModeChooser`. No other values are needed to connect the app, because everything else reaches each user from Claude for Government at sign-in. If your agency distributes Claude Desktop updates itself, also add the value described under [Automatic updates](/docs/government/deploy-desktop/configure#automatic-updates).
* **Delivery order.** Deliver the values before the app wherever you can, so that users land directly on the Claude for Government sign-in screen, as [Order of deployment](/docs/government/deploy-desktop/configure#order-of-deployment) explains.

## Network access

Claude Desktop's own traffic is HTTPS on port 443, and you can allowlist it by hostname. The [Security and data handling](/docs/government/security/security-and-data-handling#network-egress-required-domains-and-proxies) page explains what each connection carries.

* **App traffic.** Allow Claude Desktop on every device to reach the Claude for Government host, which carries the app's configuration and chat traffic.
* **Browser sign-in traffic.** Allow the browser on every device to reach the Claude for Government host, the Claude for Government sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider. Sign-in happens in each user's default browser, not in the app.
* **`downloads.claude.ai`.** The app downloads the Cowork workspace and the Claude Code command-line tool from this host when a user starts a Cowork task, a Code session, or Advanced file analysis in Chat. The offline installer includes both, so devices installed with it need this host only for application updates while automatic updates are on.
* **`www.claudeusercontent.com`.** This host serves the frame that displays artifact previews.
* **Update hosts.** While [automatic updates](/docs/government/deploy-desktop/configure#automatic-updates) are on, also allow the hosts listed under Auto-updates in [Required egress paths](/docs/third-party/claude-desktop/telemetry#required-egress-paths). The telemetry rows there never apply, because Claude for Government does not send telemetry to Anthropic.
* **Hosts your tools and connectors use.** Allow the hosts you add to [Allowed network hosts](/docs/government/config/settings#allowed-network-hosts) (such as package registries), the addresses of any connectors you configure on the Config page (including Microsoft 365 if you set up that connector), and your telemetry collector if you set one.
* **Proxies.** The app and the Cowork workspace follow the operating system's proxy settings, including PAC files, as described under [Network proxy](/docs/third-party/claude-desktop/network-proxy). If your proxy inspects TLS, validate sign-in, a chat, and a Cowork task on a pilot device before rollout.

## User accounts and seats

Make sure every user in the rollout can sign in and has a seat before their device is set up. Each user needs a [routing rule](/docs/government/tenant-admin/identity-and-access) that covers them and a [seat tier](/docs/government/org-admin/seat-tiers) with at least one model enabled. A user without a seat tier can sign in but gets an empty model picker, which can look like a device problem and is covered in the [Troubleshooting](/docs/government/deploy-desktop/configure#troubleshooting) table.
