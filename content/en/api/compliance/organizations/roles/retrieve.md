---
title: Get Compliance Role
url: https://platform.claude.com/docs/en/api/compliance/organizations/roles/retrieve
---

# Get Compliance Role

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

## Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Returns

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

## Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```
