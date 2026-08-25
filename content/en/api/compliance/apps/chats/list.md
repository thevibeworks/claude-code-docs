# List chats

**GET** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by the `order_by` key, with ties broken by id.

**Deprecation notice:** Combining `user_ids[]` with any `updated_at.*`
filter is deprecated and will be rejected with HTTP 400 after
2026-09-22. For incremental polling by update time, omit `user_ids[]`
and set `order_by=updated_at` with `after_id` cursor pagination —
this returns the same chats across the whole organization in a single
request stream. For per-user listing, use `created_at.*` filters (or
no time filter) with the default `order_by`. `user_ids[]` with
`order_by=updated_at` is already rejected.

## Query parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, maximum: 1000, minimum: 1

- `order_by: optional "created_at" or "updated_at"`

  Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids[]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

  default: created_at

  - `"created_at"`

  - `"updated_at"`

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids[]; not supported for org-wide queries.

- `updated_at: optional object`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

- `user_ids: optional array of string`

  Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`. Deprecated combination: passing `user_ids[]` together with any `updated_at.*` filter is deprecated and will be rejected after 2026-09-22. For `updated_at`-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

  maxItems: 10

## Headers

- `"x-api-key": optional string`

## Returns

- `data: array of object`

  List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Deletion timestamp if deleted

    format: date-time

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string or null`

    Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string or null`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

    format: date-time

  - `user: object or null`

    User information for compliance responses.

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization ID this chat belongs to

- `first_id: string or null`

  Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string or null`

  Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-5",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9",
  "last_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9"
}
```
