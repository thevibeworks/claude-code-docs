---
title: Create Deployment
url: https://platform.claude.com/docs/en/api/php/beta/deployments/create
---

# Create Deployment

`$client->beta->deployments->create(Agent agent, string environmentID, list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, string name, ?BetaManagedAgentsBudgetLimit budget, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments`

Create Deployment

## Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

- `environmentID: string`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

- `initialEvents: list<BetaManagedAgentsDeploymentInitialEventParams>`

  Events to send to each session immediately after creation. At least 1, maximum 50.

- `name: string`

  Human-readable name for the deployment.

- `budget?:optional BetaManagedAgentsBudgetLimit`

  Enforced spend ceiling stamped onto each session created from this deployment, copied at session-creation time. Omit to leave sessions uncapped. The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

- `description?:optional string`

  Description of what the deployment does.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources?:optional list<Resource>`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  Optional recurring cron schedule. When present, the deployment fires automatically. Both expression and timezone are required when schedule is set.

- `vaultIDs?:optional list<string>`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsDeployment`

  - `Type type`

  - `string id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    Reference to the agent this deployment runs, resolved to a concrete version.

  - `?\Datetime archivedAt`

    Time the deployment was archived. Null if not archived.

  - `\Datetime createdAt`

    Time the deployment was created.

  - `?string description`

    Description of what the deployment does.

  - `string environmentID`

    ID of the `environment` where sessions run.

  - `list<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `string name`

    Human-readable name.

  - `?BetaManagedAgentsDeploymentPausedReason pausedReason`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

  - `list<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

  - `?BetaManagedAgentsSchedule schedule`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

  - `BetaManagedAgentsDeploymentStatus status`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

  - `\Datetime updatedAt`

    Time the deployment was last updated.

  - `list<string> vaultIDs`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `?BetaManagedAgentsBudgetLimit budget`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->create(
  agent: 'string',
  environmentID: 'x',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  name: 'x',
  budget: [
    'maxListCost' => ['amount' => '2500', 'currency' => BetaCurrency::USD],
    'type' => 'limit',
  ],
  description: 'description',
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  schedule: [
    'expression' => '0 9 * * 1-5',
    'timezone' => 'America/Los_Angeles',
    'type' => 'cron',
  ],
  vaultIDs: ['string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeployment);
```

### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```
