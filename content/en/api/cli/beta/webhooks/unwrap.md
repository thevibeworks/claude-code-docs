---
title: Unwrap
url: https://platform.claude.com/docs/en/api/cli/beta/webhooks/unwrap
---

# Unwrap

`client.beta.webhooks.unwrap(body, options): BetaWebhookEvent`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Parameters

- `body: string`

  The body of the incoming webhook request, exactly as received: the signature is computed over these bytes.

- `options: { headers: Record<string, string>, key?: string}`

  - `headers: Record<string, string>`

    The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.

  - `key?: string`

    The webhook signing key. Defaults to the client's `webhookKey` option.

## Returns

- `interface BetaWebhookEvent`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `interface BetaWebhookSessionCreatedEventData`

      - `type: "session.created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionPendingEventData`

      - `type: "session.pending"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionRunningEventData`

      - `type: "session.running"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionIdledEventData`

      - `type: "session.idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionRequiresActionEventData`

      - `type: "session.requires_action"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionArchivedEventData`

      - `type: "session.archived"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionDeletedEventData`

      - `type: "session.deleted"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusRescheduledEventData`

      - `type: "session.status_rescheduled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusRunStartedEventData`

      - `type: "session.status_run_started"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusIdledEventData`

      - `type: "session.status_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusTerminatedEventData`

      - `type: "session.status_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadCreatedEventData`

      - `type: "session.thread_created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadIdledEventData`

      - `type: "session.thread_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadTerminatedEventData`

      - `type: "session.thread_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: "session.outcome_evaluation_ended"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultCreatedEventData`

      - `type: "vault.created"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultArchivedEventData`

      - `type: "vault.archived"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultDeletedEventData`

      - `type: "vault.deleted"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialCreatedEventData`

      - `type: "vault_credential.created"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialArchivedEventData`

      - `type: "vault_credential.archived"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialDeletedEventData`

      - `type: "vault_credential.deleted"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: "vault_credential.refresh_failed"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookSessionUpdatedEventData`

      - `type: "session.updated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentCreatedEventData`

      - `type: "agent.created"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentArchivedEventData`

      - `type: "agent.archived"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentDeletedEventData`

      - `type: "agent.deleted"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentPausedEventData`

      - `type: "deployment.paused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunFailedEventData`

      - `type: "deployment_run.failed"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentCreatedEventData`

      - `type: "deployment.created"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentUpdatedEventData`

      - `type: "deployment.updated"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentUnpausedEventData`

      - `type: "deployment.unpaused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentUpdatedEventData`

      - `type: "agent.updated"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentArchivedEventData`

      - `type: "deployment.archived"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunStartedEventData`

      - `type: "deployment_run.started"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentDeletedEventData`

      - `type: "deployment.deleted"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunSucceededEventData`

      - `type: "deployment_run.succeeded"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentCreatedEventData`

      - `type: "environment.created"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentUpdatedEventData`

      - `type: "environment.updated"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentArchivedEventData`

      - `type: "environment.archived"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentDeletedEventData`

      - `type: "environment.deleted"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreCreatedEventData`

      - `type: "memory_store.created"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreArchivedEventData`

      - `type: "memory_store.archived"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreDeletedEventData`

      - `type: "memory_store.deleted"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionBudgetReachedEventData`

      - `type: "session.budget_reached"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookUserProfileEnforcementActionOpenedEventData`

      - `type: "user_profile.enforcement_action_opened"`

      - `id: string`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: string`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: string`

    - `interface BetaWebhookUserProfileEnforcementActionResolvedEventData`

      - `type: "user_profile.enforcement_action_resolved"`

      - `id: string`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: string`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: string`

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// `body` is the raw body of the incoming webhook request and `headers` are its HTTP headers.
const event = client.beta.webhooks.unwrap(body, { headers });

console.log(event);
```
