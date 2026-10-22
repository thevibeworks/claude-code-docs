> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Models in Claude Desktop

> Switch models in Claude Desktop on Claude for Government, see what the 1M context window does, and find what controls which models you see.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government. The last section is for administrators.

The model picker shows which Claude model answers you and lets you switch to another. It sits at the bottom of the message box in Chat, Cowork, and Code. Which models it lists depends on the [seat tier](/docs/government/account/profile.md) your organization has assigned to you, so a colleague may see a different list.

A model that needs a newer version of Claude Desktop does not appear in the picker until the app is updated. If you are missing a model that a colleague on the same seat tier has, update Claude Desktop, or ask your IT administrator to update it.

## Larger context window

The context window is how much of a conversation Claude can keep in view at once, measured in tokens (a token is a short piece of text, roughly a word or part of one). Some models offer a window of about one million tokens (1M). Such a model appears once in the picker, and new conversations, tasks, and Code sessions on it use the 1M window.

> [!NOTE]
>
> Before Claude Desktop 2.31226.0, such a model appears twice. To be sure of the larger window, check that the entry marked **1M context window**, or **1M** in Code, is selected when you start new work.

When a long conversation or task gets close to filling the context window, Claude summarizes the earlier part to make room and carries on from the summary, which the app calls compacting. With a 1M window this happens much later than with a window of about 200,000 tokens (200K), so long pieces of work keep their full detail for longer. Past the point where a 200K window would compact, each further message carries the whole conversation rather than a summary, so it uses more of your [allowance](/docs/government/account/usage.md) and responses can take longer to start.

## Model availability for administrators

The models a member sees come from the **Allowed models** of their [seat tier](/docs/government/org-admin/seat-tiers.md). Whether a model offers the [1M context window](#larger-context-window) is set by Anthropic for each model rather than in the admin portal. When you change a tier's allowed models, access changes straight away, and the member's model picker shows the change the next time they start Claude Desktop.

A long conversation at the 1M window uses more of the spend limits, because each message carries more of the conversation.
