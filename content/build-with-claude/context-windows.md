# Context windows

## Understanding the context window

The "context window" refers to the entirety of the amount of text a language model can look back on and reference when generating new text plus the new text it generates. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model's ability to handle longer prompts or maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests<sup>1</sup>:

<img src="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=0e62b88b8d27b13a38dd2261151bada6" alt="Context window diagram" width="960" height="540" data-path="images/context-window.svg" srcset="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=280&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=15217c635e7fa4e3d0232596b130ab5f 280w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=560&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=410ccef1e9484312e5d237abebb0b92d 560w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=840&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=0cd3d05f9afc51cae39617faa8dc198b 840w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=1100&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=55b98bd4f8fbca7ed17a2e95cbe1305d 1100w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=1650&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=f24e0b490b7255ed46e20bf6741ee40c 1650w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window.svg?w=2500&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=31d2e486b9dc35bae8768035fe9dadf8 2500w" data-optimize="true" data-opv="2" />

*<sup>1</sup>For chat interfaces, such as for [claude.ai](https://claude.ai/), context windows can also be set up on a rolling "first in, first out" system.*

* **Progressive token accumulation:** As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
* **Linear growth pattern:** The context usage grows linearly with each turn, with previous turns preserved completely.
* **200K token capacity:** The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
* **Input-output flow:** Each turn consists of:
  * **Input phase:** Contains all previous conversation history plus the current user message
  * **Output phase:** Generates a text response that becomes part of a future input

## The context window with extended thinking

When using [extended thinking](/en/docs/build-with-claude/extended-thinking), all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your `max_tokens` parameter, are billed as output tokens, and count towards rate limits.

However, previous thinking blocks are automatically stripped from the context window calculation by the Anthropic API and are not part of the conversation history that the model "sees" for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:

<img src="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=04b846fd3ba0f4b7226625e6fe0df521" alt="Context window diagram with extended thinking" width="960" height="540" data-path="images/context-window-thinking.svg" srcset="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=280&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=5767751c7ffa7490582b5fcedb6ef7fc 280w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=560&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=645d7dcb55362f97bdc5b9463c0a15cb 560w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=840&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=b464ed30bc6be176abb10fdd44223880 840w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=1100&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=c3df4f5ea3abf812ee1ba821c2147249 1100w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=1650&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=982061a3bd0d9c9790e7426d1f527a5b 1650w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking.svg?w=2500&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=e47e1184fdfc6c419eb831964ed3e099 2500w" data-optimize="true" data-opv="2" />

* **Stripping extended thinking:** Extended thinking blocks (shown in dark gray) are generated during each turn's output phase, **but are not carried forward as input tokens for subsequent turns**. You do not need to strip the thinking blocks yourself. The Anthropic API automatically does this for you if you pass them back.
* **Technical implementation details:**
  * The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
  * Extended thinking tokens are billed as output tokens only once, during their generation.
  * The effective context window calculation becomes: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
  * Thinking tokens include both `thinking` blocks and `redacted_thinking` blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

<Note>
  You can read more about the context window and extended thinking in our [extended thinking guide](/en/docs/build-with-claude/extended-thinking).
</Note>

## The context window with extended thinking and tool use

The diagram below illustrates the context window token management when combining extended thinking with tool use:

<img src="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=abac14cef66ec78f5e1d5c5af3ce2a07" alt="Context window diagram with extended thinking and tool use" width="960" height="540" data-path="images/context-window-thinking-tools.svg" srcset="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=280&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=feaca52ddb494510564bf6f07c283ef2 280w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=560&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=86c2794d92ba4e383c18cf12ed4c408e 560w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=840&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=c015777c4c8a8f5ea5afab1c4ce208fa 840w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=1100&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=46f402c47bd12f5708dafa3920e34a43 1100w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=1650&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=4af8894489f02c9d3a06267f18669536 1650w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/context-window-thinking-tools.svg?w=2500&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=bdfe909837efde6d190ee362e7767168 2500w" data-optimize="true" data-opv="2" />

<Steps>
  <Step title="First turn architecture">
    * **Input components:** Tools configuration and user message
    * **Output components:** Extended thinking + text response + tool use request
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Tool result handling (turn 2)">
    * **Input components:** Every block in the first turn as well as the `tool_result`. The extended thinking block **must** be returned with the corresponding tool results. This is the only case wherein you **have to** return thinking blocks.
    * **Output components:** After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next `user` message).
    * **Token calculation:** All input and output components count toward the context window, and all output components are billed as output tokens.
  </Step>

  <Step title="Third Step">
    * **Input components:** All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next `User` turn.
    * **Output components:** Since there is a new `User` turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
    * **Token calculation:** Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current `Assistant` turn counts as part of the context window.
  </Step>
</Steps>

* **Considerations for tool use with extended thinking:**
  * When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
  * The effective context window calculation for extended thinking with tool use becomes: `context_window = input_tokens + current_turn_tokens`.
  * The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude's reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

<Note>
  Claude 4 models support [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking), which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

  Claude Sonnet 3.7 does not support interleaved thinking, so there is no interleaving of extended thinking and tool calls without a non-`tool_result` user turn in between.

  For more information about using tools with extended thinking, see our [extended thinking guide](/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use).
</Note>

## 1M token context window

Claude Sonnet 4 supports a 1-million token context window. This extended context window allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases.

<Note>
  The 1M token context window is currently in beta for organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. The 1M token context window is only available for Claude Sonnet 4.
</Note>

To use the 1M token context window, include the `context-1m-2025-08-07` [beta header](/en/api/beta-headers) in your API requests:

<CodeGroup>
  ```python Python
  from anthropic import Anthropic

  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-20250514",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Process this large document..."}
      ],
      betas=["context-1m-2025-08-07"]
  )
  ```

  ```typescript TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const msg = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 1024,
    messages: [
      { role: 'user', content: 'Process this large document...' }
    ],
    betas: ['context-1m-2025-08-07']
  });
  ```

  ```curl cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: context-1m-2025-08-07" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-20250514",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Process this large document..."}
      ]
    }'
  ```
</CodeGroup>

**Important considerations:**

* **Beta status**: This is a beta feature subject to change. Features and pricing may be modified or removed in future releases.
* **Usage tier requirement**: The 1M token context window is available to organizations in [usage tier](/en/api/rate-limits) 4 and organizations with custom rate limits. Lower tier organizations must advance to usage tier 4 to access this feature.
* **Availability**: The 1M token context window is currently available on the Anthropic API, [Amazon Bedrock](/en/api/claude-on-amazon-bedrock), and [Google Cloud's Vertex AI](/en/api/claude-on-vertex-ai).
* **Pricing**: Requests exceeding 200K tokens are automatically charged at premium rates (2x input, 1.5x output pricing). See the [pricing documentation](/en/docs/about-claude/pricing#long-context-pricing) for details.
* **Rate limits**: Long context requests have dedicated rate limits. See the [rate limits documentation](/en/api/rate-limits#long-context-rate-limits) for details.
* **Multimodal considerations**: When processing large numbers of images or pdfs, be aware that the files can vary in token usage. When pairing a large prompt with a large number of images, you may hit [request size limits](https://docs.anthropic.com/en/api/overview#request-size-limits).

## Context window management with newer Claude models

In newer Claude models (starting with Claude Sonnet 3.7), if the sum of prompt tokens and output tokens exceeds the model's context window, the system will return a validation error rather than silently truncating the context. This change provides more predictable behavior but requires more careful token management.

To plan your token usage and ensure you stay within context window limits, you can use the [token counting API](/en/docs/build-with-claude/token-counting) to estimate how many tokens your messages will use before sending them to Claude.

See our [model comparison](/en/docs/about-claude/models/overview#model-comparison-table) table for a list of context window sizes by model.

# Next steps

<CardGroup cols={2}>
  <Card title="Model comparison table" icon="scale-balanced" href="/en/docs/about-claude/models/overview#model-comparison-table">
    See our model comparison table for a list of context window sizes and input / output token pricing by model.
  </Card>

  <Card title="Extended thinking overview" icon="head-side-gear" href="/en/docs/build-with-claude/extended-thinking">
    Learn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.
  </Card>
</CardGroup>
