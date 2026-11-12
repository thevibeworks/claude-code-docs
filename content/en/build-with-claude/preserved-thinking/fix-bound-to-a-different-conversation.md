---
title: Fix a thinking block bound to a different conversation
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation
description: Get a conversation going again after the 400 error that says a thinking block is bound to a different conversation, find what your code changed, and test that the change is gone.
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

Sending the same request again can’t work, because your history still holds what your code changed. Send `"drop_block"` to [stop the errors now](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#prefix-mismatch-error). The long-term fix is to make your code [append-only](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check).

## Error: The block is bound to a different conversation

The thinking block failed the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check): something before it changed after Claude produced it (see [What counts as a change](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#what-counts-as-an-edit)), or a thinking block between others was left out or moved. The error looks like this, and can go on to [name what changed](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#prefix-mismatch-error-details):

```text wrap
messages.1.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```

“A different conversation” means different content before the block: the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check) doesn’t compare sessions or users. The error message says to remove the block, but [removing only that block isn’t enough](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#remove-by-hand). [Other errors](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#similar-errors) can look similar.

If the app isn’t yours, start a new conversation and tell its maintainer. If you [removed a secret, personal data, or injected text](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#remove-sensitive-content), or your requests [turn thinking off](https://platform.claude.com/docs/en/build-with-claude/thinking#turning-thinking-off), [remove the thinking by hand](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#remove-by-hand) instead of step 1.

<Steps>
  <Step title="Stop the errors now">
    Set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`, and send the [beta header](https://platform.claude.com/docs/en/api/beta-headers#beta-features-on-other-platforms) `anthropic-beta: thinking-binding-controls-2026-08-01`. Do this on every later request in the conversation, because the API doesn’t store the setting between requests. A saved conversation still holds the change, even after you fix your code, so store the setting with it. Set `type` to `"adaptive"`, as shown:

    ```json
    {
      "thinking": {
        "type": "adaptive",
        "block_binding": {
          "prefix_mismatch_behavior": "drop_block"
        }
      }
    }
    ```

    In the SDK, call the beta Messages method and pass the header value, as [the test program](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#how-to-tell-whether-your-integration-is-impacted-details) does. If the error [still asks for the header](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#setting-not-received), the header didn’t arrive.

    That stops the errors by dropping the invalid thinking, but it [can cost more](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost) and can affect output quality and latency. The next request succeeds, and its `input_transformations` array lists each block the API dropped.

    If your requests don’t set the `thinking` parameter, adding it changes nothing else, because [models with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes) think adaptively by default.
  </Step>

  <Step title="Long-term fix">
    Make your integration append-only:

    1. Find the change. The error can name it. To find where your code makes it, run `claude update`, then run `/claude-api preserved-thinking-migration` in Claude Code in your code’s repository. Or [look by hand](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#find-the-change-details).
    2. Stop making the change, or new conversations can get the error too. [Send an update at the end instead](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions).
    3. Keep sending each running conversation the `system` and `tools` of [its last successful request](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#saved-sessions).
  </Step>
</Steps>

If the change was recent, you can undo it instead: put back what your code changed. The thinking from before the change is valid again. Thinking produced since then fails, so remove it or keep sending `"drop_block"`.

## What dropping thinking costs

Claude can spend more output tokens working out reasoning it can no longer read. Dropping the blocks also invalidates the prompt cache from the first dropped block onward.

When something changes on every turn, every turn loses the thinking from earlier turns, so the increase repeats. Run evals on your own workload before you rely on `"drop_block"`.

<Frame>
  ![Four requests after a change: the first is rejected; the next three drop the old thinking and keep each new block](https://platform.claude.com/docs/images/preserved-thinking-drop-block-loss.svg)
</Frame>

Use `"drop_block"` to keep existing conversations going while they hold a change you’re fixing, and for a planned drop, such as [after your own summary](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#own-summary). Don’t leave it on to hide a change your code keeps making. You can [stop sending it](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost-details) once the invalid blocks are out of the history.

## Find what your code changed

The change is before the first block that the API names. The 400 error can say what changed, such as `system`, `tools`, a missing thinking block, or the first message that differs. With no error, or one that doesn’t say, [start from what you have](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#find-the-change-details), such as a `prefix_binding_mismatch` entry or more output tokens.

## Test your code for prefix check failures

You can trust a test once you’ve seen it fail. First, through your own code, run a session that makes Claude think, and change something on purpose. Send `"drop_block"` for this step, so the response lists every invalid block instead of stopping at the first, as [five steps and a program](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#how-to-tell-whether-your-integration-is-impacted-details) show.

Then take that change out, and run your real sessions. On every request, send the beta header `thinking-binding-controls-2026-08-01`, and set [`prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#preserved-thinking-controls) to `"error"`, so a change your code makes in those sessions fails the build with the 400 error.

Test sessions that compact, add tools late, change instructions, [switch models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models), or resume: plain turns don’t reach that code.

A clean run has no `prefix_binding_mismatch` entry and no error. It shows only that the blocks it checked are valid, in the sessions you ran. It proves nothing if:

* the session had no thinking blocks
* your code removes all thinking, or the model doesn’t have preserved thinking
* you didn’t send the beta header, and [the model might let failing blocks through](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes) without an error

## Watch production, and find reasoning lost with no error

Log each 400 error, and [handle it in code](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#handle-the-error-in-code) so the conversation carries on. If you leave `prefix_mismatch_behavior` unset instead, [watch production traffic](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#watch-production-traffic) for failing thinking that reached Claude.

Reasoning can be lost with no error through `"drop_block"`, a batch item, a model switch, a move to [another account](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking), or code that sends no thinking back. With the beta header, each leaves an entry except the last. For that one, check that your requests hold `thinking` blocks.

## Technical details

### What else the error message can say

The error message goes on to name what changed, where the API can tell, such as `system`, `tools`, the first message or block that differs, content that is missing or new, or an earlier thinking block that is missing or out of order. That sentence’s wording can change, so don’t match on it. If the request had no beta header, the error message adds this sentence:

```text wrap
That setting requires the `thinking-binding-controls-2026-08-01` value in the `anthropic-beta` header.
```

### The error still asks for the header, or says `Extra inputs are not permitted`

If the error still asks for the header, the header didn’t reach the API: a proxy or library might have removed it. A different error, ending `block_binding: Extra inputs are not permitted`, means the same, or that thinking is off.

### Remove the invalid thinking by hand

Use this where you can’t send the setting, or in one of these cases:

* After you removed a secret, personal data, or injected text, because `"drop_block"` leaves the thinking in your stored history.
* When thinking is off (`"disabled"` or `"between_tools"`), because `"drop_block"` needs `"adaptive"`, which would turn thinking on and add output tokens.

1. Remove the block the error names, and every `thinking` and [`redacted_thinking`](https://platform.claude.com/docs/en/build-with-claude/thinking#redacted-thinking-blocks) block after it, or the same error then names the next invalid one. But if your history holds `role: "system"` messages, or two messages of the same role in a row, remove every `thinking` and `redacted_thinking` block. The error counts such a message as part of the message before it, so the position it names can be lower than the index in your array. The `path` of an `input_transformations` entry counts every message separately.
2. Keep every other block, and send the request again. Don’t put the removed blocks back.

### Errors that look like this one

These errors don’t say that the block is bound to a different conversation, and setting `prefix_mismatch_behavior` might not clear them:

* A message that stops after “Invalid `signature` in `thinking` block”, says “cannot be modified”, or is about `budget_tokens`: [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting)
* A message about `temperature` or a prefilled reply: [Limits and feature compatibility](https://platform.claude.com/docs/en/build-with-claude/thinking#limits-and-feature-compatibility)

### When you can stop sending `"drop_block"`

To stop sending `"drop_block"`, remove the blocks it drops and keep the thinking produced since. If nothing else has changed, the conversation then passes with `"error"`.

### Handle the error in code

To handle the error in code, send the beta header and `"error"` on every request, so a failure is a 400 error on every model. When it comes, switch that conversation alone to `"drop_block"` for every later request, store that choice with it, send again once, and log the error. If the same error comes back, the setting didn’t reach the API: see [The error still asks for the header, or says `Extra inputs are not permitted`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#setting-not-received).

Your code has to recognize this error by its `message` field, the exception to the general advice not to match an error’s text. Every 400 error has the type `invalid_request_error`, and this one has no `error.details.error_code`. Match only on “The block is bound to a different conversation”, because the rest of the message can change.

### You have no error, or one that doesn’t say what changed

* **The 400 error, and it names no change:** Compare the requests yourself. One cause is a compaction block sent without removing the messages it summarizes.

* **A `prefix_binding_mismatch` entry:** Compare `system`, `tools`, and `messages` up to the first entry’s `path` with the conversation as it was when that block was produced. If every block is listed, start with `system` and `tools`.

  If nothing differs, look for [an image or document URL whose content changed](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#files-by-id), an MCP server’s changed tool list (see [Pin an MCP server’s tool list](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#pin-mcp-tool-list)), or a thinking block left out, moved, or put back. Without request logs, send the request again with `"error"`, and read the sentence that says what differs, if there is one.

* **A proxy or library that isn’t yours, in between:** Compare what it sends with what you sent, and point its maintainer to [Libraries, proxies, and gateways](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#libraries-proxies-gateways).

* **Only a suspicion, and no Claude Code:** Capture a conversation’s request bodies, one with a compaction or a tool change. Compare each with the one before, leaving out its new turns.

### Five steps for a test that can fail, and a program that runs them

1. In your own code, send the beta header and `"drop_block"` on each request of a session, to a [model with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes).
2. Use prompts that make Claude think, and check that the first response has a `thinking` block. With adaptive thinking, Claude can skip thinking on an easy prompt.
3. Fail only on an `input_transformations` entry whose reason is `prefix_binding_mismatch`. A test that wants an empty array also fails after a model switch, because entries with `model_binding_mismatch` or `organization_binding_mismatch` are expected then.
4. Change something on purpose, such as adding a `system` prompt on the third request only.
5. Check that `input_transformations` lists the thinking blocks that sit after the change. If it lists none, check that the history holds a thinking block.

This program does steps 1, 2, 4, and 5. It prints how many thinking blocks and `input_transformations` entries each response has, then each entry, which is what step 3 checks:

<CodeGroup exclude="shell:cURL, shell:CLI">
  <CodeGroupItem language="cURL">
    This workflow needs more logic than a single shell command. Use the [Anthropic SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) to run it.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This workflow needs more logic than a single shell command. Use the [Anthropic SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) to run it.
  </CodeGroupItem>

  ```python Python
  client = anthropic.Anthropic()

  user_turns = [
      "How many positive integers below 500 have exactly 6 positive divisors?",
      "How many have exactly 8?",
      "How many have exactly 10?",
  ]

  messages = []
  for turn, user_turn in enumerate(user_turns, start=1):
      messages.append({"role": "user", "content": user_turn})
      response = client.beta.messages.create(
          model="claude-opus-5-5",
          max_tokens=16000,
          thinking={
              "type": "adaptive",
              "block_binding": {"prefix_mismatch_behavior": "drop_block"},
          },
          # Only the last request adds a system prompt, which changes the prefix on purpose
          system="Answer briefly." if turn == len(user_turns) else anthropic.omit,
          messages=messages,
          betas=["thinking-binding-controls-2026-08-01"],
      )
      messages.append({"role": "assistant", "content": response.content})
      thinking_blocks = sum(block.type == "thinking" for block in response.content)
      entries = response.input_transformations or []
      print(f"thinking blocks: {thinking_blocks}, entries: {len(entries)}")
      for entry in entries:
          if entry.type == "thinking_dropped":
              print(entry.type, entry.path, entry.reason)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const userTurns = [
    "How many positive integers below 500 have exactly 6 positive divisors?",
    "How many have exactly 8?",
    "How many have exactly 10?"
  ];

  const messages: Anthropic.Beta.BetaMessageParam[] = [];
  for (const [turnIndex, userTurn] of userTurns.entries()) {
    messages.push({ role: "user", content: userTurn });
    const response = await client.beta.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 16000,
      thinking: {
        type: "adaptive",
        block_binding: { prefix_mismatch_behavior: "drop_block" }
      },
      // Only the last request adds a system prompt, which changes the prefix on purpose
      system: turnIndex === userTurns.length - 1 ? "Answer briefly." : undefined,
      messages,
      betas: ["thinking-binding-controls-2026-08-01"]
    });
    messages.push({ role: "assistant", content: response.content });
    const thinkingBlocks = response.content.filter((block) => block.type === "thinking");
    const entries = response.input_transformations ?? [];
    console.log(`thinking blocks: ${thinkingBlocks.length}, entries: ${entries.length}`);
    for (const entry of entries) {
      if (entry.type === "thinking_dropped") {
        console.log(entry.type, entry.path, entry.reason);
      }
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  string[] userTurns =
  [
      "How many positive integers below 500 have exactly 6 positive divisors?",
      "How many have exactly 8?",
      "How many have exactly 10?",
  ];

  List<BetaMessageParam> messages = [];
  foreach (var (turnIndex, userTurn) in userTurns.Index())
  {
      messages.Add(new BetaUserMessageParam { Content = userTurn });
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
              // Only the last request adds a system prompt, which changes the prefix on purpose
              System = turnIndex == userTurns.Length - 1 ? new("Answer briefly.") : null,
              Messages = messages,
              Betas = [AnthropicBeta.ThinkingBindingControls2026_08_01],
          }
      );
      messages.Add(new BetaAssistantMessageParam
      {
          Content = response.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
      });
      var thinkingBlocks = response.Content.Count(block => block.TryPickThinking(out _));
      var entries = response.InputTransformations ?? [];
      Console.WriteLine($"thinking blocks: {thinkingBlocks}, entries: {entries.Count}");
      foreach (var entry in entries)
      {
          if (entry.TryPickThinkingDropped(out var dropped))
          {
              Console.WriteLine($"{dropped.Type} {dropped.Path} {dropped.Reason.Raw()}");
          }
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  userTurns := []string{
  	"How many positive integers below 500 have exactly 6 positive divisors?",
  	"How many have exactly 8?",
  	"How many have exactly 10?",
  }

  messages := []anthropic.BetaMessageParam{}
  for turnIndex, userTurn := range userTurns {
  	messages = append(messages, anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock(userTurn)))
  	// Only the last request adds a system prompt, which changes the prefix on purpose
  	var system []anthropic.BetaTextBlockParam
  	if turnIndex == len(userTurns)-1 {
  		system = []anthropic.BetaTextBlockParam{{Text: "Answer briefly."}}
  	}
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
  		System:   system,
  		Messages: messages,
  		Betas:    []anthropic.AnthropicBeta{anthropic.AnthropicBetaThinkingBindingControls2026_08_01},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  	messages = append(messages, response.ToParam())
  	thinkingBlocks := 0
  	for _, block := range response.Content {
  		if block.Type == "thinking" {
  			thinkingBlocks++
  		}
  	}
  	fmt.Printf("thinking blocks: %d, entries: %d\n", thinkingBlocks, len(response.InputTransformations))
  	for _, entry := range response.InputTransformations {
  		if entry.Type == "thinking_dropped" {
  			fmt.Println(entry.Type, entry.Path, entry.Reason)
  		}
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaContentBlock;
  import com.anthropic.models.beta.messages.BetaInputTransformation;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaThinkingBlockBinding;
  import com.anthropic.models.beta.messages.BetaThinkingConfigAdaptive;
  import com.anthropic.models.beta.messages.BetaThinkingPrefixMismatchBehavior;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      List<String> userTurns = List.of(
          "How many positive integers below 500 have exactly 6 positive divisors?",
          "How many have exactly 8?",
          "How many have exactly 10?");

      MessageCreateParams.Builder conversation = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(16000L)
          .thinking(BetaThinkingConfigAdaptive.builder()
              .blockBinding(BetaThinkingBlockBinding.builder()
                  .prefixMismatchBehavior(BetaThinkingPrefixMismatchBehavior.DROP_BLOCK)
                  .build())
              .build())
          .addBeta(AnthropicBeta.THINKING_BINDING_CONTROLS_2026_08_01);

      for (int turnIndex = 0; turnIndex < userTurns.size(); turnIndex++) {
          if (turnIndex == userTurns.size() - 1) {
              // Only the last request adds a system prompt, which changes the prefix on purpose
              conversation.system("Answer briefly.");
          }
          conversation.addUserMessage(userTurns.get(turnIndex));
          BetaMessage response = client.beta().messages().create(conversation.build());
          conversation.addMessage(response);
          long thinkingBlocks = response.content().stream()
              .filter(BetaContentBlock::isThinking)
              .count();
          List<BetaInputTransformation> entries = response.inputTransformations().orElse(List.of());
          IO.println("thinking blocks: " + thinkingBlocks + ", entries: " + entries.size());
          for (BetaInputTransformation entry : entries) {
              entry.thinkingDropped().ifPresent(dropped ->
                  IO.println(entry.type() + " " + dropped.path() + " " + dropped.reason()));
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaThinkingBlock;
  use Anthropic\Beta\Messages\BetaThinkingBlockBinding;
  use Anthropic\Beta\Messages\BetaThinkingConfigAdaptive;
  use Anthropic\Beta\Messages\BetaThinkingDroppedInputTransformation;
  use Anthropic\Beta\Messages\BetaThinkingPrefixMismatchBehavior;
  use Anthropic\Client;
  use Anthropic\Messages\Model;

  $client = new Client();

  $userTurns = [
      'How many positive integers below 500 have exactly 6 positive divisors?',
      'How many have exactly 8?',
      'How many have exactly 10?',
  ];

  $messages = [];
  foreach ($userTurns as $turnIndex => $userTurn) {
      $messages[] = ['role' => 'user', 'content' => $userTurn];
      $response = $client->beta->messages->create(
          model: Model::CLAUDE_OPUS_5_5,
          maxTokens: 16000,
          thinking: BetaThinkingConfigAdaptive::with(
              blockBinding: BetaThinkingBlockBinding::with(
                  prefixMismatchBehavior: BetaThinkingPrefixMismatchBehavior::DROP_BLOCK,
              ),
          ),
          // Only the last request adds a system prompt, which changes the prefix on purpose
          system: $turnIndex === array_key_last($userTurns) ? 'Answer briefly.' : null,
          messages: $messages,
          betas: [AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01],
      );
      $messages[] = ['role' => 'assistant', 'content' => $response->content];
      $thinkingBlocks = array_filter(
          $response->content,
          fn ($block) => $block instanceof BetaThinkingBlock,
      );
      $entries = $response->inputTransformations ?? [];
      echo 'thinking blocks: ', count($thinkingBlocks), ', entries: ', count($entries), PHP_EOL;
      foreach ($entries as $entry) {
          if ($entry instanceof BetaThinkingDroppedInputTransformation) {
              echo $entry->type, ' ', $entry->path, ' ', $entry->reason, PHP_EOL;
          }
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_turns = [
    "How many positive integers below 500 have exactly 6 positive divisors?",
    "How many have exactly 8?",
    "How many have exactly 10?"
  ]

  messages = []
  user_turns.each_with_index do |user_turn, turn_index|
    messages << { role: "user", content: user_turn }
    # Only the last request adds a system prompt, which changes the prefix on purpose
    system_param = (turn_index == user_turns.length - 1) ? { system_: "Answer briefly." } : {}
    response = client.beta.messages.create(
      model: Anthropic::Model::CLAUDE_OPUS_5_5,
      max_tokens: 16_000,
      thinking: {
        type: "adaptive",
        block_binding: { prefix_mismatch_behavior: "drop_block" }
      },
      messages: messages,
      betas: [Anthropic::AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01],
      **system_param
    )
    messages << { role: "assistant", content: response.content }
    thinking_blocks = response.content.count { |block| block.is_a?(Anthropic::Beta::BetaThinkingBlock) }
    entries = response.input_transformations || []
    puts "thinking blocks: #{thinking_blocks}, entries: #{entries.length}"
    entries.each do |entry|
      if entry.is_a?(Anthropic::Beta::BetaThinkingDroppedInputTransformation)
        puts "#{entry.type} #{entry.path} #{entry.reason}"
      end
    end
  end
  ```
</CodeGroup>

```text Output wrap
thinking blocks: 1, entries: 0
thinking blocks: 1, entries: 0
thinking blocks: 1, entries: 2
thinking_dropped messages.1.content.0 prefix_binding_mismatch
thinking_dropped messages.3.content.0 prefix_binding_mismatch
```

With `"error"` in place of `"drop_block"`, the third request gets [the 400 error](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#prefix-mismatch-error).

### What each `input_transformations` entry means, and which are yours to fix

With the beta header, a response from a model that supports thinking has the `input_transformations` array beside `usage`. It’s empty when nothing was dropped and nothing invalid was let through. When you stream, it’s in the `message_start` event’s `message`; after a mid-stream fallback, the final `message_delta` event carries the one that counts. Unlike the error’s position, `path` is always the block’s place as you sent it:

```json
{
  "input_transformations": [
    {
      "type": "thinking_dropped",
      "path": "messages.1.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```

Each entry’s `type` and `reason`, and what they mean:

* **`thinking_dropped`, `prefix_binding_mismatch`:** What came before this block isn’t what it recorded. Yours to fix: [Find what your code changed](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#find-the-change).
* **`thinking_mismatch_allowed`, `prefix_binding_mismatch`:** The same, but Claude read the block unchanged, and it’s billed. This entry appears only where the setting is unset, on [some models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes). Yours to fix.
* **`thinking_dropped`, `model_binding_mismatch`:** This model can’t read blocks from the model that produced it. Not yours to fix: [keep sending the whole conversation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models).
* **`thinking_dropped`, `organization_binding_mismatch`:** Another account produced the block, so [the API dropped it](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking). Not yours to fix.

Ignore an entry whose `type` or `reason` you don’t recognize.

### Batches and token counting

* **[Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing):** An item that leaves `prefix_mismatch_behavior` unset never gets the 400 error. The API drops the invalid blocks, or, on [some models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes), can let them through. An item that sets `"error"` resolves as `errored` when a block fails the prefix check. `block_binding` goes in the item’s `params.thinking`.
* **[Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting):** On the Claude API, token counting can return the same 400 error, and accepts `prefix_mismatch_behavior` under the same header. It leaves dropped blocks out of the count, and returns no `input_transformations`.

## Next steps

<CardGroup cols={2}>
  <Card title="Change tools or instructions without failing the prefix check" icon="edit" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions">
    What to send instead of each change your code makes to a conversation.
  </Card>

  <Card title="Preserved thinking" icon="book" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking">
    What preserved thinking is, what a thinking block is tied to, and switching models or accounts.
  </Card>

  <Card title="Troubleshooting thinking" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting">
    Fixes for other thinking errors, such as a signature that doesn’t verify.
  </Card>
</CardGroup>
