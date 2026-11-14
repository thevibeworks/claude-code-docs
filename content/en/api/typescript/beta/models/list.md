---
title: List Models
url: https://platform.claude.com/docs/en/api/typescript/beta/models/list
---

# List Models

- Signature: `client.beta.models.list(params?: ModelListParams, options?: RequestOptions): Page<BetaModelInfo>`
- Endpoint: `GET /v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaModelInfo of client.beta.models.list()) {
  console.log(betaModelInfo.id);
}
```

## Example response (200)

```json
{
  "data": [
    {
      "id": "claude-opus-5-5",
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
            "between_tools": {
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
      "created_at": "2026-09-21T00:00:00Z",
      "deprecated_at": "2019-12-27T18:11:19.117Z",
      "display_name": "Claude Opus 5.5",
      "lifecycle": "active",
      "line": "opus",
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

## Parameters

```ts
interface ModelListParams {
  /** ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object. */
  after_id?: string; // query parameter
  /** ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object. */
  before_id?: string; // query parameter
  /** Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly. */
  lifecycle?: Array<"active" | "deprecated" | "retired">; // query parameter, maxItems: 3
  /** Number of items to return per page. Defaults to `20`. Ranges from `1` to `1000`. */
  limit?: number; // query parameter, minimum: 1, maximum: 1000
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface BetaModelInfo {
  /** Object type. For Models, this is always `"model"`. */
  type: "model";
  /** Unique model identifier. */
  id: string;
  /** Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary. */
  allowed_fallback_models: Array<string> | null; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Object mapping capability names to their support details. Keys are always present for all known capabilities. */
  capabilities: BetaModelCapabilities | null;
  /** RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown. */
  created_at: string; // format: date-time
  /** RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`. */
  deprecated_at: string | null; // format: date-time
  /** A human-readable name for the model. */
  display_name: string;
  /**
   * The model's current lifecycle stage.
   *
   * - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
   * - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
   * - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.
   */
  lifecycle: "active" | "deprecated" | "retired"; // default: active
  /** The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`. */
  line: BetaModelLine | null;
  /** Maximum input context window size in tokens for this model. */
  max_input_tokens: number | null;
  /** Maximum value for the `max_tokens` parameter when using this model. */
  max_tokens: number | null;
  /** RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal. */
  retires_at: string | null; // format: date-time
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

interface BetaModelCapabilities {
  /** Whether the model supports the Batch API. */
  batch: BetaCapabilitySupport;
  /** Whether the model supports citation generation. */
  citations: BetaCapabilitySupport;
  /** Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`. */
  code_execution: BetaCapabilitySupport;
  /** Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values. */
  compaction: BetaCompactionCapability | null; // beta header: compact-2026-09-04
  /** Context management support and available strategies. */
  context_management: BetaContextManagementCapability;
  /** Effort (reasoning_effort) support and available levels. */
  effort: BetaEffortCapability;
  /** Whether the model accepts image content blocks. */
  image_input: BetaCapabilitySupport;
  /** Whether the model accepts PDF content blocks. */
  pdf_input: BetaCapabilitySupport;
  /** Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off. */
  server_tools: BetaServerToolsCapability;
  /** Whether the model supports structured output / JSON mode / strict tool schemas. */
  structured_outputs: BetaCapabilitySupport;
  /** Thinking capability and supported type configurations. */
  thinking: BetaThinkingCapability;
}

type BetaModelLine = "haiku" | "sonnet" | "opus" | "fable" | "mythos";

interface BetaCapabilitySupport {
  /** Whether this capability is supported by the model. */
  supported: boolean;
}

interface BetaCompactionCapability {
  /** Whether the summarize compaction type is supported. */
  summarize: BetaCapabilitySupport;
  /** Whether this capability is supported by the model. */
  supported: boolean;
}

interface BetaContextManagementCapability {
  /** Whether the clear_thinking_20251015 strategy is supported. */
  clear_thinking_20251015: BetaCapabilitySupport | null;
  /** Whether the clear_tool_uses_20250919 strategy is supported. */
  clear_tool_uses_20250919: BetaCapabilitySupport | null;
  /** Whether the compact_20260112 strategy is supported. */
  compact_20260112: BetaCapabilitySupport | null;
  /** Whether this capability is supported by the model. */
  supported: boolean;
}

interface BetaEffortCapability {
  /** Whether the model supports high effort level. */
  high: BetaCapabilitySupport;
  /** Whether the model supports low effort level. */
  low: BetaCapabilitySupport;
  /** Whether the model supports max effort level. */
  max: BetaCapabilitySupport;
  /** Whether the model supports medium effort level. */
  medium: BetaCapabilitySupport;
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Whether the model supports xhigh effort level. */
  xhigh: BetaCapabilitySupport | null;
}

interface BetaServerToolsCapability {
  /** Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version. */
  code_execution: BetaCapabilitySupport;
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version. */
  web_search: BetaCapabilitySupport;
}

interface BetaThinkingCapability {
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Supported thinking type configurations. */
  types: BetaThinkingTypes;
}

interface BetaThinkingTypes {
  /** Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think). */
  adaptive: BetaCapabilitySupport;
  /** Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off. */
  between_tools: BetaCapabilitySupport;
  /** Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off. */
  disabled: BetaCapabilitySupport;
  /** Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`). */
  enabled: BetaCapabilitySupport;
}
```
