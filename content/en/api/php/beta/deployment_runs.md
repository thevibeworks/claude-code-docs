---
title: Deployment Runs
url: https://platform.claude.com/docs/en/api/php/beta/deployment_runs
---

# Deployment Runs

## List Deployment Runs

`$client->beta->deploymentRuns->list(?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool hasError, ?int limit, ?string page, ?BetaManagedAgentsTriggerType triggerType, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<BetaManagedAgentsDeploymentRun>`

**GET** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `createdAtGt?:optional \Datetime`

  Return runs created strictly after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return runs created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return runs created strictly before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return runs created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent `deployment_id` returns 200 with empty data.

- `hasError?:optional bool`

  Filter: true for runs with non-null `error`, false for runs with non-null `session_id`. Omit for all.

- `limit?:optional int`

  Maximum results per page. Default 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor. Pass `next_page` from the previous response. Invalid or expired cursors return 400.

- `triggerType?:optional BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

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

$page = $client->beta->deploymentRuns->list(
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  hasError: true,
  limit: 0,
  page: 'page',
  triggerType: BetaManagedAgentsTriggerType::SCHEDULE,
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
  ],
  "next_page": "next_page"
}
```

## Get Deployment Run

`$client->beta->deploymentRuns->retrieve(string deploymentRunID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeploymentRun`

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deploymentRunID: string`

  Unique identifier of the deployment run.

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

$betaManagedAgentsDeploymentRun = $client->beta->deploymentRuns->retrieve(
  'deployment_run_id',
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

## Domain types

### Beta Managed Agents Agent Archived Run Error

- `class BetaManagedAgentsAgentArchivedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Deployment Run

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

### Beta Managed Agents Environment Archived Run Error

- `class BetaManagedAgentsEnvironmentArchivedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Environment Not Found Run Error

- `class BetaManagedAgentsEnvironmentNotFoundRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents File Not Found Run Error

- `class BetaManagedAgentsFileNotFoundRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Manual Trigger Context

- `class BetaManagedAgentsManualTriggerContext`

  - `Type type`

### Beta Managed Agents MCP Egress Blocked Run Error

- `class BetaManagedAgentsMCPEgressBlockedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Memory Store Archived Run Error

- `class BetaManagedAgentsMemoryStoreArchivedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Organization Disabled Run Error

- `class BetaManagedAgentsOrganizationDisabledRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Schedule Trigger Context

- `class BetaManagedAgentsScheduleTriggerContext`

  - `Type type`

  - `\Datetime scheduledAt`

    The UTC instant at which the cron expression matched in the configured timezone, before jitter is applied. At most one run is recorded per (`deployment_id`, `scheduled_at`) pair.

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Session Creation Rejected Run Error

- `class BetaManagedAgentsSessionCreationRejectedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Session Rate Limited Run Error

- `class BetaManagedAgentsSessionRateLimitedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Session Resource Not Found Run Error

- `class BetaManagedAgentsSessionResourceNotFoundRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Skill Not Found Run Error

- `class BetaManagedAgentsSkillNotFoundRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Trigger Context

- `class BetaManagedAgentsTriggerContext`

  - `class BetaManagedAgentsScheduleTriggerContext`

    - `Type type`

    - `\Datetime scheduledAt`

      The UTC instant at which the cron expression matched in the configured timezone, before jitter is applied. At most one run is recorded per (`deployment_id`, `scheduled_at`) pair.

  - `class BetaManagedAgentsManualTriggerContext`

    - `Type type`

### Beta Managed Agents Trigger Type

- `enum BetaManagedAgentsTriggerType`

  - `"schedule"`

    The run was fired by the deployment's cron schedule.

  - `"manual"`

    The run was started manually by creating a session directly against the deployment.

### Beta Managed Agents Unknown Run Error

- `class BetaManagedAgentsUnknownRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Vault Archived Run Error

- `class BetaManagedAgentsVaultArchivedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Vault Not Found Run Error

- `class BetaManagedAgentsVaultNotFoundRunError`

  - `Type type`

  - `string message`

    Human-readable error description.

### Beta Managed Agents Workspace Archived Run Error

- `class BetaManagedAgentsWorkspaceArchivedRunError`

  - `Type type`

  - `string message`

    Human-readable error description.
