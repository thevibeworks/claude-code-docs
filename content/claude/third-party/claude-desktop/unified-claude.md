> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unified Claude in Claude Desktop on 3P

> Unified Claude combines Chat and Cowork into one experience, with Cowork's agentic capabilities.

> [!NOTE]
>
> Unified Claude is in beta. It is opt-in until November 10, 2026. From that date, unless an [exception](#enabling-unified-claude) applies, it is on by default. New [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md) organizations start with Unified Claude on.

Unified Claude combines Chat and Cowork into one experience in Claude Desktop 3P. Users get a single Claude interface for both quick chats and longer agentic tasks. [Code](https://claude.com/docs/third-party/claude-desktop/code.md) stays separate.

Where Cowork is on, Unified Claude contains the same capabilities as Cowork on Desktop 3P today, including bash execution, subagents, and scheduled tasks. The Chat experience is going away, but you can restrict specific Cowork capabilities in Unified Claude through your other settings options and tool policies.

Unified Claude runs without Cowork capabilities if the user's machine cannot launch the VM. If so, the application will revert to non-VM capabilities under Unified Claude.

## What users see with Unified Claude

With Unified Claude on, users type into the message box on the home screen without first choosing between Chat and Cowork. Where Cowork is on and the device can run it, each message sent from the home screen starts a Cowork session. Otherwise, the message starts a Chat conversation instead.

A Cowork session started this way has Cowork-level tools and follows your Cowork settings. For example, Claude can create and change files in folders the user attaches, and create scheduled tasks.

Users keep their earlier chats and Cowork tasks, and the sidebar lists them together.

## Enabling Unified Claude

Unified Claude is opt-in until November 10, 2026. When Claude Desktop starts after 12:00 PM Pacific Time on that date, Unified Claude is on by default where [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) is unset, except in these cases:

* **A Chat retention period that differs from Cowork's**: where Cowork is on, [`chatSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#chatsessionretentiondays) is set, and [`coworkSessionRetentionDays`](https://claude.com/docs/third-party/claude-desktop/configuration#coworksessionretentiondays) isn't set to the same number of days, Unified Claude is off until the two match or you set `desktopHome`. A later change that creates this mismatch turns Unified Claude off again.
* **Chat, Cowork, and Code all off**: Claude Desktop keeps turning one of them back on, as described under [Chat configuration](https://claude.com/docs/third-party/claude-desktop/chat.md#configuration)
* **Earlier app versions**: the default comes with an app update, so a device switches only after it installs that update

What users get by default follows [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled):

* **Cowork on**: where the key isn't `false`, Claude Desktop reads `desktopHome` as `standard`. Chat and advanced file analysis come on with Cowork, even where [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled) or [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled) is `false`. To turn off sandbox commands, see [Sandbox network access](https://claude.com/docs/third-party/claude-desktop/chat.md#sandbox-network-access).
* **Cowork off**: where the key is `false`, Cowork stays off, and Chat and advanced file analysis stay as `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` set them. With Chat off as well, nothing changes, and users keep Code alone.

To turn on Unified Claude yourself, use the setting for your deployment:

* **Enterprise Admin Console**: Go to Capabilities and toggle on "Opt into the new Chat and Cowork unified view."
* **MDM or a bootstrap server**: For MDM and bootstrap deployments, the [`desktopHome`](https://claude.com/docs/third-party/claude-desktop/configuration#desktophome) key controls Unified Claude. Create and set `desktopHome` to `standard` in your [MDM profile](https://claude.com/docs/third-party/claude-desktop/mdm.md) or [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md). Claude Desktop reads a value it doesn't recognize as `off`. Where the default doesn't apply, removing the key turns Unified Claude off.

If you use `chatSessionRetentionDays`, set `coworkSessionRetentionDays` as well before you turn on Unified Claude. `coworkSessionRetentionDays` covers new conversations that are Cowork sessions, along with users' other Cowork tasks, as described under [Automatic deletion of idle sessions](https://claude.com/docs/third-party/claude-desktop/data-storage.md#automatic-deletion-of-idle-sessions).

## How Unified Claude interacts with Chat and Cowork settings

When your configuration sets `desktopHome`, Claude Desktop ignores [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled), [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled), and [`coworkTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#coworktabenabled). New conversations that are Cowork sessions follow the Cowork retention period. The Chat retention period still covers Chat conversations, such as earlier chats.

Your other settings still apply, including [`isClaudeCodeForDesktopEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#isclaudecodefordesktopenabled), which controls Code.
