---
title: List API Keys
url: https://platform.claude.com/docs/en/api/organization/api_keys/list
---

# List API Keys

**GET** `/v1/organizations/api_keys`

List API Keys

## Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `created_by_user_id: optional string`

  Filter by the ID of the User who created the object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

  - `"active"`

  - `"archived"`

  - `"expired"`

  - `"inactive"`

- `workspace_id: optional string`

  Filter by Workspace ID.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

## Returns

- `data: array of APIKey`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    default: api_key

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: APIKeyCreatedBy or null`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

    - `id: string`

      ID of the actor that created the object.

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string or null`

    Partially redacted hint for the API key.

  - `principal: APIKeyUserActor or APIKeyServiceAccountActor or null`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `APIKeyUserActor object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

        default: user_actor

      - `user_id: string`

        ID of the User the API key acts as.

    - `APIKeyServiceAccountActor object`

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

        default: service_account_actor

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

  - `scope: APIKeyOrganizationScope or APIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `APIKeyOrganizationScope object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

        default: organization

    - `APIKeyWorkspaceScope object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        default: workspace

      - `workspace_id: string`

        ID of the Workspace the API key belongs to, including when it is the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```
