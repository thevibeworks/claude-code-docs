> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics API

> The Analytics API returns your organization's token usage and estimated cost by day, hour, member, product, or model. A Primary Owner creates the key.

> **Who this is for:** Organization owners and the teams who need their organization's usage and estimated cost in their own tools.

The Analytics API is a read-only HTTP API that returns your organization's token usage and estimated cost, from the same metering as the [Analytics](https://claude.com/docs/government/org-admin/analytics.md) page. It can return figures for each member, with the member's name and email address. It doesn't return conversation content, files, or anything your users type into Claude.

## Get access to the Analytics API

The API is off by default. To start using it:

1. As an Owner or a Primary Owner, go to **Settings > Config** in the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it), expand **Analytics API** under **Admin Console**, turn on its switch, and click **Save changes**.
2. As a [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles), [create an admin API key](https://claude.com/docs/government/org-admin/admin-api-keys.md#create-a-key) with **Usage and cost reports** selected.

A key reads only its own organization, so to cover several organizations, create a key in each. Keys from the tenant admin portal don't read usage.

If **Analytics API** is marked [**Locked by your tenant**](https://claude.com/docs/government/config/overview.md#locks), only a tenant administrator can change it.

## Send a request to the Analytics API

Send a GET request to one of these paths on your Claude for Government host, which is the domain name in the address of your organization admin portal:

* `/gateway-api/v1/organizations/analytics/usage` for token usage
* `/gateway-api/v1/organizations/analytics/cost` for estimated cost

Send your admin API key in the `x-api-key` header. Every request also needs the `anthropic-beta` header while the API is in beta. This request returns token usage for each model:

```http theme={null}
GET https://<claude-for-government-host>/gateway-api/v1/organizations/analytics/usage?starting_at=2026-10-31T00:00:00Z&ending_at=2026-11-07T00:00:00Z&group_by[]=model
x-api-key: <your-admin-api-key>
anthropic-beta: analytics-usage-cost-2026-08-24
```

A response can take close to a minute, so set your client's timeout to at least 60 seconds.

To copy your full address and a sample curl command, go to **Settings > Admin API keys** in the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it) and find **Calling the Analytics API**.

### Query parameters

The `/usage` and `/cost` paths accept these parameters. To give a parameter that ends in `[]` several values, repeat it, as in `products[]=desktop&products[]=m365`. With curl, add `--globoff` so that it doesn't interpret the `[]`.

| Parameter | Description |
| - | - |
| `starting_at` | Required. The start of the range, as an RFC 3339 timestamp with a UTC offset, such as `2026-10-01T00:00:00Z`. It can't be before July 1, 2026, or more than 365 days ago. |
| `ending_at` | The end of the range, not included, so `2026-11-01T00:00:00Z` ends it after October 31. At most 31 days after `starting_at`. Without it, the range ends at the current time or 31 days after `starting_at`, whichever is earlier. Required with `time_bucket_width`. |
| `time_bucket_width` | Splits the rows by UTC day (`1d`) or hour (`1h`). Without it, a row covers the whole range. |
| `group_by[]` | Splits the rows by any of `actor` (the member), `product`, and `model`. Without it, a row is a total. |
| `products[]` | Returns only usage of these products: `desktop` for Claude Desktop, `claude_code` for Claude Code, or `m365` for Claude for Microsoft 365, as in the Analytics page's [**By product**](https://claude.com/docs/government/org-admin/analytics.md#usage) table. |
| `models[]` | Returns only usage of these models, named as in the response. Up to 100. |
| `actor_ids[]` | Returns only usage by these members, given by the `user_id` in the response. Up to 100. |
| `exclude_deleted_users` | `true` leaves out the usage of members who are now deactivated or in another organization, so totals drop. Requires `group_by[]=actor`. |
| `order_by` | What to sort by. For usage, `total_tokens` (the default), `output_tokens`, `uncached_input_tokens`, or `requests`. For cost, `amount`. For either, `time`, which takes effect only with `time_bucket_width`. |
| `order` | `desc` (the default) or `asc`. For rows in date order, use `order_by=time` and `order=asc`. |
| `limit` | Rows per page, from 1 to 1000. The default is 20. |
| `page` | The `next_page` value from the page before. See [Read every page of results](#read-every-page-of-results). |

A misspelled model or member ID returns no rows, not an error.

Daily rows run from midnight to midnight UTC, whatever offset you send. The API rounds both ends of the range down, to midnight UTC for daily rows and to the hour otherwise. To include today in daily rows, set `ending_at` to tomorrow's date at `00:00:00Z`.

## Read the response

Each row in `data` covers one period and one combination of the fields you group by. A day, hour, member, product, or model with no usage has no row. Count a missing row as zero if its period ends at or before `data_refreshed_at`. This is a response to the [example request](#send-a-request-to-the-analytics-api), shortened to one row and three of the `group` fields:

```json theme={null}
{
  "data": [
    {
      "starting_at": "2026-10-31T00:00:00Z",
      "ending_at": "2026-11-07T00:00:00Z",
      "group": {
        "product": null,
        "model": "claude-sonnet-4-5",
        "actor": null
      },
      "usage": {
        "uncached_input_tokens": 297877,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 458327
        },
        "cache_read_input_tokens": 5718706,
        "output_tokens": 166493,
        "total_tokens": 6641403,
        "server_tool_use": {
          "web_search_requests": 0
        },
        "requests": 124
      }
    }
  ],
  "has_more": false,
  "next_page": null,
  "data_refreshed_at": "2026-11-07T04:00:00Z"
}
```

A row from `/cost` has `cost` in place of `usage`. This one, shortened the same way, is from a request with `group_by[]=actor`:

```json theme={null}
{
  "starting_at": "2026-10-31T00:00:00Z",
  "ending_at": "2026-11-07T00:00:00Z",
  "group": {
    "product": null,
    "model": null,
    "actor": {
      "type": "user_actor",
      "user_id": "usr_00000000-0000-0000-0000-000000000000",
      "name": "Carol Demo",
      "email_address": "carol@agency.example.com",
      "deleted": false
    }
  },
  "cost": {
    "currency": "USD",
    "amount": "288.678000",
    "list_amount": "288.678000",
    "requests": 73
  }
}
```

`amount` is in US cents, so `"288.678000"` is about \$2.89.

The usage and cost responses have these fields.

| Field | Description |
| - | - |
| `starting_at`, `ending_at` | The period the row covers, in UTC. |
| `group` | What the row is split by. A field is `null` if you don't group by it, or if the usage has no value for it. The fields in `group` that the examples leave out are `null`. |
| `group.actor` | The member. `deleted` is `true` once a member is deactivated or moved to another organization. After a move, `name` and `email_address` are `null`, and `user_id` stays. |
| `uncached_input_tokens` | Input tokens neither read from nor written to the prompt cache. |
| `cache_creation` | Input tokens written to the prompt cache, split into 5-minute and 1-hour cache writes. |
| `cache_read_input_tokens` | Input tokens read from the prompt cache. |
| `output_tokens` | Tokens that Claude generated. |
| `total_tokens` | Input and output tokens together, including input written to or read from the prompt cache. |
| `server_tool_use` | `web_search_requests` is `0`. |
| `requests` | Requests that reached Claude, including ones that were canceled or that ended in an error. |
| `amount`, `list_amount` | Estimated cost in US cents, as a string. `list_amount` equals `amount`. |
| `has_more`, `next_page` | Whether more rows remain, and the value of `page` that reads them. See [Read every page of results](#read-every-page-of-results). |
| `data_refreshed_at` | The time the figures run up to, as described under [How current the figures are](#how-current-the-figures-are). |

### What the estimated cost covers

`amount` covers usage on [self-managed tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers). It is an estimate, not your invoice.

> [!NOTE]
>
> **Anthropic-managed tiers.** If your agency buys seats, usage on those tiers is covered by the seat price, so it adds `0` to `amount`. The API's token and request figures still include it, and the [Analytics](https://claude.com/docs/government/org-admin/analytics.md) page shows these tiers separately.

### When totals differ from the Analytics page

A total can differ from the one on the [Analytics](https://claude.com/docs/government/org-admin/analytics.md) page for these reasons:

* **Anthropic-managed tiers**: see [What the estimated cost covers](#what-the-estimated-cost-covers).
* **Cached input**: `total_tokens` includes input written to or read from the prompt cache, and the page's token figures don't. The page's input tokens are `uncached_input_tokens`.
* **Time**: the page shows times in your browser's time zone and includes the latest usage.

### How current the figures are

The figures are one to two hours behind, and run up to `data_refreshed_at`. For example, a request sent at 15:30 UTC returns usage up to 14:00. When a row's `ending_at` is later than `data_refreshed_at`, the row covers only part of its period, so read it again later. When `data_refreshed_at` is `null`, no usage in the range is available yet.

A request to Claude is counted when it ends, in the hour it started, so an hour's figures can still rise after you read them.

### Read every page of results

While `has_more` is `true`, send the same request again with `page` set to the value of `next_page`. Without `page`, you get the first page again. Send the other parameters as they were. You can change `limit`.

For example, this query reads every member's usage for October, 1,000 members at a time:

```text theme={null}
?group_by[]=actor&limit=1000&starting_at=2026-10-01T00:00:00Z&ending_at=2026-11-01T00:00:00Z
```

For the next 1,000, add `&page=` and the value of `next_page`.

## Rate limits

An organization can send about 60 requests per minute, across all its keys, and four at the same time. A request over either limit returns a 429 error.

## Troubleshoot errors

An error response is JSON. Its `error` object has a `message`, and can have a `code` and a `request_id` to give your Anthropic representative.

| Status | Message or code | What to do |
| - | - | - |
| 400 | `The analytics API is not enabled for this organization.` | Turn on the [**Analytics API**](https://claude.com/docs/government/config/settings.md#analytics-api) setting. |
| 400 | `beta_header_required` | Send the `anthropic-beta` header. |
| 400 | `Extra inputs are not permitted` | Check the name of the parameter, including its `[]`. |
| 400 | `cursor_param_mismatch` | Start again from the first page, without `page`. |
| 400 | `query_too_large` | Use a shorter range. |
| 401 | `x-api-key header is required` | Send the key in the `x-api-key` header. A key sent as `Authorization: Bearer` isn't read, so set the header yourself if your client or SDK sends only that. |
| 401 | `invalid or revoked admin API key` | Check the key, or [create a new one](https://claude.com/docs/government/org-admin/admin-api-keys.md#create-a-key). |
| 403 | `missing_scope` | Use a key from the organization's **Admin API keys** page that was created with **Usage and cost reports**. |
| 403 | `tenant_restriction_violation` | See [Tenant restrictions](https://claude.com/docs/government/tenant-admin/tenant-restrictions.md). |
| 404 | `no such Analytics API endpoint` | Use a path that ends in `/usage` or `/cost`. |
| 414 | `Request URL is over 8 KiB or has more than 256 query parameters` | Send fewer values, in several requests. |
| 429 or 503 | `rate_limited`, `too_many_in_flight`, or `reports_unavailable` | Wait the number of seconds in the `Retry-After` header and try again. |
| 504 | `query_timeout` | Use a shorter range, or group by fewer fields. |
