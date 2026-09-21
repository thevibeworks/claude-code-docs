---
title: Delete File
url: https://platform.claude.com/docs/en/api/php/beta/files/delete
---

# Delete File

`$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

## Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaDeletedFile`

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `string id`

    ID of the deleted file.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedFile = $client->beta->files->delete(
  'file_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaDeletedFile);
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
