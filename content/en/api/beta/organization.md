# Organization

## Get Current Organization

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

### Returns

- `BetaOrganization object`

  - `id: string`

    ID of the Organization.

    format: uuid

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    default: organization

### Example

```bash
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

## Domain types

### Beta Organization

- `BetaOrganization object`

  - `id: string`

    ID of the Organization.

    format: uuid

  - `name: string`

    Name of the Organization.

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    default: organization

### Beta Organization Role

- `BetaOrganizationRole = "admin" or "billing" or "claude_code_user" or 6 more`

  - `"admin"`

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"membership_admin"`

  - `"owner"`

  - `"primary_owner"`

  - `"user"`

## Organization › API Keys

### List API Keys

**GET** `/v1/organizations/api_keys`

List API Keys

#### Query parameters

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

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

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

### Get API Key

**GET** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

#### Path parameters

- `api_key_id: string`

  ID of the API key.

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

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

### Update API Key

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Path parameters

- `api_key_id: string`

  ID of the API key.

#### Body parameters

- `name: optional string or null`

  Name of the API key.

  maxLength: 500, minLength: 1

- `status: optional "active" or "archived" or "inactive" or null`

  Status of the API key.

  - `"active"`

  - `"archived"`

  - `"inactive"`

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

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

## Organization › External Keys

### Create External Key

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Body parameters

- `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

  - `BetaAWSExternalKeyConfig object`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

      maxLength: 2048

    - `type: "aws"`

    - `region: optional string or null`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: optional string or null`

      **Deprecated**

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `BetaGCPExternalKeyConfig object`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

  - `BetaAzureExternalKeyConfigParam object`

    Azure Key Vault provider configuration.

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

    - `vault_uri: string`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: optional string or null`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `display_name: optional string or null`

  Human-friendly display name.

  maxLength: 255, minLength: 1

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

#### Returns

- `BetaExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `BetaExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `BetaExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `BetaAWSExternalKeyConfig object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `BetaGCPExternalKeyConfig object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `BetaAzureExternalKeyConfig object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    default: external_key

  - `updated_at: string`

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "type": "aws"
          }
        }'
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List External Keys

**GET** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

#### Query parameters

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `data: array of BetaExternalKey`

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `BetaExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `BetaExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `BetaAWSExternalKeyConfig object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `BetaGCPExternalKeyConfig object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `BetaAzureExternalKeyConfig object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    default: external_key

  - `updated_at: string`

    format: date-time

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "attachment": {
        "type": "attached"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "prod-us-key",
      "geo": "us",
      "provider_config": {
        "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        "type": "aws",
        "region": "us-east-1",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

### Get External Key

**GET** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

#### Path parameters

- `external_key_id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `BetaExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `BetaExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `BetaExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `BetaAWSExternalKeyConfig object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `BetaGCPExternalKeyConfig object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `BetaAzureExternalKeyConfig object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    default: external_key

  - `updated_at: string`

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update External Key

**POST** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

#### Path parameters

- `external_key_id: string`

  ID of the External Key.

  maxLength: 2048

#### Body parameters

- `display_name: optional string or null`

  Human-friendly display name.

  maxLength: 255, minLength: 1

- `geo: optional "us" or null`

  Data residency geo. Only `us` is supported.

- `provider_config: optional BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfigParam or null`

  KMS provider identity and auth coordinates.

  - `BetaAWSExternalKeyConfig object`

    - `kms_arn: string`

      Full ARN of the AWS KMS key.

      maxLength: 2048

    - `type: "aws"`

    - `region: optional string or null`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: optional string or null`

      **Deprecated**

      IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

  - `BetaGCPExternalKeyConfig object`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

    - `type: "gcp"`

  - `BetaAzureExternalKeyConfigParam object`

    Azure Key Vault provider configuration.

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `type: "azure"`

    - `vault_uri: string`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: optional string or null`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

#### Returns

- `BetaExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: BetaExternalKeyAttachedAttachment or BetaExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `BetaExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `BetaExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `BetaAWSExternalKeyConfig object`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `type: "aws"`

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `BetaGCPExternalKeyConfig object`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

    - `BetaAzureExternalKeyConfig object`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    default: external_key

  - `updated_at: string`

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete External Key

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

#### Path parameters

- `external_key_id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `id: string`

  ID of the deleted External Key.

- `type: "external_key_deleted"`

  default: external_key_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

### Validate External Key

**POST** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

#### Path parameters

- `external_key_id: string`

  ID of the External Key.

  maxLength: 2048

#### Returns

- `error: string or null`

  Error message when status is `failure`. Null otherwise.

- `status: "failure" or "success"`

  `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

  - `"failure"`

  - `"success"`

- `type: "external_key_validation"`

  default: external_key_validation

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "error": "error",
  "status": "failure",
  "type": "external_key_validation"
}
```

## Organization › Federation › Issuers

### Create Federation Issuer

**POST** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Register an OIDC issuer that Anthropic will trust for workload identity
federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and
takes one of three shapes selected by `type`: `discovery` (resolve keys
through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS
URL), or `inline` (provide a static key set). When `jwks.type` is
`discovery` and no `discovery_base` is set, the issuer URL must be
publicly reachable over HTTPS so Anthropic can fetch the discovery
document; for `explicit_url` and `inline` modes the issuer URL is only
matched as the JWT's `iss` claim and is not fetched.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `issuer_url: string`

  The `iss` claim value to match against.

  minLength: 1

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

  How signing keys are obtained. Defaults to OIDC discovery.

  - `BetaJWKSDiscovery object`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: optional string or null`

      Set when the discovery URL differs from `issuer_url`.

  - `BetaJWKSExplicitURL object`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

    - `url: string`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `BetaJWKSInline object`

    JWKS supplied directly; no network fetch.

    - `keys: array of map[unknown]`

      Inline JWK objects.

      minItems: 1

    - `type: "inline"`

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

#### Returns

- `BetaFederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_url": "x",
          "name": "x"
        }'
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Federation Issuers

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaFederationIssuer`

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Issuer

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaFederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Federation Issuer

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer to update.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `issuer_url: optional string or null`

  Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

  minLength: 1

- `jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline or null`

  Replaces the entire JWKS configuration.

  - `BetaJWKSDiscovery object`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: optional string or null`

      Set when the discovery URL differs from `issuer_url`.

  - `BetaJWKSExplicitURL object`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

    - `url: string`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `BetaJWKSInline object`

    JWKS supplied directly; no network fetch.

    - `keys: array of map[unknown]`

      Inline JWK objects.

      minItems: 1

    - `type: "inline"`

- `jwks_polling_disabled: optional boolean or null`

  Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

- `name: optional string or null`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

#### Returns

- `BetaFederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Federation Issuer

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer to archive.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaFederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Organization › Federation › Rules

### Create Federation Rule

**POST** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist
in the same organization; invalid references are rejected with a 400
error. The workspace reference is validated. Membership is not checked
at rule creation: token exchange resolves a single enabled workspace per
call and is rejected unless the target service account is a member of
that workspace (it is implicitly a member of the default workspace).
Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite,
Terraform Cloud, Google) must constrain tenant identity via an
identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). OAuth callers may only
manage rules whose `oauth_scope` is `workspace:developer` or
`workspace:inference`; other scopes require a Console session.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `issuer_id: string`

  Tagged ID of the federation issuer.

- `match: BetaFederationRuleMatch`

  Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string or null`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: optional map[string] or null`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string or null`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: optional string or null`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `oauth_scope: string`

  Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: BetaServiceAccountTarget`

  Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

  - `service_account_name: optional string or null`

    Service account's display name at read time. Ignored on writes.

- `applies_to_all_workspaces: optional boolean`

  When true, enable this rule for every workspace in the org (including workspaces created later).

- `attributes: optional map[string] or null`

  CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string or null`

  Optional free-text description.

  maxLength: 2000

- `token_lifetime_seconds: optional number`

  Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: optional string or null`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_id": "issuer_id",
          "match": {},
          "name": "x",
          "oauth_scope": "x",
          "target": {
            "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
            "type": "service_account"
          }
        }'
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### List Federation Rules

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `issuer_id: optional string`

  Filter to rules referencing this federation issuer.

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaFederationRule`

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Rule

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Update Federation Rule

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule to update.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `applies_to_all_workspaces: optional boolean or null`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: optional map[string] or null`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string or null`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `match: optional BetaFederationRuleMatch or null`

  Does the incoming JWT qualify?

  All populated fields must pass; omitted fields are skipped. At least one
  of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
  or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string or null`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: optional map[string] or null`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string or null`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: optional string or null`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: optional string or null`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `oauth_scope: optional string or null`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: optional BetaServiceAccountTarget or null`

  Bind to a fixed service account by ID.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

  - `service_account_name: optional string or null`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: optional number or null`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: optional string or null`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Archive Federation Rule

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule to archive.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Organization › Federation › Rules › Workspaces

### Add Federation Rule Workspace

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `workspace_id: string`

  Tagged ID of the workspace to enable this rule for.

#### Returns

- `BetaFederationRuleWorkspace object`

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_id": "workspace_id"
        }'
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

### List Federation Rule Workspaces

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Query parameters

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaFederationRuleWorkspace`

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

- `next_page: string or null`

  Opaque cursor for the next page; null when there are no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Federation Rule Workspace

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

- `workspace_id: string`

  ID of the workspace to disable for.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `federation_rule_id: string`

  Tagged ID of the federation rule.

- `type: "federation_rule_workspace_deleted"`

  default: federation_rule_workspace_deleted

- `workspace_id: string`

  Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

## Organization › Invites

### Create Invite

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Body parameters

- `email: string`

  Email of the User.

  format: email

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

- `rbac_group_ids: optional array of string`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

  maxItems: 100

#### Returns

- `BetaOrganizationInvite object`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string or null`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### List Invites

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: optional string`

  Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

  format: email

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `roles: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

- `statuses: optional array of "accepted" or "expired" or "pending"`

  Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

  - `"accepted"`

  - `"expired"`

  - `"pending"`

#### Returns

- `data: array of BetaOrganizationInvite`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string or null`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "rbac_group_ids": [
        "string"
      ],
      "role": "admin",
      "status": "pending",
      "type": "invite"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get Invite

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Path parameters

- `invite_id: string`

  ID of the Invite.

#### Returns

- `BetaOrganizationInvite object`

  - `id: string`

    ID of the Invite.

  - `accepted_at: string or null`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: string`

    Email of the User being invited.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: string`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: array of string`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: "accepted" or "deleted" or "expired" or "pending"`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### Delete Invite

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Path parameters

- `invite_id: string`

  ID of the Invite.

#### Returns

- `id: string`

  ID of the Invite.

- `type: "invite_deleted"`

  Deleted object type.

  For Invites, this is always `"invite_deleted"`.

  default: invite_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

## Organization › Service Accounts

### Create Service Account

**POST** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `description: optional string or null`

  Optional free-text description.

  maxLength: 2000

- `organization_role: optional "admin" or "developer"`

  Org-level role. Defaults to `developer`.

  - `"admin"`

  - `"developer"`

#### Returns

- `BetaServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string or null`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string or null`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    default: service_account

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "name": "ci-deploy-bot"
        }'
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Service Accounts

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaServiceAccount`

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string or null`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string or null`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    default: service_account

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Service Account

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Path parameters

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string or null`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string or null`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    default: service_account

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Service Account

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Path parameters

- `service_account_id: string`

  ID of the service account to update.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `description: optional string or null`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `organization_role: optional "admin" or "developer" or null`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `"admin"`

  - `"developer"`

#### Returns

- `BetaServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string or null`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string or null`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    default: service_account

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Service Account

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Path parameters

- `service_account_id: string`

  ID of the service account to archive.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string or null`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string or null`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    default: service_account

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Organization › Service Accounts › Workspaces

### Add Workspace To Service Account

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

#### Path parameters

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `workspace_id: string`

  Tagged workspace ID to add the service account to.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `BetaServiceAccountWorkspaceMember object`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_id": "workspace_id",
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### List Workspaces For Service Account

**GET** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that
workspace. Use `limit` and the `next_page` cursor to paginate. When the
service account has no explicit default-workspace membership, the
implicit (`implicit: true`) membership is returned as the first entry on
the first page; with `limit=1` the first page may return up to 2 entries
(the implicit entry plus one explicit membership) so a pagination cursor
can be derived. Memberships are returned only while
the service account is active. Without a `page` cursor, an archived
service account returns an empty list. A `page` cursor that does not
match an active membership returns a 400 invalid-request error. A cursor
stops matching when the membership is removed, the workspace is deleted,
or the service account is archived. Restart pagination from the first
page to recover.

#### Path parameters

- `service_account_id: string`

  ID of the service account.

#### Query parameters

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaServiceAccountWorkspaceMember`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Workspace From Service Account

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Path parameters

- `service_account_id: string`

  ID of the service account.

- `workspace_id: string`

  ID of the workspace.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `type: "service_account_workspace_member_deleted"`

  default: service_account_workspace_member_deleted

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Organization › Users

### List Users

**GET** `/v1/organizations/users`

List the organization's members.

#### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: optional string`

  Filter by user email.

  format: email

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `roles: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `data: array of BetaOrganizationUser`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get User

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Path parameters

- `user_id: string`

  ID of the User.

#### Returns

- `BetaOrganizationUser object`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Update User

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Path parameters

- `user_id: string`

  ID of the User.

#### Body parameters

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

#### Returns

- `BetaOrganizationUser object`

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "role": "user"
        }'
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Remove User

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Path parameters

- `user_id: string`

  ID of the User.

#### Returns

- `id: string`

  ID of the User.

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  default: user_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

## Organization › Workspaces

### List Workspaces

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `include_archived: optional boolean`

  Whether to include Workspaces that have been archived in the response

  default: false

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

#### Returns

- `data: array of BetaWorkspace`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of string`

      - `Unrestricted = "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `name: string`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `data_residency: optional BetaDataResidencyCreateConfig or null`

  Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `allowed_inference_geos: optional array of BetaAllowedInferenceGeo or "unrestricted" or null`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = array of BetaAllowedInferenceGeo`

      - `"global"`

      - `"us"`

    - `Unrestricted = "unrestricted"`

  - `default_inference_geo: optional "global" or "us" or null`

    Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `"global"`

    - `"us"`

  - `workspace_geo: optional "us" or null`

    Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

- `display_color: optional string or null`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: optional string or null`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `tags: optional map[string] or null`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `BetaWorkspace object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of string`

      - `Unrestricted = "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "name": "x",
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Get Workspace

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

#### Returns

- `BetaWorkspace object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of string`

      - `Unrestricted = "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Update Workspace

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Path parameters

- `workspace_id: string`

#### Body parameters

- `data_residency: optional BetaDataResidencyUpdateConfig or null`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: optional array of BetaAllowedInferenceGeo or "unrestricted" or null`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = array of BetaAllowedInferenceGeo`

      - `"global"`

      - `"us"`

    - `Unrestricted = "unrestricted"`

  - `default_inference_geo: optional "global" or "us" or null`

    Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `"global"`

    - `"us"`

- `display_color: optional string`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: optional string`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. This
  field is write-once: once a key is attached to a Workspace it cannot be
  detached or replaced. To rotate key material, rotate the underlying key on
  your cloud KMS; the `external_key_id` stays the same.

- `name: optional string`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `tags: optional map[string] or null`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `BetaWorkspace object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of string`

      - `Unrestricted = "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Archive Workspace

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Path parameters

- `workspace_id: string`

#### Returns

- `BetaWorkspace object`

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of string or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of string`

      - `Unrestricted = "unrestricted"`

    - `default_inference_geo: string`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: string`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Organization › Workspaces › Rate Limits

### List Workspace Rate Limits

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

This endpoint currently returns every matching entry in a single page
regardless of `limit`; follow `next_page` so that clients keep working
when pagination is enabled.

#### Path parameters

- `workspace_id: string`

  The ID of the workspace.

#### Query parameters

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  Accepted for request-shape compatibility and currently ignored: every entry is returned in a single page.

  maximum: 1000, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `data: array of BetaWorkspaceRateLimit`

  Rate-limit entries for the workspace, one per group that has at least one override.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: array of BetaWorkspaceRateLimitValue`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The workspace-level override value for this limiter type.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: string`

    The `id` of the RateLimit group this override applies to.

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `workspace_id: string`

    ID of the Workspace this override applies to.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Workspaces › Members

### List Workspace Members

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

#### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

#### Returns

- `data: array of BetaWorkspaceMember`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace Member

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

#### Body parameters

- `user_id: string`

  ID of the User.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `BetaWorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Get Workspace Member

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

#### Returns

- `BetaWorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Update Workspace Member

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

#### Body parameters

- `workspace_role: BetaWorkspaceRole`

  New workspace role for the User.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `BetaWorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Delete Workspace Member

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

- `user_id: string`

  ID of the User.

#### Returns

- `type: "workspace_member_deleted"`

  Deleted object type.

  For Workspace Members, this is always `"workspace_member_deleted"`.

  default: workspace_member_deleted

- `user_id: string`

  ID of the User.

- `workspace_id: string`

  ID of the Workspace.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Organization › Workspaces › Service Accounts

### List Service Account Workspace Members

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Path parameters

- `workspace_id: string`

  ID of the workspace.

#### Query parameters

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `data: array of BetaServiceAccountWorkspaceMember`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Create Service Account Workspace Member

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

The role determines what the service account can do in the workspace and
which workspace-scoped permissions it can be granted when authenticating
through federation. Every service account is already an implicit
`workspace_user` member of the default workspace; adding it explicitly
assigns a chosen role. If the service account is already an explicit
member of the workspace, its `workspace_role` is replaced with the
value supplied here. Archived workspaces return 400. Archived service
accounts cannot be added and are rejected.

#### Path parameters

- `workspace_id: string`

  ID of the workspace.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `service_account_id: string`

  Tagged service account ID to add.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `BetaServiceAccountWorkspaceMember object`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "service_account_id": "service_account_id",
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Get Service Account Workspace Member

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Path parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `BetaServiceAccountWorkspaceMember object`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Update Service Account Workspace Member

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Path parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Body parameters

- `workspace_role: BetaNoBillingWorkspaceRole`

  New role for the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `BetaServiceAccountWorkspaceMember object`

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Delete Service Account Workspace Member

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Path parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

#### Returns

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `type: "service_account_workspace_member_deleted"`

  default: service_account_workspace_member_deleted

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Organization › Rate Limits

### List Organization Rate Limits

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

This endpoint currently returns every matching entry in a single page
regardless of `limit`; follow `next_page` so that clients keep working
when pagination is enabled.

#### Query parameters

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  Accepted for request-shape compatibility and currently ignored: every entry is returned in a single page.

  maximum: 1000, minimum: 1

- `model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `data: array of BetaOrganizationRateLimit`

  Rate-limit entries for the organization, one per group.

  - `id: string`

    Stable identifier for this rate-limit group within the organization.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: array of BetaOrganizationRateLimitValue`

    The limiter values that apply to this group.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The configured limit value for this limiter type.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `type: "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

    default: rate_limit

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```
