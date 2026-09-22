---
title: Compaction and preserved thinking
url: https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks
description: When thinking blocks in turns kept after on-demand compaction stay valid on models with preserved thinking, and how to check.
featureMetadata:
  status: beta
  betaHeader: compact-2026-09-04
  supportedModels:
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-5
    - claude-sonnet-4-6
  supportedPlatforms:
    Claude API: beta
    Claude Platform on AWS: beta
    Amazon Bedrock: not available
    Google Cloud: beta
    Microsoft Foundry: beta
---

Skip this page unless you send thinking blocks back to a model with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) and keep turns after the compaction block. Kept turns are the turns that follow the block: recent turns you left out of the compaction request, as in [Compaction that keeps recent turns](https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns), or turns that arrived while the summary was being written, as in [Compaction in the background](https://platform.claude.com/docs/en/build-with-claude/compaction-background).

Models with preserved thinking check earlier thinking blocks against the conversation that produced them. A summary replaces part of that conversation, but the check accepts the swap when the API wrote the summary, so the thinking in kept turns can stay valid.

## Conditions for kept thinking to stay valid

The thinking blocks in kept turns stay valid while all of these hold:

* **The compaction request runs on a model with preserved thinking.** This condition covers every compaction request since a thinking block was produced, not only the most recent one. One way to meet it is to send every compaction request to the model the conversation uses.
* **The kept turns directly follow the summarized messages, and you send them unchanged.** Send each kept message exactly as it is in your history. Don't skip or add a message between the last summarized message and the first kept one. The first kept message must also have a different role from the last summarized message, and it can't be a mid-conversation `role: "system"` message. Otherwise, the API merges it into the last summarized message. One way to get the first kept message right is to compact exactly the `messages` of a request you already sent. The kept turns then start with Claude's reply to it.
* **`system` and the `tools` not marked `defer_loading: true` don't change.** They are the same on the compaction request as on the requests that produced the kept thinking, and they stay the same on the requests that follow. [Change the system prompt or tools](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#change-the-system-prompt-or-tools) covers how to change them safely.

If a condition doesn't hold, nothing fails when you compact, and the API accepts the block on later requests either way. The failure comes on the first later request that sends the kept thinking where the API enforces the check: a 400 error by default, or dropped thinking blocks if the request sets `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. In the Message Batches API, an item that leaves the field unset doesn't fail. Where the check applies by default, the API drops the blocks instead. [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) describes both outcomes, and [When the API enforces the check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#enforcement) says which requests are checked.

## Compact again without breaking older thinking

You can [compact again](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#compact-again) and keep turns: the new block covers the old summary and every message that follows it in the compaction request, and any turns you leave out of that request are kept turns of the new block.

The first of the [conditions for kept thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) counts every compaction since a thinking block was produced, so a turn that you keep through two compactions needs both to have run on a model with preserved thinking.

Compactions from before a thinking block was produced don't count against it. Thinking produced after a block is in place is bound to that block, and it stays valid through later compactions that meet the conditions.

## Change the system prompt or tools

A later request can use a different `system`, different `tools`, or a different model than the compaction request, and the API still accepts the block. Such a change can invalidate the thinking in the kept turns, but it has no other effect.

To change `system` or `tools` without invalidating any kept thinking, compact the whole conversation first, so no turns are kept. Then change them on the next request.

To add an instruction or change the available tools without touching `system` or `tools`, append the change to `messages`, as described in [Make changes without editing the prefix](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#replace-prefix-edits).

Mid-conversation system messages inside the summarized turns are summarized too, so their text instructions stop applying after the swap. To keep one in force, state it again in a `role: "system"` message directly after the first new `user` turn that follows the kept turns. Tool changes inside those turns carry over on their own when the compaction request also carries `inline-tools-2026-09-15`: the returned block records their net effect in its `tool_changes` field, so send the block back unmodified. If the block has no `tool_changes` field, restate those tool changes the same way. A system message placed between the block and the kept turns breaks their thinking.

## Check that the kept thinking held

The compaction response doesn't say whether the kept thinking holds. The first request after the swap does. To check in your tests:

1. Have a short conversation with thinking on. Use a model on which the API runs the check (see [When the API enforces the check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#enforcement)), and use it for every step, because a model that can't read a thinking block drops it with no error.
2. Compact the older turns, and keep at least one turn that holds a thinking block.
3. Send the next request, with the block first, then the kept turn, then a new `user` message, and with `thinking.block_binding.prefix_mismatch_behavior` set to `"error"`.
4. Read the result. A 200 response whose `input_transformations` array is empty means no thinking block failed the check or was dropped. A 400 error that says the block is bound to a different conversation means one did. The message starts with the path of the first block that failed, and [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) shows it in full.

The `prefix_mismatch_behavior` field needs the `thinking-binding-controls-2026-08-01` beta header in addition to [the `compact-2026-09-04` beta header](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary). Setting the field also opts the request into the check on accounts where the check isn't on by default.

The following program runs the four steps. It prints how many thinking blocks the kept turn holds and how many entries `input_transformations` has; no entries means the kept thinking held:

<CodeGroup exclude="shell">
  ```python Python
  from anthropic.types.beta import BetaMessageParam, BetaThinkingConfigParam

  client = anthropic.Anthropic()

  # Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  MODEL = "claude-fable-5-1"
  BETAS = ["compact-2026-09-04", "thinking-binding-controls-2026-08-01"]
  SYSTEM = "You help plan a recipe app's release. Keep answers short."
  # With "error", a thinking block that fails the check makes the request fail with a 400.
  THINKING: BetaThinkingConfigParam = {
      "type": "adaptive",
      "block_binding": {"prefix_mismatch_behavior": "error"},
  }

  # 1. Have a short conversation with thinking on.
  history: list[BetaMessageParam] = [
      {"role": "user", "content": "What are the main entities in the app's data model?"}
  ]
  first = client.beta.messages.create(
      model=MODEL,
      max_tokens=8192,
      system=SYSTEM,
      betas=BETAS,
      thinking=THINKING,
      messages=history,
  )
  history += [
      {"role": "assistant", "content": first.content},
      {
          "role": "user",
          "content": "Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?",
      },
  ]
  second = client.beta.messages.create(
      model=MODEL,
      max_tokens=8192,
      system=SYSTEM,
      betas=BETAS,
      thinking=THINKING,
      messages=history,
  )
  history.append({"role": "assistant", "content": second.content})
  thinking_blocks = sum(block.type == "thinking" for block in second.content)
  print(f"Thinking blocks in the kept turn: {thinking_blocks}")

  # 2. Summarize the first turn. The second turn stays out of the request.
  summary = client.beta.messages.create(
      model=MODEL,
      max_tokens=4096,
      system=SYSTEM,
      betas=BETAS,
      thinking=THINKING,
      messages=history[:2],
      compaction={"type": "summarize"},
  )
  if summary.stop_reason != "compaction":
      raise SystemExit(f"No summary: {summary.stop_reason}")

  # 3. Put the block in front of the kept turn and ask the next question.
  history = [
      {"role": "assistant", "content": summary.content},
      *history[2:],
      {"role": "user", "content": "Which day should the release go out?"},
  ]
  third = client.beta.messages.create(
      model=MODEL,
      max_tokens=8192,
      system=SYSTEM,
      betas=BETAS,
      thinking=THINKING,
      messages=history,
  )

  # 4. A 200 with no dropped blocks means the kept thinking held.
  print(f"Dropped thinking blocks: {len(third.input_transformations)}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  const model: Anthropic.Model = "claude-fable-5-1";
  const betas: Anthropic.Beta.AnthropicBeta[] = [
    "compact-2026-09-04",
    "thinking-binding-controls-2026-08-01"
  ];
  const systemPrompt = "You help plan a recipe app's release. Keep answers short.";
  // With "error", a thinking block that fails the check makes the request fail with a 400.
  const thinking: Anthropic.Beta.Messages.BetaThinkingConfigParam = {
    type: "adaptive",
    block_binding: { prefix_mismatch_behavior: "error" }
  };

  // 1. Have a short conversation with thinking on.
  let history: Anthropic.Beta.Messages.BetaMessageParam[] = [
    { role: "user", content: "What are the main entities in the app's data model?" }
  ];
  const first = await client.beta.messages.create({
    model,
    max_tokens: 8192,
    system: systemPrompt,
    betas,
    thinking,
    messages: history
  });
  history.push(
    { role: "assistant", content: first.content },
    {
      role: "user",
      content:
        "Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?"
    }
  );
  const second = await client.beta.messages.create({
    model,
    max_tokens: 8192,
    system: systemPrompt,
    betas,
    thinking,
    messages: history
  });
  history.push({ role: "assistant", content: second.content });
  const thinkingBlocks = second.content.filter((block) => block.type === "thinking").length;
  console.log(`Thinking blocks in the kept turn: ${thinkingBlocks}`);

  // 2. Summarize the first turn. The second turn stays out of the request.
  const summary = await client.beta.messages.create({
    model,
    max_tokens: 4096,
    system: systemPrompt,
    betas,
    thinking,
    messages: history.slice(0, 2),
    compaction: { type: "summarize" }
  });
  if (summary.stop_reason !== "compaction") {
    throw new Error(`No summary: ${summary.stop_reason}`);
  }

  // 3. Put the block in front of the kept turn and ask the next question.
  history = [
    { role: "assistant", content: summary.content },
    ...history.slice(2),
    { role: "user", content: "Which day should the release go out?" }
  ];
  const third = await client.beta.messages.create({
    model,
    max_tokens: 8192,
    system: systemPrompt,
    betas,
    thinking,
    messages: history
  });

  // 4. A 200 with no dropped blocks means the kept thinking held.
  console.log(`Dropped thinking blocks: ${third.input_transformations?.length ?? 0}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  // Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  const Model ModelId = Model.ClaudeFable5_1;
  AnthropicBeta[] betas = [AnthropicBeta.Compact2026_09_04, AnthropicBeta.ThinkingBindingControls2026_08_01];
  const string SystemPrompt = "You help plan a recipe app's release. Keep answers short.";
  // With "error", a thinking block that fails the check makes the request fail with a 400.
  BetaThinkingConfigAdaptive thinking = new()
  {
      BlockBinding = new() { PrefixMismatchBehavior = BetaThinkingPrefixMismatchBehavior.Error },
  };

  // 1. Have a short conversation with thinking on.
  List<BetaMessageParam> history =
  [
      new() { Role = Role.User, Content = "What are the main entities in the app's data model?" },
  ];
  var first = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = ModelId,
      MaxTokens = 8192,
      System = SystemPrompt,
      Betas = [.. betas],
      Thinking = thinking,
      Messages = history,
  });
  history.AddRange(
  [
      new()
      {
          Role = Role.Assistant,
          Content = first.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
      },
      new()
      {
          Role = Role.User,
          Content = "Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?",
      },
  ]);
  var second = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = ModelId,
      MaxTokens = 8192,
      System = SystemPrompt,
      Betas = [.. betas],
      Thinking = thinking,
      Messages = history,
  });
  history.Add(new()
  {
      Role = Role.Assistant,
      Content = second.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
  });
  var thinkingBlocks = second.Content.Count(block => block.TryPickThinking(out _));
  Console.WriteLine($"Thinking blocks in the kept turn: {thinkingBlocks}");

  // 2. Summarize the first turn. The second turn stays out of the request.
  var summary = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = ModelId,
      MaxTokens = 4096,
      System = SystemPrompt,
      Betas = [.. betas],
      Thinking = thinking,
      Messages = history[..2],
      Compaction = new BetaCompactionConfig(), // type defaults to "summarize"
  });
  if (summary.StopReason != BetaStopReason.Compaction)
  {
      throw new InvalidOperationException($"No summary: {summary.StopReason?.Raw()}");
  }

  // 3. Put the block in front of the kept turn and ask the next question.
  history =
  [
      new()
      {
          Role = Role.Assistant,
          Content = summary.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
      },
      .. history[2..],
      new() { Role = Role.User, Content = "Which day should the release go out?" },
  ];
  var third = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = ModelId,
      MaxTokens = 8192,
      System = SystemPrompt,
      Betas = [.. betas],
      Thinking = thinking,
      Messages = history,
  });

  // 4. A 200 with no dropped blocks means the kept thinking held.
  Console.WriteLine($"Dropped thinking blocks: {third.InputTransformations?.Count ?? 0}");
  ```

  ```go Go
  ctx := context.Background()
  client := anthropic.NewClient()

  // Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  const model = anthropic.ModelClaudeFable5_1
  betas := []anthropic.AnthropicBeta{
  	anthropic.AnthropicBetaCompact2026_09_04,
  	anthropic.AnthropicBetaThinkingBindingControls2026_08_01,
  }
  system := []anthropic.BetaTextBlockParam{{Text: "You help plan a recipe app's release. Keep answers short."}}
  // With "error", a thinking block that fails the check makes the request fail with a 400.
  thinking := anthropic.BetaThinkingConfigParamUnion{
  	OfAdaptive: &anthropic.BetaThinkingConfigAdaptiveParam{
  		BlockBinding: anthropic.BetaThinkingBlockBindingParam{
  			PrefixMismatchBehavior: anthropic.BetaThinkingPrefixMismatchBehaviorError,
  		},
  	},
  }

  // 1. Have a short conversation with thinking on.
  history := []anthropic.BetaMessageParam{
  	anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("What are the main entities in the app's data model?")),
  }
  first, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:     model,
  	MaxTokens: 8192,
  	System:    system,
  	Betas:     betas,
  	Thinking:  thinking,
  	Messages:  history,
  })
  if err != nil {
  	log.Fatal(err)
  }
  history = append(history,
  	first.ToParam(),
  	anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?")),
  )
  second, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:     model,
  	MaxTokens: 8192,
  	System:    system,
  	Betas:     betas,
  	Thinking:  thinking,
  	Messages:  history,
  })
  if err != nil {
  	log.Fatal(err)
  }
  history = append(history, second.ToParam())
  thinkingBlocks := 0
  for _, block := range second.Content {
  	if _, ok := block.AsAny().(anthropic.BetaThinkingBlock); ok {
  		thinkingBlocks++
  	}
  }
  fmt.Printf("Thinking blocks in the kept turn: %d\n", thinkingBlocks)

  // 2. Summarize the first turn. The second turn stays out of the request.
  summary, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:     model,
  	MaxTokens: 4096,
  	System:    system,
  	Betas:     betas,
  	Thinking:  thinking,
  	Messages:  history[:2],
  	Compaction: anthropic.BetaCompactionConfigUnionParam{
  		OfSummarize: &anthropic.BetaSummarizeCompactionParam{},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  if summary.StopReason != anthropic.BetaStopReasonCompaction {
  	log.Fatalf("No summary: %s", summary.StopReason)
  }

  // 3. Put the block in front of the kept turn and ask the next question.
  history = slices.Concat(
  	[]anthropic.BetaMessageParam{summary.ToParam()},
  	history[2:],
  	[]anthropic.BetaMessageParam{anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Which day should the release go out?"))},
  )
  third, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:     model,
  	MaxTokens: 8192,
  	System:    system,
  	Betas:     betas,
  	Thinking:  thinking,
  	Messages:  history,
  })
  if err != nil {
  	log.Fatal(err)
  }

  // 4. A 200 with no dropped blocks means the kept thinking held.
  fmt.Printf("Dropped thinking blocks: %d\n", len(third.InputTransformations))
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaCompactionConfig;
  import com.anthropic.models.beta.messages.BetaContentBlock;
  import com.anthropic.models.beta.messages.BetaMessageParam;
  import com.anthropic.models.beta.messages.BetaStopReason;
  import com.anthropic.models.beta.messages.BetaThinkingBlockBinding;
  import com.anthropic.models.beta.messages.BetaThinkingConfigAdaptive;
  import com.anthropic.models.beta.messages.BetaThinkingPrefixMismatchBehavior;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  // Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  static final Model MODEL = Model.CLAUDE_FABLE_5_1;
  static final List<AnthropicBeta> BETAS = List.of(
      AnthropicBeta.COMPACT_2026_09_04,
      AnthropicBeta.THINKING_BINDING_CONTROLS_2026_08_01
  );
  static final String SYSTEM = "You help plan a recipe app's release. Keep answers short.";
  // With "error", a thinking block that fails the check makes the request fail with a 400.
  static final BetaThinkingConfigAdaptive THINKING = BetaThinkingConfigAdaptive.builder()
      .blockBinding(BetaThinkingBlockBinding.builder()
          .prefixMismatchBehavior(BetaThinkingPrefixMismatchBehavior.ERROR)
          .build())
      .build();

  void main() {
      var client = AnthropicOkHttpClient.fromEnv();

      // 1. Have a short conversation with thinking on.
      var history = new ArrayList<BetaMessageParam>();
      history.add(BetaMessageParam.builder()
          .role(BetaMessageParam.Role.USER)
          .content("What are the main entities in the app's data model?")
          .build());
      var firstParams = MessageCreateParams.builder()
          .model(MODEL)
          .maxTokens(8192)
          .system(SYSTEM)
          .betas(BETAS)
          .thinking(THINKING)
          .messages(history)
          .build();
      var first = client.beta().messages().create(firstParams);
      history.add(first.toParam());
      history.add(BetaMessageParam.builder()
          .role(BetaMessageParam.Role.USER)
          .content("Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?")
          .build());
      var secondParams = MessageCreateParams.builder()
          .model(MODEL)
          .maxTokens(8192)
          .system(SYSTEM)
          .betas(BETAS)
          .thinking(THINKING)
          .messages(history)
          .build();
      var second = client.beta().messages().create(secondParams);
      history.add(second.toParam());
      long thinkingBlocks = second.content().stream().filter(BetaContentBlock::isThinking).count();
      IO.println("Thinking blocks in the kept turn: " + thinkingBlocks);

      // 2. Summarize the first turn. The second turn stays out of the request.
      var firstTurn = history.subList(0, 2);
      var summaryParams = MessageCreateParams.builder()
          .model(MODEL)
          .maxTokens(4096)
          .system(SYSTEM)
          .betas(BETAS)
          .thinking(THINKING)
          .messages(firstTurn)
          .compaction(BetaCompactionConfig.builder().build()) // type defaults to "summarize"
          .build();
      var summary = client.beta().messages().create(summaryParams);
      if (!summary.stopReason().map(BetaStopReason.COMPACTION::equals).orElse(false)) {
          throw new IllegalStateException("No summary: " + summary.stopReason().orElseThrow());
      }

      // 3. Put the block in front of the kept turn and ask the next question.
      firstTurn.clear();
      history.addFirst(summary.toParam());
      history.add(BetaMessageParam.builder()
          .role(BetaMessageParam.Role.USER)
          .content("Which day should the release go out?")
          .build());
      var thirdParams = MessageCreateParams.builder()
          .model(MODEL)
          .maxTokens(8192)
          .system(SYSTEM)
          .betas(BETAS)
          .thinking(THINKING)
          .messages(history)
          .build();
      var third = client.beta().messages().create(thirdParams);

      // 4. A 200 with no dropped blocks means the kept thinking held.
      IO.println("Dropped thinking blocks: " + third.inputTransformations().map(List::size).orElse(0));
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaCompactionConfig;
  use Anthropic\Beta\Messages\BetaMessageParam;
  use Anthropic\Beta\Messages\BetaMessageParam\Role;
  use Anthropic\Beta\Messages\BetaStopReason;
  use Anthropic\Beta\Messages\BetaThinkingBlock;
  use Anthropic\Beta\Messages\BetaThinkingBlockBinding;
  use Anthropic\Beta\Messages\BetaThinkingConfigAdaptive;
  use Anthropic\Beta\Messages\BetaThinkingPrefixMismatchBehavior;

  $client = new Client();

  // Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  const MODEL = Model::CLAUDE_FABLE_5_1;
  const BETAS = [AnthropicBeta::COMPACT_2026_09_04, AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01];
  const SYSTEM = "You help plan a recipe app's release. Keep answers short.";
  // With "error", a thinking block that fails the check makes the request fail with a 400.
  $thinking = BetaThinkingConfigAdaptive::with(
      blockBinding: BetaThinkingBlockBinding::with(
          prefixMismatchBehavior: BetaThinkingPrefixMismatchBehavior::ERROR,
      ),
  );

  // 1. Have a short conversation with thinking on.
  $history = [
      BetaMessageParam::with(role: Role::USER, content: "What are the main entities in the app's data model?"),
  ];
  $first = $client->beta->messages->create(
      model: MODEL,
      maxTokens: 8192,
      system: SYSTEM,
      betas: BETAS,
      thinking: $thinking,
      messages: $history,
  );
  $history[] = BetaMessageParam::with(role: Role::ASSISTANT, content: $first->content);
  $history[] = BetaMessageParam::with(
      role: Role::USER,
      content: 'Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?',
  );
  $second = $client->beta->messages->create(
      model: MODEL,
      maxTokens: 8192,
      system: SYSTEM,
      betas: BETAS,
      thinking: $thinking,
      messages: $history,
  );
  $history[] = BetaMessageParam::with(role: Role::ASSISTANT, content: $second->content);
  $thinkingBlocks = count(array_filter($second->content, fn ($block) => $block instanceof BetaThinkingBlock));
  printf("Thinking blocks in the kept turn: %d\n", $thinkingBlocks);

  // 2. Summarize the first turn. The second turn stays out of the request.
  $summary = $client->beta->messages->create(
      model: MODEL,
      maxTokens: 4096,
      system: SYSTEM,
      betas: BETAS,
      thinking: $thinking,
      messages: array_slice($history, 0, 2),
      compaction: new BetaCompactionConfig(), // type defaults to 'summarize'
  );
  if ($summary->stopReason !== BetaStopReason::COMPACTION->value) {
      throw new RuntimeException("No summary: {$summary->stopReason}");
  }

  // 3. Put the block in front of the kept turn and ask the next question.
  $history = [
      BetaMessageParam::with(role: Role::ASSISTANT, content: $summary->content),
      ...array_slice($history, 2),
      BetaMessageParam::with(role: Role::USER, content: 'Which day should the release go out?'),
  ];
  $third = $client->beta->messages->create(
      model: MODEL,
      maxTokens: 8192,
      system: SYSTEM,
      betas: BETAS,
      thinking: $thinking,
      messages: $history,
  );

  // 4. A 200 with no dropped blocks means the kept thinking held.
  printf("Dropped thinking blocks: %d\n", count($third->inputTransformations));
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
  MODEL = Anthropic::Model::CLAUDE_FABLE_5_1
  BETAS = [
    Anthropic::AnthropicBeta::COMPACT_2026_09_04,
    Anthropic::AnthropicBeta::THINKING_BINDING_CONTROLS_2026_08_01
  ]
  SYSTEM = "You help plan a recipe app's release. Keep answers short."
  # With "error", a thinking block that fails the check makes the request fail with a 400.
  THINKING = Anthropic::Beta::BetaThinkingConfigAdaptive.new(
    block_binding: Anthropic::Beta::BetaThinkingBlockBinding.new(
      prefix_mismatch_behavior: Anthropic::Beta::BetaThinkingPrefixMismatchBehavior::ERROR
    )
  )

  # 1. Have a short conversation with thinking on.
  history = [{ role: "user", content: "What are the main entities in the app's data model?" }]
  first = client.beta.messages.create(
    model: MODEL,
    max_tokens: 8192,
    system_: SYSTEM,
    betas: BETAS,
    thinking: THINKING,
    messages: history
  )
  history += [
    { role: "assistant", content: first.content },
    {
      role: "user",
      content: "Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?"
    }
  ]
  second = client.beta.messages.create(
    model: MODEL,
    max_tokens: 8192,
    system_: SYSTEM,
    betas: BETAS,
    thinking: THINKING,
    messages: history
  )
  history << { role: "assistant", content: second.content }
  thinking_blocks = second.content.count { it.is_a?(Anthropic::Beta::BetaThinkingBlock) }
  puts "Thinking blocks in the kept turn: #{thinking_blocks}"

  # 2. Summarize the first turn. The second turn stays out of the request.
  summary = client.beta.messages.create(
    model: MODEL,
    max_tokens: 4096,
    system_: SYSTEM,
    betas: BETAS,
    thinking: THINKING,
    messages: history.first(2),
    compaction: { type: "summarize" }
  )
  abort "No summary: #{summary.stop_reason}" unless summary.stop_reason == :compaction

  # 3. Put the block in front of the kept turn and ask the next question.
  history = [
    { role: "assistant", content: summary.content },
    *history.drop(2),
    { role: "user", content: "Which day should the release go out?" }
  ]
  third = client.beta.messages.create(
    model: MODEL,
    max_tokens: 8192,
    system_: SYSTEM,
    betas: BETAS,
    thinking: THINKING,
    messages: history
  )

  # 4. A 200 with no dropped blocks means the kept thinking held.
  puts "Dropped thinking blocks: #{third.input_transformations.length}"
  ```
</CodeGroup>

```text Output wrap
Thinking blocks in the kept turn: 1
Dropped thinking blocks: 0
```

In production, `"drop_block"` keeps requests succeeding when a condition doesn't hold, and reports each dropped block in `input_transformations` with `reason: "prefix_binding_mismatch"`. An entry whose `path` falls in a kept turn means that turn's thinking didn't hold. [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) describes what is dropped and says how to alert on it.
