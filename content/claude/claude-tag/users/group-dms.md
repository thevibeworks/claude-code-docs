> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Tag in a group DM

> Add Claude to a Slack group DM to share a task with a few people. See whose access and billing apply, when Claude replies, and what differs from a channel.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

A group DM is a Slack direct message among several people. Claude works in a group DM it has been added to, so a few people can share a task with Claude without creating a channel.

If Claude answers your mention with "Group DMs aren't supported yet. Try a channel or a 1:1 DM instead.", see [the causes of that reply](/docs/claude-tag/users/troubleshooting#group-dms-aren%E2%80%99t-supported-yet).

This page is for Slack members. It covers how to add Claude, what Claude can reach, when it replies, how to make it quieter, what differs from a channel, and what to do when Claude doesn't answer. If you administer Claude for your organization, see [the settings that apply to group DMs](/docs/claude-tag/admins/restrict-access#group-dms).

## Add Claude to a group DM

Add Claude as one of the people when you start the group DM. Then mention `@Claude` with your request.

```text wrap theme={null}
@Claude draft a rollout checklist for the pricing page change.
```

Claude replies in a thread under your message.

An admin decides [who can use Claude](/docs/claude-tag/admins/restrict-access#restrict-who-can-use-claude), and that choice covers group DMs as well as channels.

## Access and billing in a group DM

In a group DM, Claude acts with [its own service accounts](/docs/claude-tag/concepts/agent-identity). If you've connected a Claude account, a one-to-one DM with Claude runs on [your own account](/docs/claude-tag/concepts/agent-identity#direct-message-channels) instead.

* **Access.** Claude uses the connections, instructions, and repositories an admin set for the workspace and the organization. A connection an admin attached to one channel doesn't apply.
* **Billing.** The work bills to your organization, not to your seat.
* **Your own connectors.** Where [personal connectors in channels](/docs/claude-tag/concepts/personal-connectors) are on for your organization, Claude can use the connectors on your claude.ai account for a task you ask for, after you allow it. Only your own requests use them.

## When Claude replies in a group DM

In a group DM, Claude reads the top-level messages, including the ones that don't mention it.

* **You mention `@Claude` at the top level.** Claude replies in a thread under your message.
* **You reply in a thread that started with an `@Claude` mention.** Your reply reaches Claude without another mention.
* **You post at the top level without a mention.** Claude decides whether to reply.

## Make Claude quieter in a group DM

In a group DM, Claude reads the top-level messages that don't mention it and replies to some of them. You can have Claude reply in the group DM only when someone mentions it, or mute it in one thread.

### Quiet Claude in the whole group DM

Ask Claude to reply only when someone mentions it. The change applies to everyone in the group DM. To select **Confirm** on the card Claude posts, a person needs a connected Claude account in your organization and can't be a Slack guest.

Claude can't make the change in these cases:

* **Channel-only access.** A guest is in the group DM, and Claude runs there with [channel-only access](/docs/claude-tag/admins/restrict-access#how-channel-only-works).
* **Blocked member edits.** An admin set [**Channel member edits**](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) to **Block** for the workspace or the organization.

<Steps>
  <Step title="Ask Claude">
    Mention `@Claude` at the top level of the group DM and ask it to reply only to mentions.

    ```text wrap theme={null}
    @Claude only reply here when someone mentions you.
    ```

    Claude posts a card in the thread under your message, with **Confirm** and **Cancel** buttons.
  </Step>

  <Step title="Confirm the change">
    Select **Confirm** within 10 minutes. The card changes to a line that names the person who confirmed and says Claude now replies only when @mentioned.
  </Step>
</Steps>

After the change, Claude still answers a mention, and it still reads replies in a thread that started with an `@Claude` mention.

To have Claude reply without a mention again, mention `@Claude` and ask.

```text wrap theme={null}
@Claude go back to replying here without a mention.
```

Claude posts a new card. Select **Confirm** on that card.

### Quiet Claude in one thread of a group DM

In a thread that started with an `@Claude` mention, send [`@Claude !mute`](/docs/claude-tag/users/commands#mute-or-unmute-a-thread). `!mute` works on one thread at a time.

## Differences between a group DM and a channel

These parts of working with Claude differ between a group DM and a channel:

* **Settings.** A group DM has no [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), so you can't give it its own instructions, connections, or default model.
* **Memory.** Claude keeps notes for the group DM and reads only those notes there. It doesn't read or add to the [workspace notes](/docs/claude-tag/users/memory#channel-and-workspace-memory).
* **Routines.** A [routine](/docs/claude-tag/users/proactivity) you set up in a group DM posts its output in that group DM only.
* **Other channels.** Claude can't post, reply, or react outside the group DM. [What Claude can do in other channels](/docs/claude-tag/concepts/how-it-works#what-claude-can-do-in-other-channels) covers what it can read.
* **Forking.** You can't [fork a thread](/docs/claude-tag/users/commands#fork-a-thread) from a group DM.

## When Claude doesn't answer in a group DM

When you mention `@Claude` at the top level of a group DM and Claude can't answer, you usually see one of these outcomes.

| What you see | Why Claude can't answer | What to do |
| :- | :- | :- |
| "Group DMs aren't supported yet. Try a channel or a 1:1 DM instead." | Who is in the group DM, or how Slack shares it, keeps Claude from answering | See [Group DMs aren't supported yet](/docs/claude-tag/users/troubleshooting#group-dms-aren%E2%80%99t-supported-yet) |
| "Your Claude admin has disabled sending direct messages to Claude." | An admin turned off direct messages, which covers group DMs too | Ask in a channel, or ask your admin about turning direct messages on |
| "Claude doesn't respond in channels that include guests." | The group DM includes a Slack guest, and your admin's guest setting keeps Claude from replying | Start a group DM without the guest, or ask your admin about the guest setting |
| "Claude is disabled in this channel." | An admin turned Claude off for the workspace | Ask your admin about turning Claude on for the workspace |
| "This workspace only lets people with a connected Claude account work with me." Only you can see this notice | An admin restricted who can use Claude | Connect your Claude account, then send your message again |
| No reply and no notice | Claude isn't in the group DM | Start a new group DM that includes Claude |
| No reply and no notice | Your workspace uses the [earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier) | Ask your admin which version answers in your workspace |

## Related resources

* [Get started with Claude Tag](/docs/claude-tag/users/getting-started): choose between a channel, a group DM, and a one-to-one DM
* [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds): what makes Claude reply without an @-mention
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): whose accounts Claude acts with in each place
