---
title: Compaction that keeps recent turns
url: https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns
description: Summarize the older turns of a conversation with on-demand compaction and send the most recent turns after the summary, word for word.
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

Keep-tail compaction keeps the last few turns of a conversation word for word after the summary. It changes two things in the [compaction loop](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop): which messages go into the compaction request, and what you send after the block. Everything in [Continue from the summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) applies unchanged.

## Choose which turns to keep

No parameter sets which turns are kept. You pick a cut point in your history: the messages before it go into the compaction request, and the messages from it on are kept.

Kept turns go back to Claude at full length, so the more you keep, the less room the compaction frees.

Put the cut where no tool call is left open, with each tool call and its result on the same side. If the messages you send end in an `assistant` turn whose tool call has no result yet, the API rejects the compaction request.

## Compact the older turns and send the rest after the block

To keep a tail of recent turns word for word, leave those turns out of the compaction request. The API summarizes every message it is sent, so send only the older turns, then put the block in front of the turns you kept.

Send the kept turns exactly as they are in your history, thinking blocks included. Both requests carry the beta header, as in [Request a summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary).

In the following example, the history holds two turns, and the cut keeps the second. The compaction request carries the first turn:

```json
{
  "model": "claude-opus-5-5",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "I am building a recipe app. Help me name the main entities in the data model."
    },
    {
      "role": "assistant",
      "content": "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe."
    }
  ],
  "compaction": { "type": "summarize" }
}
```

The next request sends the returned block first, then the kept turn exactly as it was, then the new `user` message. [Continue from the summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) shows a request that starts with a block.

The following program is the loop from [Compact in a loop](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop), changed to keep the last two turns. The highlighted lines show where it differs from the loop.

<CodeGroup exclude="shell">
  ```python Python
  from anthropic.types.beta import BetaMessageParam

  client = anthropic.Anthropic()

  # Set this near your real input budget. It is low here so a short conversation compacts.
  COMPACT_AT_TOKENS = 2500
  SYSTEM = "You help design a recipe app's data model. Keep answers short."
  KEEP_TURNS = 2

  QUESTIONS = [
      "What are the main entities in the data model?",
      "Which fields should Recipe have?",
      "Which fields should Ingredient have?",
      "Which fields should RecipeIngredient have?",
      "Which fields should Step have?",
      "Which indexes should these tables have?",
      "Which fields should be required?",
      "Which fields should have default values?",
  ]

  history: list[BetaMessageParam] = []
  for turn, question in enumerate(QUESTIONS, start=1):
      history.append({"role": "user", "content": question})
      response = client.beta.messages.create(
          model="claude-opus-5-5",
          max_tokens=8192,
          system=SYSTEM,
          betas=["compact-2026-09-04"],
          messages=history,
      )
      history.append({"role": "assistant", "content": response.content})

      # The next request sends this reply too, so count it.
      conversation_tokens = response.usage.input_tokens + response.usage.output_tokens
      if conversation_tokens > COMPACT_AT_TOKENS and KEEP_TURNS < turn < len(QUESTIONS):
          # A turn is one user message and one assistant reply,
          # so the kept turns start with a user message.
          split = -2 * KEEP_TURNS
          older, recent = history[:split], history[split:]
          summary = client.beta.messages.create(
              model="claude-opus-5-5",
              max_tokens=4096,
              system=SYSTEM,
              betas=["compact-2026-09-04"],
              messages=older,
              compaction={"type": "summarize"},
          )
          if summary.stop_reason == "compaction":
              history = [{"role": "assistant", "content": summary.content}, *recent]
              print(f"Kept {len(recent) // 2} turns after the block")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // Set this near your real input budget. It is low here so a short conversation compacts.
  const compactAtTokens = 2500;
  const systemPrompt = "You help design a recipe app's data model. Keep answers short.";
  const keepTurns = 2;

  const questions = [
    "What are the main entities in the data model?",
    "Which fields should Recipe have?",
    "Which fields should Ingredient have?",
    "Which fields should RecipeIngredient have?",
    "Which fields should Step have?",
    "Which indexes should these tables have?",
    "Which fields should be required?",
    "Which fields should have default values?"
  ];

  let history: Anthropic.Beta.Messages.BetaMessageParam[] = [];
  for (const [index, question] of questions.entries()) {
    const turn = index + 1;
    history.push({ role: "user", content: question });
    const response = await client.beta.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 8192,
      system: systemPrompt,
      betas: ["compact-2026-09-04"],
      messages: history
    });
    history.push({ role: "assistant", content: response.content });

    // The next request sends this reply too, so count it.
    const conversationTokens = response.usage.input_tokens + response.usage.output_tokens;
    if (conversationTokens > compactAtTokens && turn > keepTurns && turn < questions.length) {
      // A turn is one user message and one assistant reply, so the kept turns start with a user message.
      const older = history.slice(0, -2 * keepTurns);
      const recent = history.slice(-2 * keepTurns);
      const summary = await client.beta.messages.create({
        model: "claude-opus-5-5",
        max_tokens: 4096,
        system: systemPrompt,
        betas: ["compact-2026-09-04"],
        messages: older,
        compaction: { type: "summarize" }
      });
      if (summary.stop_reason === "compaction") {
        history = [{ role: "assistant", content: summary.content }, ...recent];
        console.log(`Kept ${recent.length / 2} turns after the block`);
      }
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  // Set this near your real input budget. It is low here so a short conversation compacts.
  const int CompactAtTokens = 2500;
  const string SystemPrompt = "You help design a recipe app's data model. Keep answers short.";
  const int KeepTurns = 2;

  string[] questions =
  [
      "What are the main entities in the data model?",
      "Which fields should Recipe have?",
      "Which fields should Ingredient have?",
      "Which fields should RecipeIngredient have?",
      "Which fields should Step have?",
      "Which indexes should these tables have?",
      "Which fields should be required?",
      "Which fields should have default values?",
  ];

  List<BetaMessageParam> history = [];
  foreach (var (index, question) in questions.Index())
  {
      var turn = index + 1;
      history.Add(new() { Role = Role.User, Content = question });
      var response = await client.Beta.Messages.Create(new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 8192,
          System = SystemPrompt,
          Betas = [AnthropicBeta.Compact2026_09_04],
          Messages = history,
      });
      history.Add(new()
      {
          Role = Role.Assistant,
          Content = response.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
      });

      // The next request sends this reply too, so count it.
      var conversationTokens = response.Usage.InputTokens + response.Usage.OutputTokens;
      if (conversationTokens > CompactAtTokens && turn > KeepTurns && turn < questions.Length)
      {
          // A turn is one user message and one assistant reply, so the kept turns start with a user message.
          var older = history[..^(2 * KeepTurns)];
          var recent = history[^(2 * KeepTurns)..];
          var summary = await client.Beta.Messages.Create(new MessageCreateParams
          {
              Model = Model.ClaudeOpus5_5,
              MaxTokens = 4096,
              System = SystemPrompt,
              Betas = [AnthropicBeta.Compact2026_09_04],
              Messages = older,
              Compaction = new BetaCompactionConfig(), // type defaults to "summarize"
          });
          if (summary.StopReason == BetaStopReason.Compaction)
          {
              history =
              [
                  new()
                  {
                      Role = Role.Assistant,
                      Content = summary.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
                  },
                  .. recent,
              ];
              Console.WriteLine($"Kept {recent.Count / 2} turns after the block");
          }
      }
  }
  ```

  ```go Go
  ctx := context.Background()
  client := anthropic.NewClient()

  // Set this near your real input budget. It is low here so a short conversation compacts.
  const compactAtTokens = 2500
  system := []anthropic.BetaTextBlockParam{{Text: "You help design a recipe app's data model. Keep answers short."}}
  const keepTurns = 2

  questions := []string{
  	"What are the main entities in the data model?",
  	"Which fields should Recipe have?",
  	"Which fields should Ingredient have?",
  	"Which fields should RecipeIngredient have?",
  	"Which fields should Step have?",
  	"Which indexes should these tables have?",
  	"Which fields should be required?",
  	"Which fields should have default values?",
  }

  var history []anthropic.BetaMessageParam
  for i, question := range questions {
  	turn := i + 1
  	history = append(history, anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock(question)))
  	response, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  		Model:     anthropic.ModelClaudeOpus5_5,
  		MaxTokens: 8192,
  		System:    system,
  		Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaCompact2026_09_04},
  		Messages:  history,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  	history = append(history, response.ToParam())

  	// The next request sends this reply too, so count it.
  	conversationTokens := response.Usage.InputTokens + response.Usage.OutputTokens
  	if conversationTokens > compactAtTokens && turn > keepTurns && turn < len(questions) {
  		// A turn is one user message and one assistant reply, so the kept turns start with a user message.
  		split := len(history) - 2*keepTurns
  		older, recent := history[:split], history[split:]
  		summary, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  			Model:     anthropic.ModelClaudeOpus5_5,
  			MaxTokens: 4096,
  			System:    system,
  			Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaCompact2026_09_04},
  			Messages:  older,
  			Compaction: anthropic.BetaCompactionConfigUnionParam{
  				OfSummarize: &anthropic.BetaSummarizeCompactionParam{},
  			},
  		})
  		if err != nil {
  			log.Fatal(err)
  		}
  		if summary.StopReason == anthropic.BetaStopReasonCompaction {
  			history = slices.Replace(history, 0, split, summary.ToParam())
  			fmt.Printf("Kept %d turns after the block\n", len(recent)/2)
  		}
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaCompactionConfig;
  import com.anthropic.models.beta.messages.BetaMessageParam;
  import com.anthropic.models.beta.messages.BetaStopReason;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  // Set this near your real input budget. It is low here so a short conversation compacts.
  static final long COMPACT_AT_TOKENS = 2500;
  static final String SYSTEM = "You help design a recipe app's data model. Keep answers short.";
  static final int KEEP_TURNS = 2;

  void main() {
      var client = AnthropicOkHttpClient.fromEnv();

      var questions = List.of(
          "What are the main entities in the data model?",
          "Which fields should Recipe have?",
          "Which fields should Ingredient have?",
          "Which fields should RecipeIngredient have?",
          "Which fields should Step have?",
          "Which indexes should these tables have?",
          "Which fields should be required?",
          "Which fields should have default values?"
      );

      var history = new ArrayList<BetaMessageParam>();
      for (int turn = 1; turn <= questions.size(); turn++) {
          history.add(BetaMessageParam.builder()
              .role(BetaMessageParam.Role.USER)
              .content(questions.get(turn - 1))
              .build());
          var params = MessageCreateParams.builder()
              .model(Model.CLAUDE_OPUS_5_5)
              .maxTokens(8192)
              .system(SYSTEM)
              .addBeta(AnthropicBeta.COMPACT_2026_09_04)
              .messages(history)
              .build();
          var response = client.beta().messages().create(params);
          history.add(response.toParam());

          // The next request sends this reply too, so count it.
          long conversationTokens = response.usage().inputTokens() + response.usage().outputTokens();
          if (conversationTokens > COMPACT_AT_TOKENS && turn > KEEP_TURNS && turn < questions.size()) {
              // A turn is one user message and one assistant reply, so the kept turns start with a user message.
              var older = history.subList(0, history.size() - 2 * KEEP_TURNS);
              var summaryParams = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_5_5)
                  .maxTokens(4096)
                  .system(SYSTEM)
                  .addBeta(AnthropicBeta.COMPACT_2026_09_04)
                  .messages(older)
                  .compaction(BetaCompactionConfig.builder().build()) // type defaults to "summarize"
                  .build();
              var summary = client.beta().messages().create(summaryParams);
              if (summary.stopReason().map(BetaStopReason.COMPACTION::equals).orElse(false)) {
                  older.clear();
                  history.addFirst(summary.toParam());
                  IO.println("Kept " + (history.size() - 1) / 2 + " turns after the block");
              }
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaCompactionConfig;
  use Anthropic\Beta\Messages\BetaMessageParam;
  use Anthropic\Beta\Messages\BetaMessageParam\Role;
  use Anthropic\Beta\Messages\BetaStopReason;

  $client = new Client();

  // Set this near your real input budget. It is low here so a short conversation compacts.
  const COMPACT_AT_TOKENS = 2500;
  const SYSTEM = "You help design a recipe app's data model. Keep answers short.";
  const KEEP_TURNS = 2;

  $questions = [
      'What are the main entities in the data model?',
      'Which fields should Recipe have?',
      'Which fields should Ingredient have?',
      'Which fields should RecipeIngredient have?',
      'Which fields should Step have?',
      'Which indexes should these tables have?',
      'Which fields should be required?',
      'Which fields should have default values?',
  ];

  $history = [];
  foreach ($questions as $index => $question) {
      $turn = $index + 1;
      $history[] = BetaMessageParam::with(role: Role::USER, content: $question);
      $response = $client->beta->messages->create(
          model: Model::CLAUDE_OPUS_5_5,
          maxTokens: 8192,
          system: SYSTEM,
          betas: [AnthropicBeta::COMPACT_2026_09_04],
          messages: $history,
      );
      $history[] = BetaMessageParam::with(role: Role::ASSISTANT, content: $response->content);

      // The next request sends this reply too, so count it.
      $conversationTokens = $response->usage->inputTokens + $response->usage->outputTokens;
      if ($conversationTokens > COMPACT_AT_TOKENS && $turn > KEEP_TURNS && $turn < count($questions)) {
          // A turn is one user message and one assistant reply, so the kept turns start with a user message.
          $older = array_slice($history, 0, -2 * KEEP_TURNS);
          $recent = array_slice($history, -2 * KEEP_TURNS);
          $summary = $client->beta->messages->create(
              model: Model::CLAUDE_OPUS_5_5,
              maxTokens: 4096,
              system: SYSTEM,
              betas: [AnthropicBeta::COMPACT_2026_09_04],
              messages: $older,
              compaction: new BetaCompactionConfig(), // type defaults to 'summarize'
          );
          if ($summary->stopReason === BetaStopReason::COMPACTION->value) {
              $history = [BetaMessageParam::with(role: Role::ASSISTANT, content: $summary->content), ...$recent];
              printf("Kept %d turns after the block\n", intdiv(count($recent), 2));
          }
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Set this near your real input budget. It is low here so a short conversation compacts.
  COMPACT_AT_TOKENS = 2500
  SYSTEM = "You help design a recipe app's data model. Keep answers short."
  KEEP_TURNS = 2

  questions = [
    "What are the main entities in the data model?",
    "Which fields should Recipe have?",
    "Which fields should Ingredient have?",
    "Which fields should RecipeIngredient have?",
    "Which fields should Step have?",
    "Which indexes should these tables have?",
    "Which fields should be required?",
    "Which fields should have default values?"
  ]

  history = []
  questions.each.with_index(1) do |question, turn|
    history << { role: "user", content: question }
    response = client.beta.messages.create(
      model: Anthropic::Model::CLAUDE_OPUS_5_5,
      max_tokens: 8192,
      system_: SYSTEM,
      betas: [Anthropic::AnthropicBeta::COMPACT_2026_09_04],
      messages: history
    )
    history << { role: "assistant", content: response.content }

    # The next request sends this reply too, so count it.
    conversation_tokens = response.usage.input_tokens + response.usage.output_tokens
    if conversation_tokens > COMPACT_AT_TOKENS && turn > KEEP_TURNS && turn < questions.length
      # A turn is one user message and one assistant reply, so the kept turns start with a user message.
      older, recent = history[...-2 * KEEP_TURNS], history.last(2 * KEEP_TURNS)
      summary = client.beta.messages.create(
        model: Anthropic::Model::CLAUDE_OPUS_5_5,
        max_tokens: 4096,
        system_: SYSTEM,
        betas: [Anthropic::AnthropicBeta::COMPACT_2026_09_04],
        messages: older,
        compaction: { type: "summarize" }
      )
      if summary.stop_reason == :compaction
        history = [{ role: "assistant", content: summary.content }, *recent]
        puts "Kept #{recent.length / 2} turns after the block"
      end
    end
  end
  ```
</CodeGroup>

* **Picking the cut:** The program keeps the last two turns, where a turn is one `user` message and the reply to it. It splits the history four messages from the end, so the kept turns start with a `user` message.
* **Deciding when to compact:** The size check also requires that the conversation has more turns than the program keeps, so the older part is never empty.
* **The compaction request:** Where the loop sends the whole history, this version sends only the older messages.
* **The swap:** Where the loop replaces the whole history with the returned message, this version's new history is the returned message followed by the kept turns.

The `stop_reason` check and every request after the swap are unchanged from the loop.

## Keep thinking valid in the kept turns

If you send thinking blocks back on a model with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), the thinking in the kept turns stays valid only while the [conditions for kept thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) hold, and one of them limits where the cut can fall.

The program's cut, between a reply and the next `user` message, meets that condition. So does a cut at the end of a request you already made: compact exactly that request's `messages`, and keep everything your history has gained since.
