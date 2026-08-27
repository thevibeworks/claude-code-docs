# Retrieve a local session

**GET** `/v1/compliance/apps/sessions/local/{local_session_id}`

Retrieve one local session.

The response is the same session object the list endpoint returns,
with `user.email_address` resolved the same way. Retention is
enforced when the response is served: a session whose every
inference call has aged out returns 404.

## Path parameters

- `local_session_id: string`

## Headers

- `"x-api-key": optional string`

## Returns

- `id: string`

  Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

- `created_at: string`

  Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  format: date-time

- `organization_uuid: string`

  UUID of the child organization the session belongs to

- `product_surface: string or null`

  The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

- `type: "compliance_local_session"`

  default: compliance_local_session

- `updated_at: string`

  Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

  format: date-time

- `user: object`

  The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

  - `id: string`

    User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

  - `email_address: string or null`

    User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

- `workspace_id: string or null`

  Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "type": "compliance_local_session",
  "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
  "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
  "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
  "user": {
    "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
    "email_address": "engineer@example.com"
  },
  "product_surface": "cowork",
  "created_at": "2026-07-09T14:02:11Z",
  "updated_at": "2026-07-09T15:47:33Z"
}
```
