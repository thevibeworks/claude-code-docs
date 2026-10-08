---
title: Models
url: https://platform.claude.com/docs/en/api/java/beta/models
---

# Models

## List Models

`ModelListPage beta().models().list(params = ModelListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `ModelListParams params`

  - `Optional<String> afterId` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<List<Lifecycle>> lifecycle` (query parameter)

    Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

    maxItems: 3

    - `ACTIVE("active")`

    - `DEPRECATED("deprecated")`

    - `RETIRED("retired")`

  - `Optional<Long> limit` (query parameter)

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    Optional header to specify the beta version(s) you want to use.

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

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaModelInfo`

  - `JsonValue type = "model"`

    Object type.

    For Models, this is always `"model"`.

  - `String id`

    Unique model identifier.

  - `Optional<List<String>> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `Optional<BetaModelCapabilities> capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

    - `BetaCapabilitySupport codeExecution`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `Optional<BetaCompactionCapability> compaction`

      Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

      - `BetaCapabilitySupport summarize`

        Whether the summarize compaction type is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Whether the clear_thinking_20251015 strategy is supported.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Whether the compact_20260112 strategy is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Whether the model supports xhigh effort level.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

    - `BetaServerToolsCapability serverTools`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `BetaCapabilitySupport codeExecution`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaCapabilitySupport webSearch`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `BetaCapabilitySupport disabled`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `BetaCapabilitySupport enabled`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `Optional<LocalDateTime> deprecatedAt`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `String displayName`

    A human-readable name for the model.

  - `Lifecycle lifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    - `ACTIVE("active")`

    - `DEPRECATED("deprecated")`

    - `RETIRED("retired")`

  - `Optional<BetaModelLine> line`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `HAIKU("haiku")`

    - `SONNET("sonnet")`

    - `OPUS("opus")`

    - `FABLE("fable")`

    - `MYTHOS("mythos")`

  - `Optional<Long> maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `Optional<Long> maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `Optional<LocalDateTime> retiresAt`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.models.ModelListPage;
import com.anthropic.models.beta.models.ModelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ModelListPage page = client.beta().models().list();
    }
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "claude-opus-5",
      "allowed_fallback_models": [
        "string"
      ],
      "capabilities": {
        "batch": {
          "supported": true
        },
        "citations": {
          "supported": true
        },
        "code_execution": {
          "supported": true
        },
        "compaction": {
          "summarize": {
            "supported": true
          },
          "supported": true
        },
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          },
          "clear_tool_uses_20250919": {
            "supported": true
          },
          "compact_20260112": {
            "supported": true
          },
          "supported": true
        },
        "effort": {
          "high": {
            "supported": true
          },
          "low": {
            "supported": true
          },
          "max": {
            "supported": true
          },
          "medium": {
            "supported": true
          },
          "supported": true,
          "xhigh": {
            "supported": true
          }
        },
        "image_input": {
          "supported": true
        },
        "pdf_input": {
          "supported": true
        },
        "server_tools": {
          "code_execution": {
            "supported": true
          },
          "supported": true,
          "web_search": {
            "supported": true
          }
        },
        "structured_outputs": {
          "supported": true
        },
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            },
            "disabled": {
              "supported": true
            },
            "enabled": {
              "supported": true
            }
          }
        }
      },
      "created_at": "2026-07-24T00:00:00Z",
      "deprecated_at": "2019-12-27T18:11:19.117Z",
      "display_name": "Claude Opus 5",
      "lifecycle": "active",
      "line": "haiku",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "retires_at": "2019-12-27T18:11:19.117Z",
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get a Model

`BetaModelInfo beta().models().retrieve(params = ModelRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `ModelRetrieveParams params`

  - `Optional<String> modelId` (path parameter)

    Model identifier or alias.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    Optional header to specify the beta version(s) you want to use.

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

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaModelInfo`

  - `JsonValue type = "model"`

    Object type.

    For Models, this is always `"model"`.

  - `String id`

    Unique model identifier.

  - `Optional<List<String>> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `Optional<BetaModelCapabilities> capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

    - `BetaCapabilitySupport codeExecution`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `Optional<BetaCompactionCapability> compaction`

      Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

      - `BetaCapabilitySupport summarize`

        Whether the summarize compaction type is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Whether the clear_thinking_20251015 strategy is supported.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Whether the compact_20260112 strategy is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Whether the model supports xhigh effort level.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

    - `BetaServerToolsCapability serverTools`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `BetaCapabilitySupport codeExecution`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaCapabilitySupport webSearch`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `BetaCapabilitySupport disabled`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `BetaCapabilitySupport enabled`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `Optional<LocalDateTime> deprecatedAt`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `String displayName`

    A human-readable name for the model.

  - `Lifecycle lifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    - `ACTIVE("active")`

    - `DEPRECATED("deprecated")`

    - `RETIRED("retired")`

  - `Optional<BetaModelLine> line`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `HAIKU("haiku")`

    - `SONNET("sonnet")`

    - `OPUS("opus")`

    - `FABLE("fable")`

    - `MYTHOS("mythos")`

  - `Optional<Long> maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `Optional<Long> maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `Optional<LocalDateTime> retiresAt`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.models.BetaModelInfo;
import com.anthropic.models.beta.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaModelInfo betaModelInfo = client.beta().models().retrieve("model_id");
    }
}
```

#### Response (200)

```json
{
  "id": "claude-opus-5",
  "allowed_fallback_models": [
    "string"
  ],
  "capabilities": {
    "batch": {
      "supported": true
    },
    "citations": {
      "supported": true
    },
    "code_execution": {
      "supported": true
    },
    "compaction": {
      "summarize": {
        "supported": true
      },
      "supported": true
    },
    "context_management": {
      "clear_thinking_20251015": {
        "supported": true
      },
      "clear_tool_uses_20250919": {
        "supported": true
      },
      "compact_20260112": {
        "supported": true
      },
      "supported": true
    },
    "effort": {
      "high": {
        "supported": true
      },
      "low": {
        "supported": true
      },
      "max": {
        "supported": true
      },
      "medium": {
        "supported": true
      },
      "supported": true,
      "xhigh": {
        "supported": true
      }
    },
    "image_input": {
      "supported": true
    },
    "pdf_input": {
      "supported": true
    },
    "server_tools": {
      "code_execution": {
        "supported": true
      },
      "supported": true,
      "web_search": {
        "supported": true
      }
    },
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "disabled": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-07-24T00:00:00Z",
  "deprecated_at": "2019-12-27T18:11:19.117Z",
  "display_name": "Claude Opus 5",
  "lifecycle": "active",
  "line": "haiku",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "retires_at": "2019-12-27T18:11:19.117Z",
  "type": "model"
}
```

## Domain types

### Beta Capability Support

- `class BetaCapabilitySupport`

  Indicates whether a capability is supported.

  - `boolean supported`

    Whether this capability is supported by the model.

### Beta Compaction Capability

- `class BetaCompactionCapability`

  Compaction capability details: whether the model accepts the top-level
  `compaction` request parameter, with one entry per supported
  `compaction.type` value.

  - `BetaCapabilitySupport summarize`

    Whether the summarize compaction type is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `boolean supported`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `class BetaContextManagementCapability`

  Context management capability details.

  - `Optional<BetaCapabilitySupport> clearThinking20251015`

    Whether the clear_thinking_20251015 strategy is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `Optional<BetaCapabilitySupport> clearToolUses20250919`

    Whether the clear_tool_uses_20250919 strategy is supported.

  - `Optional<BetaCapabilitySupport> compact20260112`

    Whether the compact_20260112 strategy is supported.

  - `boolean supported`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `class BetaEffortCapability`

  Effort (reasoning_effort) capability details.

  - `BetaCapabilitySupport high`

    Whether the model supports high effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport low`

    Whether the model supports low effort level.

  - `BetaCapabilitySupport max`

    Whether the model supports max effort level.

  - `BetaCapabilitySupport medium`

    Whether the model supports medium effort level.

  - `boolean supported`

    Whether this capability is supported by the model.

  - `Optional<BetaCapabilitySupport> xhigh`

    Whether the model supports xhigh effort level.

### Beta Model Capabilities

- `class BetaModelCapabilities`

  Model capability information.

  - `BetaCapabilitySupport batch`

    Whether the model supports the Batch API.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport citations`

    Whether the model supports citation generation.

  - `BetaCapabilitySupport codeExecution`

    Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

  - `Optional<BetaCompactionCapability> compaction`

    Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

    - `BetaCapabilitySupport summarize`

      Whether the summarize compaction type is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaContextManagementCapability contextManagement`

    Context management support and available strategies.

    - `Optional<BetaCapabilitySupport> clearThinking20251015`

      Whether the clear_thinking_20251015 strategy is supported.

    - `Optional<BetaCapabilitySupport> clearToolUses20250919`

      Whether the clear_tool_uses_20250919 strategy is supported.

    - `Optional<BetaCapabilitySupport> compact20260112`

      Whether the compact_20260112 strategy is supported.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaEffortCapability effort`

    Effort (reasoning_effort) support and available levels.

    - `BetaCapabilitySupport high`

      Whether the model supports high effort level.

    - `BetaCapabilitySupport low`

      Whether the model supports low effort level.

    - `BetaCapabilitySupport max`

      Whether the model supports max effort level.

    - `BetaCapabilitySupport medium`

      Whether the model supports medium effort level.

    - `boolean supported`

      Whether this capability is supported by the model.

    - `Optional<BetaCapabilitySupport> xhigh`

      Whether the model supports xhigh effort level.

  - `BetaCapabilitySupport imageInput`

    Whether the model accepts image content blocks.

  - `BetaCapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

  - `BetaServerToolsCapability serverTools`

    Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

    - `BetaCapabilitySupport codeExecution`

      Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `boolean supported`

      Whether this capability is supported by the model.

    - `BetaCapabilitySupport webSearch`

      Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

  - `BetaCapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `BetaThinkingCapability thinking`

    Thinking capability and supported type configurations.

    - `boolean supported`

      Whether this capability is supported by the model.

    - `BetaThinkingTypes types`

      Supported thinking type configurations.

      - `BetaCapabilitySupport adaptive`

        Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `BetaCapabilitySupport disabled`

        Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

      - `BetaCapabilitySupport enabled`

        Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Beta Model Info

- `class BetaModelInfo`

  - `JsonValue type = "model"`

    Object type.

    For Models, this is always `"model"`.

  - `String id`

    Unique model identifier.

  - `Optional<List<String>> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `Optional<BetaModelCapabilities> capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `BetaCapabilitySupport batch`

      Whether the model supports the Batch API.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport citations`

      Whether the model supports citation generation.

    - `BetaCapabilitySupport codeExecution`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `Optional<BetaCompactionCapability> compaction`

      Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

      - `BetaCapabilitySupport summarize`

        Whether the summarize compaction type is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaContextManagementCapability contextManagement`

      Context management support and available strategies.

      - `Optional<BetaCapabilitySupport> clearThinking20251015`

        Whether the clear_thinking_20251015 strategy is supported.

      - `Optional<BetaCapabilitySupport> clearToolUses20250919`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Optional<BetaCapabilitySupport> compact20260112`

        Whether the compact_20260112 strategy is supported.

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaEffortCapability effort`

      Effort (reasoning_effort) support and available levels.

      - `BetaCapabilitySupport high`

        Whether the model supports high effort level.

      - `BetaCapabilitySupport low`

        Whether the model supports low effort level.

      - `BetaCapabilitySupport max`

        Whether the model supports max effort level.

      - `BetaCapabilitySupport medium`

        Whether the model supports medium effort level.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `Optional<BetaCapabilitySupport> xhigh`

        Whether the model supports xhigh effort level.

    - `BetaCapabilitySupport imageInput`

      Whether the model accepts image content blocks.

    - `BetaCapabilitySupport pdfInput`

      Whether the model accepts PDF content blocks.

    - `BetaServerToolsCapability serverTools`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `BetaCapabilitySupport codeExecution`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaCapabilitySupport webSearch`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `BetaCapabilitySupport structuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `BetaThinkingCapability thinking`

      Thinking capability and supported type configurations.

      - `boolean supported`

        Whether this capability is supported by the model.

      - `BetaThinkingTypes types`

        Supported thinking type configurations.

        - `BetaCapabilitySupport adaptive`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `BetaCapabilitySupport disabled`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `BetaCapabilitySupport enabled`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `Optional<LocalDateTime> deprecatedAt`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `String displayName`

    A human-readable name for the model.

  - `Lifecycle lifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    - `ACTIVE("active")`

    - `DEPRECATED("deprecated")`

    - `RETIRED("retired")`

  - `Optional<BetaModelLine> line`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `HAIKU("haiku")`

    - `SONNET("sonnet")`

    - `OPUS("opus")`

    - `FABLE("fable")`

    - `MYTHOS("mythos")`

  - `Optional<Long> maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `Optional<Long> maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `Optional<LocalDateTime> retiresAt`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Beta Model Line

- `enum BetaModelLine`

  A Claude model line, such as `opus` or `sonnet`. More lines may be added as new values.

  - `HAIKU("haiku")`

  - `SONNET("sonnet")`

  - `OPUS("opus")`

  - `FABLE("fable")`

  - `MYTHOS("mythos")`

### Beta Server Tools Capability

- `class BetaServerToolsCapability`

  Web search and code execution tool support, with one entry per tool.

  - `BetaCapabilitySupport codeExecution`

    Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `boolean supported`

      Whether this capability is supported by the model.

  - `boolean supported`

    Whether this capability is supported by the model.

  - `BetaCapabilitySupport webSearch`

    Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

### Beta Thinking Capability

- `class BetaThinkingCapability`

  Thinking capability details.

  - `boolean supported`

    Whether this capability is supported by the model.

  - `BetaThinkingTypes types`

    Supported thinking type configurations.

    - `BetaCapabilitySupport adaptive`

      Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `boolean supported`

        Whether this capability is supported by the model.

    - `BetaCapabilitySupport disabled`

      Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

    - `BetaCapabilitySupport enabled`

      Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Beta Thinking Types

- `class BetaThinkingTypes`

  Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.

  - `BetaCapabilitySupport adaptive`

    Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

    - `boolean supported`

      Whether this capability is supported by the model.

  - `BetaCapabilitySupport disabled`

    Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

  - `BetaCapabilitySupport enabled`

    Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).
