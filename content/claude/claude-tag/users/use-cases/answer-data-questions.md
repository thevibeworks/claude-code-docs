> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Answer data questions

> Claude Tag answers data questions in the Slack thread. See warehouse queries with charts, scheduled metric reports, and charts built from channel history alone.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How data-question prompts work

This page is for teams who answer questions from a data warehouse (the database where your analytics tables live, like BigQuery or Snowflake). These prompts turn a question asked in Slack into a query and a chart.

Each prompt below is a Slack message. You paste it in the channel where the metrics get discussed, Claude queries the warehouse or reads the channel history and posts progress in that thread, and the result lands there too. The result is a chart with a short answer, returned once or on a schedule depending on the prompt.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection     | Examples            | Why it matters here                          |
| :------------- | :------------------ | :------------------------------------------- |
| Data warehouse | BigQuery, Snowflake | Required. Runs the queries behind each chart |

## Prompts to paste

### Chart a metric on demand

The thread is debating something a number would settle. Ask in the channel where the metrics get discussed.

```text wrap theme={null}
@Claude show signup growth by week for the last quarter, and explain the two dips people were debating above.
```

### Schedule a recurring metrics report

When the team checks the same numbers every morning, schedule the post. One message sets up the recurring report.

```text wrap theme={null}
@Claude every morning at 8, post yesterday's key metrics as a chart with a two-line summary of anything unusual.
```

Naming the format, here a chart plus two lines, keeps a recurring post scannable instead of letting it grow each day. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Chart from Slack alone

Charts don't require a connection, because channel history is data. It can chart request volume in a triage channel, or how long requests waited for a first reply.

```text wrap theme={null}
@Claude chart the volume of requests in this channel by week, and how long each waited for a first reply.
```

Anyone in the thread can ask for a different cut of the same data.

## Related resources

<CardGroup cols={2}>
  <Card title="Watch monitors and alerts" href="/docs/claude-tag/users/use-cases/watch-monitors" horizontal arrow>
    When the question is about systems, not metrics
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    Recurring reports
  </Card>

  <Card title="Self-service data analytics" href="https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions" horizontal arrow>
    How Anthropic answers ad-hoc data questions in Slack with Claude
  </Card>
</CardGroup>
