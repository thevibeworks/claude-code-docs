---
title: Multilingual support
url: https://platform.claude.com/docs/en/build-with-claude/multilingual-support
description: Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.
featureMetadata:
  status: stable
  supportedModels:
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-sonnet-5
    - claude-haiku-5-5
    - claude-haiku-4-5-20251001
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-4-6
    - claude-opus-4-5-20251101
    - claude-sonnet-4-5-20250929
  supportedPlatforms:
    Claude API: stable
    Claude Platform on AWS: stable
    Amazon Bedrock: stable
    Amazon Bedrock (InvokeModel): stable
    Claude Models on Google Cloud (Google managed): stable
    Microsoft Foundry: stable
---

## Overview

Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages.

Claude is capable in many languages beyond those benchmarked in the following table. Test with any languages relevant to your specific use cases.

## Performance data

The following table shows zero-shot scores for Claude models on [Global-MMLU](https://arxiv.org/abs/2412.03304), which extends the [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) test set to 42 languages. Each score is a percentage of the same model’s English score:

| Language             | Claude Fable 5.1 | Claude Opus 5.5 | Claude Sonnet 5.5 | Claude Haiku 5.5 |
| -------------------- | ---------------- | --------------- | ----------------- | ---------------- |
| English              | 100%             | 100%            | 100%              | 100%             |
| Spanish              | 99.4%            | 99.3%           | 99.0%             | 98.1%            |
| Portuguese (Brazil)  | 99.0%            | 99.2%           | 98.7%             | 98.1%            |
| Italian              | 99.0%            | 99.2%           | 98.4%             | 97.7%            |
| French               | 99.0%            | 99.3%           | 98.7%             | 97.7%            |
| Indonesian           | 98.9%            | 99.1%           | 98.6%             | 97.1%            |
| German               | 99.1%            | 99.1%           | 98.5%             | 97.4%            |
| Arabic               | 98.7%            | 99.3%           | 98.3%             | 96.6%            |
| Chinese (Simplified) | 98.8%            | 99.3%           | 98.5%             | 97.7%            |
| Korean               | 98.8%            | 99.1%           | 98.3%             | 97.0%            |
| Japanese             | 98.7%            | 99.2%           | 98.4%             | 97.4%            |
| Hindi                | 98.9%            | 99.2%           | 98.5%             | 96.6%            |
| Bengali              | 98.3%            | 98.6%           | 97.2%             | 95.4%            |
| Swahili              | 97.7%            | 98.3%           | 96.9%             | 94.0%            |
| Yoruba               | 95.1%            | 96.3%           | 93.6%             | 87.0%            |

All scores use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) at the `max` [effort level](https://platform.claude.com/docs/en/build-with-claude/effort). Scores exclude questions that safety classifiers blocked or that went unanswered. For each score in the table, at most 1.7 percent of the questions are excluded.

<Note>
  Use the table to compare languages within a model, not to rank models. Differences of less than about 1 percentage point are within measurement noise.
</Note>

***

## Set the response language

Claude infers the response language from the conversation, but for production applications you should state the target language explicitly. The most reliable place to do this is the system prompt, which keeps the instruction stable across every turn of a conversation.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "system": "Always respond in French, regardless of the language the user writes in.",
      "messages": [
        {"role": "user", "content": "How do I reset my password?"}
      ]
    }'
  ```

  ```bash CLI
  ant messages create \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --system "Always respond in French, regardless of the language the user writes in." \
    --message '{role: user, content: "How do I reset my password?"}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      system="Always respond in French, regardless of the language the user writes in.",
      messages=[{"role": "user", "content": "How do I reset my password?"}],
  )

  print(message.content)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    system: "Always respond in French, regardless of the language the user writes in.",
    messages: [{ role: "user", content: "How do I reset my password?" }]
  });

  console.log(message.content);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      MaxTokens = 1024,
      System = "Always respond in French, regardless of the language the user writes in.",
      Messages = [new UserMessageParam { Content = "How do I reset my password?" }]
  };

  var message = await client.Messages.Create(parameters);
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	System: []anthropic.TextBlockParam{
  		{Text: "Always respond in French, regardless of the language the user writes in."},
  	},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("How do I reset my password?")),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(message.Content)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_5_5)
      .maxTokens(1024)
      .system("Always respond in French, regardless of the language the user writes in.")
      .addUserMessage("How do I reset my password?")
      .build();

  Message message = client.messages().create(params);
  System.out.println(message.content());
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [
          ['role' => 'user', 'content' => 'How do I reset my password?']
      ],
      model: Model::CLAUDE_OPUS_5_5,
      system: 'Always respond in French, regardless of the language the user writes in.',
  );

  echo json_encode($message->content, JSON_PRETTY_PRINT), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    system: "Always respond in French, regardless of the language the user writes in.",
    messages: [
      { role: "user", content: "How do I reset my password?" }
    ]
  )

  puts message.content
  ```
</CodeGroup>

If your application lets users pick a language at runtime, interpolate that choice into the system prompt rather than relying on Claude to infer it from the user’s message. To translate between two specific languages, name both: `Translate the user's message from German to Korean. Respond with only the translation.`

***

## Best practices

When working with multilingual content:

1. **Provide clear language context:** Although Claude can detect the target language automatically, explicitly stating the input and output languages you want improves reliability. For enhanced fluency, you can prompt Claude to use “idiomatic speech as if it were a native speaker.”
2. **Use native scripts:** Submit text in its native script rather than transliteration for optimal results.
3. **Consider cultural context:** Effective communication often requires cultural and regional awareness beyond pure translation.

Also follow the general guidance in [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) to further improve output quality.

***

## Language support considerations

* Claude processes input and generates output in most world languages that use standard Unicode characters.
* Performance varies by language, with particularly strong capabilities in widely spoken languages.
* Even in languages with fewer digital resources, Claude maintains meaningful capabilities.

## Next steps

<CardGroup cols={2}>
  <Card title="Prompt engineering overview" icon="edit" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview">
    Apply general prompting techniques to improve multilingual output quality.
  </Card>

  <Card title="Customer support agent" icon="headset" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat">
    Build a customer support chatbot. One chatbot can serve customers in many languages.
  </Card>

  <Card title="Models overview" icon="table" href="https://platform.claude.com/docs/en/models/overview">
    Compare model tiers to balance multilingual quality against cost and latency.
  </Card>

  <Card title="Define success criteria and build evaluations" icon="scales" href="https://platform.claude.com/docs/en/test-and-evaluate/develop-tests">
    Apply general evaluation methods to measure output quality in each language you support.
  </Card>
</CardGroup>

## Availability

Multilingual support is available on every model.

### API support

#### [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

* Availability: Always on

| Status    | Cloud platforms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Amazon Bedrock (InvokeModel)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) |

#### [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)

* Availability: Always on

| Status    | Cloud platforms                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| Available | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) |
