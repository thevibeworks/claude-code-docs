---
title: Analytics
url: https://platform.claude.com/docs/en/api/organization/analytics
---

# Analytics

## Domain types

### Analytics Artifact Activity

- `AnalyticsArtifactActivity object`

  Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket
  on a given day.

  Artifacts form a small finite cube — the canonical MIME type (8 values incl.
  `other`) crossed with shared-vs-private — so the response is the full set of
  non-empty buckets, not a ranked/paginated list. Claude Code and Cowork
  artifacts report under `text/html` and are counted from 2026-08-17
  onward; earlier days contain claude.ai chat artifacts only. With
  `group_by[]=product` / `user_id` / `rbac_group_id` each row is further
  split by the flat group keys and counts are scoped to that cut.

  - `artifact_type: string`

    Canonical artifact MIME type (e.g. `text/markdown`, `application/vnd.ant.react`, `image/svg+xml`), or `other`. Claude Code and Cowork artifacts report as `text/html`.

  - `artifacts_created_count: number`

    Number of artifacts created in this bucket on the requested day

  - `distinct_user_count: number`

    Number of distinct users who created artifacts in this bucket on the requested day

  - `is_shared: boolean`

    Whether the artifacts in this bucket have ever been shared (a Claude Code / Cowork artifact is shared once anyone beyond its creator may open it: named members, the whole organization, or anyone with the link).

  - `published_artifacts_created_count: number`

    Number of those artifacts that have been published (for Claude Code / Cowork artifacts: open to anyone with the link); never exceeds `artifacts_created_count`

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

### Analytics Artifact Group By

- `AnalyticsArtifactGroupBy = "product" or "rbac_group_id" or "user_id"`

  A dimension to group artifact activity by.

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

### Analytics Chat Cowork Unified Chat Metrics

- `AnalyticsChatCoworkUnifiedChatMetrics object`

  Chat activity recorded while members had Chat and Cowork unified turned
  on.

  - `connectors_used_count: number`

    Same measure as `chat_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `distinct_artifacts_created_count: number`

    Same measure as `chat_metrics.distinct_artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `distinct_connectors_used_count: number or null`

    Same measure as `chat_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_conversation_count: number or null`

    Same measure as `chat_metrics.distinct_conversation_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_files_uploaded_count: number or null`

    Same measure as `chat_metrics.distinct_files_uploaded_count`, for activity recorded while members had Chat and Cowork unified turned on. It counts uploaded files as well as files Claude created and images returned by Claude's tools, such as screenshots. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_projects_created_count: number`

    Same measure as `chat_metrics.distinct_projects_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `distinct_projects_used_count: number or null`

    Same measure as `chat_metrics.distinct_projects_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_shared_artifacts_viewed_count: number or null`

    Always null: shared-artifact views are not currently measured.

  - `distinct_skills_used_count: number or null`

    Same measure as `chat_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Same measure as `chat_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `shared_conversations_viewed_count: number`

    Same measure as `chat_metrics.shared_conversations_viewed_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `thinking_message_count: number`

    Same measure as `chat_metrics.thinking_message_count`, for activity recorded while members had Chat and Cowork unified turned on.

### Analytics Chat Cowork Unified Metrics

- `AnalyticsChatCoworkUnifiedMetrics object`

  Activity in Chat and Cowork unified for one user on one day: `chat` holds
  chat activity and `sessions` holds Cowork session activity.

  - `chat: AnalyticsChatCoworkUnifiedChatMetrics`

    Chat activity recorded while members had Chat and Cowork unified turned
    on.

    - `connectors_used_count: number`

      Same measure as `chat_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `distinct_artifacts_created_count: number`

      Same measure as `chat_metrics.distinct_artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_connectors_used_count: number or null`

      Same measure as `chat_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_conversation_count: number or null`

      Same measure as `chat_metrics.distinct_conversation_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_files_uploaded_count: number or null`

      Same measure as `chat_metrics.distinct_files_uploaded_count`, for activity recorded while members had Chat and Cowork unified turned on. It counts uploaded files as well as files Claude created and images returned by Claude's tools, such as screenshots. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_projects_created_count: number`

      Same measure as `chat_metrics.distinct_projects_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Same measure as `chat_metrics.distinct_projects_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_shared_artifacts_viewed_count: number or null`

      Always null: shared-artifact views are not currently measured.

    - `distinct_skills_used_count: number or null`

      Same measure as `chat_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Same measure as `chat_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `shared_conversations_viewed_count: number`

      Same measure as `chat_metrics.shared_conversations_viewed_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `thinking_message_count: number`

      Same measure as `chat_metrics.thinking_message_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `sessions: AnalyticsChatCoworkUnifiedSessionsMetrics`

    Cowork session activity recorded while members had Chat and Cowork
    unified turned on.

    - `action_count: number`

      Same measure as `cowork_metrics.action_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `artifacts_created_count: number`

      Same measure as `cowork_metrics.artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `connectors_used_count: number`

      Same measure as `cowork_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `dispatch_turn_count: number`

      Same measure as `cowork_metrics.dispatch_turn_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `distinct_connectors_used_count: number or null`

      Same measure as `cowork_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_plugins_used_count: number or null`

      Same measure as `cowork_metrics.distinct_plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Same measure as `cowork_metrics.distinct_session_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Same measure as `cowork_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `edit_tool_count: number or null`

      Same measure as `cowork_metrics.edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `file_edit_count: number or null`

      Same measure as `cowork_metrics.file_edit_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `message_count: number`

      Same measure as `cowork_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `multi_edit_tool_count: number or null`

      Same measure as `cowork_metrics.multi_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on. Claude no longer has a multi-edit tool, so expect 0 when not null; each edit is now a separate Edit tool call, counted in `edit_tool_count` and `file_edit_count`.

    - `notebook_edit_tool_count: number or null`

      Same measure as `cowork_metrics.notebook_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `plugins_used_count: number or null`

      Same measure as `cowork_metrics.plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `sessions_with_file_edits_count: number or null`

      Same measure as `cowork_metrics.sessions_with_file_edits_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `skills_used_count: number`

      Same measure as `cowork_metrics.skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `write_tool_count: number or null`

      Same measure as `cowork_metrics.write_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

### Analytics Chat Cowork Unified Sessions Metrics

- `AnalyticsChatCoworkUnifiedSessionsMetrics object`

  Cowork session activity recorded while members had Chat and Cowork
  unified turned on.

  - `action_count: number`

    Same measure as `cowork_metrics.action_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `artifacts_created_count: number`

    Same measure as `cowork_metrics.artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `connectors_used_count: number`

    Same measure as `cowork_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `dispatch_turn_count: number`

    Same measure as `cowork_metrics.dispatch_turn_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `distinct_connectors_used_count: number or null`

    Same measure as `cowork_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_plugins_used_count: number or null`

    Same measure as `cowork_metrics.distinct_plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number or null`

    Same measure as `cowork_metrics.distinct_session_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number or null`

    Same measure as `cowork_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `edit_tool_count: number or null`

    Same measure as `cowork_metrics.edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `file_edit_count: number or null`

    Same measure as `cowork_metrics.file_edit_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `message_count: number`

    Same measure as `cowork_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `multi_edit_tool_count: number or null`

    Same measure as `cowork_metrics.multi_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on. Claude no longer has a multi-edit tool, so expect 0 when not null; each edit is now a separate Edit tool call, counted in `edit_tool_count` and `file_edit_count`.

  - `notebook_edit_tool_count: number or null`

    Same measure as `cowork_metrics.notebook_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `plugins_used_count: number or null`

    Same measure as `cowork_metrics.plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `sessions_with_file_edits_count: number or null`

    Same measure as `cowork_metrics.sessions_with_file_edits_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `skills_used_count: number`

    Same measure as `cowork_metrics.skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `write_tool_count: number or null`

    Same measure as `cowork_metrics.write_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

### Analytics Chat Metrics

- `AnalyticsChatMetrics object`

  Claude.ai activity metrics for a single user on a given day.

  - `connectors_used_count: number`

    Number of MCP connector invocations.

  - `distinct_artifacts_created_count: number`

    Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `distinct_connectors_used_count: number or null`

    Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_conversation_count: number or null`

    Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_files_uploaded_count: number or null`

    Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_projects_created_count: number`

    Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `distinct_projects_used_count: number or null`

    Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_shared_artifacts_viewed_count: number or null`

    Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number or null`

    Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent

  - `shared_conversations_viewed_count: number`

    Number of times the user opened a shared conversation in a project

  - `thinking_message_count: number`

    Number of messages that used extended thinking

### Analytics Claude Code Metrics

- `AnalyticsClaudeCodeMetrics object`

  Claude Code activity metrics for a single user on a given day.

  - `core_metrics: AnalyticsCoreCodeMetrics`

    Core Claude Code activity metrics for a single user on a given day.

    - `artifacts_created_count: number`

      Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `commit_count: number`

      Number of commits made via Claude Code

    - `distinct_session_count: number or null`

      Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

    - `lines_of_code: AnalyticsLinesOfCode`

      Lines of code added and removed via Claude Code.

      - `added_count: number`

        Lines of code added

      - `removed_count: number`

        Lines of code removed

    - `pull_request_count: number`

      Number of pull requests created via Claude Code

  - `tool_actions: AnalyticsToolActions`

    Per-tool accepted/rejected counts for Claude Code file modification tools.

    - `edit_tool: AnalyticsToolActionCounts`

      Accepted/rejected counts for a single Claude Code tool type.

      - `accepted_count: number`

        Number of tool proposals accepted

      - `rejected_count: number`

        Number of tool proposals rejected

    - `multi_edit_tool: AnalyticsToolActionCounts`

      Accepted/rejected counts for a single Claude Code tool type.

    - `notebook_edit_tool: AnalyticsToolActionCounts`

      Accepted/rejected counts for a single Claude Code tool type.

    - `write_tool: AnalyticsToolActionCounts`

      Accepted/rejected counts for a single Claude Code tool type.

### Analytics Claude Tag Metrics

- `AnalyticsClaudeTagMetrics object`

  Claude Tag activity metrics for a single linked user on a given day.

  - `active_day_count: number or null`

    1 on a day the user was active in Claude Tag in Slack, otherwise 0. Summed over the window in date-range mode, so it is the number of active days; on grouped rows, the total of each member's active days. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

  - `active_message_count: number or null`

    Number of the user's Slack messages that made them active: @-mentions, direct messages, group direct message asks, and thread posts Claude answered. Other messages are not counted. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

### Analytics Connector Activity

- `AnalyticsConnectorActivity object`

  Per-connector activity data for a given day.

  - `chat_metrics: AnalyticsConnectorChatMetrics`

    Claude.ai activity metrics for a single connector on a given day.

    - `distinct_conversation_connector_used_count: number or null`

      Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsConnectorClaudeCodeMetrics`

    Claude Code activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `connector_display_name: string or null`

    Human-readable display name for rows whose `connector_name` is an opaque connector id rather than a readable name, resolved at request time from the organization's connectors (including connectors that have since been removed). `connector_name` remains the row's stable key for sorting and pagination, and `filter[]=connector_name:{value}` also matches these rows by display name. Display names are not unique, and the same connector's claude.ai usage can appear under a separate row with a readable `connector_name`. Null when `connector_name` is already a readable name, when the id cannot be resolved to one of the organization's connectors, or when display-name resolution is not enabled for this organization.

  - `connector_name: string`

    Name of the connector. Some rows carry an opaque connector id here instead of a readable name; `connector_display_name` holds the resolved name for those rows.

  - `cowork_metrics: AnalyticsConnectorCoworkMetrics`

    Cowork activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `individual_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on their own individual credential, connected through their own consent flow. Companion bucket to `managed_auth_distinct_user_count`, which carries the measurement, attribution, and null rules. Users whose requests used no stored credential count in neither bucket.

  - `managed_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on Enterprise Managed Auth (an organization-managed credential provisioned through the organization's identity provider), read from the token record each request used. Null, never 0, when managed-auth reporting is not enabled for the organization, the value cannot be attributed to the row, no credentialed requests and no managed-token mint events (a managed credential being provisioned for a user's use of the connector) were observed that day, or the day predates 2026-07-01, the first day the backing data exists (forward-only data, no backfill). When credentialed requests or mint events were observed and attributed, both managed-auth fields populate, reporting 0 for a bucket with no users; the two counts are independent, not a partition — a user whose requests that day used both kinds of credential counts in both. Mint events carry user but not surface attribution, so they count as observed auth activity on `user_id` and `rbac_group_id` cuts — attributed to the user the credential was provisioned for — but never on a cut that references `product` (group or filter). Date-range rollup mode (`starting_date`/`ending_date`) computes both fields exactly over the window — distinct users with at least one qualifying day — when the whole window starts on or after 2026-07-01, with the null-versus-0 and mint-event rules applying with the window in place of the day; a range starting earlier reports every managed-auth field as null, never a partial-window value.

  - `office_metrics: AnalyticsConnectorOfficeMetrics`

    Office Agent activity metrics for a single connector on a given day, broken out by Office product.

    - `excel: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

      - `distinct_session_connector_used_count: number or null`

        Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `powerpoint: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `word: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

  - `read_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of `read_call_count`, `write_call_count`, or `unclassified_call_count`, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in `unclassified_call_count`). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (`starting_date`/`ending_date`) applies both rules server-side.

  - `unclassified_call_count: number or null`

    Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `write_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `chat_cowork_unified_metrics: optional AnalyticsConnectorChatCoworkUnifiedMetrics or null`

    Connector use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsConnectorChatCoworkUnifiedChatMetrics`

      A connector's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_connector_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsConnectorChatCoworkUnifiedSessionsMetrics`

      A connector's use in Cowork sessions recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_session_connector_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

### Analytics Connector Chat Cowork Unified Chat Metrics

- `AnalyticsConnectorChatCoworkUnifiedChatMetrics object`

  A connector's use in chat conversations recorded while members had
  Chat and Cowork unified turned on.

  - `distinct_conversation_connector_used_count: number or null`

    Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Chat Cowork Unified Metrics

- `AnalyticsConnectorChatCoworkUnifiedMetrics object`

  A connector's use in Chat and Cowork unified on one day: `chat` holds its
  use in chat conversations and `sessions` its use in Cowork sessions.

  - `chat: AnalyticsConnectorChatCoworkUnifiedChatMetrics`

    A connector's use in chat conversations recorded while members had
    Chat and Cowork unified turned on.

    - `distinct_conversation_connector_used_count: number or null`

      Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `sessions: AnalyticsConnectorChatCoworkUnifiedSessionsMetrics`

    A connector's use in Cowork sessions recorded while members had
    Chat and Cowork unified turned on.

    - `distinct_session_connector_used_count: number or null`

      Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Chat Cowork Unified Sessions Metrics

- `AnalyticsConnectorChatCoworkUnifiedSessionsMetrics object`

  A connector's use in Cowork sessions recorded while members had
  Chat and Cowork unified turned on.

  - `distinct_session_connector_used_count: number or null`

    Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Chat Metrics

- `AnalyticsConnectorChatMetrics object`

  Claude.ai activity metrics for a single connector on a given day.

  - `distinct_conversation_connector_used_count: number or null`

    Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Claude Code Metrics

- `AnalyticsConnectorClaudeCodeMetrics object`

  Claude Code activity metrics for a single connector on a given day.

  - `distinct_session_connector_used_count: number or null`

    Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Cowork Metrics

- `AnalyticsConnectorCoworkMetrics object`

  Cowork activity metrics for a single connector on a given day.

  - `distinct_session_connector_used_count: number or null`

    Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Connector Group By

- `AnalyticsConnectorGroupBy = "product" or "rbac_group_id" or "user_id"`

  A dimension to group connector activity by.

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

### Analytics Connector Office Metrics

- `AnalyticsConnectorOfficeMetrics object`

  Office Agent activity metrics for a single connector on a given day, broken out by Office product.

  - `excel: AnalyticsConnectorOfficeProductMetrics`

    Office Agent activity metrics for a single connector on a given day within one Office product.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `outlook: AnalyticsConnectorOfficeProductMetrics`

    Office Agent activity metrics for a single connector on a given day within one Office product.

  - `powerpoint: AnalyticsConnectorOfficeProductMetrics`

    Office Agent activity metrics for a single connector on a given day within one Office product.

  - `word: AnalyticsConnectorOfficeProductMetrics`

    Office Agent activity metrics for a single connector on a given day within one Office product.

### Analytics Connector Office Product Metrics

- `AnalyticsConnectorOfficeProductMetrics object`

  Office Agent activity metrics for a single connector on a given day within one Office product.

  - `distinct_session_connector_used_count: number or null`

    Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Core Code Metrics

- `AnalyticsCoreCodeMetrics object`

  Core Claude Code activity metrics for a single user on a given day.

  - `artifacts_created_count: number`

    Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `commit_count: number`

    Number of commits made via Claude Code

  - `distinct_session_count: number or null`

    Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

  - `lines_of_code: AnalyticsLinesOfCode`

    Lines of code added and removed via Claude Code.

    - `added_count: number`

      Lines of code added

    - `removed_count: number`

      Lines of code removed

  - `pull_request_count: number`

    Number of pull requests created via Claude Code

### Analytics Cowork Metrics

- `AnalyticsCoworkMetrics object`

  Cowork activity metrics for a single user on a given day.

  - `action_count: number`

    Number of tool actions completed in Cowork sessions

  - `artifacts_created_count: number`

    Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `connectors_used_count: number`

    Total number of connector invocations in Cowork sessions

  - `dispatch_turn_count: number`

    Number of Dispatch (background agent) turns completed

  - `distinct_connectors_used_count: number or null`

    Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_plugins_used_count: number or null`

    Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number or null`

    Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number or null`

    Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `edit_tool_count: number or null`

    Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `file_edit_count: number or null`

    Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

  - `message_count: number`

    Number of messages sent in Cowork sessions

  - `multi_edit_tool_count: number or null`

    Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `notebook_edit_tool_count: number or null`

    Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `plugins_used_count: number or null`

    Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

  - `sessions_with_file_edits_count: number or null`

    Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `skills_used_count: number`

    Total number of skill invocations in Cowork sessions

  - `write_tool_count: number or null`

    Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

### Analytics Design Metrics

- `AnalyticsDesignMetrics object`

  Claude Design activity metrics for a single user on a given day.

  - `distinct_projects_created_count: number`

    Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

  - `distinct_projects_used_count: number or null`

    Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number or null`

    Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent in Claude Design sessions

### Analytics Lines Of Code

- `AnalyticsLinesOfCode object`

  Lines of code added and removed via Claude Code.

  - `added_count: number`

    Lines of code added

  - `removed_count: number`

    Lines of code removed

### Analytics Office Metrics

- `AnalyticsOfficeMetrics object`

  Office Agent activity metrics for a single user on a given day, broken out by Office product.

  - `excel: AnalyticsOfficeProductMetrics`

    Office Agent activity metrics for a single user on a given day within one Office product.

    - `connectors_used_count: number`

      Number of MCP connector invocations

    - `distinct_connectors_used_count: number or null`

      Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent

    - `skills_used_count: number`

      Number of skill invocations

  - `outlook: AnalyticsOfficeProductMetrics`

    Office Agent activity metrics for a single user on a given day within one Office product.

  - `powerpoint: AnalyticsOfficeProductMetrics`

    Office Agent activity metrics for a single user on a given day within one Office product.

  - `word: AnalyticsOfficeProductMetrics`

    Office Agent activity metrics for a single user on a given day within one Office product.

### Analytics Office Product Metrics

- `AnalyticsOfficeProductMetrics object`

  Office Agent activity metrics for a single user on a given day within one Office product.

  - `connectors_used_count: number`

    Number of MCP connector invocations

  - `distinct_connectors_used_count: number or null`

    Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_session_count: number or null`

    Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_skills_used_count: number or null`

    Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent

  - `skills_used_count: number`

    Number of skill invocations

### Analytics Order

- `AnalyticsOrder = "asc" or "desc"`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

### Analytics Plugin Activity

- `AnalyticsPluginActivity object`

  Per-plugin install + invocation activity for a given day.

  With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork`,
  `claude_code` and `chat_cowork_unified` only on this endpoint) each row is
  one (plugin, user), (plugin, group), or (plugin, product) cut: the flat
  `user_id` / `rbac_group_id` / `product` keys carry the cut and the counts
  are scoped to it.

  - `claude_code_metrics: AnalyticsPluginClaudeCodeMetrics`

    Claude Code activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsPluginCoworkMetrics`

    Cowork activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `install_count: number or null`

    Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `invocation_count: number`

    Number of plugin invocations on the requested day

  - `plugin_id: string or null`

    Stable plugin identifier when available (e.g. `serena@claude-plugins-official`). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

  - `plugin_name: string`

    Name of the plugin

  - `chat_cowork_unified_metrics: optional AnalyticsPluginChatCoworkUnifiedMetrics or null`

    Plugin use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `distinct_session_plugin_used_count: number or null`

      Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

### Analytics Plugin Chat Cowork Unified Metrics

- `AnalyticsPluginChatCoworkUnifiedMetrics object`

  A plugin's use in Cowork sessions recorded while members had Chat
  and Cowork unified turned on.

  - `distinct_session_plugin_used_count: number or null`

    Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Plugin Claude Code Metrics

- `AnalyticsPluginClaudeCodeMetrics object`

  Claude Code activity metrics for a single plugin on a given day.

  - `distinct_session_plugin_used_count: number or null`

    Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Plugin Cowork Metrics

- `AnalyticsPluginCoworkMetrics object`

  Cowork activity metrics for a single plugin on a given day.

  - `distinct_session_plugin_used_count: number or null`

    Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Plugin Group By

- `AnalyticsPluginGroupBy = "product" or "rbac_group_id" or "user_id"`

  A dimension to group plugin activity by.

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

### Analytics Project Activity

- `AnalyticsProjectActivity object`

  Per-project activity data for a given day.

  - `created_at: string or null`

    Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

    format: date-time

  - `created_by: AnalyticsUser or null`

    User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `distinct_conversation_count: number or null`

    Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `message_count: number`

    Number of messages sent in the project on the requested day

  - `project_id: string`

    Tagged project identifier (e.g. `claude_proj_...`)

  - `project_name: string`

    Name of the project

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

### Analytics Project Group By

- `AnalyticsProjectGroupBy = "rbac_group_id" or "user_id"`

  A dimension to group chat project activity by.

  - `"rbac_group_id"`

  - `"user_id"`

### Analytics Science Metrics

- `AnalyticsScienceMetrics object`

  Claude Science activity metrics for a single user on a given day.

  - `delegation_count: number`

    Number of delegations (handoffs to a specialized agent) in Claude Science sessions

  - `distinct_session_count: number or null`

    Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `message_count: number`

    Number of messages sent in Claude Science sessions

  - `remote_compute_job_count: number`

    Number of remote compute jobs launched from Claude Science sessions

  - `skills_used_count: number`

    Total number of skill invocations in Claude Science sessions

### Analytics Single Day Activity Summary

- `AnalyticsSingleDayActivitySummary object`

  Per-day entry in the /summaries response.

  - `assigned_seat_count: number or null`

    Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

  - `cowork_daily_active_user_count: number`

    Number of users with Cowork activity on the requested day

  - `cowork_monthly_active_user_count: number`

    Number of users with Cowork activity in the 30-day rolling window

  - `cowork_weekly_active_user_count: number`

    Number of users with Cowork activity in the 7-day rolling window

  - `daily_active_user_count: number`

    Number of users with token consumption on the requested day

  - `daily_adoption_rate: number or null`

    Percentage of assigned seats with activity on the requested day (`DAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `ending_at: string`

    End of the aggregation period (exclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-16T00:00:00Z`).

    format: date-time

  - `monthly_active_user_count: number`

    Number of users with token consumption in the 30-day rolling window

  - `monthly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 30-day rolling window (`MAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `pending_invite_count: number or null`

    Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

  - `starting_at: string`

    Start of the aggregation period (inclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-15T00:00:00Z`).

    format: date-time

  - `weekly_active_user_count: number`

    Number of users with token consumption in the 7-day rolling window

  - `weekly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 7-day rolling window (`WAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `chat_cowork_unified_daily_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified on the requested day. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_monthly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 28-day rolling window (30 days when the request filters by `rbac_group_id`). Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_weekly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 7-day rolling window. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_daily_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_monthly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_weekly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_daily_active_user_count: optional number or null`

    Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_monthly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_weekly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_daily_active_user_count: optional number or null`

    Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_monthly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_weekly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_tag_daily_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag on the requested day. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_monthly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 28-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_weekly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 7-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `office_agent_daily_active_user_count: optional number or null`

    Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_monthly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_weekly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_daily_active_user_count: optional number or null`

    Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_entitled_user_count: optional number or null`

    Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_monthly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_weekly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

### Analytics Skill Activity

- `AnalyticsSkillActivity object`

  Per-skill activity data for a given day.

  - `attributed_list_price: string or null`

    List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that involved the skill, not the skill's incremental cost. Unlike `estimated_overage_spend` this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does not tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on `chat` product rows and on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as `estimated_overage_spend` (spend reporting not enabled for this organization, `office_agent` product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `chat_metrics: AnalyticsSkillChatMetrics`

    Claude.ai activity metrics for a single skill on a given day.

    - `distinct_conversation_skill_used_count: number or null`

      Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsSkillClaudeCodeMetrics`

    Claude Code activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsSkillCoworkMetrics`

    Cowork activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `currency: string or null`

    Currency for this row's monetary fields (`estimated_overage_spend` and `attributed_list_price`), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

  - `distinct_user_count: number`

    Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

  - `enable_count: number or null`

    Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin `install_count`). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to `user_id` / `rbac_group_id` / `product` via `group_by[]` or `filter[]` (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (`starting_date`/`ending_date`).

  - `estimated_overage_spend: string or null`

    Estimated overage spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see `attributed_list_price` for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that involved the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (`starting_date`/`ending_date`) returns the window's sum. With `group_by[]=user_id` each row carries the user's own attributed spend. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `invocation_count: number or null`

    Total number of times this skill was invoked on the requested day (the skill analog of plugin `invocation_count`). Unlike `distinct_user_count` — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (`starting_date`/`ending_date`) returns this sum directly.

  - `office_metrics: AnalyticsSkillOfficeMetrics`

    Office Agent activity metrics for a single skill on a given day, broken out by Office product.

    - `excel: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

      - `distinct_session_skill_used_count: number or null`

        Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `powerpoint: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `word: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

  - `share_status: "organization" or "private" or "public" or null`

    Skill share status (claude.ai only): one of `private`, `organization`, or `public`. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via `filter[]=share_status:{value}`.

    - `"organization"`

    - `"private"`

    - `"public"`

  - `skill_display_name: string or null`

    Human-readable display name for rows whose `skill_name` is an opaque skill id (user/organization skill types and plugin-delivered skills, whose user-defined names usage reports generally withhold). Organization-shared skills and skills delivered by the organization's own plugins (its plugin marketplaces and its library) resolve; plugin skill names are shown without their 'plugin:' prefix. The literal 'unknown' bucket row gets a fixed 'Unknown skill' label. For a member's own skill (private or personal-plugin) it is null, except when the skill's owner used it from Claude Code or Cowork in the requested period: then it shows the name that client reported at the time. Apart from that, the names of members' own skills are not disclosed to analytics-key holders. Also null for Anthropic-provided plugin skills (not resolved), for an organization skill or plugin whose name can no longer be found (for example, one since deleted), when `skill_name` is already a display name, or when display-name resolution is not enabled for this organization.

  - `skill_name: string`

    Name of the skill

  - `chat_cowork_unified_metrics: optional AnalyticsSkillChatCoworkUnifiedMetrics or null`

    Skill use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsSkillChatCoworkUnifiedChatMetrics`

      A skill's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_skill_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsSkillChatCoworkUnifiedSessionsMetrics`

      A skill's use in Cowork sessions recorded while members had Chat
      and Cowork unified turned on.

      - `distinct_session_skill_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

### Analytics Skill Chat Cowork Unified Chat Metrics

- `AnalyticsSkillChatCoworkUnifiedChatMetrics object`

  A skill's use in chat conversations recorded while members had
  Chat and Cowork unified turned on.

  - `distinct_conversation_skill_used_count: number or null`

    Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Chat Cowork Unified Metrics

- `AnalyticsSkillChatCoworkUnifiedMetrics object`

  A skill's use in Chat and Cowork unified on one day: `chat` holds its use
  in chat conversations and `sessions` its use in Cowork sessions.

  - `chat: AnalyticsSkillChatCoworkUnifiedChatMetrics`

    A skill's use in chat conversations recorded while members had
    Chat and Cowork unified turned on.

    - `distinct_conversation_skill_used_count: number or null`

      Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `sessions: AnalyticsSkillChatCoworkUnifiedSessionsMetrics`

    A skill's use in Cowork sessions recorded while members had Chat
    and Cowork unified turned on.

    - `distinct_session_skill_used_count: number or null`

      Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Chat Cowork Unified Sessions Metrics

- `AnalyticsSkillChatCoworkUnifiedSessionsMetrics object`

  A skill's use in Cowork sessions recorded while members had Chat
  and Cowork unified turned on.

  - `distinct_session_skill_used_count: number or null`

    Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Chat Metrics

- `AnalyticsSkillChatMetrics object`

  Claude.ai activity metrics for a single skill on a given day.

  - `distinct_conversation_skill_used_count: number or null`

    Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Claude Code Metrics

- `AnalyticsSkillClaudeCodeMetrics object`

  Claude Code activity metrics for a single skill on a given day.

  - `distinct_session_skill_used_count: number or null`

    Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Cowork Metrics

- `AnalyticsSkillCoworkMetrics object`

  Cowork activity metrics for a single skill on a given day.

  - `distinct_session_skill_used_count: number or null`

    Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Skill Group By

- `AnalyticsSkillGroupBy = "product" or "rbac_group_id" or "user_id"`

  A dimension to group skill activity by.

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

### Analytics Skill Office Metrics

- `AnalyticsSkillOfficeMetrics object`

  Office Agent activity metrics for a single skill on a given day, broken out by Office product.

  - `excel: AnalyticsSkillOfficeProductMetrics`

    Office Agent activity metrics for a single skill on a given day within one Office product.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `outlook: AnalyticsSkillOfficeProductMetrics`

    Office Agent activity metrics for a single skill on a given day within one Office product.

  - `powerpoint: AnalyticsSkillOfficeProductMetrics`

    Office Agent activity metrics for a single skill on a given day within one Office product.

  - `word: AnalyticsSkillOfficeProductMetrics`

    Office Agent activity metrics for a single skill on a given day within one Office product.

### Analytics Skill Office Product Metrics

- `AnalyticsSkillOfficeProductMetrics object`

  Office Agent activity metrics for a single skill on a given day within one Office product.

  - `distinct_session_skill_used_count: number or null`

    Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

### Analytics Tool Action Counts

- `AnalyticsToolActionCounts object`

  Accepted/rejected counts for a single Claude Code tool type.

  - `accepted_count: number`

    Number of tool proposals accepted

  - `rejected_count: number`

    Number of tool proposals rejected

### Analytics Tool Actions

- `AnalyticsToolActions object`

  Per-tool accepted/rejected counts for Claude Code file modification tools.

  - `edit_tool: AnalyticsToolActionCounts`

    Accepted/rejected counts for a single Claude Code tool type.

    - `accepted_count: number`

      Number of tool proposals accepted

    - `rejected_count: number`

      Number of tool proposals rejected

  - `multi_edit_tool: AnalyticsToolActionCounts`

    Accepted/rejected counts for a single Claude Code tool type.

  - `notebook_edit_tool: AnalyticsToolActionCounts`

    Accepted/rejected counts for a single Claude Code tool type.

  - `write_tool: AnalyticsToolActionCounts`

    Accepted/rejected counts for a single Claude Code tool type.

### Analytics User

- `AnalyticsUser object`

  A user in the organization, identified by tagged id and email address.

  - `type: "user"`

    Object type. Always `user`.

    default: user

  - `id: string`

    Tagged user identifier (e.g. `user_...`)

  - `email_address: string`

    Email address of the user

### Analytics User Activity

- `AnalyticsUserActivity object`

  Per-user activity data for a given day.

  - `chat_metrics: AnalyticsChatMetrics`

    Claude.ai activity metrics for a single user on a given day.

    - `connectors_used_count: number`

      Number of MCP connector invocations.

    - `distinct_artifacts_created_count: number`

      Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_connectors_used_count: number or null`

      Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_conversation_count: number or null`

      Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_files_uploaded_count: number or null`

      Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_projects_created_count: number`

      Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_shared_artifacts_viewed_count: number or null`

      Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent

    - `shared_conversations_viewed_count: number`

      Number of times the user opened a shared conversation in a project

    - `thinking_message_count: number`

      Number of messages that used extended thinking

  - `claude_code_metrics: AnalyticsClaudeCodeMetrics`

    Claude Code activity metrics for a single user on a given day.

    - `core_metrics: AnalyticsCoreCodeMetrics`

      Core Claude Code activity metrics for a single user on a given day.

      - `artifacts_created_count: number`

        Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `commit_count: number`

        Number of commits made via Claude Code

      - `distinct_session_count: number or null`

        Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

      - `lines_of_code: AnalyticsLinesOfCode`

        Lines of code added and removed via Claude Code.

        - `added_count: number`

          Lines of code added

        - `removed_count: number`

          Lines of code removed

      - `pull_request_count: number`

        Number of pull requests created via Claude Code

    - `tool_actions: AnalyticsToolActions`

      Per-tool accepted/rejected counts for Claude Code file modification tools.

      - `edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

        - `accepted_count: number`

          Number of tool proposals accepted

        - `rejected_count: number`

          Number of tool proposals rejected

      - `multi_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `notebook_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `write_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

  - `cowork_metrics: AnalyticsCoworkMetrics`

    Cowork activity metrics for a single user on a given day.

    - `action_count: number`

      Number of tool actions completed in Cowork sessions

    - `artifacts_created_count: number`

      Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `connectors_used_count: number`

      Total number of connector invocations in Cowork sessions

    - `dispatch_turn_count: number`

      Number of Dispatch (background agent) turns completed

    - `distinct_connectors_used_count: number or null`

      Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_plugins_used_count: number or null`

      Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `edit_tool_count: number or null`

      Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `file_edit_count: number or null`

      Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

    - `message_count: number`

      Number of messages sent in Cowork sessions

    - `multi_edit_tool_count: number or null`

      Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `notebook_edit_tool_count: number or null`

      Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `plugins_used_count: number or null`

      Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

    - `sessions_with_file_edits_count: number or null`

      Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `skills_used_count: number`

      Total number of skill invocations in Cowork sessions

    - `write_tool_count: number or null`

      Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `design_metrics: AnalyticsDesignMetrics`

    Claude Design activity metrics for a single user on a given day.

    - `distinct_projects_created_count: number`

      Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Design sessions

  - `distinct_user_count: number or null`

    Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

  - `office_metrics: AnalyticsOfficeMetrics`

    Office Agent activity metrics for a single user on a given day, broken out by Office product.

    - `excel: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

      - `connectors_used_count: number`

        Number of MCP connector invocations

      - `distinct_connectors_used_count: number or null`

        Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `skills_used_count: number`

        Number of skill invocations

    - `outlook: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `powerpoint: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `word: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

  - `science_metrics: AnalyticsScienceMetrics`

    Claude Science activity metrics for a single user on a given day.

    - `delegation_count: number`

      Number of delegations (handoffs to a specialized agent) in Claude Science sessions

    - `distinct_session_count: number or null`

      Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Science sessions

    - `remote_compute_job_count: number`

      Number of remote compute jobs launched from Claude Science sessions

    - `skills_used_count: number`

      Total number of skill invocations in Claude Science sessions

  - `user: AnalyticsUser or null`

    The user this row describes. Null on rows aggregated across users.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `web_search_count: number`

    Number of web searches performed

  - `chat_cowork_unified_metrics: optional AnalyticsChatCoworkUnifiedMetrics or null`

    Activity recorded while the member had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into `chat` (chat activity) and `sessions` (Cowork activity). Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsChatCoworkUnifiedChatMetrics`

      Chat activity recorded while members had Chat and Cowork unified turned
      on.

      - `connectors_used_count: number`

        Same measure as `chat_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_artifacts_created_count: number`

        Same measure as `chat_metrics.distinct_artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number or null`

        Same measure as `chat_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number or null`

        Same measure as `chat_metrics.distinct_files_uploaded_count`, for activity recorded while members had Chat and Cowork unified turned on. It counts uploaded files as well as files Claude created and images returned by Claude's tools, such as screenshots. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Same measure as `chat_metrics.distinct_projects_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number or null`

        Same measure as `chat_metrics.distinct_projects_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number or null`

        Always null: shared-artifact views are not currently measured.

      - `distinct_skills_used_count: number or null`

        Same measure as `chat_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Same measure as `chat_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `shared_conversations_viewed_count: number`

        Same measure as `chat_metrics.shared_conversations_viewed_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `thinking_message_count: number`

        Same measure as `chat_metrics.thinking_message_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `sessions: AnalyticsChatCoworkUnifiedSessionsMetrics`

      Cowork session activity recorded while members had Chat and Cowork
      unified turned on.

      - `action_count: number`

        Same measure as `cowork_metrics.action_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `artifacts_created_count: number`

        Same measure as `cowork_metrics.artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `connectors_used_count: number`

        Same measure as `cowork_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `dispatch_turn_count: number`

        Same measure as `cowork_metrics.dispatch_turn_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_connectors_used_count: number or null`

        Same measure as `cowork_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_plugins_used_count: number or null`

        Same measure as `cowork_metrics.distinct_plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Same measure as `cowork_metrics.distinct_session_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Same measure as `cowork_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: number or null`

        Same measure as `cowork_metrics.edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `file_edit_count: number or null`

        Same measure as `cowork_metrics.file_edit_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `message_count: number`

        Same measure as `cowork_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `multi_edit_tool_count: number or null`

        Same measure as `cowork_metrics.multi_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on. Claude no longer has a multi-edit tool, so expect 0 when not null; each edit is now a separate Edit tool call, counted in `edit_tool_count` and `file_edit_count`.

      - `notebook_edit_tool_count: number or null`

        Same measure as `cowork_metrics.notebook_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `plugins_used_count: number or null`

        Same measure as `cowork_metrics.plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `sessions_with_file_edits_count: number or null`

        Same measure as `cowork_metrics.sessions_with_file_edits_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `skills_used_count: number`

        Same measure as `cowork_metrics.skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `write_tool_count: number or null`

        Same measure as `cowork_metrics.write_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `claude_tag_metrics: optional AnalyticsClaudeTagMetrics or null`

    Claude Tag activity in Slack by a user who has linked a Claude account. Activity by Slack users who have not linked an account appears only in the `/summaries` Claude Tag counts, so these rows do not add up to those counts. Omitted from the response on deployments that do not offer Claude Tag reporting.

    - `active_day_count: number or null`

      1 on a day the user was active in Claude Tag in Slack, otherwise 0. Summed over the window in date-range mode, so it is the number of active days; on grouped rows, the total of each member's active days. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

    - `active_message_count: number or null`

      Number of the user's Slack messages that made them active: @-mentions, direct messages, group direct message asks, and thread posts Claude answered. Other messages are not counted. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

  - `last_activity_date: optional string or null`

    Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

    format: date

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

### Analytics User Group By

- `AnalyticsUserGroupBy = "rbac_group_id"`

  A dimension to group user activity by.

## Analytics › Summaries

### Get Activity Summaries

**GET** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day from `starting_date` (inclusive) to `ending_date`
(exclusive) in `data`, the same `data` / `next_page` envelope as the other
analytics list endpoints; the series is currently returned in full, so
`next_page` is always null.
Data is typically available with a 1-day lag and may be revised by a few
percent over the following days: when `ending_date` is omitted it
defaults to the most recent available day + 1, so the last entry covers
the most recent available day. The series can be scoped to an RBAC group
via `filter[]=rbac_group_id:{id}`. Available to organizations on a Claude
Enterprise plan. Requires an API key with the `read:analytics` scope.

#### Query parameters

- `starting_date: string`

  UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`. Only `rbac_group_id` is supported (e.g. `filter[]=rbac_group_id:{id}`); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. `rbac_group_id` accepts the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

  maxItems: 100

- `limit: optional number`

  Number of results per page (1-1000, default 100). The day series (at most 366 entries) is currently returned in full in a single page, so `limit` does not yet shorten it.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field. `next_page` is currently always null, so there is never a cursor to send.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsSingleDayActivitySummary`

  One entry per day in the requested range, ascending by date.

  - `assigned_seat_count: number or null`

    Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

  - `cowork_daily_active_user_count: number`

    Number of users with Cowork activity on the requested day

  - `cowork_monthly_active_user_count: number`

    Number of users with Cowork activity in the 30-day rolling window

  - `cowork_weekly_active_user_count: number`

    Number of users with Cowork activity in the 7-day rolling window

  - `daily_active_user_count: number`

    Number of users with token consumption on the requested day

  - `daily_adoption_rate: number or null`

    Percentage of assigned seats with activity on the requested day (`DAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `ending_at: string`

    End of the aggregation period (exclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-16T00:00:00Z`).

    format: date-time

  - `monthly_active_user_count: number`

    Number of users with token consumption in the 30-day rolling window

  - `monthly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 30-day rolling window (`MAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `pending_invite_count: number or null`

    Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

  - `starting_at: string`

    Start of the aggregation period (inclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-15T00:00:00Z`).

    format: date-time

  - `weekly_active_user_count: number`

    Number of users with token consumption in the 7-day rolling window

  - `weekly_adoption_rate: number or null`

    Percentage of assigned seats with activity in the 7-day rolling window (`WAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `chat_cowork_unified_daily_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified on the requested day. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_monthly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 28-day rolling window (30 days when the request filters by `rbac_group_id`). Omitted from the response where Chat and Cowork unified is not available.

  - `chat_cowork_unified_weekly_active_user_count: optional number or null`

    Number of users with activity in Chat and Cowork unified in the 7-day rolling window. Omitted from the response where Chat and Cowork unified is not available.

  - `chat_daily_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_monthly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `chat_weekly_active_user_count: optional number or null`

    Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_daily_active_user_count: optional number or null`

    Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_monthly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_code_weekly_active_user_count: optional number or null`

    Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_daily_active_user_count: optional number or null`

    Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_monthly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_design_weekly_active_user_count: optional number or null`

    Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `claude_tag_daily_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag on the requested day. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_monthly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 28-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `claude_tag_weekly_active_user_count: optional number or null`

    Number of Slack users active in Claude Tag in the 7-day rolling window. Counts distinct Slack users, including users who have not linked a Claude account, so it can exceed `daily_active_user_count` and `assigned_seat_count`. Null on a day with no measured value, when Claude Tag data cannot be read for the request, and when the response is scoped to an RBAC group, because an unlinked user belongs to no group. Omitted from the response on deployments that do not offer Claude Tag reporting.

  - `office_agent_daily_active_user_count: optional number or null`

    Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_monthly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `office_agent_weekly_active_user_count: optional number or null`

    Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_daily_active_user_count: optional number or null`

    Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_entitled_user_count: optional number or null`

    Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_monthly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `science_weekly_active_user_count: optional number or null`

    Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results. Currently always null: the day series is returned in full.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/summaries \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_cowork_unified_daily_active_user_count": 0,
      "chat_cowork_unified_monthly_active_user_count": 0,
      "chat_cowork_unified_weekly_active_user_count": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "claude_tag_daily_active_user_count": 0,
      "claude_tag_monthly_active_user_count": 0,
      "claude_tag_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Users

### List User Activity

**GET** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Use `group_by[]` for per-RBAC-group aggregates, or `filter[]` to
scope results to specific members, groups, or a chat project. Available
to organizations on a Claude Enterprise plan. Requires an API key with
the `read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. A `project_id` filter limits each member's row to their claude.ai chat activity in that project and cannot be combined with `group_by[]` or an `rbac_group_id` filter. On these rows, every count in `chat_cowork_unified_metrics.sessions` is 0, because sessions are not measured per project. On any day a member sent a chat message in Chat and Cowork unified, all of that member's project activity for the day is counted in `chat_cowork_unified_metrics.chat` instead of `chat_metrics`.

  maxItems: 100

- `group_by: optional array of AnalyticsUserGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=rbac_group_id`). Supported on this endpoint: `rbac_group_id`. Rows are already per-member, so the one supported grouping aggregates them per RBAC group instead. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsUserActivity`

  - `chat_metrics: AnalyticsChatMetrics`

    Claude.ai activity metrics for a single user on a given day.

    - `connectors_used_count: number`

      Number of MCP connector invocations.

    - `distinct_artifacts_created_count: number`

      Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_connectors_used_count: number or null`

      Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_conversation_count: number or null`

      Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_files_uploaded_count: number or null`

      Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_projects_created_count: number`

      Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_shared_artifacts_viewed_count: number or null`

      Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent

    - `shared_conversations_viewed_count: number`

      Number of times the user opened a shared conversation in a project

    - `thinking_message_count: number`

      Number of messages that used extended thinking

  - `claude_code_metrics: AnalyticsClaudeCodeMetrics`

    Claude Code activity metrics for a single user on a given day.

    - `core_metrics: AnalyticsCoreCodeMetrics`

      Core Claude Code activity metrics for a single user on a given day.

      - `artifacts_created_count: number`

        Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `commit_count: number`

        Number of commits made via Claude Code

      - `distinct_session_count: number or null`

        Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

      - `lines_of_code: AnalyticsLinesOfCode`

        Lines of code added and removed via Claude Code.

        - `added_count: number`

          Lines of code added

        - `removed_count: number`

          Lines of code removed

      - `pull_request_count: number`

        Number of pull requests created via Claude Code

    - `tool_actions: AnalyticsToolActions`

      Per-tool accepted/rejected counts for Claude Code file modification tools.

      - `edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

        - `accepted_count: number`

          Number of tool proposals accepted

        - `rejected_count: number`

          Number of tool proposals rejected

      - `multi_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `notebook_edit_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `write_tool: AnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

  - `cowork_metrics: AnalyticsCoworkMetrics`

    Cowork activity metrics for a single user on a given day.

    - `action_count: number`

      Number of tool actions completed in Cowork sessions

    - `artifacts_created_count: number`

      Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `connectors_used_count: number`

      Total number of connector invocations in Cowork sessions

    - `dispatch_turn_count: number`

      Number of Dispatch (background agent) turns completed

    - `distinct_connectors_used_count: number or null`

      Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_plugins_used_count: number or null`

      Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_skills_used_count: number or null`

      Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `edit_tool_count: number or null`

      Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `file_edit_count: number or null`

      Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

    - `message_count: number`

      Number of messages sent in Cowork sessions

    - `multi_edit_tool_count: number or null`

      Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `notebook_edit_tool_count: number or null`

      Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `plugins_used_count: number or null`

      Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

    - `sessions_with_file_edits_count: number or null`

      Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `skills_used_count: number`

      Total number of skill invocations in Cowork sessions

    - `write_tool_count: number or null`

      Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `design_metrics: AnalyticsDesignMetrics`

    Claude Design activity metrics for a single user on a given day.

    - `distinct_projects_created_count: number`

      Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `distinct_projects_used_count: number or null`

      Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `distinct_session_count: number or null`

      Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Design sessions

  - `distinct_user_count: number or null`

    Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

  - `office_metrics: AnalyticsOfficeMetrics`

    Office Agent activity metrics for a single user on a given day, broken out by Office product.

    - `excel: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

      - `connectors_used_count: number`

        Number of MCP connector invocations

      - `distinct_connectors_used_count: number or null`

        Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Number of messages sent

      - `skills_used_count: number`

        Number of skill invocations

    - `outlook: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `powerpoint: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `word: AnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

  - `science_metrics: AnalyticsScienceMetrics`

    Claude Science activity metrics for a single user on a given day.

    - `delegation_count: number`

      Number of delegations (handoffs to a specialized agent) in Claude Science sessions

    - `distinct_session_count: number or null`

      Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `message_count: number`

      Number of messages sent in Claude Science sessions

    - `remote_compute_job_count: number`

      Number of remote compute jobs launched from Claude Science sessions

    - `skills_used_count: number`

      Total number of skill invocations in Claude Science sessions

  - `user: AnalyticsUser or null`

    The user this row describes. Null on rows aggregated across users.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `web_search_count: number`

    Number of web searches performed

  - `chat_cowork_unified_metrics: optional AnalyticsChatCoworkUnifiedMetrics or null`

    Activity recorded while the member had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into `chat` (chat activity) and `sessions` (Cowork activity). Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsChatCoworkUnifiedChatMetrics`

      Chat activity recorded while members had Chat and Cowork unified turned
      on.

      - `connectors_used_count: number`

        Same measure as `chat_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_artifacts_created_count: number`

        Same measure as `chat_metrics.distinct_artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_connectors_used_count: number or null`

        Same measure as `chat_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_conversation_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_files_uploaded_count: number or null`

        Same measure as `chat_metrics.distinct_files_uploaded_count`, for activity recorded while members had Chat and Cowork unified turned on. It counts uploaded files as well as files Claude created and images returned by Claude's tools, such as screenshots. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_projects_created_count: number`

        Same measure as `chat_metrics.distinct_projects_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `distinct_projects_used_count: number or null`

        Same measure as `chat_metrics.distinct_projects_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_shared_artifacts_viewed_count: number or null`

        Always null: shared-artifact views are not currently measured.

      - `distinct_skills_used_count: number or null`

        Same measure as `chat_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `message_count: number`

        Same measure as `chat_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `shared_conversations_viewed_count: number`

        Same measure as `chat_metrics.shared_conversations_viewed_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `thinking_message_count: number`

        Same measure as `chat_metrics.thinking_message_count`, for activity recorded while members had Chat and Cowork unified turned on.

    - `sessions: AnalyticsChatCoworkUnifiedSessionsMetrics`

      Cowork session activity recorded while members had Chat and Cowork
      unified turned on.

      - `action_count: number`

        Same measure as `cowork_metrics.action_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `artifacts_created_count: number`

        Same measure as `cowork_metrics.artifacts_created_count`, for activity recorded while members had Chat and Cowork unified turned on. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `connectors_used_count: number`

        Same measure as `cowork_metrics.connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `dispatch_turn_count: number`

        Same measure as `cowork_metrics.dispatch_turn_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `distinct_connectors_used_count: number or null`

        Same measure as `cowork_metrics.distinct_connectors_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_plugins_used_count: number or null`

        Same measure as `cowork_metrics.distinct_plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_session_count: number or null`

        Same measure as `cowork_metrics.distinct_session_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `distinct_skills_used_count: number or null`

        Same measure as `cowork_metrics.distinct_skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `edit_tool_count: number or null`

        Same measure as `cowork_metrics.edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `file_edit_count: number or null`

        Same measure as `cowork_metrics.file_edit_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `message_count: number`

        Same measure as `cowork_metrics.message_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `multi_edit_tool_count: number or null`

        Same measure as `cowork_metrics.multi_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on. Claude no longer has a multi-edit tool, so expect 0 when not null; each edit is now a separate Edit tool call, counted in `edit_tool_count` and `file_edit_count`.

      - `notebook_edit_tool_count: number or null`

        Same measure as `cowork_metrics.notebook_edit_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `plugins_used_count: number or null`

        Same measure as `cowork_metrics.plugins_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `sessions_with_file_edits_count: number or null`

        Same measure as `cowork_metrics.sessions_with_file_edits_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `skills_used_count: number`

        Same measure as `cowork_metrics.skills_used_count`, for activity recorded while members had Chat and Cowork unified turned on.

      - `write_tool_count: number or null`

        Same measure as `cowork_metrics.write_tool_count`, for activity recorded while members had Chat and Cowork unified turned on.

  - `claude_tag_metrics: optional AnalyticsClaudeTagMetrics or null`

    Claude Tag activity in Slack by a user who has linked a Claude account. Activity by Slack users who have not linked an account appears only in the `/summaries` Claude Tag counts, so these rows do not add up to those counts. Omitted from the response on deployments that do not offer Claude Tag reporting.

    - `active_day_count: number or null`

      1 on a day the user was active in Claude Tag in Slack, otherwise 0. Summed over the window in date-range mode, so it is the number of active days; on grouped rows, the total of each member's active days. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

    - `active_message_count: number or null`

      Number of the user's Slack messages that made them active: @-mentions, direct messages, group direct message asks, and thread posts Claude answered. Other messages are not counted. Null when Claude Tag data cannot be read for the request. Otherwise, 0 on a row filtered by project, and null on any other row when no covered day was measured.

  - `last_activity_date: optional string or null`

    Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

    format: date

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/users \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_plugins_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "message_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "skills_used_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "user": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "web_search_count": 0,
      "chat_cowork_unified_metrics": {
        "chat": {
          "connectors_used_count": 0,
          "distinct_artifacts_created_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_conversation_count": 0,
          "distinct_files_uploaded_count": 0,
          "distinct_projects_created_count": 0,
          "distinct_projects_used_count": 0,
          "distinct_shared_artifacts_viewed_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "shared_conversations_viewed_count": 0,
          "thinking_message_count": 0
        },
        "sessions": {
          "action_count": 0,
          "artifacts_created_count": 0,
          "connectors_used_count": 0,
          "dispatch_turn_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_plugins_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "edit_tool_count": 0,
          "file_edit_count": 0,
          "message_count": 0,
          "multi_edit_tool_count": 0,
          "notebook_edit_tool_count": 0,
          "plugins_used_count": 0,
          "sessions_with_file_edits_count": 0,
          "skills_used_count": 0,
          "write_tool_count": 0
        }
      },
      "claude_tag_metrics": {
        "active_day_count": 0,
        "active_message_count": 0
      },
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name"
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Apps › Chat › Projects

### Get Chat Project Usage

**GET** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Use `group_by[]` to break projects out per member or per RBAC
group, and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Available to organizations on a Claude Enterprise
plan. Requires an API key with the `read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

  maxItems: 100

- `group_by: optional array of AnalyticsProjectGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsProjectActivity`

  - `created_at: string or null`

    Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

    format: date-time

  - `created_by: AnalyticsUser or null`

    User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.

    - `type: "user"`

      Object type. Always `user`.

      default: user

    - `id: string`

      Tagged user identifier (e.g. `user_...`)

    - `email_address: string`

      Email address of the user

  - `distinct_conversation_count: number or null`

    Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `message_count: number`

    Number of messages sent in the project on the requested day

  - `project_id: string`

    Tagged project identifier (e.g. `claude_proj_...`)

  - `project_name: string`

    Name of the project

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Connectors

### Get Connector Usage

**GET** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Use `group_by[]` to break usage out per member, per RBAC
group, or per product surface, and `filter[]` to scope results; the
parameter descriptions list the supported dimensions. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `connector_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `connector_name` matches case-insensitively, a display name such as 'GitHub MCP' also matches its normalized stored form ('github'), and for rows whose `connector_name` is an opaque connector id the connector's display name (`connector_display_name`) also matches; `product` is one of `chat_cowork_unified`, `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsConnectorGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsConnectorActivity`

  - `chat_metrics: AnalyticsConnectorChatMetrics`

    Claude.ai activity metrics for a single connector on a given day.

    - `distinct_conversation_connector_used_count: number or null`

      Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsConnectorClaudeCodeMetrics`

    Claude Code activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `connector_display_name: string or null`

    Human-readable display name for rows whose `connector_name` is an opaque connector id rather than a readable name, resolved at request time from the organization's connectors (including connectors that have since been removed). `connector_name` remains the row's stable key for sorting and pagination, and `filter[]=connector_name:{value}` also matches these rows by display name. Display names are not unique, and the same connector's claude.ai usage can appear under a separate row with a readable `connector_name`. Null when `connector_name` is already a readable name, when the id cannot be resolved to one of the organization's connectors, or when display-name resolution is not enabled for this organization.

  - `connector_name: string`

    Name of the connector. Some rows carry an opaque connector id here instead of a readable name; `connector_display_name` holds the resolved name for those rows.

  - `cowork_metrics: AnalyticsConnectorCoworkMetrics`

    Cowork activity metrics for a single connector on a given day.

    - `distinct_session_connector_used_count: number or null`

      Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `individual_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on their own individual credential, connected through their own consent flow. Companion bucket to `managed_auth_distinct_user_count`, which carries the measurement, attribution, and null rules. Users whose requests used no stored credential count in neither bucket.

  - `managed_auth_distinct_user_count: number or null`

    Number of distinct users whose use of this connector on the requested day ran on Enterprise Managed Auth (an organization-managed credential provisioned through the organization's identity provider), read from the token record each request used. Null, never 0, when managed-auth reporting is not enabled for the organization, the value cannot be attributed to the row, no credentialed requests and no managed-token mint events (a managed credential being provisioned for a user's use of the connector) were observed that day, or the day predates 2026-07-01, the first day the backing data exists (forward-only data, no backfill). When credentialed requests or mint events were observed and attributed, both managed-auth fields populate, reporting 0 for a bucket with no users; the two counts are independent, not a partition — a user whose requests that day used both kinds of credential counts in both. Mint events carry user but not surface attribution, so they count as observed auth activity on `user_id` and `rbac_group_id` cuts — attributed to the user the credential was provisioned for — but never on a cut that references `product` (group or filter). Date-range rollup mode (`starting_date`/`ending_date`) computes both fields exactly over the window — distinct users with at least one qualifying day — when the whole window starts on or after 2026-07-01, with the null-versus-0 and mint-event rules applying with the window in place of the day; a range starting earlier reports every managed-auth field as null, never a partial-window value.

  - `office_metrics: AnalyticsConnectorOfficeMetrics`

    Office Agent activity metrics for a single connector on a given day, broken out by Office product.

    - `excel: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

      - `distinct_session_connector_used_count: number or null`

        Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `powerpoint: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `word: AnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

  - `read_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of `read_call_count`, `write_call_count`, or `unclassified_call_count`, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in `unclassified_call_count`). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (`starting_date`/`ending_date`) applies both rules server-side.

  - `unclassified_call_count: number or null`

    Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `write_call_count: number or null`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `chat_cowork_unified_metrics: optional AnalyticsConnectorChatCoworkUnifiedMetrics or null`

    Connector use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsConnectorChatCoworkUnifiedChatMetrics`

      A connector's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_connector_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsConnectorChatCoworkUnifiedSessionsMetrics`

      A connector's use in Cowork sessions recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_session_connector_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_connector_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/connectors \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_display_name": "connector_display_name",
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "individual_auth_distinct_user_count": 0,
      "managed_auth_distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "write_call_count": 0,
      "chat_cowork_unified_metrics": {
        "chat": {
          "distinct_conversation_connector_used_count": 0
        },
        "sessions": {
          "distinct_session_connector_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Plugins

### Get Plugin Usage

**GET** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Use `group_by[]` to break usage out per
member, per RBAC group, or per product surface (Cowork / Claude Code),
and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like `/skills`.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `plugin_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `plugin_name` matches case-insensitively; `product` is `chat_cowork_unified`, `claude_code`, or `cowork` (the only surfaces with plugin attribution); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsPluginGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. On this endpoint `product` takes the values `chat_cowork_unified`, `claude_code`, or `cowork` only (the surfaces with plugin attribution). Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsPluginActivity`

  - `claude_code_metrics: AnalyticsPluginClaudeCodeMetrics`

    Claude Code activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsPluginCoworkMetrics`

    Cowork activity metrics for a single plugin on a given day.

    - `distinct_session_plugin_used_count: number or null`

      Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `distinct_user_count: number`

    Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `install_count: number or null`

    Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `invocation_count: number`

    Number of plugin invocations on the requested day

  - `plugin_id: string or null`

    Stable plugin identifier when available (e.g. `serena@claude-plugins-official`). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

  - `plugin_name: string`

    Name of the plugin

  - `chat_cowork_unified_metrics: optional AnalyticsPluginChatCoworkUnifiedMetrics or null`

    Plugin use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `distinct_session_plugin_used_count: number or null`

      Same measure as `cowork_metrics.distinct_session_plugin_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/plugins \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_id": "plugin_id",
      "plugin_name": "plugin_name",
      "chat_cowork_unified_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Skills

### Get Skill Usage

**GET** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Use `group_by[]` to break usage out per member, per RBAC group, or per
product surface, and `filter[]` to scope results; the parameter
descriptions list the supported dimensions. Available to organizations
on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: optional string`

  UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `ending_date: optional string`

  UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `product`, `rbac_group_id`, `share_status`, `skill_name`, `user_id`. Value forms: `product` is one of `chat_cowork_unified`, `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `share_status` is one of `organization`, `private`, or `public`; `skill_name` matches case-insensitively; `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsSkillGroupBy`

  Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Number of results per page (1-1000, default 100).

  minimum: 1, maximum: 1000

- `order: optional AnalyticsOrder`

  Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

  - `"asc"`

  - `"desc"`

- `order_by: optional string`

  Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `starting_date: optional string`

  UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsSkillActivity`

  - `attributed_list_price: string or null`

    List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that involved the skill, not the skill's incremental cost. Unlike `estimated_overage_spend` this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does not tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on `chat` product rows and on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as `estimated_overage_spend` (spend reporting not enabled for this organization, `office_agent` product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `chat_metrics: AnalyticsSkillChatMetrics`

    Claude.ai activity metrics for a single skill on a given day.

    - `distinct_conversation_skill_used_count: number or null`

      Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `claude_code_metrics: AnalyticsSkillClaudeCodeMetrics`

    Claude Code activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `cowork_metrics: AnalyticsSkillCoworkMetrics`

    Cowork activity metrics for a single skill on a given day.

    - `distinct_session_skill_used_count: number or null`

      Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `currency: string or null`

    Currency for this row's monetary fields (`estimated_overage_spend` and `attributed_list_price`), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

  - `distinct_user_count: number`

    Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

  - `enable_count: number or null`

    Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin `install_count`). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to `user_id` / `rbac_group_id` / `product` via `group_by[]` or `filter[]` (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (`starting_date`/`ending_date`).

  - `estimated_overage_spend: string or null`

    Estimated overage spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see `attributed_list_price` for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that involved the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (`starting_date`/`ending_date`) returns the window's sum. With `group_by[]=user_id` each row carries the user's own attributed spend. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `invocation_count: number or null`

    Total number of times this skill was invoked on the requested day (the skill analog of plugin `invocation_count`). Unlike `distinct_user_count` — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (`starting_date`/`ending_date`) returns this sum directly.

  - `office_metrics: AnalyticsSkillOfficeMetrics`

    Office Agent activity metrics for a single skill on a given day, broken out by Office product.

    - `excel: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

      - `distinct_session_skill_used_count: number or null`

        Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `outlook: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `powerpoint: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `word: AnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

  - `share_status: "organization" or "private" or "public" or null`

    Skill share status (claude.ai only): one of `private`, `organization`, or `public`. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via `filter[]=share_status:{value}`.

    - `"organization"`

    - `"private"`

    - `"public"`

  - `skill_display_name: string or null`

    Human-readable display name for rows whose `skill_name` is an opaque skill id (user/organization skill types and plugin-delivered skills, whose user-defined names usage reports generally withhold). Organization-shared skills and skills delivered by the organization's own plugins (its plugin marketplaces and its library) resolve; plugin skill names are shown without their 'plugin:' prefix. The literal 'unknown' bucket row gets a fixed 'Unknown skill' label. For a member's own skill (private or personal-plugin) it is null, except when the skill's owner used it from Claude Code or Cowork in the requested period: then it shows the name that client reported at the time. Apart from that, the names of members' own skills are not disclosed to analytics-key holders. Also null for Anthropic-provided plugin skills (not resolved), for an organization skill or plugin whose name can no longer be found (for example, one since deleted), when `skill_name` is already a display name, or when display-name resolution is not enabled for this organization.

  - `skill_name: string`

    Name of the skill

  - `chat_cowork_unified_metrics: optional AnalyticsSkillChatCoworkUnifiedMetrics or null`

    Skill use recorded while members had Chat and Cowork unified (Cowork's features inside claude.ai chat) turned on, split into chat conversations and Cowork sessions. A count is null in date-range mode where it cannot be computed. Omitted from the response where Chat and Cowork unified is not available.

    - `chat: AnalyticsSkillChatCoworkUnifiedChatMetrics`

      A skill's use in chat conversations recorded while members had
      Chat and Cowork unified turned on.

      - `distinct_conversation_skill_used_count: number or null`

        Same measure as `chat_metrics.distinct_conversation_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `sessions: AnalyticsSkillChatCoworkUnifiedSessionsMetrics`

      A skill's use in Cowork sessions recorded while members had Chat
      and Cowork unified turned on.

      - `distinct_session_skill_used_count: number or null`

        Same measure as `cowork_metrics.distinct_session_skill_used_count`, for activity recorded while members had Chat and Cowork unified turned on. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/skills \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "attributed_list_price": "attributed_list_price",
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "currency": "currency",
      "distinct_user_count": 0,
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "share_status": "organization",
      "skill_display_name": "skill_display_name",
      "skill_name": "skill_name",
      "chat_cowork_unified_metrics": {
        "chat": {
          "distinct_conversation_skill_used_count": 0
        },
        "sessions": {
          "distinct_session_skill_used_count": 0
        }
      },
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Analytics › Artifacts

### Get Artifact Activity

**GET** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (`artifact_type`, `is_shared`) cube for the organization;
`next_page` is null except for grouped queries, which paginate. The cube
can be broken out per product, per member, or per RBAC group via
`group_by[]`, and scoped via `filter[]`. Requires an API key with the
`read:analytics` scope.

#### Query parameters

- `date: string`

  UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

  format: date

- `filter: optional array of string`

  Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `artifact_type`, `is_shared`, `product`, `rbac_group_id`, `user_id`. Value forms: `artifact_type` is a canonical artifact MIME type (e.g. `text/markdown`) or `other`; `is_shared` is `true` or `false`; `product` is `chat_cowork_unified`, `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries. `chat_cowork_unified` is accepted as a `product` value only where Chat and Cowork unified is available.

  maxItems: 100

- `group_by: optional array of AnalyticsArtifactGroupBy`

  Dimensions to break results out by: `product`, `user_id` and/or `rbac_group_id`. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via `next_page`. `product` takes the values `chat_cowork_unified`, `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts). `rbac_group_id` attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

  maxItems: 100

  - `"product"`

  - `"rbac_group_id"`

  - `"user_id"`

- `limit: optional number`

  Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; `limit` is the page size only when `group_by[]` multiplies the cube.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field. Only valid with `group_by[]` — the ungrouped cube is never paginated.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of AnalyticsArtifactActivity`

  - `artifact_type: string`

    Canonical artifact MIME type (e.g. `text/markdown`, `application/vnd.ant.react`, `image/svg+xml`), or `other`. Claude Code and Cowork artifacts report as `text/html`.

  - `artifacts_created_count: number`

    Number of artifacts created in this bucket on the requested day

  - `distinct_user_count: number`

    Number of distinct users who created artifacts in this bucket on the requested day

  - `is_shared: boolean`

    Whether the artifacts in this bucket have ever been shared (a Claude Code / Cowork artifact is shared once anyone beyond its creator may open it: named members, the whole organization, or anyone with the link).

  - `published_artifacts_created_count: number`

    Number of those artifacts that have been published (for Claude Code / Cowork artifacts: open to anyone with the link); never exceeds `artifacts_created_count`

  - `product: optional string or null`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, `office_agent`, or `chat_cowork_unified` (Chat and Cowork unified). These are the canonical Cost & Usage product names; an `office_agent` row's per-surface breakdown is in its `office_metrics`. On `/plugins` only `cowork`, `claude_code` and `chat_cowork_unified` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, `cowork` and `chat_cowork_unified` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `rbac_group_id: optional string or null`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `rbac_group_name: optional string or null`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `user_id: optional string or null`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

- `next_page: string or null`

  Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```
