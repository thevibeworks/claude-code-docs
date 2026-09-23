---
title: Compaction on demand
url: https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand
description: Ask Claude to summarize a conversation when your application chooses, then continue from the summary.
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

With on-demand compaction, your application decides when a conversation is summarized: you send one request with the `compaction` parameter, and Claude returns a summary in place of a reply.

## How on-demand compaction works

A compaction request is separate from your conversation turns. You send the conversation as it stands with the `compaction` parameter, and the response contains a single `compaction` block. The block holds the summary as text you can read, and a signature. Send it in future requests exactly as it came.

From then on the block takes the place of the messages it summarizes. It goes first in `messages`, the summarized messages are removed, and your next turn follows it. Claude sees the summary where those messages were.

![On-demand compaction: a request that carries four messages and the compaction parameter returns one compaction block and no reply; on the next request the block comes first in messages in place of those four messages, followed by the next user turn](https://platform.claude.com/docs/images/compaction-on-demand-swap.svg)

## Request a summary

Send the `compact-2026-09-04` beta header on the request that asks for the summary and on every later request that carries the signed block. To check whether a model supports on-demand compaction, call the [Models API](https://platform.claude.com/docs/en/api/beta/models/list) with the beta header and read each model's `capabilities.compaction`. You can't combine `compaction` with `context_management` on one request.

Send the conversation as it stands with `"compaction": {"type": "summarize"}`. The API summarizes every message in the request once, generates no reply after it, and returns the block alone with `stop_reason` `"compaction"`. Send the same `system` prompt and `tools` that you use for the rest of the conversation. The summarizer reads them, and if you keep turns after the block on a model with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), the thinking in those turns stays valid only if `system` and `tools` match. The conversation in this example has no `system` prompt or tools, so the request sends neither:

<CodeGroup>
  ```bash cURL
  # max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: compact-2026-09-04" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 4096,
      "messages": [
        {"role": "user", "content": "I am building a recipe app. Help me name the main entities in the data model."},
        {"role": "assistant", "content": "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe."},
        {"role": "user", "content": "Good. Now suggest field names for Recipe."}
      ],
      "compaction": {"type": "summarize"}
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta compact-2026-09-04 <<'YAML'
  model: claude-opus-5-5
  # max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
  max_tokens: 4096
  messages:
    - role: user
      content: I am building a recipe app. Help me name the main entities in the data model.
    - role: assistant
      content: Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.
    - role: user
      content: Good. Now suggest field names for Recipe.
  compaction:
    type: summarize
  YAML
  ```

  ```python Python
  from anthropic.types.beta import BetaMessageParam

  client = anthropic.Anthropic()

  history: list[BetaMessageParam] = [
      {
          "role": "user",
          "content": "I am building a recipe app. Help me name the main entities in the data model.",
      },
      {
          "role": "assistant",
          "content": "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.",
      },
      {"role": "user", "content": "Good. Now suggest field names for Recipe."},
  ]

  response = client.beta.messages.create(
      model="claude-opus-5-5",
      # max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
      max_tokens=4096,
      betas=["compact-2026-09-04"],
      messages=history,
      compaction={"type": "summarize"},
  )
  print(f"Stop reason: {response.stop_reason}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const history: Anthropic.Beta.Messages.BetaMessageParam[] = [
    {
      role: "user",
      content: "I am building a recipe app. Help me name the main entities in the data model."
    },
    {
      role: "assistant",
      content:
        "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe."
    },
    { role: "user", content: "Good. Now suggest field names for Recipe." }
  ];

  const response = await client.beta.messages.create({
    model: "claude-opus-5-5",
    // max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
    max_tokens: 4096,
    betas: ["compact-2026-09-04"],
    messages: history,
    compaction: { type: "summarize" }
  });
  console.log(`Stop reason: ${response.stop_reason}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta;
  using Anthropic.Models.Beta.Messages;
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  List<BetaMessageParam> history =
  [
      new()
      {
          Role = Role.User,
          Content = "I am building a recipe app. Help me name the main entities in the data model.",
      },
      new()
      {
          Role = Role.Assistant,
          Content = "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.",
      },
      new() { Role = Role.User, Content = "Good. Now suggest field names for Recipe." },
  ];

  var response = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      // max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
      MaxTokens = 4096,
      Betas = [AnthropicBeta.Compact2026_09_04],
      Messages = history,
      Compaction = new BetaCompactionConfig(), // type defaults to "summarize"
  });

  Console.WriteLine($"Stop reason: {response.StopReason?.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  history := []anthropic.BetaMessageParam{
  	anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("I am building a recipe app. Help me name the main entities in the data model.")),
  	{
  		Role:    anthropic.BetaMessageParamRoleAssistant,
  		Content: []anthropic.BetaContentBlockParamUnion{anthropic.NewBetaTextBlock("Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.")},
  	},
  	anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Good. Now suggest field names for Recipe.")),
  }

  response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
  	Model: anthropic.ModelClaudeOpus5_5,
  	// max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
  	MaxTokens: 4096,
  	Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaCompact2026_09_04},
  	Messages:  history,
  	Compaction: anthropic.BetaCompactionConfigUnionParam{
  		OfSummarize: &anthropic.BetaSummarizeCompactionParam{},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println("Stop reason:", response.StopReason)
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaCompactionConfig;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  void main() {
      var client = AnthropicOkHttpClient.fromEnv();

      var params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          // max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
          .maxTokens(4096)
          .addBeta(AnthropicBeta.COMPACT_2026_09_04)
          .addUserMessage("I am building a recipe app. Help me name the main entities in the data model.")
          .addAssistantMessage("Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.")
          .addUserMessage("Good. Now suggest field names for Recipe.")
          .compaction(BetaCompactionConfig.builder().build()) // type defaults to "summarize"
          .build();

      var response = client.beta().messages().create(params);
      response.stopReason().ifPresent(reason -> IO.println("Stop reason: " + reason));
  }
  ```

  ```php PHP
  use Anthropic\Beta\AnthropicBeta;
  use Anthropic\Beta\Messages\BetaCompactionConfig;
  use Anthropic\Beta\Messages\BetaMessageParam;
  use Anthropic\Beta\Messages\BetaMessageParam\Role;

  $client = new Client();

  $history = [
      BetaMessageParam::with(
          role: Role::USER,
          content: 'I am building a recipe app. Help me name the main entities in the data model.',
      ),
      BetaMessageParam::with(
          role: Role::ASSISTANT,
          content: 'Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.',
      ),
      BetaMessageParam::with(role: Role::USER, content: 'Good. Now suggest field names for Recipe.'),
  ];

  $response = $client->beta->messages->create(
      model: Model::CLAUDE_OPUS_5_5,
      // max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
      maxTokens: 4096,
      betas: [AnthropicBeta::COMPACT_2026_09_04],
      messages: $history,
      compaction: BetaCompactionConfig::with(), // type defaults to 'summarize'
  );

  echo "Stop reason: {$response->stopReason}", PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  history = [
    {
      role: "user",
      content: "I am building a recipe app. Help me name the main entities in the data model."
    },
    {
      role: "assistant",
      content: "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe."
    },
    { role: "user", content: "Good. Now suggest field names for Recipe." }
  ]

  response = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    # max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
    max_tokens: 4096,
    betas: [Anthropic::AnthropicBeta::COMPACT_2026_09_04],
    messages: history,
    compaction: { type: "summarize" }
  )
  puts "Stop reason: #{response.stop_reason}"
  ```
</CodeGroup>

```json Response
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5-5",
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: the user is designing the data model for a recipe app. The entities agreed so far are Recipe, Ingredient, Step, and RecipeIngredient, which holds the quantity and unit. The user then asked for field names for Recipe.",
      "signature": "EuYBCkQY..."
    }
  ],
  "stop_reason": "compaction",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "iterations": [{ "type": "compaction", "input_tokens": 144, "output_tokens": 276 }]
  }
}
```

The summarization call uses the request's model, `system`, `tools`, thinking settings, and `max_tokens`. The summarizer reads the tool definitions but never runs a tool, and the response carries no thinking. `max_tokens` caps the whole call, including any thinking the model does before it writes the summary, so allow several thousand tokens. [Count compaction usage](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#understanding-usage) shows how the call is billed.

If the last `assistant` turn ends in a tool call with no result yet, the API rejects the request. Send that turn's tool results first. Also leave out `stop_sequences`, structured-output `output_config.format`, and a `tool_choice` of type `any` or `tool`. They would do nothing on a summarization call, and the API rejects them. The conversation must still fit the model's context window, so compact before you outgrow it, not after.

When you stream the response, the block arrives whole. You get one `content_block_start` event carrying the complete block, then `content_block_stop`, with no `content_block_delta` events. `ping` events can arrive before or between them.

## Continue from the summary

In your history, replace the messages you sent with the returned assistant message. Keep the `compaction` block exactly as the API returned it, including its `signature`. Any turns taken after you sent the compaction request follow the block unchanged, which is what [Compaction in the background](https://platform.claude.com/docs/en/build-with-claude/compaction-background) builds on. Send the block first on every later request, with the beta header:

```json
{
  "model": "claude-opus-5-5",
  "max_tokens": 2048,
  "messages": [
    {
      "role": "assistant",
      "content": [
        {
          "type": "compaction",
          "content": "Summary of the conversation: the user is designing the data model for a recipe app. The entities agreed so far are Recipe, Ingredient, Step, and RecipeIngredient, which holds the quantity and unit. The user then asked for field names for Recipe.",
          "signature": "EuYBCkQY..."
        }
      ]
    },
    {
      "role": "assistant",
      "content": "For Recipe, use title, description, servings, prep_minutes, and cook_minutes. Add created_at and updated_at timestamps."
    },
    { "role": "user", "content": "Now do the same for Ingredient." }
  ]
}
```

This example continues the request sample, which ended on a `user` turn; the diagram shows the simpler case, where no turn is taken while the summary is written. Here the second `assistant` message is the reply to the last summarized `user` turn. It arrived while the summary was being written, so it was not among the messages summarized. Two `assistant` messages in a row are fine here, because the block still comes first.

The API puts the summary where the block stands and passes every later message to Claude unchanged. Follow these rules:

* Put the block first in `messages`, either as an `assistant` message of its own or as the first content block of the first message, whether that is a `user` or `assistant` message.
* Remove the summarized messages. If any remain in front of the block, the request returns a 400 error (`compaction_block_misplaced`).
* Send exactly one `compaction` block per request, on every later request.

<Warning>
  Two mistakes in the swap raise no error. If summarized messages remain after the block, the API sends them to Claude again. If a later request leaves the block out, Claude gets no summary.
</Warning>

Threshold compaction works the other way around: its block follows the messages it summarizes, and the API drops them for you. See [Passing compaction blocks back](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#passing-compaction-blocks-back).

In Python, use `client.beta.messages`, as the samples on this page do. If you call `client.messages` and serialize blocks yourself, use `to_dict()` or `model_dump(exclude_none=True)`: a plain `model_dump()` adds `citations: null` and `text: null` to the block, and the API rejects it.

If you keep turns after the block and send their thinking blocks back, the conditions that keep that thinking valid are on [Compaction and preserved thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks).

### Compact again

To compact a conversation that already starts with a block, send `compaction` again. The new block summarizes the old summary and everything after it. From then on, send only the newest block.

## Compact in a loop

After each turn, the loop adds the last response's input and output tokens, because the next request sends the reply too. When that total passes a limit and another turn is still to come, it sends a compaction request with the same model and `system` prompt, checks `stop_reason`, replaces its history with the returned message, and prints the turn it compacted before. The sample's limit of 2,500 tokens is deliberately low, so that a short conversation compacts. Set yours near your real input budget.

<CodeGroup exclude="shell">
  ```python Python
  from anthropic.types.beta import BetaMessageParam

  client = anthropic.Anthropic()

  # Set this near your real input budget. It is low here so a short conversation compacts.
  COMPACT_AT_TOKENS = 2500
  SYSTEM = "You help design a recipe app's data model. Keep answers short."

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
      if conversation_tokens > COMPACT_AT_TOKENS and turn < len(QUESTIONS):
          summary = client.beta.messages.create(
              model="claude-opus-5-5",
              max_tokens=4096,
              system=SYSTEM,
              betas=["compact-2026-09-04"],
              messages=history,
              compaction={"type": "summarize"},
          )
          if summary.stop_reason == "compaction":
              history = [{"role": "assistant", "content": summary.content}]
              print(f"Compacted before turn {turn + 1}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // Set this near your real input budget. It is low here so a short conversation compacts.
  const compactAtTokens = 2500;
  const systemPrompt = "You help design a recipe app's data model. Keep answers short.";

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
    if (conversationTokens > compactAtTokens && turn < questions.length) {
      const summary = await client.beta.messages.create({
        model: "claude-opus-5-5",
        max_tokens: 4096,
        system: systemPrompt,
        betas: ["compact-2026-09-04"],
        messages: history,
        compaction: { type: "summarize" }
      });
      if (summary.stop_reason === "compaction") {
        history = [{ role: "assistant", content: summary.content }];
        console.log(`Compacted before turn ${turn + 1}`);
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
      if (conversationTokens > CompactAtTokens && turn < questions.Length)
      {
          var summary = await client.Beta.Messages.Create(new MessageCreateParams
          {
              Model = Model.ClaudeOpus5_5,
              MaxTokens = 4096,
              System = SystemPrompt,
              Betas = [AnthropicBeta.Compact2026_09_04],
              Messages = history,
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
              ];
              Console.WriteLine($"Compacted before turn {turn + 1}");
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
  	if conversationTokens > compactAtTokens && turn < len(questions) {
  		summary, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  			Model:     anthropic.ModelClaudeOpus5_5,
  			MaxTokens: 4096,
  			System:    system,
  			Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaCompact2026_09_04},
  			Messages:  history,
  			Compaction: anthropic.BetaCompactionConfigUnionParam{
  				OfSummarize: &anthropic.BetaSummarizeCompactionParam{},
  			},
  		})
  		if err != nil {
  			log.Fatal(err)
  		}
  		if summary.StopReason == anthropic.BetaStopReasonCompaction {
  			history = []anthropic.BetaMessageParam{summary.ToParam()}
  			fmt.Printf("Compacted before turn %d\n", turn+1)
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
          if (conversationTokens > COMPACT_AT_TOKENS && turn < questions.size()) {
              var summaryParams = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_5_5)
                  .maxTokens(4096)
                  .system(SYSTEM)
                  .addBeta(AnthropicBeta.COMPACT_2026_09_04)
                  .messages(history)
                  .compaction(BetaCompactionConfig.builder().build()) // type defaults to "summarize"
                  .build();
              var summary = client.beta().messages().create(summaryParams);
              if (summary.stopReason().map(BetaStopReason.COMPACTION::equals).orElse(false)) {
                  history.clear();
                  history.add(summary.toParam());
                  IO.println("Compacted before turn " + (turn + 1));
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
      if ($conversationTokens > COMPACT_AT_TOKENS && $turn < count($questions)) {
          $summary = $client->beta->messages->create(
              model: Model::CLAUDE_OPUS_5_5,
              maxTokens: 4096,
              system: SYSTEM,
              betas: [AnthropicBeta::COMPACT_2026_09_04],
              messages: $history,
              compaction: new BetaCompactionConfig(), // type defaults to 'summarize'
          );
          if ($summary->stopReason === BetaStopReason::COMPACTION->value) {
              $history = [BetaMessageParam::with(role: Role::ASSISTANT, content: $summary->content)];
              printf("Compacted before turn %d\n", $turn + 1);
          }
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Set this near your real input budget. It is low here so a short conversation compacts.
  COMPACT_AT_TOKENS = 2500
  SYSTEM = "You help design a recipe app's data model. Keep answers short."

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
    if conversation_tokens > COMPACT_AT_TOKENS && turn < questions.length
      summary = client.beta.messages.create(
        model: Anthropic::Model::CLAUDE_OPUS_5_5,
        max_tokens: 4096,
        system_: SYSTEM,
        betas: [Anthropic::AnthropicBeta::COMPACT_2026_09_04],
        messages: history,
        compaction: { type: "summarize" }
      )
      if summary.stop_reason == :compaction
        history = [{ role: "assistant", content: summary.content }]
        puts "Compacted before turn #{turn + 1}"
      end
    end
  end
  ```
</CodeGroup>

The check on `stop_reason` comes before the code looks for the block; [Handle a missing summary or an error](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) says why. The history is replaced, not appended to: the returned message replaces every message the request carried, under the rules in [Continue from the summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary). When no summary comes back, the loop keeps its history and asks again after the next turn.

The SDK [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) in Python, TypeScript, C#, Go, Java, PHP, and Ruby can send the compaction request for you. When you decide to compact, call `compact_before_next_turn()` on the runner (`compactBeforeNextTurn()` in TypeScript, Java, and PHP, and `CompactBeforeNextTurn()` in C# and Go). Once the current turn and its tool calls finish, the runner sends the compaction request and replaces its history with the returned message. Create the runner with the `compact-2026-09-04` beta, because the runner doesn't add it.

The runner builds the compaction request from its own parameters and leaves `context_management` out. It also leaves out `stop_sequences`, a `tool_choice` of type `any` or `tool`, and a structured-output `output_config.format`, which the API rejects on a compaction request. [Request a summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary) explains why. The runner sends them again on its later requests. SDK versions before Python 1.8.0, TypeScript 0.128.0, C# 12.50.0, Go 1.75.0, and Java 2.65.0 send them on the compaction request too. On those versions, a runner that sets any of these parameters gets a 400 error. The runner sends a [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets) unchanged. If `output_config.task_budget` sets `remaining`, the compaction request returns a 400 error, so leave `remaining` unset, as [Limits and interactions with other features](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#how-it-fits-with-the-rest-of-the-api) says. The runner refuses to compact while its `context_management` has a compaction edit, so use one kind of compaction on a runner.

### When to compact

You can send a compaction request after any completed turn, so your code decides when.

To estimate how large the next request will be, add `input_tokens` and `output_tokens` from the last response's `usage`, as the loop does. With [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#tracking-cache-performance), `input_tokens` counts only the tokens after the last cache breakpoint, so add `cache_read_input_tokens` and `cache_creation_input_tokens` as well. You can also send the same messages to the [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint.

Compare that number with a limit you choose, below the model's [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows).

## Write your own summarization prompt

Without `instructions`, the API uses its own summarization prompt. A non-blank `instructions` string (up to 16,384 characters) replaces that prompt entirely. For example:

```json
{
  "compaction": {
    "type": "summarize",
    "instructions": "Summarize this recipe app design conversation. Preserve every entity and field name agreed so far, and the user's latest open request. Do not call tools; respond with the summary text only."
  }
}
```

The summarizer reads the whole conversation, earlier thinking included, with or without `instructions`. In your `instructions`, say what the summary must retain and tell the model not to call tools. The summarization call runs under the same safeguards as any other request.

## Handle a missing summary or an error

A summary is produced only when the summarization call ends normally with text and no tool call. Otherwise, the response is still a 200 with empty `content`, so check `stop_reason` before you look for the block. The call is still billed and reported in `usage.iterations`, with zero usage when no call could be made. The `stop_reason` is the one the summarization call ended with. In every case you can continue without a summary and compact later.

| `stop_reason`                     | Cause                                                   | What to do                                                        |
| --------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| `"max_tokens"`                    | The summary was cut off.                                | Resend with a larger `max_tokens`.                                |
| `"model_context_window_exceeded"` | There was no room for the summarization prompt.         | Resend with shorter `instructions` or fewer messages.             |
| `"tool_use"`                      | The model called a tool instead of writing the summary. | Resend with `instructions` that tell the model not to call tools. |
| `"refusal"`                       | The request was declined.                               | Continue without a summary.                                       |
| `"end_turn"`                      | The call returned no text.                              | Continue without a summary.                                       |

The summarization call is subject to the same safeguards as your other requests. After a `"refusal"`, [`stop_details`](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#refusal) identifies the policy category behind it.

### Errors

A compaction request, or a request that carries a block, can also fail outright. Most 400 errors have a message that says what to remove or resend. Some also carry an `error.details.error_code` that starts with `compaction_`. Parameter errors, such as a field that can't be combined with `compaction`, carry the message only.

| Error                                                                                                                                                                           | Cause                                                                                   | What to do                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 529 `overloaded_error`, `error.details.error_code` `compaction_unavailable`                                                                                                     | A transient server problem while producing a block, or while reading one you sent back. | Retry the request.                                                                                                                                                                  |
| 400 `compaction_block_misplaced`                                                                                                                                                | Summarized messages remain in front of the block.                                       | Remove them, so the block comes first in `messages`.                                                                                                                                |
| 400 `compaction_signature_invalid` or `compaction_content_mismatch`                                                                                                             | The block's `signature` or `content` was changed after the API returned it.             | Send the block exactly as returned, including its `signature`.                                                                                                                      |
| 400                                                                                                                                                                             | The request carries more than one `compaction` block.                                   | Send exactly one, the newest.                                                                                                                                                       |
| 400                                                                                                                                                                             | The last `assistant` turn ends in a tool call with no result yet.                       | Send that turn's tool results, then compact.                                                                                                                                        |
| 400 `compaction_nothing_to_summarize`                                                                                                                                           | `messages` has no `user` or `assistant` content, for example an empty list.             | Send at least one `user` or `assistant` message.                                                                                                                                    |
| 400 on the compaction request, with a message that says the `compaction` parameter `requires anthropic-beta: compact-2026-09-04`                                                | The compaction request left out the beta header.                                        | Add the beta header; see [Request a summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary).                                         |
| 400 on a later request that carries the block: a validation error that says `compaction` is not one of the expected content block types. The message doesn't mention the header | That request left out the beta header.                                                  | Add the beta header to every request that carries the block; see [Request a summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary). |
| 400 validation error, such as `messages.0.content.0.compaction.citations: Extra inputs are not permitted`                                                                       | A block was sent back with fields the API didn't return, such as `citations: null`.     | Send the block exactly as returned; see [Continue from the summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary).          |

## Count compaction usage

The summarization call is billed and rate-limited like any other request, and `usage.iterations` reports it as the `compaction` entry. The top-level `input_tokens` and `output_tokens` are zero because no reply was generated. To count what a conversation consumed, sum across `usage.iterations`, not the top-level fields. Sending a block back on later requests adds no compaction cost.

You have a working loop that compacts a conversation and handles a missing summary. Two pages change how it runs, and you can combine them: [Compaction that keeps recent turns](https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns) keeps the last turns word for word, and [Compaction in the background](https://platform.claude.com/docs/en/build-with-claude/compaction-background) lets the conversation continue while the summary is written. [Compaction and preserved thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks) applies if you send thinking blocks back and do either.

## Limits and interactions with other features

* **Threshold compaction and context editing.** You can't send `compaction` and `context_management` on the same request. Threshold compaction (`compact_20260112`) can't run on a request that carries a signed block.
* **Prompt caching.** `cache_control` on the block places a breakpoint after the summary.
* **Mid-conversation system messages and tool changes.** `role: "system"` messages inside the summarized range are summarized too, so their text instructions stop applying once the block replaces them. If an instruction still matters, state it again in a `role: "system"` message. Send that message right after your next new `user` turn, and leave it in your history from then on. For [tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes), and for where that message goes when you keep turns after the block, see [Change the system prompt or tools](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#change-the-system-prompt-or-tools).
* **Task budgets.** Don't send the `remaining` value of a [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets) (`output_config.task_budget.remaining`) with `compaction` or on requests that carry the block. Doing so returns a 400 error.
* **Token counting.** The [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint ignores the `compaction` parameter.
* **Content the summary can't carry.** Images, documents, `container_upload` blocks, and fetched URLs inside the summarized messages are gone once the block replaces them. Restate or re-upload anything a later turn still needs.
