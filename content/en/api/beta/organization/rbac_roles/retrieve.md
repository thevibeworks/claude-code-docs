---
title: Get RBAC Role
url: https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/retrieve
---

# Get RBAC Role

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

## Path parameters

- `rbac_role_id: string`

  ID of the RBAC Role.

## Returns

- `BetaRBACRole object`

  - `type: "rbac_role"`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    default: rbac_role

  - `id: string`

    ID of the RBAC Role.

  - `created_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `display_name: string`

    Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

  - `name: string`

    **Deprecated**: Use `display_name` instead; `name` always has the same value.

    Deprecated: use `display_name` instead. Name of the RBAC Role; always the same value as `display_name`.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
