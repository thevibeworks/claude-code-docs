---
title: Download File
url: https://platform.claude.com/docs/en/api/files/download
---

# Download File

**GET** `/v1/files/{file_id}/content`

Download File

## Path parameters

- `file_id: string`

  ID of the File.

## Headers

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Example

```bash
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
