---
title: Get Queue Statistics
url: https://platform.claude.com/docs/en/api/php/beta/environments/work/stats
---

# Get Queue Statistics

`$client->beta->environments->work->stats(string environmentID, ?list<AnthropicBeta> betas, ?string workspaceID): SelfHostedWorkQueueStats`

**GET** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

## Parameters

- `environmentID: string` (path parameter)

- `betas?: optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class SelfHostedWorkQueueStats`

  - `"work_queue_stats" type`

    The type of object

  - `int depth`

    Number of work items waiting to be picked up

  - `?string oldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `int pending`

    Number of work items being processed (polled but not acknowledged)

  - `?int workersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=php).

- `ClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSelfHostedWorkQueueStats = $client->beta->environments->work->stats(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  betas: [AnthropicBeta::COMPUTER_USE_2024_10_22],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaSelfHostedWorkQueueStats);
```

### Response (200)

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```
