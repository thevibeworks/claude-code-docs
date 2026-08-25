> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fix bugs

> Claude Tag takes a bug report from Slack to a draft pull request. See reproducing the issue, watching a bug channel, root-cause digs, and following CI to green.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How bug-fix prompts work

This page is for engineering teams. A pull request is a proposed code change opened for review; Claude opens them under its own GitHub identity, so they appear in your review queue like any other pull request.

Each prompt below is a Slack message. You paste it in the channel or thread where the bug lives, Claude works on it in an isolated workspace Anthropic hosts and posts progress in that thread, and the result lands there too. What the result is depends on the prompt, and each one below says what it returns, like a draft pull request, a root-cause writeup, or a standing watch that triages new reports as they arrive. Anything it opens on GitHub is authored by the Claude GitHub App.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples | Why it matters here                                    |
| :--------- | :------- | :----------------------------------------------------- |
| Code       | GitHub   | Required. Reads the repo and opens draft pull requests |

## Prompts to paste

### Fix a reported bug

A bug report arrives with reproduction steps and nobody free to take it. This gets you a draft pull request with the fix, linked back to the thread. Name the repository in the prompt so it's cloned before work starts.

```text wrap theme={null}
@Claude in acme/data-pipeline, reproduce the bug in this thread, fix it, and open a draft PR. Done means CI is green and the PR links back here.
```

The done definition, CI green and the PR linking back, gives the session a finish line it can check itself against.

The pull request appears under the Claude GitHub App and links back to the Slack thread it came from. See [how agent identity works](/docs/claude-tag/concepts/agent-identity#agent-access).

### Move a bug report to the owning team's channel

A report that landed in a general channel belongs with the team that owns the code. Fork the thread into their channel and put the fix prompt in the fork, so the owners see the work as it happens and the original thread gets a link to follow.

```text wrap theme={null}
@Claude !fork #data-platform in acme/data-pipeline, reproduce the bug described in the linked thread, fix it, and open a draft PR. Done means CI is green and the PR links back here.
```

Both channels must be public, and you and Claude must both be in the target. See [Fork a thread](/docs/claude-tag/users/commands#fork-a-thread).

### Watch a bug channel

Reports arrive faster than the team triages them. The standing form watches the channel and opens drafts for anything reproducible.

```text wrap theme={null}
@Claude when a bug report lands in this channel, try to reproduce it. If you can, open a draft PR and tag the area owner; if you can't, reply with what you tried.
```

With the if/can't branch, every report gets a reply, either a draft or a list of what was tried. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Diagnose a failure without a fix

Not every failure needs a pull request. Ask for the diagnosis alone, and the decision about what to do with it stays with the team.

```text wrap theme={null}
@Claude why is this failing? Trace it to a cause and post what you find — diagnosis only, no fix.
```

Naming the deliverable, a cause rather than a patch, keeps the session from jumping ahead to code changes nobody asked for.

### See a pull request through CI

Once a pull request exists, one Claude opened or one a person did, Claude can watch it instead of you refreshing the page. It subscribes to that pull request and posts when CI status changes.

```text wrap theme={null}
@Claude watch PR #482 in acme/data-pipeline. When CI finishes, post the result here, and tag me if anything failed.
```

"Tag me if anything failed" is the filter. Green runs land quietly in the thread, and only a failure interrupts you.

For repository conventions that should hold across every session that touches the code, like where files go or what a pull request must include, see [Make repo conventions stick](/docs/claude-tag/users/good-habits#teach-claude-something-that-sticks).

## Related resources

<CardGroup cols={2}>
  <Card title="Watch monitors and alerts" href="/docs/claude-tag/users/use-cases/watch-monitors" horizontal arrow>
    Catching the problem before the bug report
  </Card>

  <Card title="Good habits" href="/docs/claude-tag/users/good-habits" horizontal arrow>
    Definitions of done for code tasks
  </Card>
</CardGroup>
