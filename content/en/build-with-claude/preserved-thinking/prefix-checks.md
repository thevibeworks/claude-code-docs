---
title: Prefix checks on thinking blocks
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks
description: What the prefix check compares, which models run it, what happens when a request fails it, and how to handle the 400 error and the case with no error.
featureMetadata:
  status: stable
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-opus-5-5
    - claude-sonnet-5-5
    - claude-haiku-5-5
  supportedPlatforms:
    Claude API: stable
    Amazon Bedrock: stable
    Amazon Bedrock (bedrock-runtime): stable
    Claude Platform on AWS: stable
    Claude Models on Google Cloud (Anthropic managed): stable
    Claude Models on Google Cloud (Google managed): stable
    Microsoft Foundry: stable
---

Each request that sends thinking blocks back to a [model with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes) gets a prefix check. A prefix check fails if `system`, `tools`, or an earlier message changed after Claude produced a block. It also fails if a thinking block between others was left out or moved.

Failing the prefix check might or might not result in a 400 error, [depending on the model](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes), so [handle both cases](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#handle-either-outcome).

## Who the prefix check affects

You have nothing to change if one of these is true:

* Claude Code, claude.ai, or Claude Managed Agents manages your conversation history.
* The Claude Agent SDK manages the history, and the system prompt you give the SDK stays the same.
* Your code follows [the three habits of an append-only integration](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check), and nothing rewrites its requests on the way.
* You call no [model with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes).

If your requests pass through a library, proxy, or gateway, [compare what it sends with what you sent](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#find-the-change-details). If you run one, see [Libraries, proxies, and gateways](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#libraries-proxies-gateways) for what to pass through.

## What must stay the same, and why

Make your integration append-only. Three habits do it:

1. Send each assistant turn back exactly as the API returned it, including thinking blocks whose text is empty.
2. Build `system` and `tools` once for each conversation, and send that copy every time.
3. Put every update in a new message at the end, and leave it there.

Each thinking block’s reasoning is about exactly what came before it: `system`, `tools`, and every earlier message. That content is the block’s *prefix*, and it’s what the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check-details) compares.

The prefix check is similar to prompt caching, except that a change makes the thinking after it invalid instead of only missing the cache.

Take an app that puts today’s date in its system prompt. At midnight the date changes, and so does the prefix of the thinking already in the conversation. That thinking becomes invalid, and the next request can fail. An append-only app keeps the system prompt as it was, and states the new date in [a message at the end](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#changing-context).

<Frame>
  ![An update at the end keeps all thinking valid; a change to turn 2, or to system, invalidates the thinking after it](https://platform.claude.com/docs/images/preserved-thinking-add-or-change.svg)
</Frame>

A change makes only the thinking that already follows it invalid. The thinking before it and the thinking Claude produces afterward stay valid.

## If your code changes the system prompt, tools, or history

| If your code…                                                                    | What to do                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rebuilds the system prompt with the date, a mode, or instruction files           | Stop changing `system`. [Append your own instructions as a system message](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#new-instructions), a `role: "system"` entry in `messages`, and [state new values in the newest turn](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#changing-context). For text that other people can edit, see [Text that other people can edit](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#untrusted-text) instead. |
| Adds, removes, or rewords a tool, or gains tools when an MCP server connects     | Stop changing `tools`, and [add or remove tools in a system message](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#tool-changes).                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Trims, collapses, or summarizes older turns, and keeps the latest ones unchanged | [Let the API write the summary, or remove the kept turns’ thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#server-side-trimming).                                                                                                                                                                                                                                                                                                                                                                                                                         |

Other causes, such as skipping thinking blocks whose text is empty or rebuilding a saved conversation, have fixes of their own: see [Change tools or instructions without failing the prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions). To find yours, [have an agent check your code](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#hand-to-an-agent).

## What each model does when the prefix check fails

On the Claude API and [some cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#feature-availability), the result of failing the prefix check with [`prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#preserved-thinking-controls) unset depends on the model:

| Model with preserved thinking | Result                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Claude Fable 5.2              | 400 error                                                                                                                       |
| Claude Mythos 5.2             | 400 error                                                                                                                       |
| Claude Mythos 5.1             | 400 error                                                                                                                       |
| Claude Fable 5.1              | [Possible 400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#possible-400-error) |
| Claude Opus 5.5               | [Possible 400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#possible-400-error) |
| Claude Sonnet 5.5             | [Possible 400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#possible-400-error) |
| Claude Haiku 5.5              | [Possible 400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#possible-400-error) |

Where the table says “Possible 400 error,” there are two cases: a request that fails the prefix check might get a 400 error or no error. When no error is returned, the failing blocks reach the model. Claude reads them like any other input, you’re billed for them, and Claude works from reasoning about content that has since changed.

On those models, you can [check which case a request gets](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#check-which-case), but [handle both cases](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#handle-either-outcome).

<Tip>
  Code that follows [the three habits of an append-only integration](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check) doesn’t cause prefix check failures.
</Tip>

[Message Batches items](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#batches) that leave `prefix_mismatch_behavior` unset get no error, and the API can drop the failing blocks.

## Handle both cases

For one result on every request, make your integration append-only or set `prefix_mismatch_behavior`. Otherwise, your code must handle both behaviors.

* **Append-only:** with [the three habits](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check), your code doesn’t make a request fail the prefix check.
* **The setting:** with `"error"` on every request, each failure is a 400 error, and you [catch it in code](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#handle-the-error-in-code).
* **Both behaviors:** if you leave the setting unset, catch the 400 error, and [watch for failing thinking that reached Claude](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#watch-production-traffic).

After a 400 error, send `"drop_block"` on that conversation’s later requests to recover. It has a cost: see [What dropping thinking costs](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost). Don’t send it on all your conversations to hide errors.

## Technical details

### How the prefix check works

The models with preserved thinking record a fingerprint of each thinking block’s prefix in its `signature`. The API reference calls the prefix check the conversation check, and the 400 error says that a failing block `is bound to a different conversation`.

### Which models run the prefix check

The prefix check runs on the Claude API and on [some cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#feature-availability). It checks thinking blocks that a [model with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes) produced, on requests to one of those models. On the Claude API, other models, such as Claude Opus 5, don’t run it, and it doesn’t cover their blocks.

### What counts as a change

* **Each block is checked against its own record.** The API compares what’s before a block in this request with what its signature recorded when Claude produced it. Your last request plays no part. The prefix check looks only at content, not at sessions, IDs, or users. The same content in a new request or a fork passes it.
* **The prefix check compares what you sent, not what Claude read.** [Compaction at a token threshold](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) and context editing change only what Claude reads, so they never count. After a threshold compaction block, the API compares only the messages from that block on, plus `system` and `tools`. On-demand compaction has its own conditions: see [Conditions for kept thinking to stay valid](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid). For a file sent by URL and, on the Claude API, [an MCP tool list](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#pin-mcp-tool-list), the API compares what it fetched instead.
* **The thinking you send must be an unbroken run.** Thinking blocks aren’t compared as content. But each one you send, apart from the first, must have the same previous thinking block as when Claude produced it. So you can [leave out the oldest, the newest, or all of them](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#leave-out-thinking), but not one in between.

A change can be as small as one word of a tool description. Changing, inserting, moving, or deleting an earlier message counts, whatever its role. So does changing text before a thinking block in its own message.

### What doesn’t count

| This doesn’t count                                                                                   | Because                                                       |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `model`, `effort`, `max_tokens`, `tool_choice`, `metadata`, `thinking.display`, and other parameters | Only `system`, `tools`, and messages are compared             |
| JSON formatting or key order                                                                         | The API compares parsed JSON, not its text                    |
| `cache_control` markers                                                                              | They say where to cache, and aren’t content that Claude reads |
| A tool with `defer_loading: true` that nothing has referred to                                       | It isn’t in Claude’s context until something refers to it     |

### Set `prefix_mismatch_behavior`

The [beta header](https://platform.claude.com/docs/en/api/beta-headers#beta-features-on-other-platforms) `thinking-binding-controls-2026-08-01` adds the setting `thinking.block_binding.prefix_mismatch_behavior` and the response’s `input_transformations` array.

| Value              | If a block fails the prefix check                                                                                                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"error"`          | The API rejects the request with a 400 error that names the first invalid block                                                                                                                                                                                   |
| `"drop_block"`     | The API drops the invalid blocks, and the request succeeds. You aren’t billed for those blocks, but [dropping them can cost more](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost) |
| Not set, or `null` | [Depends on the model](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes)                                                                                                                                           |

Blocks that fail the prefix check stay invalid on every later request that sends them, while the change is in place. The setting acts on the one request that carries it. With thinking off (`"disabled"` or `"between_tools"`), sending it is a 400 error on every model.

The following request sets `prefix_mismatch_behavior` to `"drop_block"`. On a first turn there’s no thinking to send back, so `input_transformations` comes back empty:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: thinking-binding-controls-2026-08-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 16000,
      "thinking": {
        "type": "adaptive",
        "block_binding": {
          "prefix_mismatch_behavior": "drop_block"
        }
      },
      "messages": [
        {
          "role": "user",
          "content": "What is the greatest common divisor of 1071 and 462?"
        }
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta thinking-binding-controls-2026-08-01 <<'YAML'
  model: claude-opus-5-5
  max_tokens: 16000
  thinking:
    type: adaptive
    block_binding:
      prefix_mismatch_behavior: drop_block
  messages:
    - role: user
      content: What is the greatest common divisor of 1071 and 462?
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-opus-5-5",
      max_tokens=16000,
      thinking={
          "type": "adaptive",
          "block_binding": {"prefix_mismatch_behavior": "drop_block"},
      },
      messages=[
          {
              "role": "user",
              "content": "What is the greatest common divisor of 1071 and 462?",
          }
      ],
      betas=["thinking-binding-controls-2026-08-01"],
  )

  for block in response.content:
      if block.type == "text":
          print(block.text)

  print(f"Input transformations: {len(response.input_transformations or [])}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 16000,
    thinking: {
      type: "adaptive",
      block_binding: { prefix_mismatch_behavior: "drop_block" }
    },
    messages: [
      { role: "user", content: "What is the greatest common divisor of 1071 and 462?" }
    ],
    betas: ["thinking-binding-controls-2026-08-01"]
  });

  for (const block of response.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  console.log(`Input transformations: ${response.input_transformations?.length ?? 0}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var response = await client.Beta.Messages.Create(
      new()
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 16000,
          Thinking = new BetaThinkingConfigAdaptive
          {
              BlockBinding = new()
              {
                  PrefixMismatchBehavior = BetaThinkingPrefixMismatchBehavior.DropBlock,
              },
          },
          Messages =
          [
              new BetaUserMessageParam
              {
                  Content = "What is the greatest common divisor of 1071 and 462?",
              },
          ],
          Betas = [AnthropicBeta.ThinkingBindingControls2026_08_01],
      }
  );

  foreach (var block in response.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
      }
  }

  Console.WriteLine($"Input transformations: {response.InputTransformations?.Count ?? 0}");
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 16000,
  	Thinking: anthropic.BetaThinkingConfigParamUnion{
  		OfAdaptive: &anthropic.BetaThinkingConfigAdaptiveParam{
  			BlockBinding: anthropic.BetaThinkingBlockBindingParam{
  				PrefixMismatchBehavior: anthropic.BetaThinkingPrefixMismatchBehaviorDropBlock,
  			},
  		},
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("What is the greatest common divisor of 1071 and 462?")),
  	},
  	Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaThinkingBindingControls2026_08_01},
  })
  if err != nil {
  	log.Fatal(err)
  }

  for _, block := range response.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  fmt.Printf("Input transformations: %d\n", len(response.InputTransformations))
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaThinkingBlockBinding;
  import com.anthropic.models.beta.messages.BetaThinkingConfigAdaptive;
  import com.anthropic.models.beta.messages.BetaThinkingPrefixMismatchBehavior;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(16000L)
          .addBeta(AnthropicBeta.THINKING_BINDING_CONTROLS_2026_08_01)
          .thinking(BetaThinkingConfigAdaptive.builder()
              .blockBinding(BetaThinkingBlockBinding.builder()
                  .prefixMismatchBehavior(BetaThinkingPrefixMismatchBehavior.DROP_BLOCK)
                  .build())
              .build())
          .addUserMessage("What is the greatest common divisor of 1071 and 462?")
          .build();

      BetaMessage response = client.beta().messages().create(params);

      response.content().stream()
          .flatMap(block -> block.text().stream())
          .forEach(textBlock -> IO.println(textBlock.text()));
      IO.println("Input transformations: "
          + response.inputTransformations().map(List::size).orElse(0));
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaTextBlock;
  use Anthropic\Beta\Messages\BetaThinkingBlockBinding;
  use Anthropic\Beta\Messages\BetaThinkingConfigAdaptive;
  use Anthropic\Beta\Messages\BetaThinkingPrefixMismatchBehavior;
  use Anthropic\Client;
  use Anthropic\Messages\Model;

  $client = new Client();

  $response = $client->beta->messages->create(
      model: Model::CLAUDE_OPUS_5_5,
      maxTokens: 16000,
      thinking: BetaThinkingConfigAdaptive::with(
          blockBinding: BetaThinkingBlockBinding::with(
              prefixMismatchBehavior: BetaThinkingPrefixMismatchBehavior::DROP_BLOCK,
          ),
      ),
      messages: [
          ['role' => 'user', 'content' => 'What is the greatest common divisor of 1071 and 462?'],
      ],
      betas: [AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01],
  );

  foreach ($response->content as $block) {
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }

  echo 'Input transformations: ', count($response->inputTransformations ?? []), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 16_000,
    thinking: {
      type: "adaptive",
      block_binding: { prefix_mismatch_behavior: "drop_block" }
    },
    messages: [
      { role: "user", content: "What is the greatest common divisor of 1071 and 462?" }
    ],
    betas: [Anthropic::AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01]
  )

  response.content.each do |block|
    puts block.text if block.is_a?(Anthropic::Beta::BetaTextBlock)
  end

  puts "Input transformations: #{response.input_transformations&.length || 0}"
  ```
</CodeGroup>

### Watch production traffic

With `prefix_mismatch_behavior` unset, a request that fails the prefix check might get no error on [some models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes). The thinking blocks that failed it then reach the model. To find those blocks in production traffic, send the `thinking-binding-controls-2026-08-01` beta header, leave the setting unset, and log each response’s `input_transformations` array. The header adds that array and doesn’t change what the model receives.

Each of those blocks gets its own `thinking_mismatch_allowed` entry in that array. One entry looks like this:

```json
{
  "input_transformations": [
    {
      "type": "thinking_mismatch_allowed",
      "path": "messages.1.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```

To find the change, see [Find what your code changed](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#find-the-change).

### Check which case you get

On [some models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes), a request that fails the prefix check might get the 400 error or no error. This test shows which one a request gets:

1. Take a conversation that holds a thinking block from one of those models. Change or add the system prompt (`system`). The block then fails the prefix check, because the system prompt changed after Claude produced the block.
2. Send it to the same model with the `thinking-binding-controls-2026-08-01` beta header, and leave `prefix_mismatch_behavior` unset.

The response is one of these:

* **A [400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#prefix-mismatch-error) that says `bound to a different conversation`:** The request got the 400 error.
* **A 200 response whose `input_transformations` array has `thinking_mismatch_allowed` entries:** The request got no error. Each entry names a thinking block that failed the prefix check and reached Claude.
* **A 200 response whose `input_transformations` array is empty:** No block failed the prefix check, so the test shows nothing. Check that the conversation holds a thinking block from that model.

The result describes that one request and promises nothing about later ones, so write your code to [handle both cases](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#handle-either-outcome).

## Next steps

<CardGroup cols={2}>
  <Card title="Change tools or instructions without failing the prefix check" icon="edit" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions">
    What to send instead of each change your code makes to a conversation.
  </Card>

  <Card title="Fix a thinking block bound to a different conversation" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation">
    Recover a failing conversation, find what your code changes, and test that it’s gone.
  </Card>

  <Card title="Preserved thinking" icon="book" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking">
    What preserved thinking is, what a thinking block is tied to, and switching models or accounts.
  </Card>
</CardGroup>
