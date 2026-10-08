---
title: Session event stream
url: https://platform.claude.com/docs/en/managed-agents/events-and-streaming
description: Send events, stream responses, and interrupt or redirect your session mid-execution.
featureMetadata:
  topic:
    title: Managed Agents
    url: https://platform.claude.com/docs/en/managed-agents/overview
  status: beta
  betaHeader: managed-agents-2026-04-01
---

Communication with Claude Managed Agents is event-based. You open a stream to follow a session, send events to direct it, and answer it when it pauses for input.

## Event types

Events flow in two directions: you send events to the agent, and the session sends events back to you.

* **Events you send:** `user.*` events start a session and steer it as it progresses. [`system.message`](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#send-system-messages) events append system-level context.
* **Events you receive:** Session events, span events, and agent events report the session's state and the agent's progress.

These event type strings follow a `{domain}.{action}` naming convention. See [Event types](https://platform.claude.com/docs/en/managed-agents/reference#event-types) in the reference for the full catalog.

[Webhook event types](https://platform.claude.com/docs/en/managed-agents/webhooks#supported-event-types) are separate, and some of their names differ from the stream's. For example, webhooks use `session.status_idled` rather than `session.status_idle`.

## Stream events

Stream events from the session to receive real-time updates as the agent works. A stream delivers only the events emitted after it opens, so open the stream before you send events to avoid a race condition.

<CodeGroup>
  ```bash cURL
  # Open the stream first, then send the user message
  exec {stream}< <(
    curl --fail-with-body -sS -N \
      "https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream?beta=true" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" \
      -H "accept: text/event-stream"
  )

  curl --fail-with-body -sS \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- >/dev/null <<'EOF'
  {
    "events": [
      {
        "type": "user.message",
        "content": [{"type": "text", "text": "Summarize the repo README"}]
      }
    ]
  }
  EOF

  while IFS= read -r -u "$stream" event_line; do
    [[ $event_line == data:* ]] || continue
    event_json=${event_line#data: }
    case $(jq -r '.type' <<<"$event_json") in
      agent.message)
        jq -j '.content[] | select(.type == "text") | .text' <<<"$event_json"
        ;;
      session.status_idle)
        break
        ;;
      session.error)
        printf '\n[Error: %s]\n' "$(jq -r '.error.message // "unknown"' <<<"$event_json")"
        break
        ;;
    esac
  done
  exec {stream}<&-
  ```

  ```bash CLI
  # This workflow does not translate well to a one-off shell command.
  # Use one of the SDK examples in this code group instead.
  ```

  ```python Python
  # Open the stream first, then send the user message
  with client.beta.sessions.events.stream(session.id) as stream:
      client.beta.sessions.events.send(
          session.id,
          events=[
              {
                  "type": "user.message",
                  "content": [{"type": "text", "text": "Summarize the repo README"}],
              },
          ],
      )

      for event in stream:
          match event.type:
              case "agent.message":
                  for block in event.content:
                      if block.type == "text":
                          print(block.text, end="")
              case "session.status_idle":
                  break
              case "session.error":
                  error_message = event.error.message if event.error else "unknown"
                  print(f"\n[Error: {error_message}]")
                  break
  ```

  ```typescript TypeScript
  // Open the stream first, then send the user message
  const stream = await client.beta.sessions.events.stream(session.id);
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.message",
        content: [{ type: "text", text: "Summarize the repo README" }]
      }
    ]
  });

  events: for await (const event of stream) {
    switch (event.type) {
      case "agent.message":
        for (const block of event.content) {
          if (block.type === "text") {
            process.stdout.write(block.text);
          }
        }
        break;
      case "session.status_idle":
        break events;
      case "session.error":
        console.log(`\n[Error: ${event.error?.message ?? "unknown"}]`);
        break events;
    }
  }
  ```

  ```csharp C#
  // Open the stream first, then send the user message
  using var stream = await client.Beta.Sessions.Events.WithRawResponse.StreamStreaming(session.ID);
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
              Content =
              [
                  new BetaManagedAgentsTextBlock
                  {
                      Type = BetaManagedAgentsTextBlockType.Text,
                      Text = "Summarize the repo README",
                  },
              ],
          },
      ],
  });

  await foreach (var streamEvent in stream.Enumerate())
  {
      if (streamEvent.Value is BetaManagedAgentsAgentMessageEvent message)
      {
          foreach (var block in message.Content)
          {
              if (block.Value is BetaManagedAgentsTextBlock textBlock)
              {
                  Console.Write(textBlock.Text);
              }
          }
      }
      else if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent)
      {
          break;
      }
      else if (streamEvent.Value is BetaManagedAgentsSessionErrorEvent error)
      {
          Console.WriteLine($"\n[Error: {error.Error?.Message ?? "unknown"}]");
          break;
      }
  }
  ```

  ```go Go
  	// Open the stream first, then send the user message
  	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
  	defer stream.Close()

  	if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  		Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  						Text: "Summarize the repo README",
  					},
  				}},
  			},
  		}},
  	}); err != nil {
  		panic(err)
  	}

  events:
  	for stream.Next() {
  		switch event := stream.Current().AsAny().(type) {
  		case anthropic.BetaManagedAgentsAgentMessageEvent:
  			// concrete-typed list: BetaManagedAgentsTextBlock
  			for _, block := range event.Content {
  				fmt.Print(block.Text)
  			}
  		case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
  			break events
  		case anthropic.BetaManagedAgentsSessionErrorEvent:
  			fmt.Printf("\n[Error: %s]\n", cmp.Or(event.Error.Message, "unknown"))
  			break events
  		}
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}
  ```

  ```java Java
  // Open the stream first, then send the user message
  try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
      client.beta().sessions().events().send(
          session.id(),
          EventSendParams.builder()
              .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
                  .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
                  .addTextContent("Summarize the repo README")
                  .build())
              .build()
      );

      Iterable<BetaManagedAgentsStreamSessionEvents> events = stream.stream()::iterator;
      events:
      for (var event : events) {
          switch (event.type().value()) {
              case AGENT_MESSAGE -> event.asAgentMessage().content().forEach(block -> block.text().ifPresent(textBlock -> IO.print(textBlock.text())));
              case SESSION_STATUS_IDLE -> {
                  break events;
              }
              case SESSION_ERROR -> {
                  // The `message` field spans all error variants; read it from the raw JSON.
                  var errorMessage =
                      event.asSessionError().error()._json().orElse(null) instanceof JsonObject json
                          ? json.values().get("message").asStringOrThrow()
                          : "unknown";
                  IO.println("\n[Error: " + errorMessage + "]");
                  break events;
              }
          }
      }
  }
  ```

  ```php PHP
  // Open the stream first, then send the user message
  $stream = $client->beta->sessions->events->streamStream($session->id);
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'user.message',
              'content' => [['type' => 'text', 'text' => 'Summarize the repo README']],
          ],
      ],
  );

  foreach ($stream as $event) {
      match (true) {
          $event instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsAgentMessageEvent => array_walk(
              $event->content,
              static fn ($block) => $block instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsTextBlock ? print($block->text) : null,
          ),
          $event instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionErrorEvent => printf("\n[Error: %s]", $event->error?->message ?? 'unknown'),
          default => null,
      };
      if ($event->type === 'session.status_idle' || $event->type === 'session.error') {
          break;
      }
  }
  $stream->close();
  ```

  ```ruby Ruby
  # Open the stream first, then send the user message
  stream = client.beta.sessions.events.stream_events(session.id)

  client.beta.sessions.events.send_(
    session.id,
    events: [{
      type: "user.message",
      content: [{type: "text", text: "Summarize the repo README"}]
    }]
  )

  stream.each do |event|
    case event
    when Anthropic::Beta::Sessions::BetaManagedAgentsAgentMessageEvent
      event.content.each { print it.text }
    when Anthropic::Beta::Sessions::BetaManagedAgentsSessionStatusIdleEvent
      break
    when Anthropic::Beta::Sessions::BetaManagedAgentsSessionErrorEvent
      puts "\n[Error: #{event.error&.message || "unknown"}]"
      break
    else
      # ignore other event types
    end
  end
  ```
</CodeGroup>

The session reports errors through the `session.error` event. See [Event types](https://platform.claude.com/docs/en/managed-agents/reference#event-types) for its fields.

The agent's response text arrives as buffered `agent.message` events, each emitted only after the model request that produced it finishes. To render the text while the model is still generating it, see [Preview responses with event deltas](https://platform.claude.com/docs/en/managed-agents/event-deltas).

### Reconnect without missing events

To reconnect to an existing session without missing events, combine a new stream with the event history:

1. Open a new stream.
2. [List the full event history](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#list-past-events) to seed a set of seen event IDs.
3. Tail the live stream, skipping any events already returned by the history list.

<CodeGroup>
  ```bash cURL
  exec {stream}< <(
    curl --fail-with-body -sS -N \
      "https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream?beta=true" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" \
      -H "accept: text/event-stream"
  )

  # Stream is open and buffering. List history before tailing live.
  declare -A seen_event_ids
  while IFS= read -r event_id; do
    seen_event_ids[$event_id]=1
  done < <(
    curl --fail-with-body -sS \
      "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" | jq -r '.data[].id'
  )

  # Tail live events, skipping anything already seen
  while IFS= read -r -u "$stream" event_line; do
    [[ $event_line == data:* ]] || continue
    event_json=${event_line#data: }
    event_id=$(jq -r '.id' <<<"$event_json")
    [[ -n ${seen_event_ids[$event_id]+seen} ]] && continue
    seen_event_ids[$event_id]=1
    case $(jq -r '.type' <<<"$event_json") in
      agent.message)
        jq -j '.content[] | select(.type == "text") | .text' <<<"$event_json"
        ;;
      session.status_idle)
        break
        ;;
    esac
  done
  exec {stream}<&-
  ```

  ```bash CLI
  # This workflow does not translate well to a one-off shell command.
  # Use one of the SDK examples in this code group instead.
  ```

  ```python Python
  with client.beta.sessions.events.stream(session.id) as stream:
      # Stream is open and buffering. List history before tailing live.
      history = client.beta.sessions.events.list(session.id)
      seen_event_ids = {past_event.id for past_event in history}

      # Tail live events, skipping anything already seen
      for event in stream:
          if event.type == "event_start" or event.type == "event_delta":
              # Delta previews aren't enabled on this connection.
              continue
          if event.id in seen_event_ids:
              continue
          seen_event_ids.add(event.id)
          match event.type:
              case "agent.message":
                  for block in event.content:
                      if block.type == "text":
                          print(block.text, end="")
              case "session.status_idle":
                  break
  ```

  ```typescript TypeScript
  const seenEventIds = new Set<string>();
  const stream = await client.beta.sessions.events.stream(session.id);

  // Stream is open and buffering. List history before tailing live.
  for await (const event of client.beta.sessions.events.list(session.id)) {
    seenEventIds.add(event.id);
  }

  // Tail live events, skipping anything already seen
  tail: for await (const event of stream) {
    // Preview events (event_start/event_delta) carry no top-level id
    if (event.type === "event_start" || event.type === "event_delta") continue;
    if (seenEventIds.has(event.id)) continue;
    seenEventIds.add(event.id);
    switch (event.type) {
      case "agent.message":
        for (const block of event.content) {
          if (block.type === "text") {
            process.stdout.write(block.text);
          }
        }
        break;
      case "session.status_idle":
        break tail;
    }
  }
  ```

  ```csharp C#
  using var stream = await client.Beta.Sessions.Events.WithRawResponse.StreamStreaming(session.ID);

  // Stream is open and buffering. List history before tailing live.
  HashSet<string> seenEventIds = [];
  var history = await client.Beta.Sessions.Events.List(session.ID);
  await foreach (var pastEvent in history.Paginate())
  {
      seenEventIds.Add(pastEvent.ID);
  }

  // Tail live events, skipping anything already seen
  await foreach (var streamEvent in stream.Enumerate())
  {
      if (!seenEventIds.Add(streamEvent.ID))
      {
          continue;
      }
      if (streamEvent.Value is BetaManagedAgentsAgentMessageEvent message)
      {
          foreach (var block in message.Content)
          {
              if (block.Value is BetaManagedAgentsTextBlock textBlock)
              {
                  Console.Write(textBlock.Text);
              }
          }
      }
      else if (streamEvent.Value is BetaManagedAgentsSessionStatusIdleEvent)
      {
          break;
      }
  }
  ```

  ```go Go
  	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
  	defer stream.Close()

  	// Stream is open and buffering. List history before tailing live.
  	seenEventIDs := map[string]struct{}{}
  	history := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})
  	for history.Next() {
  		seenEventIDs[history.Current().ID] = struct{}{}
  	}
  	if err := history.Err(); err != nil {
  		panic(err)
  	}

  	// Tail live events, skipping anything already seen
  tail:
  	for stream.Next() {
  		event := stream.Current()
  		if _, seen := seenEventIDs[event.ID]; seen {
  			continue
  		}
  		seenEventIDs[event.ID] = struct{}{}
  		switch event := event.AsAny().(type) {
  		case anthropic.BetaManagedAgentsAgentMessageEvent:
  			// concrete-typed list: BetaManagedAgentsTextBlock
  			for _, block := range event.Content {
  				fmt.Print(block.Text)
  			}
  		case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
  			break tail
  		}
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}
  ```

  ```java Java
  try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
      // Stream is open and buffering. List history before tailing live.
      // Every event variant carries `id`; read it from the raw JSON to dedup across variants.
      var seenEventIds = new HashSet<String>();
      for (var pastEvent : client.beta().sessions().events().list(session.id()).autoPager()) {
          if (pastEvent._json().orElseThrow() instanceof JsonObject json) {
              seenEventIds.add(json.values().get("id").asStringOrThrow());
          }
      }

      // Tail live events; Set.add returns false for already-seen IDs, skipping the replay.
      stream.stream()
          .filter(event -> event._json().orElseThrow() instanceof JsonObject json
              && seenEventIds.add(json.values().get("id").asStringOrThrow()))
          .takeWhile(event -> !event.isSessionStatusIdle())
          .filter(BetaManagedAgentsStreamSessionEvents::isAgentMessage)
          .forEach(event -> event.asAgentMessage().content()
              .forEach(block -> block.text().ifPresent(textBlock -> IO.print(textBlock.text()))));
  }
  ```

  ```php PHP
  $stream = $client->beta->sessions->events->streamStream($session->id);

  // Stream is open and buffering. List history before tailing live.
  $seenEventIds = [];
  foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
      $seenEventIds[$event->id] = true;
  }

  // Tail live events, skipping anything already seen
  foreach ($stream as $event) {
      if (isset($seenEventIds[$event->id])) {
          continue;
      }
      $seenEventIds[$event->id] = true;
      match (true) {
          $event instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsAgentMessageEvent => array_walk(
              $event->content,
              static fn ($block) => $block instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsTextBlock ? print($block->text) : null,
          ),
          default => null,
      };
      if ($event->type === 'session.status_idle') {
          break;
      }
  }
  $stream->close();
  ```

  ```ruby Ruby
  stream = client.beta.sessions.events.stream_events(session.id)

  # Stream is open and buffering. List history before tailing live.
  seen_event_ids = Set.new
  client.beta.sessions.events.list(session.id).auto_paging_each { seen_event_ids << it.id }

  # Tail live events, skipping anything already seen — Set#add? returns nil for duplicates
  stream.each do |event|
    next unless seen_event_ids.add?(event.id)
    case event
    when Anthropic::Beta::Sessions::BetaManagedAgentsAgentMessageEvent
      event.content.each { print it.text }
    when Anthropic::Beta::Sessions::BetaManagedAgentsSessionStatusIdleEvent
      break
    else
      # ignore other event types
    end
  end
  ```
</CodeGroup>

## Send events

Send a `user.message` event to start or continue the agent's work:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "events": [
      {
        "type": "user.message",
        "content": [
          {"type": "text", "text": "Analyze the performance of the sort function in utils.py"}
        ]
      }
    ]
  }
  EOF
  ```

  ```bash CLI
  ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
  events:
    - type: user.message
      content:
        - type: text
          text: Analyze the performance of the sort function in utils.py
  YAML
  ```

  ```python Python
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "user.message",
              "content": [
                  {
                      "type": "text",
                      "text": "Analyze the performance of the sort function in utils.py",
                  },
              ],
          },
      ],
  )
  ```

  ```typescript TypeScript
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.message",
        content: [
          {
            type: "text",
            text: "Analyze the performance of the sort function in utils.py",
          },
        ],
      },
    ],
  });
  ```

  ```csharp C#
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
              Content =
              [
                  new BetaManagedAgentsTextBlock
                  {
                      Type = BetaManagedAgentsTextBlockType.Text,
                      Text = "Analyze the performance of the sort function in utils.py",
                  },
              ],
          },
      ],
  });
  ```

  ```go Go
  if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  		OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  			Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  			Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  				OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  					Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  					Text: "Analyze the performance of the sort function in utils.py",
  				},
  			}},
  		},
  	}},
  }); err != nil {
  	panic(err)
  }
  ```

  ```java Java
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
              .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
              .addTextContent("Analyze the performance of the sort function in utils.py")
              .build())
          .build());
  ```

  ```php PHP
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'user.message',
              'content' => [
                  [
                      'type' => 'text',
                      'text' => 'Analyze the performance of the sort function in utils.py',
                  ],
              ],
          ],
      ],
  );
  ```

  ```ruby Ruby
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.message",
        content: [
          {
            type: "text",
            text: "Analyze the performance of the sort function in utils.py"
          }
        ]
      }
    ]
  )
  ```
</CodeGroup>

Every event in the session's history includes a `processed_at` timestamp, set when the event finishes processing. On events you send, `processed_at` is null while the event is still queued behind earlier events. The exceptions are `user.define_outcome`, `user.custom_tool_result`, and `user.tool_result`, which are processed on receipt and echoed back with `processed_at` already populated.

## Respond when the session goes idle

A `session.status_idle` event means the agent has stopped and is waiting for input. Its `stop_reason.type` says why:

| `stop_reason.type` | Why the session stopped                                                                                                                            | What to do                                                                                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `end_turn`         | The agent finished its turn, or [you interrupted it](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#interrupt-the-agent). | [Send a `user.message`](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#resume-an-idle-session) when you have more work for the agent. |
| `requires_action`  | One or more tool calls need an answer from you, such as a custom tool call or a confirmation request.                                              | [Answer each blocking tool call](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#answer-tool-calls-that-pause-the-session).            |
| `budget_reached`   | The session's tracked list cost reached its [budget](https://platform.claude.com/docs/en/managed-agents/budgets).                                  | [Change or remove the budget](https://platform.claude.com/docs/en/managed-agents/budgets#resume-a-session-at-its-budget).                                      |

No event resumes a session paused at its budget. The paused work resumes automatically when you change the budget to a value above the consumed list cost, or remove it. See [When a session reaches its budget](https://platform.claude.com/docs/en/managed-agents/budgets#when-a-session-reaches-its-budget) for the events that mark the pause and the events the session still accepts.

## Answer tool calls that pause the session

A session pauses when the agent invokes a [custom tool](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools), and when a tool call needs your confirmation under a [permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies). Both pauses follow the same sequence:

1. The session emits the tool call as an `agent.custom_tool_use`, `agent.tool_use`, or `agent.mcp_tool_use` event.
2. The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3. For each blocking event ID, send a [`user.custom_tool_result`](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#return-a-custom-tool-result) or a [`user.tool_confirmation`](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#confirm-a-tool-call) event.
4. Once all blocking events are resolved, the session transitions back to `running`.

In a multiagent session, a subagent's blocking events are cross-posted to the primary thread. See [Tool permissions and custom tools](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#tool-permissions-and-custom-tools).

### Return a custom tool result

The `agent.custom_tool_use` event contains the tool name and input. Execute the tool in your system. Then send a `user.custom_tool_result` event, passing the event ID in the `custom_tool_use_id` parameter along with the result content.

<CodeGroup>
  ```bash cURL
  exec {stream_fd}< <(curl --fail-with-body -sS -N \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -H "accept: text/event-stream")

  while IFS= read -r -u "$stream_fd" line; do
    [[ $line == data:* ]] || continue
    event_json="${line#data: }"
    stop_reason=$(jq -r 'select(.type == "session.status_idle") | .stop_reason.type // empty' <<<"$event_json")
    case "$stop_reason" in
      requires_action)
        while IFS= read -r event_id; do
          # Execute the tool and send the result back
          result=$(call_tool "$event_id")
          jq -n --arg id "$event_id" --arg result "$result" \
            '{events: [{type: "user.custom_tool_result", custom_tool_use_id: $id, content: [{type: "text", text: $result}]}]}' |
            curl --fail-with-body -sS \
              "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
              -H "x-api-key: $ANTHROPIC_API_KEY" \
              -H "anthropic-version: 2023-06-01" \
              -H "anthropic-beta: managed-agents-2026-04-01" \
              -H "content-type: application/json" \
              -d @-
        done < <(jq -r '.stop_reason.event_ids[]' <<<"$event_json")
        ;;
      end_turn)
        break
        ;;
    esac
  done
  exec {stream_fd}<&-
  ```

  ```bash CLI
  # This workflow does not translate well to a one-off shell command.
  # Use one of the SDK examples in this code group instead.
  ```

  ```python Python
  with client.beta.sessions.events.stream(session.id) as stream:
      for event in stream:
          if event.type == "session.status_idle" and (stop_reason := event.stop_reason):
              match stop_reason.type:
                  case "requires_action":
                      for event_id in stop_reason.event_ids:
                          # Look up the custom tool use event and execute it
                          tool_event = events_by_id[event_id]
                          result = call_tool(tool_event.name, tool_event.input)

                          # Send the result back
                          client.beta.sessions.events.send(
                              session.id,
                              events=[
                                  {
                                      "type": "user.custom_tool_result",
                                      "custom_tool_use_id": event_id,
                                      "content": [{"type": "text", "text": result}],
                                  },
                              ],
                          )
                  case "end_turn":
                      break
  ```

  ```typescript TypeScript
  const stream = await client.beta.sessions.events.stream(session.id);

  for await (const event of stream) {
    if (event.type !== "session.status_idle") continue;
    if (event.stop_reason.type === "end_turn") break;
    if (event.stop_reason.type !== "requires_action") continue;

    for (const eventId of event.stop_reason.event_ids) {
      // Look up the custom tool use event and execute it
      const toolEvent = eventsById.get(eventId);
      if (!toolEvent) continue;
      const result = await callTool(toolEvent.name, toolEvent.input);

      // Send the result back
      await client.beta.sessions.events.send(session.id, {
        events: [
          {
            type: "user.custom_tool_result",
            custom_tool_use_id: eventId,
            content: [{ type: "text", text: result }],
          },
        ],
      });
    }
  }
  ```

  ```csharp C#
  await foreach (var streamEvent in client.Beta.Sessions.Events.StreamStreaming(session.ID))
  {
      if (streamEvent.Value is not BetaManagedAgentsSessionStatusIdleEvent idle) continue;

      if (idle.StopReason?.Value is BetaManagedAgentsSessionRequiresAction requiresAction)
      {
          foreach (var eventId in requiresAction.EventIds)
          {
              // Look up the custom tool use event and execute it
              var toolEvent = eventsById[eventId];
              var result = await CallTool(toolEvent.Name, toolEvent.Input);

              // Send the result back
              await client.Beta.Sessions.Events.Send(session.ID, new()
              {
                  Events =
                  [
                      new BetaManagedAgentsUserCustomToolResultEventParams
                      {
                          Type = BetaManagedAgentsUserCustomToolResultEventParamsType.UserCustomToolResult,
                          CustomToolUseID = eventId,
                          Content =
                          [
                              new BetaManagedAgentsTextBlock
                              {
                                  Type = BetaManagedAgentsTextBlockType.Text,
                                  Text = result,
                              },
                          ],
                      },
                  ],
              });
          }
      }
      else if (idle.StopReason?.Value is BetaManagedAgentsSessionEndTurn)
      {
          break;
      }
  }
  ```

  ```go Go
  	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
  	defer stream.Close()

  loop:
  	for stream.Next() {
  		event, ok := stream.Current().AsAny().(anthropic.BetaManagedAgentsSessionStatusIdleEvent)
  		if !ok {
  			continue
  		}
  		switch stopReason := event.StopReason.AsAny().(type) {
  		case anthropic.BetaManagedAgentsSessionRequiresAction:
  			for _, eventID := range stopReason.EventIDs {
  				// Look up the custom tool use event and execute it
  				toolEvent := eventsByID[eventID]
  				result := callTool(toolEvent.Name, toolEvent.Input)
  				// Send the result back
  				if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  					Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  						OfUserCustomToolResult: &anthropic.BetaManagedAgentsUserCustomToolResultEventParams{
  							Type:            anthropic.BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult,
  							CustomToolUseID: eventID,
  							Content: []anthropic.BetaManagedAgentsUserCustomToolResultEventParamsContentUnion{{
  								OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  									Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  									Text: result,
  								},
  							}},
  						},
  					}},
  				}); err != nil {
  					panic(err)
  				}
  			}
  		case anthropic.BetaManagedAgentsSessionEndTurn:
  			break loop
  		}
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}
  ```

  ```java Java
  try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
      stream.stream()
          .filter(BetaManagedAgentsStreamSessionEvents::isSessionStatusIdle)
          .map(idleEvent -> idleEvent.asSessionStatusIdle().stopReason())
          .takeWhile(stopReason -> !stopReason.isEndTurn())
          .filter(stopReason -> stopReason.isRequiresAction())
          .flatMap(stopReason -> stopReason.asRequiresAction().eventIds().stream())
          .forEach(eventId -> {
              // Look up the custom tool use event and execute it
              var toolEvent = eventsById.get(eventId);
              var result = callTool(toolEvent.name(), toolEvent.input());

              // Send the result back
              client.beta().sessions().events().send(
                  session.id(),
                  EventSendParams.builder()
                      .addEvent(BetaManagedAgentsUserCustomToolResultEventParams.builder()
                          .type(BetaManagedAgentsUserCustomToolResultEventParams.Type.USER_CUSTOM_TOOL_RESULT)
                          .customToolUseId(eventId)
                          .addTextContent(result)
                          .build())
                      .build());
          });
  }
  ```

  ```php PHP
  $stream = $client->beta->sessions->events->streamStream($session->id);

  foreach ($stream as $event) {
      if ($event instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionStatusIdleEvent && $event->stopReason) {
          switch (true) {
              case $event->stopReason instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionRequiresAction:
                  foreach ($event->stopReason->eventIDs as $eventId) {
                      // Look up the custom tool use event and execute it
                      $toolEvent = $eventsById[$eventId];
                      $result = callTool($toolEvent->name, $toolEvent->input);

                      // Send the result back
                      $client->beta->sessions->events->send(
                          $session->id,
                          events: [
                              [
                                  'type' => 'user.custom_tool_result',
                                  'custom_tool_use_id' => $eventId,
                                  'content' => [['type' => 'text', 'text' => $result]],
                              ],
                          ],
                      );
                  }
                  break;
              case $event->stopReason instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionEndTurn:
                  break 2;
          }
      }
  }
  ```

  ```ruby Ruby
  client.beta.sessions.events.stream_events(session.id).each do |event|
    case event
    when Anthropic::Beta::Sessions::BetaManagedAgentsSessionStatusIdleEvent
      stop_reason = event.stop_reason
      case stop_reason
      when Anthropic::Beta::Sessions::BetaManagedAgentsSessionRequiresAction
        stop_reason.event_ids.each do |event_id|
          # Look up the custom tool use event and execute it
          tool_event = events_by_id[event_id]
          result = call_tool.call(tool_event.name, tool_event.input)
          # Send the result back
          client.beta.sessions.events.send_(
            session.id,
            events: [
              {
                type: "user.custom_tool_result",
                custom_tool_use_id: event_id,
                content: [{type: "text", text: result}]
              }
            ]
          )
        end
      when Anthropic::Beta::Sessions::BetaManagedAgentsSessionEndTurn
        break
      end
    end
  end
  ```
</CodeGroup>

### Confirm a tool call

Send a `user.tool_confirmation` event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. See [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests) for which calls wait for a confirmation and how to explain a denial.

The following example approves every pending call:

<CodeGroup>
  ```bash cURL
  exec {stream_fd}< <(curl --fail-with-body -sS -N \
    "https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -H "accept: text/event-stream")

  while IFS= read -r -u "$stream_fd" line; do
    [[ $line == data:* ]] || continue
    event_json="${line#data: }"
    stop_reason=$(jq -r 'select(.type == "session.status_idle") | .stop_reason.type // empty' <<<"$event_json")
    case "$stop_reason" in
      requires_action)
        while IFS= read -r event_id; do
          # Approve the pending tool call
          jq -n --arg id "$event_id" \
            '{events: [{type: "user.tool_confirmation", tool_use_id: $id, result: "allow"}]}' |
            curl --fail-with-body -sS \
              "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
              -H "x-api-key: $ANTHROPIC_API_KEY" \
              -H "anthropic-version: 2023-06-01" \
              -H "anthropic-beta: managed-agents-2026-04-01" \
              -H "content-type: application/json" \
              -d @-
        done < <(jq -r '.stop_reason.event_ids[]' <<<"$event_json")
        ;;
      end_turn)
        break
        ;;
    esac
  done
  exec {stream_fd}<&-
  ```

  ```bash CLI
  # This workflow does not translate well to a one-off shell command.
  # Use one of the SDK examples in this code group instead.
  ```

  ```python Python
  with client.beta.sessions.events.stream(session.id) as stream:
      for event in stream:
          if event.type == "session.status_idle" and (stop_reason := event.stop_reason):
              match stop_reason.type:
                  case "requires_action":
                      for event_id in stop_reason.event_ids:
                          # Approve the pending tool call
                          client.beta.sessions.events.send(
                              session.id,
                              events=[
                                  {
                                      "type": "user.tool_confirmation",
                                      "tool_use_id": event_id,
                                      "result": "allow",
                                  },
                              ],
                          )
                  case "end_turn":
                      break
  ```

  ```typescript TypeScript
  const stream = await client.beta.sessions.events.stream(session.id);

  for await (const event of stream) {
    if (event.type !== "session.status_idle") continue;
    if (event.stop_reason.type === "end_turn") break;
    if (event.stop_reason.type !== "requires_action") continue;

    for (const eventId of event.stop_reason.event_ids) {
      // Approve the pending tool call
      await client.beta.sessions.events.send(session.id, {
        events: [
          {
            type: "user.tool_confirmation",
            tool_use_id: eventId,
            result: "allow",
          },
        ],
      });
    }
  }
  ```

  ```csharp C#
  await foreach (var streamEvent in client.Beta.Sessions.Events.StreamStreaming(session.ID))
  {
      if (streamEvent.Value is not BetaManagedAgentsSessionStatusIdleEvent idle) continue;

      if (idle.StopReason?.Value is BetaManagedAgentsSessionRequiresAction requiresAction)
      {
          foreach (var eventId in requiresAction.EventIds)
          {
              // Approve the pending tool call
              await client.Beta.Sessions.Events.Send(session.ID, new()
              {
                  Events =
                  [
                      new BetaManagedAgentsUserToolConfirmationEventParams
                      {
                          Type = BetaManagedAgentsUserToolConfirmationEventParamsType.UserToolConfirmation,
                          ToolUseID = eventId,
                          Result = BetaManagedAgentsUserToolConfirmationEventParamsResult.Allow,
                      },
                  ],
              });
          }
      }
      else if (idle.StopReason?.Value is BetaManagedAgentsSessionEndTurn)
      {
          break;
      }
  }
  ```

  ```go Go
  	stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
  	defer stream.Close()

  loop:
  	for stream.Next() {
  		event, ok := stream.Current().AsAny().(anthropic.BetaManagedAgentsSessionStatusIdleEvent)
  		if !ok {
  			continue
  		}
  		switch stopReason := event.StopReason.AsAny().(type) {
  		case anthropic.BetaManagedAgentsSessionRequiresAction:
  			for _, eventID := range stopReason.EventIDs {
  				// Approve the pending tool call
  				if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  					Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  						OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
  							Type:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
  							ToolUseID: eventID,
  							Result:    anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultAllow,
  						},
  					}},
  				}); err != nil {
  					panic(err)
  				}
  			}
  		case anthropic.BetaManagedAgentsSessionEndTurn:
  			break loop
  		}
  	}
  	if err := stream.Err(); err != nil {
  		panic(err)
  	}
  ```

  ```java Java
  try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
      stream.stream()
          .filter(BetaManagedAgentsStreamSessionEvents::isSessionStatusIdle)
          .map(idleEvent -> idleEvent.asSessionStatusIdle().stopReason())
          .takeWhile(stopReason -> !stopReason.isEndTurn())
          .filter(stopReason -> stopReason.isRequiresAction())
          .flatMap(stopReason -> stopReason.asRequiresAction().eventIds().stream())
          // Approve each pending tool call
          .forEach(toolUseId -> client.beta().sessions().events().send(
              session.id(),
              EventSendParams.builder()
                  .addEvent(BetaManagedAgentsUserToolConfirmationEventParams.builder()
                      .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                      .toolUseId(toolUseId)
                      .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.ALLOW)
                      .build())
                  .build()));
  }
  ```

  ```php PHP
  $stream = $client->beta->sessions->events->streamStream($session->id);

  foreach ($stream as $event) {
      if ($event instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionStatusIdleEvent && $event->stopReason) {
          switch (true) {
              case $event->stopReason instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionRequiresAction:
                  foreach ($event->stopReason->eventIDs as $eventId) {
                      // Approve the pending tool call
                      $client->beta->sessions->events->send(
                          $session->id,
                          events: [
                              [
                                  'type' => 'user.tool_confirmation',
                                  'tool_use_id' => $eventId,
                                  'result' => 'allow',
                              ],
                          ],
                      );
                  }
                  break;
              case $event->stopReason instanceof \Anthropic\Beta\Sessions\Events\ManagedAgentsSessionEndTurn:
                  break 2;
          }
      }
  }
  ```

  ```ruby Ruby
  client.beta.sessions.events.stream_events(session.id).each do |event|
    case event
    when Anthropic::Beta::Sessions::BetaManagedAgentsSessionStatusIdleEvent
      stop_reason = event.stop_reason
      case stop_reason
      when Anthropic::Beta::Sessions::BetaManagedAgentsSessionRequiresAction
        stop_reason.event_ids.each do |event_id|
          # Approve the pending tool call
          client.beta.sessions.events.send_(
            session.id,
            events: [
              {type: "user.tool_confirmation", tool_use_id: event_id, result: "allow"}
            ]
          )
        end
      when Anthropic::Beta::Sessions::BetaManagedAgentsSessionEndTurn
        break
      end
    end
  end
  ```
</CodeGroup>

## Resume an idle session

Sessions persist between interactions. To resume a session, send a `user.message` event to it as usual:

<CodeGroup>
  ```bash cURL
  # In production, pass the stored ID of the session you want to resume.
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "events": [
      {
        "type": "user.message",
        "content": [
          {"type": "text", "text": "Now run the tests against the changes you made earlier."}
        ]
      }
    ]
  }
  EOF
  ```

  ```bash CLI
  # In production, pass the stored ID of the session you want to resume.
  ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
  events:
    - type: user.message
      content:
        - type: text
          text: Now run the tests against the changes you made earlier.
  YAML
  ```

  ```python Python
  # Resume a previously created session by sending it a new user.message event.
  # In production, pass the stored ID of the session you want to resume.
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "user.message",
              "content": [
                  {
                      "type": "text",
                      "text": "Now run the tests against the changes you made earlier.",
                  },
              ],
          },
      ],
  )
  ```

  ```typescript TypeScript
  // Resume a previously created session by sending it a new user event.
  // In production, pass the stored ID of the session you want to resume.
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.message",
        content: [
          {
            type: "text",
            text: "Now run the tests against the changes you made earlier.",
          },
        ],
      },
    ],
  });
  ```

  ```csharp C#
  // Resume a previously created session by ID. In production, pass the
  // session ID you stored when the session was created.
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
              Content =
              [
                  new BetaManagedAgentsTextBlock
                  {
                      Type = BetaManagedAgentsTextBlockType.Text,
                      Text = "Now run the tests against the changes you made earlier.",
                  },
              ],
          },
      ],
  });
  ```

  ```go Go
  // Resume a previously created session by sending it a new user.message
  // event. In production, pass the stored ID of the session to resume.
  if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  		OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  			Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  			Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  				OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  					Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  					Text: "Now run the tests against the changes you made earlier.",
  				},
  			}},
  		},
  	}},
  }); err != nil {
  	panic(err)
  }
  ```

  ```java Java
  // Resume a previously created session by ID. In production, pass the
  // session ID you stored when the session was created.
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
              .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
              .addTextContent("Now run the tests against the changes you made earlier.")
              .build())
          .build());
  ```

  ```php PHP
  // Resume a previously created session by sending it a new user.message event.
  // In production, pass the session ID you stored when the session was created.
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'user.message',
              'content' => [
                  [
                      'type' => 'text',
                      'text' => 'Now run the tests against the changes you made earlier.',
                  ],
              ],
          ],
      ],
  );
  ```

  ```ruby Ruby
  # Resuming a session is just sending the next event to it. In production,
  # pass the session ID you stored when the session was created.
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.message",
        content: [
          {type: "text", text: "Now run the tests against the changes you made earlier."}
        ]
      }
    ]
  )
  ```
</CodeGroup>

Conversation history is preserved unless the session is explicitly deleted. When a session goes idle, its sandbox is checkpointed. The checkpoint preserves the full sandbox state, including the filesystem, installed packages, and any files the agent created.

<Note>
  Sandbox state is preserved for only 30 days after the sandbox is created, and activity does not extend this window. After 30 days the sandbox state (files, installed tools, and so on) is unrecoverable, and a resumed session starts from a fresh sandbox. If your workflow depends on sandbox contents, have the agent write important artifacts to [outputs](https://platform.claude.com/docs/en/managed-agents/define-outcomes#retrieving-deliverables) before the window ends.
</Note>

## Interrupt the agent

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

<CodeGroup>
  ```bash cURL
  # Agent is currently analyzing a file...
  # Interrupt with a new direction:
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "events": [
      {"type": "user.interrupt"},
      {
        "type": "user.message",
        "content": [
          {"type": "text", "text": "Instead, focus on fixing the bug in line 42."}
        ]
      }
    ]
  }
  EOF
  ```

  ```bash CLI
  # Agent is currently analyzing a file...
  # Interrupt with a new direction:
  ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
  events:
    - type: user.interrupt
    - type: user.message
      content:
        - type: text
          text: Instead, focus on fixing the bug in line 42.
  YAML
  ```

  ```python Python
  # Agent is currently analyzing a file...
  # Interrupt with a new direction:
  client.beta.sessions.events.send(
      session.id,
      events=[
          {"type": "user.interrupt"},
          {
              "type": "user.message",
              "content": [
                  {
                      "type": "text",
                      "text": "Instead, focus on fixing the bug in line 42.",
                  },
              ],
          },
      ],
  )
  ```

  ```typescript TypeScript
  // Agent is currently analyzing a file...
  // Interrupt with a new direction:
  await client.beta.sessions.events.send(session.id, {
    events: [
      { type: "user.interrupt" },
      {
        type: "user.message",
        content: [
          {
            type: "text",
            text: "Instead, focus on fixing the bug in line 42.",
          },
        ],
      },
    ],
  });
  ```

  ```csharp C#
  // Agent is currently analyzing a file...
  // Interrupt with a new direction:
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserInterruptEventParams
          {
              Type = BetaManagedAgentsUserInterruptEventParamsType.UserInterrupt,
          },
          new BetaManagedAgentsUserMessageEventParams
          {
              Type = BetaManagedAgentsUserMessageEventParamsType.UserMessage,
              Content =
              [
                  new BetaManagedAgentsTextBlock
                  {
                      Type = BetaManagedAgentsTextBlockType.Text,
                      Text = "Instead, focus on fixing the bug in line 42.",
                  },
              ],
          },
      ],
  });
  ```

  ```go Go
  // Agent is currently analyzing a file...
  // Interrupt with a new direction:
  if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{
  		{
  			OfUserInterrupt: &anthropic.BetaManagedAgentsUserInterruptEventParams{
  				Type: anthropic.BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt,
  			},
  		},
  		{
  			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
  				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
  				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
  					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
  						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
  						Text: "Instead, focus on fixing the bug in line 42.",
  					},
  				}},
  			},
  		},
  	},
  }); err != nil {
  	panic(err)
  }
  ```

  ```java Java
  // Agent is currently analyzing a file...
  // Interrupt with a new direction:
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(BetaManagedAgentsUserInterruptEventParams.builder()
              .type(BetaManagedAgentsUserInterruptEventParams.Type.USER_INTERRUPT)
              .build())
          .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
              .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
              .addTextContent("Instead, focus on fixing the bug in line 42.")
              .build())
          .build());
  ```

  ```php PHP
  // Agent is currently analyzing a file...
  // Interrupt with a new direction:
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          ['type' => 'user.interrupt'],
          [
              'type' => 'user.message',
              'content' => [
                  [
                      'type' => 'text',
                      'text' => 'Instead, focus on fixing the bug in line 42.',
                  ],
              ],
          ],
      ],
  );
  ```

  ```ruby Ruby
  # Agent is currently analyzing a file...
  # Interrupt with a new direction:
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {type: "user.interrupt"},
      {
        type: "user.message",
        content: [
          {type: "text", text: "Instead, focus on fixing the bug in line 42."}
        ]
      }
    ]
  )
  ```
</CodeGroup>

The call returns as soon as the events are queued. The interrupt then takes effect in this order:

1. The agent applies the interrupt. Until then, the interrupt's `processed_at` stays null and the session stays `running`. A model response in progress stops immediately, but the interrupt can take longer to apply while tool calls are running.
2. The `user.interrupt` event appears on the stream, and the interrupted turn ends with a `session.status_idle` event.
3. The agent starts its next turn with the `user.message` you sent after the interrupt.

The idle event's `stop_reason.type` is `end_turn`, the same value as a turn that finishes on its own.

## List past events

Retrieve the full event history for a session:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json"
  ```

  ```bash CLI
  ant beta:sessions:events list --session-id "$SESSION_ID" --format jsonl
  ```

  ```python Python
  events = client.beta.sessions.events.list(session.id)
  for event in events.data:
      print(f"[{event.type}] {event.processed_at}")
  ```

  ```typescript TypeScript
  const events = await client.beta.sessions.events.list(session.id);
  for (const event of events.data) {
    console.log(`[${event.type}] ${event.processed_at}`);
  }
  ```

  ```csharp C#
  var events = await client.Beta.Sessions.Events.List(session.ID);
  foreach (var sessionEvent in events.Items)
  {
      Console.WriteLine($"[{sessionEvent.Json.GetProperty("type").GetString()}] {sessionEvent.ProcessedAt}");
  }
  ```

  ```go Go
  events, err := client.Beta.Sessions.Events.List(ctx, session.ID, anthropic.BetaSessionEventListParams{})
  if err != nil {
  	panic(err)
  }
  for _, event := range events.Data {
  	fmt.Printf("[%s] %s\n", event.Type, event.ProcessedAt)
  }
  ```

  ```java Java
  var events = client.beta().sessions().events().list(session.id());
  for (var event : events.data()) {
      var eventJson = event._json().orElseThrow().convert(JsonNode.class);
      var processedAt = eventJson.path("processed_at");
      IO.println("[" + eventJson.get("type").asText() + "] "
          + (processedAt.isTextual() ? processedAt.asText() : "null"));
  }
  ```

  ```php PHP
  $events = $client->beta->sessions->events->list($session->id);
  foreach ($events->data as $event) {
      $processedAt = ($event->processedAt ?? null)?->format(DATE_RFC3339) ?? 'null';
      echo "[{$event->type}] {$processedAt}\n";
  }
  ```

  ```ruby Ruby
  events = client.beta.sessions.events.list(session.id)
  events.data.each { puts "[#{it.type}] #{it.processed_at}" }
  ```
</CodeGroup>

Pass a `types` filter to return only specific event types:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true&types[]=agent.tool_use&types[]=agent.tool_result" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01"
  ```

  ```bash CLI
  ant beta:sessions:events list --session-id "$SESSION_ID" \
    --type agent.tool_use --type agent.tool_result \
    --format jsonl
  ```

  ```python Python
  events = client.beta.sessions.events.list(
      session.id,
      types=["agent.tool_use", "agent.tool_result"],
  )
  for event in events.data:
      print(f"[{event.type}] {event.processed_at}")
  ```

  ```typescript TypeScript
  const events = await client.beta.sessions.events.list(session.id, {
    types: ["agent.tool_use", "agent.tool_result"],
  });
  for (const event of events.data) {
    console.log(`[${event.type}] ${event.processed_at}`);
  }
  ```

  ```csharp C#
  var events = await client.Beta.Sessions.Events.List(session.ID, new()
  {
      Types = ["agent.tool_use", "agent.tool_result"],
  });
  foreach (var sessionEvent in events.Items)
  {
      Console.WriteLine($"[{sessionEvent.Json.GetProperty("type").GetString()}] {sessionEvent.ProcessedAt}");
  }
  ```

  ```go Go
  events, err := client.Beta.Sessions.Events.List(ctx, session.ID, anthropic.BetaSessionEventListParams{
  	Types: []anthropic.BetaManagedAgentsSessionEventType{
  		anthropic.BetaManagedAgentsSessionEventTypeAgentToolUse,
  		anthropic.BetaManagedAgentsSessionEventTypeAgentToolResult,
  	},
  })
  if err != nil {
  	panic(err)
  }
  for _, event := range events.Data {
  	fmt.Printf("[%s] %s\n", event.Type, event.ProcessedAt)
  }
  ```

  ```java Java
  var events = client.beta().sessions().events().list(
      session.id(),
      EventListParams.builder()
          .addType(BetaManagedAgentsSessionEventType.AGENT_TOOL_USE)
          .addType(BetaManagedAgentsSessionEventType.AGENT_TOOL_RESULT)
          .build());
  for (var event : events.data()) {
      event.agentToolUse().ifPresent(toolUse ->
          IO.println("[" + toolUse.type() + "] " + toolUse.processedAt()));
      event.agentToolResult().ifPresent(toolResult ->
          IO.println("[" + toolResult.type() + "] " + toolResult.processedAt()));
  }
  ```

  ```php PHP
  // In PHP, pass the types you want on EventListParams; see the Anthropic PHP SDK.
  ```

  ```ruby Ruby
  events = client.beta.sessions.events.list(
    session.id,
    types: ["agent.tool_use", "agent.tool_result"]
  )
  events.data.each { puts "[#{it.type}] #{it.processed_at}" }
  ```
</CodeGroup>

## Send system messages

On a [supported model](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#supported-models), send a `system.message` event to give the agent privileged system-level context. The context applies to the accompanying turn and all subsequent turns. Use it when the agent needs updated system-level guidance mid-session, for example a different persona, revised constraints, or context fetched at runtime.

The event's `content` accepts 1–1000 text items. The content is appended to the session's system context as a `role: "system"` turn. It doesn't replace the top-level system prompt, which the `system` field on the agent definition sets.

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?beta=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "events": [
      {
        "type": "system.message",
        "content": [
          {"type": "text", "text": "The user's current timezone is America/New_York."}
        ]
      }
    ]
  }
  EOF
  ```

  ```bash CLI
  ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
  events:
    - type: system.message
      content:
        - type: text
          text: "The user's current timezone is America/New_York."
  YAML
  ```

  ```python Python
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "system.message",
              "content": [
                  {
                      "type": "text",
                      "text": "The user's current timezone is America/New_York.",
                  },
              ],
          },
      ],
  )
  ```

  ```typescript TypeScript
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "system.message",
        content: [
          {
            type: "text",
            text: "The user's current timezone is America/New_York.",
          },
        ],
      },
    ],
  });
  ```

  ```csharp C#
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsSystemMessageEventParams
          {
              Type = BetaManagedAgentsSystemMessageEventParamsType.SystemMessage,
              Content =
              [
                  new BetaManagedAgentsSystemContentBlock
                  {
                      Type = BetaManagedAgentsSystemContentBlockType.Text,
                      Text = "The user's current timezone is America/New_York.",
                  },
              ],
          },
      ],
  });
  ```

  ```go Go
  if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  		OfSystemMessage: &anthropic.BetaManagedAgentsSystemMessageEventParams{
  			Type: anthropic.BetaManagedAgentsSystemMessageEventParamsTypeSystemMessage,
  			Content: []anthropic.BetaManagedAgentsSystemContentBlockParam{{
  				Type: anthropic.BetaManagedAgentsSystemContentBlockTypeText,
  				Text: "The user's current timezone is America/New_York.",
  			}},
  		},
  	}},
  }); err != nil {
  	panic(err)
  }
  ```

  ```java Java
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(BetaManagedAgentsSystemMessageEventParams.builder()
              .type(BetaManagedAgentsSystemMessageEventParams.Type.SYSTEM_MESSAGE)
              .addTextContent("The user's current timezone is America/New_York.")
              .build())
          .build());
  ```

  ```php PHP
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'system.message',
              'content' => [
                  [
                      'type' => 'text',
                      'text' => "The user's current timezone is America/New_York.",
                  ],
              ],
          ],
      ],
  );
  ```

  ```ruby Ruby
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "system.message",
        content: [
          {type: "text", text: "The user's current timezone is America/New_York."}
        ]
      }
    ]
  )
  ```
</CodeGroup>

### Supported models

`system.message` is supported by these models:

* Claude Fable 5.1
* Claude Mythos 5.1
* Claude Fable 5
* Claude Mythos 5
* Claude Opus 5.5
* Claude Opus 5
* Claude Opus 4.8
* Claude Sonnet 5.5
* Claude Haiku 5.5

If the agent's primary model does not support mid-conversation system injection, the event is rejected with a `model_does_not_support_mid_conversation_system` validation error. Subagent models are not checked, because `system.message` lands on the primary thread only.

### System messages while a tool call is pending

While the session is idle with a `requires_action` stop reason, a `system.message` must trail a tool result event in the same request. Sent on its own or with a `user.message`, it is rejected until the pending tool events are resolved.

## Next steps

<CardGroup cols={2}>
  <Card title="Preview responses with event deltas" icon="text" href="https://platform.claude.com/docs/en/managed-agents/event-deltas">
    Render the agent's response text while the model is still generating it.
  </Card>

  <Card title="Inspect sessions and track usage" icon="magnifying-glass" href="https://platform.claude.com/docs/en/managed-agents/session-observability">
    Inspect a session in the Claude Console and read its token usage and list cost.
  </Card>

  <Card title="Subscribe to webhooks" icon="link" href="https://platform.claude.com/docs/en/managed-agents/webhooks">
    Get notified when major events happen without polling.
  </Card>

  <Card title="Event types" icon="book" href="https://platform.claude.com/docs/en/managed-agents/reference#event-types">
    Look up every event type a session can send or receive.
  </Card>
</CardGroup>
