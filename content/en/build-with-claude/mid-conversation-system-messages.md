---
title: Mid-conversation system messages and tool changes
url: https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages
description: Change system instructions or tool availability partway through a conversation without invalidating the cached prefix that came before them.
---

<Note>
  To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
</Note>

System instructions normally live in the top-level `system` field, ahead of every message in the conversation. That position is great for [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching): the system prompt is part of the stable prefix, so subsequent turns hit the cache. It is a poor position for instructions you only discover you need partway through a session, because editing the top-level `system` field changes the very beginning of the prompt and invalidates the cache for everything that follows.

Mid-conversation system messages close that gap. You append a `{"role": "system"}` message at the point in the conversation where the new instruction becomes relevant, instead of editing the top-level `system` field. The cached prefix stays the same, so the next request still reads it from cache, and the new instruction is still applied as a system instruction rather than as ordinary user text.

<Note>
  Mid-conversation system messages are available on the Claude API, [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), and [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai).

  This feature is available on Claude Fable 5.1, [Claude Mythos 5.1](https://anthropic.com/glasswing), Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), Claude Opus 4.8, and Claude Opus 5. No beta header is required for mid-conversation system messages. This feature is not available on Claude Sonnet 5. Use the top-level `system` field there instead.

  [Mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) are in beta and require the `mid-conversation-tool-changes-2026-07-01` beta header. They are available on the same models, on the Claude API, Amazon Bedrock, and Google Cloud.

  [Turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) (`clear_at`) are in beta and require the `mid-conversation-system-clear-at-2026-08-21` beta header, on the same models and platforms as mid-conversation system messages.
</Note>

## Mid-conversation tool changes

The `tools` array sits even earlier in the hashed request prefix than the top-level `system` field, so editing it invalidates the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for the entire conversation. Mid-conversation tool changes are the tools counterpart to mid-conversation system messages. Instead of fixing the tool list for the lifetime of the conversation, you change which tools are offered to the model between turns: declare the full tool set in `tools` up front, then use `tool_addition` and `tool_removal` blocks to offer a tool to the model, or withdraw it, from a specific point in the conversation onward. The `tools` array itself never changes, so the cached prefix stays intact.

`tool_addition` and `tool_removal` are content blocks in the `content` array of a `role: "system"` message, and they can be mixed with `text` blocks in the same message. The message follows the same placement rules as any mid-conversation system message (see [Limitations](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)), and the change applies from that point in the conversation onward. Each block's `tool` field references a tool rather than defining one: `{"type": "tool_reference", "name": "..."}` names a tool declared in the request's `tools` array, and [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) tools can be referenced individually with `mcp_tool_reference` (`server_name` and `name`) or as a whole toolset with `mcp_toolset_reference` (`server_name`). Referencing a name that is not declared in `tools` returns a 400 error.

Every tool declared in `tools` is offered to the model from the start of the conversation unless it is declared with `defer_loading: true`, which keeps it withheld until a `tool_addition` block surfaces it. `tool_addition` also re-offers a tool that an earlier `tool_removal` withdrew.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mid-conversation-tool-changes-2026-07-01" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 1024,
      "tools": [
        {
          "name": "get_weather",
          "description": "Get the current weather for a location.",
          "input_schema": {
            "type": "object",
            "properties": {
              "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Say OK."
        },
        {
          "role": "system",
          "content": [
            {
              "type": "tool_removal",
              "tool": {"type": "tool_reference", "name": "get_weather"}
            }
          ]
        }
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta mid-conversation-tool-changes-2026-07-01 \
    --transform 'content.#(type=="text").text' --raw-output <<'YAML'
  model: claude-opus-5
  max_tokens: 1024
  tools:
    - name: get_weather
      description: Get the current weather for a location.
      input_schema:
        type: object
        properties:
          location:
            type: string
            description: City name
        required:
          - location
  messages:
    - role: user
      content: Say OK.
    - role: system
      content:
        - type: tool_removal
          tool:
            type: tool_reference
            name: get_weather
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-opus-5",
      max_tokens=1024,
      betas=["mid-conversation-tool-changes-2026-07-01"],
      # The full tool set is declared up front and never changes, so the
      # cached prefix stays intact.
      tools=[
          {
              "name": "get_weather",
              "description": "Get the current weather for a location.",
              "input_schema": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string", "description": "City name"},
                  },
                  "required": ["location"],
              },
          },
      ],
      messages=[
          {
              "role": "user",
              "content": "Say OK.",
          },
          # Withdraw get_weather from this point onward. The block references
          # the tool by name instead of editing `tools`, so earlier turns stay
          # byte-identical and the cache still hits.
          {
              "role": "system",
              "content": [
                  {
                      "type": "tool_removal",
                      "tool": {"type": "tool_reference", "name": "get_weather"},
                  },
              ],
          },
      ],
  )

  for block in response.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: "claude-opus-5",
    max_tokens: 1024,
    betas: ["mid-conversation-tool-changes-2026-07-01"],
    // The full tool set is declared up front and never changes, so the
    // cached prefix stays intact.
    tools: [
      {
        name: "get_weather",
        description: "Get the current weather for a location.",
        input_schema: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "City name"
            }
          },
          required: ["location"]
        }
      }
    ],
    messages: [
      { role: "user", content: "Say OK." },
      // Withdraw get_weather from this point onward. The block references the
      // tool by name instead of editing `tools`, so earlier turns stay
      // byte-identical and the cache still hits.
      {
        role: "system",
        content: [
          {
            type: "tool_removal",
            tool: { type: "tool_reference", name: "get_weather" }
          }
        ]
      }
    ]
  });

  for (const block of response.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using Messages = Anthropic.Models.Messages;

  AnthropicClient client = new();

  var response = await client.Beta.Messages.Create(new MessageCreateParams
  {
      Model = Messages::Model.ClaudeOpus5,
      MaxTokens = 1024,
      Betas = ["mid-conversation-tool-changes-2026-07-01"],
      // The full tool set is declared up front and never changes, so the
      // cached prefix stays intact.
      Tools =
      [
          new BetaTool
          {
              Name = "get_weather",
              Description = "Get the current weather for a location.",
              InputSchema = new InputSchema
              {
                  Properties = new Dictionary<string, JsonElement>
                  {
                      ["location"] = JsonSerializer.SerializeToElement(new { type = "string", description = "City name" }),
                  },
                  Required = ["location"],
              },
          },
      ],
      Messages =
      [
          new() { Role = Role.User, Content = "Say OK." },
          // Withdraw get_weather from this point onward. The block references
          // the tool by name instead of editing `Tools`, so earlier turns stay
          // byte-identical and the cache still hits.
          new()
          {
              Role = Role.System,
              Content = new(
              [
                  new BetaRequestToolRemovalBlock
                  {
                      Tool = new BetaToolChangeToolReference { Name = "get_weather" },
                  },
              ]),
          },
      ],
  });

  foreach (var block in response.Content)
  {
      if (block.TryPickText(out var text))
      {
          Console.WriteLine(text.Text);
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5,
  	MaxTokens: 1024,
  	Betas:     []anthropic.AnthropicBeta{"mid-conversation-tool-changes-2026-07-01"},
  	// The full tool set is declared up front and never changes, so the
  	// cached prefix stays intact.
  	Tools: []anthropic.BetaToolUnionParam{
  		{OfTool: &anthropic.BetaToolParam{
  			Name:        "get_weather",
  			Description: anthropic.String("Get the current weather for a location."),
  			InputSchema: anthropic.BetaToolInputSchemaParam{
  				Properties: map[string]any{
  					"location": map[string]any{
  						"type":        "string",
  						"description": "City name",
  					},
  				},
  				Required: []string{"location"},
  			},
  		}},
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Say OK.")),
  		// Withdraw get_weather from this point onward. The block references
  		// the tool by name instead of editing Tools, so earlier turns stay
  		// byte-identical and the cache still hits.
  		{
  			Role: anthropic.BetaMessageParamRoleSystem,
  			Content: []anthropic.BetaContentBlockParamUnion{
  				anthropic.NewBetaToolRemovalBlock(anthropic.BetaToolChangeToolReferenceParam{
  					Name: "get_weather",
  				}),
  			},
  		},
  	},
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
  import com.anthropic.models.beta.messages.BetaContentBlockParam;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaMessageParam;
  import com.anthropic.models.beta.messages.BetaRequestToolRemovalBlock;
  import com.anthropic.models.beta.messages.BetaTool;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  // ...
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      // The full tool set is declared up front and never changes, so the
      // cached prefix stays intact.
      BetaTool weatherTool = BetaTool.builder()
          .name("get_weather")
          .description("Get the current weather for a location.")
          .inputSchema(BetaTool.InputSchema.builder()
              .properties(BetaTool.InputSchema.Properties.builder()
                  .putAdditionalProperty("location", JsonValue.from(Map.of(
                      "type", "string",
                      "description", "City name")))
                  .build())
              .addRequired("location")
              .build())
          .build();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5)
          .maxTokens(1024)
          .addBeta("mid-conversation-tool-changes-2026-07-01")
          .addTool(weatherTool)
          .addUserMessage("Say OK.")
          // Withdraw get_weather from this point onward. The block references
          // the tool by name instead of editing `tools`, so earlier turns stay
          // byte-identical and the cache still hits.
          .addMessage(BetaMessageParam.builder()
              .role(BetaMessageParam.Role.SYSTEM)
              .contentOfBetaContentBlockParams(List.of(
                  BetaContentBlockParam.ofToolRemoval(BetaRequestToolRemovalBlock.builder()
                      .referenceTool("get_weather")
                      .build())))
              .build())
          .build();

      BetaMessage response = client.beta().messages().create(params);
      response.content().stream()
          .flatMap(block -> block.text().stream())
          .forEach(textBlock -> IO.println(textBlock.text()));
  ```

  ```php PHP
  $client = new Client();

  $response = $client->beta->messages->create(
      model: 'claude-opus-5',
      maxTokens: 1024,
      betas: ['mid-conversation-tool-changes-2026-07-01'],
      // The full tool set is declared up front and never changes, so the
      // cached prefix stays intact.
      tools: [
          [
              'name' => 'get_weather',
              'description' => 'Get the current weather for a location.',
              'input_schema' => [
                  'type' => 'object',
                  'properties' => [
                      'location' => [
                          'type' => 'string',
                          'description' => 'City name',
                      ],
                  ],
                  'required' => ['location'],
              ],
          ],
      ],
      messages: [
          ['role' => 'user', 'content' => 'Say OK.'],
          // Withdraw get_weather from this point onward. The block references
          // the tool by name instead of editing `tools`, so earlier turns stay
          // byte-identical and the cache still hits.
          [
              'role' => 'system',
              'content' => [
                  [
                      'type' => 'tool_removal',
                      'tool' => ['type' => 'tool_reference', 'name' => 'get_weather'],
                  ],
              ],
          ],
      ],
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
    model: "claude-opus-5",
    max_tokens: 1024,
    betas: ["mid-conversation-tool-changes-2026-07-01"],
    # The full tool set is declared up front and never changes, so the
    # cached prefix stays intact.
    tools: [
      {
        name: "get_weather",
        description: "Get the current weather for a location.",
        input_schema: {
          type: "object",
          properties: {
            location: { type: "string", description: "City name" }
          },
          required: ["location"]
        }
      }
    ],
    messages: [
      { role: "user", content: "Say OK." },
      # Withdraw get_weather from this point onward. The block references
      # the tool by name instead of editing `tools`, so earlier turns stay
      # byte-identical and the cache still hits.
      {
        role: "system",
        content: [
          {
            type: "tool_removal",
            tool: { type: "tool_reference", name: "get_weather" }
          }
        ]
      }
    ]
  )

  response.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

Mid-conversation tool changes are in beta. To use them, include the beta header `mid-conversation-tool-changes-2026-07-01` in your requests.

## When to use a mid-conversation system message

[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) hashes the request prefix in order: `tools`, then `system`, then `messages`. A cache hit requires the prefix to match a recent request exactly, byte for byte, up to the cache breakpoint.

That ordering means the top-level `system` field sits near the very start of the hashed prefix. Any change to it, even appending a sentence, produces a different hash, and the request misses the cache for the system prompt and every cached message after it.

Mid-conversation system messages let you add the instruction at the **end** of the message history instead. Everything before the new instruction is unchanged, so the existing cache entry still matches, and only the new message is processed as fresh input.

A few situations where this matters:

* **Mid-session policy or persona changes.** A long agentic session needs a new constraint ("from now on, write all SQL as parameterized queries") after dozens of cached turns. Adding it to the top-level `system` field would re-process the entire history.
* **Per-turn context that must be authoritative.** You want to inject a freshness note, a session deadline, or a tool-availability change with system-level weight, and it changes too often to live in the cached prefix.
* **Per-turn reminders that shouldn't pile up.** A harness nudges the model after each batch of tool results ("request independent reads together", "the user hasn't heard from you in a while") and wants the model to see only the newest copy. A [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) renders for one turn and then costs nothing, without deleting anything from the history.
* **State changes your application observes.** Your application notices something Claude should treat as an operator-level fact: files changed on disk, the user toggled an auto-approve setting, available tools changed, or the remaining token budget dropped below a threshold.
* **User input that should not interrupt an agentic loop.** A user types a follow-up while Claude is still executing tools for the previous request. Relaying it as a system message after the next tool result lets Claude fold the new input into the work it is already doing, instead of treating it as a fresh request to switch to. See [Placement after tool results](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#placement-after-tool-results).
* **Mode switches that grant standing permissions.** A session-level mode can use a mid-conversation system message to grant standing consent to an expensive capability, such as automatically launching multiagent workflows, with a short refresher every several turns and an exit notice when the mode is turned off. For a worked example, see [Build an orchestration mode](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example).

In all of these cases you could put the instruction in a regular `user` message, and Claude does follow instructions that arrive in user turns. The difference is priority: a `user` message is treated as coming from the end user, while a `system` message is treated as coming from you, the application operator. When the two conflict, system instructions take precedence, so use the `system` role for operator-level facts and constraints that should hold even if the end user asks for something different. A mid-conversation system message keeps that operator-level priority without paying the cache-miss cost of editing the top-level `system` field.

## How it works

Add a message with `"role": "system"` to the `messages` array. Use a plain string or content blocks for `content`, the same as a `user` or `assistant` turn. The instruction applies from that point in the conversation onward. When instructions conflict, later system messages take precedence over earlier ones, and mid-conversation system messages take precedence over the top-level `system` field for the turns that follow them.

You can still set the top-level `system` field for instructions that should apply to the entire conversation. Reserve mid-conversation system messages for instructions that only become relevant later, or that you want to add without invalidating the cached prefix.

A `role: "system"` message can also carry `output_config.effort` to change the [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level from the next `user` turn on. This is in beta on Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5 on the Claude API and requires the `mid-conversation-output-config-2026-07-01` beta header. See [Per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta).

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 1024,
      "cache_control": {"type": "ephemeral"},
      "system": "You are a code review assistant. Be concise.",
      "messages": [
        {
          "role": "user",
          "content": "Review process() in utils.py for performance issues."
        },
        {
          "role": "assistant",
          "content": "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list."
        },
        {
          "role": "user",
          "content": "Now review the calling code that invokes process()."
        },
        {
          "role": "system",
          "content": "From now on, every suggestion must include explicit type annotations."
        }
      ]
    }'
  ```

  ```bash CLI
  ant messages create --transform 'content.#(type=="text").text' --raw-output <<'YAML'
  model: claude-opus-5
  max_tokens: 1024
  cache_control:
    type: ephemeral
  system: You are a code review assistant. Be concise.
  messages:
    - role: user
      content: Review process() in utils.py for performance issues.
    - role: assistant
      content: >-
        The list comprehension is fine for small inputs. For large inputs,
        consider a generator to avoid materializing the full list.
    - role: user
      content: Now review the calling code that invokes process().
    - role: system
      content: From now on, every suggestion must include explicit type annotations.
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-5",
      max_tokens=1024,
      # Automatic prompt caching: each request caches the conversation so far,
      # and the next request reads the unchanged prefix from cache.
      cache_control={"type": "ephemeral"},
      system="You are a code review assistant. Be concise.",
      messages=[
          {
              "role": "user",
              "content": "Review process() in utils.py for performance issues.",
          },
          {
              "role": "assistant",
              "content": "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.",
          },
          {
              "role": "user",
              "content": "Now review the calling code that invokes process().",
          },
          # The reviewer realizes mid-session that all suggestions must
          # also pass the team's strict typing policy. Appending the
          # instruction here keeps earlier turns byte-identical, so the
          # prefix cached by the previous request is still read from cache.
          {
              "role": "system",
              "content": "From now on, every suggestion must include explicit type annotations.",
          },
      ],
  )

  for block in response.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-5",
    max_tokens: 1024,
    // Automatic prompt caching: each request caches the conversation so far,
    // and the next request reads the unchanged prefix from cache.
    cache_control: { type: "ephemeral" },
    system: "You are a code review assistant. Be concise.",
    messages: [
      {
        role: "user",
        content: "Review process() in utils.py for performance issues."
      },
      {
        role: "assistant",
        content:
          "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list."
      },
      {
        role: "user",
        content: "Now review the calling code that invokes process()."
      },
      // The reviewer realizes mid-session that all suggestions must also pass
      // the team's strict typing policy. Appending the instruction here keeps
      // earlier turns byte-identical, so the prefix cached by the previous
      // request is still read from cache.
      {
        role: "system",
        content: "From now on, every suggestion must include explicit type annotations."
      }
    ]
  });

  const textBlock = response.content.find(
    (block): block is Anthropic.TextBlock => block.type === "text"
  );
  console.log(textBlock?.text);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus5,
      MaxTokens = 1024,
      // Automatic prompt caching: each request caches the conversation so far,
      // and the next request reads the unchanged prefix from cache.
      CacheControl = new CacheControlEphemeral(),
      System = "You are a code review assistant. Be concise.",
      Messages =
      [
          new()
          {
              Role = Role.User,
              Content = "Review process() in utils.py for performance issues."
          },
          new()
          {
              Role = Role.Assistant,
              Content = "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list."
          },
          new()
          {
              Role = Role.User,
              Content = "Now review the calling code that invokes process()."
          },
          // The reviewer realizes mid-session that all suggestions must also pass
          // the team's strict typing policy. Appending the instruction here keeps
          // earlier turns byte-identical, so the prefix cached by the previous
          // request is still read from cache.
          new()
          {
              Role = Role.System,
              Content = "From now on, every suggestion must include explicit type annotations."
          }
      ]
  };

  var response = await client.Messages.Create(parameters);
  Console.WriteLine(response);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5,
  	MaxTokens: 1024,
  	// Automatic prompt caching: each request caches the conversation so far,
  	// and the next request reads the unchanged prefix from cache.
  	CacheControl: anthropic.NewCacheControlEphemeralParam(),
  	System: []anthropic.TextBlockParam{
  		{Text: "You are a code review assistant. Be concise."},
  	},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Review process() in utils.py for performance issues.")),
  		anthropic.NewAssistantMessage(anthropic.NewTextBlock("The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.")),
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Now review the calling code that invokes process().")),
  		// The reviewer realizes mid-session that all suggestions must also
  		// pass the team's strict typing policy. Appending the instruction
  		// here keeps earlier turns byte-identical, so the prefix cached by
  		// the previous request is still read from cache.
  		{
  			Role: anthropic.MessageParamRoleSystem,
  			Content: []anthropic.ContentBlockParamUnion{
  				anthropic.NewTextBlock("From now on, every suggestion must include explicit type annotations."),
  			},
  		},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  for _, block := range response.Content {
  	if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  import com.anthropic.models.messages.CacheControlEphemeral;
  // ...
  import com.anthropic.models.messages.MessageParam;
  // ...
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5)
          .maxTokens(1024)
          // Automatic prompt caching: each request caches the conversation so far,
          // and the next request reads the unchanged prefix from cache.
          .cacheControl(CacheControlEphemeral.builder().build())
          .system("You are a code review assistant. Be concise.")
          .addUserMessage("Review process() in utils.py for performance issues.")
          .addAssistantMessage("The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.")
          .addUserMessage("Now review the calling code that invokes process().")
          // The reviewer realizes mid-session that all suggestions must also pass
          // the team's strict typing policy. Appending the instruction here keeps
          // earlier turns byte-identical, so the prefix cached by the previous
          // request is still read from cache.
          .addMessage(MessageParam.builder()
              .role(MessageParam.Role.SYSTEM)
              .content("From now on, every suggestion must include explicit type annotations.")
              .build())
          .build();

      Message response = client.messages().create(params);
      response.content().stream()
          .flatMap(block -> block.text().stream())
          .forEach(textBlock -> IO.println(textBlock.text()));
  ```

  ```php PHP
  use Anthropic\Messages\CacheControlEphemeral;
  // ...
  $client = new Client();

  $response = $client->messages->create(
      maxTokens: 1024,
      messages: [
          ['role' => 'user', 'content' => 'Review process() in utils.py for performance issues.'],
          ['role' => 'assistant', 'content' => 'The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.'],
          ['role' => 'user', 'content' => 'Now review the calling code that invokes process().'],
          // The reviewer realizes mid-session that all suggestions must also pass
          // the team's strict typing policy. Appending the instruction here keeps
          // earlier turns byte-identical, so the prefix cached by the previous
          // request is still read from cache.
          ['role' => 'system', 'content' => 'From now on, every suggestion must include explicit type annotations.']
      ],
      model: 'claude-opus-5',
      // Automatic prompt caching: each request caches the conversation so far,
      // and the next request reads the unchanged prefix from cache.
      cacheControl: CacheControlEphemeral::with(),
      system: 'You are a code review assistant. Be concise.',
  );

  foreach ($response->content as $block) {
      if ($block->type === 'text') {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.messages.create(
    model: "claude-opus-5",
    max_tokens: 1024,
    # Automatic prompt caching: each request caches the conversation so far,
    # and the next request reads the unchanged prefix from cache.
    cache_control: { type: "ephemeral" },
    system: "You are a code review assistant. Be concise.",
    messages: [
      { role: "user", content: "Review process() in utils.py for performance issues." },
      { role: "assistant", content: "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list." },
      { role: "user", content: "Now review the calling code that invokes process()." },
      # The reviewer realizes mid-session that all suggestions must also pass
      # the team's strict typing policy. Appending the instruction here keeps
      # earlier turns byte-identical, so the prefix cached by the previous
      # request is still read from cache.
      { role: "system", content: "From now on, every suggestion must include explicit type annotations." }
    ]
  )

  response.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

This example enables [automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) with the top-level `cache_control` field. Prompt caching is opt-in: if a request has no `cache_control` field (automatic or an [explicit breakpoint](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints)), nothing is cached and every request pays the regular input token price for the full conversation. With caching enabled, appending the system message leaves the already-cached turns unchanged, so the request that carries the new instruction still reads them from cache instead of processing them again. Caching also requires the conversation to meet the [minimum cacheable prompt length](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations); an example as short as this one falls below it, so `cache_creation_input_tokens` and `cache_read_input_tokens` stay at 0 until the conversation grows.

A mid-conversation system message must immediately follow a `user` turn (or an `assistant` turn ending in a server tool result), and must either be the last entry in `messages` or be immediately followed by an `assistant` turn. A `user` message that carries `tool_result` blocks counts: in an agentic loop you can place the system message right after the tool results, before Claude's next turn. Any other position, including between an `assistant` `tool_use` block and the `tool_result` that answers it, returns a 400 error.

### Placement after tool results

In an [agentic loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), the system message goes after the `user` message that delivers the tool results. This is also where your application can relay input that the user typed while Claude was working, so the new context is absorbed without restarting the turn:

```json
[
  { "role": "user", "content": "Run the test suite and fix any failures." },
  {
    "role": "assistant",
    "content": [{ "type": "tool_use", "id": "toolu_01", "name": "run_tests", "input": {} }]
  },
  {
    "role": "user",
    "content": [
      { "type": "tool_result", "tool_use_id": "toolu_01", "content": "12 passed, 0 failed" }
    ]
  },
  {
    "role": "system",
    "content": "The user sent the following message while you were working: also update the changelog before you finish."
  }
]
```

Phrase the system content as context rather than as a command that overrides the user. State the fact ("new input arrived from the user: X", "the remaining token budget is now Y") and let Claude act on it. Claude is trained to resist instructions that appear to work against the user, and that protection still applies to the system role, so language such as "ignore what the user said" is less effective than stating what changed.

This pattern is for relaying input from the conversation's own end user. Do not use it to pass tool output, retrieved documents, or other third-party content; keep that content in `tool_result` blocks (see [Limitations](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)).

### Turn-scoped system messages

To scope a `role: "system"` message to the current turn, set its `clear_at` field. It takes one of two values:

* `"never"` (the default): the message renders at its position on every request that includes it. Omitting the field is identical.
* `"next_user_message"`: the message is **turn-scoped**. Its text renders only while no `role: "user"` message comes after it in `messages`. A user message that carries only `tool_result` blocks counts as a user message here. Once a later user message exists, the message is **cleared**: it stays in the array but renders nothing and costs no input tokens, on that request and every later one.

Turn-scoped system messages are in beta. Include the [beta header](https://platform.claude.com/docs/en/api/beta-headers) `mid-conversation-system-clear-at-2026-08-21`. Without it, `clear_at` is rejected as an unknown field.

```json
{
  "role": "system",
  "clear_at": "next_user_message",
  "content": "First privately list what you need next; then request every item that doesn't depend on another's result in this one response."
}
```

The main use is a per-turn reminder in a tool loop. Append the reminder after the `tool_result` message each time you want the model to see it, and leave every earlier copy where it is. The model sees only the copies that come after the last user message, so the reminder never piles up. Nothing earlier in `messages` changes, so the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) keeps matching. On Claude Fable 5.1 this also keeps later [thinking blocks valid](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation): deleting an earlier reminder would change the conversation before those blocks and fail the conversation check, while a cleared message stays in the array and leaves that conversation unchanged.

The following request is a later step of an agent loop. `messages[3]` rendered on the earlier request, when it was the last message in the array. Once `messages[5]` (a later user message) exists, `messages[3]` is cleared: the cleared message stays in the array, so the conversation before the thinking block in `messages[4]` is unchanged, but the model no longer sees its text. `messages[6]` and `messages[7]` both render, in order.

```json
{
  "model": "claude-fable-5-1",
  "max_tokens": 16000,
  "messages": [
    { "role": "user", "content": "Fix the failing test." },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "", "signature": "..." },
        {
          "type": "tool_use",
          "id": "toolu_01",
          "name": "read_file",
          "input": { "path": "test_auth.py" }
        }
      ]
    },
    {
      "role": "user",
      "content": [{ "type": "tool_result", "tool_use_id": "toolu_01", "content": "..." }]
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "Request independent reads in one turn."
    },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "", "signature": "..." },
        {
          "type": "tool_use",
          "id": "toolu_02",
          "name": "read_file",
          "input": { "path": "auth.py" }
        },
        {
          "type": "tool_use",
          "id": "toolu_03",
          "name": "read_file",
          "input": { "path": "tokens.py" }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        { "type": "tool_result", "tool_use_id": "toolu_02", "content": "..." },
        {
          "type": "tool_result",
          "tool_use_id": "toolu_03",
          "content": "...",
          "cache_control": { "type": "ephemeral" }
        }
      ]
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "Request independent reads in one turn."
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "The shell exited with status 137."
    }
  ]
}
```

Rules for turn-scoped messages:

* **Re-send cleared messages verbatim.** A cleared message is still part of the conversation history. Rebuilding it from current state (a fresh token count, a timestamp), dropping it as redundant, or changing its `clear_at` value is an edit to an earlier message. The prompt cache misses from that point, and on Claude Fable 5.1 every thinking block produced after it fails the [conversation check](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation).
* **Text only.** `content` is one or more `text` blocks (or a string). `tool_addition` and `tool_removal` blocks return a 400 error on a turn-scoped message, and so does `output_config`. Use a separate `role: "system"` message without `clear_at` for those.
* **No `cache_control` on its blocks.** A cleared message is never part of a cache key, so a breakpoint on it could never match. Put the breakpoint on the last block of the preceding user turn instead, as the example does. The top-level [automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) field skips turn-scoped messages when it picks a breakpoint. On the request that clears a message, the reusable cached prefix ends at the user turn before it, so only the one assistant turn between that message and the new user message is reprocessed.
* **Placement rules still apply**, cleared or not. A turn-scoped message must follow a `user` turn (or an `assistant` turn ending in a server tool result) and precede an `assistant` turn or end the array, like any mid-conversation system message. One that ends the array always renders. One followed directly by another `user` message is a 400 error, not a cleared message: put all of a tool round's results in one user message and the reminders after it.
* **Assistant turns don't clear it.** A prefilled or [paused](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#pause-turn) assistant turn after the message, or a server-side tool loop, adds no user message, so the message still renders on that continuation. To keep a reminder in view through a client-side tool loop, append it again after each `tool_result` message.
* **Token counting follows what renders.** A cleared message adds nothing to `usage.input_tokens` or to a [token count](https://platform.claude.com/docs/en/build-with-claude/token-counting).
* **Imported history.** In a transcript you construct in one step (few-shot examples, a migrated conversation), a turn-scoped message that already has an assistant turn and a user message after it is cleared from the first request and never renders. That is the right state for a per-turn reminder you are carrying over. Leave `clear_at` unset only on a message the model should see on every request.

The validation errors are:

```text wrap
messages.3.clear_at: Extra inputs are not permitted
messages.3.clear_at: clear_at is only permitted on role 'system' messages
messages.3.clear_at: Input should be 'next_user_message' or 'never'
messages.3: a turn-scoped system message supports text blocks only (clear_at: 'next_user_message')
messages.3: output_config is not permitted on a turn-scoped system message (clear_at: 'next_user_message')
messages.3.content.0: cache_control is not permitted on a turn-scoped system message (clear_at: 'next_user_message')
```

The first is the error returned without the beta header. On Amazon Bedrock and Google Cloud, pass the beta value as described in [Beta headers](https://platform.claude.com/docs/en/api/beta-headers).

Through the SDKs, set `clear_at` on the `role: "system"` entry in `messages` and send the beta header. The following example appends a turn-scoped reminder after the user turn; on the next request, once a later user message exists, the reminder stays in the array but no longer renders:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: mid-conversation-system-clear-at-2026-08-21" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-fable-5-1",
      "max_tokens": 4096,
      "messages": [
        {"role": "user", "content": "Draft a short status update on the database migration for the team channel."},
        {"role": "system", "clear_at": "next_user_message", "content": "The reader is on call: keep this reply under 50 words."}
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta mid-conversation-system-clear-at-2026-08-21 \
    --transform 'content.#(type=="text").text' --raw-output <<'YAML'
  model: claude-fable-5-1
  max_tokens: 4096
  messages:
    - role: user
      content: Draft a short status update on the database migration for the team channel.
    # Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
    - role: system
      clear_at: next_user_message
      content: "The reader is on call: keep this reply under 50 words."
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-fable-5-1",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Draft a short status update on the database migration for the team channel.",
          },
          # Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
          {
              "role": "system",
              "clear_at": "next_user_message",
              "content": "The reader is on call: keep this reply under 50 words.",
          },
      ],
      betas=["mid-conversation-system-clear-at-2026-08-21"],
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
    messages: [
      {
        role: "user",
        content: "Draft a short status update on the database migration for the team channel."
      },
      // Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
      {
        role: "system",
        clear_at: "next_user_message",
        content: "The reader is on call: keep this reply under 50 words."
      }
    ],
    betas: ["mid-conversation-system-clear-at-2026-08-21"]
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
      Messages =
      [
          new() { Role = Role.User, Content = "Draft a short status update on the database migration for the team channel." },
          // Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
          new()
          {
              Role = Role.System,
              ClearAt = ClearAt.NextUserMessage,
              Content = "The reader is on call: keep this reply under 50 words.",
          },
      ],
      Betas = [AnthropicBeta.MidConversationSystemClearAt2026_08_21],
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
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Draft a short status update on the database migration for the team channel.")),
  		// Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
  		{
  			Role:    anthropic.BetaMessageParamRoleSystem,
  			ClearAt: anthropic.BetaMessageParamClearAtNextUserMessage,
  			Content: []anthropic.BetaContentBlockParamUnion{anthropic.NewBetaTextBlock("The reader is on call: keep this reply under 50 words.")},
  		},
  	},
  	Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaMidConversationSystemClearAt2026_08_21},
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
  import com.anthropic.models.beta.messages.MessageCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model("claude-fable-5-1")
          .maxTokens(4096L)
          .addBeta(AnthropicBeta.MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21)
          .addUserMessage("Draft a short status update on the database migration for the team channel.")
          // Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
          .addMessage(BetaMessageParam.builder()
              .role(BetaMessageParam.Role.SYSTEM)
              .clearAt(BetaMessageParam.ClearAt.NEXT_USER_MESSAGE)
              .content("The reader is on call: keep this reply under 50 words.")
              .build())
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
  use Anthropic\Client;

  $client = new Client();

  $response = $client->beta->messages->create(
      model: 'claude-fable-5-1',
      maxTokens: 4096,
      messages: [
          BetaMessageParam::with(role: 'user', content: 'Draft a short status update on the database migration for the team channel.'),
          // Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
          BetaMessageParam::with(
              role: 'system',
              clearAt: 'next_user_message',
              content: 'The reader is on call: keep this reply under 50 words.',
          ),
      ],
      betas: [AnthropicBeta::MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21],
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
    messages: [
      {role: "user", content: "Draft a short status update on the database migration for the team channel."},
      # Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
      {role: "system", clear_at: :next_user_message, content: "The reader is on call: keep this reply under 50 words."}
    ],
    betas: [Anthropic::AnthropicBeta::MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21]
  )

  response.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

## Combining with prompt caching

Mid-conversation system messages and [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) are designed to be used together:

* **Enable caching explicitly.** Caching only happens when the request includes `cache_control`, either the top-level [automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) field or an [explicit breakpoint](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints) on a content block. A mid-conversation system message does not create a cache entry on its own, and without caching enabled there are no savings to preserve.
* **Cache the stable prefix as usual.** Place `cache_control` on the last block that stays the same across requests, whether that is the end of the top-level `system` field, the end of your tool definitions, or a stable point in the message history.
* **Append the system message after the breakpoint.** Because it comes after the cached prefix, it does not change the prefix hash and the cache still hits.
* **A mid-conversation system message is itself cacheable.** Once it is in the conversation, it becomes part of the stable history. On the next turn you can move your cache breakpoint past it (or rely on [automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) to do so) and the system message is read from cache like any other turn.

Avoid editing or removing a mid-conversation system message that has already been sent. Like any other change to earlier messages, that invalidates the cache from that point forward. On Claude Fable 5.1 it also invalidates the [thinking blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation) in every later assistant turn. For guidance that should apply to one turn only, use a [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) and leave it in place. If the instruction needs to evolve, append a new system message rather than rewriting the old one. Consecutive system messages are accepted and treated as a single system section, which follows the same placement rule as a whole.

## Limitations

* **Not for the first message.** A `system` message that carries content cannot be the first entry in `messages`. Use the top-level `system` field for instructions that apply from the very start.
* **Placement is constrained.** A `system` message that carries content (`text`, `tool_addition`, or `tool_removal` blocks) must immediately follow a `user` turn (including a `user` turn that carries `tool_result` blocks) or an `assistant` turn ending in a server tool result, and must precede an `assistant` turn or end the array. It cannot sit between a `tool_use` block and its `tool_result`. Placing it elsewhere returns a 400 error. One exception: `tool_addition` and `tool_removal` blocks are not accepted immediately after a [paused](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#pause-turn) `assistant` turn (one ending in a server tool result), though `text` blocks are; resume the paused turn first, then send the tool change in the next `system` message. A message with empty `content` that only sets [`output_config.effort`](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) renders nothing at its position and is accepted anywhere in `messages`, including first or between an `assistant` turn and a `user` turn. Consecutive `system` messages are judged together, so adding a text-carrying message next to an effort-only one makes the whole group follow the content rule.
* **Turn-scoped messages are text-only and re-sent verbatim.** A `clear_at: "next_user_message"` message carries no `tool_addition`, `tool_removal`, `output_config`, or `cache_control`, and once cleared it must stay in `messages` byte-for-byte on later requests. See [Turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages).
* **Not a place for untrusted content.** Claude treats system content as operator instructions and follows it. Do not place text from outside the conversation, such as raw tool output, retrieved documents, or web content, directly in a system message; doing so gives that text operator-level authority. Keep that data in `tool_result` blocks and continue to follow [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).

## Related

<CardGroup cols={2}>
  <Card title="Prompt caching" icon="bolt" href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">
    How caching works, where to place breakpoints, and how to read cache usage fields.
  </Card>

  <Card title="Cache diagnostics" icon="magnifying-glass" href="https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics">
    Find out exactly where two requests diverged when a cache hit you expected does not happen.
  </Card>

  <Card title="Using the Messages API" icon="message" href="https://platform.claude.com/docs/en/build-with-claude/working-with-messages">
    Message structure, multi-turn conversations, and the `system` field.
  </Card>

  <Card title="Prompting best practices" icon="text" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">
    Writing effective prompts and system instructions.
  </Card>

  <Card title="Tool use with Claude" icon="wrench" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview">
    How `tool_use` and `tool_result` blocks are structured in the `messages` array.
  </Card>
</CardGroup>
