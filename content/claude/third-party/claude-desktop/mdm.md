> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with MDM

> Author a full configuration in the app, export it as a profile, and deploy it fleet-wide with Jamf, Intune, Group Policy, or any MDM

On the MDM delivery model, the profile you deploy carries your organization's full configuration, and every device the profile targets gets the same settings.

Before you start, install Claude Desktop on an admin workstation; see [Installation and setup](https://claude.com/docs/third-party/claude-desktop/installation.md). If you deliver configuration from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) instead, follow that page; your profile then carries only the bootstrap keys, but it is exported and deployed the same way described here.

## 1. Build a configuration in the app

Launch Claude Desktop. **Do not sign in or create an Anthropic account**; stay on the login screen. From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the login screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure Third-Party Inference…** to open the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md).

The window is organized into sections in the left sidebar. Work through them in order; each maps to a group of [configuration keys](https://claude.com/docs/third-party/claude-desktop/configuration.md), and the window validates values as you enter them.

[Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#enabling-unified-claude) is on by default in current versions of Claude Desktop, even where your profile sets `chatTabEnabled`, `chatAdvancedFileAnalysisEnabled`, or `coworkTabEnabled` to `false`.

> [!NOTE]
>
> When a managed (MDM-delivered) configuration is already present on the device, the configuration window opens read-only: it shows what the admin deployed, marks the configuration as organization-managed, and directs users to their IT administrator. To author a new configuration, use a device without a managed profile, or temporarily remove the profile. Profiles that set only the [app-behavior keys and the keys treated like them](#update-keys-and-managed-precedence) leave the window editable.

## 2. Export the profile

Once your configuration tests successfully, click **Export** and choose a format:

| Format | Platform | Deploy with |
| - | - | - |
| `.mobileconfig` | macOS | Jamf, Kandji, Mosyle, Workspace ONE, or any Apple MDM |
| `.reg` | Windows | Group Policy (import into a GPO), Intune (via custom ADMX or script), or any MDM that can write registry policy |
| `.zip` (ADMX template) | Windows | Schema-only template for Intune or Group Policy; you enter values in the management console |
| `.plist` (Profile Manifest) | macOS | Schema-only template for a profile editor such as iMazing Profile Editor or ProfileCreator; you enter values there to build the profile that your MDM installs |

**Apply Changes** and **Export** do different things:

* **Apply Changes** asks you to confirm, then writes the selected configuration to your own machine's Claude settings and relaunches the app, so you can test it end to end before deploying it.
* **Export** writes a deployment file in the format you choose and leaves your local settings untouched.

### Export a configuration template

A configuration template lists the settings that your device management tool can set for Claude Desktop, and holds no values. Export one when you enter values in your management console or profile editor and don't build a configuration in the app.

From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the sign-in screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Export Configuration Template…**. Every checkbox is selected when the window opens. Clear what you don't need, then export and pick where to save the file:

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

Push the exported configuration through your MDM. On macOS and Windows, put all of a device's managed keys in one location, either machine or user. The app reads from these locations:

> [tab] macOS
>
> | Source | Path | Precedence |
> | - | - | - |
> | Managed (per-user) | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` | Highest |
> | Managed (machine) | `/Library/Managed Preferences/com.anthropic.claudefordesktop.plist` | |
> | Local (user) | `~/Library/Application Support/Claude-3p/configLibrary/` | Lowest |
>
> A `.mobileconfig` profile delivered by MDM lands in the Managed Preferences locations automatically. Both managed paths are read; where a key appears in both, the per-user value wins.

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

When a managed source sets any key other than the [app-behavior keys and the keys treated like them](#update-keys-and-managed-precedence), the managed configuration takes effect, the in-app configuration window becomes read-only, and locally authored values in `configLibrary/` are ignored.

### Restrict a device to one deployment mode

Claude Desktop on 3P runs on the inference provider or bootstrap server in your configuration. In standard Claude Desktop, users sign in to claude.ai. To stop users from switching a device between the two, set [`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentmode) in the managed source:

* **`3p`**: the app uses the connection that the managed source sets, such as an inference provider or bootstrap keys. The sign-in screen doesn't offer **Or sign in with Claude.ai**. With nothing to connect to in the same managed source, the app opens standard Claude Desktop, so set a connection there to keep users from signing in to claude.ai.
* **`1p`**: the app always runs as standard Claude Desktop and ignores inference provider and bootstrap keys.
* **`any`**: the same as leaving the key unset. Where users can switch, the two modes [share some data on the device](https://claude.com/docs/third-party/claude-desktop/data-storage.md#data-shared-with-standard-claude-desktop).

With `3p` or `1p`, a user can't [move the device to an Enterprise Admin Console organization](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile), and the app doesn't offer or accept the [Claude API account sign-in](https://claude.com/docs/third-party/claude-desktop/claude-api.md#which-devices-offer-the-claude-api-account-sign-in). To allow the move only to your organization, set [`forceLoginOrgUUID`](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile) instead. The app ignores `deploymentMode` in a bootstrap response. It treats a misspelled value as `3p`.

`deploymentMode` requires Claude Desktop 4.16336.0 or later. Earlier versions read [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser), and later ones still read it, so an existing profile works as before. On a device without a bootstrap server, `disableDeploymentModeChooser` set to `true` in a managed source does what `3p` does, unless `deploymentMode` is `1p`. On a device with a bootstrap server, the response replaces the profile's `disableDeploymentModeChooser`, so set `deploymentMode` to `3p` in the profile to restrict that device.

While a fleet updates to 4.16336.0, plan for these cases:

* **A profile that gains `3p`, or gains `1p` and sets nothing to connect to**: also set `disableDeploymentModeChooser` to `true` until every device has updated. On a device with a bootstrap server, set it in the response too. If a profile that you export from the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) doesn't set `disableDeploymentModeChooser` to `true`, add the key to the exported file.
* **[The Linux file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file)**: versions before 4.16336.0 treat a key that they don't recognize as an error in `managed-settings.json`, so add `deploymentMode` to a device's file after that device updates.

### Update keys and managed precedence

A small group of **app-behavior keys** is treated specially, so you can set an update policy, a restart window, or a network proxy from MDM without managing the whole configuration:

* The update keys `disableAutoUpdates`, `autoUpdaterEnforcementHours`, `installedUpdateEnforcementEnabled`, `installedUpdateEnforcementHours`, `updateViaUpdatesHost`, and [`releaseChannel`](https://claude.com/docs/third-party/claude-desktop/configuration#releasechannel).
* The configuration lifecycle keys [`relaunchEnforcementHours`](https://claude.com/docs/third-party/claude-desktop/configuration#relaunchenforcementhours) and [`configRecheckIntervalMinutes`](https://claude.com/docs/third-party/claude-desktop/configuration#configrecheckintervalminutes).
* The network proxy keys `egressProxyUrl` and `egressProxyPacUrl`. See [Network proxy](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#pin-a-proxy-from-managed-configuration).
* The Code session keys [`disableWslSessions`](https://claude.com/docs/third-party/claude-desktop/configuration#disablewslsessions) and [`claudeCodeProcessWrapperEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#claudecodeprocesswrapperenabled). See [Start Code sessions through a corporate launcher](https://claude.com/docs/third-party/claude-desktop/code.md#start-code-sessions-through-a-corporate-launcher).

When a managed source sets only keys from this group (any of them), the device keeps its locally authored configuration and the configuration window stays editable. The group is still enforced as a unit: every key in it is resolved from the managed source alone, so a locally set or bootstrap-served value for any of them is ignored even if the profile sets only one. A profile that sets the update keys but not `relaunchEnforcementHours` or `configRecheckIntervalMinutes` therefore runs their defaults (24 hours and 10 minutes) on those devices, so set them in the same profile when you want other values.

A profile of only these keys leaves what the device connects to in the local configuration, which a user can edit. If that connection runs every session on a server and none on the device, that server answers the device's update checks, so the app installs only the updates that the server offers. Update, restart, and re-check timing then comes from that server or takes its default, and most of these keys stop applying, though `disableAutoUpdates` and the network proxy keys still apply. To prevent this, set the connection in the profile, or set [`deploymentMode`](#restrict-a-device-to-one-deployment-mode) to `1p` on a device that only signs in to claude.ai.

[`organizationAnnouncement`](https://claude.com/docs/third-party/claude-desktop/configuration#organizationannouncement) and [`deploymentLogo`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentlogo), the logo shown beside the announcement, aren't in the group. A profile that sets either or both of them, alone or beside keys from the group, also leaves the locally authored configuration in force. The `organizationAnnouncement` entry lists what such a profile changes. For a profile that also sets `bootstrapUrl`, see [Which configuration source applies on a device](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device).

## 5. Distribute the app

Deploy the Claude Desktop installer to enrolled devices using your standard software-distribution mechanism. On launch, the app reads the managed configuration, detects the configured inference provider and credentials, and the sign-in screen offers users the option to start in Claude Desktop on 3P.

## 6. Deploy organization plugins (optional)

If you're distributing [organization plugins](https://claude.com/docs/third-party/claude-desktop/extensions.md#organization-plugins-admin), push the plugin bundles to the org-plugins directory on each device alongside the configuration profile. Plugins are picked up at the next app launch.

## Next steps

After deployment, confirm devices picked up the configuration with the checks in [Verifying the deployment](https://claude.com/docs/third-party/claude-desktop/installation.md#verifying-the-deployment).
