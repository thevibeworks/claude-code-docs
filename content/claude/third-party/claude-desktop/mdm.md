> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with MDM

> Author a full configuration in the app, export it as a profile, and deploy it fleet-wide with Jamf, Intune, Group Policy, or any MDM

On the MDM delivery model, the profile you deploy carries your organization's full configuration, and every device the profile targets gets the same settings.

Before you start, install Claude Desktop on an admin workstation; see [Installation and setup](https://claude.com/docs/third-party/claude-desktop/installation.md). If you deliver configuration from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) instead, follow that page; your profile then carries only the bootstrap keys, but you export and deploy that profile in the same way as described here.

## 1. Build a configuration in the app

Launch Claude Desktop. **Do not sign in or create an Anthropic account**; stay on the login screen. From the macOS menu bar (or on Windows and Linux, the application menu ☰ in the top-left of the login screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure Third-Party Inference…** to open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md).

The window is organized into sections in the left sidebar. Work through them in order; each maps to a group of [configuration keys](https://claude.com/docs/third-party/claude-desktop/configuration.md), and the window validates values as you enter them.

[Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#enabling-unified-claude) is on by default in current versions of Claude Desktop, even if your profile sets `chatTabEnabled`, `chatAdvancedFileAnalysisEnabled`, or `coworkTabEnabled` to `false`.

## 2. Export the profile

To test the configuration on your own machine, click **Apply Changes**, which writes it to your Claude settings and relaunches the app. Once it works, click **Export** and choose one of the formats under [Apply locally or export for a fleet](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md#apply-locally-or-export-for-a-fleet). **Export** leaves your local settings untouched.

### Export a configuration template

A configuration template lists the settings that your device management tool can set for Claude Desktop, and holds no values. Export one when you enter values in your management console or profile editor and don't build a configuration in the app.

From the macOS menu bar (or on Windows and Linux, the application menu ☰ in the top-left of the sign-in screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Export Configuration Template…**. Every checkbox is selected when the window opens. Clear what you don't need, then export and pick where to save the file:

* **Settings to include**: **Standard Claude Desktop** is for devices that use Anthropic's models through claude.ai, and **Third-party inference** is for devices that use your organization's inference provider. Keep both for a fleet with both kinds of device, so that one template covers them all. A setting's help text says when the setting applies in one mode only, or when setting it opens Claude Desktop in third-party mode.
* **Format**: **Group Policy template (ADMX)** saves `Claude-ADMX.zip`, which holds `Claude.admx` and `en-US/Claude.adml`. **Profile Manifest (.plist)** saves `com.anthropic.claudefordesktop.plist`. With both selected, you get `Claude-Configuration-Templates.zip`, which holds all three files.

A template shows each setting under a display name. In the ADMX template, the setting's help text gives its key.

The configuration window's **Export** menu offers the same ADMX template and Profile Manifest with third-party settings only.

Profiles and Group Policy Objects built on an earlier Claude template keep working. To use a setting that only a new ADMX template lists, replace the earlier template:

* **Group Policy central store**: overwrite `Claude.admx` and `en-US\Claude.adml`
* **Intune**: note the values and assignments in the profiles that use the earlier import, delete those profiles, delete that import, import the new files, then create the profiles again, as in Microsoft's [Replace existing ADMX files](https://learn.microsoft.com/mem/intune/configuration/administrative-templates-import-custom). Until the new profiles reach a device, Intune doesn't enforce your Claude settings there.

### Creating profiles for multiple user groups

Many organizations deploy distinct configurations to different populations: for example, a permissive profile for an engineering pilot group and a restricted profile for the broader rollout, or per-region profiles that point at different inference endpoints.

The configuration window can hold multiple named configurations. Use the picker in the top-right of the window:

* **New configuration** creates an empty configuration.
* **Duplicate** copies the current configuration as a starting point for a variant.
* **Rename** and **Delete** manage the list.
* **Reveal in Finder** (**Show in Explorer** on Windows, **Show in file manager** on Linux) opens the folder where saved configurations are stored. Don't set up another device or user account from a copy of these files (see [Unreadable saved API keys](https://claude.com/docs/third-party/claude-desktop/data-storage.md#unreadable-saved-api-keys)). To use a configuration on another device, click **Export**.

Selecting a configuration in the picker loads it for editing; the **applied** badge marks the one currently active on your machine. **Apply Changes** and **Export** each act on whichever configuration is selected, so you can test each one locally and export them independently.

In your MDM, scope each exported profile to the corresponding device or user group. Targeting is handled by your MDM's assignment rules; the configuration name is for your authoring workflow and is not part of the deployed profile.

> [!NOTE]
>
> On macOS, check whether your assignment rules install a profile for the whole computer (a machine profile) or for one user account (a user profile). Give each Mac one machine profile with every key in it; see [Deploy the configuration](#4-deploy-the-configuration). To vary configuration between groups on macOS, scope machine profiles to device groups, or serve per-user configuration from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md).
>
> On Windows, check which registry hive your assignment rules write to. If your assignment rules deliver a profile in user context, it lands in user policy (`HKCU`), and the app ignores user policy entirely when machine policy is present; see [Deploy the configuration](#4-deploy-the-configuration). To vary configuration per user group on Windows, deliver every profile through user policy and keep `HKLM\SOFTWARE\Policies\Claude` empty, or serve per-user configuration from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md).
>
> Before you deliver an exported `.reg` file through user policy, make sure the registry path in the file starts with `HKEY_CURRENT_USER`, not `HKEY_LOCAL_MACHINE`.

## 3. Allow required network egress

The hosts the app needs to reach depend on the configuration you built: your inference provider's endpoint is always required, and each telemetry, update, and service setting you leave enabled adds its own hosts. The configuration window shows the exact allowlist for your settings and can export it as a text file for your network team.

> [!WARNING]
>
> `downloads.claude.ai` is required to run the app regardless of your configuration: it serves the VM workspace bundle and the Claude Code binary. Without it, Chat conversations, Cowork tasks, and Code sessions cannot start on a device that has not yet downloaded these components. App updates often change one or both of these components, and the app then downloads the new versions from the same host. The [offline installer variant](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation) builds both components into the installer package, so Chat conversations, Cowork tasks, and Code sessions on the device start without this host. The app still requests the model catalog from `downloads.claude.ai` unless [`modelCatalogEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#modelcatalogenabled) is `false` or [`modelCatalogUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#modelcatalogurl) names a mirror inside your network, and sessions start whether or not that request succeeds.

Open these hosts on your perimeter firewall before rolling out to devices. See [Telemetry and egress](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths) for the full list of hosts grouped by the setting that controls each one, and for the distinction between the perimeter firewall and the in-app sandbox allowlist.

## 4. Deploy the configuration

Push the exported configuration through your MDM. On macOS and Windows, put all of a device's managed keys in one location, preferably the machine location. To vary configuration per user group, see [Creating profiles for multiple user groups](#creating-profiles-for-multiple-user-groups). The app reads from these locations:

> [tab] macOS
>
> | Source | Path | Precedence |
> | - | - | - |
> | Machine profile | `/Library/Managed Preferences/com.anthropic.claudefordesktop.plist` | Highest |
> | User profile | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` | |
> | Local (user) | `~/Library/Application Support/Claude-3p/configLibrary/` | Lowest |
>
> A `.mobileconfig` profile delivered by MDM lands in the Managed Preferences locations automatically. A profile that your MDM installs for the whole computer is a machine profile, and a profile that it installs for one user account is a user profile. Some MDMs call these computer level and user level.
>
> * **Deploy one machine profile to each Mac**: put the complete configuration in it. If a Mac also has a user profile for the app, copy the keys that you still need into the machine profile, then remove the user profile. Before you upload an exported `.mobileconfig` file, check that its `PayloadScope` is `System`, and change it if it isn't.
> * **Leave profile installation to your MDM**: set Apple's [`allowUIConfigurationProfileInstallation`](https://developer.apple.com/documentation/devicemanagement/restrictions) restriction to `false`. The restriction applies on macOS 13 and later, and also stops users from installing certificates themselves.

> [tab] Windows
>
> | Source | Path | Precedence |
> | - | - | - |
> | Machine policy | `HKLM\SOFTWARE\Policies\Claude` | Highest |
> | User policy | `HKCU\SOFTWARE\Policies\Claude` | |
> | Local (user) | `%LOCALAPPDATA%\Claude-3p\configLibrary\` | Lowest |
>
> A Group Policy Object or Intune configuration profile writes to the registry policy paths. The hives are not merged: when machine policy is present (any `REG_SZ`, `REG_EXPAND_SZ`, or `REG_DWORD` value directly under `HKLM\SOFTWARE\Policies\Claude`, including an empty string, and the key's unnamed default value when set), the app ignores `HKCU\SOFTWARE\Policies\Claude` entirely. Deploy the complete configuration to one hive; machine policy (`HKLM`) is the recommended location.
>
> > [!WARNING]
> >
> > Values must sit directly under `HKLM\SOFTWARE\Policies\Claude` or `HKCU\SOFTWARE\Policies\Claude`. The app never reads values nested in a subkey, as some ADMX-based and Policy CSP tooling writes them: they do not apply as configuration and do not count as machine policy being present. Write values as `REG_SZ` (`REG_DWORD` is also accepted for boolean and integer keys and is read as its decimal value). Avoid `REG_EXPAND_SZ`: the app counts it as machine policy being present but cannot read its contents, so a single `REG_EXPAND_SZ` value under `HKLM` disables user policy without supplying any configuration. The app cannot see `REG_QWORD`, `REG_MULTI_SZ`, or `REG_BINARY` values at all.

> [tab] Linux
>
> The managed location is `/etc/claude-desktop/managed-settings.json`. Set its ownership and permissions as described under [The Linux configuration file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file).

When a managed source sets any key other than the [app-behavior keys and the keys treated like them](#update-keys-and-managed-precedence), the managed configuration takes effect, the in-app configuration window becomes read-only, and locally authored values in `configLibrary/` are ignored.

If you also deploy Claude Code's own managed settings to the same devices, see [Interaction with Claude Code's own managed settings](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings) for how the two combine.

### Restrict a device to one deployment mode

Claude Desktop on 3P runs on the inference provider or bootstrap server in your configuration. In standard Claude Desktop, users sign in to claude.ai. To stop users from switching a device between the two, set [`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentmode) in the managed source:

* **`3p`**: the app uses the connection that the managed source sets, such as an inference provider or bootstrap keys. The sign-in screen doesn't offer **Or sign in with Claude.ai**. With nothing to connect to in the same managed source, the app opens standard Claude Desktop, so set a connection there to keep users from signing in to claude.ai.
* **`1p`**: the app always runs as standard Claude Desktop and ignores inference provider and bootstrap keys.
* **`any`**: the same as leaving the key unset. Where users can switch, the two modes [share some data on the device](https://claude.com/docs/third-party/claude-desktop/data-storage.md#data-shared-with-standard-claude-desktop).

With `3p` or `1p`, a user can't [move the device to an Enterprise Admin Console organization](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile), and the app doesn't offer or accept the [Claude API account sign-in](https://claude.com/docs/third-party/claude-desktop/claude-api.md#which-devices-offer-the-claude-api-account-sign-in). To allow the move only to your organization, set [`forceLoginOrgUUID`](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile) instead. The app ignores `deploymentMode` in a bootstrap response. It treats a misspelled value as `3p`.

`deploymentMode` requires Claude Desktop 4.16336.0 or later. Earlier versions read [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser), and later ones still read it, so an existing profile works as before. On a device without a bootstrap server, `disableDeploymentModeChooser` set to `true` in a managed source does what `3p` does, unless `deploymentMode` is `1p`. On a device with a bootstrap server, the response replaces the profile's `disableDeploymentModeChooser`, so set `deploymentMode` to `3p` in the profile to restrict that device.

While a fleet updates to 4.16336.0, plan for these cases:

* **A profile that gains `3p`, or gains `1p` and sets nothing to connect to**: also set `disableDeploymentModeChooser` to `true` until every device has updated. On a device with a bootstrap server, set it in the response too. If a profile that you export from the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) doesn't set `disableDeploymentModeChooser` to `true`, add the key to the exported file.
* **[The Linux file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file)**: an earlier version treats `deploymentMode` as a key that it doesn't recognize (see [Keys that an earlier version does not recognize](#keys-that-an-earlier-version-does-not-recognize)), so add it to a device's file after that device updates.

### Update keys and managed precedence

A small group of **app-behavior keys** is treated specially, so you can set an update policy, a restart window, or a network proxy from MDM without managing the whole configuration:

* The update keys `disableAutoUpdates`, `autoUpdaterEnforcementHours`, `installedUpdateEnforcementEnabled`, `installedUpdateEnforcementHours`, `updateViaUpdatesHost`, and [`releaseChannel`](https://claude.com/docs/third-party/claude-desktop/configuration#releasechannel).
* The configuration lifecycle keys [`relaunchEnforcementHours`](https://claude.com/docs/third-party/claude-desktop/configuration#relaunchenforcementhours) and [`configRecheckIntervalMinutes`](https://claude.com/docs/third-party/claude-desktop/configuration#configrecheckintervalminutes).
* The network proxy keys `egressProxyUrl` and `egressProxyPacUrl`. See [Network proxy](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#pin-a-proxy-from-managed-configuration).
* The Code session keys [`disableWslSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disablewslsessions) and [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudecodeprocesswrapperenabled). See [Start Code sessions through a corporate launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher).

When a managed source sets only keys from this group (any of them), the device keeps its locally authored configuration and the configuration window stays editable. The group is still enforced as a unit: every key in it is resolved from the managed source alone, so a locally set or bootstrap-served value for any of them is ignored even if the profile sets only one. A profile that sets the update keys but not `relaunchEnforcementHours` or `configRecheckIntervalMinutes` therefore runs their defaults (24 hours and 10 minutes) on those devices, so set them in the same profile when you want other values.

A profile of only these keys leaves what the device connects to in the local configuration, which a user can edit. If a user edits the local configuration to run every session on a server, most of these keys stop applying, including the update, restart, and re-check timing keys and the network proxy keys. The keys `disableAutoUpdates`, `updateViaUpdatesHost`, and `releaseChannel` still apply. To prevent this, set the connection in the profile, or set [`deploymentMode`](#restrict-a-device-to-one-deployment-mode) to `1p` on a device that only signs in to claude.ai.

[`organizationAnnouncement`](https://claude.com/docs/third-party/claude-desktop/configuration#organizationannouncement), [`deploymentLogo`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentlogo) (the logo shown beside the announcement), and [`remoteFileDownloads`](https://claude.com/docs/third-party/claude-desktop/configuration#remotefiledownloads) aren't in the group. A profile that sets one or more of them, alone or beside keys from the group, also leaves the locally authored configuration in force. Such a profile still changes behaviors on the device (see [What a profile or policy changes on a device](#what-a-profile-or-policy-changes-on-a-device)). Update devices before you add one of these keys (see [Keys that an earlier version does not recognize](#keys-that-an-earlier-version-does-not-recognize)). For a profile that also sets `bootstrapUrl`, see [Which configuration source applies on a device](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device).

### What a profile or policy changes on a device

A profile or policy for Claude Desktop, even one that leaves the local configuration in place, changes these behaviors on the device, among others:

* **Sessions in Windows Subsystem for Linux (WSL)**: Claude Desktop refuses them unless machine policy (`HKLM`) sets [`disableWslSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disablewslsessions) to `false`. Claude Desktop ignores a per-user `false`. `disableWslSessions` is an [app-behavior key](#update-keys-and-managed-precedence), so put the app-behavior keys that you use in the same policy.
* **Shell commands in Code sessions**: Claude Code's sandbox turns on where it can run, and shell commands reach no host (see [Unset allowlist in Code sessions](https://claude.com/docs/third-party/claude-desktop/web-tools.md#unset-allowlist-in-code-sessions)). This happens when the profile leaves the local configuration in place and the user left **Allowed egress hosts** at **Not set**. Have the user add the hosts that shell commands need under **Capabilities > Allowed egress hosts** in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md). A profile that holds the whole configuration sets the hosts itself, in `coworkEgressAllowedHosts`.
* **File downloads from an SSH host or WSL**: an unset [`remoteFileDownloads`](https://claude.com/docs/third-party/claude-desktop/configuration#remotefiledownloads) means `limited` on the device. In Claude Desktop 6.6395.0 or later, an unset key means `all` on a device where Claude Desktop finds no profile, policy, or other [sign of an administrator](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#file-downloads-from-the-remote-host).
* **`coworkEgressAllowedHosts` in the profile**: keep [`coworkEgressAllowedHosts`](https://claude.com/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) out of a profile or policy that doesn't set a connection. With that key and without a connection, the profile replaces the user's configuration, and Claude Desktop starts with nothing to connect to.

### Keys that an earlier version does not recognize

Update a device before you add a key that its version of Claude Desktop doesn't recognize. What that version does with the key differs by platform:

* **Windows**: a machine policy (`HKLM`) that holds only keys that the version doesn't recognize turns off the settings from the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md), the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), or a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md). That includes the connection. If the policy also holds a key that the version recognizes, Claude Desktop ignores the unrecognized key.
* **Linux**: an unrecognized key in `/etc/claude-desktop/managed-settings.json` turns off the same settings when the file holds no other key, or only the [app-behavior keys and the keys treated like them](#update-keys-and-managed-precedence). Where the file also sets a connection, the file still applies. In that case, a device that uses the Enterprise Admin Console goes back to the file's settings at its next launch, and features that need Claude Desktop to read every key of the file, such as automatic deletion of idle sessions, can stay off.
* **macOS**: Claude Desktop doesn't see the key and keeps its settings. The profile still changes behaviors on the device (see [What a profile or policy changes on a device](#what-a-profile-or-policy-changes-on-a-device)).

## 5. Distribute the app

Deploy the Claude Desktop installer to enrolled devices using your standard software-distribution mechanism. On launch, the app reads the managed configuration, detects the configured inference provider and credentials, and the sign-in screen offers users the option to start in Claude Desktop on 3P. For Macs whose users have standard accounts, deploy the `.pkg` of Claude Desktop 7.37095.0 or later, so that [updates install with no administrator prompt](https://claude.com/docs/third-party/claude-desktop/installation.md#update-claude-desktop-on-macs-with-standard-user-accounts).

## 6. Deploy organization plugins (optional)

If you're distributing [organization plugins](https://claude.com/docs/third-party/claude-desktop/extensions.md#organization-plugins-admin), push the plugin bundles to the org-plugins directory on each macOS or Windows device alongside the configuration profile. The app picks up the plugins at its next launch.

## Next steps

After deployment, confirm devices picked up the configuration with the checks in [Verifying the deployment](https://claude.com/docs/third-party/claude-desktop/installation.md#verifying-the-deployment).
