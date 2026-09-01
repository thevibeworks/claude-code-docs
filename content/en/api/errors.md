---
title: Claude API errors
url: https://platform.claude.com/docs/en/api/errors
description: Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDKs' typed exceptions.
---

## HTTP errors

The API follows a predictable HTTP error code format:

* 400 - `invalid_request_error`: There was an issue with the format or content of your request. This error type may also be used for other 4XX status codes not listed in this section. The API also returns a 400 when usage reaches an organization or workspace [spend limit you set](https://platform.claude.com/docs/en/api/rate-limits#setting-your-own-spend-limit), except limits on the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), which can return a 429 instead.

* 401 - `authentication_error`: There's an issue with your API key (for example, it's malformed, revoked, or expired; see [Key expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration)). On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.

* 402 - `billing_error`: There's an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you're using Claude Platform on AWS.

* 403 - `permission_error`: Your API key does not have permission to use the specified resource. Check your organization's access and workspace settings in the [Claude Console](https://platform.claude.com).

* 404 - `not_found_error`: The requested resource was not found. Check the endpoint path and any resource IDs in the request URL.

* 409 - `conflict_error`: The request conflicts with the current state of a resource. For example, the resource was modified concurrently, or a value that must be unique is already in use. Resolve the conflict, then retry the request.

* 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](https://platform.claude.com/docs/en/api/errors#request-size-limits) for per-endpoint maximums.

* 429 - `rate_limit_error`: Your organization has hit a [rate limit](https://platform.claude.com/docs/en/api/rate-limits), reached its usage tier's monthly spend cap, or reached a spend limit on the Claude Code workspace. A tier spend-cap 429 has no `retry-after` header and keeps failing until access resumes; see [Reaching your spend cap](https://platform.claude.com/docs/en/api/rate-limits#reaching-your-spend-cap) for how to recognize it.

* 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems. Retry the request with exponential backoff; if the error persists, contact support with the [request ID](https://platform.claude.com/docs/en/api/errors#request-id).

* 504 - `timeout_error`: The request timed out while processing. Consider using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) for long-running requests. See [Long requests](https://platform.claude.com/docs/en/api/errors#long-requests) for more options.

* 529 - `overloaded_error`: The API is temporarily overloaded.

  <Warning>
    529 errors can occur when the API experiences high traffic across all users.

    In rare cases, if your organization has a sharp increase in usage, you might see 429 errors because of acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.
  </Warning>

The official SDKs automatically retry transient failures (such as connection errors, rate limits, and 5xx server errors) with exponential backoff, twice by default, honoring the `retry-after` header when present. Each SDK client accepts a maximum-retries option to configure or disable this behavior.

When receiving a [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) response over server-sent events (SSE), an error can occur after the API returns a 200 response. In that case, error handling doesn't follow these standard mechanisms. See [Error events](https://platform.claude.com/docs/en/build-with-claude/streaming#error-events) for the shape of mid-stream errors.

## Request size limits

The API enforces request size limits:

| Endpoint type                                                                       | Maximum request size |
| ----------------------------------------------------------------------------------- | -------------------- |
| Messages API                                                                        | 32 MB                |
| Token Counting API                                                                  | 32 MB                |
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | 256 MB               |
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)            | 500 MB               |

If you exceed these limits, you'll receive a 413 `request_too_large` error. On the direct Claude API, Cloudflare returns this error before the request reaches the API servers.

## Error shapes

The API always returns errors as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:

```json JSON
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

In accordance with the [versioning](https://platform.claude.com/docs/en/api/versioning) policy, the values within these objects may expand, and it is possible that the `type` values will grow over time.

## SDK error types

The official SDKs raise typed exceptions for these errors instead of returning raw JSON, and the class names and namespaces differ by language. For example, a 404 surfaces as `anthropic.NotFoundError` in Python, `Anthropic::Errors::NotFoundError` in Ruby, `com.anthropic.errors.NotFoundException` in Java, and as a single `*anthropic.Error` value (branch on `StatusCode`) in Go. Catch the SDK's typed classes rather than string-matching error messages, handling the most specific classes first. Each SDK page documents its full exception hierarchy:

* [Python](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-errors) · [TypeScript](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript#handling-errors) · [C#](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/csharp#error-handling) · [Go](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go#error-handling) · [Java](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java#error-handling) · [PHP](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#error-handling) · [Ruby](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby#handling-errors)

## Request ID

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. The same identifier appears as the `request_id` field in [error response bodies](https://platform.claude.com/docs/en/api/errors#error-shapes). When contacting support about a specific request, include this ID to help quickly resolve your issue.

On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.

The Python and TypeScript SDKs expose the request ID as a `_request_id` property on top-level response objects. The C#, Go, Java, and PHP SDKs expose it through their raw-response accessors, and the Ruby SDK through [middleware](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware). The same mechanisms, along with `with_raw_response` in Python and `.withResponse()` in TypeScript, read any other [response header](https://platform.claude.com/docs/en/api/overview#response-headers) too, such as `anthropic-organization-id` and [`anthropic-workspace-id`](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response). On Claude Platform on AWS, use the raw-response accessor to read the AWS request ID (`x-amzn-requestid`) as well:

<CodeGroup>
  ```bash cURL
  # Print the response headers (including request-id); discard the body
  curl -sS -D - -o /dev/null https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }'
  ```

  ```bash CLI
  # The request-id header is printed to stderr with --debug:
  ant --debug messages create \
    --model claude-sonnet-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-sonnet-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  print(f"Request ID: {message._request_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-sonnet-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  });
  console.log("Request ID:", message._request_id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  using var response = await client.WithRawResponse.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeSonnet5,
      MaxTokens = 1024,
      Messages = [new() { Role = Role.User, Content = "Hello, Claude" }]
  });
  Console.WriteLine($"Request ID: {response.RequestID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  var response *http.Response
  _, err := client.Messages.New(
  	context.Background(),
  	anthropic.MessageNewParams{
  		Model:     anthropic.ModelClaudeSonnet5,
  		MaxTokens: 1024,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  		},
  	},
  	option.WithResponseInto(&response),
  )
  if err != nil {
  	panic(err)
  }

  fmt.Println("Request ID:", response.Header.Get("request-id"))
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.http.HttpResponseFor;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      HttpResponseFor<Message> response = client.messages().withRawResponse().create(
          MessageCreateParams.builder()
              .model(Model.CLAUDE_SONNET_5)
              .maxTokens(1024)
              .addUserMessage("Hello, Claude")
              .build()
      );

      IO.println("Request ID: " + response.requestId().orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $response = $client->messages->raw->create([
      'model' => 'claude-sonnet-5',
      'maxTokens' => 1024,
      'messages' => [['role' => 'user', 'content' => 'Hello, Claude']],
  ]);
  echo 'Request ID: ' . $response->getHeaderLine('request-id') . "\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Read response headers in per-request middleware, which receives the
  # raw HTTP response before the SDK parses it
  request_id = nil
  read_request_id = lambda do |request, call_next|
    response = call_next.call(request)
    # Keys in response.headers are lowercase
    request_id = response.headers["request-id"]
    response
  end

  client.messages.create(
    model: Anthropic::Model::CLAUDE_SONNET_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    request_options: { middleware: [read_request_id] }
  )
  puts "Request ID: #{request_id}"
  ```

  ```python Python (Claude Platform on AWS)
  from anthropic import AnthropicAWS

  client = AnthropicAWS(aws_region="us-west-2")

  response = client.messages.with_raw_response.create(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  print(f"AWS request ID: {response.headers.get('x-amzn-requestid')}")
  message = response.parse()
  print(f"Anthropic request ID: {message._request_id}")
  ```

  ```typescript TypeScript (Claude Platform on AWS)
  import AnthropicAws from "@anthropic-ai/aws-sdk";

  const client = new AnthropicAws({ awsRegion: "us-west-2" });

  const { response: raw, request_id } = await client.messages
    .create({
      model: "claude-opus-4-8",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    })
    .withResponse();
  console.log("AWS request ID:", raw.headers.get("x-amzn-requestid"));
  console.log("Anthropic request ID:", request_id);
  ```
</CodeGroup>

For Claude Platform on AWS request-ID examples in other languages, see [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids).

## Long requests

<Warning>
  Consider using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create) for long-running requests, especially those over 10 minutes.
</Warning>

Avoid setting a large `max_tokens` value without using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create):

* Some networks may drop idle connections after a variable period of time, which can cause the request to fail or time out without receiving a response from Anthropic.
* Networks differ in reliability. The [Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create) can help you manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

The [SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) validate that your non-streaming Messages API requests are not expected to exceed a 10-minute timeout. They also set a socket option for TCP keep-alive.

If you don't need to process events incrementally, the SDKs can consume the stream for you and return the complete `Message` object, identical to what a non-streaming call returns:

<CodeGroup>
  ```bash cURL
  # Raw SSE output requires handling events; there is no single-command way
  # to accumulate the final message with curl. Use the SDK examples instead.
  ```

  ```bash CLI
  # The CLI streams events; --format jsonl emits one event per line
  ant messages create --stream --format jsonl <<'YAML'
  model: claude-sonnet-5
  max_tokens: 128000
  messages:
    - role: user
      content: Write a detailed analysis...
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  with client.messages.stream(
      max_tokens=128000,
      messages=[{"role": "user", "content": "Write a detailed analysis..."}],
      model="claude-sonnet-5",
  ) as stream:
      message = stream.get_final_message()

  print(next(block.text for block in message.content if block.type == "text"))
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const stream = client.messages.stream({
    max_tokens: 128000,
    messages: [{ role: "user", content: "Write a detailed analysis..." }],
    model: "claude-sonnet-5"
  });

  const message = await stream.finalMessage();
  const textBlock = message.content.find((block) => block.type === "text");
  if (textBlock && textBlock.type === "text") {
    console.log(textBlock.text);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeSonnet5,
      MaxTokens = 128000,
      Messages = [new() { Role = Role.User, Content = "Write a detailed analysis..." }]
  };

  var message = await client.Messages.CreateStreaming(parameters).Aggregate();
  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  stream := client.Messages.NewStreaming(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeSonnet5,
  	MaxTokens: 128000,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Write a detailed analysis...")),
  	},
  })

  message := anthropic.Message{}
  for stream.Next() {
  	event := stream.Current()
  	if err := message.Accumulate(event); err != nil {
  		log.Fatal(err)
  	}
  }
  if err := stream.Err(); err != nil {
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
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.helpers.MessageAccumulator;
  import com.anthropic.models.messages.ContentBlock;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_SONNET_5)
          .maxTokens(128000L)
          .addUserMessage("Write a detailed analysis...")
          .build();

      MessageAccumulator accumulator = MessageAccumulator.create();
      try (var streamResponse = client.messages().createStreaming(params)) {
          streamResponse.stream().forEach(accumulator::accumulate);
      }

      Message message = accumulator.message();
      message.content().stream()
              .filter(ContentBlock::isText)
              .findFirst()
              .flatMap(ContentBlock::text)
              .ifPresent(textBlock -> IO.println(textBlock.text()));
  }
  ```

  ```php PHP
  use Anthropic\Lib\Streaming\MessageAccumulator;

  $client = new Client();

  $stream = $client->messages->createStream(
      model: 'claude-sonnet-5',
      maxTokens: 128000,
      messages: [['role' => 'user', 'content' => 'Write a detailed analysis...']],
  );

  $accumulator = MessageAccumulator::forMessages();
  foreach ($stream as $event) {
      $accumulator->accumulate($event);
  }

  echo array_find($accumulator->message()->content, static fn ($block): bool => $block->type === 'text')->text;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.stream(
    model: "claude-sonnet-5",
    max_tokens: 128000,
    messages: [{ role: "user", content: "Write a detailed analysis..." }]
  ).accumulated_message

  puts message.content.find { it.type == :text }.text
  ```
</CodeGroup>

See [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for more details.

## Common validation errors

### Prefill not supported

Claude 4.6 and later models and [Claude Mythos Preview](https://anthropic.com/glasswing) do not support prefilling assistant messages. Sending a request with a prefilled last assistant message to any of these models returns a 400 `invalid_request_error`:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "This model does not support assistant message prefill. The conversation must end with a user message."
  }
}
```

Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) on models that support it, system prompt instructions, or [`output_config.format`](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-outputs) instead.

### Thinking blocks cannot be modified

If the most recent assistant message contains `thinking` or `redacted_thinking` blocks that were edited, reordered, filtered out, or reconstructed before being sent back to the API, the request returns a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

```text wrap
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.
```

With tool use, every `thinking` and `redacted_thinking` block from the assistant turn must be passed back exactly as received, including blocks whose `thinking` field is empty. Pass thinking blocks back unchanged, and if your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. See [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-blocks-modified), [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#preserving-thinking-blocks), and [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-thinking).

### Extended thinking not supported

Claude 4.7 and later models have removed extended thinking. Sending `thinking: {"type": "enabled"}` to any of these models returns a 400 `invalid_request_error`:

```text wrap
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) instead. [Migrating to adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#migrating-to-adaptive-thinking) shows the parameter mapping, and [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-enabled) covers the symptom-first fix.

### Adaptive thinking not supported

Models that support only extended thinking (Claude 4.5 and earlier models) reject `thinking: {"type": "adaptive"}` with a 400 `invalid_request_error`:

```text wrap
adaptive thinking is not supported on this model
```

Use `thinking: {"type": "enabled", "budget_tokens": N}` on these models; see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for the configuration and [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-adaptive) for the symptom-first fix.

### Thinking cannot be disabled

On Claude Fable 5.1, [Claude Mythos 5.1](https://anthropic.com/glasswing), Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), and [Claude Mythos Preview](https://anthropic.com/glasswing), thinking is always on. Sending `thinking: {"type": "disabled"}` to any of these models returns a 400 `invalid_request_error`:

```text wrap
"thinking.type.disabled" is not supported for this model. Thinking defaults to adaptive mode when not specified; use "thinking.type.enabled" with "budget_tokens" for extended thinking.
```

On Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5, the error message's own suggestion of `"thinking.type.enabled"` is also rejected. Omit the `thinking` parameter and the request runs with adaptive thinking. To keep thinking content out of responses without turning thinking off, set `display: "omitted"` on the thinking configuration. See [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-disabled).

### Forced tool use not supported

Claude Fable 5.1 and [Claude Mythos 5.1](https://anthropic.com/glasswing) don't support forced tool use. Sending `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` to either model, including on the [token counting endpoint](https://platform.claude.com/docs/en/build-with-claude/token-counting), returns a 400 `invalid_request_error`:

```text wrap
tool_choice: type "tool" and "any" are not supported for this model.
```

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are accepted. Use `auto` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) to keep tool inputs schema-valid, or [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) when you need the response itself in a fixed JSON shape. See [Forcing tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).

### Thinking block no longer matches the conversation

On Claude Fable 5.1, the API accepts a replayed thinking block only while the `system` prompt, `tools`, and messages that preceded it are unchanged. For new accounts created on or after August 31, 2026, and for any request that sets `thinking.block_binding.prefix_mismatch_behavior` to `"error"`, a replayed block whose earlier history changed is rejected with a 400 `invalid_request_error` (with `"drop_block"`, the API drops the block and the request succeeds). The message starts with the position of the first failing block:

```text wrap
messages.{i}.content.{j}: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```

Without the `thinking-binding-controls-2026-08-01` beta header the message also names that header. Keep the conversation history append-only, or send the beta header with `prefix_mismatch_behavior: "drop_block"` to drop the block and continue. A block from a model the target model can't read is dropped rather than rejected. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-in-conversation) and [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-block-signature).

Sending `thinking.block_binding` without the `thinking-binding-controls-2026-08-01` [beta header](https://platform.claude.com/docs/en/api/beta-headers) returns a 400 `invalid_request_error` whose message ends in:

```text wrap
block_binding: Extra inputs are not permitted
```

Add the header, or remove the field.

### Outbound web identity federation disabled (Claude Platform on AWS)

If every request to [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once per AWS account. See [Enable outbound web identity federation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#enable-outbound-web-identity-federation) for details.

## Next steps

<CardGroup cols={3}>
  <Card title="Troubleshooting thinking" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting">
    Symptom-first fixes for thinking configuration 400 errors, empty thinking blocks, and `max_tokens` stops.
  </Card>

  <Card title="Rate limits" icon="gauge" href="https://platform.claude.com/docs/en/api/rate-limits">
    To mitigate misuse and manage capacity on the API, limits are in place on how much an organization can use the Claude API.
  </Card>

  <Card title="Streaming messages" icon="lightning" href="https://platform.claude.com/docs/en/build-with-claude/streaming">
    Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
  </Card>
</CardGroup>
