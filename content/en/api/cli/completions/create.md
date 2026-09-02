# Create a Text Completion

`$ ant completions create`

**POST** `/v1/complete`

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](https://platform.claude.com/docs/en/api/messages) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) for guidance in migrating from Text Completions to Messages.

## Parameters

- `--max-tokens-to-sample: number`

  Body param: The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  minimum: 1

- `--model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

  Body param: The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `--prompt: string`

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

- `--metadata: optional object`

  Body param: An object describing metadata about the request.

- `--stop-sequence: optional array of string`

  Body param: Sequences that will cause the model to stop generating.

  Our models stop on `"

  Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--temperature: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Body param: Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  maximum: 1, minimum: 0

- `--top-k: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

  Body param: Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

  minimum: 0

- `--top-p: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Body param: Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

  maximum: 1, minimum: 0

## Returns

- `completion: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5-1"`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `"claude-mythos-5-1"`

      Our most capable model for cybersecurity and biology research, available through trusted access programs

    - `"claude-sonnet-5"`

      High-performance model for coding and agents

    - `"claude-fable-5"`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `"claude-mythos-5"`

      Most capable model for cybersecurity and biology research

    - `"claude-opus-5"`

      Powerful intelligence for long-running agents and coding

    - `"claude-opus-4-8"`

      Powerful intelligence for long-running agents and coding

    - `"claude-opus-4-7"`

      Powerful intelligence for long-running agents and coding

    - `"claude-mythos-preview"`

      New class of intelligence, strongest in coding and cybersecurity

    - `"claude-opus-4-6"`

      Powerful intelligence for long-running agents and coding

    - `"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `"claude-opus-4-5"`

      Powerful intelligence for long-running agents and coding

    - `"claude-opus-4-5-20251101"`

      Powerful intelligence for long-running agents and coding

    - `"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

  - `stop_reason: string`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

- `completion: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `completion: string`

    The resulting completion up to and excluding the stop sequences.

  - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `stop_reason: string`

    The reason that we stopped.

    This may be one the following values:

    * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
    * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

  - `type: "completion"`

    Object type.

    For Text Completions, this is always `"completion"`.

## Example

```bash
ant completions create \
  --api-key my-anthropic-api-key \
  --max-tokens-to-sample 256 \
  --model claude-fable-5-1 \
  --prompt '

Human: Hello, world!

Assistant:'
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
