---
title: Create Skill
url: https://platform.claude.com/docs/en/api/php/beta/skills/create
---

# Create Skill

`$client->beta->skills->create(list<FileParam | string> files, ?string displayName, ?list<AnthropicBeta> betas, ?string workspaceID): BetaSkill`

**POST** `/v1/skills`

Create Skill

## Parameters

- `files: list<FileParam | string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `displayName?: optional string`

  Human-readable, single-line label for the Skill. Maximum 255 characters.
  Always set: derived from the SKILL.md frontmatter `name` when omitted at
  creation. Not unique.

- `betas?: optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaSkill`

  - `"skill" type`

    Object type.

    For Skills, this is always `"skill"`.

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `string displayName`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `string latestVersionID`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `BetaSkillSource source`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

  - `\Datetime updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=php).

- `ClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledException` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedException` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `CMEKContextUnavailableException` (HTTP status 503, error code `cmek_context_unavailable`)

  The workspace's encryption settings could not be read, so the request was refused. Retry in a few minutes.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;
use Anthropic\Core\FileParam;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSkill = $client->beta->skills->create(
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  displayName: 'display_name',
  betas: [AnthropicBeta::COMPUTER_USE_2024_10_22],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaSkill);
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
