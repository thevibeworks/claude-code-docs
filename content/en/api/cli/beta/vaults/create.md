# Create Vault

`$ ant beta:vaults create`

**POST** `/v1/vaults`

Create Vault

## Parameters

- `--display-name: string`

  Body param: Human-readable name for the vault. 1-255 characters.

  minLength: 1, maxLength: 255

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_managed_agents_vault: object`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

## Example

```bash
ant beta:vaults create \
  --api-key my-anthropic-api-key \
  --display-name 'Example vault'
```

### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```
