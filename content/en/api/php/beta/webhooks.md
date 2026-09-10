---
title: Webhooks
url: https://platform.claude.com/docs/en/api/php/beta/webhooks
---

# Webhooks

## Unwrap

`$client->beta->webhooks->unwrap(): void`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$result = $client->beta->webhooks->unwrap();

var_dump($result);
```

## Parse Unverified

`$client->beta->webhooks->parseUnverified(): void`

Parses a webhook payload into an event without verifying its signature. Prefer `unwrap()` unless
you have already verified the signature yourself.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$result = $client->beta->webhooks->parseUnverified();

var_dump($result);
```

## Domain types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData`

  - `"agent.archived" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData`

  - `"agent.created" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData`

  - `"agent.deleted" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData`

  - `"agent.updated" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData`

  - `"deployment.archived" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData`

  - `"deployment.created" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData`

  - `"deployment.deleted" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData`

  - `"deployment.paused" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData`

  - `"deployment_run.failed" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData`

  - `"deployment_run.started" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData`

  - `"deployment_run.succeeded" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData`

  - `"deployment.unpaused" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData`

  - `"deployment.updated" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData`

  - `"environment.archived" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData`

  - `"environment.created" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData`

  - `"environment.deleted" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData`

  - `"environment.updated" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Event

- `BetaWebhookEvent`

  - `"event" type`

    Object type. Always `event` for webhook payloads.

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `BetaWebhookSessionCreatedEventData`

    - `"session.created" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionPendingEventData`

    - `"session.pending" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionRunningEventData`

    - `"session.running" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionIdledEventData`

    - `"session.idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionRequiresActionEventData`

    - `"session.requires_action" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionArchivedEventData`

    - `"session.archived" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionDeletedEventData`

    - `"session.deleted" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `"session.status_rescheduled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `"session.status_run_started" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionStatusIdledEventData`

    - `"session.status_idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `"session.status_terminated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `"session.thread_created" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `BetaWebhookSessionThreadIdledEventData`

    - `"session.thread_idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `"session.thread_terminated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `"session.outcome_evaluation_ended" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookVaultCreatedEventData`

    - `"vault.created" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookVaultArchivedEventData`

    - `"vault.archived" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookVaultDeletedEventData`

    - `"vault.deleted" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `"vault_credential.created" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `"vault_credential.archived" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `"vault_credential.deleted" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `"vault_credential.refresh_failed" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `BetaWebhookSessionUpdatedEventData`

    - `"session.updated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookAgentCreatedEventData`

    - `"agent.created" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookAgentArchivedEventData`

    - `"agent.archived" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookAgentDeletedEventData`

    - `"agent.deleted" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentPausedEventData`

    - `"deployment.paused" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunFailedEventData`

    - `"deployment_run.failed" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentCreatedEventData`

    - `"deployment.created" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentUpdatedEventData`

    - `"deployment.updated" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentUnpausedEventData`

    - `"deployment.unpaused" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookAgentUpdatedEventData`

    - `"agent.updated" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentArchivedEventData`

    - `"deployment.archived" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunStartedEventData`

    - `"deployment_run.started" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentDeletedEventData`

    - `"deployment.deleted" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookDeploymentRunSucceededEventData`

    - `"deployment_run.succeeded" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookEnvironmentCreatedEventData`

    - `"environment.created" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookEnvironmentUpdatedEventData`

    - `"environment.updated" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookEnvironmentArchivedEventData`

    - `"environment.archived" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookEnvironmentDeletedEventData`

    - `"environment.deleted" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookMemoryStoreCreatedEventData`

    - `"memory_store.created" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookMemoryStoreArchivedEventData`

    - `"memory_store.archived" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookMemoryStoreDeletedEventData`

    - `"memory_store.deleted" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `BetaWebhookSessionBudgetReachedEventData`

    - `"session.budget_reached" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData`

  - `"memory_store.archived" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData`

  - `"memory_store.created" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData`

  - `"memory_store.deleted" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `"session.archived" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Budget Reached Event Data

- `BetaWebhookSessionBudgetReachedEventData`

  - `"session.budget_reached" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `"session.created" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `"session.deleted" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `"session.idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `"session.outcome_evaluation_ended" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `"session.pending" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `"session.requires_action" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `"session.running" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `"session.status_idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `"session.status_rescheduled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `"session.status_run_started" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `"session.status_terminated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `"session.thread_created" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `"session.thread_idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `"session.thread_terminated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData`

  - `"session.updated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `"vault.archived" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `"vault.created" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `"vault_credential.archived" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `"vault_credential.created" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `"vault_credential.deleted" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `"vault_credential.refresh_failed" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `"vault.deleted" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`
