---
title: Update Session Resource
url: https://platform.claude.com/docs/en/api/php/beta/sessions/resources/update
---

# Update Session Resource

`$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas, ?string workspaceID): ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

## Parameters

- `sessionID: string`

- `resourceID: string`

- `authorizationToken: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ResourceUpdateResponse`

  - `class ManagedAgentsGitHubRepositoryResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `class ManagedAgentsFileResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsMemoryStoreResource`

    - `Type type`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `?Access access`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->update(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  authorizationToken: 'ghp_exampletoken',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($resource);
```

### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```
