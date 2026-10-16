> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Claude Science on devices

> Claude Science is a desktop application that stores member content locally.

Claude Science is a desktop application that stores member content locally. This page covers what IT and endpoint teams need to know: where the app writes data, how to deploy configuration with device management, what changes when Claude Science opens in its own window on a Mac, what telemetry is sent, and what members see when Anthropic requires an update.

## Where the app stores data

The app writes to these locations on each member's computer:

Configuration: config.toml in the app's default data folder (`~/.claude-science/config.toml` on macOS and Linux, `%USERPROFILE%\.claude-science\config.toml` on Windows) holds all app settings. Every key is optional; the app starts with no file present. This is the file to deploy through device management.\
Data: the app's data directory holds conversations, generated artifacts, delegation configurations, and workspace files in a per-organization subfolder (orgs/`<organization-id>`/), stored as a local database plus files.

Authentication tokens and the shared package environment live under the default data folder (`~/.claude-science/`, or `%USERPROFILE%\.claude-science\` on Windows) regardless of the data directory, so endpoint backup or wipe policies that target the data directory don't affect sign-in state.

On Windows and macOS, the program is in these places:

* **Windows**: the program itself installs per user to `%LOCALAPPDATA%\Programs\ClaudeScience` and registers under the signed-in user's **Settings** > **Apps** > **Installed apps** rather than machine-wide. The app also writes launch logs and state to `%LOCALAPPDATA%\ClaudeScience` and keeps a sandbox state folder under `%LOCALAPPDATA%`, and it unpacks components it runs, such as the app window engine and the sandbox launcher, under the data folder, so allow-listing by path needs both the program folder and the data folder. Uninstalling removes the program and sandbox state; `claude-science uninstall --purge` also removes the data and state folders.
* **macOS**: the app is **Claude Science** in the **Applications** folder, or in the **Applications** folder inside the member's home folder. When Claude Science opens in a browser tab, it runs its program from a copy at `~/.claude-science/bin/claude-science`. When it opens in its own window, it runs the program from inside the app. In its own window, Claude Science also keeps window settings, logs, and the window's page storage, which includes unsent message drafts, in `~/Library/Application Support/Claude Science` (see [Macs where Claude Science opens in its own window](#macs-where-claude-science-opens-in-its-own-window)).

Your endpoint tooling governs these folders the same way it governs any other local application data. Anthropic doesn't host a copy of these folders, so Custom Data Retention and Org Data Export don't reach them. [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) covers what Anthropic does receive from the app, including the session transcripts available to Enterprise organizations with the Compliance API enabled.

## Deploy configuration with device management

To set configuration keys organization-wide, deploy the per-member config.toml (at the path given under [Where the app stores data](#where-the-app-stores-data)) through your MDM or endpoint tool. Claude Science doesn't read its settings from a system-level managed-preferences file or registry policy keys, so there's no native MDM configuration channel on any operating system. Deploying the per-member config.toml is the supported approach. The sandbox network allowlist and the package mirror can instead be set once for every member under **Organization settings** > **Claude Science** (see [Organization settings](/docs/claude-science/admin-controls#organization-settings)). The keys most relevant to admins are:

| Key | Effect |
| - | - |
| `disable_telemetry = true` | Stops the app from sending product-usage telemetry and error reports to Anthropic. |
| `data_dir = "<path>"` | Moves conversations, artifacts, and workspaces to a managed location (for example, a volume your backup tooling covers). |
| `auto_update = false` under `[update]` | Turns off the background check for updates on Windows, on Linux, and on a Mac where Claude Science opens in a browser tab; pair with your own distribution channel. A member can still check for and install an update from inside Claude Science. |
| `enabled = false` under `[sandbox.network]` | Blocks network access from the app's local code-execution sandbox. The similarly named `network_isolated` key under `[sandbox]` doesn't control this. |

The [configuration file reference](/docs/claude-science/configuration-file-reference) documents the network-related keys and their defaults, and [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks) covers the proxy, TLS-inspection, and mirror settings.

## Macs where Claude Science opens in its own window

On a Mac, Claude Science opens either in a browser tab or in its own window. When a member installs an update from inside Claude Science, the update can switch Claude Science to its own window. It switches only if the member's account owns the installed app and can replace it, so a copy that device management installed as root never switches. When the account that owns the app switches it, Claude Science opens in its own window for every account that opens that copy.

Claude Science in its own window has the bundle identifier `com.anthropic.claudescience`, so macOS treats it as a different app from Claude Science in a browser tab. Add an entry for `com.anthropic.claudescience` to any Privacy Preferences Policy Control (PPPC) profile that grants Claude Science access. An allow-list rule on the Apple Team ID `Q6L2SF6YDW` covers both apps, and also the app's helper programs, which are signed with identifiers such as `com.anthropic.claudescience.helper`.

Claude Science in a browser tab and in its own window get updates in different ways:

| What differs | In a browser tab | In its own window |
| - | - | - |
| Updates | Checks in the background and shows **Update available** | Downloads updates by itself and installs them when the app quits |
| Connections for updates | Use the app's proxy settings | Use the proxy in macOS network settings and the certificates that macOS trusts (see [Proxy and certificates for updates in the Mac app window](/docs/claude-science/corporate-networks#proxy-and-certificates-for-updates-in-the-mac-app-window)) |

If the member's account can't write to the app or its folder, Claude Science in its own window doesn't check for updates in the background. The member can still choose **Claude Science > Check for App Updates…**, and macOS then asks for an administrator's password to install the update.

Setting `auto_update = false` under `[update]` doesn't stop Claude Science from switching to its own window, because a member can still install an update from inside Claude Science.

## Telemetry

The app sends product-usage telemetry (event counts and timings, not conversation content) to Anthropic. There's no in-app setting for this; consent is covered by your organization's acceptance of Anthropic's commercial terms.

When the app runs into an error, it also sends an error report to the error-reporting service Anthropic uses that identifies the error type and where it occurred in Claude Science's own code. The report includes the app version, its runtime version, the operating system version, and the app's most recent telemetry events. The app redacts each report on the member's computer before sending it: error messages are removed, and code locations outside Claude Science's own code are blanked. Reports contain no conversation content, research data, file contents, or file paths, and no usernames, account identifiers, or organization identifiers.

To turn telemetry and error reports off on managed devices, use either of:

Set disable\_telemetry = true in config.toml (deployable through MDM).\
Set the DO\_NOT\_TRACK environment variable (for example to 1) where the app reads it at launch. See [How the environment variables reach the app](/docs/claude-science/corporate-networks#how-the-environment-variables-reach-the-app).

Both are device-level settings. There's no per-member or per-organization telemetry toggle in Organization settings.

## Endpoint detection and response

Claude Science runs analysis code inside a local sandbox on the member's computer. On macOS, sandboxed analysis processes run as ordinary child processes and are visible to host-level EDR tools. On Windows, they run under the member's account inside a Windows AppContainer, the operating system's built-in app isolation, started by a sandbox launcher that ships inside the app, without WSL or Hyper-V. Windows asks once, optionally, for administrator approval so that Command Prompt scripts and git can run inside cells and PowerShell cells can change folders, while Python and R cells work without it. If security software holds the sandbox launcher or quarantines files in an analysis environment, Claude Science names the affected folder in its error message so you can add an exclusion. On Linux, sandboxed processes run inside a separate PID namespace with an isolated process view, so host-level EDR won't see them as ordinary children of the app.

## Windows signing certificate

Claude Science for Windows is signed by Anthropic, PBC. If your security software allows apps by their signature, allow the publisher, Anthropic, PBC, rather than one exact certificate, because a renewed certificate has a new thumbprint.

If you allow by SHA-1 thumbprint, keep both of these on your list until every PC runs version 0.1.61 or later:

* **From version 0.1.61**: `60C2D9C51F09822FFF4F194DE9EEDB67451292D1` (valid until October 28, 2027)
* **Through version 0.1.60**: `0D7581D2C51C59DF686C3000C70BF543F9F6C6CB`

Windows still treats versions signed with the certificate used through version 0.1.60 as validly signed after that certificate expires, because each signature carries a trusted timestamp.

## Required updates

Anthropic may set a minimum supported version of the app. When a member's installed version falls below that floor, the app shows a full-page notice that the installed version is no longer supported and blocks further use until the member updates. Admins don't configure this floor; it's set by Anthropic. If your organization distributes the app through its own channel with auto-update disabled, plan to push updates promptly when Anthropic raises the floor.
