> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unified Claude in Claude Desktop on 3P

> Unified Claude combines Chat and Cowork into one experience, with Cowork's agentic capabilities.

Unified Claude combines Chat and Cowork into one experience in Claude Desktop 3P. Users get a single Claude interface for both quick chats and longer agentic tasks. [Code](https://claude.com/docs/third-party/claude-desktop/code.md) stays separate. Unified Claude is [on by default](#enabling-unified-claude) in current versions of Claude Desktop.

## What users see with Unified Claude

With Unified Claude on, users type into the message box on the home screen without first choosing between Chat and Cowork. On a device that can run Cowork, each message sent from the home screen starts a Cowork session. On a device that can't run Cowork's virtual machine, the message starts a Chat conversation instead.

A Cowork session started this way has Cowork-level tools and follows your Cowork settings. For example, Claude can create and change files in folders the user attaches, and create scheduled tasks.

Users keep their earlier chats and Cowork tasks, and the sidebar lists them together.

## Enabling Unified Claude

When a current version of Claude Desktop starts, it reads an unset [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) as `standard`, the value that turns on Unified Claude. The [configuration changelog](https://claude.com/docs/third-party/claude-desktop/configuration-changelog.md) lists the releases that changed this default.

> [!WARNING]
>
> Where your configuration leaves Chat or Cowork on, the default applies even where [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), or [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled) is `false`, so Cowork is on even where you turned it off. Where it leaves only Code on (`coworkTabEnabled` is `false` and `chatTabEnabled` isn't `true`), Claude Desktop 5.1231.0 or later reads an unset `desktopHome` as `off` until December 17, 2026. To keep only Code after that date, set `desktopHome` to `off`.

If you use [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays), set [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays) as well. `coworkSessionRetentionDays` covers new conversations that are Cowork sessions, along with users' other Cowork tasks, as described under [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions).

With Unified Claude on, a device that can run Cowork needs the VM workspace bundle that Cowork uses. A device that doesn't have the bundle downloads it (more than 1 GB) from `downloads.claude.ai` when the user starts their first new conversation. If a proxy or firewall limits downloads on your network, make the changes under [Cowork workspace or Claude CLI fails to download](https://claude.com/docs/third-party/claude-desktop/installation.md#cowork-workspace-or-claude-cli-fails-to-download).

To control Unified Claude, use the setting for your deployment:

* **Enterprise Admin Console**: In **Organization settings**, go to the **Capabilities** page under **Desktop 3P** and find the **Unified Claude** switch under **Allowed surfaces**, as described under [Unified Claude in the admin console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#unified-claude-in-the-admin-console).
* **MDM or a bootstrap server**: The [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) key controls Unified Claude. To turn on Unified Claude in earlier versions of Claude Desktop, set `desktopHome` to `standard` in your [MDM profile](https://claude.com/docs/third-party/claude-desktop/mdm.md) or [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md). Claude Desktop reads a value it doesn't recognize, such as `Standard`, as `off`.

## How Unified Claude interacts with Chat and Cowork settings

Claude Desktop ignores [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), and [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled) when your configuration sets `desktopHome`, whether to `standard` or to `off`. It also ignores them while Unified Claude is on by default.

Your other settings still apply, including [`isClaudeCodeForDesktopEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#isclaudecodefordesktopenabled), which controls Code.

To limit what Claude can do in Cowork, use settings such as [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools), [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy), [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), and [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled). For example, to stop Claude from running shell commands, add `"Bash"` to `disabledBuiltinTools`. That entry applies in Code sessions too, as described under [Sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access).
