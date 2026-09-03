> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation and setup

> Install Claude Desktop on 3P, check device readiness, and choose how configuration reaches your devices: an MDM profile or a bootstrap server

Claude Desktop on third-party (3P) is the standard Claude Desktop application plus a managed configuration that activates third-party inference mode. Setup is two pieces: install the regular Claude Desktop app, and deliver the configuration to it.

## System requirements

Cowork, the agent workspace at the center of Claude Desktop on 3P, has the following device requirements:

| Requirement      | macOS                        | Windows                                                              |
| ---------------- | ---------------------------- | -------------------------------------------------------------------- |
| Operating system | macOS 14 (Sonoma) or later   | Windows 10 build 19041 (version 2004) or later, including Windows 11 |
| CPU architecture | Apple silicon or Intel (x64) | x64 or Arm64                                                         |
| Installer        | `.dmg`                       | `.msix`                                                              |

On Windows, Cowork requires the `.msix` package: fleets provisioned with the legacy `.exe` installer get Claude Desktop without Cowork, and migrating them to `.msix` enables it. Cowork also requires working hardware virtualization, which the [readiness check](#check-device-readiness) verifies along with the requirements above.

## Check device readiness

Before installing Claude Desktop, you can confirm that a device supports Cowork by running the readiness check: a small standalone program that requires no installation or sign-in.

| Platform      | Download                                                                                                                     |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| macOS         | [Cowork readiness check for macOS](https://claude.ai/api/desktop/darwin/universal/cowork-readiness-check/latest/redirect)    |
| Windows (Arm) | [Cowork readiness check for Windows arm64](https://claude.ai/api/desktop/win32/arm64/cowork-readiness-check/latest/redirect) |
| Windows (x64) | [Cowork readiness check for Windows x64](https://claude.ai/api/desktop/win32/x64/cowork-readiness-check/latest/redirect)     |

Open the downloaded program to run the check. A ready device reports **This computer is ready for Cowork**.

For fleet deployments, run the check on one device of each hardware model in your fleet before the broad rollout to identify unsupported models early.

## Install the app

Download the installer for your platform from [claude.com/download](https://claude.com/download).

| Platform | Installer | Notes                                                       |
| -------- | --------- | ----------------------------------------------------------- |
| macOS    | `.dmg`    | Drag **Claude.app** to Applications                         |
| Windows  | `.msix`   | Supports per-machine provisioning for enterprise deployment |

For fleet rollouts, distribute the installer through your standard software-distribution mechanism after the configuration reaches devices; [Choose a configuration delivery model](#choose-a-configuration-delivery-model) covers how the configuration gets there.

## Choose a configuration delivery model

Configuration reaches devices in one of two ways. Both typically use your MDM tooling to push a profile; the difference is what the profile contains.

|                            | MDM profile                                                             | Bootstrap server                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| What you deploy to devices | The full configuration, exported as a `.mobileconfig` or `.reg` profile | A minimal profile containing only the bootstrap keys (`bootstrapUrl`, optionally `bootstrapOidc` or request headers) |
| Where settings live        | In the profile, identical for every device the profile targets          | On an HTTPS endpoint you operate, which returns each user's configuration at sign-in                                 |
| Per-user values            | Separate profiles per device group                                      | The server keys its response to the signed-in user                                                                   |
| Changing settings          | Export and push an updated profile                                      | Change your server's response; devices pick it up at the next fetch, with no profile push                            |

Choose an MDM profile when one configuration, or a few group-scoped profiles, covers your fleet. Most MDMs support role-based distribution, so per-group configuration doesn't require a bootstrap server.

Building the configuration in the app is optional. The [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) can also export schema-only templates (an ADMX template for Windows, a Profile Manifest `.plist` for macOS) from its **Export** menu, so you can enter values directly in your management console instead. See [Export the profile](/docs/third-party/claude-desktop/mdm#2-export-the-profile) for all formats.

Choose a bootstrap server when your organization doesn't use MDM, or when per-user credentials or frequently changing settings would make per-group profiles unwieldy. The tradeoff is that you operate the endpoint.

The two models don't combine: when a bootstrap response is in effect, it replaces MDM-delivered values wholesale, and a few device-level keys are only available via MDM (see the Availability column in the [configuration reference](/docs/third-party/claude-desktop/configuration)).

Pick your path:

* [Deploy with MDM](/docs/third-party/claude-desktop/mdm) covers authoring the configuration in the app, exporting the profile, and deploying it to your fleet.
* [Deploy with a bootstrap server](/docs/third-party/claude-desktop/bootstrap) covers getting the bootstrap keys onto devices and running the server.

On either path, deploy the configuration before the app so users open Claude for the first time and land directly in the third-party deployment.

## Single-machine setup

For evaluating before a fleet rollout, for pilots, or for organizations that don't use MDM, a single machine can be configured directly in the app.

1. Install Claude Desktop from [claude.com/download](https://claude.com/download).
2. Launch the app. **Do not sign in or create an Anthropic account.** From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the login screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure Third-Party Inference…** to open the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration).
3. Enter the provider, endpoint, and credential values supplied by your administrator.
4. Click **Apply locally**. The app relaunches and the sign-in screen now offers the option to start in Claude Desktop on 3P using the configuration you entered.

The configuration is written to the application's local config file and applies only to that device and user account. It can be edited from the same window at any time. To return to standard Claude Desktop, choose the Anthropic sign-in option on the sign-in screen instead.

If your organization runs a [bootstrap server](/docs/third-party/claude-desktop/bootstrap) but doesn't use MDM, your administrator can instead supply a small configuration file containing only the bootstrap keys. Load it with **Import configuration** in the same window; the bootstrap server supplies everything else after you sign in.

When the configuration works on a single machine, roll it out to the fleet with the [delivery model you chose](#choose-a-configuration-delivery-model); on the MDM path, you can export the tested configuration as the profile you deploy.

## Verifying the deployment

On any configured device, open Claude Desktop and go to **Help → Troubleshooting → Copy Managed Configuration Report**. This copies a summary showing which keys were detected, where they were read from (managed profile vs. user store), and whether the inference credentials validated successfully. Secret values are redacted.

Also confirm that the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) (**Developer → Configure Third-Party Inference…**) opens read-only on a managed device. The app reads managed keys from the profile by name and silently ignores a misspelled key rather than reporting an error. On macOS, a window that is still editable means no recognized key reached the app, even if your MDM shows the profile as delivered. On Windows, even a misspelled value under `HKLM\SOFTWARE\Policies\Claude` counts as machine policy and locks the window, so use the Managed Configuration Report to see which keys were actually read. If your profile deliberately sets [only the update keys or the network proxy keys](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence), an editable window is expected.

If the app shows the standard claude.ai sign-in screen instead of Cowork, the configuration was not read. Common causes:

* `inferenceProvider` is missing, misspelled, or set to an unrecognized value
* The configuration was applied while the app was running (fully quit and relaunch)
* The configuration was written to the local config file but you're checking the managed location (or vice versa)
* A required key for the chosen provider is missing; check **Help → Troubleshooting** or the application log at `~/Library/Logs/Claude-3p/main.log` (macOS) / `%LOCALAPPDATA%\Claude-3p\Logs\main.log` (Windows)
* On Windows (v1.19367.0 and later), the configuration is in `HKCU\SOFTWARE\Policies\Claude` but machine policy is also present: any `REG_SZ`, `REG_EXPAND_SZ`, or `REG_DWORD` value directly under `HKLM\SOFTWARE\Policies\Claude` causes the app to ignore user policy entirely. The Managed Configuration Report (**Help → Troubleshooting → Copy Managed Configuration Report**) shows which source the app read. A `REG_EXPAND_SZ` value shows as present in `reg query` output while the app reports the managed configuration as invalid or absent, because the app counts the value as machine policy but cannot read its contents

## Troubleshooting

If installation or setup fails, generate a diagnostic report before requesting support: on the affected machine, go to **Help → Troubleshooting → Generate Diagnostic Report**, choose a save location, and send the resulting folder to your Anthropic representative.

The report contains the configuration state, application logs, and environment details needed to investigate. It does not include user data or conversation content.

## Endpoint security software

If your organization runs binary-authorization or EDR software (such as [Santa](https://santa.dev), CrowdStrike Falcon, or Microsoft Defender ASR) with path-based deny rules, the Cowork agent helper may be blocked from launching. The symptom is that Claude Desktop opens normally and reads the managed configuration, but Cowork sessions fail to start.

The agent helper is a signed binary that Claude Desktop installs under its user-data directory. **Allowlist by signing identity rather than path** so the rule survives version updates.

**macOS**

```
~/Library/Application Support/Claude-3p/claude-code/<version>/claude.app/Contents/MacOS/claude
```

The helper is Developer ID signed and notarized:

* Team ID: `Q6L2SF6YDW` (Anthropic PBC)
* Signing ID: `com.anthropic.claude-code`

For Santa, a `TEAMID` allow rule for `Q6L2SF6YDW` covers the helper across version updates. Standard (non-3P) installs use `~/Library/Application Support/Claude/` with the same subpath.

**Windows**

```
%LOCALAPPDATA%\Claude-3p\claude-code\<version>\claude.exe
```

The helper is Authenticode-signed with publisher `Anthropic, PBC`. For Defender ASR or AppLocker, allowlist by publisher rather than path. Standard installs use `%APPDATA%\Claude\` with the same subpath.

## Offline installation

Standard installs fetch two large runtime components from `downloads.claude.ai` at session start: the VM workspace bundle that Cowork sessions run in, and the Claude CLI binary. For networks that cannot reach `downloads.claude.ai`, Anthropic publishes an offline installer variant with both components built into the installer package and verified against checksums compiled into the application, so sessions can start without any connection to Anthropic. The offline installers are several gigabytes larger than the standard ones.

Each supported platform and architecture has a fixed download URL that serves the current offline installer:

| Platform              | Format  | Download URL                                                         |
| --------------------- | ------- | -------------------------------------------------------------------- |
| Windows (x64)         | `.msix` | `https://claude.ai/api/desktop/win32/x64/offline/latest/redirect`    |
| Windows (Arm)         | `.msix` | `https://claude.ai/api/desktop/win32/arm64/offline/latest/redirect`  |
| macOS (Apple silicon) | `.dmg`  | `https://claude.ai/api/desktop/darwin/arm64/offline/latest/redirect` |
| macOS (Intel)         | `.dmg`  | `https://claude.ai/api/desktop/darwin/x64/offline/latest/redirect`   |

Each URL responds with an HTTP redirect to a versioned installer file, so any HTTP client that follows redirects downloads the installer directly. New versions of Claude Desktop roll out to connected devices gradually; these URLs serve the newest version whose rollout has completed. The redirect's `Location` header contains the version number, so tooling can detect a new version by requesting the URL without following the redirect.

If the offline installer for the version the URL serves is not yet available, the download fails with HTTP 404 rather than falling back to an older installer; this can happen just after a new version appears in the `Location` header. Keep the installer you last downloaded and retry later.

Download the installer from a connected machine and bring it across your boundary with your usual software-distribution process.

Pair the offline installer with [`disableAutoUpdates`](/docs/third-party/claude-desktop/configuration#disableautoupdates): the app cannot reach the update feed from an air-gapped network, and you update the fleet by distributing each new offline installer through your MDM. Aside from updates, the only egress an air-gapped deployment needs is your inference provider; see [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths).

## Updates

By default, Claude Desktop downloads updates from Anthropic's update server automatically and applies them the next time the app restarts. If the app hasn't restarted within 72 hours of downloading an update, it restarts itself, waiting for 10 minutes of user inactivity before doing so. This enforcement is always on and offers no in-app prompt to defer the restart; the `autoUpdaterEnforcementHours` key tunes the 72-hour window rather than enabling it.

In 3P deployments you can:

* **Leave auto-update enabled** (recommended) so fixes reach users without IT intervention. Set `autoUpdaterEnforcementHours` to shorten the enforcement window (1 to 72 hours; values above 72 are rejected). Setting the key also makes the window strict: the restart fires as soon as the window elapses, without waiting for a pause in user activity.
* **Disable auto-update** (`disableAutoUpdates`) and redistribute new builds through your MDM on your own cadence. This is required for [air-gapped environments](#offline-installation) but means your IT team owns the update pipeline.

See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for the network paths the updater uses.
