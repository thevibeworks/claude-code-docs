---
title: Delete File
url: https://platform.claude.com/docs/en/api/cli/beta/files/delete
---

# Delete File

`$ ant beta:files delete`

**DELETE** `/v1/files/{file_id}`

Delete File

## Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_deleted_file: object`

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: string`

    ID of the deleted file.

## Example

```bash
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
