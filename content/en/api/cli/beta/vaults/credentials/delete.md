---
title: Delete Credential
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/credentials/delete
---

# Delete Credential

`$ ant beta:vaults:credentials delete`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

## Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_deleted_credential: object`

  Confirmation of a deleted credential.

  - `type: "vault_credential_deleted"`

  - `id: string`

    Unique identifier of the deleted credential.

## Example

```bash
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```
