---
title: Per-message effort
url: https://platform.claude.com/docs/en/build-with-claude/effort-per-message
description: Use a system message to change the effort level partway through a conversation and keep the prompt cache.
featureMetadata:
  status: beta
  betaHeader: mid-conversation-output-config-2026-07-01
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-haiku-5-5
  supportedPlatforms:
    Claude API: beta
    Amazon Bedrock: beta
    Amazon Bedrock (bedrock-runtime):
      availability: beta
      note: Send the beta value in the `anthropic_beta` array of the request body.
    Claude Platform on AWS: beta
    Claude Models on Google Cloud (Anthropic managed): beta
    Claude Models on Google Cloud (Google managed): beta
    Microsoft Foundry: beta
---

A per-message effort change sets a new effort level for later turns of a conversation without changing the request’s top-level value, so the cached prefix still matches.

## Change the effort level

To change the level partway through a conversation:

1. Add a `role: "system"` message to `messages`, with empty `content` and the new [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level in `output_config.effort`.
2. Send the `mid-conversation-output-config-2026-07-01` [beta header](https://platform.claude.com/docs/en/api/beta-headers).
3. Leave the top-level value unchanged.

The following example keeps the top-level value at `high` and drops to `low` for a routine follow-up:

<CodeGroup>
  ```bash cURL
  # Effort-only system message: the new level takes effect from the next user turn.
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
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
  ant beta:messages create \
    --beta mid-conversation-output-config-2026-07-01 <<'YAML'
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
  using Model = Anthropic.Models.Messages.Model;

  AnthropicClient client = new();

  var response = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeFable5_1,
      MaxTokens = 4096,
      OutputConfig = new() { Effort = Effort.High },
      Messages =
      [
          new BetaUserMessageParam { Content = "Plan a migration from SQLite to PostgreSQL in three short steps." },
          new BetaAssistantMessageParam { Content = "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts." },
          // Effort-only system message: the new level takes effect from the next user turn.
          new BetaSystemMessageParam
          {
              Content = new([]),
              OutputConfig = new() { Effort = BetaSystemMessageOutputConfigEffort.Low },
          },
          new BetaUserMessageParam { Content = "Summarize the plan in one sentence." },
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
  	Model:     anthropic.ModelClaudeFable5_1,
  	MaxTokens: 4096,
  	OutputConfig: anthropic.BetaOutputConfigParam{
  		Effort: anthropic.BetaOutputConfigEffortHigh,
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Plan a migration from SQLite to PostgreSQL in three short steps.")),
  		{OfAssistant: &anthropic.BetaAssistantMessageParam{
  			Content: []anthropic.BetaContentBlockParamUnion{anthropic.NewBetaTextBlock("1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.")},
  		}},
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
  import com.anthropic.models.beta.messages.BetaOutputConfig;
  import com.anthropic.models.beta.messages.BetaSystemMessageOutputConfig;
  import com.anthropic.models.beta.messages.BetaSystemMessageParam;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_FABLE_5_1)
          .maxTokens(4096L)
          .addBeta(AnthropicBeta.MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01)
          .outputConfig(BetaOutputConfig.builder()
              .effort(BetaOutputConfig.Effort.HIGH)
              .build())
          .addUserMessage("Plan a migration from SQLite to PostgreSQL in three short steps.")
          .addAssistantMessage("1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.")
          // Effort-only system message: the new level takes effect from the next user turn.
          .addMessage(BetaSystemMessageParam.builder()
              .contentOfBlocks(List.of())
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
  use Anthropic\Beta\Messages\BetaTextBlock;
  use Anthropic\Client;
  use Anthropic\Messages\Model;

  $client = new Client();

  $response = $client->beta->messages->create(
      model: Model::CLAUDE_FABLE_5_1,
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
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_FABLE_5_1,
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
    case block
    when Anthropic::Beta::BetaTextBlock
      puts block.text
    end
  end
  ```
</CodeGroup>

The message’s position decides when the new level starts:

* Directly after a `user` turn with new input: Claude’s reply to that turn uses the new level.
* In any other position, such as between an `assistant` turn and the next `user` turn as in the preceding example: the new level starts at the next `user` turn with new input.

A `user` turn that holds only `tool_result` blocks doesn’t count as new input.

The new level stays in effect until a later message changes it.

Put the message after everything you’ve already sent, and keep it in place on later requests. Don’t insert it before turns you’ve already sent, and don’t move or remove it later. On models with [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), any of those changes invalidates the thinking blocks in the `assistant` turns after the message. [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) says what happens next.

If it sits next to a `system` message that has content, both messages must follow the [placement rules for mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations).

With the Amazon Bedrock InvokeModel API, send the beta value in the `anthropic_beta` array of the request body instead of the header. For the models that support per-message effort there, see [Mid-conversation system messages on Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#mid-conversation-system-messages-on-bedrock).

## Errors

* Without the beta header, a per-message `output_config` returns a 400 error: `messages.N.output_config: Extra inputs are not permitted`, where `N` is the index of the `system` message in `messages`.
* With the beta header, models without per-message effort, such as Claude Fable 5, return a 400 error: `output_config.effort requires a model that supports per-turn effort; this model does not`. On Amazon Bedrock, those models and Claude Opus 5 return `Extra inputs are not permitted` instead.
* On Claude Sonnet 5.5 with `thinking: {"type": "between_tools"}`, and on Claude Haiku 5.5 with `thinking: {"type": "disabled"}`, you can’t change the effort level mid-conversation. There, a per-message `output_config.effort` with a new level returns a 400 error. To vary effort for each turn, use adaptive thinking.

## Per-message or top-level effort

Prefer per-message effort over [changing the top-level value](https://platform.claude.com/docs/en/build-with-claude/effort#top-level-effort-on-the-next-request) between requests. A per-message change leaves everything before it unchanged, so the cached prefix still matches. A top-level change restarts the cache. On Claude Fable 5.1, a top-level change also steers the model less reliably. The model’s earlier replies were written at the previous level, and the model tends to stay consistent with them.

## Availability

Per-message effort is in beta on select models.

### API support

#### [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

* Availability: Available

| Status           | Cloud platforms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Models                                                                                                                                                                                                                                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Beta             | Claude API, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) | [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview)                                                                                                                                                                         |
| Beta<sup>1</sup> | [Amazon Bedrock (bedrock-runtime)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview), [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview) |
| Beta             | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)                                                                                                   | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview), [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)     |
| Beta             | Claude API, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry (hosted on Anthropic)](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)                                                                                                                                                                                                                                               | [Claude Mythos 5.1](https://platform.claude.com/docs/en/models/mythos-5-1/overview)                                                                                                                                                                                                                                                        |
| Beta             | Claude API, [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry (hosted on Anthropic)](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)                                                                                                                                                                                     | [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview)                                                                                                                                                                                                                                                        |

1. Send the beta value in the `anthropic_beta` array of the request body.

#### [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)

* Availability: Not available
* Usage: Instead, set effort for a session by overriding the agent’s model settings.

### Required beta headers

[Beta headers overview](https://platform.claude.com/docs/en/api/beta-headers)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

* `mid-conversation-output-config-2026-07-01`
