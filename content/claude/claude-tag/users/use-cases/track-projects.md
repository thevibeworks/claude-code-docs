> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track projects and chase approvals

> Claude Tag posts project digests no one has to compile. See standing status updates and follow-ups on contracts, design reviews, and pull requests until they close.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How project-tracking prompts work

This page is for anyone running a project from a Slack channel: pulling status, chasing approvals, and posting digests so the team doesn't have to ask.

Each prompt below is a Slack message. You paste it in the project channel, Claude reads channel history and any connected trackers and posts progress and the result in that thread. What you get depends on the prompt, and each one below names it, like a one-time status digest, a scheduled daily digest, or a follow-up that runs until an approval lands.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection     | Examples            | Why it matters here                                                                         |
| :------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Issue tracking | Linear, Jira, Asana | Optional. Adds tracker state to digests; without it, digests draw from channel history only |
| Code           | GitHub              | Optional. Checks PR and review state                                                        |

## Prompts to paste

### Get a one-time status update

The reply pulls status spread across days of channel scroll into one digest. Ask in the project channel.

```text wrap theme={null}
@Claude where are we on the migration? What's blocked and on whom?
```

The digest comes back in the thread with what moved, what's blocked, and on whom, built from channel history plus any connected trackers.

### Schedule a daily project digest

One message sets up a digest that posts every weekday.

```text wrap theme={null}
@Claude every weekday at 5pm, post a project digest: what moved today, what's blocked, and what hasn't been touched in three days.
```

Name the format in the prompt, like the three sections here, so every digest comes back in the same readable shape. "Hasn't been touched in three days" is a number, so stalled work surfaces itself instead of depending on someone's sense of what counts as stale. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Chase an approval

A contract sits with legal, a design review has no comments, a pull request waits on a reviewer. Claude can follow any of them until they close. It nudges when the review stalls and posts when the state changes.

```text wrap theme={null}
@Claude every weekday, check the design review discussed in this thread. If it's gone two weekdays with no reviewer reply, nudge them here; when an approval lands, post that it's done. Done means approved, not just commented on.
```

Define what "done" includes; see [the babysit caution](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done).

Code approvals need the code connection. Scheduled follow-ups on repositories use that same GitHub connection, with nothing extra to set up.

## Related resources

<CardGroup cols={2}>
  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    Schedules and event triggers
  </Card>

  <Card title="Good habits" href="/docs/claude-tag/users/good-habits" horizontal arrow>
    Definitions of done that close threads
  </Card>
</CardGroup>
