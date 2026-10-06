> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Cowork (local mode) for a HIPAA-ready organization

> Prepare members' computers to run Cowork (local mode) under the HIPAA configuration. Covers the Claude Desktop policy, network limits, and local data.

The HIPAA configuration is an organization setting on Claude Enterprise plans, for organizations that handle protected health information (PHI) and have a [Business Associate Agreement (BAA)](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers) with Anthropic. It applies to Claude Code (local mode) and Cowork (local mode), and it restricts features in both products.

<Note>
  "(local mode)" means a local session, not a session that runs in the cloud. Local sessions run in one of these places:

  * Claude Code in the terminal
  * Claude Code in the Code tab of Claude Desktop
  * Cowork in Claude Desktop

  The Claude Code extensions for VS Code and JetBrains aren't part of (local mode). They keep working with the HIPAA configuration applied, but your BAA doesn't cover them. See the [Implementation Guide](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6\&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide) for the full list of Eligible Services.
</Note>

This page is for the IT or security administrator who manages the macOS and Windows computers where members run [Cowork](/docs/cowork/overview) in Claude Desktop. Other readers start on a different page:

* **The Primary Owner, who applies the HIPAA configuration**: see [Use Claude Code (local mode) and Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731) for what your BAA covers and how to apply the configuration
* **Administrators who prepare computers for Claude Code in the terminal**: see [Set up Claude Code (local mode) for a HIPAA-ready organization](https://code.claude.com/docs/en/hipaa-setup)
* **Administrators of a third-party deployment**: see [Legal and compliance](/docs/third-party/claude-desktop/legal). The HIPAA configuration doesn't apply to [Claude Desktop on third-party platforms](/docs/third-party/claude-desktop/overview)

The table shows when to do each part of the setup:

| When | What to do |
| :- | :- |
| Before the HIPAA configuration is applied | [Prepare computers](#prepare-computers-before-the-hipaa-configuration-is-applied) |
| After the HIPAA configuration is applied | Cowork is off until an Owner turns it back on. [Turn Cowork on and confirm the HIPAA configuration](#confirm-the-hipaa-configuration-in-claude-desktop) |
| Ongoing | [Manage Cowork data on each computer](#manage-cowork-data-on-each-computer) |
| When a member reports an error | [Troubleshoot Cowork on a managed computer](#troubleshoot-cowork-on-a-managed-computer) |

## Prepare computers before the HIPAA configuration is applied

We recommend you start with the tasks in this section and complete them before the Primary Owner applies the HIPAA configuration.

Some tasks need an Owner of your Claude organization, so arrange these requests early:

* **Your organization ID**, for the [Claude Desktop policy](#deploy-the-claude-desktop-policy)
* **The network setting for Cowork**, in [Limit network access for Cowork shell commands](#limit-network-access-for-cowork-shell-commands)
* **Turning Cowork back on** after the configuration is applied, in [Confirm the HIPAA configuration in Claude Desktop](#confirm-the-hipaa-configuration-in-claude-desktop)

### Update Claude Desktop

The HIPAA configuration requires Claude Desktop v2.19675.0 or later. To read the installed version, see [Check your version](https://code.claude.com/docs/en/desktop#check-your-version).

For organizations with the HIPAA configuration, Anthropic's servers reject requests from versions older than the minimum version. Anthropic raises the minimum version over time.

On an older version, members see an **Update required** dialog that tells them to update Claude Desktop. The dialog's text names Code, but members see it in Cowork too. What the dialog offers depends on whether automatic updates are on:

* **Automatic updates are on**: the dialog has an **Update now** button
* **You turned off automatic updates** with the [`disableAutoUpdates`](/docs/third-party/claude-desktop/configuration#disableautoupdates) key: the dialog has no **Update now** button and tells the member to ask their administrator. Deploy each new version with your device management tool

### Allow network access for Claude Desktop

Allow the Anthropic hosts listed in [Desktop network access requirements](https://code.claude.com/docs/en/desktop#network-access-requirements) through your proxy and firewall. Claude Desktop reaches them over HTTPS on port 443. The table shows what Claude Desktop uses three of those hosts for. The setup on this page depends on all three.

| Host | Needed for |
| :- | :- |
| `claude.ai` | Sign-in, the Claude Desktop interface, and your organization's settings |
| `api.anthropic.com` | Claude API requests, update checks, and the status that tells Claude Desktop the HIPAA configuration is on |
| `downloads.claude.ai` | The virtual machine image that Cowork runs shell commands in, the Claude Code binary, and app updates |

### Deploy the Claude Desktop policy

A Claude Desktop policy is a set of settings that your device management tool installs on each computer, as a configuration profile on macOS or as registry values on Windows. You can use one to restrict sign-in to your organization, turn off local MCP servers and desktop extensions, and keep session content out of [Cowork monitoring](/docs/cowork/monitoring) events.

The policy in this section is a sample that we recommend as a starting point. Your organization is responsible for deciding what its own environment needs and for confirming that its configuration meets those needs.

The following sample sets four keys that you could add to the Claude Desktop policy your organization deploys. If your organization doesn't deploy one yet, [Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration) explains how to deliver a policy with your device management tool.

<Tabs>
  <Tab title="macOS">
    Add these keys to a configuration profile for the `com.anthropic.claudefordesktop` preference domain:

    ```xml theme={null}
    <key>forceLoginOrgUUID</key>
    <string>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</string>
    <key>isLocalDevMcpEnabled</key>
    <string>false</string>
    <key>isDesktopExtensionEnabled</key>
    <string>false</string>
    <key>otlpContentCapture</key>
    <string>[]</string>
    ```
  </Tab>

  <Tab title="Windows">
    Write these values under `HKLM\SOFTWARE\Policies\Claude`:

    ```reg theme={null}
    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude]
    "forceLoginOrgUUID"="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    "isLocalDevMcpEnabled"="false"
    "isDesktopExtensionEnabled"="false"
    "otlpContentCapture"="[]"
    ```
  </Tab>
</Tabs>

The sample writes every value as a string, including `false` and `[]`. [Value types](/docs/third-party/claude-desktop/configuration#value-types) lists the other encodings Claude Desktop accepts.

<Note>
  The Claude Desktop policy is separate from Claude Code's managed settings, which [also apply to Cowork](#check-which-claude-code-managed-settings-apply-in-cowork).
</Note>

#### What each Claude Desktop key does

The table shows what to set each key to and what Claude Desktop enforces for it. The key names link to the [configuration reference](/docs/third-party/claude-desktop/configuration), which describes third-party deployments. Some of its keys apply only to third-party deployments, such as `coworkEgressAllowedHosts` and `otlpEndpoint`.

| Key | Value | What Claude Desktop enforces |
| :- | :- | :- |
| `forceLoginOrgUUID` | Your organization ID, which an Owner can copy from [claude.ai admin settings](https://claude.ai/admin-settings/organization) | After a member of your organization signs in, Claude Desktop switches them to your organization. Anyone else sees a page that reads "This account is not approved by your enterprise admin" and can only log out |
| [`isLocalDevMcpEnabled`](/docs/third-party/claude-desktop/configuration#islocaldevmcpenabled) | `false` | Members can't add local MCP servers to chat or Cowork. Local MCP servers that plugins provide stop loading too, including plugins your organization distributes. Claude Desktop also skips the setup that connects it to the Claude in Chrome extension |
| [`isDesktopExtensionEnabled`](/docs/third-party/claude-desktop/configuration#isdesktopextensionenabled) | `false` | Installed desktop extensions stop loading, and members can't install new ones |
| [`otlpContentCapture`](/docs/third-party/claude-desktop/configuration#otlpcontentcapture) | `[]` | Cowork monitoring events carry metadata only |

Cowork monitoring sends events to the OpenTelemetry collector that your organization sets up. When `otlpContentCapture` isn't set, those events can include prompt text, model responses, and tool inputs.

<Warning>
  Check these values before you deploy:

  * **`otlpContentCapture`**: write the two characters `[]`. Claude Desktop reads an empty string as if the key weren't set, and Cowork monitoring events can then include prompt text, model responses, and tool inputs.
  * **`forceLoginOrgUUID`**: if you deploy a value that Claude Desktop can't read as an organization ID, nobody can use the app on that computer. Members see "Sign-in is blocked by this device’s configuration".
</Warning>

#### Confirm the Claude Desktop policy loaded

Claude Desktop applies these keys when it starts, so quit Claude Desktop on a managed computer and open it again first. The table shows how to check each key.

| Key | How to check it |
| :- | :- |
| `isLocalDevMcpEnabled` | Open **Settings** in Claude Desktop. The list of entries has no **Developer** entry |
| `isDesktopExtensionEnabled` | Open **Settings** in Claude Desktop. The list of entries has no **Extensions** entry |
| `forceLoginOrgUUID` | Sign in with an account that isn't in your organization. Claude Desktop shows "This account is not approved by your enterprise admin" |
| `otlpContentCapture` | Run a Cowork task and read the events your [Cowork monitoring](/docs/cowork/monitoring) collector receives. They contain no prompt text, model responses, or tool inputs |

### Check which Claude Code managed settings apply in Cowork

Cowork runs Claude Code on the member's computer, so Claude Code's [managed settings](https://code.claude.com/docs/en/managed-settings) apply to Cowork tasks as well as to the terminal.

To control how long a computer keeps Cowork tasks, set [`cleanupPeriodDays`](#when-claude-desktop-deletes-cowork-tasks). It's a Claude Code managed setting, not a Claude Desktop policy key, so you deliver it through Claude Code's managed settings even if your organization uses only Cowork. [Deploy managed settings](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings) on the Claude Code setup page has a sample that sets it.

Cowork tasks read only the managed settings that are on the computer itself:

* **A `managed-settings.json` file on the computer, or a Claude Code policy from your device management tool**: Cowork tasks read these settings
* **[Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)**: Cowork tasks never receive them. Keep the file or the device management policy on each computer even when an Owner delivers the same keys from claude.ai

`cleanupPeriodDays` works differently, because Claude Desktop reads it and the task doesn't. [When Claude Desktop deletes Cowork tasks](#when-claude-desktop-deletes-cowork-tasks) says which sources Claude Desktop reads.

The table shows what Cowork does with the keys from the Claude Code setup page, and with other Claude Code keys that change how Cowork works.

| Claude Code key | What happens in Cowork |
| :- | :- |
| `cleanupPeriodDays` | With the HIPAA configuration applied, Claude Desktop [deletes inactive Cowork tasks](#when-claude-desktop-deletes-cowork-tasks) after this many days |
| `allowedProviders` | With `anthropic` in the list, Cowork tasks start as usual. Without it, no Cowork task starts |
| `forceLoginMethod`, `forceLoginOrgUUID` | Cowork tasks skip both checks, because Claude Desktop signs the task in. Set `forceLoginOrgUUID` in the [Claude Desktop policy](#deploy-the-claude-desktop-policy) |
| `permissions.deny` | A rule that denies `Bash` with no pattern also stops Claude from running shell commands in Cowork |
| `allowManagedPermissionRulesOnly` | In a Cowork task that asks before edits, Claude can't write to the folders a member connects until you [add allow rules for those folders](https://code.claude.com/docs/en/managed-settings#keep-cowork-folder-access-when-only-managed-rules-apply) |
| `allowManagedMcpServersOnly` with an empty `allowedMcpServers` | The key doesn't apply to connectors or Cowork's built-in tools. MCP servers that plugins provide are blocked |
| `disableSideloadFlags` | Claude Desktop passes no plugins to Cowork tasks |
| `sandbox.enabled` with `sandbox.failIfUnavailable` | On Windows, Cowork tasks fail with [Sandbox required but unavailable](#sandbox-required-but-unavailable) |

Apart from `cleanupPeriodDays`, Claude Code's managed settings stop applying to Cowork if the Claude Desktop policy sets `requireCoworkFullVmSandbox` to `true`. With that key set, Claude Code runs inside Cowork's virtual machine, where it [doesn't read the computer's managed settings](https://code.claude.com/docs/en/managed-settings#where-and-when-a-policy-applies). If you rely on those settings for Cowork, leave the key out of the Claude Desktop policy.

### Limit network access for Cowork shell commands

Cowork runs shell commands in a virtual machine (VM) on the member's computer. An Owner sets which hosts the VM can reach, in your organization's settings.

To restrict which hosts the VM reaches, you can ask an Owner to go to [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities) and turn off the **Allow network egress** toggle under **Code execution**. Turning the toggle off has these effects:

* **Cowork**: the VM reaches only `anthropic.com` and `claude.com` hosts, plus your OpenTelemetry collector if [Cowork monitoring](/docs/cowork/monitoring) is set up
* **Chat**: the toggle also applies to code execution in chat
* **[Web search](#turn-off-web-search-in-cowork) and connectors**: neither goes through the VM, so the toggle doesn't limit them

If Cowork tasks need other hosts, such as a package registry, the Owner turns on the **Allow network egress** toggle and uses these controls:

* **Domain allowlist**: the Owner selects a preset list of domains. With the HIPAA configuration applied, the **All domains** option is unavailable
* **Additional allowed domains**: the Owner adds each domain your organization needs

If **All domains** is still selected when your organization applies the HIPAA configuration, the VM reaches only `anthropic.com` and `claude.com` hosts, plus your OpenTelemetry collector if Cowork monitoring is set up. Entries in **Additional allowed domains** have no effect. To avoid or undo this, ask the Owner to select a different **Domain allowlist** option.

### Turn off web search in Cowork

Web search in Cowork follows your organization's web search setting. Applying the HIPAA configuration doesn't change it. If web search is on and your organization's own policy forbids it, turn it off at one of these levels:

* **For your whole organization, in chat and Cowork**: ask an Owner to go to [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities) and turn off the **Web search** toggle under **Data sources**
* **For Cowork and the Code tab on managed computers**: add the [`disabledBuiltinTools`](/docs/third-party/claude-desktop/configuration#disabledbuiltintools) key to the [Claude Desktop policy](#deploy-the-claude-desktop-policy)

The `disabledBuiltinTools` key takes a list of tool names, written as a string:

<Tabs>
  <Tab title="macOS">
    Add the key to the profile for the `com.anthropic.claudefordesktop` preference domain:

    ```xml theme={null}
    <key>disabledBuiltinTools</key>
    <string>["WebSearch"]</string>
    ```
  </Tab>

  <Tab title="Windows">
    Add the value under `HKLM\SOFTWARE\Policies\Claude`:

    ```reg theme={null}
    "disabledBuiltinTools"="[\"WebSearch\"]"
    ```
  </Tab>
</Tabs>

After a member restarts Claude Desktop, Claude can't search the web in Cowork tasks or Code tab sessions on that computer.

<Warning>
  If you deploy a `disabledBuiltinTools` value that Claude Desktop can't read as a list, Claude Desktop turns off every built-in tool.
</Warning>

## Confirm the HIPAA configuration in Claude Desktop

Run this check on one managed computer after the Primary Owner applies the HIPAA configuration.

<Steps>
  <Step title="Ask an Owner to turn Cowork back on">
    Applying the HIPAA configuration turns Cowork off for your organization. Ask an Owner to go to [**Organization settings > Cowork**](https://claude.ai/admin-settings/cowork) and turn on the **Enable for your organization** toggle.
  </Step>

  <Step title="Restart Claude Desktop">
    Quit Claude Desktop and open it again.
  </Step>

  <Step title="Check the title bar">
    Confirm that the title bar shows a **HIPAA configured** label. On a Mac, open the sidebar to see it.
  </Step>

  <Step title="Check your monitoring events">
    If your organization uses [Cowork monitoring](/docs/cowork/monitoring), run a Cowork task. Confirm that the events your collector receives contain no prompt text, model responses, or tool inputs.
  </Step>
</Steps>

The [HIPAA feature availability table](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers) lists which Cowork features are off with the HIPAA configuration applied, and which ones an Owner can turn back on.

## Manage Cowork data on each computer

Cowork (local mode) stores task data on each member's computer. Securing and deleting that data is your organization's responsibility.

### Where Cowork stores data

Cowork keeps most of its data in the Claude Desktop data folder, which is in a different place on each operating system:

* **macOS**: `~/Library/Application Support/Claude`
* **Windows**: `%APPDATA%\Claude`, or `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude` for the installer downloaded from Anthropic. Check both for a `local-agent-mode-sessions` folder

The table shows what each location holds, and whether Claude Desktop deletes it with the HIPAA configuration applied. It isn't a complete list of the files in the Claude Desktop data folder.

| Location | What it holds | Deleted automatically |
| :- | :- | :- |
| Task folders in `local-agent-mode-sessions`, in the Claude Desktop data folder | One folder per Cowork task, with the task's transcript, uploaded files, and outputs | Yes, [after `cleanupPeriodDays`](#when-claude-desktop-deletes-cowork-tasks), with one exception |
| Everything else in `local-agent-mode-sessions`, in the Claude Desktop data folder | Data that Cowork keeps between tasks, such as memory and plugins | No |
| `vm_bundles`, in the Claude Desktop data folder | The disk images of the virtual machine that runs shell commands | No |
| The Cowork files folder, `~/Claude` by default | Artifacts, scheduled tasks, and project files | No |
| Folders a member connects to a task | The member's own files, including any that Claude created or changed there | No |

On Windows, `~` means `%USERPROFILE%`.

To find a member's Cowork files folder, go to **Settings > Cowork** in Claude Desktop and read the path under **Cowork files**. Members can change the folder, and some computers use `~/Documents/Claude`.

### When Claude Desktop deletes Cowork tasks

You can set `cleanupPeriodDays` in Claude Code's [managed settings](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings) to the number of days your records policy lets a computer keep Cowork tasks. The value must be a whole number of 1 or more. Without a managed value, Claude Desktop uses the value in the member's `~/.claude/settings.json`, or 30 days.

If your organization also uses [server-managed settings](https://code.claude.com/docs/en/server-managed-settings), have an Owner set `cleanupPeriodDays` there too. Claude Desktop reads server-managed settings for this check, and [uses one managed source at a time](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources).

With the HIPAA configuration applied, Claude Desktop deletes Cowork tasks that have been inactive for longer than `cleanupPeriodDays`, including starred and archived ones. Running or opening a task counts as activity. Task folders for background sessions that Dispatch created before your organization applied the HIPAA configuration stay until you delete them.

Claude Desktop checks for tasks to delete after it starts, and every six hours while it stays open. The check needs all of these conditions:

* **Claude Desktop is open**: a computer where nobody opens the app keeps its data
* **The member who owns the tasks is signed in**: after a member signs out, their tasks stay on the computer
* **The member is switched to your organization**: while a member stays switched to another organization, your organization's tasks stay on the computer
* **The computer is online**: an offline computer keeps its data
* **Claude Desktop can read `cleanupPeriodDays`**: if `managed-settings.json` can't be parsed, Claude Desktop skips the check and deletes nothing. The same happens when no managed value is set and the member's settings file can't be parsed or sets an invalid value

### Offboard a member

Removing a member from your organization doesn't delete Cowork data on their computer, and neither does signing out of Claude Desktop. To remove all of it, you can wipe the computer with your device management tool.

## Troubleshoot Cowork on a managed computer

Each entry in this section is headed by the message or symptom a member reports.

### Sandbox required but unavailable

On Windows, Cowork tasks fail with a message that starts "Sandbox required but unavailable" when Claude Code's managed settings set both `sandbox.enabled` and `sandbox.failIfUnavailable` to `true`.

Remove the `sandbox` block from the Claude Code managed settings that your Windows computers use, whether that's a `managed-settings.json` file or a registry policy. Cowork still runs shell commands in its own virtual machine.

### Update required

The computer runs a version of Claude Desktop older than the minimum required for the HIPAA configuration. See [Update Claude Desktop](#update-claude-desktop).

### This account is not approved by your enterprise admin

The member signed in with an account that isn't in the organization that `forceLoginOrgUUID` names. See [What each Claude Desktop key does](#what-each-claude-desktop-key-does).

### Sign-in is blocked by this device’s configuration

Claude Desktop can't read the `forceLoginOrgUUID` value in the Claude Desktop policy. Correct the value, deploy the policy again, and restart Claude Desktop. See [Deploy the Claude Desktop policy](#deploy-the-claude-desktop-policy).

### The HIPAA configured label is missing

Restart Claude Desktop, then open the account menu, which shows the same **HIPAA configured** label. If the label is missing from both places, check these causes in order:

1. **The wrong organization**: confirm in the account menu that the member is signed in with their work account. If the menu lists more than one organization, confirm that your Claude Enterprise organization is selected
2. **The HIPAA configuration isn't applied yet**: ask the Primary Owner to check [**Organization settings > Data and privacy**](https://claude.ai/admin-settings/data-privacy-controls). To find out what that page shows after the configuration is applied, see [Use Claude Code (local mode) and Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731)

### Restrictions remain after a member switches organizations

Restart Claude Desktop. After Claude Desktop has run under the HIPAA configuration, it keeps some restrictions until it restarts, whichever organization the member switches to.

## Related resources

* [Set up Claude Code (local mode) for a HIPAA-ready organization](https://code.claude.com/docs/en/hipaa-setup)
* [Cowork monitoring](/docs/cowork/monitoring)
* [Claude Code managed settings](https://code.claude.com/docs/en/managed-settings)
