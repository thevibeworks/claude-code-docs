---
title: Unwrap
url: https://platform.claude.com/docs/en/api/ruby/beta/webhooks/unwrap
---

# Unwrap

`beta.webhooks.unwrap(payload, headers:, key: @client.webhook_key) -> BetaWebhookEvent`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Parameters

- `payload: String`

  The body of the incoming webhook request, exactly as received: the signature is computed over these bytes.

- `headers: Hash<String, String>`

  The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.

- `key: optional String`

  The webhook signing key. Defaults to the client's `webhook_key` option.

## Returns

- `class BetaWebhookEvent`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `type: :"session.created"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `type: :"session.pending"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `type: :"session.running"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `type: :"session.idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `type: :"session.requires_action"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `type: :"session.archived"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `type: :"session.deleted"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `type: :"session.status_rescheduled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `type: :"session.status_run_started"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `type: :"session.status_idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `type: :"session.status_terminated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `type: :"session.thread_created"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `type: :"session.thread_idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `type: :"session.thread_terminated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: :"session.outcome_evaluation_ended"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `type: :"vault.created"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `type: :"vault.archived"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `type: :"vault.deleted"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `type: :"vault_credential.created"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `type: :"vault_credential.archived"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `type: :"vault_credential.deleted"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: :"vault_credential.refresh_failed"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `type: :"session.updated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `type: :"agent.created"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `type: :"agent.archived"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `type: :"agent.deleted"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `type: :"deployment.paused"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `type: :"deployment_run.failed"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `type: :"deployment.created"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `type: :"deployment.updated"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `type: :"deployment.unpaused"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `type: :"agent.updated"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `type: :"deployment.archived"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `type: :"deployment_run.started"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `type: :"deployment.deleted"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `type: :"deployment_run.succeeded"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `type: :"environment.created"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `type: :"environment.updated"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `type: :"environment.archived"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `type: :"environment.deleted"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `type: :"memory_store.created"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `type: :"memory_store.archived"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `type: :"memory_store.deleted"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `type: :"session.budget_reached"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookUserProfileEnforcementActionOpenedEventData`

      - `type: :"user_profile.enforcement_action_opened"`

      - `id: String`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: String`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: String`

    - `class BetaWebhookUserProfileEnforcementActionResolvedEventData`

      - `type: :"user_profile.enforcement_action_resolved"`

      - `id: String`

        ID of the user profile the enforcement action is on.

      - `enforcement_action_id: String`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `organization_id: String`

    - `class BetaWebhookUserProfileProgramStatusUpdatedEventData`

      - `type: :"user_profile.program_status_updated"`

      - `id: String`

        ID of the user profile that triggered the event.

      - `organization_id: String`

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

# `payload` is the raw body of the incoming webhook request and `headers` are its HTTP headers.
event = anthropic.beta.webhooks.unwrap(payload, headers: headers)

puts(event)
```
