---
title: Handle errors
url: https://platform.claude.com/docs/en/api/handle-errors
description: Use the SDK to catch Claude API errors by error code, HTTP status, or connection failure and to handle an error that arrives in a stream.
---

Use the SDK to catch Claude API errors by error code, HTTP status, or connection failure and to handle an error that arrives in a stream. To learn what each error means or to call the API without the SDK, see [Claude API errors](https://platform.claude.com/docs/en/api/errors).

<Note>
  The examples on this page need the [latest version of the SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview#latest-versions).
</Note>

## Catch errors by kind

This example handles one [error code](https://platform.claude.com/docs/en/api/errors#error-codes), one HTTP status, a connection failure, and every other error response:

<CodeGroup exclude="shell:cURL, shell:CLI">
  ```python Python
  client = anthropic.Anthropic()

  try:
      client.messages.create(
          model="claude-opus-5-5",
          max_tokens=1024,
          messages=[{"role": "user", "content": "Hello, Claude"}],
      )
  except anthropic.EnforcedSpendLimitReachedError as e:
      # One error code: enforced_spend_limit_reached
      print("Monthly spend cap reached:", e.api_message)
  except anthropic.RateLimitError as e:
      # One HTTP status: any other 429
      print("Rate limited. Request ID:", e.request_id)
  except anthropic.APIConnectionError:
      # An error with no response, such as a network failure or a timeout
      print("Connection failed")
  except anthropic.APIStatusError as e:
      # Every other error response
      print(e.status_code)  # HTTP status
      print(e.type)  # error.type
      print(e.api_message)  # error.message
      print(e.error_code)  # error.details.error_code if any
      print(e.details)  # error.details if any
      print(e.request_id)  # request_id
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  try {
    await client.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    });
  } catch (err) {
    if (err instanceof Anthropic.EnforcedSpendLimitReachedError) {
      // One error code: enforced_spend_limit_reached
      console.log("Monthly spend cap reached:", err.apiMessage);
    } else if (err instanceof Anthropic.RateLimitError) {
      // One HTTP status: any other 429
      console.log("Rate limited. Request ID:", err.requestID);
    } else if (err instanceof Anthropic.APIConnectionError) {
      // An error with no response, such as a network failure or a timeout
      console.log("Connection failed");
    } else if (err instanceof Anthropic.APIError) {
      // Every other error response
      console.log(err.status); // HTTP status
      console.log(err.type); // error.type
      console.log(err.apiMessage); // error.message
      console.log(err.errorCode); // error.details.error_code if any
      console.log(err.details); // error.details if any
      console.log(err.requestID); // request_id
    } else {
      throw err;
    }
  }
  ```

  ```csharp C#
  using Anthropic.Exceptions;
  using Anthropic.Models;
  using Anthropic.Models.Messages;

  AnthropicClient client = new();

  try
  {
      await client.Messages.Create(new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new UserMessageParam { Content = "Hello, Claude" }]
      });
  }
  catch (AnthropicEnforcedSpendLimitReachedException e)
  {
      // One error code: enforced_spend_limit_reached
      Console.WriteLine($"Monthly spend cap reached: {e.ApiMessage}");
  }
  catch (AnthropicRateLimitException e)
  {
      // One HTTP status: any other 429
      Console.WriteLine($"Rate limited. Request ID: {e.RequestID}");
  }
  catch (Exception e) when (e is AnthropicIOException or TaskCanceledException)
  {
      // An error with no response, such as a network failure or a timeout
      Console.WriteLine("Connection failed");
  }
  catch (AnthropicApiException e)
  {
      // Every other error response
      Console.WriteLine((int)e.StatusCode); // HTTP status
      Console.WriteLine(e.Type?.Raw()); // error.type
      Console.WriteLine(e.ApiMessage); // error.message
      Console.WriteLine(e.ErrorCode); // error.details.error_code if any
      Console.WriteLine(e.Details); // error.details if any
      Console.WriteLine(e.RequestID); // request_id
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  _, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  })

  // The Go SDK has one error type. Branch on the error's code and status.
  var apierr *anthropic.Error
  if errors.As(err, &apierr) {
  	switch {
  	case apierr.ErrorCode() == anthropic.ErrorCodeEnforcedSpendLimitReached:
  		// One error code: enforced_spend_limit_reached
  		fmt.Println("Monthly spend cap reached:", apierr.Message)
  	case apierr.StatusCode == http.StatusTooManyRequests:
  		// One HTTP status: any other 429
  		fmt.Println("Rate limited. Request ID:", apierr.RequestID)
  	default:
  		// Every other error response
  		fmt.Println(apierr.StatusCode)        // HTTP status
  		fmt.Println(apierr.Type())            // error.type
  		fmt.Println(apierr.Message)           // error.message
  		fmt.Println(apierr.ErrorCode())       // error.details.error_code if any
  		fmt.Println(apierr.Details.RawJSON()) // error.details if any
  		fmt.Println(apierr.RequestID)         // request_id
  	}
  } else if err != nil {
  	// Any other error, such as a network failure or a timeout
  	fmt.Println("Connection failed")
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.errors.AnthropicIoException;
  import com.anthropic.errors.AnthropicServiceException;
  import com.anthropic.errors.RateLimitException;
  import com.anthropic.models.EnforcedSpendLimitReachedException;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024L)
          .addUserMessage("Hello, Claude")
          .build();

      try {
          client.messages().create(params);
      } catch (EnforcedSpendLimitReachedException e) {
          // One error code: enforced_spend_limit_reached
          IO.println("Monthly spend cap reached: " + e.apiMessage().orElse(""));
      } catch (RateLimitException e) {
          // One HTTP status: any other 429
          IO.println("Rate limited. Request ID: " + e.requestId().orElse(""));
      } catch (AnthropicIoException e) {
          // An error with no response, such as a network failure or a timeout
          IO.println("Connection failed");
      } catch (AnthropicServiceException e) {
          // Every other error response
          IO.println(e.statusCode()); // HTTP status
          IO.println(e.type().orElse(null)); // error.type
          IO.println(e.apiMessage().orElse(null)); // error.message
          IO.println(e.errorCode().orElse(null)); // error.details.error_code if any
          IO.println(e.errorDetails().orElse(null)); // error.details if any
          IO.println(e.requestId().orElse(null)); // request_id
      }
  }
  ```

  ```php PHP
  use Anthropic\Core\Exceptions\APIConnectionException;
  use Anthropic\Core\Exceptions\APIStatusException;
  use Anthropic\Core\Exceptions\RateLimitException;
  use Anthropic\EnforcedSpendLimitReachedException;
  use Anthropic\Messages\Model;

  $client = new Client();

  try {
      $client->messages->create(
          model: Model::CLAUDE_OPUS_5_5,
          maxTokens: 1024,
          messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      );
  } catch (EnforcedSpendLimitReachedException $e) {
      // One error code: enforced_spend_limit_reached
      echo 'Monthly spend cap reached: ', $e->getAPIMessage(), PHP_EOL;
  } catch (RateLimitException $e) {
      // One HTTP status: any other 429
      echo 'Rate limited. Request ID: ', $e->getRequestID(), PHP_EOL;
  } catch (APIConnectionException) {
      // An error with no response, such as a network failure or a timeout
      echo 'Connection failed', PHP_EOL;
  } catch (APIStatusException $e) {
      // Every other error response
      echo $e->status, PHP_EOL; // HTTP status
      echo $e->getType(), PHP_EOL; // error.type
      echo $e->getAPIMessage(), PHP_EOL; // error.message
      echo $e->getErrorCode(), PHP_EOL; // error.details.error_code if any
      echo json_encode($e->getDetails()), PHP_EOL; // error.details if any
      echo $e->getRequestID(), PHP_EOL; // request_id
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  begin
    client.messages.create(
      model: Anthropic::Model::CLAUDE_OPUS_5_5,
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    )
  rescue Anthropic::EnforcedSpendLimitReachedError => e
    # One error code: enforced_spend_limit_reached
    puts "Monthly spend cap reached: #{e.api_message}"
  rescue Anthropic::Errors::RateLimitError => e
    # One HTTP status: any other 429
    puts "Rate limited. Request ID: #{e.request_id}"
  rescue Anthropic::Errors::APIConnectionError
    # An error with no response, such as a network failure or a timeout
    puts "Connection failed"
  rescue Anthropic::Errors::APIStatusError => e
    # Every other error response
    puts e.status # HTTP status
    puts e.type # error.type as a symbol
    puts e.api_message # error.message
    puts e.error_code # error.details.error_code as a symbol if any
    puts e.details # error.details if any
    puts e.request_id # request_id
  end
  ```
</CodeGroup>

An error reaches your code after the SDK’s own retries, if any, have failed (see [Retries](https://platform.claude.com/docs/en/api/errors#retries)). For what each status means, see [HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors).

Keep a narrow case before a broad one. The Messages API returns `enforced_spend_limit_reached`, the code for the [monthly spend cap](https://platform.claude.com/docs/en/api/rate-limits#reaching-your-spend-cap), with a 429. If the branch for a 429 came first, it would catch that code too.

To handle another case, such as a 404, see [SDK error types](https://platform.claude.com/docs/en/api/errors#sdk-error-types).

## Handle a specific error code

To handle another error code, add its branch to [Catch errors by kind](https://platform.claude.com/docs/en/api/handle-errors#catch-errors-by-kind) before any broader branch.

Each code has its own class or constant named after the code, such as `anthropic.EnforcedSpendLimitReachedError` (typescript: `Anthropic.EnforcedSpendLimitReachedError`; ruby: `Anthropic::EnforcedSpendLimitReachedError`; java: `com.anthropic.models.EnforcedSpendLimitReachedException`; php: `Anthropic\EnforcedSpendLimitReachedException`; csharp: `Anthropic.Models.AnthropicEnforcedSpendLimitReachedException`; go: `anthropic.ErrorCodeEnforcedSpendLimitReached`). Classes for other codes might sit in other namespaces. To find one, search the SDK’s source for the class name. A method’s doc comment lists the class or constant for each code that the method can return.

For the full list of codes, see [`ErrorDetails`](https://platform.claude.com/docs/en/api/$shared#error_details) in the API reference.

## Handle an error in a stream

After a stream starts, the API has already returned a 200, so it sends an error as an [error event](https://platform.claude.com/docs/en/build-with-claude/streaming#error-events). The SDK doesn’t retry the request.

Every error event reaches you as `APIStatusError` (typescript: `APIError`; csharp: `AnthropicSseException`; java: `SseException`; php: `APIStatusException`; go: `*anthropic.Error`). Its HTTP status is the stream’s 200 or is missing. So a branch for one status or for one code’s class doesn’t catch it. Instead, check its `error.type` for one of the types in [HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors):

<CodeGroup exclude="shell:cURL, shell:CLI">
  ```python Python
  client = anthropic.Anthropic()

  try:
      with client.messages.stream(
          model="claude-opus-5-5",
          max_tokens=1024,
          messages=[{"role": "user", "content": "Hello, Claude"}],
      ) as stream:
          for text in stream.text_stream:
              print(text, end="", flush=True)
  except anthropic.APIStatusError as e:
      if e.type == "overloaded_error":
          # One error.type: overloaded_error
          print("\nOverloaded:", e.api_message)
      else:
          raise
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  try {
    await client.messages
      .stream({
        model: "claude-opus-5-5",
        max_tokens: 1024,
        messages: [{ role: "user", content: "Hello, Claude" }]
      })
      .on("text", (text) => {
        process.stdout.write(text);
      })
      .finalMessage();
  } catch (err) {
    if (err instanceof Anthropic.APIError && err.type === "overloaded_error") {
      // One error.type: overloaded_error
      console.log("\nOverloaded:", err.apiMessage);
    } else {
      throw err;
    }
  }
  ```

  ```csharp C#
  using Anthropic.Exceptions;
  using Anthropic.Models.Messages;

  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus5_5,
      MaxTokens = 1024,
      Messages = [new UserMessageParam { Content = "Hello, Claude" }]
  };

  try
  {
      await foreach (var streamEvent in client.Messages.CreateStreaming(parameters))
      {
          if (
              streamEvent.TryPickContentBlockDelta(out var deltaEvent)
              && deltaEvent.Delta.TryPickText(out var textDelta)
          )
          {
              Console.Write(textDelta.Text);
          }
      }
  }
  // The base class of AnthropicSseException (error events)
  // and AnthropicApiException (error responses)
  catch (AnthropicServiceException e) when (e.Type?.Raw() == "overloaded_error")
  {
      // One error.type: overloaded_error
      Console.WriteLine($"\nOverloaded: {e.ApiMessage}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  stream := client.Messages.NewStreaming(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5_5,
  	MaxTokens: 1024,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  	},
  })

  for stream.Next() {
  	event := stream.Current()
  	switch eventVariant := event.AsAny().(type) {
  	case anthropic.ContentBlockDeltaEvent:
  		switch deltaVariant := eventVariant.Delta.AsAny().(type) {
  		case anthropic.TextDelta:
  			fmt.Print(deltaVariant.Text)
  		}
  	}
  }

  err := stream.Err()
  var apierr *anthropic.Error
  if errors.As(err, &apierr) && apierr.Type() == anthropic.ErrorTypeOverloadedError {
  	// One error.type: overloaded_error
  	fmt.Println("\nOverloaded:", apierr.Message)
  } else if err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.errors.AnthropicServiceException;
  import com.anthropic.models.ErrorType;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024L)
          .addUserMessage("Hello, Claude")
          .build();

      try (var streamResponse = client.messages().createStreaming(params)) {
          streamResponse.stream().forEach(event -> {
              event.contentBlockDelta().ifPresent(deltaEvent ->
                  deltaEvent.delta().text().ifPresent(textDelta ->
                      IO.print(textDelta.text())
                  )
              );
          });
      } catch (AnthropicServiceException e) {
          // Catches error events (SseException) and error responses
          if (ErrorType.OVERLOADED_ERROR.equals(e.type().orElse(null))) {
              // One error.type: overloaded_error
              IO.println("\nOverloaded: " + e.apiMessage().orElse(""));
          } else {
              throw e;
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Core\Exceptions\APIStatusException;
  use Anthropic\Messages\Model;
  use Anthropic\Messages\RawContentBlockDeltaEvent;
  use Anthropic\Messages\TextDelta;

  $client = new Client();

  try {
      $stream = $client->messages->createStream(
          model: Model::CLAUDE_OPUS_5_5,
          maxTokens: 1024,
          messages: [['role' => 'user', 'content' => 'Hello, Claude']],
      );

      foreach ($stream as $event) {
          if (
              $event instanceof RawContentBlockDeltaEvent
              && $event->delta instanceof TextDelta
          ) {
              echo $event->delta->text;
          }
      }
  } catch (APIStatusException $e) {
      if ($e->getType() === 'overloaded_error') {
          // One error.type: overloaded_error
          echo PHP_EOL, 'Overloaded: ', $e->getAPIMessage(), PHP_EOL;
      } else {
          throw $e;
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  begin
    stream = client.messages.stream(
      model: Anthropic::Model::CLAUDE_OPUS_5_5,
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    )

    stream.text.each { |text| print(text) }
  rescue Anthropic::Errors::APIStatusError => e
    if e.type == :overloaded_error
      # One error.type: overloaded_error
      puts "\nOverloaded: #{e.api_message}"
    else
      raise
    end
  end
  ```
</CodeGroup>

An error event can also have an [error code](https://platform.claude.com/docs/en/api/errors#error-codes). Read it from `error_code` (typescript: `errorCode`; csharp: `ErrorCode`; java: `errorCode().orElse(null)`; php: `getErrorCode()`; go: `ErrorCode()`) and compare it with the code that you want to handle, such as `"enforced_spend_limit_reached"` (ruby: `:enforced_spend_limit_reached`; go: `anthropic.ErrorCodeEnforcedSpendLimitReached`).

A stream can fail in two other ways:

* **The request fails before the stream starts:** You get the errors in [Catch errors by kind](https://platform.claude.com/docs/en/api/handle-errors#catch-errors-by-kind).
* **The connection drops in mid-stream:** No error event arrives, and the connection branch in [Catch errors by kind](https://platform.claude.com/docs/en/api/handle-errors#catch-errors-by-kind) might not catch the error. To find what does, see [SDK error types](https://platform.claude.com/docs/en/api/errors#sdk-error-types).

To continue the response after a stream fails, see [Error recovery](https://platform.claude.com/docs/en/build-with-claude/streaming#error-recovery).
