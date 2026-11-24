---
title: Get Workspace
url: https://platform.claude.com/docs/en/api/beta/organization/workspaces/retrieve
---

# Get Workspace

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

## Path parameters

- `workspace_id: string`

  ID of the Workspace.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional. Send `efs-2026-10-01` in this header to use this endpoint's beta features: additional parameters, accepted values and response fields.

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

## Returns

- `BetaWorkspace object`

  - `type: "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: string`

    ID of the Workspace.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: string`

    Identifier for this Workspace's encryption compartment. When you configure an
    AWS KMS customer-managed encryption key (CMEK) that isn't bound to a user
    profile, reference this value in your KMS key-policy condition so the key is
    scoped to this compartment. On GCP and Azure, Anthropic enforces the compartment
    binding automatically; you do not need to reference this value in your key
    configuration. See the CMEK integration guide for the required key
    configuration; unless your organization is on Claude Platform on AWS, it
    includes a separate value used during key validation. On Claude Platform on AWS
    there is no separate validation value: your organization's own key is validated
    against this Workspace's own value when it is attached, so if its key policy
    uses the compartment condition, add this value to it before attaching the key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: array of BetaAllowedInferenceGeo or "unrestricted"`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = array of BetaAllowedInferenceGeo`

        - `"global"`

        - `"us"`

      - `"unrestricted"`

    - `default_inference_geo: "global" or "us"`

      Default inference geo applied when requests omit the parameter.

      - `"global"`

      - `"us"`

    - `workspace_geo: "us"`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: string or null`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your
    organization's own key must be a single-Region key in the same Region as the
    Workspace. If that key is outside the Workspace's AWS account, it can be attached
    only by updating an active Workspace. On that platform the key is validated
    against this Workspace when it is attached, so a key-policy problem is reported
    as an error on this request. This field is write-once: once a key is attached to
    a Workspace it cannot be detached or replaced. To rotate key material, rotate
    the underlying key on your cloud KMS; the `external_key_id` stays the same.

  - `name: string`

    Name of the Workspace.

  - `tags: map[string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `user_profile_id: string or null`

    ID of the user profile attached to the Workspace, or null if it has none. Every inference request through a Workspace that has a user profile must name that profile.

  - `inference_data_privacy: optional BetaInferenceDataPrivacy`

    Where the Workspace's retained inference data and transcript copies go, and whether Anthropic's human review applies. Returned only to requests that send the `efs-2026-10-01` `anthropic-beta` value, and each member only to organizations enabled for it.

    - `human_review: optional BetaAnthropicHumanReview`

      The Workspace's human review setting. Human review is off only while this is `disabled` and Anthropic's approval stands.

      - `type: "disabled" or "enabled"`

        - `"disabled"`

        - `"enabled"`

    - `safeguards_storage: optional BetaStorageMember`

      Where the data Anthropic's safeguards systems retain for the Workspace goes. `external` sends it to the External Storage that `external_storage_id` names. `internal` means no External Storage: it goes to Anthropic's storage or, on a cloud provider's platform, to that provider's storage. A recent change may not have taken effect yet.

      - `BetaInternalStorage object`

        No External Storage for this purpose.

        - `type: "internal"`

          default: internal

      - `BetaExternalStorageMember object`

        The organization's External Storage that `external_storage_id` names.

        - `type: "external"`

          default: external

        - `external_storage_id: string`

          The External Storage ID, which starts with `estrg_`. Through Claude Platform on AWS, storage whose `provider_config.type` is `aws` has its bucket ARN as its ID instead: `arn:<partition>:s3:::<bucket_name>`, where `<partition>` is the partition of the bucket's region.

    - `transcripts_storage: optional BetaStorageMember`

      Where copies of the Workspace's transcripts and its cases (Anthropic's safety findings about those transcripts) go. `external` sends them to the External Storage that `external_storage_id` names. `internal` means no External Storage, so no copies are made. A recent change may not have taken effect yet.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK",
  "inference_data_privacy": {
    "human_review": {
      "type": "disabled"
    },
    "safeguards_storage": {
      "type": "internal"
    },
    "transcripts_storage": {
      "type": "internal"
    }
  }
}
```
