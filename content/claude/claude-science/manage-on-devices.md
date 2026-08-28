> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Claude Science on devices

> Claude Science is a desktop application that stores member content locally.

Claude Science is a desktop application that stores member content locally. This page covers what IT and endpoint teams need to know: where the app writes data, how to deploy configuration with device management, what telemetry is sent, and what members see when Anthropic requires an update.

## Where the app stores data

The app writes to two locations on each member's computer:

Configuration: \~/.claude-science/config.toml holds all app settings. Every key is optional; the app starts with no file present. This is the file to deploy through device management.\
Data: the app's data directory holds conversations, generated artifacts, delegation configurations, and workspace files in a per-organization subfolder (orgs/`<organization-id>`/), stored as a local database plus files.

Authentication tokens and the shared package environment live under \~/.claude-science/ regardless of the data directory, so endpoint backup or wipe policies that target the data directory don't affect sign-in state.

Your endpoint tooling governs these folders the same way it governs any other local application data. Anthropic doesn't host a copy of these folders, so Custom Data Retention and Org Data Export don't reach them. [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) covers what Anthropic does receive from the app, including the session transcripts available to Enterprise organizations with the Compliance API enabled.

## Deploy configuration with device management

To set configuration keys organization-wide, deploy \~/.claude-science/config.toml through your MDM or endpoint tool. Claude Science doesn't read a system-level managed-preferences file, so there's no native MDM configuration channel. Deploying the per-member config.toml is the supported approach. The keys most relevant to admins are:

| Key                                | Effect                                                                                                                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| disable\_telemetry = true          | Stops the app from sending product-usage telemetry to Anthropic.                                                                               |
| data\_dir = "`<path>`"             | Moves conversations, artifacts, and workspaces to a managed location (for example, a volume your backup tooling covers).                       |
| \[update] auto\_update = false     | Prevents the app from updating itself; pair with your own distribution channel.                                                                |
| \[sandbox.network] enabled = false | Blocks network access from the app's local code-execution sandbox. The similarly named \[sandbox] network\_isolated key does not control this. |

The [configuration file reference](/docs/claude-science/configuration-file-reference) documents the network-related keys and their defaults, and [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks) covers the proxy, TLS-inspection, and mirror settings.

## Telemetry

The app sends product-usage telemetry (event counts and timings, not conversation content) to Anthropic. There's no in-app setting for this; consent is covered by your organization's acceptance of Anthropic's commercial terms. To turn telemetry off on managed devices, use either of:

Set disable\_telemetry = true in \~/.claude-science/config.toml (deployable through MDM).\
Set the DO\_NOT\_TRACK environment variable on the device.

Both are device-level settings. There's no per-member or per-organization telemetry toggle in Organization settings.

## Endpoint detection and response

Claude Science runs analysis code inside a local sandbox on the member's computer. On macOS, sandboxed analysis processes run as ordinary child processes and are visible to host-level EDR tools. On Linux, they run inside a separate PID namespace with an isolated process view, so host-level EDR won't see them as ordinary children of the app.

## Required updates

Anthropic may set a minimum supported version of the app. When a member's installed version falls below that floor, the app shows a full-page notice that the installed version is no longer supported and blocks further use until the member updates. Admins don't configure this floor; it's set by Anthropic. If your organization distributes the app through its own channel with auto-update disabled, plan to push updates promptly when Anthropic raises the floor.
