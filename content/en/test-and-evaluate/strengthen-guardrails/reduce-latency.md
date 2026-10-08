---
title: Reducing latency
url: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency
description: Reduce Claude's response latency by choosing a faster model like Claude Haiku 5.5, trimming prompt and output tokens, and streaming responses.
---

Latency refers to the time it takes for the model to process a prompt and generate an output. Latency can be influenced by various factors, such as the size of the model, the complexity of the prompt, and the underlying infrastructure supporting the model and point of interaction.

<Note>
  It's always better to first engineer a prompt that works well without model or prompt constraints, and then try latency reduction strategies afterward. Trying to reduce latency prematurely might prevent you from discovering what top performance looks like.
</Note>

***

## How to measure latency

When discussing latency, you might come across several terms and measurements:

* **Baseline latency:** This is the time taken by the model to process the prompt and generate the response, without considering the input and output tokens per second. It provides a general idea of the model's speed.
* **Time to first token (TTFT):** This metric measures the time it takes for the model to generate the first token of the response, from when the prompt was sent. It's particularly relevant when you're using streaming (more on that later) and want to provide a responsive experience to your users.

For a more in-depth understanding of these terms, check out the [glossary](https://platform.claude.com/docs/en/about-claude/glossary).

***

## How to reduce latency

### 1. Choose the right model

One of the most direct ways to reduce latency is to select the appropriate model for your use case. Anthropic offers a [range of models](https://platform.claude.com/docs/en/models/overview) with different capabilities and performance characteristics. Consider your specific requirements and choose the model that best fits your needs in terms of speed and output quality.

For speed-critical applications, **Claude Haiku 5.5** offers the fastest response times while maintaining high intelligence. [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) is its main control for speed and cost. See [Use effort to control thinking](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5#use-effort-to-control-thinking). The following example runs it at `low`, the cheapest and fastest level, and leaves room in `max_tokens` for thinking:

<CodeGroup>
  ```bash cURL
  # For time-sensitive applications, use Claude Haiku 5.5 at low effort
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-haiku-5-5",
      "max_tokens": 1024,
      "output_config": {"effort": "low"},
      "messages": [{"role": "user", "content": "Summarize this customer feedback in 2 sentences: [feedback text]"}]
    }'
  ```

  ```bash CLI
  # For time-sensitive applications, use Claude Haiku 5.5 at low effort
  ant messages create \
    --model claude-haiku-5-5 \
    --max-tokens 1024 \
    --output-config '{effort: low}' \
    --message '{"role": "user", "content": "Summarize this customer feedback in 2 sentences: [feedback text]"}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  # For time-sensitive applications, use Claude Haiku 5.5 at low effort
  message = client.messages.create(
      model="claude-haiku-5-5",
      max_tokens=1024,
      output_config={"effort": "low"},
      messages=[
          {
              "role": "user",
              "content": "Summarize this customer feedback in 2 sentences: [feedback text]",
          }
      ],
  )
  print(next(block.text for block in message.content if block.type == "text"))
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // For time-sensitive applications, use Claude Haiku 5.5 at low effort
  const message = await client.messages.create({
    model: "claude-haiku-5-5",
    max_tokens: 1024,
    output_config: { effort: "low" },
    messages: [
      {
        role: "user",
        content: "Summarize this customer feedback in 2 sentences: [feedback text]"
      }
    ]
  });
  const textBlock = message.content.find((block) => block.type === "text");
  console.log(textBlock?.text);
  ```

  ```csharp C#
  AnthropicClient client = new();

  // For time-sensitive applications, use Claude Haiku 5.5 at low effort
  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeHaiku5_5,
      MaxTokens = 1024,
      OutputConfig = new() { Effort = Effort.Low },
      Messages = [
          new()
          {
              Role = Role.User,
              Content = "Summarize this customer feedback in 2 sentences: [feedback text]"
          }
      ]
  };
  var message = await client.Messages.Create(parameters);
  foreach (var block in message.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
          break;
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  // For time-sensitive applications, use Claude Haiku 5.5 at low effort
  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeHaiku5_5,
  	MaxTokens: 1024,
  	OutputConfig: anthropic.OutputConfigParam{
  		Effort: anthropic.OutputConfigEffortLow,
  	},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Summarize this customer feedback in 2 sentences: [feedback text]")),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  for _, block := range message.Content {
  	if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
  		fmt.Println(textBlock.Text)
  		break
  	}
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  // For time-sensitive applications, use Claude Haiku 5.5 at low effort
  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_HAIKU_5_5)
      .maxTokens(1024L)
      .outputConfig(OutputConfig.builder()
          .effort(OutputConfig.Effort.LOW)
          .build())
      .addUserMessage("Summarize this customer feedback in 2 sentences: [feedback text]")
      .build();
  Message message = client.messages().create(params);
  IO.println(message.content().stream()
      .flatMap(block -> block.text().stream())
      .map(TextBlock::text)
      .findFirst()
      .orElse(""));
  ```

  ```php PHP
  $client = new Client();

  // For time-sensitive applications, use Claude Haiku 5.5 at low effort
  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Summarize this customer feedback in 2 sentences: [feedback text]']],
      model: 'claude-haiku-5-5',
      outputConfig: ['effort' => 'low'],
  );
  foreach ($message->content as $block) {
      if ($block->type === 'text') {
          echo $block->text;
          break;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # For time-sensitive applications, use Claude Haiku 5.5 at low effort
  message = client.messages.create(
    model: "claude-haiku-5-5",
    max_tokens: 1024,
    output_config: { effort: :low },
    messages: [{ role: "user", content: "Summarize this customer feedback in 2 sentences: [feedback text]" }]
  )
  puts message.content.find { |block| block.type == :text }&.text
  ```
</CodeGroup>

For more details about model metrics, see the [models overview](https://platform.claude.com/docs/en/models/overview) page.

### 2. Optimize prompt and output length

Minimize the number of tokens in both your input prompt and the expected output, while still maintaining high performance. The fewer tokens the model has to process and generate, the faster the response will be.

Here are some tips to help you optimize your prompts and outputs:

* **Be clear but concise:** Aim to convey your intent clearly and concisely in the prompt. Avoid unnecessary details or redundant information, while keeping in mind that [Claude lacks context](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct) on your use case and might not make the intended leaps of logic if instructions are unclear.
* **Ask for shorter responses:** Ask Claude directly to be concise. If Claude is outputting unwanted length, ask Claude to [curb its chattiness](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct).
  <Tip>
    Because of how LLMs count 

    [tokens](https://platform.claude.com/docs/en/about-claude/glossary#tokens)

     instead of words, asking for an exact word count or a word count limit is not as effective a strategy as asking for paragraph or sentence count limits.
  </Tip>
* **Set appropriate output limits:** Use the `max_tokens` parameter to set a hard limit on the maximum length of the generated response. This prevents Claude from generating overly long outputs.
  <Note>
    When the response reaches 

    `max_tokens`

     tokens, the response will be cut off, perhaps mid-sentence or mid-word, so this is a blunt technique that might require post-processing and is usually most appropriate for multiple choice or short answer responses where the answer comes right at the beginning.
  </Note>
* **Experiment with temperature:** The `temperature` [parameter](https://platform.claude.com/docs/en/api/messages/create) controls the randomness of the output. Lower values (for example, 0.2) can sometimes lead to more focused and shorter responses, while higher values (for example, 0.8) might result in more diverse but potentially longer outputs. Claude Haiku 5.5 accepts only the default `temperature` and returns a 400 error for any other value, so lower its [effort](https://platform.claude.com/docs/en/build-with-claude/effort) instead.

Finding the right balance among prompt clarity, output quality, and token count might require some experimentation.

### 3. Stream responses

Streaming is a feature that allows the model to start sending back its response before the full output is complete. This can significantly improve the perceived responsiveness of your application, as users can see the model's output in real time.

With streaming enabled, you can process the model's output as it arrives, updating your user interface or performing other tasks in parallel.

Visit [Streaming messages](https://platform.claude.com/docs/en/build-with-claude/streaming) to learn about how you can implement streaming for your use case.

***

## Next steps

<CardGroup cols={2}>
  <Card title="Reduce hallucinations" icon="shield" href="https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations">
    Minimize hallucinations in Claude's outputs by allowing uncertainty, grounding responses in direct quotes, and verifying claims with citations.
  </Card>

  <Card title="Streaming messages" icon="bolt" href="https://platform.claude.com/docs/en/build-with-claude/streaming">
    Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
  </Card>
</CardGroup>
