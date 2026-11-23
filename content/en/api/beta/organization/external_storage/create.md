---
title: Create External Storage
url: https://platform.claude.com/docs/en/api/beta/organization/external_storage/create
---

# Create External Storage

**POST** `/v1/organizations/external_storage`

Register a bucket in the organization's own cloud account. It is saved
as `pending_configuration` and verified when activated.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": array of AnthropicBeta`

  This endpoint is in beta: requests must send `efs-2026-10-01` in this header.

  - `string`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"output-128k-2025-02-19"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"admin-user-sign-out-2026-10-08"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

  - `"ce-claude-code-managed-settings-2026-10-06"`

  - `"efs-2026-10-01"`

  - `"user-profiles-billing-2026-10-01"`

  - `"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

## Body parameters

- `provider_config: BetaAWSExternalStorageConfigParam or BetaGCPExternalStorageConfigParam`

  - `BetaAWSExternalStorageConfigParam object`

    An Amazon S3 bucket.

    - `type: "aws"`

    - `account_id: string`

      12-digit ID of the AWS account that owns the bucket.

    - `bucket_name: string`

      The bucket's name, without `s3://`: 3 to 63 lower-case letters, digits and hyphens, starting and ending with a letter or digit.

    - `region: string`

      The bucket's AWS region. Activating the storage fails if Anthropic can't use buckets in that region.

  - `BetaGCPExternalStorageConfigParam object`

    A Google Cloud Storage bucket.

    - `type: "gcp"`

    - `bucket_name: string`

      The bucket's name, without `gs://`: 3 to 63 lower-case letters, digits and hyphens, starting and ending with a letter or digit. It can't start with `goog` or contain `google`.

    - `project_number: string`

      Project number, not project ID, of the Google Cloud project that holds the bucket.

    - `region: string`

      The bucket's Google Cloud region, such as `us-east5`: one of the single regions that the setup guide lists. Dual-regions and multi-regions aren't supported.

- `display_name: optional string or null`

  Human-friendly display name.

  minLength: 1, maxLength: 255

- `user_profile_id: optional string or null`

  The user profile to bind the storage to. It can't be changed later. The storage can be attached only to Workspaces with this profile, and the bucket's setup must name the same ID.

## Returns

- `BetaExternalStorage object`

  A storage bucket in the organization's own cloud account. Anthropic writes
  inference data to it from each Workspace it is attached to.

  - `type: "external_storage"`

    default: external_storage

  - `id: string`

    The External Storage ID, which starts with `estrg_`. Through Claude Platform on AWS, storage whose `provider_config.type` is `aws` has its bucket ARN as its ID instead: `arn:<partition>:s3:::<bucket_name>`, where `<partition>` is the partition of the bucket's region.

  - `created_at: string`

    format: date-time

  - `display_name: string or null`

    Human-friendly display name. Null if none was set.

  - `provider_config: BetaAWSExternalStorageConfig or BetaGCPExternalStorageConfig`

    - `BetaAWSExternalStorageConfig object`

      An Amazon S3 bucket.

      - `type: "aws"`

        default: aws

      - `account_id: string`

        12-digit ID of the AWS account that owns the bucket.

      - `bucket_name: string`

        The bucket's name, without `s3://`.

      - `region: string`

        The bucket's AWS region.

    - `BetaGCPExternalStorageConfig object`

      A Google Cloud Storage bucket.

      - `type: "gcp"`

        default: gcp

      - `bucket_name: string`

        The bucket's name, without `gs://`.

      - `project_number: string`

        Number of the Google Cloud project that holds the bucket.

      - `region: string`

        The bucket's Google Cloud region.

  - `setup_template_version: string or null`

    The version of Anthropic's setup template whose IAM role names this storage was found to use at activation. Null if no version was recorded, as for storage not yet activated or not on S3.

  - `status: BetaPendingConfigurationExternalStorageStatus or BetaAvailableExternalStorageStatus or BetaActiveExternalStorageStatus or BetaDrainingExternalStorageStatus`

    - `BetaPendingConfigurationExternalStorageStatus object`

      The storage isn't verified yet.

      - `type: "pending_configuration"`

        default: pending_configuration

    - `BetaAvailableExternalStorageStatus object`

      The storage is verified, no Workspace has it attached, and Anthropic doesn't use
      the bucket.

      - `type: "available"`

        default: available

      - `healthy: boolean`

        Whether the bucket passed its latest recorded check. It can stay `true` after the bucket stops working, so don't use it for monitoring.

      - `last_checked_at: string`

        When the bucket's latest recorded check ran, in RFC 3339.

        format: date-time

    - `BetaActiveExternalStorageStatus object`

      At least one Workspace has the storage attached.

      - `type: "active"`

        default: active

      - `healthy: boolean`

        Whether the bucket passed its latest recorded check. It can stay `true` after the bucket stops working, so don't use it for monitoring.

      - `last_checked_at: string`

        When the bucket's latest recorded check ran, in RFC 3339.

        format: date-time

    - `BetaDrainingExternalStorageStatus object`

      No Workspace has the storage attached. A Workspace can attach it again, unless
      `removal_started` is true.

      - `type: "draining"`

        default: draining

      - `healthy: boolean`

        Whether the bucket passed its latest recorded check. It can stay `true` after the bucket stops working, so don't use it for monitoring.

      - `last_checked_at: string`

        When the bucket's latest recorded check ran, in RFC 3339.

        format: date-time

      - `removal_started: boolean`

        True once a delete has started removing this storage, which can't be undone. It then can't be attached, and another delete finishes the removal.

        default: false

  - `updated_at: string`

    format: date-time

  - `user_profile_id: string or null`

    The user profile the storage is bound to, or null.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=http).

Each code below is the value of `error.details.error_code` in the response body.

- `grant_required` (HTTP status 400)

  Anthropic has not approved External Storage for the organization, for the Workspace or, for storage bound to a user profile, for that user profile. Contact your Anthropic account team.

- `organization_not_eligible` (HTTP status 400)

  The feature isn't offered to this organization. The error's `message` names the kind of organization or, when it names none, says to contact your Anthropic account team.

- `provider_not_allowed` (HTTP status 400)

  The request can't use External Storage on this cloud provider. The error's message says why.

- `unsupported_region` (HTTP status 400)

  `provider_config.region` is not a region where External Storage is available.

- `user_profile_not_found` (HTTP status 400)

  The request depends on a user profile that does not exist in the organization or is no longer active. The request either names this user profile by ID, or names a resource, such as an External Key, that is bound to it.

- `sandbox_egress_restricted` (HTTP status 403)

  The request came from a Claude sandbox with restricted network access, which is not allowed to make this request. Send it from outside the sandbox, or from a sandbox with unrestricted network access.

- `storage_already_registered` (HTTP status 409)

  The organization already has External Storage for this bucket that it has not deleted. List the organization's External Storage to find it.

- `authorization_check_unavailable` (HTTP status 503)

  One of the organization's approvals from Anthropic could not be read right now, so nothing was done. Retry after the `Retry-After` delay.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/external_storage \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: efs-2026-10-01' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "provider_config": {
            "account_id": "111122223333",
            "bucket_name": "acme-safety-retention",
            "region": "us-east-2",
            "type": "aws"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
        }'
```

### Response (200)

```json
{
  "id": "estrg_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "provider_config": {
    "account_id": "111122223333",
    "bucket_name": "acme-safety-retention",
    "region": "us-east-2",
    "type": "aws"
  },
  "setup_template_version": "2",
  "status": {
    "type": "pending_configuration"
  },
  "type": "external_storage",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```
