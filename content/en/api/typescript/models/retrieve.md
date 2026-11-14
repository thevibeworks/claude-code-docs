---
title: Get a Model
url: https://platform.claude.com/docs/en/api/typescript/models/retrieve
---

# Get a Model

- Signature: `client.models.retrieve(modelID: string, params?: ModelRetrieveParams, options?: RequestOptions): ModelInfo`
- Endpoint: `GET /v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const modelInfo = await client.models.retrieve("model_id");

console.log(modelInfo.id);
```

## Example response (200)

```json
{
  "id": "claude-opus-5-5",
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
```

## Parameters

```ts
/** Model identifier or alias. */
modelID: string; // path parameter

interface ModelRetrieveParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface ModelInfo {
  /** Object type. For Models, this is always `"model"`. */
  type: "model";
  /** Unique model identifier. */
  id: string;
  /** Object mapping capability names to their support details. Keys are always present for all known capabilities. */
  capabilities: ModelCapabilities | null;
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
  line: ModelLine | null;
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
interface ModelCapabilities {
  /** Whether the model supports the Batch API. */
  batch: CapabilitySupport;
  /** Whether the model supports citation generation. */
  citations: CapabilitySupport;
  /** Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`. */
  code_execution: CapabilitySupport;
  /** Context management support and available strategies. */
  context_management: ContextManagementCapability;
  /** Effort (reasoning_effort) support and available levels. */
  effort: EffortCapability;
  /** Whether the model accepts image content blocks. */
  image_input: CapabilitySupport;
  /** Whether the model accepts PDF content blocks. */
  pdf_input: CapabilitySupport;
  /** Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off. */
  server_tools: ServerToolsCapability;
  /** Whether the model supports structured output / JSON mode / strict tool schemas. */
  structured_outputs: CapabilitySupport;
  /** Thinking capability and supported type configurations. */
  thinking: ThinkingCapability;
}

type ModelLine = "haiku" | "sonnet" | "opus" | "fable" | "mythos";

interface CapabilitySupport {
  /** Whether this capability is supported by the model. */
  supported: boolean;
}

interface ContextManagementCapability {
  /** Whether the clear_thinking_20251015 strategy is supported. */
  clear_thinking_20251015: CapabilitySupport | null;
  /** Whether the clear_tool_uses_20250919 strategy is supported. */
  clear_tool_uses_20250919: CapabilitySupport | null;
  /** Whether the compact_20260112 strategy is supported. */
  compact_20260112: CapabilitySupport | null;
  /** Whether this capability is supported by the model. */
  supported: boolean;
}

interface EffortCapability {
  /** Whether the model supports high effort level. */
  high: CapabilitySupport;
  /** Whether the model supports low effort level. */
  low: CapabilitySupport;
  /** Whether the model supports max effort level. */
  max: CapabilitySupport;
  /** Whether the model supports medium effort level. */
  medium: CapabilitySupport;
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Whether the model supports xhigh effort level. */
  xhigh: CapabilitySupport | null;
}

interface ServerToolsCapability {
  /** Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version. */
  code_execution: CapabilitySupport;
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version. */
  web_search: CapabilitySupport;
}

interface ThinkingCapability {
  /** Whether this capability is supported by the model. */
  supported: boolean;
  /** Supported thinking type configurations. */
  types: ThinkingTypes;
}

interface ThinkingTypes {
  /** Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think). */
  adaptive: CapabilitySupport;
  /** Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off. */
  between_tools: CapabilitySupport;
  /** Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off. */
  disabled: CapabilitySupport;
  /** Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`). */
  enabled: CapabilitySupport;
}
```
