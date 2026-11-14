---
title: Create Environment
url: https://platform.claude.com/docs/en/api/php/beta/environments/create
---

# Create Environment

`$client->beta->environments->create(string name, ?Config config, ?string description, ?array<string,string> metadata, ?Scope scope, ?list<AnthropicBeta> betas, ?string workspaceID): BetaEnvironment`

**POST** `/v1/environments`

Create a new environment with the specified configuration.

## Parameters

- `name: string`

  Human-readable name for the environment

- `config?: optional Config`

  Environment configuration

- `description?: optional string`

  Optional description of the environment

- `metadata?: optional array<string,string>`

  User-provided metadata key-value pairs

- `scope?: optional Scope`

  The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. API organizations support only 'organization'; 'account' is rejected. If not specified, defaults based on organization type.

- `betas?: optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaEnvironment`

  - `"environment" type`

    The type of object (always 'environment')

  - `string id`

    Environment identifier (e.g., 'env_...')

  - `?string archivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config config`

    Environment configuration (either Anthropic Cloud or self-hosted)

  - `string createdAt`

    RFC 3339 timestamp when environment was created

  - `?string description`

    User-provided description for the environment; null when unset

  - `array<string,string> metadata`

    User-provided metadata key-value pairs

  - `string name`

    Human-readable name for the environment

  - `string updatedAt`

    RFC 3339 timestamp when environment was last updated

  - `?Scope scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=php).

- `ClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `BetaEnvironmentCreateDisabledException` (HTTP status 403, error code `environment_create_disabled`)

  Anthropic has turned off creating environments for this organization. Existing environments still work.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironment = $client->beta->environments->create(
  name: 'python-data-analysis',
  config: [
    'type' => 'cloud',
    'networking' => [
      'type' => 'limited',
      'allowMCPServers' => true,
      'allowPackageManagers' => true,
      'allowedHosts' => ['api.example.com'],
    ],
    'packages' => [
      'apt' => ['string'],
      'cargo' => ['string'],
      'gem' => ['string'],
      'go' => ['string'],
      'npm' => ['string'],
      'pip' => ['pandas', 'numpy'],
      'type' => 'packages',
    ],
  ],
  description: 'Python environment with data-analysis packages.',
  metadata: ['foo' => 'string'],
  scope: 'organization',
  betas: [AnthropicBeta::COMPUTER_USE_2024_10_22],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaEnvironment);
```

### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [],
      "cargo": [],
      "gem": [],
      "go": [],
      "npm": [],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```
