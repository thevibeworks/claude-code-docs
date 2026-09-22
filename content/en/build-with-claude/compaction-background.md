---
title: Compaction in the background
url: https://platform.claude.com/docs/en/build-with-claude/compaction-background
description: Request an on-demand compaction summary while the conversation continues on its full history, then swap the block in when it arrives.
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

Background compaction, often called async compaction, changes two things in the [compaction loop](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop): the compaction request runs while the conversation continues on its full history, and the swap waits until the block arrives. [Continue from the summary](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) and [Handle a missing summary or an error](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) apply unchanged.

## How the swap works while work continues

The compaction request and the block it returns are the same as in the loop. Your history grows between sending the request and using its result, and the swap must leave that growth in place.

1. Send the [compaction request](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#request-a-summary) with your history as it stands, and record how many messages it held.
2. While that request runs, keep the conversation going on the full history. Append each new turn, don't edit anything already in the history, and don't start another compaction request until this one is swapped in or has failed.
3. When the response arrives with `stop_reason` `"compaction"`, drop exactly the messages you sent from the front of your history and put the returned message in their place. Every turn appended since step 1 stays after it.
4. Send the swapped history on the first request after the block arrives, so that thinking produced while the summary was being written stays valid.

For example, if the compaction request held messages 1 to 5 and the conversation gained messages 6 to 8 while it ran, after the swap your history is the block followed by messages 6 to 8.

![Background compaction timeline: the compaction request is sent with messages 1 to 5 while the conversation continues on its full history and gains messages 6 to 8; when the block arrives, it replaces messages 1 to 5 at the front of the history, and the history becomes the block followed by messages 6 to 8](https://platform.claude.com/docs/images/compaction-background-timeline.svg)

If the response has any other `stop_reason`, no summary was produced, which counts as a failure in step 2. Keep the full history; [Handle a missing summary or an error](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) lists the causes and what to do for each.

## Request the summary in the background

The compaction request counts against your rate limits like any other request, and while it runs your application has two requests open at once. The conversation keeps growing on its full history until the swap, so start the compaction request while the context window still has room for the turns that arrive meanwhile.

The following program is the loop from [Compact in a loop](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop) with the compaction request taken off the conversation's path. It has no PHP version, because the example depends on running two requests at once. The highlighted lines show where it differs from the loop, and the following list takes them in the order the program runs them.

<CodeGroup exclude="shell, php">
  ```python Python
  from concurrent.futures import Future, ThreadPoolExecutor

  import anthropic
  from anthropic.types.beta import BetaMessage, BetaMessageParam

  client = anthropic.Anthropic()
  executor = ThreadPoolExecutor(max_workers=1)

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


  def swap_in(history: list[BetaMessageParam], summary: BetaMessage, sent: int) -> None:
      if summary.stop_reason == "compaction":
          # Replace exactly the messages the compaction request held.
          # Later turns stay after the block.
          history[:sent] = [{"role": "assistant", "content": summary.content}]
          print(f"Swapped {sent} messages")


  history: list[BetaMessageParam] = []
  pending: Future[BetaMessage] | None = None
  sent = 0
  for turn, question in enumerate(QUESTIONS, start=1):
      if pending is not None and pending.done():
          swap_in(history, pending.result(), sent)
          pending = None

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
      if (
          conversation_tokens > COMPACT_AT_TOKENS
          and turn < len(QUESTIONS)
          and pending is None
      ):
          sent = len(history)
          pending = executor.submit(
              client.beta.messages.create,
              model="claude-opus-5-5",
              max_tokens=4096,
              system=SYSTEM,
              betas=["compact-2026-09-04"],
              messages=history.copy(),
              compaction={"type": "summarize"},
          )

  # Swap in a summary that is still on its way before you save
  # or continue the conversation.
  if pending is not None:
      swap_in(history, pending.result(), sent)
  executor.shutdown()
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

  function swapIn(
    history: Anthropic.Beta.Messages.BetaMessageParam[],
    summary: Anthropic.Beta.Messages.BetaMessage,
    sent: number
  ): Anthropic.Beta.Messages.BetaMessageParam[] {
    if (summary.stop_reason !== "compaction") {
      return history;
    }
    console.log(`Swapped ${sent} messages`);
    // Replace exactly the messages the compaction request held. Later turns stay after the block.
    return [{ role: "assistant", content: summary.content }, ...history.slice(sent)];
  }

  let history: Anthropic.Beta.Messages.BetaMessageParam[] = [];
  let pending: Promise<Anthropic.Beta.Messages.BetaMessage> | undefined;
  let settled = false;
  let sent = 0;
  for (const [index, question] of questions.entries()) {
    const turn = index + 1;
    if (pending && settled) {
      history = swapIn(history, await pending, sent);
      pending = undefined;
      settled = false;
    }

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
    if (conversationTokens > compactAtTokens && turn < questions.length && !pending) {
      sent = history.length;
      pending = client.beta.messages.create({
        model: "claude-opus-5-5",
        max_tokens: 4096,
        system: systemPrompt,
        betas: ["compact-2026-09-04"],
        messages: [...history],
        compaction: { type: "summarize" }
      });
      // Mark the request settled either way. Awaiting it then returns the summary or throws.
      const markSettled = () => {
        settled = true;
      };
      pending.then(markSettled, markSettled);
    }
  }

  // Swap in a summary that is still on its way before you save or continue the conversation.
  if (pending) {
    history = swapIn(history, await pending, sent);
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

  static List<BetaMessageParam> SwapIn(List<BetaMessageParam> history, BetaMessage summary, int sent)
  {
      if (summary.StopReason != BetaStopReason.Compaction)
      {
          return history;
      }
      Console.WriteLine($"Swapped {sent} messages");
      // Replace exactly the messages the compaction request held. Later turns stay after the block.
      return
      [
          new()
          {
              Role = Role.Assistant,
              Content = summary.Content.Select(block => new BetaContentBlockParam(block.Json)).ToList(),
          },
          .. history[sent..],
      ];
  }

  List<BetaMessageParam> history = [];
  Task<BetaMessage>? pending = null;
  var sent = 0;
  foreach (var (index, question) in questions.Index())
  {
      var turn = index + 1;
      if (pending is { IsCompleted: true })
      {
          history = SwapIn(history, await pending, sent);
          pending = null;
      }

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
      if (conversationTokens > CompactAtTokens && turn < questions.Length && pending is null)
      {
          sent = history.Count;
          pending = client.Beta.Messages.Create(new MessageCreateParams
          {
              Model = Model.ClaudeOpus5_5,
              MaxTokens = 4096,
              System = SystemPrompt,
              Betas = [AnthropicBeta.Compact2026_09_04],
              Messages = [.. history],
              Compaction = new BetaCompactionConfig(), // type defaults to "summarize"
          });
      }
  }

  // Swap in a summary that is still on its way before you save or continue the conversation.
  if (pending is not null)
  {
      history = SwapIn(history, await pending, sent);
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
  var pending chan *anthropic.BetaMessage
  var sent int
  swapIn := func(summary *anthropic.BetaMessage) {
  	if summary.StopReason != anthropic.BetaStopReasonCompaction {
  		return
  	}
  	fmt.Printf("Swapped %d messages\n", sent)
  	// Replace exactly the messages the compaction request held. Later turns stay after the block.
  	history = slices.Replace(history, 0, sent, summary.ToParam())
  }

  for i, question := range questions {
  	turn := i + 1
  	// Receiving from a nil channel never succeeds, so this skips when nothing is pending.
  	select {
  	case summary := <-pending:
  		swapIn(summary)
  		pending = nil
  	default:
  	}

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
  	if conversationTokens > compactAtTokens && turn < len(questions) && pending == nil {
  		sent = len(history)
  		pending = make(chan *anthropic.BetaMessage, 1)
  		go func(messages []anthropic.BetaMessageParam, result chan<- *anthropic.BetaMessage) {
  			summary, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  				Model:     anthropic.ModelClaudeOpus5_5,
  				MaxTokens: 4096,
  				System:    system,
  				Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaCompact2026_09_04},
  				Messages:  messages,
  				Compaction: anthropic.BetaCompactionConfigUnionParam{
  					OfSummarize: &anthropic.BetaSummarizeCompactionParam{},
  				},
  			})
  			if err != nil {
  				log.Fatal(err)
  			}
  			result <- summary
  		}(slices.Clone(history), pending)
  	}
  }

  // Swap in a summary that is still on its way before you save or continue the conversation.
  if pending != nil {
  	swapIn(<-pending)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.AnthropicBeta;
  import com.anthropic.models.beta.messages.BetaCompactionConfig;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaMessageParam;
  import com.anthropic.models.beta.messages.BetaStopReason;
  import com.anthropic.models.beta.messages.MessageCreateParams;

  // Set this near your real input budget. It is low here so a short conversation compacts.
  static final long COMPACT_AT_TOKENS = 2500;
  static final String SYSTEM = "You help design a recipe app's data model. Keep answers short.";

  void swapIn(List<BetaMessageParam> history, BetaMessage summary, int sent) {
      if (!summary.stopReason().map(BetaStopReason.COMPACTION::equals).orElse(false)) {
          return;
      }
      IO.println("Swapped " + sent + " messages");
      // Replace exactly the messages the compaction request held. Later turns stay after the block.
      history.subList(0, sent).clear();
      history.addFirst(summary.toParam());
  }

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
      CompletableFuture<BetaMessage> pending = null;
      int sent = 0;
      for (int turn = 1; turn <= questions.size(); turn++) {
          if (pending != null && pending.isDone()) {
              swapIn(history, pending.join(), sent);
              pending = null;
          }

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
          if (conversationTokens > COMPACT_AT_TOKENS && turn < questions.size() && pending == null) {
              sent = history.size();
              var summaryParams = MessageCreateParams.builder()
                  .model(Model.CLAUDE_OPUS_5_5)
                  .maxTokens(4096)
                  .system(SYSTEM)
                  .addBeta(AnthropicBeta.COMPACT_2026_09_04)
                  .messages(List.copyOf(history))
                  .compaction(BetaCompactionConfig.builder().build()) // type defaults to "summarize"
                  .build();
              pending = client.async().beta().messages().create(summaryParams);
          }
      }

      // Swap in a summary that is still on its way before you save or continue the conversation.
      if (pending != null) {
          swapIn(history, pending.join(), sent);
      }
      client.close();
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

  def swap_in(history, summary, sent)
    return history unless summary.stop_reason == :compaction

    puts "Swapped #{sent} messages"
    # Replace exactly the messages the compaction request held. Later turns stay after the block.
    [{ role: "assistant", content: summary.content }, *history[sent..]]
  end

  history = []
  pending = nil
  sent = 0
  questions.each.with_index(1) do |question, turn|
    if pending && !pending.alive?
      history = swap_in(history, pending.value, sent)
      pending = nil
    end

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
    if conversation_tokens > COMPACT_AT_TOKENS && turn < questions.length && pending.nil?
      sent = history.length
      pending = Thread.new(history.dup) do |snapshot|
        client.beta.messages.create(
          model: Anthropic::Model::CLAUDE_OPUS_5_5,
          max_tokens: 4096,
          system_: SYSTEM,
          betas: [Anthropic::AnthropicBeta::COMPACT_2026_09_04],
          messages: snapshot,
          compaction: { type: "summarize" }
        )
      end
    end
  end

  # Swap in a summary that is still on its way before you save or continue the conversation.
  history = swap_in(history, pending.value, sent) if pending
  ```
</CodeGroup>

* **Deciding when to compact:** The size check also requires that no compaction request is pending.
* **Starting the request:** Where the loop waits for the compaction response, this version records how many messages the history holds, starts the request on a copy of the history with each language's own concurrency tool, and goes on to the next turn without waiting.
* **Checking for the result:** At the top of each turn, the program checks whether the pending request has finished. If it has, the program makes the swap before it sends that turn's request.
* **Making the swap:** Where the loop replaces the whole history with the returned message, this version's swap function replaces only the messages the request held, counted from the front, and keeps everything appended since.
* **Ending the loop:** If the compaction request is still pending when the loop ends, the program waits for it and makes the swap, so a summary that is still on its way isn't lost before you save or continue the conversation.

The `stop_reason` check is unchanged from the loop: a response without a block leaves the history as it was. Because nothing is pending any more, the program can then start a new compaction request.

## Keep thinking valid while the summary is built

Turns that arrive while the summary is being written are kept turns. If you send thinking blocks back on a model with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), the thinking in those turns stays valid only while the [conditions for kept thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) hold.
