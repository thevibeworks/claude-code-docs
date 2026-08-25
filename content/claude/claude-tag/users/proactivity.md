> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up routines

> Claude Tag runs routines you set up from the channel. See scheduled jobs, channel watching, pull request subscriptions, paste-ready routine recipes, and how to list or pause standing work.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

You can give Claude standing work from any channel it's in. This standing work is called a routine: a job that runs on a schedule, such as watching a channel, following a pull request, or posting status updates. You set a routine up in the channel where it should run, and it uses that channel's connections with the same permissions as a typed request.

## Set up standing work

### Scheduled jobs

Describe the schedule you want and the work Claude should do in one message:

```text wrap theme={null}
@Claude every weekday at 9am, read the open threads in this channel, check the tickets and pull requests linked in them, and post a one-line status per item. Skip anything with a ✅ reaction.
```

Name the output format in the job so recurring posts stay scannable.

### Watch channels

Ask Claude to watch named channels and post here when something matches a topic:

```text wrap theme={null}
@Claude watch #product-announce, #eng-announce, and #design-announce. Once a day, post here if anything is relevant to user education. Skip days with nothing.
```

Naming both the channels and the topic is what keeps a watch useful. The watch can cover this channel too ("keep an eye on this channel and post a morning summary").

### Follow a pull request

Claude can subscribe to a single pull request and react when it updates. A subscription is the one way Claude reacts to GitHub events; it wakes on activity on that pull request, such as a comment, a failed check, or a merge. You can't set up a routine from Slack that fires on other repository events, such as every new pull request.

```text wrap theme={null}
@Claude subscribe to PR #482 in acme/data-pipeline. When CI finishes or a review lands, post here, and tag me if anything failed.
```

## Routine recipes

Each recipe below sets up a complete routine with one message. Adapt the channel names, repositories, and times to your own, and name the timezone so the schedule fires when you expect.

### Daily standup summary

Claude posts a morning rollup of open threads and anything waiting on someone, before the team starts the day.

```text wrap theme={null}
@Claude every weekday at 9am Pacific, post a summary of open threads in this channel and anything that looks like it's waiting on someone.
```

"Waiting on someone" makes the rollup surface actions, not just a recap; [Catch up](/docs/claude-tag/users/use-cases/catch-up) has the one-off version.

### Weekly channel digest

Claude posts one recap at the end of each week, so the channel has a single place to see what happened.

```text wrap theme={null}
@Claude every Friday at 3pm Eastern, post a digest of this week in this channel: what got decided, what's still open, and anything waiting on someone.
```

For an intake channel, the [Triage requests](/docs/claude-tag/users/use-cases/triage-requests) version of this rollup also sweeps posts that never tagged Claude.

### Watch a pull request until it merges

Claude subscribes to a single pull request and posts as it moves through CI, review, and merge.

```text wrap theme={null}
@Claude subscribe to PR #482 in acme/data-pipeline. Post here when CI finishes, a review lands, or it merges, and tag me if anything failed.
```

[Follow a pull request](#follow-a-pull-request) explains what the subscription reacts to.

### Alert investigation when a monitor fires

Claude checks the alerting dashboard on a schedule and posts a first pass at diagnosis for anything new, so the investigation is underway before anyone asks. This recipe needs a monitoring connection such as Datadog or PagerDuty; [Watch monitors and alerts](/docs/claude-tag/users/use-cases/watch-monitors) has the full setup.

```text wrap theme={null}
@Claude every two hours, check the alerting dashboard against its last state. For anything new, post when it started, what changed around then, and what to look at first.
```

The routine posts only when something changed, not on every check.

### Automatic triage for new requests

Claude answers, deduplicates, and routes requests as they arrive. This recipe is a standing role rather than a schedule; "remember for this channel" saves it to [channel memory](/docs/claude-tag/users/memory), so it applies to everyone's threads.

```text wrap theme={null}
@Claude remember for this channel: when someone tags you on a request, check whether it duplicates something already reported, answer it directly if the answer exists, and otherwise route it to the right owner with a one-line summary.
```

Pair it with a weekly rollup so untagged posts are still swept; [Triage requests](/docs/claude-tag/users/use-cases/triage-requests) has both messages.

## Manage standing work

Anyone in the channel can list, edit, or disable its standing work:

* **List.** Ask "what routines do you have set up in this channel?", or send [`@Claude !routines`](/docs/claude-tag/users/commands#list-the-routines-in-a-channel). Add a channel mention or its ID, as in `@Claude !routines #other-channel`, to list another channel's routines; pick the channel from Slack's autocomplete so it lands as a real mention, since a typed name on its own isn't accepted.
* **Edit.** Describe the change and it updates the job
* **Disable.** Name the job to stop, as in "disable the Friday rollup"

Standing work is visible to the channel: jobs post into the channel they belong to, or into another public channel you name that Claude has been added to. Routines keep running if their creator leaves the organization, but stop firing if the creator is removed from the channel.

A few boundaries apply:

* A job runs with the channel's connections, the same as an interactive request.
* Claude can post a job's output into another public channel in the same workspace only if the job's own channel is public and Claude has been added to the target channel. It labels the message with the channel it came from.
* Claude doesn't post job output to private channels, DMs, group DMs, or externally shared channels, and doesn't message people directly. The one exception is the completion or failure notice it sends to whoever set up the routine, and only when that person's Slack account is connected to their Claude account.
* Schedules default to UTC. When you say "every weekday at 9am," include the timezone (for example "9am Pacific") so Claude converts correctly; without one it may guess. Ask "what triggers do you have set up?" to confirm the time it actually scheduled.
* A scheduled job that touches a github.com repository uses the same GitHub connection your admin set up for interactive work. See [Configure GitHub access](/docs/claude-tag/admins/configure-github#scheduled-work-uses-the-same-connection).

## Related resources

* [Use case library](/docs/claude-tag/users/use-cases): every entry has a proactive form to copy
* [Prompt library](/docs/claude-tag/users/prompt-library#manage-routines): prompts to create, audit, and stop routines
* [Good habits](/docs/claude-tag/users/good-habits): write schedules that keep working
