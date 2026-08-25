> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with MDM

> Author a full configuration in the app, export it as a profile, and deploy it fleet-wide with Jamf, Intune, Group Policy, or any MDM

On the MDM delivery model, the profile you deploy carries your organization's full configuration, and every device the profile targets gets the same settings. This page covers the workflow end to end: build the configuration in the app, export it, open the firewall, and deploy the profile and installer to your fleet.

Before you start, install Claude Desktop on an admin workstation; see [Installation and setup](/docs/third-party/claude-desktop/installation). If you deliver configuration from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap) instead, follow that page; your profile then carries only the bootstrap keys, but it is exported and deployed the same way described here.

## Recommended rollout

Roll out in this order; the numbered sections on this page cover each step in detail.

<Steps>
  <Step title="Build a configuration in the app">
    An admin builds and tests a working configuration in the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) on their own device.
  </Step>

  <Step title="Export the profile">
    Export the validated configuration in the format your MDM expects.
  </Step>

  <Step title="Allow required network egress">
    Open the hostnames your configuration requires on your perimeter firewall; the configuration window lists them for the exact settings you chose.
  </Step>

  <Step title="Deploy the configuration, then the app">
    Distribute the profile through your MDM, then push the installer. Deploying the configuration first means users open Claude for the first time and land directly in the third-party deployment, with no opportunity to sign in to claude.ai by mistake.
  </Step>
</Steps>

## 1. Build a configuration in the app

Launch Claude Desktop. **Do not sign in or create an Anthropic account**; stay on the login screen. From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the login screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure Third-Party Inference…** to open the configuration window.

The window is organized into sections in the left sidebar. Work through them in order; each maps to a group of [configuration keys](/docs/third-party/claude-desktop/configuration), and the window validates values as you enter them.

| Section                 | What you set                                                                                                                                                                                                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connection**          | Inference provider (Gateway, Claude API, Google Cloud's Agent Platform, Bedrock, Bedrock Mantle, or Foundry) and its credentials<br />Model list<br />Organization UUID<br />Optional credential-helper script                                                                                     |
| **Workspace**           | Which of Cowork, Code, and Chat are available<br />Allowed egress hosts for the sandbox<br />Disabled built-in tools<br />Allowed workspace folders                                                                                                                                                |
| **Connectors**          | Managed MCP servers pushed to all users<br />Whether users can add their own local MCP servers<br />Whether desktop extensions (`.mcpb`) are allowed<br />Whether unsigned extensions are rejected                                                                                                 |
| **Telemetry & updates** | OpenTelemetry collector endpoint<br />Whether auto-updates are blocked, and the enforcement window if not<br />The three Anthropic-bound telemetry toggles (essential, nonessential, nonessential services)                                                                                        |
| **Limits**              | Per-device token cap and its window length                                                                                                                                                                                                                                                         |
| **Appearance**          | Persistent banner shown across the app window<br />Deployment display name and subtitle<br />Whether the signed-in user's identity is shown and exported (end-user attribution)<br />Whether feature announcements are shown                                                                       |
| **Plugins**             | [Plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin), added by GitHub repo, git URL, or hosted `marketplace.json` URL<br />Shows the org-plugins folder path for your platform; plugin bundles are mounted to that folder via your MDM, not through this window |
| **Egress**              | A read-only firewall allowlist derived from everything you've entered above, grouped by feature<br />**Copy hostnames**, **Download .txt**, and **Test connectivity** actions                                                                                                                      |
| **Source**              | The bootstrap keys, if you are using the [bootstrap server](/docs/third-party/claude-desktop/bootstrap) delivery model instead of a full MDM profile<br />Bootstrap-delivered configuration takes priority over MDM-delivered values: it replaces them wholesale rather than merging key by key         |

<Note>
  When a managed (MDM-delivered) configuration is already present on the device, the configuration window opens read-only: it shows what the admin deployed, marks the configuration as organization-managed, and directs users to their IT administrator. To author a new configuration, use a device without a managed profile, or temporarily remove the profile. Profiles that set [only the update keys](#update-keys-and-managed-precedence) leave the window editable.
</Note>

## 2. Export the profile

Once your configuration tests successfully, click **Export** and choose a format:

| Format                      | Platform | Deploy with                                                                                                     |
| --------------------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `.mobileconfig`             | macOS    | Jamf, Kandji, Mosyle, Workspace ONE, or any Apple MDM                                                           |
| `.reg`                      | Windows  | Group Policy (import into a GPO), Intune (via custom ADMX or script), or any MDM that can write registry policy |
| `.zip` (ADMX template)      | Windows  | Schema-only template for Intune or Group Policy; you enter values in the management console                     |
| `.plist` (Profile Manifest) | macOS    | Schema-only template for Jamf, ProfileCreator, or similar macOS tools                                           |

The two actions in the configuration window do different things:

* **Apply locally** writes the selected configuration to your own machine's Claude settings and relaunches the app, so you can test it end to end before deploying it.
* **Export** writes a deployment file in the format you choose and leaves your local settings untouched.

### Creating profiles for multiple user groups

Many organizations deploy distinct configurations to different populations: for example, a permissive profile for an engineering pilot group and a restricted profile for the broader rollout, or per-region profiles that point at different inference endpoints.

The configuration window can hold multiple named configurations. Use the picker in the top-right of the window:

* **New configuration** creates an empty configuration.
* **Duplicate** copies the current configuration as a starting point for a variant.
* **Rename** and **Delete** manage the list.
* **Reveal in Finder** opens the on-disk location where saved configurations are stored.

Selecting a configuration in the picker loads it for editing; the **applied** badge marks the one currently active on your machine. **Apply locally** and **Export** each act on whichever configuration is selected, so you can test each one locally and export them independently.

In your MDM, scope each exported profile to the corresponding device or user group. Targeting is handled by your MDM's assignment rules; the configuration name is for your authoring workflow and is not part of the deployed profile.

<Note>
  On Windows, check which registry hive your assignment rules write to. If your assignment rules deliver a profile in user context, it lands in user policy (`HKCU`), and the app ignores user policy entirely when machine policy is present; see [Deploy the configuration](#4-deploy-the-configuration). To vary configuration per user group on Windows, deliver every profile through user policy and keep `HKLM\SOFTWARE\Policies\Claude` empty, or serve per-user configuration from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap).
</Note>

## 3. Allow required network egress

The hosts the app needs to reach depend on the configuration you built: your inference provider's endpoint is always required, and each telemetry, update, and service setting you leave enabled adds its own hosts. The configuration window shows the exact allowlist for your settings and can export it as a text file for your network team.

<Warning>
  `downloads.claude.ai` is required to run the app regardless of your configuration: it serves the VM workspace bundle and the latest Claude Code binary, fetched at session start. Without it, Cowork sessions cannot start. The [offline installer variant](/docs/third-party/claude-desktop/installation#offline-installation) builds both components into the installer package and does not need this host.
</Warning>

Open these hosts on your perimeter firewall before rolling out to devices. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths) for the full list of hosts grouped by the setting that controls each one, and for the distinction between the perimeter firewall and the in-app sandbox allowlist.

## 4. Deploy the configuration

Push the exported configuration through your MDM. The app reads from these locations:

<Tabs>
  <Tab title="macOS">
    | Source             | Path                                                                       | Precedence |
    | ------------------ | -------------------------------------------------------------------------- | ---------- |
    | Managed (per-user) | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` | Highest    |
    | Managed (machine)  | `/Library/Managed Preferences/com.anthropic.claudefordesktop.plist`        |            |
    | Local (user)       | `~/Library/Application Support/Claude-3p/configLibrary/`                   | Lowest     |

    A `.mobileconfig` profile delivered by MDM lands in the Managed Preferences locations automatically. Both managed paths are read; where a key appears in both, the per-user value wins.
  </Tab>

  <Tab title="Windows">
    | Source         | Path                                      | Precedence |
    | -------------- | ----------------------------------------- | ---------- |
    | Machine policy | `HKLM\SOFTWARE\Policies\Claude`           | Highest    |
    | User policy    | `HKCU\SOFTWARE\Policies\Claude`           |            |
    | Local (user)   | `%LOCALAPPDATA%\Claude-3p\configLibrary\` | Lowest     |

    A Group Policy Object or Intune configuration profile writes to the registry policy paths. The hives are not merged: when machine policy is present (any `REG_SZ`, `REG_EXPAND_SZ`, or `REG_DWORD` value directly under `HKLM\SOFTWARE\Policies\Claude`, including an empty string, and the key's unnamed default value when set), the app ignores `HKCU\SOFTWARE\Policies\Claude` entirely. Deploy the complete configuration to one hive; machine policy (`HKLM`) is the recommended location.

    <Warning>
      Values must sit directly under `HKLM\SOFTWARE\Policies\Claude` or `HKCU\SOFTWARE\Policies\Claude`. The app never reads values nested in a subkey, as some ADMX-based and Policy CSP tooling writes them: they do not apply as configuration and do not count as machine policy being present. Write values as `REG_SZ` (`REG_DWORD` is also accepted for boolean and integer keys and is read as its decimal value). Avoid `REG_EXPAND_SZ`: the app counts it as machine policy being present but cannot read its contents, so a single `REG_EXPAND_SZ` value under `HKLM` disables user policy without supplying any configuration. The app cannot see `REG_QWORD`, `REG_MULTI_SZ`, or `REG_BINARY` values at all.
    </Warning>

    <Note>
      In releases before v1.19367.0, the app read both hives and merged them key by key, with the `HKLM` value winning where a key appeared in both. Fleets that split keys across both hives must consolidate the full configuration into one hive before updating to v1.19367.0 or later.
    </Note>
  </Tab>
</Tabs>

When a managed source sets any key other than the update keys, the managed configuration owns the device: it takes effect, the in-app configuration window becomes read-only, and locally authored values in `configLibrary/` are ignored.

### Update keys and managed precedence

The update keys `disableAutoUpdates`, `autoUpdaterEnforcementHours`, and `updateViaUpdatesHost` are treated specially, so you can set an update policy from MDM without managing the whole configuration. When a managed source sets only these keys (any of them), the device keeps its locally authored configuration and the configuration window stays editable. The update keys themselves are still enforced as a group: all of them are resolved from the managed source alone, so a locally set value for any of them is ignored even if the profile sets only one.

If the managed profile sets any other recognized key, the normal rule above applies and the whole configuration is managed.

## 5. Distribute the app

Deploy the Claude Desktop installer to enrolled devices using your standard software-distribution mechanism. On launch, the app reads the managed configuration, detects the configured inference provider and credentials, and the sign-in screen offers users the option to start in Claude Desktop on 3P.

## 6. Deploy organization plugins (optional)

If you're distributing [organization plugins](/docs/third-party/claude-desktop/extensions#organization-plugins-admin), push the plugin bundles to the org-plugins directory on each device alongside the configuration profile. Plugins are picked up at the next app launch.

## Next steps

After deployment, confirm devices picked up the configuration with the checks in [Verifying the deployment](/docs/third-party/claude-desktop/installation#verifying-the-deployment).
