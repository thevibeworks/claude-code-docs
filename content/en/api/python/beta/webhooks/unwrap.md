---
title: Unwrap
url: https://platform.claude.com/docs/en/api/python/beta/webhooks/unwrap
---

# Unwrap

`beta.webhooks.unwrap(payload, headers, key) -> BetaWebhookEvent`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Parameters

- `payload: str`

  The body of the incoming webhook request, exactly as received: the signature is computed over these bytes.

- `headers: Mapping[str, str]`

  The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.

- `key: Optional[Union[str, bytes]]`

  The webhook signing key. Defaults to the client's `webhook_key` option.

## Returns

- `class BetaWebhookEvent`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `type: Literal["session.created"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData`

      - `type: Literal["session.pending"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData`

      - `type: Literal["session.running"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData`

      - `type: Literal["session.idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `type: Literal["session.requires_action"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData`

      - `type: Literal["session.archived"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData`

      - `type: Literal["session.deleted"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `type: Literal["session.status_rescheduled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `type: Literal["session.status_run_started"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `type: Literal["session.status_idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `type: Literal["session.status_terminated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `type: Literal["session.thread_created"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `type: Literal["session.thread_idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `type: Literal["session.thread_terminated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: Literal["session.outcome_evaluation_ended"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData`

      - `type: Literal["vault.created"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData`

      - `type: Literal["vault.archived"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData`

      - `type: Literal["vault.deleted"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `type: Literal["vault_credential.created"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `type: Literal["vault_credential.archived"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `type: Literal["vault_credential.deleted"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: Literal["vault_credential.refresh_failed"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData`

      - `type: Literal["session.updated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData`

      - `type: Literal["agent.created"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData`

      - `type: Literal["agent.archived"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData`

      - `type: Literal["agent.deleted"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData`

      - `type: Literal["deployment.paused"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `type: Literal["deployment_run.failed"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `type: Literal["deployment.created"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `type: Literal["deployment.updated"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `type: Literal["deployment.unpaused"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData`

      - `type: Literal["agent.updated"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `type: Literal["deployment.archived"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `type: Literal["deployment_run.started"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `type: Literal["deployment.deleted"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `type: Literal["deployment_run.succeeded"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `type: Literal["environment.created"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `type: Literal["environment.updated"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `type: Literal["environment.archived"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `type: Literal["environment.deleted"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `type: Literal["memory_store.created"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `type: Literal["memory_store.archived"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `type: Literal["memory_store.deleted"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `type: Literal["session.budget_reached"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookUserProfileEnforcementActionOpenedEventData`

      - `type: Literal["user_profile.enforcement_action_opened"]`

      - `id: str`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: str`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: str`

    - `class BetaWebhookUserProfileEnforcementActionResolvedEventData`

      - `type: Literal["user_profile.enforcement_action_resolved"]`

      - `id: str`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: str`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: str`

    - `class BetaWebhookUserProfileProgramStatusUpdatedEventData`

      - `type: Literal["user_profile.program_status_updated"]`

      - `id: str`

        ID of the user profile that triggered the event.

      - `organization_id: str`

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
# `payload` is the raw body of the incoming webhook request and `headers` are its HTTP headers.
event = client.beta.webhooks.unwrap(
    payload,
    headers=headers,
)
print(event)
```
