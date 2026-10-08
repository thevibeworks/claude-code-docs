> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unified Claude in Claude Desktop on 3P

> Unified Claude combines Chat and Cowork into one experience, with Cowork's agentic capabilities.

<Note>
  Unified Claude is in beta. It is opt-in until November 10, when it becomes enforced for all Desktop 3P deployments. New [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console) organizations start with Unified Claude on.
</Note>

Unified Claude combines Chat and Cowork into one experience in Claude Desktop 3P. Users get a single Claude interface for both quick chats and longer agentic tasks. [Code](/docs/third-party/claude-desktop/code) stays separate.

Unified Claude contains the same capabilities as Cowork on Desktop 3P today, including bash execution, subagents, and scheduled tasks. The Chat experience is going away, but you can restrict specific Cowork capabilities in Unified Claude through your other settings options and tool policies.

The only time Unified Claude runs without Cowork capabilities is if the user's machine cannot launch the VM. If so, the application will revert to non-VM capabilities under Unified Claude.

## What users see with Unified Claude

With Unified Claude on, users type into the message box on the home screen without first choosing between Chat and Cowork. On a device that can run Cowork, each message sent from the home screen starts a Cowork session. On a device that can't run Cowork, the message starts a Chat conversation instead.

A Claude session started this way has Cowork-level tools and follows your Cowork settings. For example, Claude can create and change files in folders the user attaches, and create scheduled tasks.

Users keep their earlier chats and Cowork tasks, and the sidebar lists them together.

## Enabling Unified Claude

Unified Claude is opt-in today. To enable it, follow the instructions below:

* **Enterprise Admin Console**: Go to Capabilities and toggle on "Opt into the new Chat and Cowork unified view."
* **MDM or a bootstrap server**: For MDM and bootstrap deployments, the [`desktopHome`](/docs/third-party/claude-desktop/configuration#desktophome) key controls Unified Claude. Create and set `desktopHome` to `standard` in your [MDM profile](/docs/third-party/claude-desktop/mdm) or [bootstrap response](/docs/third-party/claude-desktop/bootstrap). Claude Desktop reads a value it doesn't recognize as `off`. Remove the key to disable the Unified Claude experience.

## How Unified Claude interacts with Chat and Cowork settings

When Unified Claude is enabled, Claude Desktop ignores [`chatTabEnabled`](/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), and [`coworkTabEnabled`](/docs/third-party/claude-desktop/configuration#coworktabenabled). New conversations follow the Cowork retention period. The Chat retention period still covers Chat conversations, such as earlier chats.

Your other settings still apply while `desktopHome` has a value, including [`isClaudeCodeForDesktopEnabled`](/docs/third-party/claude-desktop/configuration#isclaudecodefordesktopenabled), which controls Code.
