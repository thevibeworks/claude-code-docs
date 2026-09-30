> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Claude Code to Claude for Government

> Deploy the managed settings that send the Claude Code command-line tool to Claude for Government sign-in, limit what it contacts before a user signs in, and verify the result on macOS, Windows, and Linux.

> **Who this is for:** IT administrators who install the Claude Code command-line tool on agency devices and connect it to Claude for Government.

In Claude for Government, Claude Code is in early access. To request access for your agency, contact your Anthropic representative.

A fresh install of Claude Code asks the user to sign in with a claude.ai or Claude Console account. To connect it to Claude for Government instead, each device needs a small managed settings file that sends users to your agency's Claude for Government sign-in. Everything else that governs Claude Code is set on the [Config](/docs/government/config/settings) page in this portal and delivered to Claude Code after the user signs in.

This page covers the device side: the managed settings, where to put them on each operating system, how a user signs in, and how to confirm a device is set up. Claude Code built into Claude Desktop (the **Code** tab) is configured through Claude Desktop instead, as [Connect Claude Desktop to Claude for Government](/docs/government/deploy-desktop/configure) describes.

## Before you begin

* **Claude Code is turned on for the organization.** A tenant administrator or organization owner turns on the **Claude Code** switch under [Product availability](/docs/government/config/settings#product-availability) on the **Config** page. It is off by default, and while it is off Claude Code exits right after the user signs in.
* **User accounts exist.** Claude Code signs users in to the same accounts as this portal. Each user needs a [routing rule](/docs/government/tenant-admin/identity-and-access) that covers them and a [seat tier](/docs/government/org-admin/seat-tiers) with at least one model enabled.
* **Claude Code is current.** This setup requires Claude Code 2.1.267 or later (`claude --version`).
* **Claude Desktop is current.** Update Claude Desktop to [the supported version](/docs/government/deploy-desktop/configure#before-you-begin) before turning on Claude Code for the terminal.
* **Devices can reach Claude for Government.** Claude Code must reach the gateway address over HTTPS on port 443, and the user's browser must reach the Claude for Government host, its sign-in service, and your agency's identity provider, the same hosts that [Claude Desktop sign-in](/docs/government/deploy-desktop/configure#before-you-begin) needs.
* **You can place a system-level file or policy.** The settings count only from a system-level location: a file in a system directory, a macOS configuration profile, or a machine-level Windows registry policy. Deliver them through your device management system or by hand with administrator rights.

## The managed settings

Claude Code reads device-level policy from what it calls managed settings. For Claude for Government they contain two keys that turn on gateway sign-in, an `env` block, and one key recommended on devices that also run Claude Desktop.

| Key | Value | Purpose |
| - | - | - |
| `forceLoginMethod` | `"gateway"` | Required. Replaces Claude Code's sign-in choices with a single **Cloud gateway** screen. |
| `forceLoginGatewayUrl` | The Claude for Government gateway address | Required. The address the **Cloud gateway** screen connects to. |
| `env` | The eight variables shown below | Required. Keeps Claude Code's telemetry to Anthropic and its pre-sign-in background connections off from the first launch, and sets its request headers, request body fields, and certificate checking as described below. |
| `parentSettingsBehavior` | `"merge"` | Recommended on devices that also run Claude Desktop, harmless elsewhere: Code sessions inside Claude Desktop then keep Claude Desktop's own restrictions alongside these settings, as [Interaction with Claude Code's own managed settings](/docs/third-party/claude-desktop/code#interaction-with-claude-code%E2%80%99s-own-managed-settings) describes. |

As a `managed-settings.json` file:

```json theme={null}
{
  "forceLoginMethod": "gateway",
  "forceLoginGatewayUrl": "https://<claude-for-government-gateway-address>",
  "env": {
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL": "1",
    "ANTHROPIC_CUSTOM_HEADERS": "",
    "CLAUDE_CODE_EXTRA_BODY": "",
    "NODE_TLS_REJECT_UNAUTHORIZED": "1",
    "NODE_EXTRA_CA_CERTS": ""
  },
  "parentSettingsBehavior": "merge"
}
```

Your Anthropic representative provides the gateway address. Replace `<claude-for-government-gateway-address>` with it so the value is the full address starting with a single `https://`, including any path. The address is the same for every device and contains no credentials, so one file serves your whole fleet.

Claude Code honors the two sign-in keys only from a system-level location and ignores them in a user's own settings or a per-user registry policy.

### Before sign-in

Your organization's settings reach Claude Code only after a user has signed in. Until then, the first four variables keep Claude Code's release-notes download, update checks, automatic setup of the official plugin marketplace, and usage telemetry and error reporting to Anthropic off from the first launch. After sign-in the organization's settings keep them off.

The last four variables are required as shown. `ANTHROPIC_CUSTOM_HEADERS` and `CLAUDE_CODE_EXTRA_BODY` set to empty strings keep extra request headers and extra request body fields off. `NODE_TLS_REJECT_UNAUTHORIZED` set to `"1"` keeps certificate checking on. `NODE_EXTRA_CA_CERTS` names your agency's certificate authority bundle if your devices need one, and is otherwise left empty.

For what each variable controls, see [Environment variables](https://code.claude.com/docs/en/env-vars) in the Claude Code documentation.

### Optional: web proxy settings in the managed settings

If your devices use a web proxy that you manage, add `HTTPS_PROXY` and `HTTP_PROXY` (the proxy's address, for example `http://proxy.example.gov:8080`) and `NO_PROXY` (your bypass list, keeping `localhost`, `127.0.0.1`, and `::1`) to the same `env` block, each under both its uppercase and lowercase name. Claude Code then uses that proxy wherever the device connects from, in place of any other proxy setting on the device. If your devices connect directly, leave these variables out rather than setting them to empty strings, because an empty value switches off a proxy a user would otherwise use. On a device that also runs Claude Desktop, Claude Desktop applies the same proxy values to the sessions it runs, as [Interaction with Claude Code managed settings](/docs/third-party/claude-desktop/network-proxy#interaction-with-claude-code-managed-settings) describes.

## Deploy the settings

Deliver the settings through your device management system wherever you can, and before users start Claude Code for the first time, so that their first launch lands on the **Cloud gateway** screen. Claude Code reads managed settings when it starts; a user who had it open when the settings arrived quits and starts it again. Use one location per device. If a device receives more than one, Claude Code uses the macOS profile or machine-level Windows policy and ignores the file.

### macOS

Place the JSON above at `/Library/Application Support/ClaudeCode/managed-settings.json`, or deploy a configuration profile that sets the same top-level keys in the `com.anthropic.claudecode` managed preferences domain, with `env` as a dictionary of strings.

### Windows

Place the JSON above at `C:\Program Files\ClaudeCode\managed-settings.json`, or deliver it as machine policy: a string (`REG_SZ`) value named `Settings` under `HKLM\SOFTWARE\Policies\ClaudeCode` whose data is the whole JSON document on one line. As a `.reg` file:

```text theme={null}
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\ClaudeCode]
; substitute the Claude for Government gateway address
"Settings"="{\"forceLoginMethod\":\"gateway\",\"forceLoginGatewayUrl\":\"https://<claude-for-government-gateway-address>\",\"env\":{\"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC\":\"1\",\"DISABLE_TELEMETRY\":\"1\",\"DISABLE_ERROR_REPORTING\":\"1\",\"CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL\":\"1\",\"ANTHROPIC_CUSTOM_HEADERS\":\"\",\"CLAUDE_CODE_EXTRA_BODY\":\"\",\"NODE_TLS_REJECT_UNAUTHORIZED\":\"1\",\"NODE_EXTRA_CA_CERTS\":\"\"},\"parentSettingsBehavior\":\"merge\"}"
```

A value under `HKEY_CURRENT_USER` does not turn on gateway sign-in.

### Linux and Windows Subsystem for Linux

On Linux, place the JSON above at `/etc/claude-code/managed-settings.json` (root required).

Claude Code inside Windows Subsystem for Linux (WSL) reads that same path inside each distribution. To manage the setting from Windows instead, add `"wslInheritsWindowsSettings": true` to the machine-level Windows policy or file alongside the keys above; Claude Code inside WSL then reads the Windows settings first and needs no file inside the distribution.

### A single machine set up by hand

To try the setup before a fleet rollout, create the file at the path for the machine's operating system from an administrator account, then start Claude Code as an ordinary user.

## Sign in

With the settings in place, a user's first sign-in on a device goes as follows.

<Steps>
  <Step title="Start Claude Code">
    The user runs `claude` in a terminal. After the first-run theme choice, the **Cloud gateway** screen shows the gateway address, and the user presses **Enter** to connect.
  </Step>

  <Step title="Confirm the gateway certificate">
    The first time each user connects from a device, Claude Code shows the first 16 characters of the gateway's TLS certificate fingerprint (SHA-256) and asks them to trust it. Publish the expected fingerprint to your users with the rollout (they compare it ignoring colons and letter case), and again when Anthropic renews the certificate, because users are asked again after a renewal. Your Anthropic representative provides it.
  </Step>

  <Step title="Finish sign-in in the browser">
    Claude Code opens the Claude for Government sign-in page in the default browser and shows a one-time code in the terminal. The user signs in with your identity provider, checks that the code on the page matches the terminal, and approves.
  </Step>

  <Step title="Return to the terminal">
    If the terminal shows **Signed in to Cloud gateway as** followed by the user's email address, the user confirms with **Yes, continue**. The terminal then shows **Connected to Cloud gateway**, and Claude Code downloads the organization's settings and restarts to apply them. If those settings include items Claude Code asks users to approve, such as a [Telemetry endpoint](/docs/government/config/settings#telemetry-endpoint), it shows a **Managed settings require approval** prompt the first time and whenever those settings change; **No** exits Claude Code. Unattended runs such as `claude -p` apply the settings without prompting.
  </Step>
</Steps>

A sign-in lasts until the organization's [Session idle timeout](/docs/government/config/settings#session-idle-timeout) or [Maximum session length](/docs/government/config/settings#maximum-session-length) is reached, and at most 30 days. It also ends when the user's account is deactivated, or when the user signs in to Claude Code on more devices than Claude for Government allows at once (six), which ends the sign-in closest to expiring (see [Sessions](/docs/government/account/sessions#how-long-sessions-last)). Claude Code then asks the user to sign in again, which they do with `/login`.

## Confirm it worked

Run through these checks on one configured device before the wider rollout.

<Steps>
  <Step title="Check the sign-in screen">
    Start `claude` as a user who has not signed in. The only sign-in option is the **Cloud gateway** screen showing your gateway address. If Claude Code offers claude.ai or Claude Console sign-in instead, the managed settings did not reach it.
  </Step>

  <Step title="Check the background connections are off">
    Before signing in, run `claude doctor`. On the standard installer it reports auto-updates as disabled by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, which shows the `env` block reached Claude Code. (Homebrew, WinGet, and Linux package installs report updates as managed by the package manager instead.)
  </Step>

  <Step title="Check the setting sources">
    After sign-in, run `/status` inside Claude Code. The API provider reads **Cloud gateway** with your gateway address, and **Setting sources** lists **Enterprise managed settings (remote)**.
  </Step>

  <Step title="Check that organization settings arrived">
    Change one visible Claude Code setting on the [Config](/docs/government/config/settings#claude-code) page for a test organization, start a new Claude Code session as a member of it, and confirm the change took effect.
  </Step>
</Steps>

## Troubleshooting

| What you see | Likely cause | What to do |
| - | - | - |
| Claude Code offers claude.ai and Claude Console sign-in instead of the **Cloud gateway** screen | The managed settings did not reach Claude Code: wrong path, a Windows value under `HKEY_CURRENT_USER` or with another name, a misspelled key, or Claude Code was already running | Check the location for the operating system above, then quit and restart Claude Code |
| The **Cloud gateway** screen says to contact your IT administrator | `forceLoginGatewayUrl` is missing or empty | Add the gateway address to the same managed settings and restart Claude Code |
| Claude Code reports that it could not resolve the gateway host, or another connection error for the address shown | The address in `forceLoginGatewayUrl` is not exactly the one your Anthropic representative provided, or the device cannot reach it | Correct the address, or restore the device's route to the gateway over HTTPS on port 443, then restart Claude Code |
| `Unable to connect to Anthropic services` at first start, before any sign-in screen | The sign-in keys did not reach Claude Code from a system-level location, or Claude Code is out of date | Update Claude Code, or check the settings location, then start it again |
| `claude doctor`, run before sign-in on the standard installer, reports auto-updates as enabled | The `env` block did not reach Claude Code | Compare the deployed settings with the sample above, then restart Claude Code |
| When it starts or right after sign-in, Claude Code exits with `Cloud gateway <address> refused managed settings for this account (403): Claude Code may not be enabled for your organization` | The **Claude Code** switch is off at a level that applies to the user (tenant, organization, or directory group) | Turn on the **Claude Code** switch under [Product availability](/docs/government/config/settings#product-availability) at that level (at the tenant level, **Reset to default** instead lets each organization's own switch decide), then have the user start Claude Code again. [**Compare config across levels**](/docs/government/config/overview#comparing-settings-across-levels) on the **Config** page shows which level turns it off for a user |
| When it starts or right after sign-in, Claude Code exits with `Couldn't load settings from Cloud gateway <address>` | Claude Code could not reach the gateway while loading the organization's settings | Confirm the device reaches the gateway over HTTPS on port 443, then have the user start Claude Code again. If it persists on a connected device, contact your Anthropic representative |
| In a session that was working, every request fails with a 403 error saying the product is not available for the organization | The **Claude Code** switch was turned off while Claude Code was running | Turn the switch back on at the level that turned it off; the next request then succeeds |
| Before the user has signed in, Claude Code exits with `Administrator policy requires a Cloud gateway sign-in on this machine` | A credential from earlier use is present: `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` in the environment, an `apiKeyHelper` in the user's settings, or a saved Claude Console key | Remove the variable or the `apiKeyHelper` entry, or have the user run `claude auth logout`, then start `claude` and sign in |
| Claude Code says the gateway's TLS certificate changed and asks the user to run `/login` | The gateway certificate was renewed | Confirm the new fingerprint with your Anthropic representative, send it to users, and have them run `/login` and accept it |

## Things to know

* Only the gateway sign-in described on this page delivers the organization's settings to Claude Code.
* A claude.ai sign-in left on a device from earlier use is ignored once these settings are in place. A leftover `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, or saved Claude Console key is not: until the user has signed in through the gateway, Claude Code stops and asks for its removal, as [Troubleshooting](#troubleshooting) describes.
* Where the Claude Code extension for VS Code is used, have users remove an earlier claude.ai sign-in with `claude auth logout` or the extension's **Claude Code: Logout** command before they sign in through the gateway, not after: both commands clear every credential Claude Code has stored, the gateway sign-in included.
* To take a device out of this setup, have its users sign out with `claude auth logout` before you remove the settings.
* After sign-in, the organization's settings turn off the Claude Code settings that run a helper command (`apiKeyHelper`, `proxyAuthHelper`, `awsAuthRefresh`, `awsCredentialExport`, `gcpAuthRefresh`, `otelHeadersHelper`), wherever it is set. If your devices reach the network through a proxy that needs a helper command to authenticate, raise this with your Anthropic representative before you deploy.
* With these settings Claude Code does not check for or install updates in the background. Distribute new versions through your software deployment tooling, or have users run `claude update` (standard installer) or their package manager.
* Code sessions inside Claude Desktop sign in through Claude Desktop, not through these settings, but on a device that has this file its `env` block applies to them too, and `parentSettingsBehavior` set to `"merge"` keeps Claude Desktop's own restrictions in force alongside it.
