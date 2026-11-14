---
title: Delete Skill
url: https://platform.claude.com/docs/en/api/php/beta/skills/delete
---

# Delete Skill

`$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaDeletedSkill`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

## Parameters

- `skillID: string` (path parameter)

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?: optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaDeletedSkill`

  - `"skill_deleted" type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

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

$betaDeletedSkill = $client->beta->skills->delete(
  'skill_id',
  betas: [AnthropicBeta::COMPUTER_USE_2024_10_22],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaDeletedSkill);
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```
