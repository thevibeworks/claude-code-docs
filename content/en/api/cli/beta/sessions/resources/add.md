---
title: Add Session Resource
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/resources/add
---

# Add Session Resource

`$ ant beta:sessions:resources add`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

## Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--file-id: string`

  Body param: ID of a previously uploaded file.

  minLength: 1, maxLength: 128

- `--type: "file"`

  Body param

- `--mount-path: optional string`

  Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  minLength: 1, maxLength: 4096

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_file_resource: object`

  - `type: "file"`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: string`

  - `mount_path: string`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

## Example

```bash
ant beta:sessions:resources add \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --file-id file_011CNha8iCJcU1wXNR6q4V8w \
  --type file
```

### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```
