> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Claude Desktop to Claude for Government

> Choose between single-machine setup and fleet deployment, understand the administrator requirements for each, and connect Claude Desktop to Claude for Government.

> **Who this is for:** IT administrators who install Claude Desktop on agency devices and connect it to Claude for Government.

A fresh install of Claude Desktop connects to claude.ai. To connect it to Claude for Government instead, each device needs one managed setting that tells the app where to reach Claude for Government. Once that setting is in place, everything else that governs the app (which products and features are available, model access, [connectors](/docs/government/connectors/overview), usage limits, the Claude Desktop banner) is controlled through the [tenant](/docs/government/tenant-admin/configuration) and [organization](/docs/government/org-admin/configuration) configuration pages in this portal and delivered to each user when they sign in.

## Choose how to deploy

There are two ways to get Claude Desktop installed and connected to Claude for Government. They differ in who runs the installer, what rights that requires, and how the setting reaches the app.

|                                 | Configure a single machine                                                                                                 | Deploy to your fleet                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Best for                        | Confirming the app works on a representative device before a wider rollout, or setting up a small group of devices by hand | Production rollout across your agency                                              |
| Who installs the app            | A person at the device                                                                                                     | Your device management system (for example Intune, Configuration Manager, or Jamf) |
| Administrator rights to install | Needed by the person doing each install                                                                                    | Not needed by end users; the management system installs with elevated rights       |
| How the address is set          | Entered in the app's built-in configuration window                                                                         | Pushed as a configuration profile alongside the app                                |

For a production rollout, use your device management system so end users never need administrator rights. The single-machine path is for testing first or for a small group you set up by hand, with an administrator doing each install. That path can also export a ready-made profile for your management system, so it is a useful starting point even when the fleet path is your destination.

## Before you begin

Confirm each of the following before you start either path.

* **User accounts exist.** Claude Desktop signs users in to the same accounts as this portal. For each user, including your own test account, check with your tenant administrators that the user can sign in (a [routing rule](/docs/government/tenant-admin/identity-and-access) covers them) and has a [seat tier](/docs/government/org-admin/seat-tiers) with at least one model enabled.
* **Devices can reach Claude for Government.** Claude Desktop on every device must reach the Claude for Government host over HTTPS on port 443. That one host carries the app's configuration and chat traffic.
* **Browsers can reach sign-in.** Sign-in happens in the user's default web browser, not in the app. Browsers on each device must reach the Claude for Government host, its sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider.
* **The device meets Claude Desktop's requirements.** See the Claude Desktop [system requirements](/docs/third-party/claude-desktop/installation#system-requirements) for macOS and Windows device requirements. For a Windows fleet, work through the [Windows fleet checklist](/docs/government/deploy-desktop/windows-checklist), which covers the Virtual Machine Platform feature that Cowork needs along with the installer, policy, and network prerequisites.
* **Windows devices used for Code have Git for Windows.** On Windows, only the Code part of Claude Desktop needs Git for Windows. Chat and Cowork work without it. Install Git on the devices whose users will work in Code, or turn **Code in Claude Desktop** off under [Product availability](/docs/government/config/settings#product-availability) so that users are not prompted to install Git.
* **You can install the app.** Installing by hand needs administrator rights on each device; see [Configure a single machine](#configure-a-single-machine) for what that means on each platform. Installing through your device management system does not, because the management system installs with elevated rights. The [macOS deployment guide](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos) and the [Windows deployment guide](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows) cover where to download the installer and how to distribute it.
* **The app is current.** The configuration mechanism on this page requires Claude Desktop 1.10628.0 or later.

## The managed setting

The setting is called `bootstrapUrl`, and its value is the Claude for Government host followed by the fixed path `/gateway-api/user/bootstrap`.

```text theme={null}
https://<claude-for-government-host>/gateway-api/user/bootstrap
```

The Claude for Government host is the same domain name you use to access Claude for Government. If you are unsure of it, ask your Anthropic representative. The app uses the address exactly as entered; it fetches each user's configuration from it and starts sign-in from it, so include the full path.

### How the app uses the bootstrap address

The address is the same for every device and user in your agency and carries no credentials or user information, so the same profile is safe to push to your whole fleet. A request to the address without a signed-in session is refused.

When a user chooses **Sign in with your organization**, the app asks the Claude for Government host to start a sign-in, shows the pairing code it receives, and opens the host's sign-in page in the user's default browser. That page asks for the user's agency email address, then sends the browser to the sign-in service and on to your agency's identity provider. After signing in, the user acknowledges the system-use notification, confirms that the code shown in the browser matches the one in the app, and approves.

Claude for Government then issues the app a session for that user, which the app stores encrypted on the device. The app presents that session, and nothing from the profile, when it downloads the user's configuration from this address and when it sends chat traffic to the same host. It re-checks the configuration about every 30 minutes and at each launch.

The configuration that the app downloads for a user includes the following settings, all of which you manage in this portal.

| What the app receives                                                                                | Where it is set                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Which of Chat, Cowork, and Code the user can open, and whether Advanced file analysis is on in Chat  | [Product availability](/docs/government/config/settings#product-availability) on the Config page                                                                                                    |
| The models the user can choose                                                                       | The user's [seat tier](/docs/government/org-admin/seat-tiers)                                                                                                                                       |
| Connectors, plugins, and the settings for the built-in tools                                         | The [tool and connector cards](/docs/government/config/settings#tool-and-connector-cards) on the Config page                                                                                        |
| The hosts that tools may reach                                                                       | [Allowed network hosts](/docs/government/config/settings#allowed-network-hosts)                                                                                                                     |
| The folders a user can choose as a workspace                                                         | [Allowed workspace folders](/docs/government/config/settings#allowed-workspace-folders)                                                                                                             |
| The banner shown across the top of the app                                                           | [Claude Desktop banner](/docs/government/config/settings#claude-desktop-banner)                                                                                                                     |
| Where the app sends your agency's own telemetry, if you have set a collector                         | [Telemetry endpoint (Claude Desktop)](/docs/government/config/settings#telemetry-endpoint-claude-desktop)                                                                                           |
| Whether automatic updates are blocked, and the restart deadline for an update the app has downloaded | [Block automatic updates](/docs/government/config/settings#block-automatic-updates) and [Restart deadline for updates](/docs/government/config/settings#restart-deadline-for-updates) on the Config page |

## Configure a single machine

<Note>
  Installing by hand needs administrator rights on the device. On Windows, the installer registers a Windows system service, so it must run as a local administrator. On macOS, installing to the shared Applications folder requires an administrator. On Linux, installing the package requires root.
</Note>

Claude Desktop has a built-in configuration window that is hidden until you enable developer mode. These steps use it to set the address on one machine without any management tooling.

<Steps>
  <Step title="Launch the app without signing in">
    Install Claude Desktop on the test machine and open it. On Windows, run the installer while signed in as a local administrator. The claude.ai sign-in screen appears; this is expected before the app is configured. Stay on this screen.
  </Step>

  <Step title="Enable developer mode">
    From the **Help** menu, choose **Troubleshooting**, then **Enable Developer Mode**, and confirm the prompt. On Windows the **Help** menu is under the application menu (☰) on the sign-in screen. The app relaunches with a **Developer** menu added.
  </Step>

  <Step title="Open the configuration window">
    From the **Developer** menu, choose **Configure Third-Party Inference**. This is the correct option for Claude for Government despite the name. The window opens on its **Connection** section.
  </Step>

  <Step title="Enter the bootstrap address">
    In the window's left sidebar, click **Source**. On an unconfigured machine it appears last in the list and is dimmed, but is still clickable. Enter the full address from the section above in the **Bootstrap config URL** field. Leave every other field alone; Claude for Government supplies the provider, credentials, and model list after sign-in.
  </Step>

  <Step title="Apply and sign in">
    Click **Apply Changes** and let the app relaunch. The sign-in screen now offers **Sign in with your organization** alongside the claude.ai option. Choose it. The app shows a pairing code and opens the sign-in page in your browser. Sign in with your agency credentials, confirm that the code in the browser matches the one in the app, and approve. The app picks up the session and opens to Claude.
  </Step>

  <Step title="Run the verification checklist">
    Work through [Confirm it worked](#confirm-it-worked) below.
  </Step>
</Steps>

After the test, the same configuration window has an **Export** menu that produces files ready for your management system: a `.mobileconfig` profile for macOS, a `.reg` file for Windows, an ADMX template for Intune or Group Policy, and a Profile Manifest for Jamf. Before exporting, turn on **Disable Claude.ai sign-in** in the window's **Workspace** section so the exported profile hides the claude.ai option on managed devices.

## Deploy to your fleet

When your device management system deploys Claude Desktop, end users receive the app without running an installer themselves. The management system installs the package with the system or root account on each platform, so end users need no administrator rights and see no elevation prompt. Push both the app installer and the configuration profile below through the same system.

The recommended profile contains two keys. In the macOS and Windows profiles below, write every value as a string exactly as shown, including booleans as the strings `"true"` or `"false"`; the Linux file uses native JSON types, as shown.

| Key                            | Value                                                             | Purpose                                                                                                                                                                                                                                                      |
| ------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bootstrapUrl`                 | `https://<claude-for-government-host>/gateway-api/user/bootstrap` | Required. Points the app at Claude for Government.                                                                                                                                                                                                           |
| `disableDeploymentModeChooser` | `"true"`                                                          | Recommended. Hides the claude.ai sign-in option so users can only sign in to Claude for Government. Like any recognized key other than the automatic update settings, it also marks the device as managed (see [Order of deployment](#order-of-deployment)). |

No other keys are needed to connect the app; Claude for Government supplies everything else per user after sign-in. If your agency distributes Claude Desktop updates itself, [Automatic updates](#automatic-updates) below describes one more key to add. The profile contains no secrets, only a host. Keys documented for other Claude plans, such as `forceLoginOrgUUID` or `loginSsoOrgDomain`, apply only to claude.ai workspaces and are not used here.

### macOS

Claude Desktop reads managed preferences in the `com.anthropic.claudefordesktop` domain. Deploy a configuration profile that sets the two keys in that domain as strings.

```xml theme={null}
<key>bootstrapUrl</key>
<!-- substitute the Claude for Government host -->
<string>https://<claude-for-government-host>/gateway-api/user/bootstrap</string>
<key>disableDeploymentModeChooser</key>
<string>true</string>
```

Most device management consoles, including Jamf and Intune, build the profile around these keys for you. For a complete `.mobileconfig` ready to upload, use the Export menu described in the single-machine path.

### Windows

Claude Desktop reads string (`REG_SZ`) values by name under `HKLM\SOFTWARE\Policies\Claude`. Deliver them with Intune, Group Policy, or any tool that writes machine policy. The ADMX template from the Export menu makes both keys available in the policy editor. As a `.reg` file:

```text theme={null}
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude]
; substitute the Claude for Government host
"bootstrapUrl"="https://<claude-for-government-host>/gateway-api/user/bootstrap"
"disableDeploymentModeChooser"="true"
```

The `.reg` file from the Export menu targets `HKEY_CURRENT_USER`, which is correct for single-machine testing. For fleet deployment, deliver the values under `HKEY_LOCAL_MACHINE` as shown here.

<Note>
  Cowork, the agentic workspace in Claude Desktop, requires the **Virtual Machine Platform** Windows optional feature. Enable that feature through your device management system before rollout. On a device where the feature is not enabled, Cowork is unavailable until someone turns the feature on, which requires administrator rights that a standard user does not have. Chat works regardless of this feature. The [Windows fleet checklist](/docs/government/deploy-desktop/windows-checklist) lists the remaining Windows prerequisites.
</Note>

### Linux

Place a JSON file at `/etc/claude-desktop/managed-settings.json` containing the same keys at the top level.

```json theme={null}
{
  "bootstrapUrl": "https://<claude-for-government-host>/gateway-api/user/bootstrap",
  "disableDeploymentModeChooser": true
}
```

The file must be a regular file (not a symlink), and the file and its directory must be owned by root and must not be group- or world-writable. If the permissions are wrong, the app rejects the file, logs the reason to `main.log`, and treats the device as managed but unreadable, so local settings are also disabled until the permissions are corrected and the app is relaunched.

### Order of deployment

Deploy the configuration before the app wherever you can. A user whose device already has the profile opens Claude Desktop for the first time and lands directly on the Claude for Government sign-in screen, with no opportunity to sign in to claude.ai by mistake.

<Note>
  Once `bootstrapUrl`, `disableDeploymentModeChooser`, or any other recognized key except the automatic update settings is present in the profile, the device is managed. The in-app configuration window becomes read-only, and locally authored settings, including a single-machine test configuration, are ignored in favor of the profile. A managed device uses only the connection in the profile: users cannot add, import, or switch to other configurations in that window. If a group of users needs a different connection, scope a different profile to their devices or users in your management system, or leave those devices without a profile and set them up as described under [Configure a single machine](#configure-a-single-machine). Removing the profile returns the device to local control.
</Note>

The app reads managed configuration at launch. After you change the profile on a device where the app is already running, have the user fully quit and reopen it.

### Automatic updates

On macOS and Windows, Claude Desktop downloads and installs its own updates by default. If your agency distributes Claude Desktop updates itself, turn automatic updates off in both of the following places so that devices never update themselves.

* **On the Config page.** Have a tenant administrator or organization owner turn on [Block automatic updates](/docs/government/config/settings#block-automatic-updates) and [lock](/docs/government/config/overview#locks) it, so that no level below theirs can turn updates back on. Claude Desktop applies this setting once a user has signed in and the app has loaded their configuration from Claude for Government. With that configuration loaded, the app follows this setting alone, whether it is on or off, and ignores the profile value.
* **In the profile.** Add `disableAutoUpdates` with the value `"true"` to the [macOS](#macos) and [Windows](#windows) profiles above. The app applies the profile value only when it starts without a signed-in user, for example on a newly deployed device or when a user opens the app and has to sign in again because their session expired. Without the Config page setting, the profile value does not stop signed-in devices from updating.

Claude Desktop reads its update settings when it starts. If the app is already running on a device when you change the Config page setting or the profile, the change applies the next time the app starts. If you leave automatic updates on, [Restart deadline for updates](/docs/government/config/settings#restart-deadline-for-updates) on the Config page sets how long a user can put off the restart that installs a downloaded update.

## Confirm it worked

Run through these checks on a configured machine from either path.

<Steps>
  <Step title="Check the sign-in screen">
    Launch the app. The sign-in screen offers **Sign in with your organization**. On a managed device with `disableDeploymentModeChooser` set, it is the only option. If only the claude.ai sign-in appears, the configuration did not reach the app.
  </Step>

  <Step title="Check that the device is managed">
    On a device that received the profile through your management system, open the configuration window (the first three steps of the single-machine path). It should be read-only with a banner noting that your organization manages the configuration. If it is still editable, no recognized key reached the app, even if your management console reports the profile as delivered. The diagnostic report's Configuration section (next step) shows exactly what the app read.
  </Step>

  <Step title="Generate a diagnostic report">
    From **Help**, choose **Troubleshooting**, then **Generate Diagnostic Report**. The report's Configuration section lists which keys the app read, where each came from, and any values that failed to parse. Secret values are redacted, so the report is safe to attach to a help-desk ticket.
  </Step>

  <Step title="Sign in and send a message">
    Sign in as a provisioned test user. Chat works and the model picker lists the models you expect for that user's seat tier.
  </Step>

  <Step title="Confirm per-user settings arrived">
    After sign-in, what the app offers matches that user's [product availability](/docs/government/config/settings#product-availability) settings (with everything on, the sidebar shows **Home** and **Code**), and any organization-managed connectors appear in the app. One end-to-end test is to set a short message in the **Claude Desktop banner** setting on the tenant [Config](/docs/government/tenant-admin/configuration) page during rollout; if the message appears across the top of the app after sign-in, per-user delivery is working. If sign-in succeeds but none of these settings arrive, re-check the configured address.
  </Step>
</Steps>

## Troubleshooting

| What you see                                                                                                                                                                                     | Likely cause                                                                                                                                                                                          | What to do                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Only the claude.ai sign-in screen; no organization option                                                                                                                                        | The configuration never reached the app: the profile was not delivered, a key name is misspelled, the value is in the wrong location or registry type, or the app was not relaunched after the change | Verify delivery in your management console, generate a diagnostic report and check its Configuration section, then fully quit and reopen the app                                        |
| Sign-in times out, or the browser says the code expired                                                                                                                                          | The app stops waiting after about five minutes                                                                                                                                                        | Cancel and start sign-in again; a fresh code is issued                                                                                                                                  |
| The diagnostic report or `main.log` shows "Managed configuration is invalid; local settings are disabled until it is fixed"                                                                      | The app detected a managed profile but could not read any of its values                                                                                                                               | Correct the profile and redeploy; the report's Configuration section names each key that failed                                                                                         |
| Signed in, but the model picker is empty, or the app shows a **Configuration can't be used** banner whose **Details** or **Copy report for IT** text says the provider returned no usable models | The user has no seat tier, or none of the tier's models is available in Claude for Government, so the app received an empty model list. Nothing is wrong with the device's configuration              | Have an organization owner check the user's seat tier on the [Users](/docs/government/org-admin/users) page and the tier's models on the [Seat tiers](/docs/government/org-admin/seat-tiers) page |

For anything else, the app writes its log to `~/Library/Logs/Claude-3p/main.log` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\main.log` on Windows, and `~/.config/Claude-3p/logs/main.log` on Linux. The log records which configuration keys were read or dropped and why. The diagnostic report from the verification checklist produces a bundle, without conversation content, that you can send to your Anthropic representative.

## Things to know

* Configuration changes made in this portal do not need to be pushed to devices. The app re-checks Claude for Government for changes about every 30 minutes and at each launch, and prompts users to relaunch when something changed.
* New and retired models appear in the model picker without any profile change or app update; model access is controlled through [seat tiers](/docs/government/org-admin/seat-tiers).
* The sign-in flow and what a user sees on the [Sessions](/docs/government/account/sessions) page after pairing a device are covered on that page.
