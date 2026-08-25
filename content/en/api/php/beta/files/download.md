---
title: Download File
url: https://platform.claude.com/docs/en/api/php/beta/files/download
---

## Download File

`$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `mixed`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->files->download(
  'file_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($response);
```
