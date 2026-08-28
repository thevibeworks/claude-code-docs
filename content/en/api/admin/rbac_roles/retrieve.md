# Get RBAC Role

**GET** `/v1/organizations/rbac_roles/{role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

## Path parameters

- `role_id: string`

  ID of the RBAC Role.

## Returns

- `RbacRole object`

  - `id: string`

    ID of the RBAC Role.

  - `created_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `name: string`

    Name of the RBAC Role.

  - `type: "rbac_role"`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    default: rbac_role

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
