# API Keys

## List API Keys

**GET** `/v1/organizations/api_keys`

List API Keys

### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `created_by_user_id: optional string`

  Filter by the ID of the User who created the object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

  - `"active"`

  - `"archived"`

  - `"expired"`

  - `"inactive"`

- `workspace_id: optional string`

  Filter by Workspace ID.

### Returns

- `data: array of BetaAPIKey`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy or null`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string or null`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor or null`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `BetaAPIKeyUserActor object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

        default: user_actor

      - `user_id: string`

        ID of the User the API key acts as.

    - `BetaAPIKeyServiceAccountActor object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

        default: service_account_actor

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `BetaAPIKeyOrganizationScope object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

        default: organization

    - `BetaAPIKeyWorkspaceScope object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        default: workspace

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    default: api_key

  - `workspace_id: string or null`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get API Key

**GET** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

### Path parameters

- `api_key_id: string`

  ID of the API key.

### Returns

- `BetaAPIKey object`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy or null`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string or null`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor or null`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `BetaAPIKeyUserActor object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

        default: user_actor

      - `user_id: string`

        ID of the User the API key acts as.

    - `BetaAPIKeyServiceAccountActor object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

        default: service_account_actor

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `BetaAPIKeyOrganizationScope object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

        default: organization

    - `BetaAPIKeyWorkspaceScope object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        default: workspace

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    default: api_key

  - `workspace_id: string or null`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Update API Key

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

### Path parameters

- `api_key_id: string`

  ID of the API key.

### Body parameters

- `name: optional string or null`

  Name of the API key.

  maxLength: 500, minLength: 1

- `status: optional "active" or "archived" or "inactive" or null`

  Status of the API key.

  - `"active"`

  - `"archived"`

  - `"inactive"`

### Returns

- `BetaAPIKey object`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy or null`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string or null`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor or null`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `BetaAPIKeyUserActor object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

        default: user_actor

      - `user_id: string`

        ID of the User the API key acts as.

    - `BetaAPIKeyServiceAccountActor object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

        default: service_account_actor

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `BetaAPIKeyOrganizationScope object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

        default: organization

    - `BetaAPIKeyWorkspaceScope object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        default: workspace

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    default: api_key

  - `workspace_id: string or null`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Domain types

### Beta API Key

- `BetaAPIKey object`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `created_by: BetaAPIKeyCreatedBy or null`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `id: string`

      ID of the actor that created the object.

    - `type: "service_account" or "user"`

      Type of the actor that created the object.

      - `"service_account"`

      - `"user"`

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string or null`

    Partially redacted hint for the API key.

  - `principal: BetaAPIKeyUserActor or BetaAPIKeyServiceAccountActor or null`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `BetaAPIKeyUserActor object`

      - `type: "user_actor"`

        Principal type. Always `"user_actor"` for a User.

        default: user_actor

      - `user_id: string`

        ID of the User the API key acts as.

    - `BetaAPIKeyServiceAccountActor object`

      - `service_account_id: string`

        ID of the Service Account the API key acts as.

      - `type: "service_account_actor"`

        Principal type. Always `"service_account_actor"` for a Service Account.

        default: service_account_actor

  - `scope: BetaAPIKeyOrganizationScope or BetaAPIKeyWorkspaceScope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `BetaAPIKeyOrganizationScope object`

      - `type: "organization"`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

        default: organization

    - `BetaAPIKeyWorkspaceScope object`

      - `type: "workspace"`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

        default: workspace

      - `workspace_id: string`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    default: api_key

  - `workspace_id: string or null`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

### Beta API Key Created By

- `BetaAPIKeyCreatedBy object`

  - `id: string`

    ID of the actor that created the object.

  - `type: "service_account" or "user"`

    Type of the actor that created the object.

    - `"service_account"`

    - `"user"`

### Beta API Key Organization Scope

- `BetaAPIKeyOrganizationScope object`

  - `type: "organization"`

    Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    default: organization

### Beta API Key Service Account Actor

- `BetaAPIKeyServiceAccountActor object`

  - `service_account_id: string`

    ID of the Service Account the API key acts as.

  - `type: "service_account_actor"`

    Principal type. Always `"service_account_actor"` for a Service Account.

    default: service_account_actor

### Beta API Key User Actor

- `BetaAPIKeyUserActor object`

  - `type: "user_actor"`

    Principal type. Always `"user_actor"` for a User.

    default: user_actor

  - `user_id: string`

    ID of the User the API key acts as.

### Beta API Key Workspace Scope

- `BetaAPIKeyWorkspaceScope object`

  - `type: "workspace"`

    Scope type. Always `"workspace"`: the API key belongs to one Workspace.

    default: workspace

  - `workspace_id: string`

    ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.
