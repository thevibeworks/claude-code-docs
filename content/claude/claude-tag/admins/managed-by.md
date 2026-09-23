> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage a channel's instructions from another channel

> Managed by lets a central team write a Slack channel's standing Claude instructions from its own channel. Covers setup, the Confirm card, and limits.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

**Managed by** is a channel setting that names other Slack channels whose members can write that channel's standing instructions for Claude. The channel that carries the setting is the managed channel, and each channel it names is a managing channel. People in a managing channel ask Claude to set or update the managed channel's instructions and confirm the change on a card, and Claude follows that text in every new conversation in the managed channel. This page is for admins who set up the pairing and for the people in a managing channel who write the instructions.

Setting up **Managed by** takes an Owner or Admin in your Claude organization, the roles that see the **Admin** tab on a channel's Configure page. A managing channel isn't a [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers). A channel manager is a person with a role that lets them configure one channel. A managing channel is a Slack channel, and the full workspace members in it can propose and confirm changes.

## When to use Managed by

The table compares the places standing instructions for Claude can live and who writes each.

| You want                                                                                                                      | Use                                                                                                                                | Who writes it                                                                                                                           |
| :---------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| The same rules in every channel of a workspace or your whole organization                                                     | [Custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) on the workspace or organization scope           | An Owner, in admin settings                                                                                                             |
| A central team to write the rules for a few channels it runs, such as a help desk or an on-call channel, without being admins | **Managed by**                                                                                                                     | Members of a managing channel, by asking Claude in Slack                                                                                |
| The people who work in a channel to set its conventions themselves                                                            | The **Channel instructions** field on the channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) | Channel members, unless an admin has [restricted editing](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) |

You set up **Managed by** one channel at a time, and someone confirms each change to a channel's text in Slack. That suits a handful of channels. To give many channels the same text, use workspace or organization custom instructions.

Members of the managed channel can still change the managed text by asking Claude. Read [Limits of Managed by as a control](#limits-of-managed-by-as-a-control) before you rely on it to keep a channel's instructions fixed.

## Channel requirements for Managed by

The **Managed by** list on the managed channel's Configure page refuses a pairing that doesn't meet these requirements.

* **Every channel in the pairing:** Claude is a member, and the channel is an ordinary channel in the same Slack workspace as the others. Direct messages and group direct messages can't be managed or managing channels.
* **Sharing:** no channel in the pairing is shared outside its workspace. That rules out Slack Connect channels, including ones with a pending invitation, and channels shared across the workspaces of an Enterprise Grid.
* **You:** you are a member of every managing channel you add.
* **Managed channel:** the channel has its own channel scope on the **Slack** tab in admin settings. If it doesn't appear there, [add the channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel).

A managed channel can have up to five managing channels. A private managed channel has extra rules, listed under [Public and private channels](#public-and-private-channels).

## Choose the managing channels

<Steps>
  <Step title="Open the managed channel's Configure page">
    In the channel whose instructions will be managed, select the **Configure** link in the footer of any Claude reply, or send [`@Claude !configure`](/docs/claude-tag/users/commands#get-the-link-to-configure-a-channel) and follow the link Claude posts. Go to the **Admin** tab.
  </Step>

  <Step title="Select channels under Managed by">
    Open the **Managed by** list and select up to five channels. The list shows channels that you and Claude are both in. It finds them through the Slack account connected to your Claude account, and it asks you to connect one if you haven't. The selection saves when you close the list.
  </Step>

  <Step title="Tell the managing channel">
    Nothing is posted in the managing channel when you add it. Claude learns about the pairing at the start of a conversation, so ask people there to start a new thread before they make the first change, and point them to [Write or update managed instructions](#write-or-update-managed-instructions).
  </Step>
</Steps>

To stop a channel managing another, clear it from the same list. Removing a channel works even when the pairing no longer meets the requirements.

## Write or update managed instructions

A managing channel is a Slack channel that an admin selected under **Managed by** on another channel's Configure page. Any full member of the workspace who is in a managing channel can ask Claude there to change the managed channel's instructions. Guests and people from other organizations can't.

<Steps>
  <Step title="Ask Claude in the managing channel">
    Mention Claude, name the managed channel, and say what the instructions should be.

    ```text wrap theme={null}
    @Claude set the instructions for #it-help to: Answer from the IT handbook first. For laptop requests, link the hardware form. If someone reports a security problem, tell them to page the on-call and stop.
    ```

    Claude reads the managed channel's current text, then posts a card in the managing channel that shows every line the change adds or removes.
  </Step>

  <Step title="Confirm the card">
    Any full member of the managing channel can select **Confirm**. Nothing changes until someone selects it. **Cancel** drops the proposal.
  </Step>

  <Step title="Check the result">
    Start a new thread in the managed channel and ask Claude to repeat its admin instructions. The text you confirmed appears after your workspace's instructions and before the channel's own. You need to be a member of the managed channel to check.
  </Step>
</Steps>

To add long material as a [reference file](#how-managed-instructions-load), give the file a short name made of lowercase letters, digits, hyphens, or underscores.

```text wrap theme={null}
@Claude add a reference file called escalation-list to the managed instructions for #it-help with this text: ...
```

Claude posts the same kind of card, and the file exists once someone confirms it. Deleting works the same way. Ask Claude to delete the managed channel's instructions or one reference file, then confirm the card, which quotes every line being removed.

These rules apply to every card.

* **One change per card:** each card carries one change to the core instructions or to one reference file, and shows the whole change
* **Long rewrites:** Claude proposes a long rewrite in parts. After you confirm one part, ask for the next in a new message.
* **Text changed since Claude read it:** confirming the card changes nothing. Ask Claude again so it proposes the change against the current text.

## How managed instructions load

Managed instructions are either core instructions, which Claude always reads, or reference files, which Claude opens when the core instructions call for one.

| Kind              | How many                                             | Size limit   | When Claude reads it                                          |
| :---------------- | :--------------------------------------------------- | :----------- | :------------------------------------------------------------ |
| Core instructions | One per managed channel                              | 16 KiB       | At the start of every new conversation in the managed channel |
| Reference files   | Up to 20 per managed channel, each with a short name | 100 KiB each | When the core instructions point Claude to one by name        |

Put what Claude must always follow in the core instructions. Put long material, such as a runbook or an escalation list, in a reference file, and name that file in the core instructions so Claude knows when to open it.

Claude reads standing instructions in this order:

1. Organization instructions
2. Workspace instructions
3. The managed channel's core instructions
4. The channel's own **Channel instructions**

All of them outrank channel memory. Managed instructions add to the channel's own instructions and don't replace them.

A confirmed change applies to conversations that start after it.

* **New threads:** Claude reads the new text
* **Threads already running:** Claude keeps the text the thread started with
* **The channel's top level:** Claude picks up the change on a later channel message

## Public and private channels

A managing channel's members can read the managed channel's instructions through Claude, so a private channel's text can be managed only from other private channels.

| Managed channel | Managing channels can be | Who can add managing channels                                 |
| :-------------- | :----------------------- | :------------------------------------------------------------ |
| Public          | Public or private        | An Owner or Admin                                             |
| Private         | Private only             | An Owner or Admin who is also a member of the private channel |

Anyone in the workspace can join a public managing channel and confirm changes there, so prefer a private managing channel for anything sensitive.

When a public managed channel is made private, its managing channels are removed. An Owner or Admin who is a member of the now-private channel can add private managing channels again.

## Limits of Managed by as a control

**Managed by** sets which channels' members can write a channel's standing instructions through Claude. It isn't an access control. The managed text is stored with the managed channel's [memory](/docs/claude-tag/users/memory), so a member of the managed channel who asks Claude to change what it has saved there can still alter or remove the text.

For instructions that channel members can't change, use [organization or workspace custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions). For anything Claude must not do, use [access controls](/docs/claude-tag/admins/restrict-access).

If Claude can't read managed instructions when a conversation starts, the conversation starts without them.

## Troubleshoot Managed by

Claude words a refusal differently each time, so match a row on its meaning. The table covers the refusals Claude or the Configure page gives for a pairing or a change.

| What you're told                                                                                    | Cause                                                                                                                                | Fix                                                                                                                                       |
| :-------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| This channel isn't set as a manager of the other channel                                            | No pairing exists, or it was removed                                                                                                 | Add this channel under **Managed by** on the other channel's Configure page                                                               |
| A channel is shared with another organization                                                       | The managed or managing channel is a Slack Connect channel, has a pending invitation, or is shared across Enterprise Grid workspaces | Use channels that belong to one workspace only                                                                                            |
| You aren't in the managing channel, or in the private managed channel                               | You tried to add a managing channel you haven't joined, or to add managing channels to a private channel you aren't in               | Join the channel in Slack, then try again                                                                                                 |
| Claude isn't in one of the channels                                                                 | Claude was removed from the managed or managing channel, or never added                                                              | Run `/invite @Claude` in that channel                                                                                                     |
| A private channel can only be managed by private channels                                           | The managed channel is private and the managing channel is public, or was made public later                                          | Pick a private managing channel                                                                                                           |
| The managed channel may have been made private or deleted                                           | The managed channel was made private or deleted, or Claude is no longer in it                                                        | Check the channel in Slack. If it was made private, an Owner or Admin who is a member of it adds private managing channels again          |
| Claude isn't set up in the managed channel with its own channel configuration                       | The managed channel has no channel scope of its own on the **Slack** tab                                                             | [Add the channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) in admin settings                                               |
| The managed channel already has five managing channels                                              | Five is the most a managed channel can have                                                                                          | Remove one before adding another                                                                                                          |
| The file would be too large                                                                         | The core instructions are over 16 KiB, or a reference file is over 100 KiB                                                           | Shorten the text, or move detail into a reference file                                                                                    |
| The managed channel already has the most reference files                                            | Twenty reference files exist                                                                                                         | Ask Claude to delete one first                                                                                                            |
| The change is too large to show                                                                     | The card can't display every changed line                                                                                            | Ask for a smaller part, confirm it, then ask for the next part                                                                            |
| The text was refused by the content check                                                           | The text is blank or contains characters, links, or formatting the content check doesn't allow                                       | Remove that part or write it as plain text, then ask again                                                                                |
| Managed instructions changes aren't available for organizations with restricted compliance settings | Your organization has restricted compliance settings                                                                                 | See [Restricted compliance settings block Claude Tag](/docs/claude-tag/admins/troubleshooting#restricted-compliance-settings-block-claude-tag) |

## Related resources

* [How custom instructions stack](/docs/claude-tag/admins/attach-to-scope#custom-instructions): how organization, workspace, and channel instructions combine
* [Customize Claude Tag](/docs/claude-tag/admins/customize): every layer that shapes Claude's behavior and who sets it
* [What Claude Tag remembers](/docs/claude-tag/users/memory): channel memory, where managed text is stored
