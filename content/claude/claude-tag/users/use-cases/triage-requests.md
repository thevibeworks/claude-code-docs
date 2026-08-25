> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Triage requests

> Claude Tag triages a Slack request channel with two setup messages. See in-thread answers, duplicate flags, owner routing, weekly theme rollups, and optional ticket filing.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How triage prompts work

This page is for any team with an intake channel, like #ask-it, #design-requests, or #legal-help, where people post questions and someone has to route or answer each one.

The two prompts below are Slack messages you paste in the request channel, in order. Together they set up a standing role: when someone tags `@Claude` on their request, it replies in-thread, answering what it can, flagging duplicates, and routing the rest. The weekly rollup lands as a top-level post in the same channel and sweeps anything that wasn't tagged.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection     | Examples     | Why it matters here                     |
| :------------- | :----------- | :-------------------------------------- |
| None           | —            | Works on Slack content alone            |
| Issue tracking | Linear, Jira | Optional. Files routed items as tickets |

## Prompts to paste

Add Claude to the channel with `/invite @Claude` if it isn't there, then two messages set it up.

<Steps>
  <Step title="Give the channel a standing role">
    ```text wrap theme={null}
    @Claude remember for this channel: when someone tags you on a request, check whether it duplicates something already reported, answer it directly if the answer exists, and otherwise route it to the right owner with a one-line summary. Track recurring themes.
    ```

    "Remember for this channel" saves the role to [channel memory](/docs/claude-tag/users/memory), so it applies to everyone's threads, not just yours. Tell requesters to include `@Claude` when they post; pin the convention or add it to the channel topic.
  </Step>

  <Step title="Add a weekly rollup so nothing is missed">
    ```text wrap theme={null}
    @Claude every Friday at 3pm, post a summary of this week's requests: how many, top themes, and anything still unrouted, including posts that didn't tag you.
    ```

    "Including posts that didn't tag you" turns the recap into a sweep, so requests that arrived without a mention are still caught. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).
  </Step>
</Steps>

Answers draw on what the channel has already settled, meaning its [memory](/docs/claude-tag/users/memory) and its own past threads, and routing gets more accurate as corrections land in channel memory.

## Hand a request to the team that owns it

When a request belongs to another team, fork its thread into that team's channel from inside the thread. Claude starts a new thread there with the request as background and leaves a link in the original thread, so the requester can follow the work without being re-asked for details.

```text wrap theme={null}
@Claude !fork #payments-eng take this request: the reporter needs refunds on partial orders, and their screenshots and the duplicate check are in the linked thread.
```

The channel you name must be public, with both you and Claude in it. See [Fork a thread](/docs/claude-tag/users/commands#fork-a-thread) for the other rules.

## Related resources

<CardGroup cols={2}>
  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    How the weekly rollup runs on a schedule
  </Card>

  <Card title="What Claude Tag remembers" href="/docs/claude-tag/users/memory" horizontal arrow>
    How the standing role persists and improves
  </Card>
</CardGroup>
