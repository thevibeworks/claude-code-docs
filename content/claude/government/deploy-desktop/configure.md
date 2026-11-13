> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Claude Desktop to Claude for Government

> Connect Claude Desktop to Claude for Government: the bootstrap URL, device profiles for macOS, Windows, and Linux, network hosts, updates, and troubleshooting.

> **Who this is for:** IT administrators who install Claude Desktop on agency devices and connect it to Claude for Government.

A fresh install of Claude Desktop connects to claude.ai. To connect it to Claude for Government instead, each device needs a setting that tells the app where to reach Claude for Government, and on managed devices the configuration profile also hides the claude.ai sign-in option. Once that setting is in place, everything else that governs the app (which products and features are available, model access, [connectors](https://claude.com/docs/government/connectors/overview.md), usage limits, a banner message) is controlled through the [tenant](https://claude.com/docs/government/tenant-admin/configuration.md) and [organization](https://claude.com/docs/government/org-admin/configuration.md) configuration pages in this portal and delivered to each user when they sign in.

## Choose how to deploy

* **[Configure a single machine](#configure-a-single-machine)** to confirm the app works on a representative device before a wider rollout, or to set up a small group of devices. An administrator installs the app on each device and enters the [bootstrap address](#the-bootstrap-address) in the app's built-in configuration window. On a device set up this way, the user can still sign in to claude.ai.
* **[Deploy to your fleet](#deploy-to-your-fleet)** for a production rollout. Your device management system (for example Intune, Configuration Manager, or Jamf) installs the app with elevated rights and pushes the address as a configuration profile, so end users need no administrator rights to install it.

## Before you begin

Confirm each of the following before you start either path.

* **User accounts exist.** Claude Desktop signs users in to the same accounts as this portal. For each user, including your own test account, check with your tenant administrators that the user can sign in (a [routing rule](https://claude.com/docs/government/tenant-admin/identity-and-access.md) covers them) and has a [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md) with at least one model enabled.
* **Devices and browsers can reach the hosts they need.** Allow the hosts under [Network access](#network-access).
* **The device meets Claude Desktop's requirements.** See the Claude Desktop [system requirements](https://claude.com/docs/third-party/claude-desktop/installation.md#system-requirements) for macOS and Windows device requirements. For a Windows fleet, work through the [Windows fleet checklist](https://claude.com/docs/government/deploy-desktop/windows-checklist.md).
* **Devices used for Code have the software your users' work needs.** Code runs its commands with the software installed on the device. Cowork and Advanced file analysis in Chat run theirs in the app's own virtual machine, which includes Python. For Git on Windows, see [Installer and packaging](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#installer-and-packaging).
* **You have the installer.** The [macOS deployment guide](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos) and the [Windows deployment guide](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows) cover where to download the installer and how to distribute it.
* **The app is current.** Deploy Claude Desktop 1.46388.1 or later.

### Network access

Connections to the Claude for Government host and its sign-in service use HTTPS on port 443. Claude for Government does not publish IP addresses for its host or its sign-in service, so allowlist both by hostname.

* **App traffic.** Allow Claude Desktop on every device to reach the Claude for Government host, which carries the app's configuration and model inference.
* **Browser sign-in traffic.** Allow the browser on every device to reach the Claude for Government host, the Claude for Government sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider. Sign-in happens in each user's default browser, not in the app.
* **`downloads.claude.ai`.** From this host the app downloads the agent helper described under [Endpoint security software](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software), which Chat, Cowork, and Code all need, and the Cowork workspace, which Cowork tasks and Advanced file analysis in Chat need. The app downloads each one whenever the device does not already have the version that the app needs. The [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation) for macOS and Windows includes them.
* **Hosts for icons, previews, and widgets.** For connector icons, the artifact preview frame, and the interactive widgets that some connectors display, the app reaches the hosts listed under Non-essential services in [Required egress paths](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths), including `www.claudeusercontent.com` and `www.google.com`. If traffic is blocked, the app will run without icons, previews, and widgets.
* **Update hosts.** On macOS and Windows, while [automatic updates](#automatic-updates) are on, also allow the hosts listed under Auto-updates in [Required egress paths](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths). The telemetry rows there never apply, because Claude for Government does not send telemetry to Anthropic.
* **Hosts your tools and connectors use.** Allow the hosts you add to [Allowed network hosts](https://claude.com/docs/government/config/settings.md#allowed-network-hosts) (such as package registries), the addresses of any connectors you configure on the Config page (including Microsoft 365 if you set up that connector), and your telemetry collector if you set one.
* **Proxies.** The app supports routing its traffic through your network's proxy server, as the [Security and data handling](https://claude.com/docs/government/security/security-and-data-handling.md#network-egress-required-domains-and-proxies) page describes. If your proxy inspects TLS, validate sign-in, sending a message, and a shell command that Claude runs on a pilot device before rollout. See also [Network proxy](https://claude.com/docs/third-party/claude-desktop/network-proxy.md) in the Claude Desktop documentation.

## The bootstrap address

The setting that holds the address is called `bootstrapUrl`, and its value is the Claude for Government host followed by the fixed path `/gateway-api/user/bootstrap`.

```text theme={null}
https://<claude-for-government-host>/gateway-api/user/bootstrap
```

The Claude for Government host is the same domain name you use to access Claude for Government. If you are unsure of it, ask your Anthropic representative. The app uses the address exactly as entered, so include the full path.

Use the host exactly as it was provided to your agency. An alias that your agency sets up on its own, such as a DNS record, redirect, or reverse proxy under your own domain that forwards to Claude for Government, does not work as the bootstrap address. The app accepts sign-in addresses only on the host in `bootstrapUrl`, and Claude for Government answers sign-in only on the host provided to your agency, so the app cannot sign in through such an alias.

### How the app uses the bootstrap address

The address is the same for every device and user in your agency and carries no credentials or user information, so the same profile is safe to push to your whole fleet. A request to the address without a signed-in session is refused.

When a user chooses **Sign in with your organization**, the app asks the Claude for Government host to start a sign-in, shows the pairing code it receives, and opens the host's sign-in page in the user's default browser. That page asks for the user's agency email address, then sends the browser to the sign-in service and on to your agency's identity provider. After signing in, the user acknowledges the system-use notification, confirms that the code shown in the browser matches the one in the app, and approves.

Claude for Government then issues the app a session for that user, which the app stores encrypted on the device. The app presents that session, and nothing from the profile, when it downloads the user's configuration from this address and for model inference on the same host.

The configuration that the app downloads for a user includes [product availability](https://claude.com/docs/government/config/settings.md#product-availability), [tools, connectors, and plugins](https://claude.com/docs/government/config/settings.md#integrations), [network and folder limits](https://claude.com/docs/government/config/settings.md#sessions-and-access), [a banner message](https://claude.com/docs/government/config/settings.md#appearance), and [telemetry, update, and restart settings](https://claude.com/docs/government/config/settings.md#compliance-and-telemetry), all of which you manage in this portal. The models the user can choose come from the user's [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md).

## Configure a single machine

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/f0r7JXkdrdWXuNu4/images/government/videos/admin-08-pilot-claude-desktop-on-one-machine-v2.mp4?fit=max&auto=format&n=f0r7JXkdrdWXuNu4&q=85&s=ea3b436b903baf714ef2cb0a7279c8ca" aria-label="Video walkthrough: Pilot Claude Desktop on one machine" />

Video: Pilot Claude Desktop on one machine (1 min 34 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#pilot-claude-desktop-on-one-machine)

Claude Desktop has a built-in configuration window that is hidden until you enable developer mode. These steps use it to set the address on one machine.

**1. Launch the app without signing in**

Install Claude Desktop on the test machine and open it. On Windows, the installer registers a Windows system service, so it must run as a local administrator. The claude.ai sign-in screen appears; this is expected before the app is configured. Stay on this screen.

**2. Enable developer mode**

From the **Help** menu, choose **Troubleshooting**, then **Enable Developer Mode**, and confirm the prompt. On Windows the **Help** menu is under the application menu (☰) on the sign-in screen. The app relaunches with a **Developer** menu added.

**3. Open the configuration window**

From the **Developer** menu, choose **Configure Third-Party Inference**. This is the correct option for Claude for Government despite the name.

**4. Enter the bootstrap address**

In the window's left sidebar, click **Source**, which on an unconfigured machine appears last in the list and is dimmed but is still clickable. Enter the full address from [The bootstrap address](#the-bootstrap-address) in the **Bootstrap config URL** field. You do not need to change any other field, because Claude for Government supplies the provider, credentials, and model list after sign-in. A **Trust bootstrap-delivered settings** switch (the `trustBootstrapDelivery` key) appears once the field has a value. Leave it off. With the switch on, the app trusts everything your Claude for Government host delivers without asking, including connectors and helper scripts that run on the device. That is the same trust the app extends when the bootstrap address comes from machine-wide device management. If you do turn it on, first confirm that the bootstrap address is on your Claude for Government host.

**5. Apply and sign in**

Click **Apply Changes**, then click **Save & Restart** and let the app relaunch. The sign-in screen now offers **Sign in with your organization** alongside the claude.ai option. Choose it. The app shows a pairing code and opens the sign-in page in your browser. Sign in with your agency credentials, confirm that the code in the browser matches the one in the app, and approve.

**6. Allow the gateway address**

After sign-in, the app opens a small **Apply settings from your organization?** window that lists a **Gateway base URL**, the address that Claude for Government sends the app to use for model inference. If your browser is still in front, switch back to Claude to find it. Expand **Gateway base URL** and confirm that the address is on your Claude for Government host, then click **Allow**. The app applies none of your organization's settings until you click **Allow**.

If the address is not on your host, do not click **Allow**. Reopen the configuration window from the **Developer** menu, correct the **Bootstrap config URL** in its **Source** section, click **Apply Changes**, and then click **Save & Restart** so that the app relaunches with the corrected address. If the app has no **Developer** menu, repeat the **Enable developer mode** step. Choosing **Quit**, pressing Esc, or closing the window quits the app, and it asks again the next time it opens. For why the app asks and the other settings this prompt can cover, see [Keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent).

**7. Run the verification checklist**

Work through [Confirm it worked](#confirm-it-worked).

After the test, the same configuration window has an **Export** menu that produces files for your management system, listed under [Export the profile](https://claude.com/docs/third-party/claude-desktop/mdm.md#2-export-the-profile). If the app has no **Developer** menu, repeat the **Enable developer mode** step. Before exporting, make sure **Trust bootstrap-delivered settings** in the **Source** section is off so the exported files do not carry it. Before you deploy a profile made from these files, make sure it sets the keys listed under [Deploy to your fleet](#deploy-to-your-fleet).

## Deploy to your fleet

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/KoTvDoB4EQ3eCbkB/images/government/videos/admin-09-deploy-to-your-fleet-v2.mp4?fit=max&auto=format&n=KoTvDoB4EQ3eCbkB&q=85&s=e82e0d3f6ee54735ef5e7a3d4b0f3b43" aria-label="Video walkthrough: Deploy to your fleet" />

Video: Deploy to your fleet (1 min 32 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#deploy-to-your-fleet)

Push both the app installer and the configuration profile through your device management system.

The profile needs these keys. In the macOS and Windows profiles, write every value as a string exactly as shown, including booleans as the strings `"true"` or `"false"`; the Linux file uses native JSON types, as shown.

| Key | Value | Purpose |
| - | - | - |
| `bootstrapUrl` | `https://<claude-for-government-host>/gateway-api/user/bootstrap` | Required. Points the app at Claude for Government. |
| `disableDeploymentModeChooser` | `"true"` | Required. Hides the claude.ai sign-in option. Claude for Government also sends this setting, but the profile must set it too (see [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) in the Claude Desktop configuration reference). |
| `deploymentMode` | `"3p"` | Required on Claude Desktop 4.16336.0 or later. Keeps the app on Claude for Government. Earlier versions read `disableDeploymentModeChooser`, so set both. |

No other keys are needed to connect the app; Claude for Government [supplies everything else](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) per user after sign-in. If your agency distributes Claude Desktop updates itself, [Automatic updates](#automatic-updates) describes one more key to add.

Leave these keys unset:

* Keys for a separate sign-in provider, such as **`bootstrapOidc`** and **`inferenceGatewayOidc`**, do not work with Claude for Government, because you cannot connect the app directly to your identity provider
* **`deploymentDisplayName` and `deploymentDisplaySubtitle`**, which name the connection in the app's window, are discarded once the app downloads the user's configuration after sign-in
* **`desktopHome`**, because the app's home comes from [Product availability](https://claude.com/docs/government/config/settings.md#product-availability) on the Config page

### macOS

Claude Desktop reads managed preferences in the `com.anthropic.claudefordesktop` domain. Deploy a configuration profile that sets the keys in that domain as strings.

```xml theme={null}
<key>bootstrapUrl</key>
<!-- substitute the Claude for Government host -->
<string>https://<claude-for-government-host>/gateway-api/user/bootstrap</string>
<key>disableDeploymentModeChooser</key>
<string>true</string>
<key>deploymentMode</key>
<string>3p</string>
```

For a `.mobileconfig` to start from, use the Export menu described under [Configure a single machine](#configure-a-single-machine), and check it as that section says before you upload it.

### Windows

Claude Desktop reads string (`REG_SZ`) values by name under `HKLM\SOFTWARE\Policies\Claude`. Deliver them with Intune, Group Policy, or any tool that writes machine policy. As a `.reg` file:

```text theme={null}
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude]
; substitute the Claude for Government host
"bootstrapUrl"="https://<claude-for-government-host>/gateway-api/user/bootstrap"
"disableDeploymentModeChooser"="true"
"deploymentMode"="3p"
```

Before you deploy a `.reg` file from the **Export** menu, check that the line in square brackets names `HKEY_LOCAL_MACHINE`, and change it if it does not. Under `HKEY_CURRENT_USER`, the app asks each user to allow the gateway address after sign-in, as in the **Allow the gateway address** step under [Configure a single machine](#configure-a-single-machine).

Keep every value in the same hive as `bootstrapUrl`, because once any value exists under `HKLM\SOFTWARE\Policies\Claude` the app ignores `HKEY_CURRENT_USER` entirely.

Cowork, the agentic workspace in Claude Desktop, requires the **Virtual Machine Platform** Windows optional feature. The [Windows fleet checklist](https://claude.com/docs/government/deploy-desktop/windows-checklist.md) covers [that feature](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#cowork-virtualization) and the remaining Windows prerequisites, and explains what to do [if some devices are not ready for Cowork](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#if-some-devices-are-not-ready-for-cowork).

### Linux

Place a JSON file at `/etc/claude-desktop/managed-settings.json` containing these keys at the top level.

```json theme={null}
{
  "bootstrapUrl": "https://<claude-for-government-host>/gateway-api/user/bootstrap",
  "disableDeploymentModeChooser": true
}
```

Once the device runs Claude Desktop 4.16336.0 or later, add `"deploymentMode": "3p"`. Earlier versions treat a key they don't recognize in this file as an error.

The file must be a regular file (not a symlink), and the file and its directory must be owned by root and must not be group- or world-writable. [The Linux configuration file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file) in the Claude Desktop documentation describes what the app does when the permissions are wrong.

### Order of deployment

Deploy the configuration before the app wherever you can. A user whose device already has the profile opens Claude Desktop for the first time and lands directly on the Claude for Government sign-in screen, with no opportunity to sign in to claude.ai by mistake. The app reads managed configuration at launch. After you change the profile on a device where the app is already running, have the user fully quit it, including from the menu bar or system tray, and reopen it.

Once the profile sets `bootstrapUrl`, `disableDeploymentModeChooser`, or any other key except [the few that Claude Desktop exempts](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), the device is managed. The in-app configuration window becomes read-only, and the app ignores any configuration saved in that window.

Turning on developer mode does not change this: the configuration window stays read-only, so users can view the connection there but not change it. If a group of users needs a different connection, scope a different profile to their devices in your management system, or leave those devices without a profile and set them up as described under [Configure a single machine](#configure-a-single-machine). Removing the profile returns the device to local control.

### Automatic updates

On macOS and Windows, Claude Desktop downloads and installs its own updates by default. On a Mac with the app in `/Applications`, macOS asks a user who is not an administrator for an administrator's name and password before an update installs. Until someone enters them, the update does not install. If your agency distributes Claude Desktop updates itself, turn automatic updates off in both of the following places so that devices never update themselves.

* **On the Config page.** Have a tenant administrator turn on [Block automatic updates](https://claude.com/docs/government/config/settings.md#block-automatic-updates) and [lock](https://claude.com/docs/government/config/overview.md#locks) it, so that no level below theirs can turn updates back on. An organization owner can turn it on for their own organization, whose Config page offers no lock. Claude Desktop applies this setting once a user has signed in and the app has loaded their configuration from Claude for Government. With that configuration loaded, the app follows this setting alone, whether it is on or off, and ignores the profile value.
* **In the profile.** Add `disableAutoUpdates` with the value `"true"` beside [`bootstrapUrl`](#the-bootstrap-address) in your [macOS](#macos) and [Windows](#windows) profiles. The app applies the profile value only when it starts without a signed-in user, for example on a newly deployed device or when a user opens the app and has to sign in again because their session expired. Without the Config page setting, the profile value does not stop signed-in devices from updating.

Claude Desktop reads its update settings when it starts. If the app is already running on a device when you change the Config page setting or the profile, the change applies the next time the app starts. If you leave automatic updates on, see [Restart deadline for updates](https://claude.com/docs/government/config/settings.md#restart-deadline-for-updates).

On Claude Desktop versions earlier than 1.25927.0, the Config page setting alone does not reliably stop updates. On those versions, a profile that sets `disableAutoUpdates` to `"true"` stops automatic updates for signed-in users too, until you remove the key.

On Linux, apt installs Claude Desktop updates, and the app does not download or install its own. The **Block automatic updates** setting and the `disableAutoUpdates` key do not change these updates. To stop the app's own check of Anthropic's [update hosts](https://claude.com/docs/third-party/claude-desktop/telemetry.md#required-egress-paths) for a new version, use both, with the key in the [Linux file](#linux). To keep Linux devices on the versions your agency distributes, follow [Auto-updates](https://claude.com/docs/third-party/claude-desktop/telemetry.md#auto-updates) in the Claude Desktop documentation.

## Confirm it worked

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/f0r7JXkdrdWXuNu4/images/government/videos/admin-10-verify-a-managed-device-and-spot-common-failures-v2.mp4?fit=max&auto=format&n=f0r7JXkdrdWXuNu4&q=85&s=03c3b66f877fa1a3e80ce7a23b1176e8" aria-label="Video walkthrough: Verify a managed device and spot common failures" />

Video: Verify a managed device and spot common failures (1 min 40 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#verify-a-managed-device-and-spot-common-failures)

Run through these checks on a configured machine from either path.

**1. Check the sign-in screen**

Launch the app. The sign-in screen offers **Sign in with your organization**. If the profile sets `disableDeploymentModeChooser` to true, the claude.ai sign-in option is hidden. If only the claude.ai sign-in appears, the configuration did not reach the app.

**2. Check that the device is managed**

On a device that received the profile through your management system, open the configuration window (the second and third steps of the single-machine path). It should be read-only with a banner noting that your organization manages the configuration. If it is still editable, no recognized key reached the app, even if your management console reports the profile as delivered. The diagnostic report (next step) shows what the app read.

**3. Generate a diagnostic report**

From **Help**, choose **Troubleshooting**, then **Generate Diagnostic Report**, and click **Export to file**. In the saved `.zip` file, `managed-config.txt` shows where the configuration was read from and each key's configured or default value, and lists anything it could not parse under `Parse errors`. Secret values are redacted. If the report has no such file, no configuration reached the app.

**4. Sign in and send a message**

Sign in as a provisioned test user. If the app asks **Apply settings from your organization?**, answer it as in the **Allow the gateway address** step under [Configure a single machine](#configure-a-single-machine). Claude replies, and the model picker lists the models you expect for that user's seat tier.

**5. Confirm per-user settings arrived**

After sign-in, what the app offers matches that user's [product availability](https://claude.com/docs/government/config/settings.md#product-availability) settings, and any organization-managed connectors appear in the app. One end-to-end test is to set a short [banner message](https://claude.com/docs/government/config/settings.md#appearance) on the tenant [Config](https://claude.com/docs/government/tenant-admin/configuration.md) page during rollout; if the message appears across the top of the app after sign-in, per-user delivery is working. If sign-in succeeds but none of these settings arrive, re-check the configured address.

## Troubleshooting

| What you see | Likely cause | What to do |
| - | - | - |
| Only the claude.ai sign-in screen; no organization option | The configuration never reached the app: the profile was not delivered, a key name is misspelled, the value is in the wrong location or registry type, or the app was not relaunched after the change. A profile that sets a key such as `desktopHome` or an `otlp*` telemetry key but no `bootstrapUrl` also produces this screen, even on a device that was set up in the app's configuration window | Verify delivery in your management console, check a [diagnostic report](#confirm-it-worked), then fully quit and reopen the app. If the profile has no `bootstrapUrl`, add `bootstrapUrl` to the profile or remove the profile, then fully quit and reopen the app |
| Sign-in times out, or the browser says the code expired | The app stops waiting after about five minutes | Start sign-in again; a fresh code is issued |
| Sign-in fails as soon as the user chooses **Sign in with your organization**, and the error on the sign-in screen or in `main.log` says that an address "must be same-origin" as the configured host | `bootstrapUrl` points at an alias that your agency operates, rather than the host provided to your agency (see [The bootstrap address](#the-bootstrap-address)) | Use the host provided to your agency in `bootstrapUrl`, exactly as provided, redeploy the profile, then fully quit and reopen the app |
| The diagnostic report or `main.log` shows "Managed configuration is invalid; local settings are disabled until it is fixed" | The app detected a managed profile but could not read any of its values | Correct the profile and redeploy. The [diagnostic report](#confirm-it-worked) lists what the app could not parse |
| Signed in, but the model picker is empty, or the app shows a **Configuration can't be used** banner whose **Details** or **Copy report for IT** text says the provider returned no usable models | The user has no seat tier, or none of the tier's models is available in Claude for Government. Nothing is wrong with the device's configuration | Have an organization owner check the user's seat tier on the [Users](https://claude.com/docs/government/org-admin/users.md) page and the tier's models on the [Seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) page |
| An **Apply settings from your organization?** window appears after sign-in or at every launch, or the app quits when the user dismisses that window | The bootstrap address was entered in the app or set per user (for example under `HKEY_CURRENT_USER`), and the user has not yet clicked **Allow** | Have the user answer it as in the **Allow the gateway address** step under [Configure a single machine](#configure-a-single-machine). If the address is not on your host, check the bootstrap address configured on that device. To stop the prompt across a fleet, deliver the bootstrap address through machine-wide device management, as described under [Deploy to your fleet](#deploy-to-your-fleet) |
| The browser shows a connection error instead of Claude for Government or its sign-in page: "Secure Connection Failed" with `PR_CONNECT_RESET_ERROR` in Firefox, or `ERR_CONNECTION_RESET` in Chrome | A web filter, firewall, or proxy reset the connection, either on your agency's network or on the Claude for Government side. | If the address opens in another browser on the same computer, check the first browser's proxy and DNS settings. Otherwise, open the address from outside your agency's network, for example on a phone using cellular data. If the phone shows a web page, not a connection error, have your network team allow the host in that address and the hosts described under [Network access](#network-access). If the phone also fails, or the team finds no block, contact your Anthropic representative with the address, the time and time zone of the error, and your network's public IP addresses. |
| During sign-in, the browser shows a Microsoft page titled "You cannot access this right now", sometimes in one browser but not in another | Microsoft Entra ID shows this page when one of your agency's Conditional Access policies blocks the sign-in, for example a policy that limits which browsers, devices, or locations can sign in. The refusal happens before the sign-in reaches Claude for Government, so nothing in the app or in this portal changes it. | Ask your identity team to find the failed sign-in in the identity provider's sign-in logs. Adjust the policy, or have the user sign in from a browser or device the policy allows (Claude Desktop opens sign-in in the computer's default browser). |
| The app shows **Your session has expired** or **Couldn't verify your sign-in** with a **Sign in again** button, or a device that was already set up opens to the sign-in screen | The user's Claude for Government session ended. A session ends once the user has gone without using Claude for longer than the [Session idle timeout](https://claude.com/docs/government/config/settings.md#session-idle-timeout) your tenant administrators set, which is 24 hours unless they change it, or when it reaches the [Maximum session length](https://claude.com/docs/government/config/settings.md#maximum-session-length) if one is set. A session also ends when the user or an administrator signs it out. A device left idle, locked, or asleep does not keep a session alive. [How long sessions last](https://claude.com/docs/government/account/sessions.md#how-long-sessions-last) lists other ways a session ends | Have the user sign in again. When a session has ended, the app keeps the user's configuration and asks them to sign in again, with a message and a **Sign in again** button while the app is open, or with the sign-in screen the next time it starts, and it reloads the configuration once they sign in. If people are asked to sign in more often than you intend, ask a tenant administrator or organization owner to review **Session idle timeout** and **Maximum session length** on the [Config](https://claude.com/docs/government/tenant-admin/configuration.md) page |
| A **Configuration sync issue** banner on a Claude Desktop version earlier than 1.34493.0 | On these versions, an ended session can appear as this banner. Versions earlier than 1.32352.0 that ask for the **Apply settings from your organization?** approval also show it, with "bootstrap response is missing required field(s): inferenceGatewayBaseUrl" | Update the app to the latest version, then sign in again or answer the prompt |
| On a Windows device, Cowork tasks fail, the app shows an error about starting Claude's workspace that mentions a Windows update, or, with [Advanced file analysis in Chat](https://claude.com/docs/government/config/settings.md#advanced-file-analysis-in-chat) on, Claude can't read some attached files in Chat, such as Word, Excel, or PowerPoint files | The device has installed the Windows update released September 8, 2026, but not Microsoft's later update that fixes the problem. Cowork tasks and Advanced file analysis in Chat need the workspace. | Install the latest Windows update on the device and restart it. On Windows 11 24H2 and 25H2, the fix is KB5129195. No Claude Desktop update is needed. See [Resolved: Cowork on Windows](https://claude.com/docs/cowork/changelog.md#resolved-cowork-on-windows) in the Claude Desktop changelog. |
| [Web search](https://claude.com/docs/government/config/settings.md#web-search) is on for your organization, but a user does not have it, and under **Customize**, then **Connectors**, **Web Search** shows as not connected and **Connect** fails, while chat works | A firewall or secure web gateway on that user's network path filters traffic by application. Claude Desktop connects to web search on your Claude for Government host over HTTPS, and such equipment can classify that connection as Model Context Protocol (MCP) traffic and block it even when the host itself is allowed. | Ask your network team to allow this traffic to your Claude for Government host for the affected users. The user's `main.log` records each failed attempt, including any block page the network returned. Then have the user select **Connect** next to **Web Search**, or restart the app. |
| The app shows **Couldn't download Claude's workspace**, or **Failed to start Claude's workspace** with a download error under it, or Chat conversations and Cowork tasks fail to start with "Host Claude Code binary not available. Check that the download completed." | Claude Desktop could not download a complete, verified copy of the Cowork workspace or the [agent helper](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software) from `downloads.claude.ai`. | Follow [Cowork workspace or Claude CLI fails to download](https://claude.com/docs/third-party/claude-desktop/installation.md#cowork-workspace-or-claude-cli-fails-to-download) in the Claude Desktop documentation. |
| Chat conversations, Cowork tasks, or Code sessions fail to start with **Claude Code crashed** or **Managed settings kept Claude Code from starting**, and `main.log` says that Claude Code "is newer than the maximum version allowed by your organization" | The device's [Claude Code managed settings](https://claude.com/docs/government/deploy-claude-code/configure.md#deploy-the-settings) set a maximum version below the Claude Code in Claude Desktop's [agent helper](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software), which runs Chat, Cowork, and Code. An app update can bring a newer Claude Code | Raise or remove [`requiredMaximumVersion`](https://code.claude.com/docs/en/settings-reference#requiredmaximumversion) in those settings on the device |
| On a Windows device, the app shows **A Windows security policy is blocking Claude's workspace** | A Group Policy or MDM policy applied to the device assigns the **Log on as a service** right without the `NT VIRTUAL MACHINE\Virtual Machines` group, or lists that group under **Deny log on as a service** | Follow [Windows security policy blocks the Cowork workspace](https://claude.com/docs/third-party/claude-desktop/installation.md#windows-security-policy-blocks-the-cowork-workspace) in the Claude Desktop documentation. |

For anything else, the app writes its log to `~/Library/Logs/Claude-3p/main.log` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\main.log` on Windows, and `~/.config/Claude-3p/logs/main.log` on Linux (`~/.config/Claude/logs/main.log` until the app is configured). The diagnostic report from the verification checklist produces a bundle that you can send to your Anthropic representative. [Review it first](https://claude.com/docs/third-party/claude-desktop/installation.md#troubleshooting).

## Things to know

* Configuration changes made in this portal do not need to be pushed to devices. The app re-checks Claude for Government for changes about every 10 minutes (about every 30 minutes on Claude Desktop versions earlier than 1.46388.1) and at each launch. See [When changes take effect](https://claude.com/docs/government/config/overview.md#when-changes-take-effect).
* New and retired models appear in the model picker without any profile change; model access is controlled through [seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md). [Models in Claude Desktop](https://claude.com/docs/government/desktop/models.md) covers a model that needs a newer version of Claude Desktop.
