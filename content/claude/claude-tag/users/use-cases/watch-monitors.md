> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Watch monitors and alerts

> Claude Tag watches dashboards and alert channels so you see one line per issue. See scheduled checks, alert investigation before anyone asks, and the prompts to set both up.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How monitor-watch prompts work

This page is for operations and on-call teams. A monitor is an automated check in a tool like Datadog or PagerDuty that fires an alert when a metric crosses a threshold. These prompts have Claude check those dashboards or investigate alerts as they arrive.

Each prompt below is a Slack message. You paste it in the channel that receives the alerts, Claude checks the connected dashboards or investigates the alert and posts progress in that thread, and the findings land there too. What comes back depends on the prompt, and each one below names it, like a scheduled one-line-per-service check, a single alert's diagnosis, or a standing watch that posts only changes.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples                   | Why it matters here                        |
| :--------- | :------------------------- | :----------------------------------------- |
| Monitoring | Datadog, Sentry, PagerDuty | Required. Reads dashboards and alert state |

## Prompts to paste

### Schedule a recurring dashboard check

One message sets up a standing check that posts every morning, one line per service.

```text wrap theme={null}
@Claude every morning at 7, check the service dashboards and post one line per service: green, or what's off and since when.
```

Name the output format in the schedule, like "one line per service" above, so every post reads the same way. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Investigate a single alert

Reply in the thread the alert landed in for a first pass at diagnosis. The prompt names what diagnosis means here and where to put the result.

```text wrap theme={null}
@Claude investigate this alert: when it started, what changed around then, and what you'd look at first. Post findings here.
```

"When it started, what changed around then" points the work at diagnosis, and "post findings here" keeps the trail in the thread for whoever picks it up.

### Start the diagnosis before anyone asks

Set this up as a routine to get both: a scheduled check against the last known state, and an investigation kicked off for any change. The routine posts only when something changed, not on every check.

```text wrap theme={null}
@Claude every two hours, check the alerting dashboard against its last state. For anything new, post when it started, what changed around then, and what to look at first.
```

## Related resources

<CardGroup cols={2}>
  <Card title="Fix bugs" href="/docs/claude-tag/users/use-cases/fix-bugs" horizontal arrow>
    When the investigation should end in a pull request
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    Schedules and event triggers
  </Card>

  <Card title="Claude on call" href="https://claude.com/blog/ai-ci-cd-on-call" horizontal arrow>
    How Anthropic runs Claude as first responder for CI/CD failures
  </Card>

  <Card title="On-call kit" href="https://github.com/anthropics/oncall-kit" horizontal arrow>
    Reference playbooks, templates, and guided setup for an on-call channel
  </Card>
</CardGroup>
