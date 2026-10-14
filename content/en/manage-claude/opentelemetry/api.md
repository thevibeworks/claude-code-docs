---
title: Use OpenTelemetry with the Claude API
url: https://platform.claude.com/docs/en/manage-claude/opentelemetry/api
description: Add a destination in the Claude Console to send OpenTelemetry traces of your Messages API requests and Managed Agents sessions to your observability platform.
featureMetadata:
  topic:
    title: OpenTelemetry
    url: https://platform.claude.com/docs/en/manage-claude/opentelemetry
  status: beta
  zdr:
    eligibility: eligible
    note: Excludes [Covered Models](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements). Only for features that are themselves ZDR eligible, such as the Messages API. Claude Managed Agents isn't ZDR eligible.
  supportedPlatforms:
    Claude API: beta
    Claude Platform on AWS: beta
  rows:
    - label: Works with
      value: Messages API, Claude Managed Agents
  details:
    - After delivery, the data is held by the service that you chose, outside Anthropic, under that service's retention and access controls.
---

With OpenTelemetry, the Claude API can emit a span for each model request and each tool use that it runs. You can view these spans in your observability platform without changing your code.

The API emits spans for your Messages API requests and Managed Agents sessions. To receive them, add a *destination* in the Claude Console. A destination tells the API your observability platform's OTLP endpoint and how to authenticate with it.

## What you need

* **The admin role** in a Claude Console organization, to add and change destinations. With the developer role, you can view them. If your organization is on Claude Platform on AWS, sign in to the Console through the AWS Console, as [Signing in](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#signing-in) describes.
* **An OTLP/HTTP endpoint** that accepts protobuf encoding at an HTTPS URL on port 443. If you run your own [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), its OTLP/HTTP receiver listens on port 4318 by default. Configure the receiver to accept HTTPS on port 443, or put a load balancer or reverse proxy in front of the Collector.
* **Credentials for the endpoint**, such as an API key.

## 1. Add a destination

<Info>
  When you add a telemetry destination, Anthropic will send traces of Claude Platform activity in your organization to the third-party provider's OTLP/HTTP endpoint that you specify, in accordance with your provider terms and access controls. After delivery, the data is held by the service that you chose, outside Anthropic, under that service's retention and access controls.
</Info>

1. In the Console, open your organization's [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) and click **Add destination**.

2. Configure the destination:

   | Field                          | What to enter                                                                                                                                                                                                                                                                                                                                                                                                       |
   | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Provider**                   | Your observability platform, or **Custom** if it isn't listed. If you choose a listed platform, the Console asks for its details, such as an API key, instead of the **OTLP endpoint URL**, **Request headers**, and **OTLP traces endpoint URL**.                                                                                                                                                                  |
   | **Name**                       | Optional. For example, "Acme's observability platform."                                                                                                                                                                                                                                                                                                                                                             |
   | **OTLP endpoint URL**          | The base HTTPS URL of your observability platform's OTLP/HTTP endpoint, with a hostname, not an IP address. It can have a path prefix, for example `https://gateway.example.com/otlp`. Don't add `/v1/traces`, because the API adds it. If you set an **OTLP traces endpoint URL**, the API uses that URL instead.                                                                                                  |
   | **Request headers**            | The headers that the API sends with each request, for example your observability platform's API key header. Put credentials only in header values. After you save, the Console doesn't show the values again.                                                                                                                                                                                                       |
   | **Content mode**               | **Metadata only** or **Full content**. See [how the content modes differ](https://platform.claude.com/docs/en/manage-claude/opentelemetry#choose-a-content-mode).                                                                                                                                                                                                                                                   |
   | **Workspaces**                 | The workspaces whose spans the destination receives: **All**, **Selected**, or **All except**. See [Choose workspaces for a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#choose-workspaces-for-a-destination).                                                                                                                                                                  |
   | **OTLP traces endpoint URL**   | Optional, under **Advanced settings**. The full URL of your observability platform's traces endpoint, for example `https://gateway.example.com/custom/traces`. Set it when the platform receives traces at a URL other than the OTLP endpoint URL plus `/v1/traces`. It must have the same host as the OTLP endpoint URL.                                                                                           |
   | **Maximum content size in MB** | Optional, under **Advanced settings** when the content mode is **Full content**. The most content that the API sends in each span. The Console fills it in based on the **Provider** you choose. Change it to fit what your observability platform accepts. Leave it empty to send as much as the API allows. See [Content limits](https://platform.claude.com/docs/en/manage-claude/opentelemetry#content-limits). |

3. Click **Add destination** to save.

4. Click **Test** in the destination's **More actions** menu. You will see a message that the test span was delivered to your collector, or how the delivery failed (see [Delivery errors](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-errors)).

5. Check that the `anthropic.test` span arrived in your observability platform.

### Admin API and CLI

You can also add a destination with the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) instead of the Console. Sign in to the CLI as an admin, or use an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) in `ANTHROPIC_API_KEY`. On Claude Platform on AWS, send the requests to `https://aws-external-anthropic.{region}.api.aws` instead, signed with your AWS credentials as in [Making requests](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#making-requests). There, your [IAM policy](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions) determines who can manage destinations. A request can include only the workspaces of your AWS account in that Region.

<CodeGroup>
  ```bash CLI
  # Sign in once as an admin, which opens a browser. Leave ANTHROPIC_API_KEY unset, because it overrides the profile.
  ant auth login --profile admin --scope "org:admin"
  ant --profile admin beta:organization:telemetry-destinations create \
    --endpoint-url https://gateway.example.com/otlp \
    --headers '{authorization: "Bearer YOUR_OBSERVABILITY_API_KEY"}' \
    --traces.content-mode metadata_only \
    --workspaces.type all
  ```

  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/telemetry_destinations" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: telemetry-destinations-2026-08-11" \
    -H "content-type: application/json" \
    -d '{
      "endpoint_url": "https://gateway.example.com/otlp",
      "headers": {"authorization": "Bearer YOUR_OBSERVABILITY_API_KEY"},
      "traces": {"content_mode": "metadata_only"},
      "workspaces": {"type": "all"}
    }'
  ```

  ```python Python
  client = anthropic.Anthropic()

  destination = client.beta.organization.telemetry_destinations.create(
      endpoint_url="https://gateway.example.com/otlp",
      headers={"authorization": "Bearer YOUR_OBSERVABILITY_API_KEY"},
      traces={"content_mode": "metadata_only"},
      workspaces={"type": "all"},
  )

  print(destination.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const destination = await client.beta.organization.telemetryDestinations.create({
    endpoint_url: "https://gateway.example.com/otlp",
    headers: { authorization: "Bearer YOUR_OBSERVABILITY_API_KEY" },
    traces: { content_mode: "metadata_only" },
    workspaces: { type: "all" }
  });

  console.log(destination.id);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.TelemetryDestinations;

  AnthropicClient client = new();

  var destination = await client.Beta.Organization.TelemetryDestinations.Create(
      new()
      {
          EndpointUrl = "https://gateway.example.com/otlp",
          Headers = new Dictionary<string, string>
          {
              ["authorization"] = "Bearer YOUR_OBSERVABILITY_API_KEY",
          },
          Traces = new() { ContentMode = BetaTelemetryDestinationContentMode.MetadataOnly },
          Workspaces = new BetaTelemetryDestinationWorkspacesAllParams(),
      }
  );

  Console.WriteLine(destination.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  destination, err := client.Beta.Organization.TelemetryDestinations.New(
  	context.Background(),
  	anthropic.BetaOrganizationTelemetryDestinationNewParams{
  		EndpointURL: "https://gateway.example.com/otlp",
  		Headers: map[string]string{
  			"authorization": "Bearer YOUR_OBSERVABILITY_API_KEY",
  		},
  		Traces: anthropic.BetaTelemetryDestinationTracesParams{
  			ContentMode: anthropic.BetaTelemetryDestinationContentModeMetadataOnly,
  		},
  		Workspaces: anthropic.BetaTelemetryDestinationWorkspacesParamsUnion{
  			OfAll: &anthropic.BetaTelemetryDestinationWorkspacesAllParams{},
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(destination.ID)
  ```

  ```java Java
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.organization.telemetrydestinations.BetaTelemetryDestinationContentMode;
  import com.anthropic.models.beta.organization.telemetrydestinations.BetaTelemetryDestinationTracesParams;
  import com.anthropic.models.beta.organization.telemetrydestinations.BetaTelemetryDestinationWorkspacesAllParams;
  import com.anthropic.models.beta.organization.telemetrydestinations.TelemetryDestinationCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = TelemetryDestinationCreateParams.builder()
          .endpointUrl("https://gateway.example.com/otlp")
          .headers(TelemetryDestinationCreateParams.Headers.builder()
              .putAdditionalProperty("authorization", JsonValue.from("Bearer YOUR_OBSERVABILITY_API_KEY"))
              .build())
          .traces(BetaTelemetryDestinationTracesParams.builder()
              .contentMode(BetaTelemetryDestinationContentMode.METADATA_ONLY)
              .build())
          .workspaces(BetaTelemetryDestinationWorkspacesAllParams.builder().build())
          .build();
      var destination = client.beta().organization().telemetryDestinations().create(params);

      IO.println(destination.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $destination = $client->beta->organization->telemetryDestinations->create(
      endpointURL: 'https://gateway.example.com/otlp',
      headers: ['authorization' => 'Bearer YOUR_OBSERVABILITY_API_KEY'],
      traces: ['contentMode' => 'metadata_only'],
      workspaces: ['type' => 'all'],
  );

  echo "{$destination->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  destination = client.beta.organization.telemetry_destinations.create(
    endpoint_url: "https://gateway.example.com/otlp",
    headers: {authorization: "Bearer YOUR_OBSERVABILITY_API_KEY"},
    traces: {content_mode: :metadata_only},
    workspaces: {type: :all}
  )

  puts destination.id
  ```
</CodeGroup>

A create request takes the Console's settings except **Provider**, so enter your observability platform's endpoint URL and headers yourself. Set `traces.max_content_bytes` (csharp, go: `Traces.MaxContentBytes`; java, php: `traces.maxContentBytes`), in bytes, to fit what your observability platform accepts (see [Content limits](https://platform.claude.com/docs/en/manage-claude/opentelemetry#content-limits)). To list, change, or delete destinations, or to add or remove one workspace, use the other methods of the telemetry destinations API.

## 2. Choose workspaces for a destination

A destination receives the spans of the workspaces that it covers. Choose them when you add the destination. For **Workspaces**, select one of the following:

* **All:** Every workspace in the organization, including the [Default Workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work) and workspaces created later.
* **Selected:** Only the workspaces that you select.
* **All except:** Like **All**, but without the workspaces that you select.

For **Selected** or **All except**, select the workspaces in the search box that appears under the options. To change a destination's workspaces later, open its **More actions** menu on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) while the **Workspace** filter shows **All**. Click **Edit**, then choose another **Workspaces** option or change the workspaces in the search box.

If you have the developer role in the organization and the Workspace Admin role in a workspace, you can add that workspace to a **Selected** destination or remove it. Set the **Workspace** filter to that workspace, then open the destination's **More actions** menu. On Claude Platform on AWS, the Console has no Workspace Admin role. There, your [IAM policy](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions) determines who can add a workspace to a destination or remove it.

The API sends spans to every enabled destination that covers the [workspace where the request or session runs](https://platform.claude.com/docs/en/manage-claude/workspaces#api-keys-and-resource-scoping).

## 3. Check that spans arrive

1. In the Console, select a workspace that the destination covers and send a Messages API request in [playground](https://platform.claude.com/playground). You can also send a Messages API request from your application or start a Managed Agents session in that workspace. To start a session, you can follow the steps in [Get started with Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/quickstart).
2. In the Console, on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations), check that the **Delivery** column shows **Healthy** for the destination. This can take about a minute.
3. In your observability platform, filter on `service.name` = `claude-platform` to find the request's spans.

If the column shows **Failing**, hover over it to see the last error. To find the likely cause, see [Delivery errors](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-errors).

## 4. Connect API spans to your own traces

By default, the API spans for a Messages API request or a Managed Agents session are in their own traces. Connect them to your application's traces, so that they nest under your own spans.

The API reads each request's trace context from the W3C [`traceparent` header](https://www.w3.org/TR/trace-context/). If the sampled flag in the header is off, the API doesn't emit the request's span or the spans under it. Claude Platform on AWS doesn't support this header yet. The spans for requests that you send to it always start their own traces, even when the sampled flag is off.

<Tabs>
  <Tab title="With the Claude SDK">
    To connect the API spans, [set up SDK tracing](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk) in your application and call the SDK from inside one of your own spans. Your span then contains the SDK span, which contains the API span. Send all of these spans to the same observability platform, so that it can show them as one trace. See the example traces of [a Messages API request](https://platform.claude.com/docs/en/manage-claude/opentelemetry#a-messages-api-request) and [a Managed Agents session](https://platform.claude.com/docs/en/manage-claude/opentelemetry#a-managed-agents-session).

    The following example sends a user message to a session inside your own span:

    <CodeGroup exclude="shell">
      ```python Python
      from opentelemetry import trace

      tracer = trace.get_tracer("my-service")

      with tracer.start_as_current_span("summarize_issues"):
          client.beta.sessions.events.send(
              session.id,
              events=[
                  {
                      "type": "user.message",
                      "content": [{"type": "text", "text": "Summarize the open issues"}],
                  },
              ],
          )
      ```

      ```typescript TypeScript
      import { trace } from "@opentelemetry/api";

      const tracer = trace.getTracer("my-service");

      await tracer.startActiveSpan("summarize_issues", async (span) => {
        try {
          await client.beta.sessions.events.send(session.id, {
            events: [
              {
                type: "user.message",
                content: [{ type: "text", text: "Summarize the open issues" }]
              }
            ]
          });
        } finally {
          span.end();
        }
      });
      ```

      ```csharp C#
      using System.Diagnostics;

      // Add this source to your tracer provider, next to com.anthropic.sdk.csharp.
      var source = new ActivitySource("MyService");

      using (source.StartActivity("summarize_issues"))
      {
          // parameters holds a user.message event.
          await client.Beta.Sessions.Events.Send(session.ID, parameters);
      }
      ```

      ```go Go
      // Pass the context that has your span.
      ctx, span := otel.Tracer("my-service").Start(ctx, "summarize_issues")
      defer span.End()

      // params holds a user.message event.
      _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, params)
      ```

      ```java Java
      Tracer tracer = GlobalOpenTelemetry.getTracer("my-service");
      Span span = tracer.spanBuilder("summarize_issues").startSpan();

      try (Scope scope = span.makeCurrent()) {
          // params holds a user.message event.
          client.beta().sessions().events().send(session.id(), params);
      } finally {
          span.end();
      }
      ```

      ```php PHP
      use OpenTelemetry\API\Globals;

      $tracer = Globals::tracerProvider()->getTracer('my-service');
      $span = $tracer->spanBuilder('summarize_issues')->startSpan();
      $scope = $span->activate();

      try {
          $client->beta->sessions->events->send(
              $session->id,
              events: [
                  [
                      'type' => 'user.message',
                      'content' => [
                          ['type' => 'text', 'text' => 'Summarize the open issues'],
                      ],
                  ],
              ],
          );
      } finally {
          $scope->detach();
          $span->end();
      }
      ```

      ```ruby Ruby
      tracer = OpenTelemetry.tracer_provider.tracer("my-service")

      tracer.in_span("summarize_issues") do
        client.beta.sessions.events.send_(
          session.id,
          events: [
            {
              type: "user.message",
              content: [{type: "text", text: "Summarize the open issues"}]
            }
          ]
        )
      end
      ```
    </CodeGroup>

    The SDK writes the `traceparent` header with your application's propagator, and the sampled flag in it follows your sampler. If your application uses a propagator other than W3C trace context, such as B3, also add the W3C trace context propagator.
  </Tab>

  <Tab title="With other clients">
    Copy the current span's trace context into the request headers, for example when you create a Managed Agents session or send a user message:

    <CodeGroup exclude="shell:CLI">
      ```bash cURL
      # TRACEPARENT is the traceparent of the active span in your own service,
      # for example 00-<trace-id>-<span-id>-01.
      curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -H "anthropic-beta: managed-agents-2026-04-01" \
        -H "content-type: application/json" \
        -H "traceparent: $TRACEPARENT" \
        -d '{
          "events": [
            {
              "type": "user.message",
              "content": [{"type": "text", "text": "Summarize the open issues"}]
            }
          ]
        }'
      ```

      ```python Python
      import os
      import httpx2
      from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

      headers = {
          "x-api-key": os.environ["ANTHROPIC_API_KEY"],
          "anthropic-version": "2023-06-01",
          "anthropic-beta": "managed-agents-2026-04-01",
          "content-type": "application/json",
      }
      # Copy the active span's trace context into the request headers.
      TraceContextTextMapPropagator().inject(headers)

      httpx2.post(
          f"https://api.anthropic.com/v1/sessions/{os.environ['SESSION_ID']}/events",
          headers=headers,
          json={
              "events": [
                  {
                      "type": "user.message",
                      "content": [{"type": "text", "text": "Summarize the open issues"}],
                  },
              ],
          },
      )
      ```

      ```typescript TypeScript
      import { context, defaultTextMapSetter } from "@opentelemetry/api";
      import { W3CTraceContextPropagator } from "@opentelemetry/core";

      const headers: Record<string, string> = {
        "x-api-key": process.env.ANTHROPIC_API_KEY!,
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "managed-agents-2026-04-01",
        "content-type": "application/json"
      };
      // Copy the active span's trace context into the request headers.
      new W3CTraceContextPropagator().inject(context.active(), headers, defaultTextMapSetter);

      await fetch(`https://api.anthropic.com/v1/sessions/${process.env.SESSION_ID}/events`, {
        method: "POST",
        headers,
        body: JSON.stringify({
          events: [
            {
              type: "user.message",
              content: [{ type: "text", text: "Summarize the open issues" }]
            }
          ]
        })
      });
      ```

      ```csharp C#
      using System.Diagnostics;
      using System.Net.Http.Json;
      using OpenTelemetry;
      using OpenTelemetry.Context.Propagation;

      using var httpClient = new HttpClient();
      using var request = new HttpRequestMessage(
          HttpMethod.Post,
          $"https://api.anthropic.com/v1/sessions/{Environment.GetEnvironmentVariable("SESSION_ID")}/events")
      {
          // JsonContent sets the content-type header.
          Content = JsonContent.Create(new
          {
              events = new[]
              {
                  new
                  {
                      type = "user.message",
                      content = new[] { new { type = "text", text = "Summarize the open issues" } },
                  },
              },
          }),
      };
      request.Headers.Add("x-api-key", Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY"));
      request.Headers.Add("anthropic-version", "2023-06-01");
      request.Headers.Add("anthropic-beta", "managed-agents-2026-04-01");

      // Copy the active span's trace context into the request headers.
      new TraceContextPropagator().Inject(
          new PropagationContext(Activity.Current?.Context ?? default, Baggage.Current),
          request,
          (carrier, key, value) => carrier.Headers.Add(key, value));

      await httpClient.SendAsync(request);
      ```

      ```go Go
      import (
      	"context"
      	"net/http"
      	"os"
      	"strings"

      	"go.opentelemetry.io/otel/propagation"
      )

      func sendMessage(ctx context.Context) error {
      	body := strings.NewReader(`{
      		"events": [
      			{
      				"type": "user.message",
      				"content": [{"type": "text", "text": "Summarize the open issues"}]
      			}
      		]
      	}`)
      	req, err := http.NewRequestWithContext(ctx, http.MethodPost,
      		"https://api.anthropic.com/v1/sessions/"+os.Getenv("SESSION_ID")+"/events", body)
      	if err != nil {
      		return err
      	}
      	req.Header.Set("x-api-key", os.Getenv("ANTHROPIC_API_KEY"))
      	req.Header.Set("anthropic-version", "2023-06-01")
      	req.Header.Set("anthropic-beta", "managed-agents-2026-04-01")
      	req.Header.Set("content-type", "application/json")

      	// Copy the active span's trace context into the request headers.
      	propagation.TraceContext{}.Inject(ctx, propagation.HeaderCarrier(req.Header))

      	resp, err := http.DefaultClient.Do(req)
      	if err != nil {
      		return err
      	}
      	return resp.Body.Close()
      }
      ```

      ```java Java
      import io.opentelemetry.api.trace.propagation.W3CTraceContextPropagator;
      import io.opentelemetry.context.Context;
      import java.net.URI;
      import java.net.http.HttpClient;
      import java.net.http.HttpRequest;
      import java.net.http.HttpResponse;

      void main() throws Exception {
          var request = HttpRequest.newBuilder(URI.create(
                  "https://api.anthropic.com/v1/sessions/" + System.getenv("SESSION_ID") + "/events"))
              .header("x-api-key", System.getenv("ANTHROPIC_API_KEY"))
              .header("anthropic-version", "2023-06-01")
              .header("anthropic-beta", "managed-agents-2026-04-01")
              .header("content-type", "application/json")
              .POST(HttpRequest.BodyPublishers.ofString("""
                  {
                    "events": [
                      {
                        "type": "user.message",
                        "content": [{"type": "text", "text": "Summarize the open issues"}]
                      }
                    ]
                  }
                  """));

          // Copy the active span's trace context into the request headers.
          W3CTraceContextPropagator.getInstance()
              .inject(Context.current(), request, HttpRequest.Builder::header);

          HttpClient.newHttpClient().send(request.build(), HttpResponse.BodyHandlers.ofString());
      }
      ```

      ```php PHP
      use OpenTelemetry\API\Trace\Propagation\TraceContextPropagator;

      $headers = [
          'x-api-key' => getenv('ANTHROPIC_API_KEY'),
          'anthropic-version' => '2023-06-01',
          'anthropic-beta' => 'managed-agents-2026-04-01',
          'content-type' => 'application/json',
      ];
      // Copy the active span's trace context into the request headers.
      TraceContextPropagator::getInstance()->inject($headers);

      $ch = curl_init('https://api.anthropic.com/v1/sessions/' . getenv('SESSION_ID') . '/events');
      curl_setopt_array($ch, [
          CURLOPT_RETURNTRANSFER => true,
          CURLOPT_HTTPHEADER => array_map(
              static fn ($name, $value) => "$name: $value",
              array_keys($headers),
              $headers,
          ),
          CURLOPT_POSTFIELDS => json_encode([
              'events' => [
                  [
                      'type' => 'user.message',
                      'content' => [
                          ['type' => 'text', 'text' => 'Summarize the open issues'],
                      ],
                  ],
              ],
          ]),
      ]);
      curl_exec($ch);
      ```

      ```ruby Ruby
      require "json"
      require "net/http"
      require "opentelemetry"

      headers = {
        "x-api-key" => ENV.fetch("ANTHROPIC_API_KEY"),
        "anthropic-version" => "2023-06-01",
        "anthropic-beta" => "managed-agents-2026-04-01",
        "content-type" => "application/json"
      }
      # Copy the active span's trace context into the request headers.
      OpenTelemetry::Trace::Propagation::TraceContext.text_map_propagator.inject(headers)

      Net::HTTP.post(
        URI("https://api.anthropic.com/v1/sessions/#{ENV.fetch("SESSION_ID")}/events"),
        {
          events: [
            {
              type: "user.message",
              content: [{type: "text", text: "Summarize the open issues"}]
            }
          ]
        }.to_json,
        headers
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

The Messages API also passes the trace on to your MCP server when you connect it with the [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector), so that it can put its own spans under the API spans. Each request and notification that the API sends to your MCP server has a W3C `traceparent` in `params._meta`. In a `tools/call` request, it references the [`anthropic.mcp_tool_use`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span of that tool use. In the other messages, it references the [`anthropic.messages.create`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-create) span. For a request that the API doesn't trace, such as one whose `traceparent` header has the sampled flag off, the API sends no `traceparent`.

## Next steps

<CardGroup cols={2}>
  <Card title="Set up SDK tracing" icon="code-brackets" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk">
    Get observability into your client.
  </Card>

  <Card title="See example traces" icon="sitemap" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry#example-traces-and-how-to-read-them">
    Follow a request from your client into the Claude API.
  </Card>
</CardGroup>

## Delivery and health

The following rules apply to the spans that the API sends to your destinations.

* **At least once:** A destination can receive the same span more than once. To remove duplicates, use the trace ID and span ID.
* **Best effort:** A span can be lost before delivery. The API can't send a lost span again.
* **Compression:** The API compresses every delivery's first request with gzip and sets the header `Content-Encoding: gzip`. If your endpoint answers that request with a `400` or `415` response, the API sends the same spans again right away without compression.
* **Retries:** The API retries a delivery later, a limited number of times, after a timeout, a connection, TLS, or DNS failure, or a `408`, `429`, or `5xx` response. It doesn't retry other failures.
* **Timeouts:** For each request, your endpoint must complete the TLS handshake within 5 seconds and send the response headers within 5 seconds. Each delivery times out after 10 seconds in total, including the resend without compression.
* **User agent:** Each request has the header `User-Agent: Claude-Platform`.

The **Delivery** column shows each destination's state. The state can be up to a minute late.

| Delivery state | Meaning                                                                     |
| -------------- | --------------------------------------------------------------------------- |
| **Healthy**    | The last delivery succeeded.                                                |
| **Failing**    | The last delivery failed. To see the error, hover over **Failing**.         |
| **No data**    | The API hasn't tried a delivery yet.                                        |
| **Disabled**   | The destination doesn't receive spans. To see why, hover over **Disabled**. |

The API disables a destination when:

* The endpoint sends a `3xx` redirect.
* The endpoint's hostname resolves to an IP address that isn't public.
* All deliveries fail for 24 hours.

The API doesn't send spans to a disabled destination. To resume export, fix the cause. Then, with the **Workspace** filter on the [OpenTelemetry settings page](https://platform.claude.com/settings/telemetry-destinations) showing **All**, click **Enable** in the destination's **More actions** menu. Export starts again within about a minute.

To change a destination, open its **More actions** menu while the **Workspace** filter shows **All**. Then click **Edit**, **Disable**, **Enable**, or **Delete**. If you change the host of the **OTLP endpoint URL**, enter the header values again. If the destination has an **OTLP traces endpoint URL**, give it the same new host, or clear it.

## Limits

| Limit                                                       | Value            |
| ----------------------------------------------------------- | ---------------- |
| Destinations for each organization, including disabled ones | 10               |
| Workspaces that you select for a destination                | 1,000            |
| Request headers for each destination                        | 20               |
| Length of a header name                                     | 128 bytes        |
| Length of a header value                                    | 4,096 bytes      |
| Length of all header names and values together              | 16,384 bytes     |
| Length of an endpoint URL                                   | 2,048 characters |

## Troubleshooting

| Problem                                                                            | What to check                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No API spans                                                                       | The workspace needs an enabled destination that covers it. See [Choose workspaces for a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#choose-workspaces-for-a-destination). After a destination starts covering a workspace, spans from that workspace can take up to a minute to arrive. |
| The **Delivery** column shows **Failing**                                          | Hover over it to see the last error. To find the likely cause, see [Delivery errors](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-errors).                                                                                                                                                   |
| The **Delivery** column shows **Disabled**                                         | Hover over it to see why. For the reasons, see [when the API disables a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-and-health).                                                                                                                                               |
| Spans have no prompts or responses, but the destination is set to **Full content** | Your organization might have a HIPAA, FERPA, or K-12 data-handling restriction with Anthropic. See [Content modes](https://platform.claude.com/docs/en/manage-claude/opentelemetry#choose-a-content-mode).                                                                                                                   |

### Delivery errors

When a delivery fails, the **Delivery** column shows **Failing**. Hover over it to see the error, then find the likely cause:

| Error                                              | Likely cause                                                                                                                                              |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTP error (status 401) or HTTP error (status 403) | A wrong authentication header                                                                                                                             |
| HTTP error (status 404)                            | A wrong path in the **OTLP endpoint URL** or the **OTLP traces endpoint URL**                                                                             |
| DNS resolution failure                             | The endpoint's hostname doesn't resolve                                                                                                                   |
| TLS failure                                        | A TLS problem, for example with the endpoint's certificate                                                                                                |
| Timeout                                            | The endpoint didn't respond in time. See [the delivery timeouts](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-and-health) |
| Connection failure                                 | The API couldn't connect to the endpoint                                                                                                                  |
