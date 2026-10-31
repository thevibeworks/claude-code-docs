---
title: Create External Key
url: https://platform.claude.com/docs/en/api/beta/organization/external_keys/create
---

# Create External Key

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

## Body parameters

- `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfigParam`

  KMS provider identity and auth coordinates.

  - `BetaAWSExternalKeyConfig object`

    - `type: "aws"`

    - `kms_arn: string`

      Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

      maxLength: 2048

    - `region: optional string or null`

      AWS region. Derived from `kms_arn` if omitted.

    - `role_arn: optional string or null`

      **Deprecated**

      IAM role ARN. Deprecated; this field is ignored.

  - `BetaGCPExternalKeyConfig object`

    - `type: "gcp"`

    - `key_name: string`

      Full resource name of the Cloud KMS key.

  - `BetaAzureExternalKeyConfigParam object`

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

  ID of a user profile to bind the key to. Omit this field for a key that isn't bound to a user profile. Such a key can be attached to a Workspace whatever its user profile. The binding cannot be changed later. A key bound to a user profile can only be attached to a Workspace that has the same user profile.

## Returns

- `BetaExternalKey object`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `type: "external_key"`

    default: external_key

  - `id: string`

    Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.

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

    Data residency geo. Selects the region that handles this key's encrypt/decrypt roundtrips.

  - `provider_config: BetaAWSExternalKeyConfig or BetaGCPExternalKeyConfig or BetaAzureExternalKeyConfig`

    KMS provider identity and auth coordinates.

    - `BetaAWSExternalKeyConfig object`

      - `type: "aws"`

      - `kms_arn: string`

        Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

        maxLength: 2048

      - `region: optional string or null`

        AWS region. Derived from `kms_arn` if omitted.

      - `role_arn: optional string or null`

        **Deprecated**

        IAM role ARN. Deprecated; this field is ignored.

    - `BetaGCPExternalKeyConfig object`

      - `type: "gcp"`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

    - `BetaAzureExternalKeyConfig object`

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

## Example

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

### Response (200)

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
