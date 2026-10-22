---
title: List Vaults
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/list
---

# List Vaults

`$ ant beta:vaults list`

**GET** `/v1/vaults`

List Vaults

## Parameters

- `--include-archived: optional boolean` (query parameter)

  Whether to include archived vaults in the results. Defaults to `false`.

- `--limit: optional number` (query parameter)

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  format: int32

- `--page: optional string` (query parameter)

  The `next_page` value from a previous [List Vaults](https://platform.claude.com/docs/en/api/beta/vaults/list?sdk_languages=cli) response, to get the next page. Leave it out to get the first page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsListVaultsResponse: object`

  Response containing a paginated list of vaults.

  - `data: optional array of BetaManagedAgentsVault`

    The vaults on this page, newest first.

    - `type: "vault"`

    - `id: string`

      The unique ID of the vault (`vlt_...`).

    - `archived_at: string`

      When the vault was archived. Null if not archived.

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `display_name: string`

      Human-readable name for the vault.

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the vault.

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

## Example

```bash
ant beta:vaults list
```

### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
