---
title: Set up OpenTelemetry with the Claude SDK
url: https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk
description: Trace the Claude SDK's requests and tool uses in Python, TypeScript, C#, Go, Java, PHP, or Ruby, and send the spans to your observability platform.
featureMetadata:
  topic:
    title: OpenTelemetry
    url: https://platform.claude.com/docs/en/manage-claude/opentelemetry
  status: beta
  supportedPlatforms:
    Claude API: beta
    Claude Platform on AWS: beta
    Amazon Bedrock: beta
    Claude Models on Google Cloud (Google managed): beta
    Microsoft Foundry: beta
  rows:
    - label: Works with
      value: Messages API, Claude Managed Agents
---

With OpenTelemetry, the Claude SDK can emit a span for each request that it sends and each tool use that the [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) runs. You can view these spans in your observability platform, nested in your own traces.

The SDK emits spans in your application. Your application’s OpenTelemetry exporter sends them to your observability platform.

<Note>
  During the beta, the SDK options and the span schema can change in ways that break your code, your queries, or your dashboards. For example, a new version of the SDK can rename a span, an attribute, an option, or an environment variable. Pin the SDK version in your dependencies to choose when you adopt the changes.
</Note>

## 1. Install the SDK

Install or upgrade to the latest version of the Claude SDK:

<Tabs>
  <Tab title="Python">
    ```bash
    pip install --upgrade anthropic
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    pip install opentelemetry-sdk
    ```
  </Tab>

  <Tab title="TypeScript">
    ```bash
    npm install @anthropic-ai/sdk@latest
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    npm install @opentelemetry/sdk-trace-node
    ```
  </Tab>

  <Tab title="C#">
    ```bash
    dotnet add package Anthropic
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    dotnet add package OpenTelemetry.Exporter.Console
    ```
  </Tab>

  <Tab title="Go">
    ```bash
    go get github.com/anthropics/anthropic-sdk-go/v2@latest
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    go get go.opentelemetry.io/otel/sdk go.opentelemetry.io/otel/exporters/stdout/stdouttrace
    ```
  </Tab>

  <Tab title="Java">
    Add the Claude SDK to your dependencies, or update it to at least the following version if your build file already declares it:

    <CodeGroup exclude="shell, python, typescript, csharp, go, php, ruby">
      ```kotlin Gradle
      implementation("com.anthropic:anthropic-java:3.3.0")
      ```

      ```xml Maven
      <dependency>
          <groupId>com.anthropic</groupId>
          <artifactId>anthropic-java</artifactId>
          <version>3.3.0</version>
      </dependency>
      ```
    </CodeGroup>

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans. Add `io.opentelemetry:opentelemetry-sdk` and `io.opentelemetry:opentelemetry-exporter-logging` to your build, both at the latest version on [Maven Central](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-sdk).
  </Tab>

  <Tab title="PHP">
    ```bash
    composer require "anthropic-ai/sdk" "guzzlehttp/guzzle:^7"
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    composer require open-telemetry/sdk
    ```
  </Tab>

  <Tab title="Ruby">
    If your `Gemfile` doesn’t list `anthropic` yet, add the gem:

    ```bash
    bundle add anthropic
    ```

    If your `Gemfile` already lists `anthropic`, update the gem:

    ```bash
    bundle update anthropic
    ```

    If your application doesn’t use the OpenTelemetry SDK yet, install it with a console exporter, which you use in the next step to print spans:

    ```bash
    bundle add opentelemetry-sdk
    ```
  </Tab>
</Tabs>

## 2. Register a tracer provider

A *tracer provider* is the OpenTelemetry object that creates spans and passes them to your exporter. The SDK uses the tracer provider that your application registers, so your SDK calls stay the same. Register it before the first call that you want to trace.

The following example registers a tracer provider that prints each span to the console and then makes one call. Use it to see spans before you connect an observability platform:

<CodeGroup exclude="shell">
  ```python Python
  from anthropic import Anthropic
  from opentelemetry import trace
  from opentelemetry.sdk.trace import TracerProvider
  from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

  # Register a tracer provider that prints each span to the console.
  provider = TracerProvider()
  provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
  trace.set_tracer_provider(provider)

  client = Anthropic()

  message = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  print(message.content)
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";
  import {
    ConsoleSpanExporter,
    NodeTracerProvider,
    SimpleSpanProcessor
  } from "@opentelemetry/sdk-trace-node";

  // Register a tracer provider that prints each span to the console.
  const provider = new NodeTracerProvider({
    spanProcessors: [new SimpleSpanProcessor(new ConsoleSpanExporter())]
  });
  // register() also installs the context manager, which lets the SDK spans nest under your spans.
  provider.register();

  const client = new Anthropic();

  const message = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  });
  console.log(message.content);
  ```

  ```csharp C#
  using Anthropic;
  using Anthropic.Models.Messages;
  using OpenTelemetry;
  using OpenTelemetry.Trace;

  // Register a tracer provider that prints each span to the console.
  using var tracerProvider = Sdk.CreateTracerProviderBuilder()
      .AddSource("com.anthropic.sdk.csharp*")
      .AddConsoleExporter()
      .Build();

  AnthropicClient client = new();

  var message = await client.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      MaxTokens = 1024,
      Messages = [new UserMessageParam { Content = "Hello, Claude" }],
  });
  Console.WriteLine(message);
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"

  	"github.com/anthropics/anthropic-sdk-go/v2"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/exporters/stdout/stdouttrace"
  	"go.opentelemetry.io/otel/propagation"
  	sdktrace "go.opentelemetry.io/otel/sdk/trace"
  )

  func main() {
  	ctx := context.Background()

  	// Register a tracer provider that prints each span to the console.
  	exporter, err := stdouttrace.New(stdouttrace.WithPrettyPrint())
  	if err != nil {
  		panic(err)
  	}
  	provider := sdktrace.NewTracerProvider(sdktrace.WithSyncer(exporter))
  	defer provider.Shutdown(ctx)
  	otel.SetTracerProvider(provider)
  	// OpenTelemetry for Go doesn't register a propagator by default, so
  	// register the W3C trace context propagator.
  	otel.SetTextMapPropagator(propagation.TraceContext{})

  	client := anthropic.NewClient()

  	message, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  		Model:     anthropic.ModelClaudeOpus5_5,
  		MaxTokens: 1024,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  		},
  	})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(message.Content)
  }
  ```

  ```java Java
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import io.opentelemetry.api.trace.propagation.W3CTraceContextPropagator;
  import io.opentelemetry.context.propagation.ContextPropagators;
  import io.opentelemetry.exporter.logging.LoggingSpanExporter;
  import io.opentelemetry.sdk.OpenTelemetrySdk;
  import io.opentelemetry.sdk.trace.SdkTracerProvider;
  import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;

  void main() {
      // Register a tracer provider that writes each span to the log.
      var tracerProvider = SdkTracerProvider.builder()
          .addSpanProcessor(SimpleSpanProcessor.create(LoggingSpanExporter.create()))
          .build();
      OpenTelemetrySdk.builder()
          .setTracerProvider(tracerProvider)
          // OpenTelemetry for Java doesn't register a propagator when you build
          // it in code, so register the W3C trace context propagator.
          .setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))
          .buildAndRegisterGlobal();

      var client = AnthropicOkHttpClient.fromEnv();

      var message = client.messages().create(MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .build());
      IO.println(message.content());

      tracerProvider.close();
  }
  ```

  ```php PHP
  use Anthropic\Client;
  use Anthropic\Messages\Model;
  use OpenTelemetry\API\Trace\Propagation\TraceContextPropagator;
  use OpenTelemetry\SDK\Sdk;
  use OpenTelemetry\SDK\Trace\SpanExporter\ConsoleSpanExporterFactory;
  use OpenTelemetry\SDK\Trace\SpanProcessor\SimpleSpanProcessor;
  use OpenTelemetry\SDK\Trace\TracerProvider;

  // Register a tracer provider that prints each span to the console.
  $tracerProvider = new TracerProvider(
      new SimpleSpanProcessor((new ConsoleSpanExporterFactory())->create()),
  );
  Sdk::builder()
      ->setTracerProvider($tracerProvider)
      // OpenTelemetry for PHP doesn't register a propagator when you build
      // it in code, so register the W3C trace context propagator.
      ->setPropagator(TraceContextPropagator::getInstance())
      ->buildAndRegisterGlobal();

  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
  );
  echo $message;
  ```

  ```ruby Ruby
  require "anthropic"
  require "opentelemetry/sdk"

  # Register a tracer provider that prints each span to the console.
  OpenTelemetry::SDK.configure do |config|
    config.add_span_processor(
      OpenTelemetry::SDK::Trace::Export::SimpleSpanProcessor.new(
        OpenTelemetry::SDK::Trace::Export::ConsoleSpanExporter.new
      )
    )
  end

  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{role: "user", content: "Hello, Claude"}]
  )
  puts(message.content)
  ```
</CodeGroup>

The console shows one [`anthropic.messages.create`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-create) span.

## 3. Send spans to your observability platform

Replace the console exporter with an OTLP exporter that points to your observability platform. For the setup in your language, see the OpenTelemetry docs on [Python exporters](https://opentelemetry.io/docs/languages/python/exporters/), [TypeScript exporters](https://opentelemetry.io/docs/languages/js/exporters/), [.NET exporters](https://opentelemetry.io/docs/languages/dotnet/exporters/), [Go exporters](https://opentelemetry.io/docs/languages/go/exporters/), [Java SDK configuration](https://opentelemetry.io/docs/languages/java/configuration/), [PHP exporters](https://opentelemetry.io/docs/languages/php/exporters/), or [Ruby exporters](https://opentelemetry.io/docs/languages/ruby/exporters/).

## 4. Configure the SDK

Use the following options to decide what goes into your spans and where they are sent. You can set an option in your code or, if it has one, with the environment variable under its name.

<Note>
  If you pass `open_telemetry` (typescript, java, php: `openTelemetry`; csharp: `OpenTelemetry`; go: `option.With…()`) to the client, it overrides that option’s environment variables as a whole, including nested keys. Any nested key that you leave out uses its default from the table, even if its environment variable is set.
</Note>

| Option                                                                                                                                                                                                                         | Use it to                                                                                                                                                                                                                         | Default                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `traces.content_mode` (typescript, java, php: `traces.contentMode`; csharp: `Traces.ContentMode`; go: `option.WithOpenTelemetryTracesContentMode()`)<br />`ANTHROPIC_OPEN_TELEMETRY_TRACES_CONTENT_MODE=content`               | Include prompts and responses in spans. See [Content modes](https://platform.claude.com/docs/en/manage-claude/opentelemetry#choose-a-content-mode).                                                                               | `metadata_only`                                                                                                                                                |
| `traces.max_content_bytes` (typescript, java, php: `traces.maxContentBytes`; csharp: `Traces.MaxContentBytes`; go: `option.WithOpenTelemetryTracesMaxContentBytes()`)<br />`ANTHROPIC_OPEN_TELEMETRY_TRACES_MAX_CONTENT_BYTES` | Change the content limit of each span. See [Content limits](https://platform.claude.com/docs/en/manage-claude/opentelemetry#content-limits).                                                                                      | 0.75 MB                                                                                                                                                        |
| `conversation_id` (typescript, java, php: `conversationId`; csharp: `ConversationId`; go: `option.WithOpenTelemetryConversationID()`)                                                                                          | Link several calls into one conversation. The SDK writes the ID to `gen_ai.conversation.id`. The ID is exported in both content modes, so don’t put personal data or secrets in it.                                               | None                                                                                                                                                           |
| `tracer_provider` (typescript, java, php: `tracerProvider`; csharp: `AddSource("com.anthropic.sdk.csharp*")`; go: `option.WithTracerProvider()`)                                                                               | Choose the tracer provider that gets the SDK’s spans.                                                                                                                                                                             | The tracer provider you set up in [Register a tracer provider](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#register-a-tracer-provider) |
| `propagation` (go: `option.WithOpenTelemetryPropagation()`)<br />`ANTHROPIC_OPEN_TELEMETRY_PROPAGATION=false`                                                                                                                  | Stop sending trace context and baggage headers with requests, for example when your HTTP client instrumentation already sends them. The SDK still emits spans. Available in the Python, TypeScript, Go, Java, Ruby, and PHP SDKs. | On                                                                                                                                                             |
| `open_telemetry` (typescript, java, php: `openTelemetry`; csharp: `OpenTelemetry`; go: `option.WithoutOpenTelemetry()`)<br />`ANTHROPIC_OPEN_TELEMETRY=false`                                                                  | Turn spans off for one client, for example when another library already traces the SDK.                                                                                                                                           | On                                                                                                                                                             |

The following example shows how to use each option:

<CodeGroup exclude="shell">
  ```python Python
  # Use a specific tracer provider and record content.
  # Setting open_telemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
  client = Anthropic(
      open_telemetry={"tracer_provider": provider, "traces": {"content_mode": "content"}}
  )

  # Turn spans off for one client.
  quiet_client = Anthropic(open_telemetry=False)

  # Set a conversation ID with with_options(), which returns a copy of the client.
  # with_options() replaces the whole option, so start from client.open_telemetry.
  message = client.with_options(
      open_telemetry={**client.open_telemetry, "conversation_id": "conv_42"}
  ).messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  ```

  ```typescript TypeScript
  // Use a specific tracer provider and record content.
  // Setting openTelemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
  const client = new Anthropic({
    openTelemetry: { tracerProvider: provider, traces: { contentMode: "content" } }
  });

  // Turn spans off for one client.
  const quietClient = new Anthropic({ openTelemetry: false });

  // Set a conversation ID in the request options of one call.
  const message = await client.messages.create(
    {
      model: "claude-opus-5-5",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    },
    { openTelemetry: { conversationId: "conv_42" } }
  );
  ```

  ```csharp C#
  // Use a specific tracer provider: add the SDK's source to it.
  using var tracerProvider = Sdk.CreateTracerProviderBuilder()
      .AddSource("com.anthropic.sdk.csharp*")
      .AddConsoleExporter()
      .Build();

  // Record content.
  // Setting OpenTelemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
  AnthropicClient client = new()
  {
      OpenTelemetry = new() { Traces = new() { ContentMode = OpenTelemetryContentMode.Content } },
  };

  // Turn spans off for one client.
  AnthropicClient quietClient = new() { OpenTelemetry = false };

  // Set a conversation ID for the calls of one conversation.
  var conversation = client.WithOptions(options => options with
  {
      OpenTelemetryRequest = new() { ConversationId = "conv_42" },
  });
  var message = await conversation.Messages.Create(new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      MaxTokens = 1024,
      Messages = [new UserMessageParam { Content = "Hello, Claude" }],
  });
  ```

  ```go Go
  // Use a specific tracer provider and record content.
  client := anthropic.NewClient(
  	option.WithTracerProvider(provider),
  	option.WithOpenTelemetryTracesContentMode(option.OpenTelemetryContentModeContent),
  )

  // Turn spans off for one client.
  quietClient := anthropic.NewClient(option.WithoutOpenTelemetry())

  // Set a conversation ID in the request options of one call.
  message, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  }, option.WithOpenTelemetryConversationID("conv_42"))
  ```

  ```java Java
  // A client reads the environment variables only when you build it with fromEnv().
  // The system properties anthropic.openTelemetry, anthropic.openTelemetryTracesContentMode,
  // and anthropic.openTelemetryTracesMaxContentBytes take precedence over the environment
  // variables.

  // Use a specific tracer provider and record content. Start from
  // OpenTelemetryOptions.fromEnv() to keep the options that fromEnv() read.
  var envOptions = OpenTelemetryOptions.fromEnv();
  var client = AnthropicOkHttpClient.builder()
      .fromEnv()
      .openTelemetry(envOptions.toBuilder()
          .tracerProvider(tracerProvider)
          .traces(envOptions.traces().toBuilder()
              .contentMode(OpenTelemetryContentMode.CONTENT)
              .build())
          .build())
      .build();

  // Turn spans off for one client.
  var quietClient = AnthropicOkHttpClient.builder()
      .fromEnv()
      .openTelemetry(false)
      .build();

  // Set a conversation ID in the request options of one call.
  var params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_5_5)
      .maxTokens(1024)
      .addUserMessage("Hello, Claude")
      .build();
  var message = client.messages().create(params, RequestOptions.builder()
      .openTelemetry(OpenTelemetryRequestOptions.builder()
          .conversationId("conv_42")
          .build())
      .build());
  ```

  ```php PHP
  // Use a specific tracer provider and record content.
  // Setting openTelemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
  $client = new Client(
      openTelemetry: ['tracerProvider' => $tracerProvider, 'traces' => ['contentMode' => 'content']],
  );

  // Turn spans off for one client.
  $quietClient = new Client(openTelemetry: false);

  // Set a conversation ID in the request options of one call.
  $message = $client->messages->create(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      model: Model::CLAUDE_OPUS_5_5,
      requestOptions: ['openTelemetry' => ['conversationId' => 'conv_42']],
  );
  ```

  ```ruby Ruby
  # Use a specific tracer provider and record content.
  # Setting open_telemetry overrides all ANTHROPIC_OPEN_TELEMETRY* environment variables.
  client = Anthropic::Client.new(
    open_telemetry: {
      tracer_provider: OpenTelemetry.tracer_provider,
      traces: {content_mode: :content}
    }
  )

  # Turn spans off for one client.
  quiet_client = Anthropic::Client.new(open_telemetry: false)

  # Set a conversation ID in the request options of one call.
  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{role: "user", content: "Hello, Claude"}],
    request_options: {open_telemetry: {conversation_id: "conv_42"}}
  )
  ```
</CodeGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Set up API tracing" icon="cloud" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry/api">
    Get observability into the Claude API.
  </Card>

  <Card title="See example traces" icon="sitemap" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry#example-traces-and-how-to-read-them">
    Follow a request from your client into the Claude API.
  </Card>
</CardGroup>

## Tracing a stream

A stream’s `anthropic.messages.create` span ends when your code has read the whole stream or closed it, so close a stream that you stop reading early. In content mode, the span has the model response only when you read the stream with `messages.stream()` (go: `Messages.NewStreaming()`; java: `messages().createStreaming()`; csharp: `Messages.CreateStreaming()`; php: `messages->createStream()`).

Spans that you start while you read a stream are siblings of the SDK span, not its children. To group them with the request, start your own span around both the call and the read loop.

## Tracing a Managed Agents self-hosted sandbox

In a Managed Agents [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes), your sandbox runs the tools, so the tool spans come from the SDK instead of the API. The environment worker in the Python, TypeScript, and Go SDKs emits a span for each tool that it runs and each request that it sends. It groups them under one [`anthropic.environment.work`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-environment-work) span for each work item.

To get these spans:

1. In the process that runs the worker, [set up SDK tracing](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#install-the-sdk) as in steps 1 to 4.
2. Allow network traffic from the sandbox to your observability platform or OpenTelemetry Collector.

When the worker sends a tool result, that request’s API span is nested under its SDK span.

## Trace context and baggage

With each request, the SDK uses your application’s propagator to send the trace context to the API in headers such as `traceparent`. If that propagator also writes baggage, the SDK sends your baggage too. To send the trace context without baggage, register only the W3C trace context propagator.

To stop the SDK from sending these headers, for example when your HTTP client instrumentation already sends them, turn off the SDK’s propagation:

<CodeGroup exclude="shell">
  ```python Python
  client = Anthropic(open_telemetry={"propagation": False})
  ```

  <CodeGroupItem>
    ```typescript TypeScript
    const client = new Anthropic({ openTelemetry: { propagation: false } });
    ```

    <Warning>
      Set 

      `propagation: false`

       if you use 

      `@opentelemetry/instrumentation-undici`

      , which 

      `@opentelemetry/auto-instrumentations-node`

       includes. Otherwise, an 

      [undici instrumentation bug](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3711)

       adds a second 

      `traceparent`

       header to each request, which makes the trace context invalid.
    </Warning>
  </CodeGroupItem>

  ```csharp C#
  using System.Diagnostics;

  // The SDK writes these headers with .NET's DistributedContextPropagator.
  // The no-output propagator stops these headers for every HttpClient in the process.
  // Set it before you create any client.
  DistributedContextPropagator.Current = DistributedContextPropagator.CreateNoOutputPropagator();

  AnthropicClient client = new();
  ```

  ```go Go
  client := anthropic.NewClient(option.WithOpenTelemetryPropagation(false))
  ```

  ```java Java
  var envOptions = OpenTelemetryOptions.fromEnv();
  var client = AnthropicOkHttpClient.builder()
      .fromEnv()
      .openTelemetry(envOptions.toBuilder()
          .propagation(false)
          .build())
      .build();
  ```

  ```php PHP
  $client = new Client(openTelemetry: ['propagation' => false]);
  ```

  ```ruby Ruby
  client = Anthropic::Client.new(open_telemetry: {propagation: false})
  ```
</CodeGroup>

While the SDK calls an [MCP tool](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#client-side-mcp-helpers), the SDK’s tool span is the current span. Some MCP client libraries send the trace context to the MCP server in `_meta`, so a server that reads it can add its spans to your trace under that tool span. The Python `mcp` package from version 2.0 and the C# `ModelContextProtocol` package do this. The TypeScript, Go, Java, Ruby, and PHP MCP SDKs don’t do it on their own.

## Troubleshooting

| Problem                                                                                                       | What to check                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No spans from the SDK                                                                                         | Register the tracer provider before the first call. Make sure that you installed the SDK as in [Install the SDK](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#install-the-sdk) and that `ANTHROPIC_OPEN_TELEMETRY` isn’t `false`.                                                                 |
| The Java SDK doesn’t send spans to the registered tracer provider, or doesn’t send trace context to the API   | Another dependency sets `opentelemetry-api` below 1.57.0. Upgrade `opentelemetry-api` to 1.57.0 or later.                                                                                                                                                                                                                |
| The SDK spans don’t nest under your spans, or the spans that your tool creates don’t nest under the tool span | Call the SDK from inside one of your own spans, as the example in [Connect API spans to your own traces](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#connect-api-spans-to-your-own-traces) does. In Go, start the spans that your tool creates from the `ctx` that the tool runner passes to it. |
| Requests from the SDK don’t have a `traceparent` header                                                       | Register the W3C trace context propagator with OpenTelemetry. The SDK writes the headers with your application’s propagator.                                                                                                                                                                                             |
| A stream’s SDK span doesn’t end or doesn’t have the response                                                  | See [Tracing a stream](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#trace-a-stream).                                                                                                                                                                                                              |
| Each request appears twice                                                                                    | A request’s SDK span and API span have the same name. Use the span kind or `service.name` to tell them apart. If another library also traces the SDK, turn off one of the two.                                                                                                                                           |
