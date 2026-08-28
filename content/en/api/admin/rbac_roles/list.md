# List RBAC Roles

**GET** `/v1/organizations/rbac_roles`

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

## Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

## Returns

- `data: array of RbacRole`

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

- `has_more: boolean`

  Indicates whether there are more results beyond this page.

- `next_page: string or null`

  Opaque cursor for the next page. Pass as the `page` parameter on the next
  request.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```
