---
title: Deployments
url: https://platform.claude.com/docs/en/api/php/beta/deployments
---

# Deployments

## Create Deployment

`$client->beta->deployments->create(Agent agent, string environmentID, list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, string name, ?BetaManagedAgentsBudgetLimit budget, ?string description, ?array<string,string> metadata, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments`

Create Deployment

### Parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## List Deployments

`$client->beta->deployments->list(?string agentID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?BetaManagedAgentsDeploymentStatus status, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<BetaManagedAgentsDeployment>`

**GET** `/v1/deployments`

List Deployments

### Parameters

- `agentID?:optional string`

  Filter by agent ID.

- `createdAtGte?:optional \Datetime`

  Return deployments created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return deployments created at or before this time (inclusive).

- `includeArchived?:optional bool`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 100.

- `page?:optional string`

  Opaque pagination cursor.

- `status?:optional BetaManagedAgentsDeploymentStatus`

  Filter by status: `active` or `paused`. Omit for both. To include archived deployments, use `include_archived` instead; the two cannot be combined.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->deployments->list(
  agentID: 'agent_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
  status: BetaManagedAgentsDeploymentStatus::ACTIVE,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

#### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`$client->beta->deployments->retrieve(string deploymentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->retrieve(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeployment);
```

#### Response (200)

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

## Update Deployment

`$client->beta->deployments->update(string deploymentID, ?Agent agent, ?BetaManagedAgentsBudgetLimit budget, ?string description, ?string environmentID, ?list<BetaManagedAgentsDeploymentInitialEventParams> initialEvents, ?array<string,string> metadata, ?string name, ?list<Resource> resources, ?BetaManagedAgentsScheduleParams schedule, ?list<string> vaultIDs, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment to update.

- `agent?:optional Agent`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

- `budget?:optional BetaManagedAgentsBudgetLimit`

  Spend ceiling for future sessions. Full replacement. Omit to preserve; send null to clear (sessions created afterwards are uncapped). The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

- `description?:optional string`

  Description. Omit to preserve; send empty string or null to clear.

- `environmentID?:optional string`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `initialEvents?:optional list<BetaManagedAgentsDeploymentInitialEventParams>`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name?:optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `resources?:optional list<Resource>`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

- `schedule?:optional BetaManagedAgentsScheduleParams`

  Cron schedule. Full replacement. Omit to preserve; send null to clear (revert to manual-only).

- `vaultIDs?:optional list<string>`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->update(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  agent: 'string',
  budget: [
    'maxListCost' => ['amount' => '2500', 'currency' => BetaCurrency::USD],
    'type' => 'limit',
  ],
  description: 'description',
  environmentID: 'environment_id',
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  metadata: ['foo' => 'string'],
  name: 'name',
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

#### Response (200)

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

## Archive Deployment

`$client->beta->deployments->archive(string deploymentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment to archive.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->archive(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeployment);
```

#### Response (200)

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

## Run Deployment Now

`$client->beta->deployments->run(string deploymentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeploymentRun`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment to run.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeploymentRun`

  - `Type type`

  - `string id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    Snapshot of the agent at fire time. Always fully resolved — deployments pin agent + version.

  - `\Datetime createdAt`

    Time this run record was persisted.

  - `string deploymentID`

    ID of the deployment that produced this run.

  - `?Error error`

    Populated on creation failure. Null on success. Exactly one of `session_id` or `error` is non-null.

  - `?string sessionID`

    Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    What triggered this run and trigger-specific metadata.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeploymentRun = $client->beta->deployments->run(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeploymentRun);
```

#### Response (200)

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Pause Deployment

`$client->beta->deployments->pause(string deploymentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment to pause.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->pause(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeployment);
```

#### Response (200)

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

## Unpause Deployment

`$client->beta->deployments->unpause(string deploymentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deploymentID: string`

  Unique identifier of the deployment to unpause.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeployment = $client->beta->deployments->unpause(
  'depl_011CZkZcDH3vPqd7xnEfwTai',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeployment);
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule`

  - `Type type`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `?\Datetime lastRunAt`

    Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams`

  - `Type type`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

### Beta Managed Agents Deployment

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

### Beta Managed Agents Deployment Initial Event

- `class BetaManagedAgentsDeploymentInitialEvent`

  - `class BetaManagedAgentsDeploymentUserMessageEvent`

    - `Type type`

    - `list<Content> content`

      Array of content blocks for the user message.

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

    - `Type type`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      How to grade the outcome. Text or file reference.

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class BetaManagedAgentsDeploymentSystemMessageEvent`

    - `Type type`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

### Beta Managed Agents Deployment Initial Event Params

- `class BetaManagedAgentsDeploymentInitialEventParams`

  - `class ManagedAgentsUserMessageEventParams`

    - `Type type`

    - `list<Content> content`

      Array of content blocks for the user message.

  - `class ManagedAgentsUserDefineOutcomeEventParams`

    - `Type type`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      How to grade the outcome. Text or file reference.

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class ManagedAgentsSystemMessageEventParams`

    - `Type type`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

### Beta Managed Agents Deployment Paused Reason

- `class BetaManagedAgentsDeploymentPausedReason`

  - `class BetaManagedAgentsManualDeploymentPausedReason`

    - `Type type`

  - `class BetaManagedAgentsErrorDeploymentPausedReason`

    - `Type type`

    - `BetaManagedAgentsDeploymentPausedReasonError error`

      The failed run's error.

### Beta Managed Agents Deployment Paused Reason Error

- `class BetaManagedAgentsDeploymentPausedReasonError`

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

    - `Type type`

  - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

    - `Type type`

### Beta Managed Agents Deployment Status

- `enum BetaManagedAgentsDeploymentStatus`

  - `"active"`

    The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

  - `"paused"`

    The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent`

  - `Type type`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

  - `Type type`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    How to grade the outcome. Text or file reference.

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent`

  - `Type type`

  - `list<Content> content`

    Array of content blocks for the user message.

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason`

  - `Type type`

  - `BetaManagedAgentsDeploymentPausedReasonError error`

    The failed run's error.

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig`

  - `Type type`

  - `string fileID`

    ID of a previously uploaded file.

  - `?string mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig`

  - `Type type`

  - `string url`

    Github URL of the repository

  - `?Checkout checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

  - `?string mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig`

  - `Type type`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `?Access access`

    Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule`

  - `Type type`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `?\Datetime lastRunAt`

    Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

  - `?list<\Datetime> upcomingRunsAt`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams`

  - `Type type`

  - `string expression`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `string timezone`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Session Resource Config

- `class BetaManagedAgentsSessionResourceConfig`

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

    - `Type type`

    - `string url`

      Github URL of the repository

    - `?Checkout checkout`

      Branch or commit to check out. Defaults to the repository's default branch.

    - `?string mountPath`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig`

    - `Type type`

    - `string fileID`

      ID of a previously uploaded file.

    - `?string mountPath`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig`

    - `Type type`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `?Access access`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

  - `Type type`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

  - `Type type`
