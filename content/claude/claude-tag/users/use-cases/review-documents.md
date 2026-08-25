> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Review documents against a checklist

> Claude Tag reviews documents in a connected tool against a checklist or policy and posts findings in the thread. See single-document checks, batch reviews, filing lists, comparisons with past reviews, and a scheduled weekly sweep.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How document-review prompts work

Each prompt below is a Slack message. You paste it in the channel where the review belongs, Claude reads the documents and the criteria from the connected tool and posts progress in that thread, and the findings land there too. The criteria can be whatever your team already uses, like a checklist, a policy document, or a filing list.

Read the findings before you act on them, in proportion to what's at stake. If a finding needs checking, ask Claude to show its work in the same thread.

## Check the channel's connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection         | Examples                         | Why it matters here                                                                                                      |
| :----------------- | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| Knowledge and docs | Google Drive, Notion, Confluence | Required. Claude reads the documents under review, and the checklist or policy they're checked against, from these tools |

Claude can reach only what the connected account can see in that tool. If a document is missing from a review, ask an admin to [share it with the connected account](/docs/claude-tag/admins/add-connections#limit-access-to-specific-resources).

## Prompts to paste

### Review one document against a checklist

A draft is ready to go out, and it has to pass the team's checklist first. Name the document and the checklist in the channel where the review is happening.

```text wrap theme={null}
@Claude review the launch announcement doc against the review checklist, and post one finding per item: met, not met, or unclear, plus the section you based each call on.
```

Asking for the section keeps each finding checkable, since you can open what it read.

### Review a batch against a policy

A quarter's worth of vendor documents landed in one folder, and each needs the same check. Name the folder and the policy.

```text wrap theme={null}
@Claude go through each document in the vendor-docs folder and check it against the data-handling policy. Post a table with one row per document: what it covers, what's missing, and anything unclear.
```

One row per document bounds the work, so the review comes back in a shape you can check.

### Work through a filing list

Your team keeps a list of filings to check, and each item needs a verdict by the end of the week. Point Claude at the list and where the filings live.

```text wrap theme={null}
@Claude work through this week's filing list in the shared folder. For each item, find the matching filing, check it against the list's criteria, and post its status and what's missing.
```

Naming both the list and the folder scopes the search to the documents that matter.

### Compare with the last review

A revised draft is in, and you need to know whether it fixes what the last review flagged.

```text wrap theme={null}
@Claude review the updated vendor agreement against the checklist, then compare with what the review in this channel found last month and post what changed.
```

Naming the timeframe matters, since Claude looks back by listing this channel's earlier sessions and reading them.

### Schedule a recurring review

New documents arrive every week, and the same check applies to each. Schedule the review instead of asking each time.

```text wrap theme={null}
@Claude every Monday at 9am Pacific, check the shared folder for documents added in the past week, review each against the review checklist, and post the findings here.
```

Including the timezone matters, since schedules default to UTC. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

Keep the checklist as a document Claude can read, in the connected tool or linked in the channel, rather than re-describing its contents in [channel memory](/docs/claude-tag/users/memory).

## Related resources

<CardGroup cols={2}>
  <Card title="Find answers in your docs" href="/docs/claude-tag/users/use-cases/find-answers" horizontal arrow>
    The same connections pointed at a single question
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    How the recurring review runs on a schedule
  </Card>
</CardGroup>
