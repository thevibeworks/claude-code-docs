> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Tag for marketing teams

> Claude Tag recipes for marketing teams in Slack. See policy answers in an intake channel, campaign channel recaps and send-ready drafts, lead and campaign state from the CRM, a weekly metrics digest, and brand voice rules saved to channel memory.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How marketing prompts work

This page is for marketing teams. The recipes below run in the channels where marketing work already happens, like an intake channel where other teams post requests, a campaign channel during a launch, and the channel where lead numbers get discussed.

Each prompt below is a Slack message. You paste it in the channel where that work lives, Claude posts progress in that thread, and the result lands there too. What you get depends on the prompt, and each recipe names it, like an answer with the doc it came from, a channel recap, a send-ready draft, a list of CRM records, or a scheduled digest.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing. Each recipe below names the connection it uses.

| Connection         | Examples                         | Why it matters here                                                      |
| :----------------- | :------------------------------- | :----------------------------------------------------------------------- |
| None               | —                                | Recaps, drafts, and brand voice rules work on Slack content alone        |
| Knowledge and docs | Google Drive, Notion, Confluence | Answers policy and process questions from the docs where they're written |
| Go-to-market       | HubSpot, Salesforce              | Reads CRM records, like contacts, leads, and deals                       |
| Data warehouse     | BigQuery, Snowflake              | Runs the queries behind the metrics digest                               |

## Prompts to paste

### Answer policy questions in an intake channel

Other teams bring marketing their process questions, like whether the company can sponsor an event, who approves a use of the logo, and who owns customer stories. When the answers are written in the team's connected docs, Claude can answer each request in the thread where it was asked.

```text wrap theme={null}
@Claude a vendor asked us to sponsor their conference. What's our sponsorship policy, and which doc says so?
```

Asking for the doc keeps the answer checkable, since you can open what it read.

To answer requests as they arrive instead of prompting each time, give the channel a standing role:

```text wrap theme={null}
@Claude remember for this channel: when someone tags you on a request, answer it from the brand guidelines and the marketing process docs, name the doc you used, and route anything the docs don't cover to the right owner with a one-line summary.
```

"Remember for this channel" saves the role to [channel memory](/docs/claude-tag/users/memory), so it applies to everyone's threads, not just yours. [Triage requests](/docs/claude-tag/users/use-cases/triage-requests) adds a weekly rollup that also sweeps posts that never tagged Claude.

Some questions have no doc to cite, and a person on the team answers in the thread. When that answer will come up again, tell Claude to save it:

```text wrap theme={null}
@Claude remember for this channel: conference sponsorships are capped at $5,000, and the events lead approves each one.
```

The next person who asks gets the answer from channel memory instead of waiting for the team. When the policy changes, ask `@Claude what do you remember about this channel?` and tell it to update the entry.

### Recap a campaign channel and draft from it

During a launch, a campaign channel fills with decisions, status updates, and copy changes faster than anyone can read them all. Ask for a recap bounded by a time window, and when a thread settles what an announcement should say, ask for the draft in that thread.

```text wrap theme={null}
@Claude catch me up on this channel since Monday: what got decided, what's still open, and anything waiting on marketing.
```

The time window bounds the recap, so it comes back in a shape you can check.

```text wrap theme={null}
@Claude turn this thread into an announcement draft I can send to the customer list. Keep it under 200 words and match the messaging doc linked above.
```

Name the format, the length, and the source the draft should match. The same prompt shape produces a decision doc or a status memo; [Turn threads into docs and tickets](/docs/claude-tag/users/use-cases/create-artifacts) lists the variants.

### Check lead and campaign state in the CRM

A lead is a prospect record in a CRM like HubSpot or Salesforce, created when someone responds to a campaign. When the channel is debating whether a campaign's leads are moving, ask the question against those records.

```text wrap theme={null}
@Claude which leads from last month's webinar campaign still have no owner, and how long has each been waiting?
```

Asking how long each has waited tells you which lead to chase first.

```text wrap theme={null}
@Claude compare the leads the June campaign created against the ones that reached a queue, and post which ones stalled and at what stage.
```

The reply lists the stalled records and the stage where each stopped. The [HubSpot connection](/docs/claude-tag/admins/connections/hubspot) is created with read scopes, so prompts in this channel pull records and don't change them. For account questions, pre-call briefs, and a pipeline digest, see [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state).

### Schedule a weekly campaign metrics digest

When the team checks the same campaign numbers at the start of every week, schedule the post instead of asking each time. One message sets up the recurring report, and it needs a data warehouse connection to run the queries.

```text wrap theme={null}
@Claude every Monday at 9am Eastern, post last week's campaign metrics as a chart: signups by campaign, week-over-week change, and a two-line note on anything unusual.
```

Naming the timezone matters, since schedules default to UTC. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Save brand voice rules to channel memory

Claude follows the tone and terminology rules saved to a channel's memory, so a rule saved once applies to every later draft in that channel.

```text wrap theme={null}
@Claude remember for this channel: headlines use sentence case, "sign up" is the verb and "signup" is the noun, and the product is never called a platform.
```

Keep saved entries short, since long entries crowd out everything else. For a full style guide, link the document in the channel or store it in a connected tool Claude can read, instead of re-describing its contents in memory. [What Claude Tag remembers](/docs/claude-tag/users/memory) covers how to check and correct what's saved.

## Related resources

<CardGroup cols={2}>
  <Card title="Pull deal and account state" href="/docs/claude-tag/users/use-cases/pull-deal-state" horizontal arrow>
    The full set of go-to-market prompts
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    How the scheduled digest runs, and more recipes
  </Card>
</CardGroup>
