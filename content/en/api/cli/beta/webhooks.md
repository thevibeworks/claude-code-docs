---
title: Webhooks
url: https://platform.claude.com/docs/en/api/cli/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `beta_webhook_agent_archived_event_data: object`

  - `type: "agent.archived"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `beta_webhook_agent_created_event_data: object`

  - `type: "agent.created"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `beta_webhook_agent_deleted_event_data: object`

  - `type: "agent.deleted"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `beta_webhook_agent_updated_event_data: object`

  - `type: "agent.updated"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `beta_webhook_deployment_archived_event_data: object`

  - `type: "deployment.archived"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `beta_webhook_deployment_created_event_data: object`

  - `type: "deployment.created"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `beta_webhook_deployment_deleted_event_data: object`

  - `type: "deployment.deleted"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `beta_webhook_deployment_paused_event_data: object`

  - `type: "deployment.paused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `beta_webhook_deployment_run_failed_event_data: object`

  - `type: "deployment_run.failed"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `beta_webhook_deployment_run_started_event_data: object`

  - `type: "deployment_run.started"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `beta_webhook_deployment_run_succeeded_event_data: object`

  - `type: "deployment_run.succeeded"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `beta_webhook_deployment_unpaused_event_data: object`

  - `type: "deployment.unpaused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `beta_webhook_deployment_updated_event_data: object`

  - `type: "deployment.updated"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `beta_webhook_environment_archived_event_data: object`

  - `type: "environment.archived"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `beta_webhook_environment_created_event_data: object`

  - `type: "environment.created"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `beta_webhook_environment_deleted_event_data: object`

  - `type: "environment.deleted"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `beta_webhook_environment_updated_event_data: object`

  - `type: "environment.updated"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Event

- `beta_webhook_event: object`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 41 more`

    - `beta_webhook_session_created_event_data: object`

      - `type: "session.created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object`

      - `type: "session.pending"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object`

      - `type: "session.running"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object`

      - `type: "session.idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object`

      - `type: "session.requires_action"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object`

      - `type: "session.archived"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object`

      - `type: "session.deleted"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_status_rescheduled_event_data: object`

      - `type: "session.status_rescheduled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object`

      - `type: "session.status_run_started"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object`

      - `type: "session.status_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object`

      - `type: "session.status_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object`

      - `type: "session.thread_created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object`

      - `type: "session.thread_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object`

      - `type: "session.thread_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object`

      - `type: "session.outcome_evaluation_ended"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object`

      - `type: "vault.created"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object`

      - `type: "vault.archived"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object`

      - `type: "vault.deleted"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object`

      - `type: "vault_credential.created"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object`

      - `type: "vault_credential.archived"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object`

      - `type: "vault_credential.deleted"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object`

      - `type: "vault_credential.refresh_failed"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_session_updated_event_data: object`

      - `type: "session.updated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_agent_created_event_data: object`

      - `type: "agent.created"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_agent_archived_event_data: object`

      - `type: "agent.archived"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_agent_deleted_event_data: object`

      - `type: "agent.deleted"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_paused_event_data: object`

      - `type: "deployment.paused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_failed_event_data: object`

      - `type: "deployment_run.failed"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_created_event_data: object`

      - `type: "deployment.created"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_updated_event_data: object`

      - `type: "deployment.updated"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_unpaused_event_data: object`

      - `type: "deployment.unpaused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_agent_updated_event_data: object`

      - `type: "agent.updated"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_archived_event_data: object`

      - `type: "deployment.archived"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_started_event_data: object`

      - `type: "deployment_run.started"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_deleted_event_data: object`

      - `type: "deployment.deleted"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_succeeded_event_data: object`

      - `type: "deployment_run.succeeded"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_environment_created_event_data: object`

      - `type: "environment.created"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_environment_updated_event_data: object`

      - `type: "environment.updated"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_environment_archived_event_data: object`

      - `type: "environment.archived"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_environment_deleted_event_data: object`

      - `type: "environment.deleted"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_memory_store_created_event_data: object`

      - `type: "memory_store.created"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_memory_store_archived_event_data: object`

      - `type: "memory_store.archived"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_memory_store_deleted_event_data: object`

      - `type: "memory_store.deleted"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `beta_webhook_session_budget_reached_event_data: object`

      - `type: "session.budget_reached"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

### Beta Webhook Event Data

- `beta_webhook_event_data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 41 more`

  - `beta_webhook_session_created_event_data: object`

    - `type: "session.created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_pending_event_data: object`

    - `type: "session.pending"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_running_event_data: object`

    - `type: "session.running"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_idled_event_data: object`

    - `type: "session.idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_requires_action_event_data: object`

    - `type: "session.requires_action"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_archived_event_data: object`

    - `type: "session.archived"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_deleted_event_data: object`

    - `type: "session.deleted"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_status_rescheduled_event_data: object`

    - `type: "session.status_rescheduled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_status_run_started_event_data: object`

    - `type: "session.status_run_started"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_status_idled_event_data: object`

    - `type: "session.status_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_status_terminated_event_data: object`

    - `type: "session.status_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_thread_created_event_data: object`

    - `type: "session.thread_created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `beta_webhook_session_thread_idled_event_data: object`

    - `type: "session.thread_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `beta_webhook_session_thread_terminated_event_data: object`

    - `type: "session.thread_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `beta_webhook_session_outcome_evaluation_ended_event_data: object`

    - `type: "session.outcome_evaluation_ended"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_vault_created_event_data: object`

    - `type: "vault.created"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_vault_archived_event_data: object`

    - `type: "vault.archived"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_vault_deleted_event_data: object`

    - `type: "vault.deleted"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_vault_credential_created_event_data: object`

    - `type: "vault_credential.created"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_archived_event_data: object`

    - `type: "vault_credential.archived"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_deleted_event_data: object`

    - `type: "vault_credential.deleted"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_refresh_failed_event_data: object`

    - `type: "vault_credential.refresh_failed"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_session_updated_event_data: object`

    - `type: "session.updated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_agent_created_event_data: object`

    - `type: "agent.created"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_agent_archived_event_data: object`

    - `type: "agent.archived"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_agent_deleted_event_data: object`

    - `type: "agent.deleted"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_paused_event_data: object`

    - `type: "deployment.paused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_failed_event_data: object`

    - `type: "deployment_run.failed"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_created_event_data: object`

    - `type: "deployment.created"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_updated_event_data: object`

    - `type: "deployment.updated"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_unpaused_event_data: object`

    - `type: "deployment.unpaused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_agent_updated_event_data: object`

    - `type: "agent.updated"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_archived_event_data: object`

    - `type: "deployment.archived"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_started_event_data: object`

    - `type: "deployment_run.started"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_deleted_event_data: object`

    - `type: "deployment.deleted"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_succeeded_event_data: object`

    - `type: "deployment_run.succeeded"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_environment_created_event_data: object`

    - `type: "environment.created"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_environment_updated_event_data: object`

    - `type: "environment.updated"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_environment_archived_event_data: object`

    - `type: "environment.archived"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_environment_deleted_event_data: object`

    - `type: "environment.deleted"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_memory_store_created_event_data: object`

    - `type: "memory_store.created"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_memory_store_archived_event_data: object`

    - `type: "memory_store.archived"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_memory_store_deleted_event_data: object`

    - `type: "memory_store.deleted"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `beta_webhook_session_budget_reached_event_data: object`

    - `type: "session.budget_reached"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `beta_webhook_memory_store_archived_event_data: object`

  - `type: "memory_store.archived"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `beta_webhook_memory_store_created_event_data: object`

  - `type: "memory_store.created"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `beta_webhook_memory_store_deleted_event_data: object`

  - `type: "memory_store.deleted"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `beta_webhook_session_archived_event_data: object`

  - `type: "session.archived"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `beta_webhook_session_budget_reached_event_data: object`

  - `type: "session.budget_reached"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `beta_webhook_session_created_event_data: object`

  - `type: "session.created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `beta_webhook_session_deleted_event_data: object`

  - `type: "session.deleted"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `beta_webhook_session_idled_event_data: object`

  - `type: "session.idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `beta_webhook_session_outcome_evaluation_ended_event_data: object`

  - `type: "session.outcome_evaluation_ended"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `beta_webhook_session_pending_event_data: object`

  - `type: "session.pending"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `beta_webhook_session_requires_action_event_data: object`

  - `type: "session.requires_action"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `beta_webhook_session_running_event_data: object`

  - `type: "session.running"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `beta_webhook_session_status_idled_event_data: object`

  - `type: "session.status_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `beta_webhook_session_status_rescheduled_event_data: object`

  - `type: "session.status_rescheduled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `beta_webhook_session_status_run_started_event_data: object`

  - `type: "session.status_run_started"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `beta_webhook_session_status_terminated_event_data: object`

  - `type: "session.status_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `beta_webhook_session_thread_created_event_data: object`

  - `type: "session.thread_created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `beta_webhook_session_thread_idled_event_data: object`

  - `type: "session.thread_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `beta_webhook_session_thread_terminated_event_data: object`

  - `type: "session.thread_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `beta_webhook_session_updated_event_data: object`

  - `type: "session.updated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `beta_webhook_vault_archived_event_data: object`

  - `type: "vault.archived"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `beta_webhook_vault_created_event_data: object`

  - `type: "vault.created"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `beta_webhook_vault_credential_archived_event_data: object`

  - `type: "vault_credential.archived"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `beta_webhook_vault_credential_created_event_data: object`

  - `type: "vault_credential.created"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `beta_webhook_vault_credential_deleted_event_data: object`

  - `type: "vault_credential.deleted"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `beta_webhook_vault_credential_refresh_failed_event_data: object`

  - `type: "vault_credential.refresh_failed"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `beta_webhook_vault_deleted_event_data: object`

  - `type: "vault.deleted"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`
