# Create a Text Completion

`client.Completions.New(ctx, params) (*Completion, error)`

**POST** `/v1/complete`

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://platform.claude.com/docs/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) for guidance in migrating from Text Completions to Messages.

## Parameters

- `params CompletionNewParams`

  - `MaxTokensToSample param.Field[int64]`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    minimum: 1

  - `Model param.Field[Model]`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Prompt param.Field[string]`

    Body param: The prompt that you want Claude to complete.

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

  - `Metadata param.Field[Metadata] Optional`

    Body param: An object describing metadata about the request.

  - `StopSequences param.Field[[]string] Optional`

    Body param: Sequences that will cause the model to stop generating.

    Our models stop on `"

    Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

  - `Temperature param.Field[float64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `TopK param.Field[int64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `TopP param.Field[float64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

## Returns

- `type Completion struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Completion string`

    The resulting completion up to and excluding the stop sequences.

  - `Model Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `type Model string`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `const ModelClaudeFable5_1 Model = "claude-fable-5-1"`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `const ModelClaudeMythos5_1 Model = "claude-mythos-5-1"`

        Our most capable model for cybersecurity and biology research, available through trusted access programs

      - `const ModelClaudeSonnet5 Model = "claude-sonnet-5"`

        High-performance model for coding and agents

      - `const ModelClaudeFable5 Model = "claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `const ModelClaudeMythos5 Model = "claude-mythos-5"`

        Most capable model for cybersecurity and biology research

      - `const ModelClaudeOpus5 Model = "claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeOpus4_8 Model = "claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeOpus4_7 Model = "claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeMythosPreview Model = "claude-mythos-preview"`

        New class of intelligence, strongest in coding and cybersecurity

      - `const ModelClaudeOpus4_6 Model = "claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `const ModelClaudeOpus4_5 Model = "claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `string`

  - `StopReason string`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `Type Completion`

    Object type.

    For Text Completions, this is always `"completion"`.

    default: completion

- `type Completion struct{…}`

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	completion, err := client.Completions.New(context.TODO(), anthropic.CompletionNewParams{
		MaxTokensToSample: 256,
		Model:             anthropic.ModelClaudeFable5_1,
		Prompt:            "\n\nHuman: Hello, world!\n\nAssistant:",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", completion.ID)
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
