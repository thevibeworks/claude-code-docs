---
title: What's new in Claude Fable 5.1
url: https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
description: Overview of new features, breaking changes, and capability improvements in Claude Fable 5.1 and Claude Mythos 5.1.
---

Claude Fable 5.1 extends Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost, and brings stronger long-running agentic coding, multistep research, and document, spreadsheet, and slide work. For most workloads, start with Claude Opus 5 (see [Choosing a model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)). Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. Claude Mythos 5.1 offers the same capabilities to [Project Glasswing](https://anthropic.com/glasswing) participants only.

If you already call Claude Fable 5, three changes are breaking: [forced tool use returns an error](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#forced-tool-use-is-not-supported), [earlier models can't read its thinking blocks](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#thinking-blocks-are-tied-to-the-model-that-produced-them), and [editing earlier turns invalidates thinking blocks](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#editing-earlier-turns-invalidates-thinking-blocks). Five are additive: [per-message effort](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#change-effort-mid-conversation-beta) (beta), [turn-scoped system messages](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#turn-scoped-system-messages-beta) (beta), [readable progress updates between tool calls](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#progress-updates-between-tool-calls-beta) (`display: "updates"`, beta), a [lower cache read price](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#pricing), and [content provenance](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#content-provenance).

## Models

| Model             | Claude API ID     | Description                                                                                | Availability                                                           |
| ----------------- | ----------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Claude Fable 5.1  | claude-fable-5-1  | Successor to Claude Fable 5, for long-running agentic coding, knowledge work, and research | All customers, on the Claude API and partner platforms                 |
| Claude Mythos 5.1 | claude-mythos-5-1 | Same capabilities as Claude Fable 5.1. Successor to Claude Mythos 5.                       | [Project Glasswing](https://anthropic.com/glasswing) participants only |

Claude Fable 5.1 and Claude Mythos 5.1 share specs and pricing:

* **Context window and output:** a [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) (default and maximum) at standard per-token pricing across the whole window, and 128k max output tokens.
* **Thinking:** [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) is always on. Use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.
* **Pricing:** the same as Claude Fable 5, except for a [lower cache read price](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#pricing).
* **Tokenizer:** the same as Claude Fable 5 (introduced with Claude Opus 4.7). Compared with models older than Claude Opus 4.7, the same text produces roughly 30% more tokens. See [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting).

For all current models, see the [models overview](https://platform.claude.com/docs/en/models/overview).

## Breaking changes

### Forced tool use is not supported

Claude Fable 5.1 and Claude Mythos 5.1 don't support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

```text wrap
tool_choice: type "tool" and "any" are not supported for this model.
```

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are unchanged. The same validation applies to the [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint.

Thinking is always on for these models, and a forced tool call would skip it. The model would write its working-out into the tool arguments instead, which lowers argument quality. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use), or move the schema to [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs). To make the model call a tool rather than reply in text, state in the prompt when the tool applies (for example, "Use the `get_weather` tool to answer"). Claude Fable 5.1 follows explicit tool instructions reliably.

### Earlier models can't read Claude Fable 5.1 thinking blocks

Every thinking block records which model produced it, and it's preserved in one direction only: Claude Fable 5.1 reads earlier models' thinking blocks, and no earlier model reads Claude Fable 5.1's. A conversation that moves onto Claude Fable 5.1 (from Claude Opus 5, Claude Fable 5, or any earlier Claude model) keeps its reasoning. A conversation that moves from Claude Fable 5.1 to any of those models loses it for the turns that run there.

When a request carries a block the target model can't read (a router or fallback that switches models mid-conversation, for example), the API drops the block before the model sees it. Dropped blocks don't count toward `input_tokens` and aren't billed. With the `thinking-binding-controls-2026-08-01` beta header, the drop is reported in a top-level `input_transformations` array. Without it, the drop is silent. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-for-model).

### Editing earlier turns invalidates thinking blocks

Modifying anything before a Claude Fable 5.1 thinking block (the `system` prompt, the `tools`, or an earlier message) results in an error on the next request, or in the block being dropped if you opt into that. Claude Mythos 5.1 doesn't run this check. Claude Code, claude.ai, [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), and the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) keep that prefix intact for you. If your code builds the `messages` array itself, check it before you migrate: [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) walks through the check and each fix. The check is enforced for new accounts created on or after August 31, 2026. For accounts created earlier, the API records the mismatch but acts on it only when the request sets `thinking.block_binding.prefix_mismatch_behavior`.

These patterns invalidate every later thinking block:

* Editing, reordering, or removing an earlier turn while keeping later ones.
* Injecting per-request text into an earlier turn (a reminder or status line) that you remove on the next request.
* Rebuilding the top-level `system` prompt or `tools` array between requests in the same conversation.
* An image or document URL that serves different bytes on a later request (the check covers the bytes, not the URL, so a rotating signed URL for the same file is fine).

These keep later blocks valid: removing a leading run of thinking blocks (oldest first), letting server-side compaction or context editing trim the history, moving `cache_control` markers, and changing `effort` between requests. Removing a thinking block from anywhere other than the start of the run invalidates every thinking block after it.

Where the check is enforced, a request that replays an invalidated block is rejected with a 400 whose message says `The block is bound to a different conversation`. To drop the block and continue instead, send the `thinking-binding-controls-2026-08-01` beta header with `thinking.block_binding.prefix_mismatch_behavior: "drop_block"`. The drop is reported in `input_transformations` with `reason: "prefix_binding_mismatch"`.

To keep thinking valid across a long session, treat the conversation as append-only. Add instructions with a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) ([turn-scoped](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#turn-scoped-system-messages-beta) if it should apply to one turn only) and change tools with [mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) rather than editing `system` or `tools`. Trim context with server-side [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) or [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction), which don't count as edits. These patterns also keep the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) warm. To find out whether your integration edits history, run a session with `prefix_mismatch_behavior: "drop_block"` and log `input_transformations`: the [migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide#fable-5-1-preserved-thinking) has the three-step check. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation) for the full rules.

## New features

### Change effort mid-conversation (beta)

On Claude Fable 5.1 you can change the [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level mid-conversation without invalidating the prompt cache. Raise it for a hard step and lower it for routine ones. Per-message effort is in beta: include the `mid-conversation-output-config-2026-07-01` beta header. Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5 support it on the Claude API.

<CodeGroup>
  ```bash cURL
  # Effort-only system message: the new level takes effect from the next user turn.
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mid-conversation-output-config-2026-07-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-fable-5-1",
      "max_tokens": 4096,
      "output_config": {"effort": "high"},
      "messages": [
        {"role": "user", "content": "Plan a migration from SQLite to PostgreSQL in three short steps."},
        {"role": "assistant", "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts."},
        {"role": "system", "content": [], "output_config": {"effort": "low"}},
        {"role": "user", "content": "Summarize the plan in one sentence."}
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta mid-conversation-output-config-2026-07-01 \
    --transform 'content.#(type=="text").text' --raw-output <<'YAML'
  model: claude-fable-5-1
  max_tokens: 4096
  output_config:
    effort: high
  messages:
    - role: user
      content: Plan a migration from SQLite to PostgreSQL in three short steps.
    - role: assistant
      content: "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts."
    # Effort-only system message: the new level takes effect from the next user turn.
    - role: system
      content: []
      output_config:
        effort: low
    - role: user
      content: Summarize the plan in one sentence.
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-fable-5-1",
      max_tokens=4096,
      output_config={"effort": "high"},
      messages=[
          {
              "role": "user",
              "content": "Plan a migration from SQLite to PostgreSQL in three short steps.",
          },
          {
              "role": "assistant",
              "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.",
          },
          # Effort-only system message: the new level takes effect from the next user turn.
          {"role": "system", "content": [], "output_config": {"effort": "low"}},
          {"role": "user", "content": "Summarize the plan in one sentence."},
      ],
      betas=["mid-conversation-output-config-2026-07-01"],
  )

  for block in response.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: "claude-fable-5-1",
    max_tokens: 4096,
    output_config: { effort: "high" },
    messages: [
      {
        role: "user",
        content: "Plan a migration from SQLite to PostgreSQL in three short steps."
      },
      {
        role: "assistant",
        content:
          "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts."
      },
      // Effort-only system message: the new level takes effect from the next user turn.
      { role: "system", content: [], output_config: { effort: "low" } },
      { role: "user", content: "Summarize the plan in one sentence." }
    ],
    betas: ["mid-conversation-output-config-2026-07-01"]
  });

  for (const block of response.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;

  AnthropicClient client = new();

  var response = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = "claude-fable-5-1",
      MaxTokens = 4096,
      OutputConfig = new() { Effort = Effort.High },
      Messages =
      [
          new() { Role = Role.User, Content = "Plan a migration from SQLite to PostgreSQL in three short steps." },
          new() { Role = Role.Assistant, Content = "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts." },
          // Effort-only system message: the new level takes effect from the next user turn.
          new()
          {
              Role = Role.System,
              Content = new([]),
              OutputConfig = new() { Effort = BetaSystemMessageOutputConfigEffort.Low },
          },
          new() { Role = Role.User, Content = "Summarize the plan in one sentence." },
      ],
      Betas = [AnthropicBeta.MidConversationOutputConfig2026_07_01],
  });

  foreach (var block in response.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Beta.Messages.New(context.Background(), anthropic.BetaMessageNewParams{
  	Model:     "claude-fable-5-1",
  	MaxTokens: 4096,
  	OutputConfig: anthropic.BetaOutputConfigParam{
  		Effort: anthropic.BetaOutputConfigEffortHigh,
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Plan a migration from SQLite to PostgreSQL in three short steps.")),
  		{
  			Role:    anthropic.BetaMessageParamRoleAssistant,
  			Content: []anthropic.BetaContentBlockParamUnion{anthropic.NewBetaTextBlock("1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.")},
  		},
  		// Effort-only system message: the new level takes effect from the next user turn.
  		anthropic.NewBetaSystemMessage(anthropic.BetaSystemMessageOutputConfigParam{
  			Effort: anthropic.BetaSystemMessageOutputConfigEffortLow,
  		}),
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Summarize the plan in one sentence.")),
  	},
  	Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaMidConversationOutputConfig2026_07_01},
  })
  if err != nil {
  	log.Fatal(err)
  }

  for _, block := range response.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaMessageParam;
  import com.anthropic.models.beta.messages.BetaOutputConfig;
  import com.anthropic.models.beta.messages.BetaSystemMessageOutputConfig;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model("claude-fable-5-1")
          .maxTokens(4096L)
          .addBeta(AnthropicBeta.MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01)
          .outputConfig(BetaOutputConfig.builder()
              .effort(BetaOutputConfig.Effort.HIGH)
              .build())
          .addUserMessage("Plan a migration from SQLite to PostgreSQL in three short steps.")
          .addAssistantMessage("1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.")
          // Effort-only system message: the new level takes effect from the next user turn.
          .addMessage(BetaMessageParam.builder()
              .role(BetaMessageParam.Role.SYSTEM)
              .contentOfBetaContentBlockParams(List.of())
              .outputConfig(BetaSystemMessageOutputConfig.builder()
                  .effort(BetaSystemMessageOutputConfig.Effort.LOW)
                  .build())
              .build())
          .addUserMessage("Summarize the plan in one sentence.")
          .build();

      BetaMessage response = client.beta().messages().create(params);
      response.content().stream()
          .flatMap(block -> block.text().stream())
          .forEach(textBlock -> IO.println(textBlock.text()));
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaMessageParam;
  use Anthropic\Beta\Messages\BetaOutputConfig;
  use Anthropic\Beta\Messages\BetaSystemMessageOutputConfig;
  use Anthropic\Client;

  $client = new Client();

  $response = $client->beta->messages->create(
      model: 'claude-fable-5-1',
      maxTokens: 4096,
      outputConfig: BetaOutputConfig::with(effort: 'high'),
      messages: [
          BetaMessageParam::with(role: 'user', content: 'Plan a migration from SQLite to PostgreSQL in three short steps.'),
          BetaMessageParam::with(role: 'assistant', content: '1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.'),
          // Effort-only system message: the new level takes effect from the next user turn.
          BetaMessageParam::with(
              role: 'system',
              content: [],
              outputConfig: BetaSystemMessageOutputConfig::with(effort: 'low'),
          ),
          BetaMessageParam::with(role: 'user', content: 'Summarize the plan in one sentence.'),
      ],
      betas: [AnthropicBeta::MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01],
  );

  foreach ($response->content as $block) {
      if ($block->type === 'text') {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.beta.messages.create(
    model: "claude-fable-5-1",
    max_tokens: 4096,
    output_config: {effort: :high},
    messages: [
      {role: "user", content: "Plan a migration from SQLite to PostgreSQL in three short steps."},
      {role: "assistant", content: "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts."},
      # Effort-only system message: the new level takes effect from the next user turn.
      {role: "system", content: [], output_config: {effort: :low}},
      {role: "user", content: "Summarize the plan in one sentence."}
    ],
    betas: [Anthropic::AnthropicBeta::MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01]
  )

  response.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

See [Per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) for details.

### Turn-scoped system messages (beta)

A [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) can be scoped to one turn. Set `clear_at: "next_user_message"` on a `role: "system"` message and its text carries system-prompt authority for the current turn, then stops rendering once a later `user` message exists. The message stays in `messages` and you keep sending it back verbatim, so nothing earlier in the conversation changes. The [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) keeps matching, later [thinking blocks stay valid](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation), and a cleared message costs no input tokens. Use it for per-turn reminders in a tool loop ("check your inbox before running more code", "the user can't see that tool output") instead of injecting text into the history and deleting it on the next request. Turn-scoped system messages are in beta: include the `mid-conversation-system-clear-at-2026-08-21` beta header. See [Turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages).

```json
{
  "role": "system",
  "clear_at": "next_user_message",
  "content": "Results have landed in your inbox. Check it before running more code."
}
```

### Progress updates between tool calls (beta)

Like Claude Fable 5, Claude Fable 5.1 writes short progress updates between tool calls on what it found and what it will do next, though fewer of them (see [Changed from Claude Fable 5](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#changed-from-claude-fable-5)). Each update arrives as its own `thinking` block immediately before the tool call. Under the default `thinking.display` of `"omitted"` those blocks come back empty, like reasoning, so a long agentic turn can look silent to your users. What's new is the `display: "updates"` option: set it with the `thinking-display-updates-2026-08-18` beta header to receive the progress updates as text while reasoning stays hidden. Any `thinking` block with non-empty text is then a status line you can show the user. `"summarized"` returns them too, mixed with summarized reasoning. See [Progress updates between tool calls](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates).

### Content provenance

Text generated by Claude Fable 5.1 and Claude Mythos 5.1 carries Anthropic's statistical text watermark on every platform where the model is available. Supported image, video, and audio files Claude produces (through the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), for example) carry signed [C2PA](https://c2pa.org/) Content Credentials when you retrieve them through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) on the Claude API.

The watermark doesn't change the meaning, quality, or readability of the output. It adds no tokens or hidden characters, carries no information about you or your organization, and needs no changes to your requests or responses. For background, see [How Claude marks AI-generated content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) and [How Claude's text watermark works](https://www.anthropic.com/news/claude-text-watermark).

## Behavior differences

### Changed from Claude Fable 5

Claude Fable 5.1 differs from Claude Fable 5 in several ways that show up without any code change. Each has a prompting fix in [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1):

* **Parallel tool calling is more variable.** Claude Fable 5.1 may issue one tool call per turn where Claude Fable 5 batched several. This shows up in long agent loops where the next independent reads are only implied: custom coding agents, bash-and-editor harnesses, computer use. The extra turns cost tokens, round trips, and wall-clock time but don't reduce answer quality. Requests naming several things to fetch still run in parallel. Add the one-line batching instruction from [Batch independent tool calls in agent loops](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#batch-independent-tool-calls-in-agent-loops).
* **Fewer progress updates during long tool runs.** The model writes less user-facing text between tool calls, especially at higher effort. Set `thinking.display` to `"updates"` (beta) to receive the [progress updates](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates) it does write, and remove any prompt line that tells it to hold findings for the final response. If your UI depends on narration, ask explicitly for an opening line, periodic updates, and a closing recap. See [Ask for user-facing progress updates](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#ask-for-user-facing-progress-updates).
* **Answers from memory more often at `low` effort.** At the lowest effort level the model calls a search or retrieval tool less often. Raise effort for turns that need fresh information, including [mid-conversation](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#change-effort-mid-conversation-beta), or add the verification nudge from [Search triggering at low effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#search-triggering-at-low-effort).
* **Denser prose in places.** In some cases its prose is denser than Claude Fable 5's, with longer sentences and fewer paragraph breaks. See [Writing density](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#writing-density).
* **Less formatting in chat.** The model uses bold, headers, and lists less than earlier Claude models, so anti-formatting rules written for those models can suppress structure the content needs. See [Formatting in chat](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat).
* **Unmarked quotations in summaries.** When summarizing documents, the model is more likely to reproduce passages of the source without marking them as quotations. See [Quoting retrieved sources](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#quoting-retrieved-sources).
* **Whole-file rewrites for small changes.** When editing text files, the model is more likely to rewrite the entire file than make a targeted edit. The result is usually the same, but the rewrite costs more output tokens and time. See [Prefer targeted edits over whole-file rewrites](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#prefer-targeted-edits-over-whole-file-rewrites).

### Unchanged from Claude Fable 5

These Messages API behaviors carry over from Claude Fable 5 unchanged:

* Adaptive thinking is always on. `thinking: {"type": "enabled"}` with `budget_tokens` and `thinking: {"type": "disabled"}` both return a 400 error. Omit `thinking` or send `{"type": "adaptive"}`.
* `thinking.display` defaults to `"omitted"`. `"summarized"` is available, and the raw chain of thought is never returned.
* Reasoning between tool calls appears in thinking blocks rather than text, and [interleaved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#interleaved-thinking) is automatic with no beta header.
* Prefilling the assistant response returns a 400 error.
* Non-default `temperature`, `top_p`, or `top_k` values return a 400 error.
* The minimum cacheable prompt length is 512 tokens.
* [Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) and tool changes are supported.

## Capability improvements

Claude Fable 5.1 improves on Claude Fable 5, and the gap is widest at higher [effort](https://platform.claude.com/docs/en/build-with-claude/effort) levels. The gains concentrate in six areas:

* **Agentic coding over long sessions**, including multi-file features, large refactors and migrations, debugging, and code review across sessions that run for hours.
* **Knowledge work with documents, spreadsheets, and slides**, taking an analysis from a first question to a finished document, live-formula spreadsheet, or slide deck built from a blank page.
* **Research and search**, with higher accuracy on multistep web research and deep-research tasks that follow up on what they find.
* **Vision**, reading dense charts, filings, and tables nested in PDFs, including with crop-and-zoom tools on charts.
* **Long-context work**, reasoning over and connecting details across the full [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows).
* **Computer use**, operating a browser and desktop applications more reliably and recovering from failed steps.

Multilingual performance is on par with Claude Fable 5.

## Refusals, fallback, and billing

Claude Fable 5.1 includes safety classifiers covering the same `stop_details` categories as Claude Fable 5, and everything in [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) applies. It can return `stop_reason: "refusal"`, so handle refusals and configure fallback.

* **Refusals:** a declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) object naming the policy area that fired.
* **Fallback:** retry a refused request on another model with [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback), the [SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback), or your own retry. `fallbacks: "default"` (beta) retries a declined request on the model Anthropic recommends for that category. The permitted fallback targets for Claude Fable 5.1 are Claude Opus 4.8 and Claude Opus 5.
* **Billing:** you aren't billed for a refusal that arrives before any output, and, for Claude Fable 5.1, [fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) refunds the prompt-cache cost of switching models.

## Pricing

Claude Fable 5.1 and Claude Mythos 5.1 are priced the same as Claude Fable 5, except for cache reads (prices in USD):

| Base input | 5m cache writes | 1h cache writes | Cache reads  | Output     |
| ---------- | --------------- | --------------- | ------------ | ---------- |
| $10 / MTok | $12.50 / MTok   | $20 / MTok      | $0.25 / MTok | $50 / MTok |

Cache reads (hits and refreshes) cost 0.025 times the base input price on these models, compared with 0.1 on other Claude models. Long agentic sessions that re-read a cached prefix pay a quarter of the Claude Fable 5 rate. Cache writes and the [512-token minimum cacheable prompt length](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations) are unchanged.

[Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) is $5 USD per million input tokens and $25 USD per million output tokens. See [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) for data residency and tool pricing.

## Availability

Claude Fable 5.1 is available on:

* **Claude API:** all customers, as `claude-fable-5-1`.
* **AWS:** [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), as `anthropic.claude-fable-5-1`, and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), as `claude-fable-5-1`.
* **Google Cloud:** [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), as `claude-fable-5-1`.
* **Microsoft Foundry:** [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), on Anthropic infrastructure.

Claude Mythos 5.1 is offered only to approved customers in [Project Glasswing](https://anthropic.com/glasswing). For access, contact your Anthropic, AWS, or Google Cloud account team.

Claude Fable 5.1 and Claude Mythos 5.1 carry 30-day data retention and aren't available under zero data retention unless expressly authorized by Anthropic. Both are [Covered Models](https://support.claude.com/en/articles/15425695), like Claude Fable 5 and Claude Mythos 5. See [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).

## Migrate from Claude Fable 5

To migrate from Claude Fable 5, update your model ID:

<CodeGroup exclude="shell">
  ```python Python
  model = "claude-fable-5"  # Before
  model = "claude-fable-5-1"  # After
  ```

  ```typescript TypeScript
  let model = "claude-fable-5"; // Before
  model = "claude-fable-5-1"; // After
  ```

  ```csharp C#
  var model = "claude-fable-5"; // Before
  model = "claude-fable-5-1"; // After
  ```

  ```go Go
  model := "claude-fable-5"  // Before
  model = "claude-fable-5-1" // After
  ```

  ```java Java
  String model = "claude-fable-5"; // Before
  model = "claude-fable-5-1"; // After
  ```

  ```php PHP
  $model = 'claude-fable-5'; // Before
  $model = 'claude-fable-5-1'; // After
  ```

  ```ruby Ruby
  model = "claude-fable-5" # Before
  model = "claude-fable-5-1" # After
  ```
</CodeGroup>

Then review these items:

1. Remove any `tool_choice` of type `any` or `tool`. Move schema enforcement to [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) with `tool_choice: {"type": "auto"}` or to [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs).
2. Pass thinking blocks back unchanged and keep the history append-only. If your code builds the `messages` array itself, run the [history-editing check](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide#fable-5-1-preserved-thinking): move per-turn reminders you currently inject and delete to [turn-scoped system messages](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#turn-scoped-system-messages-beta), move `system` and `tools` changes to mid-conversation system messages, trim context server-side or strip thinking blocks from turns you carry across a client-side summary, then pick a production [`prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-thinking-controls) and monitor `input_transformations`.
3. Re-tune effort from the default (`high`), and consider [changing it mid-conversation](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#change-effort-mid-conversation-beta) instead of holding one level for the whole session.
4. In agent loops, watch for one tool call per turn where Claude Fable 5 batched several, and add the per-turn note from [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1).
5. Re-run your evals. Refusal handling, fallback, fallback credit, and token counts carry over unchanged. Cache reads cost less (see [Pricing](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#pricing)), and default behavior differs in the ways listed under [Changed from Claude Fable 5](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#changed-from-claude-fable-5).

See the [migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) for step-by-step instructions, including from Claude Opus 5 and earlier models.

## Next steps

<CardGroup cols={3}>
  <Card title="Models overview" icon="arrow-right" href="https://platform.claude.com/docs/en/models/overview">
    Specs and pricing for every current Claude model.
  </Card>

  <Card title="Migration guide" icon="code" href="https://platform.claude.com/docs/en/models/fable-5-1/migration-guide">
    Migrating from Claude Fable 5, Claude Opus 5, and earlier models.
  </Card>

  <Card title="Prompting Claude Fable 5.1" icon="terminal" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1">
    Prompting patterns specific to Claude Fable 5.1.
  </Card>
</CardGroup>
