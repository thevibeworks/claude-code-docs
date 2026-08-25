---
title: Delete File
url: https://platform.claude.com/docs/en/api/php/beta/files/delete
---

## Delete File

`$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): BetaDeletedFile`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaDeletedFile`

  - `string id`

    ID of the deleted file.

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedFile = $client->beta->files->delete(
  'file_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaDeletedFile);
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
