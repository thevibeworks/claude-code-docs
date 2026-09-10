---
title: Delete Vault
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/delete
---

# Delete Vault

`$ ant beta:vaults delete`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

## Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_deleted_vault: object`

  Confirmation of a deleted vault.

  - `type: "vault_deleted"`

  - `id: string`

    Unique identifier of the deleted vault.

## Example

```bash
ant beta:vaults delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```
