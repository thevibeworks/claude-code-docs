> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Attribute costs to users

> Pull channel spend per Slack user from the Claude Enterprise Analytics API for showback or chargeback reporting, and see how Claude's work is attributed to people.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

You can pull Claude Tag channel spend broken out by the Slack user Claude did the work for. The [Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api) reports your organization's spend over time, and grouping its [cost report](https://platform.claude.com/docs/en/api/admin/analytics/cost/list) by `claude_tag_user_id` returns one row per attributed Slack user. Use the rows to attribute spend to people or departments for showback and chargeback reporting.

The Analytics API is available to organizations on a Claude Enterprise plan. To call it, you need an API key with the `read:analytics` scope. Only your organization's primary owner can create that key, at [`claude.ai/admin-settings/api-access`](https://claude.ai/admin-settings/api-access). See [Get access to the Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api#get-access-to-the-claude-enterprise-analytics-api) for the steps.

On the [analytics page](https://claude.ai/analytics/claude-tag) in claude.ai you see spend by channel and by kind of work, not by user. For spend by user, use the cost report.

## Get spend per user

Call the cost report with `claude_tag_user_id` in `group_by[]`. This example requests one week of channel spend, one row per user per day:

```bash theme={null}
curl --globoff "https://api.anthropic.com/v1/organizations/analytics/cost_report?\
starting_at=2026-09-01T00:00:00Z&\
ending_at=2026-09-08T00:00:00Z&\
group_by[]=claude_tag_user_id&\
products[]=claude-tag" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANALYTICS_API_KEY"
```

`products[]=claude-tag` limits the report to Claude's work in Slack channels, which bills to your organization's usage balance. DMs with Claude bill to the sender's own seat and aren't reported under `claude-tag`, so this filter leaves them out.

Each row's `claude_tag_user_id` is a Slack user ID such as `U0123ABCDEF`, not a claude.ai user ID. A row with a null `claude_tag_user_id` is channel spend with no attributed user, and [How costs map to users](#how-costs-map-to-users) lists those cases. For the full parameters, response schema, and data freshness, see the [cost report reference](https://platform.claude.com/docs/en/api/admin/analytics/cost/list), which also covers grouping by `slack_channel_id` and `claude_tag_category`.

## How costs map to users

Channel spend is attributed to at most one Slack user at a time, by these rules:

* **Work someone asked for goes to the person who asked.** Spend for each of Claude's replies goes to the member whose message Claude was responding to, so when several people address Claude in one thread, the spend is split across them.
* **Work Claude picks up on its own goes to a person in the thread where it did the work.** That person is the member whose message Claude acted on, if there is one. Otherwise it is whoever mentioned Claude into the thread, or, if no one did, the person who started the thread.
* **Scheduled routines go to the person who set the routine up.**
* **The null row collects spend with no attributable person.** Examples are work Claude started on its own in a thread that another app or bot posted, and a routine whose creator can't be identified. Monitoring, meaning Claude reading a channel it was asked to watch, is never attributed to a user. Per-user rows therefore sum to less than your total channel spend.

Per-user attribution doesn't change billing. Channel work still bills to your organization's usage balance, not to any user's seat. See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for the billing split.

## Related resources

* [Get cost over time](https://platform.claude.com/docs/en/api/admin/analytics/cost/list): the cost report's parameters, response schema, and limits
* [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api): key setup, data freshness, and pagination
* [Set a spend limit](/docs/claude-tag/admins/set-spend-limit): what bills to the organization's balance versus a user's seat
