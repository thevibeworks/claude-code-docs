> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pull deal and account state

> Claude Tag pulls account and deal state into the Slack channel. See in-thread account answers, pre-call briefs, and a scheduled weekly pipeline digest.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How deal-state prompts work

This page is for sales and customer-success teams. A deal (also called an opportunity) is a sales prospect tracked in a CRM like Salesforce or HubSpot; an account is a customer record. These prompts pull that state into the Slack channel where the team discusses it.

Each prompt below is a Slack message. You paste it in the account or deal channel, Claude pulls from the connected CRM and the channel discussion and posts progress in that thread, and the result is posted in that thread. What you get depends on the prompt, and each one below names it, like one account's state, a pre-call brief, or a scheduled pipeline digest.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection   | Examples                  | Why it matters here                      |
| :----------- | :------------------------ | :--------------------------------------- |
| Go-to-market | Salesforce, HubSpot, Gong | Required. Pulls account and deal records |

## Prompts to paste

### Check one account's state

The reply lists last activity, open items, and who owns the next step for the named account.

```text wrap theme={null}
@Claude what's the state of the Acme renewal? Last activity, open items, and who owns the next step.
```

### Find stalled deals

The reply lists deals stuck at the named stage and how long each has been there.

```text wrap theme={null}
@Claude which deals are stuck in stage 3, and how long has each been there?
```

"How long has each been there" is the actionable half. Aging tells you which deal to work first.

### Get a pre-call brief

The brief pairs what's in the system with what was discussed in the channel.

```text wrap theme={null}
@Claude brief me on Initech before my 2pm: account history, recent activity, and anything discussed in this channel lately.
```

### Schedule a weekly digest

One message sets up a standing digest posted to the team channel every Monday.

```text wrap theme={null}
@Claude every Monday at 9am, post a pipeline digest: deals that moved stage last week, deals stalled more than two weeks, and renewals due in the next 30 days.
```

The three lines cover what moved, what's stuck, and what's coming due, so the digest reads the same way every Monday. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

## Related resources

<CardGroup cols={2}>
  <Card title="Answer data questions" href="/docs/claude-tag/users/use-cases/answer-data-questions" horizontal arrow>
    When the question is metrics, not accounts
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    Scheduled digests
  </Card>
</CardGroup>
