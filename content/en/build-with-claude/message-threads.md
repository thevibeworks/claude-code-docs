---
title: Message threads
url: https://platform.claude.com/docs/en/build-with-claude/message-threads
description: Give long-running agents a faster time to first token, especially in long conversations, by sending only the new messages on each request.
featureMetadata:
  status: beta
  betaHeader: message-threads-2026-08-12
  zdr:
    eligibility: not-eligible
    note: A thread's contents (the conversation, system prompt, and tools) are held in memory, encrypted under a server-managed key, never written to durable storage, and deleted no more than 1 hour after the thread's last use. Using this feature does not affect your use of other ZDR eligible features.
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
    Claude API: beta
    Claude Platform on AWS: beta
    Claude Models on Google Cloud (Anthropic managed): beta
    Microsoft Foundry: beta
---

With a message thread, requests are smaller, and time to first token stays lower and steadier as the conversation grows. Threads help most in long agent loops. Without a thread, every turn uploads the whole conversation again, and the API validates and tokenizes all of it again. With a thread, most of that work covers only the new turn.

A message thread keeps a conversation on the server for a short time. You send the full conversation once, with your system prompt and tools. On each later turn, you send only the new messages and the `id` of the previous response. The API rebuilds the conversation before it calls the model. You add one parameter, `thread`, to a [Messages API](https://platform.claude.com/docs/en/api/messages) request. The response is the usual message.

<Note>
  Message threads are different from [session threads](https://platform.claude.com/docs/en/managed-agents/session-threads) in Claude Managed Agents.
</Note>

## How message threads work

* **Create.** Send your first request as you do today, with the full conversation, `system`, and `tools`, and add `"thread": {"type": "create"}`. The API stores the conversation, including Claude’s reply, under the response `id`.
* **Continue.** Send only the messages since the previous response, and add `"thread": {"type": "continue", "previous_message_id": "<previous id>"}`. Leave `system` and `tools` out of the request. The thread keeps the values from the create request. Use each new response `id` for the next turn.
* **Replay.** A thread is best-effort. It expires 5 minutes after its last request, and the API deletes it no more than 1 hour after its last use. Each response that the API stores restarts the 5 minutes. If the API can no longer continue the thread, a continue request returns a 404 error. Send the full conversation again in a new create request, and continue from that response’s `id`. The SDK thread helper does this replay for you (see [How the SDK helper behaves](https://platform.claude.com/docs/en/build-with-claude/message-threads#sdk-helper-handles)). After a response from a fallback model, see [Use fallbacks with a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#fallbacks).

Your application stays the source of truth for the conversation. Keep your own copy of every message, and build the [replay path](https://platform.claude.com/docs/en/build-with-claude/message-threads#recover) from the start. No response, to a create or a continue request, says whether the API stored that turn. You find out on the next continue request. The SDK thread helper keeps this copy in memory while the helper object exists, and saves it nowhere else. If the conversation has to outlive your process, keep your own copy.

## Use a thread with an SDK

The SDK has a thread helper that builds the thread requests for you. Create it with the same fields as a Messages request, then send it one turn at a time. The helper keeps the full conversation in memory.

This example has two turns. The helper creates a thread on the first turn and continues it on the second, and it adds the beta header for you. The top-level `cache_control` is optional. It asks for prompt caching on each turn (see [Prompt caching on a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#prompt-caching)). Without it, each later turn still sends only the new messages, but nothing is cached unless you add cache breakpoints yourself.

<CodeGroup exclude="shell">
  ```python Python
  client = anthropic.Anthropic()

  # Create the helper. This call sends no request.
  thread = client.beta.messages.thread(
      model="claude-opus-5-5",
      max_tokens=1024,
      cache_control={"type": "ephemeral"},
      system="You are a support agent for Acme. Keep replies short.",
  )

  # Turn 1: the helper creates a thread and sends the full conversation
  thread.send({"role": "user", "content": "Hi! I have a question about an order."})

  # Turn 2: the helper continues the thread and sends only the new message
  second = thread.send(
      {"role": "user", "content": "How long does standard shipping usually take?"}
  )

  for block in second.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // Create the helper. This call sends no request.
  const thread = client.beta.messages.thread({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    cache_control: { type: "ephemeral" },
    system: "You are a support agent for Acme. Keep replies short."
  });

  // Turn 1: the helper creates a thread and sends the full conversation
  await thread.send({ role: "user", content: "Hi! I have a question about an order." });

  // Turn 2: the helper continues the thread and sends only the new message
  const second = await thread.send({
    role: "user",
    content: "How long does standard shipping usually take?"
  });

  for (const block of second.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Helpers.Beta;

  AnthropicClient client = new();

  // Create the helper. This call sends no request.
  var thread = client.Beta.Messages.Thread(
      new ThreadCreateParams
      {
          Model = Messages::Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [],
          CacheControl = new(),
          System = "You are a support agent for Acme. Keep replies short.",
      }
  );

  // Turn 1: the helper creates a thread and sends the full conversation
  await thread.Send(
      new BetaUserMessageParam { Content = "Hi! I have a question about an order." }
  );

  // Turn 2: the helper continues the thread and sends only the new message
  var second = await thread.Send(
      new BetaUserMessageParam { Content = "How long does standard shipping usually take?" }
  );

  foreach (var block in second.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()
  ctx := context.Background()

  // Create the helper. This call sends no request.
  thread := client.Beta.Messages.NewThread(anthropic.BetaMessageThreadCreateParams{
  	Model:        anthropic.ModelClaudeOpus5_5,
  	MaxTokens:    1024,
  	CacheControl: anthropic.NewBetaCacheControlEphemeralParam(),
  	System: []anthropic.BetaTextBlockParam{
  		{Text: "You are a support agent for Acme. Keep replies short."},
  	},
  })

  // Turn 1: the helper creates a thread and sends the full conversation
  _, err := thread.Send(ctx, anthropic.BetaMessageThreadSendParams{
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hi! I have a question about an order.")),
  	},
  })
  if err != nil {
  	panic(err)
  }

  // Turn 2: the helper continues the thread and sends only the new message
  second, err := thread.Send(ctx, anthropic.BetaMessageThreadSendParams{
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("How long does standard shipping usually take?")),
  	},
  })
  if err != nil {
  	panic(err)
  }

  for _, block := range second.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  var client = AnthropicOkHttpClient.fromEnv();

  // Create the helper. This call sends no request.
  var thread = client.beta().messages().thread(
      ThreadCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .cacheControl(BetaCacheControlEphemeral.builder().build())
          .system("You are a support agent for Acme. Keep replies short.")
          .build()
  );

  // Turn 1: the helper creates a thread and sends the full conversation
  thread.send("Hi! I have a question about an order.");

  // Turn 2: the helper continues the thread and sends only the new message
  var second = thread.send("How long does standard shipping usually take?");

  second.content().stream()
      .flatMap(block -> block.text().stream())
      .forEach(textBlock -> IO.println(textBlock.text()));
  ```

  ```php PHP
  $client = new Client();

  // Create the helper. This call sends no request.
  $thread = $client->beta->messages->thread(
      maxTokens: 1024,
      model: Model::CLAUDE_OPUS_5_5,
      cacheControl: new BetaCacheControlEphemeral,
      system: 'You are a support agent for Acme. Keep replies short.',
  );

  // Turn 1: the helper creates a thread and sends the full conversation
  $thread->send(['role' => 'user', 'content' => 'Hi! I have a question about an order.']);

  // Turn 2: the helper continues the thread and sends only the new message
  $second = $thread->send(['role' => 'user', 'content' => 'How long does standard shipping usually take?']);

  foreach ($second->content as $block) {
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Create the helper. This call sends no request.
  thread = client.beta.messages.thread(
    model: :"claude-opus-5-5",
    max_tokens: 1024,
    cache_control: {type: "ephemeral"},
    system_: "You are a support agent for Acme. Keep replies short."
  )

  # Turn 1: the helper creates a thread and sends the full conversation
  thread.send_message({role: "user", content: "Hi! I have a question about an order."})

  # Turn 2: the helper continues the thread and sends only the new message
  second = thread.send_message({role: "user", content: "How long does standard shipping usually take?"})

  second.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

## Send the `thread` field yourself

To build thread requests yourself, for example with cURL, the CLI, or an SDK’s usual `create` method, add the `thread` field to each request.

Send the `message-threads-2026-08-12` beta header on every request of a thread.

This example creates a thread on the first turn and continues it on the second. The top-level `cache_control` asks for prompt caching on each turn. It takes effect once the conversation is longer than the [minimum cacheable length](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

<CodeGroup>
  ```bash cURL
  # Turn 1: send the full conversation and create a thread
  curl -sS --fail-with-body https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: message-threads-2026-08-12" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "cache_control": {"type": "ephemeral"},
      "system": "You are a support agent for Acme. Keep replies short.",
      "messages": [{"role": "user", "content": "Hi! I have a question about an order."}],
      "thread": {"type": "create"}
    }'

  # Turn 2: send only the new message. Set message_id to the id of the turn 1 response.
  # Leave out system and tools: the thread keeps them.
  curl -sS --fail-with-body https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: message-threads-2026-08-12" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "cache_control": {"type": "ephemeral"},
      "messages": [{"role": "user", "content": "How long does standard shipping usually take?"}],
      "thread": {"type": "continue", "previous_message_id": "'"$message_id"'"}
    }'
  ```

  ```bash CLI
  # Turn 1: send the full conversation and create a thread
  ant beta:messages create --beta message-threads-2026-08-12 <<'YAML'
  model: claude-opus-5-5
  max_tokens: 1024
  cache_control:
    type: ephemeral
  system: "You are a support agent for Acme. Keep replies short."
  messages:
    - role: user
      content: "Hi! I have a question about an order."
  thread:
    type: create
  YAML

  # Turn 2: send only the new message. Set message_id to the id of the turn 1 response.
  # Leave out system and tools: the thread keeps them.
  ant beta:messages create --beta message-threads-2026-08-12 <<YAML
  model: claude-opus-5-5
  max_tokens: 1024
  cache_control:
    type: ephemeral
  messages:
    - role: user
      content: "How long does standard shipping usually take?"
  thread:
    type: continue
    previous_message_id: $message_id
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  # Turn 1: send the full conversation and create a thread
  first = client.beta.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      cache_control={"type": "ephemeral"},
      system="You are a support agent for Acme. Keep replies short.",
      messages=[{"role": "user", "content": "Hi! I have a question about an order."}],
      thread={"type": "create"},
      betas=["message-threads-2026-08-12"],
  )

  # Turn 2: send only the new message and the id of the turn 1 response.
  # Leave out system and tools: the thread keeps them.
  second = client.beta.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      cache_control={"type": "ephemeral"},
      messages=[
          {"role": "user", "content": "How long does standard shipping usually take?"}
      ],
      thread={"type": "continue", "previous_message_id": first.id},
      betas=["message-threads-2026-08-12"],
  )

  for block in second.content:
      if block.type == "text":
          print(block.text)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // Turn 1: send the full conversation and create a thread
  const first = await client.beta.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    cache_control: { type: "ephemeral" },
    system: "You are a support agent for Acme. Keep replies short.",
    messages: [{ role: "user", content: "Hi! I have a question about an order." }],
    thread: { type: "create" },
    betas: ["message-threads-2026-08-12"]
  });

  // Turn 2: send only the new message and the id of the turn 1 response.
  // Leave out system and tools: the thread keeps them.
  const second = await client.beta.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    cache_control: { type: "ephemeral" },
    messages: [{ role: "user", content: "How long does standard shipping usually take?" }],
    thread: { type: "continue", previous_message_id: first.id },
    betas: ["message-threads-2026-08-12"]
  });

  for (const block of second.content) {
    if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  // Turn 1: send the full conversation and create a thread
  var first = await client.Beta.Messages.Create(
      new()
      {
          Model = Messages::Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          CacheControl = new(),
          System = "You are a support agent for Acme. Keep replies short.",
          Messages =
          [
              new BetaUserMessageParam { Content = "Hi! I have a question about an order." },
          ],
          Thread = new BetaThreadCreateParams(),
          Betas = [AnthropicBeta.MessageThreads2026_08_12],
      }
  );

  // Turn 2: send only the new message and the id of the turn 1 response.
  // Leave out System and Tools: the thread keeps them.
  var second = await client.Beta.Messages.Create(
      new()
      {
          Model = Messages::Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          CacheControl = new(),
          Messages =
          [
              new BetaUserMessageParam { Content = "How long does standard shipping usually take?" },
          ],
          Thread = new BetaThreadContinueParams(first.ID),
          Betas = [AnthropicBeta.MessageThreads2026_08_12],
      }
  );

  foreach (var block in second.Content)
  {
      if (block.TryPickText(out var textBlock))
      {
          Console.WriteLine(textBlock.Text);
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()
  ctx := context.Background()

  // Turn 1: send the full conversation and create a thread
  threadCreate := anthropic.NewBetaThreadCreateParams()
  first, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:        anthropic.ModelClaudeOpus5_5,
  	MaxTokens:    1024,
  	CacheControl: anthropic.NewBetaCacheControlEphemeralParam(),
  	System: []anthropic.BetaTextBlockParam{
  		{Text: "You are a support agent for Acme. Keep replies short."},
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Hi! I have a question about an order.")),
  	},
  	Thread: anthropic.BetaMessageThreadParamUnion{OfCreate: &threadCreate},
  	Betas:  []anthropic.AnthropicBeta{anthropic.AnthropicBetaMessageThreads2026_08_12},
  })
  if err != nil {
  	panic(err)
  }

  // Turn 2: send only the new message and the id of the turn 1 response.
  // Leave out System and Tools: the thread keeps them.
  second, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:        anthropic.ModelClaudeOpus5_5,
  	MaxTokens:    1024,
  	CacheControl: anthropic.NewBetaCacheControlEphemeralParam(),
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("How long does standard shipping usually take?")),
  	},
  	Thread: anthropic.BetaMessageThreadParamOfContinue(first.ID),
  	Betas:  []anthropic.AnthropicBeta{anthropic.AnthropicBetaMessageThreads2026_08_12},
  })
  if err != nil {
  	panic(err)
  }

  for _, block := range second.Content {
  	if textBlock, ok := block.AsAny().(anthropic.BetaTextBlock); ok {
  		fmt.Println(textBlock.Text)
  	}
  }
  ```

  ```java Java
  var client = AnthropicOkHttpClient.fromEnv();

  // Turn 1: send the full conversation and create a thread
  var first = client.beta().messages().create(
      MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .cacheControl(BetaCacheControlEphemeral.builder().build())
          .system("You are a support agent for Acme. Keep replies short.")
          .addUserMessage("Hi! I have a question about an order.")
          .thread(BetaThreadCreateParams.builder().build())
          .addBeta(AnthropicBeta.MESSAGE_THREADS_2026_08_12)
          .build()
  );

  // Turn 2: send only the new message and the id of the turn 1 response.
  // Leave out system and tools: the thread keeps them.
  var second = client.beta().messages().create(
      MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .cacheControl(BetaCacheControlEphemeral.builder().build())
          .addUserMessage("How long does standard shipping usually take?")
          .continueThread(first.id())
          .addBeta(AnthropicBeta.MESSAGE_THREADS_2026_08_12)
          .build()
  );

  second.content().stream()
      .flatMap(block -> block.text().stream())
      .forEach(textBlock -> IO.println(textBlock.text()));
  ```

  ```php PHP
  $client = new Client();

  // Turn 1: send the full conversation and create a thread
  $first = $client->beta->messages->create(
      model: Model::CLAUDE_OPUS_5_5,
      maxTokens: 1024,
      cacheControl: new BetaCacheControlEphemeral,
      system: 'You are a support agent for Acme. Keep replies short.',
      messages: [
          ['role' => 'user', 'content' => 'Hi! I have a question about an order.'],
      ],
      thread: BetaThreadCreateParams::with(),
      betas: ['message-threads-2026-08-12'],
  );

  // Turn 2: send only the new message and the id of the turn 1 response.
  // Leave out system and tools: the thread keeps them.
  $second = $client->beta->messages->create(
      model: Model::CLAUDE_OPUS_5_5,
      maxTokens: 1024,
      cacheControl: new BetaCacheControlEphemeral,
      messages: [
          ['role' => 'user', 'content' => 'How long does standard shipping usually take?'],
      ],
      thread: BetaThreadContinueParams::with(previousMessageID: $first->id),
      betas: ['message-threads-2026-08-12'],
  );

  foreach ($second->content as $block) {
      if ($block instanceof BetaTextBlock) {
          echo $block->text, PHP_EOL;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Turn 1: send the full conversation and create a thread
  first = client.beta.messages.create(
    model: :"claude-opus-5-5",
    max_tokens: 1024,
    cache_control: {type: "ephemeral"},
    system_: "You are a support agent for Acme. Keep replies short.",
    messages: [{role: "user", content: "Hi! I have a question about an order."}],
    thread: {type: "create"},
    betas: ["message-threads-2026-08-12"]
  )

  # Turn 2: send only the new message and the id of the turn 1 response.
  # Leave out system_ and tools: the thread keeps them.
  second = client.beta.messages.create(
    model: :"claude-opus-5-5",
    max_tokens: 1024,
    cache_control: {type: "ephemeral"},
    messages: [{role: "user", content: "How long does standard shipping usually take?"}],
    thread: {type: "continue", previous_message_id: first.id},
    betas: ["message-threads-2026-08-12"]
  )

  second.content.each do |block|
    puts block.text if block.type == :text
  end
  ```
</CodeGroup>

## What to send on each request

| Group       | Fields                                                                                                                                                                                                                                      | Rule                                                                                                                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create-only | `system`, `tools`                                                                                                                                                                                                                           | Send them on the create request only, with any `cache_control` breakpoints on them. Sending either one on a continue request, even as `null`, returns a 400 error.                                                              |
| Fixed       | `model`, `tool_choice`, `thinking`, `mcp_servers` (apart from each server’s authorization token), `context_management`, `output_config`, the `skills` in `container`, the top-level `cache_control`, and the set of `anthropic-beta` values | Send them on every request of the thread, with the same values as on the create request. A different value returns a 400 error with the code `thread_fingerprint_mismatch`, and the error message names the fields that differ. |
| Free        | `max_tokens`, `stop_sequences`, `stream`, `metadata`, `service_tier`, and other fields not named on this page                                                                                                                               | These can change from turn to turn.                                                                                                                                                                                             |

The API does not store MCP server URLs, MCP authorization tokens, or the container `id`. Send `mcp_servers` and `container` on every request that uses them. An MCP authorization token can change between requests.

The SDK thread helper leaves `system` and `tools` out of continue requests for you and sends the fixed fields again on every turn.

If you use [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback), send the `fallbacks` field on every request of a thread or on none. See [Use fallbacks with a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#fallbacks).

To change a create-only or fixed field, start a new thread: send the full conversation in a create request with the new values.

On Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5, changing `system` or `tools` makes the `thinking` and `redacted_thinking` blocks already in the conversation invalid, and the create request can return a 400 error. To avoid it, leave every `thinking` and `redacted_thinking` block out of the conversation you send. The model then answers without that earlier reasoning. See [What counts as an edit](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#what-counts-as-an-edit), [When `prefix_mismatch_behavior` is unset](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#enforcement), and [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior).

Send only the new messages on a continue request. The API doesn’t check them against the messages it already has. A message you send again can appear twice in the conversation, or the request can return an error. For example, a continue request that starts with the previous response returns an error.

The new messages usually start with a `user` message: your next user turn, or the `tool_result` blocks that answer a `tool_use` in the previous response. If a response stops with [`stop_reason: "pause_turn"`](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#pause-turn), resume it with a continue request from that response’s `id` and an empty `messages` list (`"messages": []`). If that request returns a 404 error, replay the full conversation, including the paused response, in a new create request. Don’t send a new `user` message while the turn is paused: the API rejects it. With the SDK thread helper, call `send()` (go, csharp: `Send()`; ruby: `send_message()`) with no messages: the helper sends this request and replays on a 404 error.

A thread is append-only, and each response `id` can be continued once. Always continue from the latest response `id` of the thread. To edit or branch an earlier message, start a new thread with a create request. To replace earlier turns with a summary, see [Compact a conversation](https://platform.claude.com/docs/en/build-with-claude/message-threads#compaction).

## Prompt caching on a thread

A thread does not cache your prompt for you. [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) works as it does without a thread: you choose where the cache breakpoints go.

To cache each turn, send a top-level `cache_control` on every request of the thread, as in the earlier example. The API applies it to the last block of each request’s `messages` that can be cached. Each turn then reads the earlier conversation from the cache and writes the new turn to it. The top-level `cache_control` is a fixed field: send the same value on every request.

You can also place `cache_control` breakpoints on blocks yourself:

* Breakpoints that you send on the create request keep working on every later turn if they are on `tools`, on `system`, or on a message block before the last one. A breakpoint on the last block of a request’s `messages` writes the cache on that request. To cache each new turn, send a breakpoint on every request. A request without a breakpoint might still read part of the conversation from the cache.
* You can’t move or remove a breakpoint after you send it, because a continue request can’t send an earlier message again.
* A request with `thread` can carry at most 4 `cache_control` breakpoints. The top-level `cache_control` counts as one. Breakpoints on the `system` and `tools` of the create request count again on every continue request. Breakpoints on earlier stored messages do not count. One breakpoint too many returns a 400 error with the code `thread_unsupported_request`.
* If you place breakpoints on message blocks yourself, remove them from earlier messages when you replay the conversation in a new create request, and keep one on the last block, so the request stays within the limit of 4.

## Streaming

Threads work with [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming). The response `id` arrives in the `message_start` event, but continue from it only after you receive the `message_stop` event. A continue request sent earlier can return a 404 error.

If the stream of a continue request drops before `message_stop`, send the same continue request again. If that request returns a `thread_already_continued` or `thread_continue_in_flight` error, replay the full conversation in a new create request.

Your connection might have dropped while the server was still generating the response, or after the server saved it. That is why the API can reject the retry. Replaying is always safe.

The SDK thread helper doesn’t retry the continue request after a dropped stream. See [How the SDK helper behaves](https://platform.claude.com/docs/en/build-with-claude/message-threads#sdk-helper-handles).

## Recover when a thread can’t be continued

A continue request returns a 404 error with `error.details.error_code` set to `thread_not_found` when the API can’t continue the thread. The response does not say why. The causes include the following:

* The thread expired.
* The API served the previous turn but did not store it. For example, the API does not store a response that ends in a tool call cut off by `max_tokens`.
* A fallback model wrote the previous response. See [Use fallbacks with a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#fallbacks).
* The previous response is still generating.
* The request comes from a different organization or workspace.
* The request comes from a different user or service account from the one that created the thread. A thread created with a [workspace key (legacy)](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) stays with that key, so use the same key for the whole thread.
* The new messages add something that the stored conversation can’t take. For example, the first image in a conversation that had none can return this error.

To recover, send the full conversation from your own copy in a new create request, with `system` and `tools`. The SDK thread helper sends this create request once by itself, and leaves out the `cache_control` breakpoints of earlier turns when it does. If earlier messages in your copy carry `cache_control` breakpoints, remove them first (see [Prompt caching on a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#prompt-caching)). Then continue from the new response `id`. If a fallback model wrote the previous response, see [Use fallbacks with a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#fallbacks). To rule out the ownership causes, use the same API key and workspace for every request of a thread. On Claude Platform on AWS, sign every request of a thread with credentials for the IAM role or IAM user that created it.

A request for a model that does not exist also returns a 404 error, so check `error.details.error_code` before you replay.

If a continue request still returns a 404 error right after you replay, the API might be unable to store that conversation, for example a very large one. Send it without `thread`. The SDK thread helper does this when you create it with `unsupported_request_behavior` (typescript, java, php: `unsupportedRequestBehavior`; go, csharp: `UnsupportedRequestBehavior`) set to `continue_unthreaded` (ruby: `:continue_unthreaded`; java: `CONTINUE_UNTHREADED`; csharp: `ContinueUnthreaded`; go: `BetaMessageThreadUnsupportedRequestBehaviorContinueUnthreaded`). Otherwise it replays on every turn.

### After a refusal

When a response has `stop_reason: "refusal"`, do not continue the thread. The API might already hold the refused turn, and a continue request can’t remove it. Start a new thread with a create request that leaves out or rephrases the turn that led to the refusal. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback). The SDK thread helper does this for you: it doesn’t keep the refused turn, and its next turn starts a new thread.

### Use fallbacks with a thread

[Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) is available with threads on the Claude API. Decide when you create the thread: send `fallbacks` on every request of the thread, or on none. The value of `fallbacks` can change between requests. A continue request that adds or drops `fallbacks` returns a 400 error with the code `thread_fingerprint_mismatch`.

A thread keeps one model, so the API doesn’t store a turn that a fallback model wrote. You get the response as usual, but you can’t continue from its `id`. After each response, follow these steps:

1. If `stop_reason` is `"refusal"`, follow [After a refusal](https://platform.claude.com/docs/en/build-with-claude/message-threads#after-a-refusal).

2. Otherwise, look for a `fallback_message` entry in `usage.iterations`. On a stream, read it from the final `message_delta` event. If there is none, continue the thread as usual.

3. If there is one, a fallback model wrote the response. Send the full conversation, including that response and your next message, in a new create request. Keep the `server-side-fallback-2026-07-01` beta header on it. Choose one of these two requests:

   * **The same request again.** Keep `model`, `fallbacks`, and your other parameters as they were. If the model you requested answers, the API stores the new thread. If a fallback model answers, the response has a `fallback_message` entry again and the API doesn’t store it, so repeat this step on the next turn. [Sticky routing](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#sticky-routing) might send these requests straight to the fallback model, so every turn might send the full conversation. The SDK thread helper works this way.
   * **A new thread on the fallback model.** Set `model` to the `model` in that `fallback_message` entry, leave `fallbacks` out, and use parameters that this model accepts. The API stores this thread at once, and it stays on the fallback model. The fallback attempt might have run with different settings from the ones you sent, so the API might reject values copied from your first request.

4. Go back to step 1 with the response to that request. When it has no `fallback_message` entry, continue the new thread from its `id`.

[Sticky routing](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#sticky-routing) starts after a request falls back (a create request, or a request without `thread`). For about an hour, it might send later create requests for the same conversation that include `fallbacks` straight to the fallback model, without trying the model you requested. The API stores none of those turns, and each answered one restarts the hour. A continue request never starts this routing and never uses it. Sticky routing doesn’t apply if your organization or workspace uses zero data retention or customer-managed encryption keys.

## Compact a conversation

A thread is append-only, so you can’t replace its earlier turns with a summary. To compact a conversation, start a new thread from the summary. Write the summary in your code, and send it as an ordinary message in a new create request, with `system` and `tools`. [Compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) is not available with threads (see [Features that threads don’t support](https://platform.claude.com/docs/en/build-with-claude/message-threads#unsupported)).

## How the SDK helper behaves

What the helper does for you:

* Adds the `message-threads-2026-08-12` beta header to every request that uses the thread.
* Creates a thread on the first turn and continues it after that, sending only the new messages and leaving out `system` and `tools`.
* Replays the full conversation once in a new create request when a continue request returns `thread_not_found`, `thread_already_continued`, or `thread_continue_in_flight`.
* Resumes a `pause_turn` response when you call `send()` (go, csharp: `Send()`; ruby: `send_message()`) with no messages.
* Starts a new thread after a refusal. You get the `stop_reason: "refusal"` response as usual, but the helper doesn’t keep that turn: it takes back the messages you gave to that call. Messages that you added with `thread.append(...)` (csharp, go: `thread.Append(...)`; php: `$thread->append(...)`), or gave when you created the helper, stay staged. Your next turn sends them with the conversation from before the refused turn, in a new create request. Send a rephrased message, or, if a staged message led to the refusal, start a new thread from the params without it.
* Sends a new create request after a response from a fallback model. When a response has a `fallback_message` entry in `usage.iterations`, the helper keeps the response and sends the full conversation in a new create request on the next turn. It doesn’t wait for a 404 error. That request keeps the `model` and `fallbacks` that you set.
* Leaves out the `cache_control` breakpoints of earlier turns whenever it sends them again, for example in a replay or in the first turn of a fork. Your newest messages, `system`, `tools`, and the top-level `cache_control` go out as you gave them.

What you handle yourself:

* **Fallbacks.** While the API keeps answering from a fallback model, the helper sends the full conversation in a new create request on every turn, because the API stores none of those turns. It goes back to continue requests after a response from the model that you requested. To move the conversation to the fallback model instead, start a new thread from the params with that `model` and without `fallbacks`, as in [Use fallbacks with a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#fallbacks).
* **Dropped streams.** If a stream ends partway through a response, the helper keeps the finished blocks and any text that arrived, and the next turn sends the full conversation in a new create request. The helper doesn’t retry by itself: to re-send the interrupted turn instead, call `send()` (go, csharp: `Send()`; ruby: `send_message()`) with no messages. If the kept part ends in tool calls, answer them in your next message. If you stop reading a stream after it shows `stop_reason: "refusal"`, the helper treats that turn as a refusal.
* **Other errors.** `thread_fingerprint_mismatch` and `thread_unsupported_request` errors reach your code. To carry on without `thread` after a `thread_unsupported_request` error, create the helper with `unsupported_request_behavior` (typescript, java, php: `unsupportedRequestBehavior`; go, csharp: `UnsupportedRequestBehavior`) set to `continue_unthreaded` (ruby: `:continue_unthreaded`; java: `CONTINUE_UNTHREADED`; csharp: `ContinueUnthreaded`; go: `BetaMessageThreadUnsupportedRequestBehaviorContinueUnthreaded`). With that setting, the helper also stops using `thread` when the first continue request after a replay returns `thread_not_found` again. The API might be unable to store that conversation. Without that setting, the helper replays on every turn. A tool runner that creates its own thread uses that setting by default.

The SDK’s beta tool runner also uses a thread by default, which you can turn off when you create the runner.

### Other helper methods

| To do this                                      | Use                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stream a turn                                   | `thread.stream(...)` (csharp: `thread.SendStreaming(...)`; go: `thread.SendStreaming(ctx, params)`; java: `thread.sendStreaming(...)`; php: `$thread->sendStream(...)`)                                                                                                                                                              |
| Finished response of a streamed turn            | `stream.get_final_message()` (typescript: `stream.finalMessage()`; csharp: `thread.LastMessage`; go: `thread.LastMessage()`; java: `thread.lastMessage()`; php: `$thread->lastMessage()`; ruby: `stream.accumulated_message`)                                                                                                        |
| Full conversation                               | `thread.messages` (csharp: `thread.Messages`; go: `thread.Messages()`; java: `thread.messages()`; php: `$thread->messages()`)                                                                                                                                                                                                        |
| Response `id` that the next turn continues from | `thread.previous_message_id` (typescript: `thread.previousMessageId`; csharp: `thread.PreviousMessageID`; go: `thread.PreviousMessageID()`; java: `thread.previousMessageId()`; php: `$thread->previousMessageId()`)                                                                                                                 |
| Add messages without sending                    | `thread.append(...)` (csharp, go: `thread.Append(...)`; php: `$thread->append(...)`)                                                                                                                                                                                                                                                 |
| Change fields for later turns                   | `thread.update(...)` (csharp: `thread.Update(p => p with { ... })`; go: `thread.Params.MaxTokens = ...`; java: `thread.update(b -> ...)`; php: `$thread->update([...])`)                                                                                                                                                             |
| Copy the thread                                 | `thread.fork()` (csharp, go: `thread.Fork()`; php: `$thread->fork()`; ruby: `thread.fork`)                                                                                                                                                                                                                                           |
| Fields and conversation, to start a new thread  | `thread.params` (csharp, go: `thread.Params`; java: `thread.params()`; php: `$thread->params()`)                                                                                                                                                                                                                                     |
| Tool runner on this thread                      | `thread.tool_runner()` (typescript, java: `thread.toolRunner()`; csharp: `thread.ToolRunner(tools)`; go: `thread.NewToolRunner(tools)`; php: `$thread->toolRunner()`; ruby: `thread.tool_runner`)                                                                                                                                    |
| Tool runner without a thread                    | `tool_runner(..., thread=False)` (typescript: `toolRunner({ ..., thread: false })`; csharp: `ToolRunner(parameters, tools, thread: false)`; go: `BetaToolRunnerParams{DisableThread: true}`; java: `ToolRunnerCreateParams.builder().thread(false)`; php: `toolRunner(..., thread: false)`; ruby: `tool_runner(..., thread: false)`) |

**Streaming.** The helper records the response when the stream reaches `message_stop`, so read the stream to its end. If you stop reading early, end the stream so that the thread is free for the next turn:

* Python: leave the `with` block.
* TypeScript: leave the loop or call `abort()`.
* Go: call `Close`.
* Java and Ruby: call `close()`.
* C#: dispose of the enumerator. Leaving `await foreach` does this.
* PHP: call `close()`.

In C#, the request goes out when you start to read the stream.

In C#, Go, Java, and PHP, after a refusal `thread.LastMessage` (go: `thread.LastMessage()`; java: `thread.lastMessage()`; php: `$thread->lastMessage()`) still returns the previous turn’s response, or nothing on a first turn. Read the refusal from the stream’s events.

**Changing fields.** An update sends nothing and applies to every later turn. Once a thread has a response, the helper refuses a turn that changes `system` or `tools`, and the API rejects a change to any other fixed field (see [What to send on each request](https://platform.claude.com/docs/en/build-with-claude/message-threads#what-to-send)). To change one of these fields, start a new thread from the params, or fork the thread and update the fork before its first turn.

**Forking.** A fork copies the conversation, the fields, and the request options, and sends nothing. Its first turn sends the full conversation in a new create request, and the two threads are independent after that. A fork always starts from the whole conversation, not from an earlier response.

**Params.** The params hold the helper’s fields and the full conversation. Pass them to the method that creates a helper to start a new thread, for example with a different `system` (see [What to send on each request](https://platform.claude.com/docs/en/build-with-claude/message-threads#what-to-send)), or with `messages` cut back to drop later turns. A thread that you start from the params sends every message as you gave it, `cache_control` breakpoints included, so keep within the limit of 4 (see [Prompt caching on a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#prompt-caching)). Except in Ruby, the params leave out the request options, so pass those again.

**Structured output.** Give the output format when you create the helper. A later turn can’t change it. How you get the parsed result depends on the SDK:

* Python and TypeScript: call `thread.parse(...)`.
* C#: create the helper with `client.Beta.Messages.Thread<T>(...)`.
* Go: `Send` unmarshals into the struct that `Params.OutputConfig.Format.Schema` points to.
* Java: create the helper with `thread(...)` and `outputConfig(MyClass.class)`.
* PHP: `send()` sets `parsed` on the text blocks when `outputConfig` names a model class.
* Ruby: pass `output_config: {format: MyModel}` to `thread(...)`, then read `reply.parsed_output`.

## Errors

The API returns the errors in this table before the model runs. The request uses no tokens, and the thread and its expiry time do not change. `error.type` is `invalid_request_error` for the 400 errors and `not_found_error` for the 404 error.

| Status | `error_code`                  | Meaning                                                                                                                              | What to do                                                                                                 |
| ------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| 404    | `thread_not_found`            | The API can’t continue the thread.                                                                                                   | Send the full conversation in a new create request.                                                        |
| 400    | `thread_fingerprint_mismatch` | A fixed field differs from the value stored with the thread. The error message names the fields.                                     | Keep the fixed fields the same, or start a new thread to change one.                                       |
| 400    | `thread_already_continued`    | Each response `id` can be continued once.                                                                                            | Continue from the latest response `id` of the thread. If your client never received that response, replay. |
| 400    | `thread_continue_in_flight`   | Another continue request from this response `id` is still running. This is usually your own earlier attempt.                         | Let it finish and continue from its response `id`, or replay.                                              |
| 400    | `thread_unsupported_request`  | The request uses a feature or an organization setting that threads don’t support. `error.details.unsupported` names it when present. | Remove that feature from the request, or send the full conversation without `thread`.                      |

Some 400 errors for thread requests carry no `error_code`, for example a continue request without `previous_message_id`, or one that includes `system` or `tools`.

The following example shows an error body:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "thread: a maximum of 4 blocks with cache_control may be provided when `thread` is set. Found 5.",
    "details": {
      "error_code": "thread_unsupported_request",
      "unsupported": ["cache_control"]
    }
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

## Features that threads don’t support

Threads don’t support these features:

* [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing). A request item that includes `thread` ends with an `invalid_request_error` in the batch results.
* [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting). A token counting request that includes `thread` returns a 400 error. Count the full conversation instead, with `system` and `tools`.
* [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction). [Compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) is not available with threads. A request that includes `thread` returns a 400 error if it sets the `compaction` parameter, or if it sends a `compaction` block with the `compact-2026-09-04` beta header. See [Compact a conversation](https://platform.claude.com/docs/en/build-with-claude/message-threads#compaction).
* [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing), except `clear_thinking_20251015` with `keep: "all"`.
* Organizations that have [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness) enabled.
* Organizations that have [Inference hooks](https://platform.claude.com/docs/en/manage-claude/inference-hooks) turned on.

The API rejects most requests that threads don’t support with a 400 error and the code `thread_unsupported_request`. When `error.details.unsupported` is present, it holds one of these values:

| Value                | Meaning                                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `context_management` | The request uses context management or compaction that threads don’t support.                                                                                                    |
| `cache_control`      | The request has more than 4 `cache_control` breakpoints. See [Prompt caching on a thread](https://platform.claude.com/docs/en/build-with-claude/message-threads#prompt-caching). |
| `fallbacks`          | The request sets `fallbacks`, and your organization can’t use `fallbacks` with threads.                                                                                          |
| `hipaa`              | Your organization has HIPAA readiness enabled.                                                                                                                                   |
| `inference_hooks`    | Your organization has Inference hooks turned on.                                                                                                                                 |

The API can add values to this list. If you get a value that you don’t recognize, send the full conversation without `thread`. A request that meets several of these conditions gets an error that names only one.

## Limitations

* There is no API to list, read, or delete a thread.
* Threads are available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), Claude Models on Google Cloud (Anthropic managed), and [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).

## Pricing and rate limits

Threads do not change pricing or [rate limits](https://platform.claude.com/docs/en/api/rate-limits).

## Data retention

Message threads are not ZDR eligible. Using this feature does not affect your use of other ZDR eligible features. The API holds a thread in memory, encrypted under a server-managed key, never writes it to durable storage, and deletes it no more than 1 hour after its last use.

A thread holds the conversation that the API sends to the model, the `system` and `tools` from the create request, and a fingerprint of the fixed fields, which it uses to check later requests. It holds files by reference, so keep every file the conversation uses available while you use the thread.

For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).

## See also

* [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
* [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming)
* [Errors](https://platform.claude.com/docs/en/api/errors)

## Availability

Message threads are in beta on every model.

### API support

#### [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

* Availability: Available

| Status | Cloud platforms                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Beta   | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) |

### Required beta headers

[Beta headers overview](https://platform.claude.com/docs/en/api/beta-headers)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

* `message-threads-2026-08-12`

### Data handling

[Data handling overview](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)

| Item    | Zero data retention                                                                                                                                                                                                                                                                                                                                                                                      | HIPAA        |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Status  | Not eligible                                                                                                                                                                                                                                                                                                                                                                                             | Not eligible |
| Details | A thread’s contents (the conversation, system prompt, and tools) are held in memory, encrypted under a server-managed key, never written to durable storage, and deleted no more than 1 hour after the thread’s last use. Using this feature does not affect your use of other ZDR eligible features. [Learn more](https://platform.claude.com/docs/en/build-with-claude/message-threads#data-retention) | —            |

Applicable endpoints:

* `/v1/messages` with `thread`
