> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Find answers in your docs

> Claude Tag finds answers in connected docs and replies in the thread. See policy lookups, runbook checks, prior decisions, and answers from the Slack channel alone.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How answer-finding prompts work

Each prompt below is a Slack message. You paste it in the channel where the question came up, Claude searches the connected docs or the channel history and posts progress in that thread, and the answer lands there too. The result is always an answer with the source it came from, so you can open what it read.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection         | Examples                         | Why it matters here                                                                                             |
| :----------------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Knowledge and docs | Google Drive, Notion, Confluence | Required to search those sources; channel-history-only answers need none. Searches the docs the answers live in |

## Prompts to paste

### Look up a policy

A customer asks about data retention and you need the policy, not a recollection. Ask where the question comes up.

```text wrap theme={null}
@Claude what's our policy on data retention, and which doc says so?
```

Asking for the doc keeps the answer checkable, since you can open what it read.

### Check a named document

Launch is close and you need to know whether the plan covers the EU rollout, without re-reading it. Point it at the document and the question.

```text wrap theme={null}
@Claude does the launch plan cover the EU rollout? Quote the relevant section if it's there.
```

"Quote the relevant section" turns a yes/no into evidence.

### Find the latest version

The pricing deck gets recreated every quarter, and the link you saved is two versions old. Ask for the current one.

```text wrap theme={null}
@Claude find the latest pricing deck and post where it lives.
```

### Answer from the channel alone

Without any connection, Claude can still answer from the channel's own history.

```text wrap theme={null}
@Claude what did this channel decide about the retention policy, and when?
```

Answers come from this channel's history and [memory](/docs/claude-tag/users/memory).

## Related resources

<CardGroup cols={2}>
  <Card title="Catch up" href="/docs/claude-tag/users/use-cases/catch-up" horizontal arrow>
    The same mechanism pointed at "what did I miss"
  </Card>

  <Card title="What Claude Tag remembers" href="/docs/claude-tag/users/memory" horizontal arrow>
    How channel knowledge accumulates
  </Card>
</CardGroup>
