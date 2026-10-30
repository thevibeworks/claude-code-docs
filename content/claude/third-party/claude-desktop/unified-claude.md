> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unified Claude in Claude Desktop on 3P

> Unified Claude combines Chat and Cowork into one experience, with Cowork's agentic capabilities.

> [!NOTE]
>
> Unified Claude is in beta. It is opt-in until November 10, 2026. From that date, Unified Claude is [on by default](#enabling-unified-claude). Cowork is then on too, even where you turned Cowork off. New [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) organizations start with Unified Claude on.

Unified Claude combines Chat and Cowork into one experience in Claude Desktop 3P. Users get a single Claude interface for both quick chats and longer agentic tasks. [Code](https://claude.com/docs/third-party/claude-desktop/code.md) stays separate.

Unified Claude contains the same capabilities as Cowork on Desktop 3P today, including bash execution, subagents, and scheduled tasks. The Chat experience is going away, but you can restrict specific Cowork capabilities in Unified Claude through your other settings options and tool policies.

Unified Claude runs without Cowork capabilities if the user's machine cannot launch the VM. If so, the application will revert to non-VM capabilities under Unified Claude.

## What users see with Unified Claude

With Unified Claude on, users type into the message box on the home screen without first choosing between Chat and Cowork. On a device that can run Cowork, each message sent from the home screen starts a Cowork session. On a device that can't run Cowork's virtual machine, the message starts a Chat conversation instead.

A Cowork session started this way has Cowork-level tools and follows your Cowork settings. For example, Claude can create and change files in folders the user attaches, and create scheduled tasks.

Users keep their earlier chats and Cowork tasks, and the sidebar lists them together.

## Enabling Unified Claude

Unified Claude is opt-in until November 10, 2026. When a current version of Claude Desktop starts after 12:00 PM Pacific Time on that date, it reads an unset [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) as `standard`, the value that turns on Unified Claude. Unified Claude is then on by default.

> [!WARNING]
>
> The default applies even where [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), or [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled) is `false`. Cowork is on even where you turned it off.

If you use [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays), set [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays) as well, before November 10, 2026, or earlier if you turn on Unified Claude yourself. `coworkSessionRetentionDays` covers new conversations that are Cowork sessions, along with users' other Cowork tasks, as described under [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions).

To turn on Unified Claude yourself, use the setting for your deployment:

* **Enterprise Admin Console**: Go to Capabilities and toggle on "Opt into the new Chat and Cowork unified view."
* **MDM or a bootstrap server**: For MDM and bootstrap deployments, the [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) key controls Unified Claude. Create and set `desktopHome` to `standard` in your [MDM profile](https://claude.com/docs/third-party/claude-desktop/mdm.md) or [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md). Claude Desktop reads a value it doesn't recognize as `off`. Until November 10, 2026, removing the key turns Unified Claude off.

## How Unified Claude interacts with Chat and Cowork settings

Claude Desktop ignores [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), and [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled) when your configuration sets `desktopHome`, whether to `standard` or to `off`. It also ignores them while Unified Claude is on by default. New conversations that are Cowork sessions follow the Cowork retention period. The Chat retention period still covers Chat conversations, such as earlier chats.

Your other settings still apply, including [`isClaudeCodeForDesktopEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#isclaudecodefordesktopenabled), which controls Code.

To limit what Claude can do in Cowork, use settings such as [`disabledBuiltinTools`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledbuiltintools), [`builtinToolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#builtintoolpolicy), [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), and [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled). For example, to stop Claude from running shell commands, add `"Bash"` to `disabledBuiltinTools`. That entry applies in Code sessions too, as described under [Sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access).
