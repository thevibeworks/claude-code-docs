> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Claude Code in the terminal from the Enterprise Admin Console

> Stop deploying managed-settings.json. Apply Enterprise Admin Console settings to Claude Code in the terminal and in VS Code when developers sign in.

The [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) can administer settings for Claude Code in the terminal and in VS Code. Each developer signs in to your organization from Claude Code, and Claude Code applies your settings as managed settings and sends model requests to the provider on your **Connection** page.

You can use this to stop deploying `managed-settings.json`. You move most of those settings into the console and remove the file from developers' computers. Developers then get your settings when they sign in.

## How console settings reach Claude Code

You already manage Claude Desktop from the console. You save your provider on the **Connection** page and the rest of your settings on the other **Desktop 3P** pages. When a person signs in to Claude Desktop, the app follows what you saved.

Claude Code works the same way. A developer signs in to your organization from Claude Code, and Claude Code downloads your console settings. While the developer stays signed in, Claude Code does the following on that computer:

* It sends its model requests to your connection, which is the provider or gateway on your **Connection** page
* It follows your console settings, and the developer's own settings files can't override them

Signing in is each developer's choice. If a developer doesn't sign in, or signs in with other credentials, your settings aren't applied. The console can't require the sign-in. A small managed settings file on the developer's computer can, but that file also stops Claude Desktop from working on that computer. See [Require the sign-in with managed settings](#require-the-sign-in-with-managed-settings).

While a terminal uses your connection, model requests and their content go from the developer's terminal to your provider or gateway. If you set an OpenTelemetry collector, the terminal also sends it telemetry, with the content that you selected. Claude Code contacts Anthropic for the sign-in, for your settings, and for a few other things, such as its own telemetry. For details, see [Where data goes](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#where-data-goes).

## Which settings take priority

Claude Code can get settings from three places, from lowest to highest priority:

1. **The developer's own settings files.**
2. **Your console settings.** They arrive when the developer signs in to your organization.
3. **The computer's managed settings.** These are Claude Code settings that you deploy to the developer's computer: a `managed-settings.json` file, an MDM profile on macOS, or a registry policy on Windows. The configuration profile that you deploy for Claude Desktop doesn't count. A registry policy under `HKCU` doesn't count either. A sign-in replaces that policy's settings, except its retention period (`cleanupPeriodDays`).

Each developer's computer has either:

* **No Claude Code managed settings**: a developer signs in, and your settings apply
* **Claude Code managed settings**: the computer ignores your console completely. Even one setting counts, such as a proxy variable.

To make a computer with managed settings follow your console, do one of these:

* **Remove its Claude Code managed settings**: first move the settings into the console, and then remove all of them. After that, you deploy no Claude Code settings to the computer.
* **Keep them, and name your organization in them**: do this if you need a setting that the console can't set, or if you want to require the sign-in

## Before you start

Ensure that:

* You're an Owner or Primary Owner of the organization
* You saved the **Connection** page under **Organization settings > Desktop 3P**
* Your developers are members of your organization, like your Claude Desktop users
* Your developers have Claude Code 2.1.331 or later, and the same version of the VS Code extension. Earlier versions ignore the console or follow only part of it.
* Developers on Claude Code's [`stable` release channel](https://code.claude.com/docs/en/setup#configure-release-channel) switch to `latest`, unless `stable` has reached that version. `stable` is about a week behind `latest`. Homebrew's `claude-code` cask and the apt, dnf, and apk install commands in Claude Code's docs use `stable`.
* Your developers have access to your provider. The sign-in tells Claude Code where to send requests, but it doesn't give the developer access. With a cloud provider, each developer needs cloud credentials. With a gateway, each developer must be able to sign in to it.
* If you use a **Helper script** on the **Connection** page or an **OTLP headers helper script** on the **Telemetry & updates** page, you [installed it for Claude Code in the terminal](https://claude.com/docs/third-party/claude-desktop/credential-helper.md#install-the-helper-for-claude-code-in-the-terminal). A script that works in Claude Desktop can fail in the terminal.
* The developer's terminal can reach `api.anthropic.com`, `platform.claude.com`, and your OpenTelemetry collector, if you set one
* The developer's browser can reach `claude.com`, `claude.ai`, `platform.claude.com`, `hcaptcha.com`, `*.hcaptcha.com`, and, if your organization uses single sign-on, `sso.claude.com`

Then follow these steps in order:

1. [Review the settings you already saved](#review-the-settings-you-already-saved).
2. If you use a gateway, [prepare your gateway](#prepare-your-gateway).
3. If developers' computers have Claude Code managed settings, [move them into the console](#move-your-managed-settings-into-the-console).
4. [Turn on sign-in from Claude Code](#turn-on-sign-in-from-claude-code), for a pilot group first if you can. If you can't, choose a few developers as your pilot.
5. If developers' computers have Claude Code managed settings, [remove them](#remove-the-managed-settings-from-the-computers) from the pilot developers' computers. If you need to keep some, [keep managed settings beside the console](#keep-managed-settings-beside-the-console) instead.
6. On the same day, [send the pilot developers the sign-in instructions](#send-developers-the-sign-in-instructions).
7. [Check that your settings apply](#check-that-your-settings-apply). Then turn on sign-in for everyone else, repeat step 5 on their computers, and send them the instructions.
8. If you want to, [require the sign-in with a small managed settings file](#require-the-sign-in-with-managed-settings).

## Review the settings you already saved

Claude Code follows some of the fields on the **Desktop 3P** pages. The values that you saved for Claude Desktop also apply in the terminal. Go to **Organization settings > Desktop 3P**, and check that each value also works for developers.

These fields can change what developers can do, or what you collect from them:

* **OTLP endpoint**, on the **Telemetry & updates** page: if you filled this in, terminals also send OpenTelemetry data to your collector. This includes what you selected under **Content capture**, such as prompts and responses. A different collector that the computer's managed settings name [stops getting that data](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#managed-settings-beside-the-console). Claude Code doesn't ask developers first, so [tell them](#send-developers-the-sign-in-instructions). To exclude terminals, add `"env": {"CLAUDE_CODE_ENABLE_TELEMETRY": "0"}` to your [JSON on the **Claude Code** page](#add-claude-code-settings-as-json). This also stops export to a collector that the computer's managed settings name.
* **Allowed egress hosts**, on the **Capabilities** page: if you filled this in, Claude's shell commands run in a sandbox on macOS, Linux, and WSL2. A command that needs a host outside your list, such as a package install, fails. A list that has a `*` entry has no effect in the terminal.
* **Built-in tool policy**, on the **Capabilities** page: if you set an entry to `ask`, Claude Code asks the developer before each call that matches it. In a script that runs `claude -p`, nobody can answer, so Claude Code refuses the call.
* **Allowed plugin MCP servers**, on the **Connectors** page: if you filled this in, Claude Code ignores the MCP servers that developers or their projects set up themselves
* **Block nonessential telemetry**, on the **Telemetry & updates** page: if this is on, Claude Code turns off its automatic updates
* **Model list**, on the **Connection** page: developers can pick only the models on your list
* **Bedrock base URL**, or the same field for another cloud provider, on the **Connection** page: if you filled this in, Claude Code in the terminal uses the provider set on the computer instead of your connection, and it doesn't start without one. In that case, you can't stop deploying managed settings, so [keep them beside the console](#keep-managed-settings-beside-the-console).

For the full list of fields that Claude Code follows, see [Console settings that Claude Code follows](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#console-settings-that-claude-code-follows).

### Add Claude Code settings as JSON

The **Claude Code** page takes JSON in the same format as `managed-settings.json`. Use it for restrictions that have no console field, such as deny rules or a list of blocked models.

Go to **Organization settings > Products > Claude Code**, enter the settings as a JSON object, and click **Save changes**. This example denies reads of the `secrets` folder in the current directory, blocks one model, and turns off workflows:

```json theme={null}
{
  "permissions": {
    "deny": ["Read(./secrets/**)"]
  },
  "deniedModels": ["claude-opus-4-6"],
  "disableWorkflows": true
}
```

Unlike `managed-settings.json`, the JSON takes only [a fixed list of settings](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#settings-that-claude-code-applies), and Claude Code ignores the rest. No setting in the JSON can grant a permission, run a command, sign in, or choose a provider or a model. The console doesn't check the JSON against that list. You see what Claude Code ignored when you [check that your settings apply](#check-that-your-settings-apply).

The JSON doesn't apply to Code sessions in Claude Desktop. Those sessions follow the fields on the **Desktop 3P** pages.

## Prepare your gateway

Skip this section if your **Connection** page uses a direct cloud provider rather than a gateway.

**1. Register the redirect URI**

If developers sign in through your identity provider, add the terminal's redirect URI to the application that you registered there for Claude Desktop's single sign-on. The URI that you registered for Claude Desktop doesn't work for the terminal. Keep both.

* **Microsoft Entra ID**: under **Mobile and desktop applications**, add `http://127.0.0.1/gateway-sign-in/callback`
* **A provider that also matches the port, such as Okta**: add `http://127.0.0.1:53180/gateway-sign-in/callback`, with your **Redirect port** in place of `53180`
* **A Redirect host of `localhost`**: use `localhost` in place of `127.0.0.1`

**2. Check the sign-in flow**

If your sign-in flow is `broker`, Claude Code in the terminal can't use your gateway until you [allow browser sign-in](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#allow-browser-sign-in-where-your-gateway-uses-the-entra-broker). Follow those steps now, but leave the last one, **Turn on both switches**, until you [turn on sign-in from Claude Code](#turn-on-sign-in-from-claude-code).

## Move your managed settings into the console

Skip this section if developers' computers have no Claude Code managed settings.

Move the settings into the console now. You remove them from the computers later, after you turn on sign-in.

### Where each setting goes

Go through your `managed-settings.json`, MDM profile, or registry policy, and put each setting where the console keeps it:

* **Provider, region, project or resource, and custom request headers**: check that the **Connection** page has them
* **`availableModels`**: use the **Model list** on the **Connection** page. Put your default `model` first.
* **The sandbox and the hosts it allows**: use **Allowed egress hosts** on the **Capabilities** page. The sandbox settings in the JSON work only if this field lists hosts, with no `*` entry.
* **Restrictions**: copy them into the [JSON on the **Claude Code** page](#add-claude-code-settings-as-json). Examples are `permissions.deny`, `permissions.ask`, `deniedModels`, `deniedMcpServers`, and `sandbox.filesystem.denyRead`. For the rest, see [Settings that Claude Code applies](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#settings-that-claude-code-applies). The JSON applies to every developer. For settings that differ by team, use a group's policy.
* **`apiKeyHelper`**: use the **Helper script** on the **Connection** page. It takes the path to a program, not a shell command. You still need to [install that program on each computer](https://claude.com/docs/third-party/claude-desktop/credential-helper.md#install-the-helper-for-claude-code-in-the-terminal).
* **OpenTelemetry export (`CLAUDE_CODE_ENABLE_TELEMETRY` and the `OTEL_` variables)**: use **OTLP endpoint** and the other OTLP fields on the **Telemetry & updates** page. If you [keep managed settings beside the console](#keep-managed-settings-beside-the-console), leave these variables in them until each computer has Claude Code 2.1.331. Earlier versions export only where these variables say.

The fields on the **Desktop 3P** pages also apply to Claude Desktop, so check that each value also works in Claude Desktop.

If an entry under `sandbox` or in `disabledMcpjsonServers` starts with `//`, remove one slash, because Claude Code ignores such an entry. Leave `//` in deny and ask rules.

### Settings that the console can't set

Check your managed settings for these before you remove them.

Developers set these themselves from now on:

* **Proxy and certificate variables**: ask developers to set `HTTPS_PROXY` or `NODE_EXTRA_CA_CERTS` in their shell or in their own settings file
* **Cloud credentials in `env`**: each developer needs their own. The **Connection** page can name an AWS profile, a credentials file, or a helper script, but these must already be on the computer.
* **Allow rules (`permissions.allow`), the default permission mode, added directories, `statusLine`, `skillOverrides`, `claudeMdExcludes`, and `autoMemoryEnabled`**: the developer's own settings decide these, even if you keep managed settings

These need managed settings on the computer. If you can't do without one, [keep managed settings beside the console](#keep-managed-settings-beside-the-console):

* **Requiring the sign-in**: a managed settings file applies to every session on the computer. Console settings apply only while the developer is signed in, and a sign-in lasts about a month. Without a file, a developer can sign in to another organization, or not sign in at all. See [Require the sign-in with managed settings](#require-the-sign-in-with-managed-settings).
* **Hooks, and the plugins and MCP servers that you install for developers**: the console can't install them in the terminal
* **`requiredMinimumVersion`, `cleanupPeriodDays`, `allowedProviders`, and the managed `CLAUDE.md` text**: the console has no place for these. Claude Code also ignores anything else that isn't on [the JSON's list](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#settings-that-claude-code-applies).
* **`strictKnownMarketplaces`, `allowManagedPermissionRulesOnly`, `sandbox.filesystem.allowManagedReadPathsOnly`, and Auto mode's deny rules (`autoMode`)**: Claude Code ignores these in the JSON
* **A private address for your provider, such as a VPC endpoint**: your connection overrides it, even if you keep managed settings, so requests go to the provider's default address. To keep it, also fill in **Bedrock base URL**, or the same field for another cloud provider, on the **Connection** page. Claude Code in the terminal then uses the provider set on each computer, not your connection, so each computer must keep managed settings that set your provider and the private address.

After you remove the managed settings from a computer, their rules also stop applying in Code sessions in Claude Desktop, unless a field on the **Desktop 3P** pages sets them.

## Turn on sign-in from Claude Code

Turn on the **Allow sign-in from Claude Code in terminals and IDEs** switch, for a pilot group first if you can:

* **For a pilot group, if your organization has a parent organization**: go to **Organization settings > People > Permission policies**, and open the group's policy. In the **Claude Code** section, turn on the switch, and click **Save changes**.
* **For everyone**: go to **Organization settings > Products > Claude Code**, turn on the switch, and click **Save changes**
* **If your sign-in flow is `broker`**: take the last step of [Allow browser sign-in where your gateway uses the Entra broker](https://claude.com/docs/third-party/claude-desktop/entra-broker.md#allow-browser-sign-in-where-your-gateway-uses-the-entra-broker) instead. It turns on both switches, for a group or for everyone.

The switch is off by default, and it doesn't affect Claude Desktop. While it's off, a developer who tries to sign in sees a message: `You chose an organization that is managed in Anthropic's Enterprise Admin Console`, and Claude Code doesn't save the sign-in. If you turn the switch off later, Claude Code won't start for signed-in developers, and it shows why.

## Remove the managed settings from the computers

Skip this section if developers' computers have no Claude Code managed settings.

Remove the `managed-settings.json` file and any drop-in files, the MDM profile, or the registry policy for Claude Code from the pilot developers' computers. Leave the Claude Desktop configuration profile in place.

* **Remove all of it**: if one setting stays behind, the computer still ignores your console. A developer who signs in there sees a message: `Signed in to the organization` and `The organization's settings won't apply on this computer, because the computer's own managed settings take priority.` Their own Claude login or API key can also stop working, until you finish the removal or they run `claude auth logout`.
* **Send the sign-in instructions straight away**: until a developer signs in, neither the old file nor your console settings apply on that computer

## Send developers the sign-in instructions

Send each developer a message with these items.

* The name of the organization to select in the browser
* How to get credentials for your provider, or how to sign in to your gateway
* How to set a proxy or a certificate, if your managed settings used to set one
* What your OpenTelemetry collector gets from their sessions, if you set one
* The sign-in steps, and what the sign-in changes

You can start from this text:

```text wrap theme={null}
We now manage Claude Code from our admin console. Please sign in on each computer you use.

1. Install or update the claude command to 2.1.331 or later. If the update stops at an earlier version, switch to the latest release channel (https://code.claude.com/docs/en/setup#configure-release-channel). If you use the VS Code extension, update it too.
2. <How to get credentials for our provider. How to set our proxy or certificate, if you need one.>
3. In your terminal, run: claude auth login
4. The browser may ask you to sign in with your email. Select <organization name> and click Authorize. If the browser shows a code, paste it into the terminal.
5. Check that the terminal prints "Signed in to the organization". If it also says that the settings won't apply on this computer, send us that message. If it prints "Login successful." instead, you picked another account, so run the command again.
6. Close any open Claude Code sessions. Then run: claude
7. <If our gateway has its own sign-in:> In Claude Code, run /login and follow the steps.

While you're signed in, every Claude Code session on this computer uses our provider and settings, in any project, in the terminal and in VS Code. Remote Control, cloud sessions, voice mode, and connectors from your claude.ai account aren't available.

<If we set an OpenTelemetry collector:> Claude Code also sends telemetry about your sessions to us. It includes your computer user name and usage figures such as token counts. <If End-user attribution is on:> It also includes your sign-in name or email. <If we capture content:> It also includes your prompts, Claude's responses, and tool inputs and outputs. We choose what it includes. To see where it goes and what it includes, run /status in Claude Code and read the Telemetry row.

The sign-in lasts about a month. When you see "no usable organization sign-in", run claude auth login again.
```

### What developers see at sign-in

Developers may also see these, or ask you about them:

* **Managed settings require approval**: Claude Code asks the developer to approve some of your settings before it uses them, such as your gateway's address. If they decline, Claude Code exits and asks again at the next start.
* **Select login method**: the developer selects **Your organization** if it's listed, and otherwise **Claude account with subscription**. Then they select your organization in the browser again.
* **`Could not load AWS credentials`, or the same for Google Cloud or Azure**: the developer has no working credentials for your cloud provider
* **A gateway that has its own sign-in**: the developer signs in a second time, with `/login` in Claude Code. Until they do, Claude Code refuses each prompt and tells them what to do.
* **How to get their own account back**: the developer runs `claude auth login` and selects their own account. To sign out of everything, they run `claude auth logout`. Developers who use VS Code run these commands in a terminal.

## Check that your settings apply

Ask one developer to start `claude` and run `/status` in Claude Code. Check these rows:

* **Setting sources**: the row includes `Enterprise managed settings (remote)`. That's Claude Code's name for your console settings.
* **API provider**, if you use a cloud provider: the row names your provider and ends with `(chosen by your organization)`
* **Anthropic base URL**, if you use a gateway: the row shows your gateway's address, and no row says that your connection `isn't used`
* **Telemetry**, if you filled in **OTLP endpoint**: the row shows your collector's host with `(set by your organization)` and the content that Claude Code sends
* **Managed settings (remote)**: this row appears only if Claude Code has something to tell you. It gives the cause of any problem, and it names the settings in your JSON that Claude Code ignored.

The console doesn't list the developers who signed in from Claude Code, and the **Desktop usage** page doesn't show sessions in the terminal or in VS Code.

## When setting changes take effect

Claude Code downloads your current settings every time it starts. An open session checks again every hour and applies most changes without a restart. A change to your connection, your **Model list**, or your OpenTelemetry export applies the next time the developer starts Claude Code.

While a developer is signed in, Claude Code doesn't start if it can't reach Anthropic to download your settings.

## When a sign-in ends

A sign-in lasts about a month. When it ends, Claude Code may stop with the message `no usable organization sign-in`. If the developer runs `claude` again without signing in, it can start with their own Claude login or API key. Their requests then go to the Anthropic API, without your settings.

## Remove a developer

When a developer leaves, do these steps in order:

**1. Remove their access to your provider or gateway**

Removing them from the organization doesn't change that access. If they sign in to your gateway through an identity provider, revoke their sessions there.

**2. Ask them to sign out**

The developer runs `claude auth logout` in their terminal. The command signs the developer out and deletes the stored copy of your settings. If they can't run the command, go on to the next step.

**3. Remove them from the organization**

Anthropic then revokes the developer's sign-in, and later sessions don't use your connection. A session that's already open can keep using your connection until the developer exits it.

## Keep managed settings beside the console

Keep the computer's managed settings only if you need something that the console can't set. Add your organization's ID to them as `forceLoginOrgUUID`. The computer then follows your console too, and refuses other organizations.

**1. Check what changes**

While a developer is signed in, your connection replaces the computer's connection, the computer's restrictions apply together with your console's restrictions, and some managed settings stop applying. Read [Managed settings beside the console](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#managed-settings-beside-the-console). Fix the conflicts that it lists, and move the settings that stop applying [into the console](#where-each-setting-goes).

**2. Ask developers to remove their Anthropic API keys**

Claude Code doesn't start a session that has `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` on a computer that sets `forceLoginOrgUUID`. If your managed settings set `apiKeyHelper`, remove it from them too. A gateway on your **Connection** page doesn't need those keys. If a developer needs a key for a different gateway, leave `forceLoginOrgUUID` off that computer.

**3. Add forceLoginOrgUUID**

After you [turn on sign-in from Claude Code](#turn-on-sign-in-from-claude-code), go to **Organization settings > Organization and access**, and copy the **Organization ID**, not the **Parent organization ID**. Add it to the managed settings, and deploy them to the pilot developers' computers first:

```json theme={null}
{
  "forceLoginOrgUUID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

If `forceLoginOrgUUID` already holds another organization's ID, list both: `"forceLoginOrgUUID": ["other-id", "your-id"]`.

## Require the sign-in with managed settings

The console alone can't require the sign-in. The console settings that Claude Code applies at sign-in are a client-side control, not a security boundary. If a developer signs out or never signs in, they can keep using Claude Code with their own provider, Claude login, or API key, and none of your settings apply.

> [!WARNING]
>
> Don't set `enforceAnthropicSignIn` or `requiredMinimumVersion` on a computer that also runs Claude Desktop on your provider.
>
> * **`enforceAnthropicSignIn`**: Claude Code also refuses the sessions that Claude Desktop starts, even when the developer is signed in. This stops Code sessions, Cowork, Chat, and scheduled tasks.
> * **`requiredMinimumVersion`**: Claude Desktop runs its own copy of Claude Code, which updates only with Claude Desktop. While that copy is older than the minimum, none of Claude Desktop's sessions start.
>
> On those computers, deploy `forceLoginOrgUUID` without those keys, and put `"parentSettingsBehavior": "merge"` next to it. The computer then refuses other organizations, but it doesn't require the sign-in. Without `parentSettingsBehavior`, Claude Code ignores the settings that Claude Desktop passes to its sessions, including the sandbox for Code sessions.

To require the sign-in, first turn on sign-in from Claude Code. If you removed your managed settings, you then deploy one small file, the only one that you still deploy. If you kept them, you add the keys to them. These are the keys:

```json theme={null}
{
  "forceLoginOrgUUID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "enforceAnthropicSignIn": true,
  "requiredMinimumVersion": "2.1.331"
}
```

* **`forceLoginOrgUUID`**: makes the computer follow your console and refuse other organizations, as described in [Keep managed settings beside the console](#keep-managed-settings-beside-the-console). By itself, it doesn't require the sign-in. A developer who isn't signed in can still start a session on a cloud provider. Ask developers to remove their Anthropic API keys first, because Claude Code doesn't start a session that has one.
* **`enforceAnthropicSignIn`**: a session on a cloud provider or a gateway starts only if the developer is signed in to your organization. Write `true` without quotation marks, or Claude Code doesn't start.
* **`requiredMinimumVersion`**: blocks earlier versions, including the ones that ignore `enforceAnthropicSignIn`. Developers on Claude Code's [`stable` release channel](https://code.claude.com/docs/en/setup#configure-release-channel) can't start Claude Code until that channel reaches this version. Move them to `latest` before you deploy this key.

If you set a retention period under `HKCU` on Windows, add it to this file as `cleanupPeriodDays`. Claude Code ignores `HKCU` once the computer has managed settings.

To test the requirement, ask a developer who isn't signed in to run `claude`. Claude Code prints a message, `This computer's managed settings require a sign-in to Anthropic`, and exits. If Claude Code starts instead, check that its version is 2.1.331 or later, and that developers' accounts can read the file.

For other ways around your settings, see [Security considerations](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code-reference.md#security-considerations).
