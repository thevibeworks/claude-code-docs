# Groups

## List Compliance Groups

**GET** `/v1/compliance/groups`

List Compliance Groups

### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, maximum: 1000, minimum: 1

- `name_prefix: optional string`

  Filter groups by name prefix

  default: ""

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Headers

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  List of groups

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2025-03-12T18:22:41.123456",
      "description": "All members of the engineering organization",
      "name": "Engineering Team",
      "roles": [
        "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
        "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
      ],
      "source_type": "scim",
      "updated_at": "2025-03-14T09:05:17.456789"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Get Compliance Group

**GET** `/v1/compliance/groups/{group_id}`

Get Compliance Group

### Path parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Headers

- `"x-api-key": optional string`

### Returns

- `id: string`

  Group identifier (tagged ID)

- `created_at: string or null`

  Group creation timestamp (ISO 8601)

- `description: string`

  Group description

- `name: string`

  Group name

- `roles: array of string or null`

  Role IDs assigned to this group.

- `source_type: string`

  How the group was created ('direct' or 'scim')

- `updated_at: string or null`

  Group last-updated timestamp (ISO 8601)

### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

## Domain types

### Group List Response

- `GroupListResponse object`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

### Group Retrieve Response

- `GroupRetrieveResponse object`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

## Groups › Members

### List Compliance Group Members

**GET** `/v1/compliance/groups/{group_id}/members`

List Compliance Group Members

#### Path parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of group members

  - `created_at: string or null`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string or null`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```
