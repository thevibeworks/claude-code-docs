> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Claude Code to Claude for Government

> Connect the Claude Code command-line tool to Claude for Government with managed settings on macOS, Windows, and Linux, and confirm a device is set up.

> **Who this is for:** IT administrators who install the Claude Code command-line tool on agency devices and connect it to Claude for Government.

In Claude for Government, Claude Code is in early access. To request access for your agency, contact your Anthropic representative.

Each device needs managed settings that send users to your agency's Claude for Government sign-in. The organization's Claude Code settings are set on the [Config](https://claude.com/docs/government/config/settings.md) page.

> [!NOTE]
>
> Claude Code in Claude Desktop's **Code** tab signs in through Claude Desktop and is turned on by the [**Code in Claude Desktop**](https://claude.com/docs/government/config/settings.md#code-in-claude-desktop) switch, not the **Claude Code** switch; see [Connect Claude Desktop to Claude for Government](https://claude.com/docs/government/deploy-desktop/configure.md). The `env` block of these managed settings still applies to Code tab sessions. For the other settings that govern them on a device that also has these managed settings, see [Code in Claude Desktop](https://claude.com/docs/government/security/security-and-data-handling.md#code-in-claude-desktop).

## Before you begin

* **Claude Code is turned on for the organization.** A tenant administrator or organization owner turns on the **Claude Code** switch under [Product availability](https://claude.com/docs/government/config/settings.md#product-availability) on the **Config** page. It is off by default, and while it is off, Claude Code exits right after the user signs in.
* **User accounts exist.** Claude Code signs users in to the same accounts as this portal. Each user needs a [routing rule](https://claude.com/docs/government/tenant-admin/identity-and-access.md) that covers them and a [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md) with at least one model enabled.
* **Claude Code is current.** This setup requires Claude Code 2.1.308 or later (`claude --version` in a terminal).
* **Devices can reach Claude for Government.** Claude Code must reach the gateway address over HTTPS on port 443, and the user's browser must reach the same sign-in hosts that [Claude Desktop needs](https://claude.com/docs/government/deploy-desktop/configure.md#network-access).
* **You can place a system-level file or policy.** The settings are enforced only from a system file, a macOS configuration profile, or a machine-level Windows policy, and values for the same keys in a user's own settings cannot override them.

## The managed settings

For Claude for Government, Claude Code's [managed settings](https://code.claude.com/docs/en/managed-settings) contain these keys, shown as a `managed-settings.json` file:

```json theme={null}
{
  "forceLoginMethod": "gateway",
  "forceLoginGatewayUrl": "https://<claude-for-government-host>/gateway-api",
  "env": {
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL": "1",
    "ANTHROPIC_CUSTOM_HEADERS": "",
    "CLAUDE_CODE_EXTRA_BODY": "",
    "CLAUDE_CODE_EXTRA_METADATA": "",
    "NODE_TLS_REJECT_UNAUTHORIZED": "1",
    "NODE_EXTRA_CA_CERTS": ""
  },
  "parentSettingsBehavior": "merge"
}
```

* **`forceLoginMethod`** (required): replaces Claude Code's sign-in choices with a single **Cloud gateway** screen.
* **`forceLoginGatewayUrl`** (required): the Claude for Government gateway address that the **Cloud gateway** screen connects to. If your agency reaches Claude for Government on a hostname of its own, ask your Anthropic representative which address to use. Otherwise, replace `<claude-for-government-host>` with the domain name you use to access Claude for Government, the host in your Claude Desktop [`bootstrapUrl`](https://claude.com/docs/government/deploy-desktop/configure#the-managed-setting). The address contains no credentials.
* **`env`** (required): holds the variables that [Before sign-in](#before-sign-in) describes.
* **`parentSettingsBehavior`** (devices that also run Claude Desktop): where these managed settings govern Claude Desktop's sessions, `"merge"` layers the policy that Claude Desktop supplies, Code's sandbox included, under them. Without it, Claude Code [can ignore that policy](https://claude.com/docs/third-party/claude-desktop/code.md#interaction-with-claude-code%E2%80%99s-own-managed-settings).

### Before sign-in

Your organization's settings reach Claude Code only after a user has signed in. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, and `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` together keep Claude Code's release-notes download, update checks, automatic setup of the official plugin marketplace, and usage telemetry and error reporting to Anthropic off from the first launch. They stay off after sign-in.

Every variable in the sample is required. `ANTHROPIC_CUSTOM_HEADERS`, `CLAUDE_CODE_EXTRA_BODY`, and `CLAUDE_CODE_EXTRA_METADATA` must be empty strings, so a user's or a repository's settings file can't change them. `NODE_TLS_REJECT_UNAUTHORIZED` must be `"1"`, which keeps certificate checking on. `NODE_EXTRA_CA_CERTS` is the path to your agency's certificate authority bundle if your devices need one, as [TLS inspection can require](https://code.claude.com/docs/en/network-config#ca-certificate-store), and is otherwise empty.

For Claude Code's other environment variables, see [Environment variables](https://code.claude.com/docs/en/env-vars) in the Claude Code documentation.

### Web proxy settings

If your devices use a web proxy that you manage, add `HTTPS_PROXY` and `HTTP_PROXY` (the proxy's address, for example `http://proxy.example.corp:8080`) and `NO_PROXY` (your bypass list, keeping `localhost`, `127.0.0.1`, and `::1`) to the same `env` block, each under both its uppercase and lowercase name. Claude Code then uses that proxy wherever the device connects from, in place of any other proxy setting on the device. If your devices connect directly, leave these variables out rather than setting them to empty strings, because an empty value switches off a proxy a user would otherwise use.

## Deploy the settings

Deliver the settings through your device management system wherever you can, and before users start Claude Code for the first time, so that their first launch opens the **Cloud gateway** screen. Use one location for each device. Claude Desktop runs Chat, Cowork, and Code through its own Claude Code, which reads these settings, including [proxy values](https://claude.com/docs/third-party/claude-desktop/network-proxy.md#interaction-with-claude-code-managed-settings) and any [`requiredMaximumVersion`](https://claude.com/docs/government/deploy-desktop/configure#claude-code-maximum-version). For how they combine with your organization's settings, see [Code in Claude Desktop](https://claude.com/docs/government/security/security-and-data-handling.md#code-in-claude-desktop).

### macOS

Place the managed settings file at `/Library/Application Support/ClaudeCode/managed-settings.json`, or deploy a configuration profile that sets the same top-level keys in the `com.anthropic.claudecode` managed preferences domain, with `env` as a dictionary of strings.

### Windows

Place the managed settings file at `C:\Program Files\ClaudeCode\managed-settings.json`, or deliver it as machine policy: a `REG_SZ` value named `Settings` under `HKLM\SOFTWARE\Policies\ClaudeCode` holding the whole JSON document, as in this `.reg` file:

```text theme={null}
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\ClaudeCode]
; substitute your gateway address from "The managed settings"
"Settings"="{\"forceLoginMethod\":\"gateway\",\"forceLoginGatewayUrl\":\"https://<claude-for-government-host>/gateway-api\",\"env\":{\"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC\":\"1\",\"DISABLE_TELEMETRY\":\"1\",\"DISABLE_ERROR_REPORTING\":\"1\",\"CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL\":\"1\",\"ANTHROPIC_CUSTOM_HEADERS\":\"\",\"CLAUDE_CODE_EXTRA_BODY\":\"\",\"CLAUDE_CODE_EXTRA_METADATA\":\"\",\"NODE_TLS_REJECT_UNAUTHORIZED\":\"1\",\"NODE_EXTRA_CA_CERTS\":\"\"},\"parentSettingsBehavior\":\"merge\"}"
```

A value under `HKEY_CURRENT_USER` does not turn on gateway sign-in.

### Linux and Windows Subsystem for Linux

On Linux, place the managed settings file at `/etc/claude-code/managed-settings.json` (root required).

Claude Code inside Windows Subsystem for Linux (WSL) reads that same path inside each distribution. To manage the settings from Windows instead, add `"wslInheritsWindowsSettings": true` to the machine-level Windows policy or file alongside the other keys. Claude Code inside WSL then reads the Windows settings first and needs no file inside the distribution.

## Sign in

Before a user's first gateway sign-in, have them remove any earlier claude.ai sign-in with `claude auth logout` in a terminal, or VS Code's **Claude Code: Logout** command. Signing out later also removes the gateway sign-in. VS Code extension users who sign in through the gateway in a terminal need the standalone command-line tool. The copy of Claude Code that the extension runs follows these managed settings and must also meet the [minimum version](#before-you-begin). The version of the copy it bundles is the extension's version number in VS Code's **Extensions** view.

A user who has used Claude Code on the device before starts the same sign-in with `/login` at the Claude Code prompt. With the settings in place, a first sign-in goes as follows.

**1. Start Claude Code**

The user runs `claude` in a terminal. The **Cloud gateway** screen shows the gateway address, and the user presses **Enter** to connect.

**2. Confirm the gateway certificate**

The first time each user connects from a device, Claude Code shows the first 16 characters of the gateway's TLS certificate fingerprint (SHA-256) and asks them to trust it. Publish the expected fingerprint to your users with the rollout (they compare it ignoring colons and letter case), and again when the certificate is renewed. Your Anthropic representative provides it. If your network inspects TLS connections to the gateway, users behind the inspection see the fingerprint of the certificate it presents for the gateway's host. Get that fingerprint from the team that runs the inspection and publish it too. Each time the certificate a device sees changes, its user confirms the new fingerprint and signs in again.

**3. Finish sign-in in the browser**

Claude Code opens the Claude for Government sign-in page in the default browser and shows a one-time code in the terminal. The user signs in with your identity provider, checks that the code on the page matches the terminal, and approves.

**4. Return to the terminal**

If the terminal shows **Signed in to Cloud gateway as** followed by the user's email address, the user confirms with **Yes, continue**. The terminal then shows **Connected to Cloud gateway**, and Claude Code downloads the organization's settings and restarts to apply them. If those settings include items Claude Code asks users to approve, such as a [Telemetry endpoint](https://claude.com/docs/government/config/settings.md#telemetry-endpoint), it shows a **Managed settings require approval** prompt the first time and whenever those settings change; **No** exits Claude Code. Unattended runs such as `claude -p` apply the settings without prompting.

A sign-in lasts until the organization's [Session idle timeout](https://claude.com/docs/government/config/settings.md#session-idle-timeout) or [Maximum session length](https://claude.com/docs/government/config/settings.md#maximum-session-length) is reached, and at most 30 days. It also ends when the user's account is deactivated or an administrator signs the user out. A new Claude Code sign-in by the same user while six are active ends the one closest to expiring (see [Sessions](https://claude.com/docs/government/account/sessions.md#how-long-sessions-last)). Claude Code then asks the user to sign in again, which they do with `/login` at the Claude Code prompt.

## Confirm it worked

Before the wider rollout, place the managed settings on one device, at the [location for the operating system](#deploy-the-settings), from an administrator account, then run these checks as an ordinary user.

**1. Check the sign-in screen**

Start `claude` in a terminal as a user who has not signed in, running `/login` at the Claude Code prompt if they have used Claude Code on the device before. The only sign-in option is the **Cloud gateway** screen showing your gateway address.

**2. Check that the env block arrived**

Before signing in, run `claude doctor` in a terminal. On the standard installer or an npm install it reports auto-updates as disabled by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, which shows the `env` block reached Claude Code. (Homebrew, WinGet, and Linux package installs report updates as managed by the package manager instead.)

**3. Check the setting sources**

After sign-in, run `/status` inside Claude Code. **API provider** reads **Cloud gateway**, **Gateway URL** shows your gateway address, and **Setting sources** lists **Enterprise managed settings (remote)**.

**4. Check that organization settings arrived**

Change one visible setting under [Claude Code](https://claude.com/docs/government/config/settings.md#claude-code) on the **Config** page for a test organization, start a new Claude Code session as a member of it, and confirm the change took effect.

## Troubleshooting

| What you see | Likely cause | What to do |
| - | - | - |
| Claude Code offers claude.ai and Claude Console sign-in instead of the **Cloud gateway** screen | The managed settings did not reach Claude Code: wrong path, a Windows value under `HKEY_CURRENT_USER` or with another name, a misspelled key, or Claude Code was already running | Check the [location for the operating system](#deploy-the-settings), then exit and restart Claude Code |
| The **Cloud gateway** screen says `Gateway login is required by your organization's policy` | `forceLoginGatewayUrl` is missing or empty | Add the gateway address to the same managed settings and restart Claude Code |
| At sign-in, Claude Code shows `Login Error: Hostname/IP does not match certificate's altnames` | The proxy's address starts with `https://` and Claude Code is older than 2.1.307 | Update Claude Code, then have the user sign in again |
| Sign-in ends with `Could not verify the gateway's TLS certificate` | Claude Code doesn't trust the certificate's issuer, such as your TLS inspection | Add the issuer's root certificate to the device's [certificate store](https://code.claude.com/docs/en/network-config#ca-certificate-store), or to a bundle that [`NODE_EXTRA_CA_CERTS`](#before-sign-in) names in these managed settings, not where the message says, then restart Claude Code |
| Claude Code reports `Could not resolve gateway host`, or another connection error for the address shown | The address in `forceLoginGatewayUrl` is not the [gateway address](#the-managed-settings), or the device cannot reach it | Correct the address, or restore the device's route to the gateway over HTTPS on port 443, then restart Claude Code |
| `Unable to connect to Anthropic services` at first start, before any sign-in screen | `forceLoginMethod` and `forceLoginGatewayUrl` did not reach Claude Code from a system-level location | Check the [location for the operating system](#deploy-the-settings), then start Claude Code again |
| `claude doctor`, run before sign-in on the standard installer or an npm install, reports auto-updates as enabled | The `env` block did not reach Claude Code | Compare the deployed settings with the [sample managed settings](#the-managed-settings), then restart Claude Code |
| When it starts or right after sign-in, Claude Code exits with `Cloud gateway <address> refused managed settings for this account (403): Claude Code may not be enabled for your organization` | The **Claude Code** switch is off at a level that applies to the user (tenant, organization, or directory group) | Turn on the **Claude Code** switch under [Product availability](https://claude.com/docs/government/config/settings.md#product-availability) at that level (at the tenant level, **Reset to default** instead lets each organization's own switch decide), then have the user start Claude Code again. [**Compare config across levels**](https://claude.com/docs/government/config/overview.md#comparing-settings-across-levels) on the **Config** page shows which level turns it off |
| When it starts or right after sign-in, Claude Code exits with `Couldn't load settings from Cloud gateway <address>` | Claude Code could not reach the gateway, or could not apply the settings it sent (the rest of the message says which) | If the message says to check the network connection, confirm the device reaches the gateway over HTTPS on port 443, then have the user start Claude Code again. Otherwise, or if it persists, contact your Anthropic representative |
| In a session that was working, every request fails with a 403 error that says `Claude Code is not turned on for your organization` | The **Claude Code** switch was turned off while Claude Code was running | Turn the switch back on at the level that turned it off; the next request then succeeds |
| Before the user has signed in, Claude Code exits with `Administrator policy requires a Cloud gateway sign-in on this machine` | A credential from earlier use is present: `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` in the environment, an `apiKeyHelper` in the user's settings, or a saved Claude Console key | Remove the variable or the `apiKeyHelper` entry, or have the user run `claude auth logout` in a terminal, then start `claude` and sign in |
| Claude Code says `TLS certificate changed since you connected` and asks the user to run `/login` | The gateway certificate was renewed, or your TLS inspection presents a different one | Confirm the new fingerprint with your Anthropic representative, or with the team that runs the inspection, send it to users, and have them run `/login` at the Claude Code prompt, accept it, and sign in again |
| Sign-in ends with `The gateway's TLS certificate changed during sign-in` | Your TLS inspection presented a different certificate later in the same sign-in | Have every inspecting appliance present the same certificate for the gateway's host on every connection, then have the user sign in again |

## Things to know

* Only a gateway sign-in delivers the organization's settings to the Claude Code command-line tool, which fetches them before each start and hourly while it runs. After a user signs in, the organization's settings replace the Claude Code policy in these managed settings, including hooks and permission rules. From these managed settings, Claude Code still reads the sign-in keys (`forceLoginMethod` and `forceLoginGatewayUrl`), any `env` variables the organization's settings leave unset, and the [keys Claude Code reads from every admin source](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source).
* A cloud provider selected earlier in a user's environment or Claude Code settings, such as Amazon Bedrock, still applies whenever Claude Code has no gateway sign-in for the user, for example before the first sign-in or after one expires. Claude Code then uses that provider instead of requiring the gateway sign-in. Remove that provider selection from devices you set up for Claude for Government.
* After sign-in, the organization's settings turn off these six Claude Code settings wherever they are set: `apiKeyHelper`, `proxyAuthHelper`, `awsAuthRefresh`, `awsCredentialExport`, `gcpAuthRefresh`, and `otelHeadersHelper`. If your proxy needs `proxyAuthHelper`, raise it with your Anthropic representative before you deploy.
* To take a device out of this setup, have its users sign out with `claude auth logout` in a terminal, then remove the managed settings.
* With Claude for Government, the command-line tool has no access to Claude Code features that [require a claude.ai account](https://code.claude.com/docs/en/feature-availability#features-that-require-a-claude-subscription), such as cloud sessions, Remote Control, and cloud scheduled tasks. [Fast mode](https://code.claude.com/docs/en/fast-mode) isn't available either.
* Because these settings turn off background updates, distribute new versions through your software deployment tooling, or have users run `claude update` in a terminal (standard installer) or their package manager.
