---
title: List External Keys
url: https://platform.claude.com/docs/en/api/admin/external_keys/list
---

## List External Keys

**get** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

### Query Parameters

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Returns

- `data: array of object { id, attachment, created_at, 5 more }`

  - `id: string`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `attachment: object { type }  or object { type }`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `Attached object { type }`

      - `type: "attached"`

        - `"attached"`

    - `Unattached object { type }`

      - `type: "unattached"`

        - `"unattached"`

  - `created_at: string`

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `geo: string`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `provider_config: object { kms_arn, type, region, role_arn }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more }`

    KMS provider identity and auth coordinates.

    - `Aws object { kms_arn, type, region, role_arn }`

      - `kms_arn: string`

        Full ARN of the AWS KMS key.

      - `type: "aws"`

        - `"aws"`

      - `region: optional string or null`

        AWS region. Derived from kms_arn if omitted.

      - `role_arn: optional string or null`

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `Gcp object { key_name, type }`

      - `key_name: string`

        Full resource name of the Cloud KMS key.

      - `type: "gcp"`

        - `"gcp"`

    - `Azure object { key_name, tenant_id, type, 2 more }`

      - `key_name: string`

        Name of the key within the vault.

      - `tenant_id: string`

        Azure AD tenant ID.

      - `type: "azure"`

        - `"azure"`

      - `vault_uri: string`

        Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

      - `client_id: optional string or null`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `type: "external_key"`

    - `"external_key"`

  - `updated_at: string`

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

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
