> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Models in Claude Desktop

> How the model picker in Claude Desktop works in Claude for Government, what the 1M context window entry does for long conversations that would otherwise be compacted at the standard 200K window, how to choose it, and what controls which models you see.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government. The last section is for administrators.

The model picker shows which Claude model answers you and lets you switch to another. It sits at the bottom of the message box in Chat, Cowork, and Code. Which models it lists depends on the [seat tier](/docs/government/account/profile) your organization has assigned to you, so a colleague may see a different list.

## Larger context window

Some models appear in the picker twice. In Chat and Cowork the second entry has **1M context window** under the model's name, and in Code it shows **1M** after the name. Both entries are the same model, and the difference is how much of a conversation Claude can keep in view at once, which is called the context window and is measured in tokens (a token is a short piece of text, roughly a word or part of one). The standard entry keeps up to about 200,000 tokens (200K) in view. The **1M context window** entry keeps up to about one million (1M), five times as much.

When a long conversation or task gets close to filling the context window, Claude summarizes the earlier part to make room and carries on from the summary, which the app calls compacting. With the **1M context window** entry this happens much later, so long pieces of work keep their full detail for longer. Until a conversation outgrows the standard entry's window, the two entries behave the same and use the same amount of your [allowance](/docs/government/account/usage). Past that point the **1M context window** entry keeps sending Claude the whole conversation rather than a summary, so each further message uses more of your allowance and responses can take longer to start.

To use the larger window, open the model picker and choose the model's entry marked **1M context window**, or **1M** in Code. The entry in use has a check mark next to it, and the model name in the message box reads the same for both entries in Chat and Cowork, so open the picker to check. If you have not picked a model before, the larger window may already be selected. The entry appears only for models where Claude for Government offers the larger window, so if no model in your picker has it, ask your organization's owner whether your seat tier can include a model that does.

<Note>
  The **1M context window** entry appears in Claude Desktop 1.17377.1 and later. Claude Desktop 1.28929.0 and later also keep the entry you chose for new conversations and after a restart. Versions in between return to the standard entry each time, so choose the **1M context window** entry again when you start new work, or ask your IT administrator to update Claude Desktop.
</Note>

## Model availability for administrators

The models a member sees come from the **Allowed models** of their [seat tier](/docs/government/org-admin/seat-tiers). Whether a model also offers the **1M context window** entry is set by Anthropic for each model rather than in the admin portal. To see which models offer it, open the model picker in Claude Desktop, which shows the entries for your own seat tier. When you change a tier's allowed models, access changes straight away. A change of either kind, to a tier's allowed models or to which models offer the entry, shows in the picker's list the next time the member starts Claude Desktop.

Usage on either entry counts against the same spend limits. A long conversation on the **1M context window** entry uses more only because each message carries more of the conversation.
