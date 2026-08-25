# Users

## List organization users

**GET** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

### Path parameters

- `org_uuid: string`

  The organization UUID

### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Headers

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  List of current organization members sorted by organization join date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

    format: date-time

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Domain types

### User List Response

- `UserListResponse object`

  User member information for compliance responses.

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

    format: date-time

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`
