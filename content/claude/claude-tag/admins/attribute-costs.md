> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Attribute costs to users

> Pull channel spend per Slack user from the Usage and Cost Analytics API for showback or chargeback reporting, and see how Claude's work is attributed to people.

> [!NOTE]
>
> Claude Tag is in public beta. Features and behavior described here may change before general availability.

You can pull Claude Tag channel spend broken out by the Slack user Claude did the work for. The [Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api) reports your organization's spend, and grouping its [cost endpoint](https://platform.claude.com/docs/en/api/beta/organization/analytics/cost/list) by `claude_tag_user_id` returns one row per attributed Slack user. Use the rows to attribute spend to people or departments for showback and chargeback reporting.

The Analytics API is available to organizations on a Claude Enterprise plan. To call it, you need an API key with the `read:analytics` scope. Only your organization's primary owner can create that key, at [`claude.ai/admin-settings/api-access`](https://claude.ai/admin-settings/api-access). See [Get access to the Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api#get-access-to-the-claude-enterprise-analytics-api) for the steps.

On the [analytics page](https://claude.ai/analytics/claude-tag) in claude.ai you see spend by channel and by kind of work, not by user. For spend by user, use the cost endpoint.

## Get spend per user

Call `GET /v1/organizations/analytics/cost` with `claude_tag_user_id` in `group_by[]`. The endpoint is in beta, so send the `anthropic-beta: analytics-usage-cost-2026-08-24` header on every request. This example requests one week of spend, one row per user per day:

```bash theme={null}
curl --globoff "https://api.anthropic.com/v1/organizations/analytics/cost?\
starting_at=2026-09-01T00:00:00Z&\
ending_at=2026-09-08T00:00:00Z&\
group_by[]=claude_tag_user_id&\
time_bucket_width=1d&\
products[]=claude-tag&\
limit=1000" \
  --header "anthropic-version: 2023-06-01" \
  --header "anthropic-beta: analytics-usage-cost-2026-08-24" \
  --header "x-api-key: $ANALYTICS_API_KEY"
```

`products[]=claude-tag` limits the report to Claude's usage in Slack, such as Claude's work in channels and [DMs from members who haven't connected a Claude account](https://claude.com/docs/claude-tag/admins/restrict-access.md#direct-messages-from-members-without-a-claude-account). One-to-one DMs from members who have connected a Claude account bill to the sender's own seat and are reported under `claude-tag` too, so this filter includes them.

Each row's `group.claude_tag_user_id` is a Slack user ID such as `U0123ABCDEF`, not a claude.ai user ID. The value can be null: that row is spend with no attributed user, and [How costs map to users](#how-costs-map-to-users) lists those cases. When a response has `has_more` set to `true`, repeat the request with its `next_page` value as the `page` parameter until you have every row. For the full parameters and response schema, see the [cost endpoint reference](https://platform.claude.com/docs/en/api/beta/organization/analytics/cost/list), which also covers grouping by `slack_channel_id` and `claude_tag_category`.

> [!WARNING]
>
> Use `/v1/organizations/analytics/cost` for per-user spend, because `/v1/organizations/analytics/cost_report` can drop people at larger organizations. The `cost_report` endpoint keeps only the top 100 combinations in each time bucket and gives no warning about the rest.

## How costs map to users

Channel spend is attributed to at most one Slack user at a time, by these rules:

* **Work someone asked for goes to the person who asked.** Spend for each of Claude's replies goes to the member whose message Claude was responding to, so when several people address Claude in one thread, the spend is split across them.
* **Work Claude picks up on its own goes to a person in the thread where it did the work.** That person is the member whose message Claude acted on, if there is one. Otherwise it is whoever mentioned Claude into the thread, or, if no one did, the person who started the thread.
* **Scheduled routines go to the person who set the routine up.**
* **The null row collects spend with no attributable person.** Examples are:
  * the [channel session's](https://claude.com/docs/claude-tag/concepts/how-it-works.md#lifecycle-of-a-request) own work, which is `monitoring` spend
  * work Claude started on its own in a thread started by Claude, another app, or a bot, which is `proactive` spend
  * a routine whose creator can't be identified

Per-user rows can therefore sum to less than your Claude Tag total.

Per-user attribution doesn't change billing. Channel work still bills to your organization's usage balance, not to any user's seat. See [Set a spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit.md) for the billing split.

## Related resources

* [Get cost by dimension](https://platform.claude.com/docs/en/api/beta/organization/analytics/cost/list): the cost endpoint's parameters, response schema, and limits
* [Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api): the beta header, data freshness, and moving from `cost_report`
* [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api): key setup, data freshness, and pagination
* [Set a spend limit](https://claude.com/docs/claude-tag/admins/set-spend-limit.md): what bills to the organization's balance versus a user's seat
