---
title: Webhooks
url: https://platform.claude.com/docs/en/api/typescript/beta/webhooks
---

# Webhooks

## Unwrap

`client.beta.webhooks.unwrap(options?): void`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

await client.beta.webhooks.unwrap();
```

## Parse Unverified

`client.beta.webhooks.parseUnverified(options?): void`

Parses a webhook payload into an event without verifying its signature. Prefer `unwrap()` unless
you have already verified the signature yourself.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

await client.beta.webhooks.parseUnverified();
```

## Domain types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData`

  - `type: "agent.archived"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData`

  - `type: "agent.created"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData`

  - `type: "agent.deleted"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData`

  - `type: "agent.updated"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData`

  - `type: "deployment.archived"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData`

  - `type: "deployment.created"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData`

  - `type: "deployment.deleted"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData`

  - `type: "deployment.paused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData`

  - `type: "deployment_run.failed"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData`

  - `type: "deployment_run.started"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData`

  - `type: "deployment_run.succeeded"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData`

  - `type: "deployment.unpaused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData`

  - `type: "deployment.updated"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData`

  - `type: "environment.archived"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData`

  - `type: "environment.created"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData`

  - `type: "environment.deleted"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData`

  - `type: "environment.updated"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `type: "session.created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `type: "session.pending"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `type: "session.running"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `type: "session.idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `type: "session.requires_action"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `type: "session.archived"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `type: "session.deleted"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `type: "session.status_rescheduled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `type: "session.status_run_started"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `type: "session.status_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `type: "session.status_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `type: "session.thread_created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `type: "session.thread_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `type: "session.thread_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: "session.outcome_evaluation_ended"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `type: "vault.created"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `type: "vault.archived"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `type: "vault.deleted"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `type: "vault_credential.created"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `type: "vault_credential.archived"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `type: "vault_credential.deleted"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: "vault_credential.refresh_failed"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData`

      - `type: "session.updated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData`

      - `type: "agent.created"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData`

      - `type: "agent.archived"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData`

      - `type: "agent.deleted"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData`

      - `type: "deployment.paused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData`

      - `type: "deployment_run.failed"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData`

      - `type: "deployment.created"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData`

      - `type: "deployment.updated"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData`

      - `type: "deployment.unpaused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData`

      - `type: "agent.updated"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData`

      - `type: "deployment.archived"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData`

      - `type: "deployment_run.started"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData`

      - `type: "deployment.deleted"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData`

      - `type: "deployment_run.succeeded"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData`

      - `type: "environment.created"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData`

      - `type: "environment.updated"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData`

      - `type: "environment.archived"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData`

      - `type: "environment.deleted"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData`

      - `type: "memory_store.created"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData`

      - `type: "memory_store.archived"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData`

      - `type: "memory_store.deleted"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData`

      - `type: "session.budget_reached"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `BetaWebhookSessionCreatedEventData`

    - `type: "session.created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData`

    - `type: "session.pending"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData`

    - `type: "session.running"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData`

    - `type: "session.idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData`

    - `type: "session.requires_action"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData`

    - `type: "session.archived"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData`

    - `type: "session.deleted"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `type: "session.status_rescheduled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `type: "session.status_run_started"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData`

    - `type: "session.status_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `type: "session.status_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `type: "session.thread_created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData`

    - `type: "session.thread_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `type: "session.thread_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `type: "session.outcome_evaluation_ended"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData`

    - `type: "vault.created"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData`

    - `type: "vault.archived"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData`

    - `type: "vault.deleted"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `type: "vault_credential.created"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `type: "vault_credential.archived"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `type: "vault_credential.deleted"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `type: "vault_credential.refresh_failed"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData`

    - `type: "session.updated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData`

    - `type: "agent.created"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData`

    - `type: "agent.archived"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData`

    - `type: "agent.deleted"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData`

    - `type: "deployment.paused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData`

    - `type: "deployment_run.failed"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData`

    - `type: "deployment.created"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData`

    - `type: "deployment.updated"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData`

    - `type: "deployment.unpaused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData`

    - `type: "agent.updated"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData`

    - `type: "deployment.archived"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData`

    - `type: "deployment_run.started"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData`

    - `type: "deployment.deleted"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData`

    - `type: "deployment_run.succeeded"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData`

    - `type: "environment.created"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData`

    - `type: "environment.updated"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData`

    - `type: "environment.archived"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData`

    - `type: "environment.deleted"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData`

    - `type: "memory_store.created"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData`

    - `type: "memory_store.archived"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData`

    - `type: "memory_store.deleted"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionBudgetReachedEventData`

    - `type: "session.budget_reached"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData`

  - `type: "memory_store.archived"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData`

  - `type: "memory_store.created"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData`

  - `type: "memory_store.deleted"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `type: "session.archived"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `BetaWebhookSessionBudgetReachedEventData`

  - `type: "session.budget_reached"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `type: "session.created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `type: "session.deleted"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `type: "session.idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `type: "session.outcome_evaluation_ended"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `type: "session.pending"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `type: "session.requires_action"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `type: "session.running"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `type: "session.status_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `type: "session.status_rescheduled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `type: "session.status_run_started"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `type: "session.status_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `type: "session.thread_created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `type: "session.thread_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `type: "session.thread_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData`

  - `type: "session.updated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `type: "vault.archived"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `type: "vault.created"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `type: "vault_credential.archived"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `type: "vault_credential.created"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `type: "vault_credential.deleted"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `type: "vault_credential.refresh_failed"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `type: "vault.deleted"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`
