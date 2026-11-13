---
title: Organization
url: https://platform.claude.com/docs/en/api/organization
---

# Organization

## Get Current Organization

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Returns

- `OrganizationInfo object`

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    default: organization

  - `id: string`

    ID of the Organization.

    format: uuid

  - `name: string`

    Name of the Organization.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

### Concurrent Membership Change Error Details

- `ConcurrentMembershipChangeErrorDetails object`

  Another change to the organization's members is in progress. Retry the request once it completes.

  - `error_code: "concurrent_membership_change"`

### Org Member Limit Exceeded Error Details

- `OrgMemberLimitExceededErrorDetails object`

  The organization has reached the member limit that Anthropic set for it. Pending invites count toward the limit.

  - `error_code: "org_member_limit_exceeded"`

### Organization Info

- `OrganizationInfo object`

  - `type: "organization"`

    Object type.

    For Organizations, this is always `"organization"`.

    default: organization

  - `id: string`

    ID of the Organization.

    format: uuid

  - `name: string`

    Name of the Organization.

### Organization Role

- `OrganizationRole = "admin" or "billing" or "claude_code_user" or 6 more`

  - `"admin"`

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"membership_admin"`

  - `"owner"`

  - `"primary_owner"`

  - `"user"`

### RBAC Role Not Found Error Details

- `RBACRoleNotFoundErrorDetails object`

  No RBAC Role with this ID was found.

  - `error_code: "rbac_role_not_found"`

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

  default: 20, minimum: 1, maximum: 1000

- `status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

  - `"active"`

  - `"archived"`

  - `"expired"`

  - `"inactive"`

- `workspace_id: optional string`

  Filter by Workspace ID.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

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

### Retrieve API Key (Admin API)

**GET** `/v1/organizations/api_keys/{api_key_id}`

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](https://platform.claude.com/settings/keys) in the Claude Console.

#### Path parameters

- `api_key_id: string`

  ID of the API key.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `APIKey object`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
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
```

### Update API Key

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Path parameters

- `api_key_id: string`

  ID of the API key.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `name: optional string or null`

  Name of the API key.

  minLength: 1, maxLength: 500

- `status: optional "active" or "archived" or "inactive" or null`

  Status of the API key.

  - `"active"`

  - `"archived"`

  - `"inactive"`

#### Returns

- `APIKey object`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
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
```

## Organization › External Keys

### Create External Key

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `provider_config: AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

  - `AWSExternalKeyConfig object`

    - `type: "aws"`

    - `kms_arn: string`

      Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

      maxLength: 2048

    - `region: optional string or null`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: optional string or null`

      **Deprecated**

      IAM role ARN. Deprecated; this field is ignored.

  - `GCPExternalKeyConfig object`

    - `type: "gcp"`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

  - `AzureExternalKeyConfigParam object`

    Azure Key Vault provider configuration.

    - `type: "azure"`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `vault_uri: string`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: optional string or null`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

- `display_name: optional string or null`

  Human-friendly display name.

  minLength: 1, maxLength: 255

- `geo: optional "us"`

  Data residency geo. Only `us` is supported.

- `user_profile_id: optional string or null`

  ID of a user profile to bind the key to. A user profile represents one of your customers: bind a customer's key to that customer's user profile. A key bound to a user profile can only be attached to a Workspace that has the same user profile, and the binding cannot be changed later. Omit this field only for your organization's own key, because a key created without a user profile ID can be attached to any Workspace, including another customer's.

#### Returns

- `ExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: "external_key"`

    default: external_key

  - `id: string`

    Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.

  - `attachment: ExternalKeyAttachedAttachment or ExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `ExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `ExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects the region this key is used in.

  - `provider_config: AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `AWSExternalKeyConfig object`

      - `type: "aws"`

      - `kms_arn: string`

        Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

        maxLength: 2048

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated; this field is ignored.

    - `GCPExternalKeyConfig object`

      - `type: "gcp"`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

    - `AzureExternalKeyConfig object`

      - `type: "azure"`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: string`

    format: date-time

  - `user_profile_id: string or null`

    ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can be attached to a Workspace whatever its user profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "type": "aws"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of ExternalKey`

  - `type: "external_key"`

    default: external_key

  - `id: string`

    Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.

  - `attachment: ExternalKeyAttachedAttachment or ExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `ExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `ExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects the region this key is used in.

  - `provider_config: AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `AWSExternalKeyConfig object`

      - `type: "aws"`

      - `kms_arn: string`

        Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

        maxLength: 2048

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated; this field is ignored.

    - `GCPExternalKeyConfig object`

      - `type: "gcp"`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

    - `AzureExternalKeyConfig object`

      - `type: "azure"`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: string`

    format: date-time

  - `user_profile_id: string or null`

    ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can be attached to a Workspace whatever its user profile.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `ExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: "external_key"`

    default: external_key

  - `id: string`

    Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.

  - `attachment: ExternalKeyAttachedAttachment or ExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `ExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `ExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects the region this key is used in.

  - `provider_config: AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `AWSExternalKeyConfig object`

      - `type: "aws"`

      - `kms_arn: string`

        Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

        maxLength: 2048

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated; this field is ignored.

    - `GCPExternalKeyConfig object`

      - `type: "gcp"`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

    - `AzureExternalKeyConfig object`

      - `type: "azure"`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: string`

    format: date-time

  - `user_profile_id: string or null`

    ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can be attached to a Workspace whatever its user profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `display_name: optional string or null`

  Human-friendly display name.

  minLength: 1, maxLength: 255

- `geo: optional "us" or null`

  Data residency geo. Only `us` is supported.

- `provider_config: optional AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfigParam or null`

  KMS provider identity and auth coordinates.

  - `AWSExternalKeyConfig object`

    - `type: "aws"`

    - `kms_arn: string`

      Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

      maxLength: 2048

    - `region: optional string or null`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: optional string or null`

      **Deprecated**

      IAM role ARN. Deprecated; this field is ignored.

  - `GCPExternalKeyConfig object`

    - `type: "gcp"`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

  - `AzureExternalKeyConfigParam object`

    Azure Key Vault provider configuration.

    - `type: "azure"`

    - `key_name: string`

      Name of the key within the vault.

    - `tenant_id: string`

      Azure AD tenant ID.

    - `vault_uri: string`

      Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

    - `client_id: optional string or null`

      Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

#### Returns

- `ExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: "external_key"`

    default: external_key

  - `id: string`

    Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.

  - `attachment: ExternalKeyAttachedAttachment or ExternalKeyUnattachedAttachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `ExternalKeyAttachedAttachment object`

      - `type: "attached"`

        default: attached

    - `ExternalKeyUnattachedAttachment object`

      - `type: "unattached"`

        default: unattached

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects the region this key is used in.

  - `provider_config: AWSExternalKeyConfig or GCPExternalKeyConfig or AzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `AWSExternalKeyConfig object`

      - `type: "aws"`

      - `kms_arn: string`

        Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

        maxLength: 2048

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated; this field is ignored.

    - `GCPExternalKeyConfig object`

      - `type: "gcp"`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

    - `AzureExternalKeyConfig object`

      - `type: "azure"`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `vault_uri: string`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `updated_at: string`

    format: date-time

  - `user_profile_id: string or null`

    ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can be attached to a Workspace whatever its user profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "external_key_deleted"`

  default: external_key_deleted

- `id: string`

  ID of the deleted External Key.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "external_key_validation"`

  default: external_key_validation

- `error: string or null`

  Error message when status is `failure`. Null otherwise.

- `status: "failure" or "success"`

  `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

  - `"failure"`

  - `"success"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `issuer_url: string`

  The `iss` claim value to match against.

  minLength: 1

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `jwks: optional JWKSDiscovery or JWKSExplicitURL or JWKSInline`

  How signing keys are obtained. Defaults to OIDC discovery.

  - `JWKSDiscovery object`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: optional string or null`

      Set when the discovery URL differs from `issuer_url`.

  - `JWKSExplicitURL object`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

    - `url: string`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `JWKSInline object`

    JWKS supplied directly; no network fetch.

    - `type: "inline"`

    - `keys: array of map[unknown]`

      Inline JWK objects.

      minItems: 1

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  minimum: 1, maximum: 176400

#### Returns

- `FederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: "federation_issuer"`

    default: federation_issuer

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

  - `jwks: JWKSDiscovery or JWKSExplicitURL or JWKSInline`

    How signing keys are obtained for signature verification.

    - `JWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `JWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `JWKSInline object`

      JWKS supplied directly; no network fetch.

      - `type: "inline"`

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: FederationIssuerPollStatus or null`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `limit: optional number`

  Number of results per page.

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of FederationIssuer`

  - `type: "federation_issuer"`

    default: federation_issuer

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

  - `jwks: JWKSDiscovery or JWKSExplicitURL or JWKSInline`

    How signing keys are obtained for signature verification.

    - `JWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `JWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `JWKSInline object`

      JWKS supplied directly; no network fetch.

      - `type: "inline"`

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: FederationIssuerPollStatus or null`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `FederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: "federation_issuer"`

    default: federation_issuer

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

  - `jwks: JWKSDiscovery or JWKSExplicitURL or JWKSInline`

    How signing keys are obtained for signature verification.

    - `JWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `JWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `JWKSInline object`

      JWKS supplied directly; no network fetch.

      - `type: "inline"`

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: FederationIssuerPollStatus or null`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `issuer_url: optional string or null`

  Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

  minLength: 1

- `jwks: optional JWKSDiscovery or JWKSExplicitURL or JWKSInline or null`

  Replaces the entire JWKS configuration.

  - `JWKSDiscovery object`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: optional string or null`

      Set when the discovery URL differs from `issuer_url`.

  - `JWKSExplicitURL object`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

    - `url: string`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `JWKSInline object`

    JWKS supplied directly; no network fetch.

    - `type: "inline"`

    - `keys: array of map[unknown]`

      Inline JWK objects.

      minItems: 1

- `jwks_polling_disabled: optional boolean or null`

  Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  minimum: 1, maximum: 176400

- `name: optional string or null`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

#### Returns

- `FederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: "federation_issuer"`

    default: federation_issuer

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

  - `jwks: JWKSDiscovery or JWKSExplicitURL or JWKSInline`

    How signing keys are obtained for signature verification.

    - `JWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `JWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `JWKSInline object`

      JWKS supplied directly; no network fetch.

      - `type: "inline"`

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: FederationIssuerPollStatus or null`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer to archive.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `FederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `type: "federation_issuer"`

    default: federation_issuer

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

  - `jwks: JWKSDiscovery or JWKSExplicitURL or JWKSInline`

    How signing keys are obtained for signature verification.

    - `JWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `JWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `JWKSInline object`

      JWKS supplied directly; no network fetch.

      - `type: "inline"`

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: FederationIssuerPollStatus or null`

    Live state of Anthropic's JWKS polling for this issuer. Populated on both single-issuer retrieval and list responses, including archived issuers. Typically null for inline-key issuers (no polling), or when poll status is temporarily unavailable or polling has not started yet.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `issuer_id: string`

  Tagged ID of the federation issuer.

- `match: FederationRuleMatch`

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

  minLength: 1, maxLength: 255

- `oauth_scope: string`

  Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: ServiceAccountTarget`

  Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `type: "service_account"`

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

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

  minimum: 60, maximum: 86400

- `workspace_id: optional string or null`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

#### Returns

- `FederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: "federation_rule"`

    default: federation_rule

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

  - `match: FederationRuleMatch`

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

  - `target: ServiceAccountTarget`

    What this rule targets. Check `type` before reading the other fields. Tokens minted via a rule whose target `type` is `service_account` act as that service account.

    - `type: "service_account"`

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of FederationRule`

  - `type: "federation_rule"`

    default: federation_rule

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

  - `match: FederationRuleMatch`

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

  - `target: ServiceAccountTarget`

    What this rule targets. Check `type` before reading the other fields. Tokens minted via a rule whose target `type` is `service_account` act as that service account.

    - `type: "service_account"`

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `FederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: "federation_rule"`

    default: federation_rule

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

  - `match: FederationRuleMatch`

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

  - `target: ServiceAccountTarget`

    What this rule targets. Check `type` before reading the other fields. Tokens minted via a rule whose target `type` is `service_account` act as that service account.

    - `type: "service_account"`

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `applies_to_all_workspaces: optional boolean or null`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: optional map[string] or null`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string or null`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `match: optional FederationRuleMatch or null`

  Replaces the entire match object. All populated matcher fields must pass.

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

  minLength: 1, maxLength: 255

- `oauth_scope: optional string or null`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: optional ServiceAccountTarget or null`

  Replaces the entire target object. Currently always a `service_account` target.

  - `type: "service_account"`

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `service_account_name: optional string or null`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: optional number or null`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  minimum: 60, maximum: 86400

- `workspace_id: optional string or null`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

#### Returns

- `FederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: "federation_rule"`

    default: federation_rule

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

  - `match: FederationRuleMatch`

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

  - `target: ServiceAccountTarget`

    What this rule targets. Check `type` before reading the other fields. Tokens minted via a rule whose target `type` is `service_account` act as that service account.

    - `type: "service_account"`

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `FederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: "federation_rule"`

    default: federation_rule

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

  - `match: FederationRuleMatch`

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

  - `target: ServiceAccountTarget`

    What this rule targets. Check `type` before reading the other fields. Tokens minted via a rule whose target `type` is `service_account` act as that service account.

    - `type: "service_account"`

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `workspace_id: string`

  Tagged ID of the workspace to enable this rule for.

#### Returns

- `FederationRuleWorkspace object`

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of FederationRuleWorkspace`

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

- `next_page: string or null`

  Opaque cursor for the next page; null when there are no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "federation_rule_workspace_deleted"`

  default: federation_rule_workspace_deleted

- `federation_rule_id: string`

  Tagged ID of the federation rule.

- `workspace_id: string`

  Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `email: string`

  Email of the User.

  format: email

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`; inviting with the `managed` role requires the `write:rbac_groups` scope in addition to `write:members`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

- `rbac_group_ids: optional array of string`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

  maxItems: 100

#### Returns

- `OrganizationInvite object`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

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

  - `role: OrganizationRole`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

  default: 20, minimum: 1, maximum: 1000

- `roles: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

- `statuses: optional array of "accepted" or "expired" or "pending"`

  Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

  - `"accepted"`

  - `"expired"`

  - `"pending"`

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of OrganizationInvite`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

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

  - `role: OrganizationRole`

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

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `OrganizationInvite object`

  - `type: "invite"`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

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

  - `role: OrganizationRole`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "invite_deleted"`

  Deleted object type.

  For Invites, this is always `"invite_deleted"`.

  default: invite_deleted

- `id: string`

  ID of the Invite.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  minLength: 1, maxLength: 255

- `description: optional string or null`

  Optional free-text description.

  maxLength: 2000

- `organization_role: optional "admin" or "developer"`

  Org-level role. Defaults to `developer`.

  - `"admin"`

  - `"developer"`

#### Returns

- `ServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: "service_account"`

    default: service_account

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

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of ServiceAccount`

  - `type: "service_account"`

    default: service_account

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Retrieve a service account by its ID (`svac_...`).

#### Path parameters

- `service_account_id: string`

  ID of the service account.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `ServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: "service_account"`

    default: service_account

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

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Path parameters

- `service_account_id: string`

  ID of the service account to update.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `description: optional string or null`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `organization_role: optional "admin" or "developer" or null`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `"admin"`

  - `"developer"`

#### Returns

- `ServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: "service_account"`

    default: service_account

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

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Path parameters

- `service_account_id: string`

  ID of the service account to archive.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `ServiceAccount object`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: "service_account"`

    default: service_account

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

  - `updated_at: string`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/archive \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `workspace_id: string`

  Tagged workspace ID to add the service account to.

- `workspace_role: NoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `ServiceAccountWorkspaceMember object`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of ServiceAccountWorkspaceMember`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "service_account_workspace_member_deleted"`

  default: service_account_workspace_member_deleted

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

  default: 20, minimum: 1, maximum: 1000

- `roles: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of OrganizationUser`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: OrganizationRole`

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

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `OrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: OrganizationRole`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`; changing a User's role to `managed` requires the `write:rbac_groups` scope in addition to `write:members`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

#### Returns

- `OrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: OrganizationRole`

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "role": "user"
        }'
```

##### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  default: user_deleted

- `id: string`

  ID of the User.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

- `ids: optional array of string`

  Only the Workspaces with these IDs, at most 100. `include_archived` and `include_default` still apply, and IDs of Workspaces the caller can't list are left out.

- `include_archived: optional boolean`

  Whether to include Workspaces that have been archived in the response

  default: false

- `include_default: optional boolean`

  Whether to include the organization's default Workspace in the response

  default: false

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of Workspace`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: DataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of AllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of AllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same AWS account and
    Region as the Workspace. On that platform the key is validated against this
    Workspace when it is attached, so a key-policy problem is reported as an error
    on this request. This field is write-once: once a key is attached to a Workspace
    it cannot be detached or replaced. To rotate key material, rotate the underlying
    key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
        "default_inference_geo": "global",
        "workspace_geo": "us"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace",
      "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `name: string`

  Name of the Workspace.

  minLength: 1, maxLength: 255

- `data_residency: optional DataResidencyCreateConfig or null`

  Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `allowed_inference_geos: optional array of AllowedInferenceGeo or "unrestricted" or null`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = array of AllowedInferenceGeo`

      - `"global"`

      - `"us"`

    - `"unrestricted"`

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
  referenced key. Create key configurations with the External Keys API. On
  Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
  organization's own key must be a single-Region key in the same AWS account and
  Region as the Workspace. On that platform the key is validated against this
  Workspace when it is attached, so a key-policy problem is reported as an error
  on this request. This field is write-once: once a key is attached to a Workspace
  it cannot be detached or replaced. To rotate key material, rotate the underlying
  key on your cloud KMS; the `external_key_id` stays the same.

- `tags: optional map[string] or null`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `user_profile_id: optional string or null`

  ID of a user profile to attach to the Workspace. Every inference request through the Workspace must then name this user profile; the API rejects a request that names none or a different one. The user profile can't be replaced or removed later; only deleting the user profile clears it.

#### Returns

- `Workspace object`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: DataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of AllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of AllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same AWS account and
    Region as the Workspace. On that platform the key is validated against this
    Workspace when it is attached, so a key-policy problem is reported as an error
    on this request. This field is write-once: once a key is attached to a Workspace
    it cannot be detached or replaced. To rotate key material, rotate the underlying
    key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "x",
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```

### Get Workspace

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Path parameters

- `workspace_id: string`

  ID of the Workspace.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `Workspace object`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: DataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of AllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of AllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same AWS account and
    Region as the Workspace. On that platform the key is validated against this
    Workspace when it is attached, so a key-policy problem is reported as an error
    on this request. This field is write-once: once a key is attached to a Workspace
    it cannot be detached or replaced. To rotate key material, rotate the underlying
    key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```

### Update Workspace

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Path parameters

- `workspace_id: string`

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `data_residency: optional DataResidencyUpdateConfig or null`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: optional array of AllowedInferenceGeo or "unrestricted" or null`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = array of AllowedInferenceGeo`

      - `"global"`

      - `"us"`

    - `"unrestricted"`

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
  referenced key. Create key configurations with the External Keys API. On
  Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
  organization's own key must be a single-Region key in the same AWS account and
  Region as the Workspace. On that platform the key is validated against this
  Workspace when it is attached, so a key-policy problem is reported as an error
  on this request. This field is write-once: once a key is attached to a Workspace
  it cannot be detached or replaced. To rotate key material, rotate the underlying
  key on your cloud KMS; the `external_key_id` stays the same.

- `name: optional string`

  Name of the Workspace.

  minLength: 1, maxLength: 255

- `tags: optional map[string] or null`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `user_profile_id: optional string`

  ID of a user profile to attach to the Workspace. Every inference request through the Workspace must then name this user profile; the API rejects a request that names none or a different one. Once set, it can't be replaced or removed (sending the same ID again changes nothing); only deleting the user profile clears it. The default Workspace can't have a user profile.

#### Returns

- `Workspace object`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: DataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of AllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of AllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same AWS account and
    Region as the Workspace. On that platform the key is validated against this
    Workspace when it is attached, so a key-policy problem is reported as an error
    on this request. This field is write-once: once a key is attached to a Workspace
    it cannot be detached or replaced. To rotate key material, rotate the underlying
    key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```

### Archive Workspace

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Path parameters

- `workspace_id: string`

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `Workspace object`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: DataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of AllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of AllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same AWS account and
    Region as the Workspace. On that platform the key is validated against this
    Workspace when it is attached, so a key-policy problem is reported as an error
    on this request. This field is write-once: once a key is attached to a Workspace
    it cannot be detached or replaced. To rotate key material, rotate the underlying
    key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```

## Organization › Workspaces › Rate Limits

### List Workspace Rate Limits

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List a workspace's rate limits.

By default, returns only the groups and limiter types that have a
workspace-level override. With `include_inherited=true`, returns every
group with organization-level limits the workspace can see, listing for
each the values it inherits from the organization as well as its own
overrides. Each value's `source` says which it is.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

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

- `include_inherited: optional boolean`

  Also list the limiter values the workspace inherits from the organization, including groups with no workspace-level override.

  default: false

- `limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of WorkspaceRateLimit`

  Rate-limit entries for the workspace: one per group with at least one override, or, with `include_inherited` set to `true`, one per group the workspace can see that has organization-level limits.

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: OrganizationRateLimitModelGroup or OrganizationRateLimitBatchGroup or OrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to.

    - `OrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `OrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of WorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: WorkspaceRateLimitWorkspaceSource or WorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `WorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `WorkspaceRateLimitOrganizationSource object`

        - `type: "organization"`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `value: number`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group.type` is not `"model_group"`. The list covers the models this workspace has access to, so it can differ between workspaces.

  - `rate_limit_id: string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: string`

    ID of the Workspace this entry applies to.

- `next_page: string or null`

  Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
      "limits": [
        {
          "org_limit": 0,
          "source": {
            "type": "workspace"
          },
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

### Set Workspace Rate Limits

**POST** `/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}`

Set or clear rate-limit overrides for one rate-limit group in a workspace.

Only the limiter types named in `limits` change: an integer `value` sets
that type's override and `null` clears it. Types not named keep their
current value. A value above the organization's own limit is stored, but
the organization limit still applies, so the lower of the two is
enforced.

Returns the targeted group's entry with this request applied, in the shape
`GET /v1/organizations/workspaces/{workspace_id}/rate_limits` returns.
Changes take effect within about an hour.

#### Path parameters

- `workspace_id: string`

  The ID of the workspace.

- `rate_limit_id: string`

  The `id` of the organization's rate-limit entry to set overrides for.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `limits: array of WorkspaceRateLimitUpdateValue`

  Limits to set or clear. Unspecified limit types are unchanged.

  minItems: 1, maxItems: 16

  - `type: WorkspaceRateLimitType`

    Rate limiter type.

    - `"fast_itpmca"`

    - `"fast_otpm"`

    - `"input_tokens_per_minute"`

    - `"input_tokens_per_minute_cache_aware"`

    - `"output_tokens_per_minute"`

    - `"requests_per_minute"`

    - `"tokens_per_day"`

    - `"tokens_per_minute"`

    - `"tool_uses_per_second"`

  - `value: number or null`

    New limit value. Set to null to clear the workspace override and fall back to the organization limit.

    minimum: 0, maximum: 9007199254740991

#### Returns

- `WorkspaceRateLimit object`

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: OrganizationRateLimitModelGroup or OrganizationRateLimitBatchGroup or OrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to.

    - `OrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `OrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of WorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: WorkspaceRateLimitWorkspaceSource or WorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `WorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `WorkspaceRateLimitOrganizationSource object`

        - `type: "organization"`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `value: number`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group.type` is not `"model_group"`. The list covers the models this workspace has access to, so it can differ between workspaces.

  - `rate_limit_id: string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: string`

    ID of the Workspace this entry applies to.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits/$RATE_LIMIT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "limits": [
            {
              "type": "fast_itpmca",
              "value": 0
            }
          ]
        }'
```

##### Response (200)

```json
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
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

  default: 20, minimum: 1, maximum: 1000

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of WorkspaceMember`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `user_id: string`

  ID of the User.

- `workspace_role: NoBillingWorkspaceRole`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `WorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `WorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: WorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/members/$USER_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `workspace_role: WorkspaceRole`

  New workspace role for the User.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `WorkspaceMember object`

  - `type: "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: string`

    ID of the User.

  - `workspace_id: string`

    ID of the Workspace.

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_role": "workspace_admin"
        }'
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Organization › Workspaces › Service Accounts

### List Service Account Workspace Members

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of ServiceAccountWorkspaceMember`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `service_account_id: string`

  Tagged service account ID to add.

- `workspace_role: NoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `ServiceAccountWorkspaceMember object`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `ServiceAccountWorkspaceMember object`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `workspace_role: NoBillingWorkspaceRole`

  New role for the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `ServiceAccountWorkspaceMember object`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

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
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api?sdk_languages=http).

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `type: "service_account_workspace_member_deleted"`

  default: service_account_workspace_member_deleted

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
or an API-surface category such as the Message Batches API or the web
search tool) and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

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

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  minimum: 1, maximum: 1000

- `model: optional string`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of OrganizationRateLimit`

  Rate-limit entries for the organization, one per group.

  - `type: "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

    default: rate_limit

  - `id: string`

    Identifier of this rate-limit entry. It is stable within the organization and differs between organizations; the group's own identifier is `group.id`. Pass it as `rate_limit_id` to set a workspace's overrides for this group.

  - `group: OrganizationRateLimitModelGroup or OrganizationRateLimitBatchGroup or OrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to.

    - `OrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `OrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of OrganizationRateLimitValue`

    The limiter values that apply to this group.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: number`

      The configured limit value for this limiter type.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group.type` is not `"model_group"`. The list covers the models your organization has access to, so it can differ between organizations.

- `next_page: string or null`

  Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
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

## Organization › Compliance Settings

### Get Compliance Settings

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `OrganizationComplianceSettings object`

  - `type: "compliance_settings"`

    default: compliance_settings

  - `state: ComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `ComplianceSettingsStateEnabled object`

      - `type: "enabled"`

        default: enabled

    - `ComplianceSettingsStateDisabled object`

      - `type: "disabled"`

        default: disabled

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

### Update Compliance Settings

**POST** `/v1/organizations/compliance_settings`

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins
capturing organization activity events. Setting it to `disabled` turns
both off. Access Transparency events are an exception: they are still
captured while the Compliance API is disabled, and the Compliance API
activity feed returns them once it is enabled again. `state` reflects
whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the
resource unchanged. A `disabled` request stays in effect until a later
`enabled` request or the organization's next provisioning action that
enables Access Transparency: enabling Access Transparency also enables
the Compliance API, which serves its activity events, so such
provisioning (including re-runs) re-enables the Compliance API even
after a `disabled` request. Automated provisioning never disables
compliance settings.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `state: ComplianceSettingsStateParam`

  Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

  - `ComplianceSettingsStateEnabledParam object`

    - `type: "enabled"`

  - `ComplianceSettingsStateDisabledParam object`

    - `type: "disabled"`

#### Returns

- `OrganizationComplianceSettings object`

  - `type: "compliance_settings"`

    default: compliance_settings

  - `state: ComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `ComplianceSettingsStateEnabled object`

      - `type: "enabled"`

        default: enabled

    - `ComplianceSettingsStateDisabled object`

      - `type: "disabled"`

        default: disabled

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "state": {
            "type": "enabled"
          }
        }'
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

## Organization › Analytics › Summaries

### Get Activity Summaries

**GET** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day from `starting_date` (inclusive) to `ending_date`
(exclusive) in `data`, the same `data` / `next_page` envelope as the other
analytics list endpoints; the series is currently returned in full, so
`next_page` is always null.
Data is typically available with a 1-day lag and may be revised by a few
percent over the following days: when `ending_date` is omitted it
defaults to the most recent available day + 1, so the last entry covers
the most recent available day. The series can be scoped to an RBAC group
via `filter[]=rbac_group_id:{id}`. Available to organizations on a Claude
Enterprise plan. Requires an API key with the `read:analytics` scope.

#### Query parameters

- `starting_date: string`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`. Only `rbac_group_id` is supported (e.g. `filter[]=rbac_group_id:{id}`); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. `rbac_group_id` accepts the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

  maxItems: 100

- `limit: optional number`

  Number of results per page (1-1000, default 100). The day series (at most 366 entries) is currently returned in full in a single page, so `limit` does not yet shorten it.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field. `next_page` is currently always null, so there is never a cursor to send.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsSingleDayActivitySummary`

  One entry per day in the requested range, ascending by date.

  - `assigned_seat_count: number or null`

    Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

  - `cowork_daily_active_user_count: number`

    Number of users with Cowork activity on the requested day

  - `cowork_monthly_active_user_count: number`

    Number of users with Cowork activity in the 30-day rolling window

  - `cowork_weekly_active_user_count: number`

    Number of users with Cowork activity in the 7-day rolling window

  - `daily_active_user_count: number`

    Number of users with token consumption on the requested day

  - `daily_adoption_rate: number or null`

    Percentage of assigned seats with activity on the requested day (`DAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `ending_at: string`

    End of the aggregation period (exclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-16T00:00:00Z`).

    format: date-time

  - `monthly_active_user_count: number`

    Number of users with token consumption in the 30-day rolling window

  - `monthly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 30-day rolling window (`MAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `pending_invite_count: number or null`

    Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

  - `starting_at: string`

    Start of the aggregation period (inclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-15T00:00:00Z`).

    format: date-time

  - `weekly_active_user_count: number`

    Number of users with token consumption in the 7-day rolling window

  - `weekly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 7-day rolling window (`WAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `chat_cowork_unified_daily_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified on the requested day. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_monthly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 28-day rolling window (30 days when the request filters by `rbac_group_id`). Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_weekly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 7-day rolling window. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_daily_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_monthly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_weekly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_daily_active_user_count: optional number or null`

    Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_monthly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_weekly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_daily_active_user_count: optional number or null`

    Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_monthly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_weekly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_tag_daily_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag on the requested day. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_monthly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 28-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_weekly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 7-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `office_agent_daily_active_user_count: optional number or null`

    Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_monthly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_weekly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_daily_active_user_count: optional number or null`

    Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_entitled_user_count: optional number or null`

    Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_monthly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_weekly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results. Currently always null: the day series is returned in full.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_cowork_unified_daily_active_user_count": 0,
      "chat_cowork_unified_monthly_active_user_count": 0,
      "chat_cowork_unified_weekly_active_user_count": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "claude_tag_daily_active_user_count": 0,
      "claude_tag_monthly_active_user_count": 0,
      "claude_tag_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Users

### List User Activity

**GET** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Use `group_by[]` for per-RBAC-group aggregates, or `filter[]` to
scope results to specific members, groups, or a chat project. Available
to organizations on a Claude Enterprise plan. Requires an API key with
the `read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. A `project_id` filter limits each member's row to their claude.ai chat activity in that project and cannot be combined with `group_by[]` or an `rbac_group_id` filter. On these rows, every count in `chat_cowork_unified_metrics.sessions` is 0, because sessions are not measured per project. On any day a member sent a chat message in Chat and Cowork unified, all of that member's project activity for the day is counted in `chat_cowork_unified_metrics.chat` instead of `chat_metrics`.

  maxItems: 100

- `group_by: optional array of AnalyticsUserGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=rbac_group_id`). Supported on this endpoint: `rbac_group_id`. Rows are already per-member, so the one supported grouping aggregates them per RBAC group instead. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsUserActivity`

  - `chat_metrics: AnalyticsChatMetrics`

    Claude.ai activity metrics for a single user on a given day.

    - `connectors_used_count: number`

      Number of MCP connector invocations.

    - `distinct_artifacts_created_count: number`

      Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_connectors_used_count: number or null`

      Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_conversation_count: number or null`

      Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_files_uploaded_count: number or null`

      Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_projects_created_count: number`

      Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_shared_artifacts_viewed_count: number or null`

      Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent

    - `shared_conversations_viewed_count: number`

      Number of times the user opened a shared conversation in a project

    - `thinking_message_count: number`

      Number of messages that used extended thinking

  - `claude_code_metrics: AnalyticsClaudeCodeMetrics`

    Claude Code activity metrics for a single user on a given day.

    - `core_metrics: AnalyticsCoreCodeMetrics`

      Core Claude Code activity metrics for a single user on a given day.

      - `artifacts_created_count: number`

        Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `commit_count: number`

        Number of commits made via Claude Code

      - `distinct_session_count: number or null`

        Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

      - `lines_of_code: AnalyticsLinesOfCode`

        Lines of code added and removed via Claude Code.

        - `added_count: number`

          Lines of code added

        - `removed_count: number`

          Lines of code removed

      - `pull_request_count: number`

        Number of pull requests created via Claude Code

    - `tool_actions: AnalyticsToolActions`

      Per-tool accepted/rejected counts for Claude Code file modification tools.

      - `edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

        - `accepted_count: number`

          Number of tool proposals accepted

        - `rejected_count: number`

          Number of tool proposals rejected

      - `multi_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `notebook_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `write_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

  - `cowork_metrics: AnalyticsCoworkMetrics`

    Cowork activity metrics for a single user on a given day.

    - `action_count: number`

      Number of tool actions completed in Cowork sessions

    - `artifacts_created_count: number`

      Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `connectors_used_count: number`

      Total number of connector invocations in Cowork sessions

    - `dispatch_turn_count: number`

      Number of Dispatch (background agent) turns completed

    - `distinct_connectors_used_count: number or null`

      Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_plugins_used_count: number or null`

      Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `edit_tool_count: number or null`

      Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `file_edit_count: number or null`

      Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

    - `message_count: number`

      Number of messages sent in Cowork sessions

    - `multi_edit_tool_count: number or null`

      Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `notebook_edit_tool_count: number or null`

      Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `plugins_used_count: number or null`

      Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

    - `sessions_with_file_edits_count: number or null`

      Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `skills_used_count: number`

      Total number of skill invocations in Cowork sessions

    - `write_tool_count: number or null`

      Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `design_metrics: AnalyticsDesignMetrics`

    Claude Design activity metrics for a single user on a given day.

    - `distinct_projects_created_count: number`

      Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Design sessions

  - `distinct_user_count: number or null`

    Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

  - `office_metrics: AnalyticsOfficeMetrics`

    Office Agent activity metrics for a single user on a given day, broken out by Office product.

    - `excel: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

      - `connectors_used_count: number`

        Number of MCP connector invocations

      - `distinct_connectors_used_count: number or null`

        Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `skills_used_count: number`

        Number of skill invocations

    - `outlook: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `powerpoint: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `word: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

  - `science_metrics: AnalyticsScienceMetrics`

    Claude Science activity metrics for a single user on a given day.

    - `delegation_count: number`

      Number of delegations (handoffs to a specialized agent) in Claude Science sessions

    - `distinct_session_count: number or null`

      Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Science sessions

    - `remote_compute_job_count: number`

      Number of remote compute jobs launched from Claude Science sessions

    - `skills_used_count: number`

      Total number of skill invocations in Claude Science sessions

  - `user: AnalyticsUser or null`

    The user this row describes. Null on rows aggregated across users.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `web_search_count: number`

    Number of web searches performed

  - `chat_cowork_unified_metrics: optional AnalyticsChatCoworkUnifiedMetrics or null`

    Activity recorded while the member had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into `chat` (chat activity) and `sessions` (Cowork activity). Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsChatCoworkUnifiedChatMetrics`

      Chat activity recorded while members had Chat and Cowork unified turned
      on.

      - `connectors_used_count: number`

        Same measure as `chat_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_artifacts_created_count: number`

        Same measure as `chat_metrics.distinct_artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number or null`

        Same measure as `chat_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number or null`

        Same measure as `chat_metrics.distinct_files_uploaded_count`, for activity recorded while members had Chat and Cowork unified turned on. It counts uploaded files as well as files Claude created and images returned by Claude's tools, such as screenshots. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Same measure as `chat_metrics.distinct_projects_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number or null`

        Same measure as `chat_metrics.distinct_projects_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number or null`

        Always null: shared-artifact views are not currently measured.

      - `distinct_skills_used_count: number or null`

        Same measure as `chat_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Same measure as `chat_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `shared_conversations_viewed_count: number`

        Same measure as `chat_metrics.shared_conversations_viewed_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `thinking_message_count: number`

        Same measure as `chat_metrics.thinking_message_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `sessions: AnalyticsChatCoworkUnifiedSessionsMetrics`

      Cowork session activity recorded while members had Chat and Cowork
      unified turned on.

      - `action_count: number`

        Same measure as `cowork_metrics.action_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `artifacts_created_count: number`

        Same measure as `cowork_metrics.artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `connectors_used_count: number`

        Same measure as `cowork_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `dispatch_turn_count: number`

        Same measure as `cowork_metrics.dispatch_turn_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_connectors_used_count: number or null`

        Same measure as `cowork_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_plugins_used_count: number or null`

        Same measure as `cowork_metrics.distinct_plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Same measure as `cowork_metrics.distinct_session_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Same measure as `cowork_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: number or null`

        Same measure as `cowork_metrics.edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `file_edit_count: number or null`

        Same measure as `cowork_metrics.file_edit_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `message_count: number`

        Same measure as `cowork_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `multi_edit_tool_count: number or null`

        Same measure as `cowork_metrics.multi_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on. Claude no longer has a multi-edit tool, so expect 0 when not null; each edit is now a separate Edit tool call, counted in `edit_tool_count` and `file_edit_count`.

      - `notebook_edit_tool_count: number or null`

        Same measure as `cowork_metrics.notebook_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `plugins_used_count: number or null`

        Same measure as `cowork_metrics.plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `sessions_with_file_edits_count: number or null`

        Same measure as `cowork_metrics.sessions_with_file_edits_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `skills_used_count: number`

        Same measure as `cowork_metrics.skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `write_tool_count: number or null`

        Same measure as `cowork_metrics.write_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `claude_tag_metrics: optional AnalyticsClaudeTagMetrics or null`

    Claude Tag activity in Slack by a user who has linked a Claude account. Activity by Slack users who have not linked an account appears only in the `/summaries` Claude Tag counts, so these rows do not add up to those counts. Omitted from the response on deployments that do not offer Claude Tag reporting.

    - `active_day_count: number or null`

      1 on a day the user was active in Claude Tag in Slack, otherwise 0. Summed over the window in date-range mode, so it is the number of active days; on grouped rows, the total of each member's active days. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

    - `active_message_count: number or null`

      Number of the user's Slack messages that made them active: @-mentions, direct messages, group direct message asks, and thread posts Claude answered. Other messages are not counted. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

  - `last_activity_date: optional string or null`

    Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

    format: date

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_plugins_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "message_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "skills_used_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "user": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "web_search_count": 0,
      "chat_cowork_unified_metrics": {
        "chat": {
          "connectors_used_count": 0,
          "distinct_artifacts_created_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_conversation_count": 0,
          "distinct_files_uploaded_count": 0,
          "distinct_projects_created_count": 0,
          "distinct_projects_used_count": 0,
          "distinct_shared_artifacts_viewed_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "shared_conversations_viewed_count": 0,
          "thinking_message_count": 0
        },
        "sessions": {
          "action_count": 0,
          "artifacts_created_count": 0,
          "connectors_used_count": 0,
          "dispatch_turn_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_plugins_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "edit_tool_count": 0,
          "file_edit_count": 0,
          "message_count": 0,
          "multi_edit_tool_count": 0,
          "notebook_edit_tool_count": 0,
          "plugins_used_count": 0,
          "sessions_with_file_edits_count": 0,
          "skills_used_count": 0,
          "write_tool_count": 0
        }
      },
      "claude_tag_metrics": {
        "active_day_count": 0,
        "active_message_count": 0
      },
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Apps › Chat › Projects

### Get Chat Project Usage

**GET** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Use `group_by[]` to break projects out per member or per RBAC
group, and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Available to organizations on a Claude Enterprise
plan. Requires an API key with the `read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: optional array of AnalyticsProjectGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsProjectActivity`

  - `created_at: string or null`

    Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

    format: date-time

  - `created_by: AnalyticsUser or null`

    User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `distinct_conversation_count: number or null`

    Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `message_count: number`

    Number of messages sent in the project on the requested day

  - `project_id: string`

    Tagged project identifier (e.g. `claude_proj_...`)

  - `project_name: string`

    Name of the project

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Connectors

### Get Connector Usage

**GET** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Use `group_by[]` to break usage out per member, per RBAC
group, or per product surface, and `filter[]` to scope results; the
parameter descriptions list the supported dimensions. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `connector_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `connector_name` matches case-insensitively, a display name such as 'GitHub MCP' also matches its normalized stored form ('github'), and for rows whose `connector_name` is an opaque connector id the connector's display name (`connector_display_name`) also matches; `product` is one of `chat_cowork_unified`, `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsConnectorGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsConnectorActivity`

  - `chat_metrics: AnalyticsConnectorChatMetrics`

    Claude.ai activity metrics for a single connector on a given day.

    - `distinct_conversation_connector_used_count: number or null`

      Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsConnectorClaudeCodeMetrics`

    Claude Code activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `connector_display_name: string or null`

    Human-readable display name for rows whose `connector_name` is an opaque connector id rather than a readable name, resolved at request time from the organization's connectors (including connectors that have since been removed). `connector_name` remains the row's stable key for sorting and pagination, and `filter[]=connector_name:{value}` also matches these rows by display name. Display names are not unique, and the same connector's claude.ai usage can appear under a separate row with a readable `connector_name`. Null when `connector_name` is already a readable name, when the id cannot be resolved to one of the organization's connectors, or when display-name resolution is not enabled for this organization.

  - `connector_name: string`

    Name of the connector. Some rows carry an opaque connector id here instead of a readable name; `connector_display_name` holds the resolved name for those rows.

  - `cowork_metrics: AnalyticsConnectorCoworkMetrics`

    Cowork activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `individual_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on their own individual credential, connected through their own consent flow. Companion bucket to `managed_auth_distinct_user_count`, which carries the measurement, attribution, and null rules. Users whose requests used no stored credential count in neither bucket.

  - `managed_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on Enterprise Managed Auth (an organization-managed credential provisioned through the organization's identity provider), read from the token record each request used. Null, never 0, when managed-auth reporting is not enabled for the organization, the value cannot be attributed to the row, no credentialed requests and no managed-token mint events (a managed credential being provisioned for a user's use of the connector) were observed that day, or the day predates 2026-07-01, the first day the backing data exists (forward-only data, no backfill). When credentialed requests or mint events were observed and attributed, both managed-auth fields populate, reporting 0 for a bucket with no users; the two counts are independent, not a partition — a user whose requests that day used both kinds of credential counts in both. Mint events carry user but not surface attribution, so they count as observed auth activity on `user_id` and `rbac_group_id` cuts — attributed to the user the credential was provisioned for — but never on a cut that references `product` (group or filter). Date-range rollup mode (`starting_date`/`ending_date`) computes both fields exactly over the window — distinct users with at least one qualifying day — when the whole window starts on or after 2026-07-01, with the null-versus-0 and mint-event rules applying with the window in place of the day; a range starting earlier reports every managed-auth field as null, never a partial-window value.

  - `office_metrics: AnalyticsConnectorOfficeMetrics`

    Office Agent activity metrics for a single connector on a given day, broken out by Office product.

    - `excel: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

      - `distinct_session_connector_used_count: number or null`

        Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `powerpoint: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `word: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

  - `read_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of `read_call_count`, `write_call_count`, or `unclassified_call_count`, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in `unclassified_call_count`). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (`starting_date`/`ending_date`) applies both rules server-side.

  - `unclassified_call_count: number or null`

    Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `write_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `chat_cowork_unified_metrics: optional AnalyticsConnectorChatCoworkUnifiedMetrics or null`

    Connector use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsConnectorChatCoworkUnifiedChatMetrics`

      A connector's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_connector_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsConnectorChatCoworkUnifiedSessionsMetrics`

      A connector's use in Cowork sessions recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_session_connector_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/connectors \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_display_name": "connector_display_name",
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "individual_auth_distinct_user_count": 0,
      "managed_auth_distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "write_call_count": 0,
      "chat_cowork_unified_metrics": {
        "chat": {
          "distinct_conversation_connector_used_count": 0
        },
        "sessions": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Plugins

### Get Plugin Usage

**GET** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Use `group_by[]` to break usage out per
member, per RBAC group, or per product surface (Cowork / Claude Code),
and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like `/skills`.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `plugin_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `plugin_name` matches case-insensitively; `product` is `chat_cowork_unified`, `claude_code`, or `cowork` (the only surfaces with plugin attribution); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsPluginGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. On this endpoint `product` takes the values `chat_cowork_unified`, `claude_code`, or `cowork` only (the surfaces with plugin attribution). Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsPluginActivity`

  - `claude_code_metrics: AnalyticsPluginClaudeCodeMetrics`

    Claude Code activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsPluginCoworkMetrics`

    Cowork activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `install_count: number or null`

    Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `invocation_count: number`

    Number of plugin invocations on the requested day

  - `plugin_id: string or null`

    Stable plugin identifier when available (e.g. `serena@claude-plugins-official`). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

  - `plugin_name: string`

    Name of the plugin

  - `chat_cowork_unified_metrics: optional AnalyticsPluginChatCoworkUnifiedMetrics or null`

    Plugin use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `distinct_session_plugin_used_count: number or null`

      Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/plugins \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_id": "plugin_id",
      "plugin_name": "plugin_name",
      "chat_cowork_unified_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Skills

### Get Skill Usage

**GET** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Use `group_by[]` to break usage out per member, per RBAC group, or per
product surface, and `filter[]` to scope results; the parameter
descriptions list the supported dimensions. Available to organizations
on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `product`, `rbac_group_id`, `share_status`, `skill_name`, `user_id`. Value forms: `product` is one of `chat_cowork_unified`, `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `share_status` is one of `organization`, `private`, or `public`; `skill_name` matches case-insensitively; `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsSkillGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsSkillActivity`

  - `attributed_list_price: string or null`

    List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that involved the skill, not the skill's incremental cost. Unlike `estimated_overage_spend` this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does not tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on `chat` product rows and on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as `estimated_overage_spend` (spend reporting not enabled for this organization, `office_agent` product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `chat_metrics: AnalyticsSkillChatMetrics`

    Claude.ai activity metrics for a single skill on a given day.

    - `distinct_conversation_skill_used_count: number or null`

      Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsSkillClaudeCodeMetrics`

    Claude Code activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsSkillCoworkMetrics`

    Cowork activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `currency: string or null`

    Currency for this row's monetary fields (`estimated_overage_spend` and `attributed_list_price`), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

  - `distinct_user_count: number`

    Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

  - `enable_count: number or null`

    Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin `install_count`). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to `user_id` / `rbac_group_id` / `product` via `group_by[]` or `filter[]` (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (`starting_date`/`ending_date`).

  - `estimated_overage_spend: string or null`

    Estimated overage spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see `attributed_list_price` for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that involved the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (`starting_date`/`ending_date`) returns the window's sum. With `group_by[]=user_id` each row carries the user's own attributed spend. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `invocation_count: number or null`

    Total number of times this skill was invoked on the requested day (the skill analog of plugin `invocation_count`). Unlike `distinct_user_count` — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (`starting_date`/`ending_date`) returns this sum directly.

  - `office_metrics: AnalyticsSkillOfficeMetrics`

    Office Agent activity metrics for a single skill on a given day, broken out by Office product.

    - `excel: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

      - `distinct_session_skill_used_count: number or null`

        Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `powerpoint: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `word: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

  - `share_status: "organization" or "private" or "public" or null`

    Skill share status (claude.ai only): one of `private`, `organization`, or `public`. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via `filter[]=share_status:{value}`.

    - `"organization"`

    - `"private"`

    - `"public"`

  - `skill_display_name: string or null`

    Human-readable display name for rows whose `skill_name` is an opaque skill id (user/organization skill types and plugin-delivered skills, whose user-defined names usage reports generally withhold). Organization-shared skills and skills delivered by the organization's own plugins (its plugin marketplaces and its library) resolve; plugin skill names are shown without their 'plugin:' prefix. The literal 'unknown' bucket row gets a fixed 'Unknown skill' label. For a member's own skill (private or personal-plugin) it is null, except when the skill's owner used it from Claude Code or Cowork in the requested period: then it shows the name that client reported at the time. Apart from that, the names of members' own skills are not disclosed to analytics-key holders. Also null for Anthropic-provided plugin skills (not resolved), for an organization skill or plugin whose name can no longer be found (for example, one since deleted), when `skill_name` is already a display name, or when display-name resolution is not enabled for this organization.

  - `skill_name: string`

    Name of the skill

  - `chat_cowork_unified_metrics: optional AnalyticsSkillChatCoworkUnifiedMetrics or null`

    Skill use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsSkillChatCoworkUnifiedChatMetrics`

      A skill's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_skill_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsSkillChatCoworkUnifiedSessionsMetrics`

      A skill's use in Cowork sessions recorded while members had Chat
      and Cowork unified turned on.

      - `distinct_session_skill_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/skills \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "attributed_list_price": "attributed_list_price",
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "currency": "currency",
      "distinct_user_count": 0,
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "share_status": "organization",
      "skill_display_name": "skill_display_name",
      "skill_name": "skill_name",
      "chat_cowork_unified_metrics": {
        "chat": {
          "distinct_conversation_skill_used_count": 0
        },
        "sessions": {
          "distinct_session_skill_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Analytics › Artifacts

### Get Artifact Activity

**GET** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (`artifact_type`, `is_shared`) cube for the organization;
`next_page` is null except for grouped queries, which paginate. The cube
can be broken out per product, per member, or per RBAC group via
`group_by[]`, and scoped via `filter[]`. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `artifact_type`, `is_shared`, `product`, `rbac_group_id`, `user_id`. Value forms: `artifact_type` is a canonical artifact MIME type (e.g. `text/markdown`) or `other`; `is_shared` is `true` or `false`; `product` is `chat_cowork_unified`, `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsArtifactGroupBy`

  Dimensions to break results out by: `product`, `user_id` and/or `rbac_group_id`. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via `next_page`. `product` takes the values `chat_cowork_unified`, `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts). `rbac_group_id` attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; `limit` is the page size only when `group_by[]` multiplies the cube.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field. Only valid with `group_by[]` — the ungrouped cube is never paginated.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsArtifactActivity`

  - `artifact_type: string`

    Canonical artifact MIME type (e.g. `text/markdown`, `application/vnd.ant.react`, `image/svg+xml`), or `other`. Claude Code and Cowork artifacts report as `text/html`.

  - `artifacts_created_count: number`

    Number of artifacts created in this bucket on the requested day

  - `distinct_user_count: number`

    Number of distinct users who created artifacts in this bucket on the requested day

  - `is_shared: boolean`

    Whether the artifacts in this bucket have ever been shared (a Claude Code / Cowork artifact is shared once anyone beyond its creator may open it: named members, the whole organization, or anyone with the link).

  - `published_artifacts_created_count: number`

    Number of those artifacts that have been published (for Claude Code / Cowork artifacts: open to anyone with the link); never exceeds `artifacts_created_count`

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Spend Limits › Effective

### List Effective Spend Limits

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.
Supported for Claude Enterprise organizations only, not for Claude Console
organizations.

#### Query parameters

- `limit: optional number`

  Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `period: optional array of SpendLimitPeriod`

  Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

  maxItems: 3

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `user_ids: optional array of string`

  Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

  maxItems: 100

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of SpendSummary`

  - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: SpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `spend_limit_id: string`

- `next_page: string or null`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```

## Organization › Spend Limits › Increase Requests

### List Spend Limit Increase Requests

**GET** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

#### Query parameters

- `actor_ids: optional array of string`

  Filter by requester, as `user_...` tagged IDs.

- `limit: optional number`

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `status: optional array of SpendLimitIncreaseRequestStatus`

  Filter by status. Omit to return all.

  - `"approved"`

  - `"denied"`

  - `"pending"`

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of SpendLimitIncreaseRequest`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

- `next_page: string or null`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "daily",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "daily",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

### Get Spend Limit Increase Request

**GET** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}`

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the
requester at the request's period.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `SpendLimitIncreaseRequest object`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Approve Spend Limit Increase Request

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `amount: string`

  New per-user spend limit as a non-negative integer decimal string (minor units).

- `period: optional SpendLimitPeriod or null`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `suppress_notification: optional boolean`

#### Returns

- `type: "spend_limit_increase_request"`

  default: spend_limit_increase_request

- `id: string`

- `actor: SpendLimitIncreaseRequestActor`

  Who submitted the increase request.

  - `SpendLimitUserActor object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `type: "user_actor"`

      Actor type. Always `user_actor`.

      default: user_actor

    - `deleted: boolean`

      True only when the underlying account has been deleted.

      default: false

    - `email_address: string or null`

      The user's email address. Null when the account is unavailable or has been deleted.

    - `name: string or null`

      The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

    - `user_id: string`

      Tagged ID of the user.

  - `SpendLimitScopedAPIKeyActor object`

    A scoped Admin API key acting on behalf of the organization.

    - `type: "scoped_api_key_actor"`

      default: scoped_api_key_actor

    - `scoped_api_key_id: string`

- `created_at: string`

  format: date-time

- `period: SpendLimitPeriod`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `resolved_at: string or null`

  format: date-time

- `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

  Who approved or denied the increase request.

  - `SpendLimitUserActor object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

  - `SpendLimitScopedAPIKeyActor object`

    A scoped Admin API key acting on behalf of the organization.

- `spend_limit: SpendLimit or null`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `type: "spend_limit"`

    Object type. Always `spend_limit`.

    default: spend_limit

  - `id: string`

    Unique tagged ID of the spend limit (`spl_...`).

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `is_enabled: boolean`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: SpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

- `spend_summary: SpendSummary or null`

  Per-member effective-limit report row (`GET /spend_limits/effective`).

  - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: SpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `spend_limit_id: string`

- `status: SpendLimitIncreaseRequestStatus`

  - `"approved"`

  - `"denied"`

  - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "amount": "50000",
          "period": "monthly"
        }'
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Deny Spend Limit Increase Request

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `suppress_notification: optional boolean`

#### Returns

- `SpendLimitIncreaseRequest object`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/deny \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Organization › RBAC Groups

### Create RBAC Group

**POST** `/v1/organizations/rbac_groups`

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `name: string`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `RBACGroup object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string or null`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "Engineering"
        }'
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List RBAC Groups

**GET** `/v1/organizations/rbac_groups`

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of RBACGroup`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string or null`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Engineering",
      "role_ids": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "source_type": "direct",
      "type": "rbac_group",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Get RBAC Group

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}`

Retrieve an RBAC Group by ID.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `RBACGroup object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string or null`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update RBAC Group

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `name: optional string or null`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `RBACGroup object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string or null`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "Engineering"
        }'
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete RBAC Group

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}`

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `DeletedRBACGroup object`

  - `type: "rbac_group_deleted"`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

    default: rbac_group_deleted

  - `id: string`

    ID of the RBAC Group.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

## Organization › RBAC Groups › Members

### List RBAC Group Members

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of RBACGroupMember`

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `rbac_group_id: string`

    ID of the RBAC Group.

  - `user_id: string`

    ID of the User.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Add RBAC Group Member

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `user_id: string`

  ID of the User.

#### Returns

- `RBACGroupMember object`

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `rbac_group_id: string`

    ID of the RBAC Group.

  - `user_id: string`

    ID of the User.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        }'
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
}
```

### Remove RBAC Group Member

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

- `user_id: string`

  ID of the User.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `DeletedRBACGroupMember object`

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    default: rbac_group_member_deleted

  - `rbac_group_id: string`

    ID of the RBAC Group.

  - `user_id: string`

    ID of the User.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
}
```

## Organization › RBAC Roles

### List RBAC Roles

**GET** `/v1/organizations/rbac_roles`

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of RBACRole`

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

    Name of the RBAC Role. For a built-in role, this is Anthropic's name for the access that the role grants. Anthropic may change this name, so to keep a lasting reference to a role, store its `id`.

  - `source: RBACRoleSource`

    Whether the RBAC Role is built-in or custom. More values of `type` may be added, so do not treat every role that is not `built_in` as `custom`.

    - `RBACRoleSourceBuiltIn object`

      - `type: "built_in"`

        Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

        default: built_in

    - `RBACRoleSourceCustom object`

      - `type: "custom"`

        The organization's administrators can change and delete the RBAC Role.

        default: custom

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

- `has_more: boolean`

  Indicates whether there are more results beyond this page.

- `next_page: string or null`

  Opaque cursor for the next page. Pass as the `page` parameter on the next
  request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Project Editor",
      "source": {
        "type": "built_in"
      },
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

### Get RBAC Role

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_role_id: string`

  ID of the RBAC Role.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `RBACRole object`

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

    Name of the RBAC Role. For a built-in role, this is Anthropic's name for the access that the role grants. Anthropic may change this name, so to keep a lasting reference to a role, store its `id`.

  - `source: RBACRoleSource`

    Whether the RBAC Role is built-in or custom. More values of `type` may be added, so do not treat every role that is not `built_in` as `custom`.

    - `RBACRoleSourceBuiltIn object`

      - `type: "built_in"`

        Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

        default: built_in

    - `RBACRoleSourceCustom object`

      - `type: "custom"`

        The organization's administrators can change and delete the RBAC Role.

        default: custom

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "source": {
    "type": "built_in"
  },
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Organization › RBAC Roles › Permissions

### List RBAC Role Permissions

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}/permissions`

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Path parameters

- `rbac_role_id: string`

  ID of the RBAC Role.

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of RBACRolePermission`

  - `type: "rbac_role_permission"`

    Object type.

    For RBAC Role Permissions, this is always `"rbac_role_permission"`.

    default: rbac_role_permission

  - `action: string`

    Action the permission grants on the resource.

    The vocabulary follows the resource: an `organization` grant carries a
    product-feature entitlement (for example `chat`), an admin-panel
    permission entitlement (`permission_*`), or a blanket capability-access
    mode — `capability_access_all` grants every product-feature entitlement
    except `inference_hooks_inspection`, which a role holds only through its
    own row, and `capability_access_all_ga` grants the subset of those for
    stable features as it stands at permission-check time; neither mode grants
    model-access entitlements. A consumer enumerating a role's per-feature grants should
    treat a blanket row as granting every product-feature entitlement it
    covers, or it will under-report the role's effective access. A `connector_tool` grant carries
    a tool-access action (`use` or `always_allow`); a `connector_scope` grant
    carries the scope action `grant` (the role may receive the named OAuth
    scope when tokens are minted for the connector); `connector` and
    `all_connectors` grants carry a tool-access action, the scope action, or
    an authentication-method action (`interactive` or `managed`).

  - `resource: RBACOrganizationPermissionResource or RBACConnectorToolPermissionResource or RBACConnectorScopePermissionResource or 2 more`

    What the permission applies to.

    A tagged union: `type` names the kind of resource and determines which
    identifier fields are present.

    - `RBACOrganizationPermissionResource object`

      - `type: "organization"`

        Kind of resource the permission applies to.

        default: organization

      - `organization_id: string`

        UUID of the organization the permission applies to.

    - `RBACConnectorToolPermissionResource object`

      - `type: "connector_tool"`

        Kind of resource the permission applies to.

        default: connector_tool

      - `connector_id: string`

        ID of the connector the permission applies to.

      - `tool_name: string`

        Published name of the connector tool the permission applies to.

        When the published name contains characters outside `[a-zA-Z0-9_-]` (or
        collides with a reserved form), it is server-encoded into a stable
        `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus
        a hash — from which the published name is not recoverable.

    - `RBACConnectorScopePermissionResource object`

      - `type: "connector_scope"`

        Kind of resource the permission applies to.

        default: connector_scope

      - `connector_id: string`

        ID of the connector the permission applies to.

      - `scope: string`

        OAuth scope the permission names — the role may receive this scope when
        tokens are minted for the connector.

        Subject to the same encoding rule as `tool_name`: a scope containing
        characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form)
        appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth
        scopes routinely contain `:` and `/`, so most appear encoded.

    - `RBACConnectorPermissionResource object`

      - `type: "connector"`

        Kind of resource the permission applies to.

        default: connector

      - `connector_id: string`

        ID of the connector the permission applies to.

    - `RBACAllConnectorsPermissionResource object`

      - `type: "all_connectors"`

        Kind of resource the permission applies to.

        default: all_connectors

- `has_more: boolean`

  Indicates whether there are more results beyond this page.

- `next_page: string or null`

  Opaque cursor for the next page. Pass as the `page` parameter on the next
  request.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID/permissions \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```
