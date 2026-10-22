---
title: Vaults
url: https://platform.claude.com/docs/en/api/java/beta/vaults
---

# Vaults

## Create a Vault

`BetaManagedAgentsVault beta().vaults().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults`

Create a Vault

### Parameters

- `VaultCreateParams params`

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `String displayName`

    Human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultCreateParams params = VaultCreateParams.builder()
            .displayName("Example vault")
            .build();
        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().create(params);
    }
}
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`VaultListPage beta().vaults().list(params = VaultListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults`

List Vaults

### Parameters

- `VaultListParams params`

  - `Optional<Boolean> includeArchived` (query parameter)

    Whether to include archived vaults in the results. Defaults to `false`.

  - `Optional<Long> limit` (query parameter)

    Maximum number of vaults to return per page. Defaults to 20, maximum 100.

    format: int32

  - `Optional<String> page` (query parameter)

    The `next_page` value from a previous [List Vaults](https://platform.claude.com/docs/en/api/beta/vaults/list?sdk_languages=java) response, to get the next page. Leave it out to get the first page.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.VaultListPage;
import com.anthropic.models.beta.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultListPage page = client.beta().vaults().list();
    }
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Retrieve a Vault

`BetaManagedAgentsVault beta().vaults().retrieve(params = VaultRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}`

Retrieve a Vault

### Parameters

- `VaultRetrieveParams params`

  - `Optional<String> vaultId` (path parameter)

    Unique identifier of the vault to retrieve.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update a Vault

`BetaManagedAgentsVault beta().vaults().update(params = VaultUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}`

Update a Vault

### Parameters

- `VaultUpdateParams params`

  - `Optional<String> vaultId` (path parameter)

    Unique identifier of the vault to update.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `Optional<String> displayName`

    Updated human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().update("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete a Vault

`BetaManagedAgentsDeletedVault beta().vaults().delete(params = VaultDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/vaults/{vault_id}`

Delete a Vault

### Parameters

- `VaultDeleteParams params`

  - `Optional<String> vaultId` (path parameter)

    Unique identifier of the vault to delete.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `JsonValue type = "vault_deleted"`

  - `String id`

    The unique ID of the deleted vault (`vlt_...`).

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsDeletedVault;
import com.anthropic.models.beta.vaults.VaultDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedVault betaManagedAgentsDeletedVault = client.beta().vaults().delete("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive a Vault

`BetaManagedAgentsVault beta().vaults().archive(params = VaultArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/archive`

Archive a Vault

### Parameters

- `VaultArchiveParams params`

  - `Optional<String> vaultId` (path parameter)

    Unique identifier of the vault to archive.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().archive("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `JsonValue type = "vault_deleted"`

  - `String id`

    The unique ID of the deleted vault (`vlt_...`).

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `JsonValue type = "vault"`

  - `String id`

    The unique ID of the vault (`vlt_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the vault was archived. Null if not archived.

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

## Vaults › Credentials

### Create a Credential

`BetaManagedAgentsCredential beta().vaults().credentials().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials`

Create a Credential

#### Parameters

- `CredentialCreateParams params`

  - `Optional<String> vaultId` (path parameter)

    Identifier of the vault to create the credential in.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `Auth auth`

    Authentication configuration for the credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams`

      Parameters for creating an MCP OAuth credential.

      - `JsonValue type = "mcp_oauth"`

      - `String accessToken`

        The OAuth access token to send to the MCP server.

        minLength: 1, maxLength: 8192

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `Optional<LocalDateTime> expiresAt`

        When `access_token` expires, in RFC 3339.

        Must be in the future.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

          minLength: 1, maxLength: 1024

        - `String refreshToken`

          The OAuth refresh token that the API uses to get a new access token when the current one expires.

          minLength: 1, maxLength: 8192

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

            - `String clientSecret`

              The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostParam`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

            - `String clientSecret`

              The OAuth client secret, sent to `token_endpoint` in the POST body.

              minLength: 1, maxLength: 512

        - `Optional<String> resource`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `Optional<String> scope`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsStaticBearerCreateParams`

      Parameters for creating a static bearer token credential.

      - `JsonValue type = "static_bearer"`

      - `String token`

        The static bearer token to send to the MCP server, such as an API key or personal access token.

        minLength: 1, maxLength: 8192

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

    - `class BetaManagedAgentsEnvironmentVariableCreateParams`

      Parameters for creating an environment variable credential.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsCredentialNetworkingParams networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `String secretName`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `String secretValue`

        The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

        minLength: 1, maxLength: 4096

      - `Optional<BetaManagedAgentsInjectionLocationParams> injectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

  - `Optional<String> displayName`

    Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonValue type = "vault_credential"`

  - `String id`

    The unique ID of the credential (`vcrd_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `Auth auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonValue type = "mcp_oauth"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID used when refreshing the access token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonValue type = "static_bearer"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `String secretName`

        Name of the environment variable.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsStaticBearerCreateParams;
import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
                .token("bearer_exampletoken")
                .mcpServerUrl("https://example-server.modelcontextprotocol.io/sse")
                .build())
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().create(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### List Credentials

`CredentialListPage beta().vaults().credentials().list(params = CredentialListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `CredentialListParams params`

  - `Optional<String> vaultId` (path parameter)

    Identifier of the vault to list credentials for.

  - `Optional<Boolean> includeArchived` (query parameter)

    Whether to include archived credentials in the results. Defaults to `false`.

  - `Optional<Long> limit` (query parameter)

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `Optional<String> page` (query parameter)

    The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=java) response, to get the next page. Leave it out to get the first page.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonValue type = "vault_credential"`

  - `String id`

    The unique ID of the credential (`vcrd_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `Auth auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonValue type = "mcp_oauth"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID used when refreshing the access token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonValue type = "static_bearer"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `String secretName`

        Name of the environment variable.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.CredentialListPage;
import com.anthropic.models.beta.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().vaults().credentials().list("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Credential

`BetaManagedAgentsCredential beta().vaults().credentials().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Retrieve a Credential

#### Parameters

- `CredentialRetrieveParams params`

  - `String vaultId` (path parameter)

    Identifier of the vault containing the credential.

  - `Optional<String> credentialId` (path parameter)

    Unique identifier of the credential to retrieve.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonValue type = "vault_credential"`

  - `String id`

    The unique ID of the credential (`vcrd_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `Auth auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonValue type = "mcp_oauth"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID used when refreshing the access token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonValue type = "static_bearer"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `String secretName`

        Name of the environment variable.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialRetrieveParams params = CredentialRetrieveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYPQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().retrieve(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Update a Credential

`BetaManagedAgentsCredential beta().vaults().credentials().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update a Credential

#### Parameters

- `CredentialUpdateParams params`

  - `String vaultId` (path parameter)

    Identifier of the vault containing the credential.

  - `Optional<String> credentialId` (path parameter)

    Unique identifier of the credential to update.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `Optional<Auth> auth`

    New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed.

    - `class BetaManagedAgentsMcpOAuthUpdateParams`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `JsonValue type = "mcp_oauth"`

      - `Optional<String> accessToken`

        The new OAuth access token to replace the stored one.

        minLength: 1, maxLength: 8192

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

        If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

        Must be in the future.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

        Updated refresh token configuration.

        - `Optional<String> refreshToken`

          The new OAuth refresh token to replace the stored one.

          minLength: 1, maxLength: 8192

        - `Optional<String> scope`

          The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

          maxLength: 8192

        - `Optional<TokenEndpointAuth> tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `JsonValue type = "client_secret_basic"`

            - `Optional<String> clientSecret`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

            Updated POST body authentication parameters for the token endpoint.

            - `JsonValue type = "client_secret_post"`

            - `Optional<String> clientSecret`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

    - `class BetaManagedAgentsStaticBearerUpdateParams`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `JsonValue type = "static_bearer"`

      - `Optional<String> token`

        The new static bearer token to replace the stored one.

        minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `JsonValue type = "environment_variable"`

      - `Optional<BetaManagedAgentsInjectionLocationUpdateParams> injectionLocation`

        Updated injection location.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

      - `Optional<BetaManagedAgentsCredentialNetworkingParams> networking`

        The new networking scope, which replaces the stored one as a whole.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `Optional<String> secretValue`

        The new secret value to replace the stored one.

        minLength: 1, maxLength: 4096

  - `Optional<String> displayName`

    Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonValue type = "vault_credential"`

  - `String id`

    The unique ID of the credential (`vcrd_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `Auth auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonValue type = "mcp_oauth"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID used when refreshing the access token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonValue type = "static_bearer"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `String secretName`

        Name of the environment variable.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialUpdateParams params = CredentialUpdateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYPQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().update(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Delete a Credential

`BetaManagedAgentsDeletedCredential beta().vaults().credentials().delete(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

#### Parameters

- `CredentialDeleteParams params`

  - `String vaultId` (path parameter)

    Identifier of the vault containing the credential.

  - `Optional<String> credentialId` (path parameter)

    Unique identifier of the credential to delete.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `JsonValue type = "vault_credential_deleted"`

  - `String id`

    The unique ID of the deleted credential (`vcrd_...`).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsDeletedCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYPQfSkw")
            .build();
        BetaManagedAgentsDeletedCredential betaManagedAgentsDeletedCredential = client.beta().vaults().credentials().delete(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive a Credential

`BetaManagedAgentsCredential beta().vaults().credentials().archive(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive a Credential

#### Parameters

- `CredentialArchiveParams params`

  - `String vaultId` (path parameter)

    Identifier of the vault containing the credential.

  - `Optional<String> credentialId` (path parameter)

    Unique identifier of the credential to archive.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonValue type = "vault_credential"`

  - `String id`

    The unique ID of the credential (`vcrd_...`).

  - `Optional<LocalDateTime> archivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `Auth auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonValue type = "mcp_oauth"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Optional<LocalDateTime> expiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `String clientId`

          The OAuth client ID used when refreshing the access token.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonValue type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonValue type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonValue type = "client_secret_post"`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonValue type = "static_bearer"`

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonValue type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonValue type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonValue type = "limited"`

          - `List<String> allowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `String secretName`

        Name of the environment variable.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialArchiveParams params = CredentialArchiveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYPQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().archive(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Validate an MCP OAuth Credential

`BetaManagedAgentsCredentialValidation beta().vaults().credentials().mcpOAuthValidate(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

#### Parameters

- `CredentialMcpOAuthValidateParams params`

  - `String vaultId` (path parameter)

    Identifier of the vault containing the credential.

  - `Optional<String> credentialId` (path parameter)

    Unique identifier of the credential to validate.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `JsonValue type = "vault_credential_validation"`

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

        format: int32

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `Status status`

      Outcome of the refresh attempt.

      - `SUCCEEDED("succeeded")`

        The token endpoint returned a new access token.

      - `FAILED("failed")`

        The token endpoint returned an error response. See `http_response` for detail.

      - `CONNECT_ERROR("connect_error")`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `NO_REFRESH_TOKEN("no_refresh_token")`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of the validation probe.

    - `VALID("valid")`

      The credential successfully authenticated against its MCP server.

    - `INVALID("invalid")`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `UNKNOWN("unknown")`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `LocalDateTime validatedAt`

    When the validation probe was performed.

    format: date-time

  - `String vaultId`

    Identifier of the vault containing the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYPQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
}
```

##### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```
