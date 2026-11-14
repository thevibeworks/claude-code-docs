---
title: Webhooks
url: https://platform.claude.com/docs/en/api/typescript/beta/webhooks
---

# Webhooks

## Unwrap

- Signature: `client.beta.webhooks.unwrap(body: string, options: { headers: Record<string, string>; key?: string }): BetaWebhookEvent`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Replace these with the raw body and the HTTP headers of the incoming webhook request.
const body =
  '{"type":"event","id":"whe_0f1e2d3c4b5a69788796a5b4c3d2e1f0","created_at":"2026-03-15T10:00:00Z","data":{"type":"session.status_idled"}}';
const headers = {
  "webhook-id": "msg_0123456789",
  "webhook-timestamp": "1773568800",
  "webhook-signature": "v1,ZmFrZS1zaWduYXR1cmU="
};
const event = client.beta.webhooks.unwrap(body, { headers });

console.log(event);
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

/** The body of the incoming webhook request, exactly as received: the signature is computed over these bytes. */
body: string;

/**
 * - `headers: Record<string, string>`: The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.
 * - `key?: string`: The webhook signing key. Defaults to the client's `webhookKey` option.
 */
options: { headers: Record<string, string>; key?: string };
```

### Returns

```ts
interface BetaWebhookEvent {
  /** Object type. Always `event` for webhook payloads. */
  type: "event";
  /** Unique event identifier for idempotency. */
  id: string;
  /** RFC 3339 timestamp when the event occurred. */
  created_at: string; // format: date-time
  data: BetaWebhookEventData;
}
```

### Types

```ts
type BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | BetaWebhookSessionIdledEventData | BetaWebhookSessionRequiresActionEventData | BetaWebhookSessionArchivedEventData | BetaWebhookSessionDeletedEventData | BetaWebhookSessionStatusRescheduledEventData | BetaWebhookSessionStatusRunStartedEventData | BetaWebhookSessionStatusIdledEventData | BetaWebhookSessionStatusTerminatedEventData | BetaWebhookSessionThreadCreatedEventData | BetaWebhookSessionThreadIdledEventData | BetaWebhookSessionThreadTerminatedEventData | BetaWebhookSessionOutcomeEvaluationEndedEventData | BetaWebhookVaultCreatedEventData | BetaWebhookVaultArchivedEventData | BetaWebhookVaultDeletedEventData | BetaWebhookVaultCredentialCreatedEventData | BetaWebhookVaultCredentialArchivedEventData | BetaWebhookVaultCredentialDeletedEventData | BetaWebhookVaultCredentialRefreshFailedEventData | BetaWebhookSessionUpdatedEventData | BetaWebhookAgentCreatedEventData | BetaWebhookAgentArchivedEventData | BetaWebhookAgentDeletedEventData | BetaWebhookDeploymentPausedEventData | BetaWebhookDeploymentRunFailedEventData | BetaWebhookDeploymentCreatedEventData | BetaWebhookDeploymentUpdatedEventData | BetaWebhookDeploymentUnpausedEventData | BetaWebhookAgentUpdatedEventData | BetaWebhookDeploymentArchivedEventData | BetaWebhookDeploymentRunStartedEventData | BetaWebhookDeploymentDeletedEventData | BetaWebhookDeploymentRunSucceededEventData | BetaWebhookEnvironmentCreatedEventData | BetaWebhookEnvironmentUpdatedEventData | BetaWebhookEnvironmentArchivedEventData | BetaWebhookEnvironmentDeletedEventData | BetaWebhookMemoryStoreCreatedEventData | BetaWebhookMemoryStoreArchivedEventData | BetaWebhookMemoryStoreDeletedEventData | BetaWebhookSessionBudgetReachedEventData | BetaWebhookUserProfileEnforcementActionOpenedEventData | BetaWebhookUserProfileEnforcementActionResolvedEventData | BetaWebhookUserProfileProgramStatusUpdatedEventData;

interface BetaWebhookSessionCreatedEventData {
  type: "session.created";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionPendingEventData {
  type: "session.pending";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionRunningEventData {
  type: "session.running";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionIdledEventData {
  type: "session.idled";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionRequiresActionEventData {
  type: "session.requires_action";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionArchivedEventData {
  type: "session.archived";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionDeletedEventData {
  type: "session.deleted";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionStatusRescheduledEventData {
  type: "session.status_rescheduled";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionStatusRunStartedEventData {
  type: "session.status_run_started";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionStatusIdledEventData {
  type: "session.status_idled";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionStatusTerminatedEventData {
  type: "session.status_terminated";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionThreadCreatedEventData {
  type: "session.thread_created";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the session thread this event refers to. */
  session_thread_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionThreadIdledEventData {
  type: "session.thread_idled";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the session thread this event refers to. */
  session_thread_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionThreadTerminatedEventData {
  type: "session.thread_terminated";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the session thread this event refers to. */
  session_thread_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionOutcomeEvaluationEndedEventData {
  type: "session.outcome_evaluation_ended";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultCreatedEventData {
  type: "vault.created";
  /** ID of the vault that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultArchivedEventData {
  type: "vault.archived";
  /** ID of the vault that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultDeletedEventData {
  type: "vault.deleted";
  /** ID of the vault that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultCredentialCreatedEventData {
  type: "vault_credential.created";
  /** ID of the vault credential that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the vault that owns this credential. */
  vault_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultCredentialArchivedEventData {
  type: "vault_credential.archived";
  /** ID of the vault credential that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the vault that owns this credential. */
  vault_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultCredentialDeletedEventData {
  type: "vault_credential.deleted";
  /** ID of the vault credential that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the vault that owns this credential. */
  vault_id: string;
  workspace_id: string;
}

interface BetaWebhookVaultCredentialRefreshFailedEventData {
  type: "vault_credential.refresh_failed";
  /** ID of the vault credential that triggered the event. */
  id: string;
  organization_id: string;
  /** ID of the vault that owns this credential. */
  vault_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionUpdatedEventData {
  type: "session.updated";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookAgentCreatedEventData {
  type: "agent.created";
  /** ID of the agent that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookAgentArchivedEventData {
  type: "agent.archived";
  /** ID of the agent that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookAgentDeletedEventData {
  type: "agent.deleted";
  /** ID of the agent that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentPausedEventData {
  type: "deployment.paused";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentRunFailedEventData {
  type: "deployment_run.failed";
  /** ID of the deployment run that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentCreatedEventData {
  type: "deployment.created";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentUpdatedEventData {
  type: "deployment.updated";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentUnpausedEventData {
  type: "deployment.unpaused";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookAgentUpdatedEventData {
  type: "agent.updated";
  /** ID of the agent that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentArchivedEventData {
  type: "deployment.archived";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentRunStartedEventData {
  type: "deployment_run.started";
  /** ID of the deployment run that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentDeletedEventData {
  type: "deployment.deleted";
  /** ID of the deployment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookDeploymentRunSucceededEventData {
  type: "deployment_run.succeeded";
  /** ID of the deployment run that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookEnvironmentCreatedEventData {
  type: "environment.created";
  /** ID of the environment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookEnvironmentUpdatedEventData {
  type: "environment.updated";
  /** ID of the environment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookEnvironmentArchivedEventData {
  type: "environment.archived";
  /** ID of the environment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookEnvironmentDeletedEventData {
  type: "environment.deleted";
  /** ID of the environment that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookMemoryStoreCreatedEventData {
  type: "memory_store.created";
  /** ID of the memory store that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookMemoryStoreArchivedEventData {
  type: "memory_store.archived";
  /** ID of the memory store that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookMemoryStoreDeletedEventData {
  type: "memory_store.deleted";
  /** ID of the memory store that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookSessionBudgetReachedEventData {
  type: "session.budget_reached";
  /** ID of the session that triggered the event. */
  id: string;
  organization_id: string;
  workspace_id: string;
}

interface BetaWebhookUserProfileEnforcementActionOpenedEventData {
  type: "user_profile.enforcement_action_opened";
  /** ID of the user profile the enforcement action is on. */
  id: string;
  /** ID (`enac_...`) of the enforcement action that was opened or resolved. */
  enforcement_action_id: string;
  organization_id: string;
}

interface BetaWebhookUserProfileEnforcementActionResolvedEventData {
  type: "user_profile.enforcement_action_resolved";
  /** ID of the user profile the enforcement action is on. */
  id: string;
  /** ID (`enac_...`) of the enforcement action that was opened or resolved. */
  enforcement_action_id: string;
  organization_id: string;
}

interface BetaWebhookUserProfileProgramStatusUpdatedEventData {
  type: "user_profile.program_status_updated";
  /** ID of the user profile that triggered the event. */
  id: string;
  organization_id: string;
}
```

## Parse Unverified

- Signature: `client.beta.webhooks.parseUnverified(body: string): BetaWebhookEvent`

Parses a webhook payload into an event without verifying its signature. Prefer `unwrap()` unless
you have already verified the signature yourself.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Replace this with the raw body of the incoming webhook request.
const body =
  '{"type":"event","id":"whe_0f1e2d3c4b5a69788796a5b4c3d2e1f0","created_at":"2026-03-15T10:00:00Z","data":{"type":"session.status_idled"}}';
const event = client.beta.webhooks.parseUnverified(body);

console.log(event);
```

### Parameters

```ts
/** The raw JSON body of the incoming webhook request. */
body: string;
```
