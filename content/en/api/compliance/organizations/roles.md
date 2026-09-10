---
title: Roles
url: https://platform.claude.com/docs/en/api/compliance/organizations/roles
---

# Roles

## List Compliance Roles

**GET** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (RFC 3339)

    format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Get Compliance Role

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

- `"x-api-key": optional string`

### Returns

- `id: string`

  Role identifier (tagged ID)

- `created_at: string or null`

  Role creation timestamp (RFC 3339)

  format: date-time

- `description: string`

  Role description

- `name: string`

  Role name

- `updated_at: string or null`

  Role last-updated timestamp (RFC 3339)

  format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

## Domain types

### Role Retrieve Response

- `RoleRetrieveResponse object`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (RFC 3339)

    format: date-time

### Role List Response

- `RoleListResponse object`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (RFC 3339)

    format: date-time

## Roles › Permissions

### List Compliance Role Permissions

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

#### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of permissions

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "claude_code",
      "resource_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "resource_type": "organization"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```
