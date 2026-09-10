---
title: Download File
url: https://platform.claude.com/docs/en/api/cli/beta/files/download
---

# Download File

`$ ant beta:files download`

**GET** `/v1/files/{file_id}/content`

Download File

## Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `unnamed_schema_1: file path`

## Example

```bash
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```
