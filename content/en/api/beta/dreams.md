# Dreams

## Create a Dream

**POST** `/v1/dreams`

Create a Dream

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

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

    - `"ce-user-management-2026-07-13"`

### Body parameters

- `inputs: array of BetaDreamInput`

  - `BetaDreamMemoryStoreInput object`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: string`

      minLength: 1

    - `type: "memory_store"`

  - `BetaDreamSessionsInput object`

    Input session transcripts the dream reads.

    - `session_ids: array of string`

    - `type: "sessions"`

- `model: string or BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `string`

  - `BetaDreamModelConfigParam object`

    Model identifier and configuration applied to every pipeline stage.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast" or null`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `instructions: optional string or null`

  minLength: 1, maxLength: 4096

- `output_behavior: optional BetaOutputBehavior`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `BetaOutputBehaviorCreateNew object`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: "create_new"`

  - `BetaOutputBehaviorUpdateExisting object`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: string`

      minLength: 1

    - `type: "update_existing"`

### Returns

- `BetaDream object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

### Example

```bash
curl https://api.anthropic.com/v1/dreams \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "inputs": [
            {
              "memory_store_id": "x",
              "type": "memory_store"
            }
          ],
          "model": "string"
        }'
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## List Dreams

**GET** `/v1/dreams`

List Dreams

### Query parameters

- `"created_at[gt]": optional string`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  format: date-time

- `"created_at[lt]": optional string`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  format: date-time

- `include_archived: optional boolean`

  Query parameter for include_archived

- `limit: optional number`

  Query parameter for limit

  format: int32

- `page: optional string`

  Query parameter for page

- `statuses: optional array of BetaDreamStatus`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

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

    - `"ce-user-management-2026-07-13"`

### Returns

- `data: array of BetaDream`

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

- `next_page: string or null`

### Example

```bash
curl https://api.anthropic.com/v1/dreams \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

## Get a Dream

**GET** `/v1/dreams/{dream_id}`

Get a Dream

### Path parameters

- `dream_id: string`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

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

    - `"ce-user-management-2026-07-13"`

### Returns

- `BetaDream object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

### Example

```bash
curl https://api.anthropic.com/v1/dreams/$DREAM_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Cancel a Dream

**POST** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Path parameters

- `dream_id: string`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

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

    - `"ce-user-management-2026-07-13"`

### Returns

- `BetaDream object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

### Example

```bash
curl https://api.anthropic.com/v1/dreams/$DREAM_ID/cancel \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive a Dream

**POST** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Path parameters

- `dream_id: string`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

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

    - `"ce-user-management-2026-07-13"`

### Returns

- `BetaDream object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

### Example

```bash
curl https://api.anthropic.com/v1/dreams/$DREAM_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain types

### Beta Dream

- `BetaDream object`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError or null`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `BetaDreamMemoryStoreInput object`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "memory_store"`

    - `BetaDreamSessionsInput object`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

  - `instructions: string or null`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `BetaOutputBehaviorCreateNew object`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: "create_new"`

    - `BetaOutputBehaviorUpdateExisting object`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: string`

        minLength: 1

      - `type: "update_existing"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

  - `session_id: string or null`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

      format: int32

### Beta Dream Error

- `BetaDreamError object`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: string`

  - `type: string`

### Beta Dream Input

- `BetaDreamInput = BetaDreamMemoryStoreInput or BetaDreamSessionsInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `BetaDreamMemoryStoreInput object`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: string`

      minLength: 1

    - `type: "memory_store"`

  - `BetaDreamSessionsInput object`

    Input session transcripts the dream reads.

    - `session_ids: array of string`

    - `type: "sessions"`

### Beta Dream Memory Store Input

- `BetaDreamMemoryStoreInput object`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `memory_store_id: string`

    minLength: 1

  - `type: "memory_store"`

### Beta Dream Memory Store Output

- `BetaDreamMemoryStoreOutput object`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

### Beta Dream Model Config

- `BetaDreamModelConfig object`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

    minLength: 1, maxLength: 256

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `BetaDreamModelConfigParam object`

  Model identifier and configuration applied to every pipeline stage.

  - `id: string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

    minLength: 1, maxLength: 256

  - `speed: optional "standard" or "fast" or null`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `BetaDreamOutput object`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

### Beta Dream Sessions Input

- `BetaDreamSessionsInput object`

  Input session transcripts the dream reads.

  - `session_ids: array of string`

  - `type: "sessions"`

### Beta Dream Status

- `BetaDreamStatus = "pending" or "running" or "completed" or 2 more`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `BetaDreamUsage object`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: number`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    format: int32

  - `cache_read_input_tokens: number`

    Total tokens read from prompt cache.

    format: int32

  - `input_tokens: number`

    Total uncached input tokens consumed across every pipeline stage.

    format: int32

  - `output_tokens: number`

    Total output tokens generated across every pipeline stage.

    format: int32

### Beta Output Behavior

- `BetaOutputBehavior = BetaOutputBehaviorCreateNew or BetaOutputBehaviorUpdateExisting`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `BetaOutputBehaviorCreateNew object`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: "create_new"`

  - `BetaOutputBehaviorUpdateExisting object`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: string`

      minLength: 1

    - `type: "update_existing"`

### Beta Output Behavior Create New

- `BetaOutputBehaviorCreateNew object`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type: "create_new"`

### Beta Output Behavior Update Existing

- `BetaOutputBehaviorUpdateExisting object`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `memory_store_id: string`

    minLength: 1

  - `type: "update_existing"`
