> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration implementation

> Compare where Claude Desktop on 3P reads configuration in each kind of deployment, and write values for a profile, the registry, or the Linux file

You configure Claude Desktop on third-party (3P) with the keys in the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) in every kind of deployment, but where you set them, how they reach the app, and how you write their values differ between a device's own configuration, the Enterprise Admin Console, and a self-hosted install.

> [!NOTE]
>
> To choose how configuration reaches your devices, see [Choose a configuration delivery model](https://claude.com/docs/third-party/claude-desktop/installation.md#choose-a-configuration-delivery-model).

## How configuration differs by deployment

Each kind of deployment stores and delivers the configuration differently.

| | [Configuration on the device](#configuration-on-the-device) | [Enterprise Admin Console](#configuration-from-the-enterprise-admin-console) | [Self-hosted install](#configuration-on-a-self-hosted-install) |
| - | - | - | - |
| Where the configuration lives | In an MDM profile or registry policy, in the local configuration file, or on a bootstrap server that the device points to | In your organization's settings on claude.ai, which Anthropic hosts | Keys labeled **Server side** live in the document your session host reads. Keys labeled **MDM profile** live in Claude Desktop's own configuration on the device |
| How it reaches the app | The app reads it at launch, or fetches it from your bootstrap server. Users don't sign in to a Claude account | Each user signs in with their work account, and the app downloads the settings that apply to them | Sessions run on a session host your organization operates, which applies a **Server side** key itself or passes it on to Claude Desktop. Claude Desktop reads keys labeled **MDM profile** from the device, as on any device |
| What an MDM profile does | Carries the full configuration, or the bootstrap keys | You don't need one. A profile on the device can still decide some settings, or keep the device off the console. See [What an MDM profile does alongside the Enterprise Admin Console](#what-an-mdm-profile-does-alongside-the-enterprise-admin-console) | Usually names the session host, and carries the keys labeled **MDM profile**. See [What an MDM profile does on a self-hosted install](#what-an-mdm-profile-does-on-a-self-hosted-install) |
| How you write values | Strings in a macOS profile or the Windows registry. JSON in the Linux file or a bootstrap response | Fields on the console's pages, or JSON in an imported file or an Admin API request | As on any device, for keys labeled **MDM profile**. See [Value types in a profile or registry policy](#value-types-in-a-profile-or-registry-policy) |
| Where to go next | [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md), [Deploy with a bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) | [Deploy with Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) | [Keys that work on a self-hosted install](https://claude.com/docs/third-party/claude-desktop/configuration.md?works-with=self-hosted) |

## Configuration on the device

> [!TIP]
>
> Most settings are easier to configure in the [in-app configuration window](https://claude.com/docs/third-party/claude-desktop/in-app-configuration.md) (**Developer → Configure Third-Party Inference…**), which validates values, shows per-provider requirements, and exports directly to `.mobileconfig` or `.reg`. To write an MDM profile, registry policy, or bootstrap response yourself, start with [Where Claude Desktop reads configuration on a device](#where-claude-desktop-reads-configuration-on-a-device).

On the device, Claude Desktop reads its configuration from OS-native managed preferences (a `.mobileconfig` profile on macOS, registry policy on Windows, or a root-owned JSON file on Linux) or from the local configuration file that the in-app configuration window writes. Either one can instead carry the bootstrap keys that point at a bootstrap server you host.

### Where Claude Desktop reads configuration on a device

Claude Desktop reads a managed location and a local location on each platform.

| Platform | Managed (MDM) location | Local (user) location |
| - | - | - |
| macOS | `/Library/Managed Preferences/<user>/com.anthropic.claudefordesktop.plist` (per user), `/Library/Managed Preferences/com.anthropic.claudefordesktop.plist` (machine) | `~/Library/Application Support/Claude-3p/configLibrary/` |
| Windows | `HKLM\SOFTWARE\Policies\Claude` (machine), `HKCU\SOFTWARE\Policies\Claude` (user) | `%LOCALAPPDATA%\Claude-3p\configLibrary\` |
| Linux | `/etc/claude-desktop/managed-settings.json` | `~/.config/Claude-3p/configLibrary/` |

The local location is a directory: `_meta.json` records which saved configuration is applied, and each configuration is a `<id>.json` file alongside it. The in-app configuration window writes here.

### Which configuration source applies on a device

* **A managed source and a local file**: when a managed source sets any key other than the [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), the managed configuration takes effect and locally written values are ignored.
* **A managed source that sets only app-behavior keys**: those keys (the update keys `disableAutoUpdates`, `autoUpdaterEnforcementHours`, `installedUpdateEnforcementEnabled`, `installedUpdateEnforcementHours`, `updateViaUpdatesHost`, and [`releaseChannel`](https://claude.com/docs/third-party/claude-desktop/configuration#releasechannel), the lifecycle keys `relaunchEnforcementHours` and `configRecheckIntervalMinutes`, and the [network proxy keys](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#pin-a-proxy-from-managed-configuration) `egressProxyUrl` and `egressProxyPacUrl`) are enforced from the managed source, but the rest of the configuration stays local and user-editable. Any of those keys that the profile leaves out runs its default.
* **A bootstrap response**: when a response is available, it is the effective configuration, apart from the app-behavior keys where a profile sets only those. A key that the server can set and your response omits is treated as unset, not inherited from the profile. The app ignores the keys labeled **MDM only** in the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) in a response, so set them in the profile or the local file.
* **Two macOS managed paths**: both are read, and where a key appears in both, the app uses the per-user value.
* **Two Windows policy hives**: the hives aren't merged. When machine policy is present under `HKLM\SOFTWARE\Policies\Claude`, the app ignores `HKCU\SOFTWARE\Policies\Claude` entirely.

[Deploy the configuration](https://claude.com/docs/third-party/claude-desktop/mdm.md#4-deploy-the-configuration) has the exact rules for managed sources. For a bootstrap response, see also [Keys that require user consent](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent) and [Origin pinning](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#origin-pinning).

> [!NOTE]
>
> Claude Desktop on 3P reads the same managed-configuration sources as standard Claude Desktop but ignores keys scoped to standard deployments, except [`forceLoginOrgUUID`](https://claude.com/docs/cowork/hipaa-setup#what-each-claude-desktop-key-does), as described under [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile).

### When a configuration change on a device takes effect

Configuration takes effect **at launch**, so fully quit and reopen the app after any change. A running app also notices a changed managed configuration at its next re-check ([`configRecheckIntervalMinutes`](https://claude.com/docs/third-party/claude-desktop/configuration#configrecheckintervalminutes), 10 minutes by default) and, for most settings, prompts the user to restart and requires the restart after [`relaunchEnforcementHours`](https://claude.com/docs/third-party/claude-desktop/configuration#relaunchenforcementhours) (24 hours by default). The re-check of a managed configuration requires Claude Desktop 1.46388.1 or later. On those releases a changed bootstrap response follows the same re-check and restart window. Earlier releases re-check a response every 30 minutes. See [How it works](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#how-it-works) and [Availability](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#availability).

### Value types in a profile or registry policy

Write every value as a **string** in the OS preference store, even booleans and arrays. This rule applies to plist and registry sources. [The Linux file](#the-linux-configuration-file) and a [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#response-schema) take JSON values. Each key's entry in the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) gives the key's type and the values or fields it accepts.

| Documented type | What to write | Example |
| - | - | - |
| string | Plain string | `vertex` |
| boolean | `"true"` or `"false"` (or `1` / `0`) | `"true"` |
| enum | One of the values the key's entry lists, as a plain string | `gateway` |
| integer | Decimal string | `"3600"` |
| number | Decimal string | `"0.85"` |
| string\[] (JSON) | JSON array **encoded as a string** | `["claude-sonnet-5","claude-opus-5"]` |
| enum\[] (JSON) | JSON array of values the key's entry lists, **encoded as a string** | `["userPrompts","toolDetails"]` |
| object: name → value (JSON) | JSON object mapping name to value, as a string | `{"X-Org-Id":"team1"}` |
| object (JSON) | JSON object with the fields the key's entry lists, as a string | see [`inferenceIdpOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpoidc) |
| object\[] (JSON) | JSON array of objects, as a string | see [`managedMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) |

> [!NOTE]
>
> Array- and object-typed keys such as `inferenceModels`, `inferenceGatewayOidc`, `managedMcpServers`, `coworkEgressAllowedHosts`, and `otlpHeaders` are single keys whose value is a whole JSON document. The portable encoding is a JSON string, which works on every platform. In a `.mobileconfig` that is a single `<string>` element containing `[...]` or `{...}`, and on Windows a `REG_SZ` value. A macOS profile may instead carry the value as a native `<array>` or `<dict>`, which the app reads as the equivalent JSON. Separate keys with dotted names, such as `inferenceGatewayOidc.clientId`, are never read.

On Windows, write registry values as `REG_SZ`, directly under the policy key rather than nested in a subkey (the app never reads subkeys). `REG_DWORD` is also accepted for boolean and integer keys and is read as its decimal value. Avoid `REG_EXPAND_SZ`: the app counts it toward machine policy being present but can't read its contents. The app can't see `REG_QWORD`, `REG_MULTI_SZ`, or `REG_BINARY` values at all.

### The Linux configuration file

The managed source on Linux is a single JSON file, `/etc/claude-desktop/managed-settings.json`, with keys at the top level exactly as named in the [reference](https://claude.com/docs/third-party/claude-desktop/configuration.md), with no wrapper object and no nesting:

```json theme={null}
{
  "inferenceProvider": "gateway",
  "inferenceGatewayBaseUrl": "https://gateway.example.com/v1",
  "inferenceGatewayApiKey": "sk-example",
  "inferenceCustomHeaders": { "X-Tenant-Id": "acme" }
}
```

Because the file is real JSON, array- and object-typed keys use native JSON values. String-encoded values are also accepted, so a profile generated for another platform can be reused.

The file is only honored when it can't be edited by the user it configures:

* `managed-settings.json` must be a regular file (not a symlink), owned by root, and not group- or world-writable.
* `/etc/claude-desktop` itself must be a directory (not a symlink), owned by root, and not group- or world-writable.

A file that fails these checks is rejected: none of its settings are applied, the app treats the device as managed but unreadable, and local settings are also disabled until the file is fixed and the app is relaunched. The reason is logged to `main.log` in the app's logs directory, `~/.config/Claude/logs/` (or `~/.config/Claude-3p/logs/` once the app is running in 3P mode). Search the log for `managed-settings.json`. The same log names any key that fails schema validation.

There is no per-user managed location on Linux. Per-user configuration goes through the in-app configuration window, which writes to the local `configLibrary` directory listed under [Where Claude Desktop reads configuration on a device](#where-claude-desktop-reads-configuration-on-a-device).

## Configuration from the Enterprise Admin Console

From the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), administrators edit the configuration in a browser, and no MDM profile or bootstrap server is needed.

* **Where you edit it**: each field in the **Desktop 3P** section of **Organization settings** on [claude.ai](https://claude.ai) sets one of the documented configuration keys. A [permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies) sets the settings that differ for one group of users.
* **How the app gets it**: the app contacts `api.anthropic.com` at every launch to check the user's sign-in and download the configuration. Until that download succeeds, the app can't connect to your inference provider. [Configuration kept on devices](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-kept-on-devices) covers what each device keeps of the last download and applies meanwhile.
* **What the console can't set**: among others, API keys, tokens, and secrets (apart from the client secret of a Google Desktop-app OAuth client), bootstrap keys and settings that only make sense on the device, keys that Anthropic fills in from your organization's settings, such as its name, and the Claude API as the inference provider. See [Limitations](https://claude.com/docs/third-party/claude-desktop/admin-console.md#limitations).
* **How you write values**: enter each value in its field, [import a JSON configuration](https://claude.com/docs/third-party/claude-desktop/admin-console.md#start-from-an-existing-configuration-file), or replace the whole configuration as one nested JSON document with the [Admin API](https://claude.com/docs/third-party/claude-desktop/admin-console.md#manage-the-configuration-with-the-admin-api). A value set in the console needs no approval from the user.
* **When a change takes effect**: at launch. A running app also re-checks every 10 minutes by default and, for most settings, asks the user to relaunch. The 10-minute default requires Claude Desktop 1.46388.1 or later. Earlier releases re-check about every 30 minutes. See [Configuration updates](https://claude.com/docs/third-party/claude-desktop/admin-console.md#configuration-updates).

### What an MDM profile does alongside the Enterprise Admin Console

* **`disableDeploymentModeChooser` set to `true`**: the device stays on the profile's configuration and ignores the console. A device that already moved returns to the profile at its next launch.
* **Only [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence)**: the profile's values apply instead of the console's for all of those keys. Any of those keys that the profile leaves out runs its default.
* **Any other key**: the device uses the profile's configuration until its user moves the device to the console's configuration by signing in, which requires Claude Desktop 2.37337.0 or later. With `forceLoginOrgUUID` set to your organization's ID, the user can move the device only to your organization's configuration. After the move, the app still takes a few keys from the profile, for example the network proxy keys. Other settings come from the console, and the profile's values don't apply even where the console leaves a setting unset.

[Which settings apply on a device with a managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#which-settings-apply-on-a-device-with-a-managed-profile) lists the keys that the app takes from the profile, and [Keep a device on its managed profile](https://claude.com/docs/third-party/claude-desktop/admin-console.md#keep-a-device-on-its-managed-profile) covers the keys that prevent or limit the move.

## Configuration on a self-hosted install

On a self-hosted install, sessions run on a session host that your organization operates and not on the person's device. Each key's label in the reference says which place in the following table counts for it.

| Place | Label of its keys in the reference | Who acts on the key |
| - | - | - |
| The document your session host reads | **Server side** | The session host. It applies the key itself, or passes it on to Claude Desktop, which applies it in its own windows or on the person's device. |
| Claude Desktop's own configuration on the device: an MDM profile, the local file, or a bootstrap server that configuration names | **MDM profile** | Claude Desktop, by the same rules as [configuration on the device](#which-configuration-source-applies-on-a-device). The session host ignores the key. |
| The session host's own configuration | **Not supported**, for the matching keys | Whoever runs the host sets the host's route to the model, and names your telemetry collector's address, protocol, and headers in the host's own configuration. |

An MDM profile that sets only [app-behavior keys](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence) decides all of those keys itself, whatever their label. Outside that case, nothing acts on a key labeled **Not supported**, wherever you set it.

The label is what the current Claude Desktop release declares. On that release, a session host acts on a **Server side** key only from the host version that reads it. Until then, unless an MDM profile sets only app-behavior keys, nothing applies the key, and Claude Desktop doesn't fall back to a value set on the device. An earlier Claude Desktop release can still apply a value set on the device, so keep a restriction in the MDM profile as well until every device runs the current release.

Each key's entry in the reference gives its label and a one-line reason. The [published schemas](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#response-schema) carry the self-hosted word (`server`, `reported`, `client`, or `none`) and its reason in `x-selfHosted` for each key they list. The [legend for the self-hosted labels](https://claude.com/docs/third-party/claude-desktop/configuration.md#self-hosted-column) defines the labels and maps each word to its label.

### What an MDM profile does on a self-hosted install

The MDM profile usually names the session host, and carries the keys labeled **MDM profile**. Each of those keys is about the person's device, as its reason in the reference says. For example:

* **Sign-in to the session host**: on a self-hosted install [`inferenceCredentialKind`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencecredentialkind) names the device's sign-in to the host, never the host's model credential, and [`inferenceIdpOidc`](https://claude.com/docs/third-party/claude-desktop/configuration#inferenceidpoidc) configures the sign-in that the device reuses for the host.
* **The device's network proxy**: [`egressProxyUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#egressproxyurl) and [`egressProxyPacUrl`](https://claude.com/docs/third-party/claude-desktop/configuration#egressproxypacurl).
* **Telemetry and updates**: [`disableEssentialTelemetry`](https://claude.com/docs/third-party/claude-desktop/configuration#disableessentialtelemetry) and [`disableAutoUpdates`](https://claude.com/docs/third-party/claude-desktop/configuration#disableautoupdates).

Write each value in the profile as [Value types in a profile or registry policy](#value-types-in-a-profile-or-registry-policy) describes.

### When a change takes effect on a self-hosted install

* **A key in the session host's document**: the host refreshes its own copy at least every [`configRecheckIntervalMinutes`](https://claude.com/docs/third-party/claude-desktop/configuration#configrecheckintervalminutes) (10 minutes by default) and tells Claude Desktop how often to ask it again.
* **A key on the device**: as on any device. The re-check interval and the restart window are themselves **Server side** keys, so the session host's document sets them, unless an MDM profile sets only app-behavior keys. See [When a configuration change on a device takes effect](#when-a-configuration-change-on-a-device-takes-effect).

A value that the session host delivers for a field labeled **Consent required** applies after the user approves it. Where machine-scoped device management set the host's address, the value applies without a prompt. [`trustBootstrapDelivery`](https://claude.com/docs/third-party/claude-desktop/configuration#trustbootstrapdelivery) covers what a bootstrap server delivers, not what a session host delivers.
