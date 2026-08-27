# Create a Text Completion

`Completion completions().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/complete`

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://platform.claude.com/docs/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) for guidance in migrating from Text Completions to Messages.

## Parameters

- `CompletionCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

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

  - `long maxTokensToSample`

    The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    minimum: 1

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `String prompt`

    The prompt that you want Claude to complete.

    For proper response generation you will need to format your prompt using alternating `

    Human:`and`

    Assistant:` conversational turns. For example:

    ```
    "
    
    Human: {userQuestion}
    
    Assistant:"
    ```

    See [prompt validation](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) and our guide to [prompt design](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) for more details.

    minLength: 1

  - `Optional<Metadata> metadata`

    An object describing metadata about the request.

  - `Optional<List<String>> stopSequences`

    Sequences that will cause the model to stop generating.

    Our models stop on `"

    Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

  - `Optional<Double> temperature`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `Optional<Long> topK`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `Optional<Double> topP`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

## Returns

- `class Completion:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `String completion`

    The resulting completion up to and excluding the stop sequences.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `CLAUDE_SONNET_5("claude-sonnet-5")`

      High-performance model for coding and agents

    - `CLAUDE_FABLE_5("claude-fable-5")`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `CLAUDE_MYTHOS_5("claude-mythos-5")`

      Most capable model for cybersecurity and biology research

    - `CLAUDE_OPUS_5("claude-opus-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

      New class of intelligence, strongest in coding and cybersecurity

    - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

      Best combination of speed and intelligence

    - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

      High-performance model for agents and coding

    - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

      High-performance model for agents and coding

  - `Optional<String> stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `JsonValue type constant`

    Object type.

    For Text Completions, this is always `"completion"`.

- `class Completion:`

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.completions.Completion;
import com.anthropic.models.completions.CompletionCreateParams;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CompletionCreateParams params = CompletionCreateParams.builder()
            .maxTokensToSample(256L)
            .model(Model.CLAUDE_SONNET_5)
            .prompt("\n\nHuman: Hello, world!\n\nAssistant:")
            .build();
        Completion completion = client.completions().create(params);
    }
}
```

### Response (200)

```json
{
  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"
}
```
