---
title: Claude API errors
url: https://platform.claude.com/docs/en/api/errors
description: Understand the HTTP status codes, error response shape, and request IDs the Claude API returns, and handle errors with the SDK's typed exceptions.
---

To find the SDK error that an API error becomes, see [SDK error types](https://platform.claude.com/docs/en/api/errors#sdk-error-types). To catch it in your code, see [Handle errors](https://platform.claude.com/docs/en/api/handle-errors).

## HTTP errors

The API follows a predictable HTTP error code format:

* 400 - `invalid_request_error`: There’s an issue with the format or content of your request. The API might also use this error type for other 4XX status codes not listed in this section. The API also returns a 400 when usage reaches an organization or workspace [spend limit you set](https://platform.claude.com/docs/en/api/rate-limits#setting-your-own-spend-limit). Limits on the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace) are the exception: they can return a 429 instead. If the message names a problem with your request, look for it in [Common validation errors](https://platform.claude.com/docs/en/api/errors#common-validation-errors).

* 401 - `authentication_error`: There’s an issue with your [API key](https://platform.claude.com/docs/en/get-api-key) (for example, it’s malformed, revoked, or expired; see [Key expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration)). On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.

  On Claude Models on Google Cloud (Anthropic managed), a 401 can mean a problem with your [Google Cloud credentials](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#authentication).

  A 401 whose message begins `CORS requests are not allowed for this Organization` is not a problem with your API key. The request included an `Origin` header, which browsers add, and your organization cannot call the Claude API directly from a browser. The message continues `because of custom retention settings` or `because of its settings`. The first appears only for data retention arrangements such as zero data retention (ZDR); the second is the general case. No change to the browser request fixes it, so send the request from your own back end; see [Browser-based applications](https://platform.claude.com/docs/en/manage-claude/authentication#browser-based-applications).

* 402 - `billing_error`: There’s an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you’re using Claude Platform on AWS.

* 403 - `permission_error`: Your API key does not have permission to use the specified resource. Check your organization’s access and workspace settings in the [Claude Console](https://platform.claude.com).

  On Claude Models on Google Cloud (Anthropic managed), Google Cloud checks each request before forwarding it to Anthropic. To fix a 403, do the following:

  * Check that `claude.googleapis.com` is enabled on your project.
  * Check that the caller’s [IAM role](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#iam-roles) allows the request.
  * If the 403 says `Permission 'UNKNOWN' denied`, check the request’s path. Google Cloud doesn’t offer that route, so no IAM role fixes it.

* 404 - `not_found_error`: The requested resource was not found. Check the endpoint path and any resource IDs in the request URL.

* 409 - `conflict_error`: The request conflicts with the current state of a resource. For example, the resource was modified concurrently, or a value that must be unique is already in use. Resolve the conflict, then retry the request.

* 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](https://platform.claude.com/docs/en/api/errors#request-size-limits) for per-endpoint maximums.

* 429 - `rate_limit_error`: Your organization has hit a [rate limit](https://platform.claude.com/docs/en/api/rate-limits), reached its usage tier’s monthly spend cap, or reached a spend limit on the Claude Code workspace. A tier spend-cap 429 has no `retry-after` header and keeps failing until access resumes; see [Reaching your spend cap](https://platform.claude.com/docs/en/api/rate-limits#reaching-your-spend-cap) for how to recognize it. A sharp increase in usage can also cause a 429 even while you’re under your rate limits; see [Ramp limits](https://platform.claude.com/docs/en/api/rate-limits#ramp-limits).

  To tell the spend cap from a rate limit in code, check the [error code](https://platform.claude.com/docs/en/api/errors#error-codes).

* 500 - `api_error`: An unexpected error has occurred internal to Anthropic’s systems. Retry only if the response’s `x-should-retry` header isn’t `false` (see [Retries](https://platform.claude.com/docs/en/api/errors#retries)). If the error persists, contact support with the [request ID](https://platform.claude.com/docs/en/api/errors#request-id). If the error type is `timeout_error` instead, see the 504 entry.

* 504 - `timeout_error`: The request timed out while processing. The API also returns `timeout_error` with other status codes, such as a 500 when a request reaches the server’s time limit before the response starts. For long-running Messages API requests, use the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming). See [Long requests](https://platform.claude.com/docs/en/api/errors#long-requests) for more options.

* 529 - `overloaded_error`: The API is temporarily overloaded.

  <Warning>
    A 529 error can occur when the API experiences high traffic across all users.
  </Warning>

When receiving a [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) response over server-sent events (SSE), an error can occur after the API returns a 200 response. In that case, error handling doesn’t follow these standard mechanisms. See [Error events](https://platform.claude.com/docs/en/build-with-claude/streaming#error-events) for the shape of mid-stream errors.

The SDK doesn’t retry an error in a stream. To catch one, see [Handle an error in a stream](https://platform.claude.com/docs/en/api/handle-errors#handle-an-error-in-a-stream).

### Retries

By default, the SDK retries a failed request up to two times (three attempts in all). To change the number of retries, set `max_retries` (typescript, php: `maxRetries`; java: `.maxRetries()`; csharp: `MaxRetries`; go: `option.WithMaxRetries()`) on the client. A value of `0` turns retries off.

For each failed attempt, the SDK determines two things:

* **Whether the SDK retries:** If the response has an `x-should-retry` header (`true` or `false`), the SDK follows it. Otherwise, the SDK retries connection errors, timeouts, and the statuses 408, 409, 429, and 500 and above.
* **How long the SDK waits:** If the response has a `retry-after` header, the SDK waits as long as the header says. Otherwise, it uses exponential backoff from 0.5 to 8 seconds.

The Go SDK retries some create methods in fewer cases. See [Retries for create methods in the Go SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go#retries-for-create-methods).

Without the SDK, follow `x-should-retry` and `retry-after` in your own code and use backoff and a retry limit.

## Request size limits

The first-party Claude API enforces these request size limits. For other platforms, see the [API overview](https://platform.claude.com/docs/en/api/overview#request-size-limits).

| Endpoint type | Maximum request size |
| ----- | ----- |
| Messages API | 128 MB |
| Token Counting API | 128 MB |
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | 256 MB |
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files) | 500 MB |

If you exceed these limits, you’ll receive a 413 `request_too_large` error. On the first-party Claude API, Cloudflare returns this error before the request reaches the API servers.

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

Under the [API versioning policy](https://platform.claude.com/docs/en/api/versioning), the values within these objects can expand, and new `type` values can appear.

### Error codes

Some errors also have an error code in `error.details.error_code`. One `type` can cover several causes, and a code names one of them.

For example, hitting a rate limit and reaching your [monthly spend cap](https://platform.claude.com/docs/en/api/rate-limits#reaching-your-spend-cap) both cause a 429 `rate_limit_error`. On the Messages API, the spend-cap response adds a code:

```json JSON
{
  "type": "error",
  "error": {
    "type": "rate_limit_error",
    "message": "You have reached your API usage limits: ...",
    "details": { "error_code": "enforced_spend_limit_reached" }
  },
  "request_id": "req_018EeWyXxfu5pfWkrYcMdjWG"
}
```

Other APIs that return this 429, such as Claude Managed Agents, don’t add the code. There, only the `message` tells the two causes apart, and you shouldn’t match it in code. A spend-cap 429 keeps failing until access resumes, so limit your retries after a 429.

The set of codes can grow. If an error has no code or has a code that you don’t recognize, handle it by its `type` or HTTP status.

For the full list of codes, see [`ErrorDetails`](https://platform.claude.com/docs/en/api/$shared#error_details) in the API reference. To find the codes that a method can return, see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code).

## SDK error types

This section lists what to catch or check in the SDK for each kind of error. To write a handler, see [Handle errors](https://platform.claude.com/docs/en/api/handle-errors).

<Tabs>
  <Tab title="Python">
    These classes are in the `anthropic` package unless a row names another. A class also catches its subclasses, so put the narrower class first. For example, `RateLimitError` also catches `EnforcedSpendLimitReachedError`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `anthropic.EnforcedSpendLimitReachedError` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `BadRequestError` |
    | 401 | `AuthenticationError` |
    | 403 | `PermissionDeniedError` |
    | 404 | `NotFoundError` |
    | 409 | `ConflictError` |
    | 413 | `ContentTooLargeError` |
    | 422 | `UnprocessableEntityError` |
    | 429 | `RateLimitError` |
    | 504 | `GatewayTimeoutError` |
    | 529 | `OverloadedError` |
    | Every 5xx, such as 500, 504, and 529 | `InternalServerError` |
    | Every error response | `APIStatusError` |
    | An error event in a stream | `APIStatusError` |
    | A client timeout (the SDK stopped waiting) | `APITimeoutError` |
    | Every connection failure before a response arrives (including a client timeout) | `APIConnectionError` |
    | A connection that drops or stalls in mid-stream | `httpx2.TransportError` (`httpx2` is the SDK’s HTTP library) |
    | Every error in this table except a dropped stream | `APIError` |

    For a status that has no row, such as 402, catch `APIStatusError` and compare its `status_code`.

    To reach the underlying exception or the raw response, see [Handling errors in Python](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-errors).
  </Tab>

  <Tab title="TypeScript">
    These classes are properties of `Anthropic` unless a row says otherwise. A class also catches its subclasses, so put the narrower class first. For example, `RateLimitError` also catches `EnforcedSpendLimitReachedError`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `Anthropic.EnforcedSpendLimitReachedError` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `BadRequestError` |
    | 401 | `AuthenticationError` |
    | 403 | `PermissionDeniedError` |
    | 404 | `NotFoundError` |
    | 409 | `ConflictError` |
    | 413 | `ContentTooLargeError` |
    | 422 | `UnprocessableEntityError` |
    | 429 | `RateLimitError` |
    | 504 | `GatewayTimeoutError` |
    | 529 | `OverloadedError` |
    | Every 5xx, such as 500, 504, and 529 | `InternalServerError` |
    | A client timeout (the SDK stopped waiting) | `APIConnectionTimeoutError` |
    | Every connection failure before a response arrives (including a client timeout) | `APIConnectionError` |
    | A connection that drops in mid-stream | `AnthropicError` from `client.messages.stream()`. With `stream: true`, catch the runtime’s own error, such as `TypeError`. |
    | An error event in a stream | `APIError` |
    | Every error in this table except a dropped stream | `APIError` |

    For a status that has no row, such as 402, catch `APIError` and compare its `status`.

    To read the response headers, see [Handling errors in TypeScript](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript#handling-errors).
  </Tab>

  <Tab title="C#">
    These classes are in the `Anthropic.Exceptions` namespace unless a row names another. A class also catches its subclasses, so put the narrower class first. For example, `AnthropicRateLimitException` also catches `AnthropicEnforcedSpendLimitReachedException`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `Anthropic.Models.AnthropicEnforcedSpendLimitReachedException` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `AnthropicBadRequestException` |
    | 401 | `AnthropicUnauthorizedException` |
    | 403 | `AnthropicForbiddenException` |
    | 404 | `AnthropicNotFoundException` |
    | 409 | `AnthropicConflictException` |
    | 413 | `AnthropicContentTooLargeException` |
    | 422 | `AnthropicUnprocessableEntityException` |
    | 429 | `AnthropicRateLimitException` |
    | 504 | `AnthropicGatewayTimeoutException` |
    | 529 | `AnthropicOverloadedException` |
    | Every 4xx | `Anthropic4xxException` |
    | Every 5xx, such as 500, 504, and 529 | `Anthropic5xxException` |
    | Every error response | `AnthropicApiException` |
    | An error event in a stream | `AnthropicSseException` |
    | Every error response and every error event in a stream | `AnthropicServiceException` |
    | A connection failure before a response arrives | `AnthropicIOException` |
    | A connection that drops in mid-stream | .NET’s own `IOException` in `System.IO` |
    | A client timeout (the SDK stopped waiting) | .NET’s own `TaskCanceledException` in `System.Threading.Tasks` |
    | Every error in this table except a client timeout and a dropped stream | `AnthropicException` |

    For a status that has no row of its own, such as 402, catch `Anthropic4xxException` and compare its `StatusCode`.
  </Tab>

  <Tab title="Go">
    The Go SDK has one error type, `*anthropic.Error`. You compare its fields instead of catching a class. In this table, `apierr` is a `*anthropic.Error` variable that `errors.As()` fills.

    | To handle | Check |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | `apierr.ErrorCode() == anthropic.ErrorCodeEnforcedSpendLimitReached` |
    | One HTTP status | `apierr.StatusCode == http.StatusTooManyRequests` |
    | Every error response | `errors.As(err, &apierr)` |
    | An error event in a stream | `errors.As(stream.Err(), &apierr)` |
    | A connection failure, a client timeout, or a connection that drops in mid-stream | Any other `err` that isn’t `nil` |

    Each error code has its own constant (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)).

    To print the raw request and response of a `*anthropic.Error`, see [Error handling in Go](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go#error-handling).
  </Tab>

  <Tab title="Java">
    These classes are in the `com.anthropic.errors` package unless a row names another. A class also catches its subclasses, so put the narrower class first. For example, `RateLimitException` also catches `EnforcedSpendLimitReachedException`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `com.anthropic.models.EnforcedSpendLimitReachedException` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `BadRequestException` |
    | 401 | `UnauthorizedException` |
    | 403 | `PermissionDeniedException` |
    | 404 | `NotFoundException` |
    | 409 | `ConflictException` |
    | 413 | `ContentTooLargeException` |
    | 422 | `UnprocessableEntityException` |
    | 429 | `RateLimitException` |
    | 504 | `GatewayTimeoutException` |
    | 529 | `OverloadedException` |
    | Every 5xx, such as 500, 504, and 529 | `InternalServerException` |
    | An error event in a stream | `SseException` |
    | Every error response and every error event in a stream | `AnthropicServiceException` |
    | A connection failure, a client timeout, or a connection that drops in mid-stream | `AnthropicIoException` |
    | Every error in this table | `AnthropicException` |

    For a status that has no row, such as 402, catch `AnthropicServiceException` and compare its `statusCode()`.

    The error’s `errorCode()` and `type()` each return an `Optional`.

    To read the response headers, see [Error handling in Java](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java#error-handling).
  </Tab>

  <Tab title="PHP">
    These classes are in the `Anthropic\Core\Exceptions` namespace unless a row names another. A class also catches its subclasses, so put the narrower class first. For example, `RateLimitException` also catches `EnforcedSpendLimitReachedException`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `Anthropic\EnforcedSpendLimitReachedException` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `BadRequestException` |
    | 401 | `AuthenticationException` |
    | 403 | `PermissionDeniedException` |
    | 404 | `NotFoundException` |
    | 409 | `ConflictException` |
    | 413 | `ContentTooLargeException` |
    | 422 | `UnprocessableEntityException` |
    | 429 | `RateLimitException` |
    | 504 | `GatewayTimeoutException` |
    | 529 | `OverloadedException` |
    | Every 5xx, such as 500, 504, and 529 | `InternalServerException` |
    | Every error response | `APIStatusException` |
    | An error event in a stream | `APIStatusException` |
    | A connection failure before a response arrives or a client timeout | `APIConnectionException` |
    | A connection that drops in mid-stream | The HTTP client’s own exception or none (see the paragraph after this table). With Guzzle 7, a connection reset raises PHP’s `\RuntimeException`. |
    | Every error in this table except a dropped stream | `APIException` |

    If the server closes the connection in mid-stream, the stream ends with no error. Check that a `message_stop` event arrived.

    For a status that has no row, such as 402, catch `APIStatusException` and compare its `status`.

    To reach the underlying exception, see [Error handling in PHP](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#error-handling).
  </Tab>

  <Tab title="Ruby">
    These classes are in the `Anthropic::Errors` module unless a row names another. A class also catches its subclasses, so put the narrower class first. For example, `RateLimitError` also catches `EnforcedSpendLimitReachedError`.

    | To handle | Catch |
    | ----- | ----- |
    | One [error code](https://platform.claude.com/docs/en/api/errors#error-codes) | Its own class, such as `Anthropic::EnforcedSpendLimitReachedError` (see [Handle a specific error code](https://platform.claude.com/docs/en/api/handle-errors#handle-a-specific-error-code)) |
    | 400 | `BadRequestError` |
    | 401 | `AuthenticationError` |
    | 403 | `PermissionDeniedError` |
    | 404 | `NotFoundError` |
    | 409 | `ConflictError` |
    | 413 | `ContentTooLargeError` |
    | 422 | `UnprocessableEntityError` |
    | 429 | `RateLimitError` |
    | 504 | `GatewayTimeoutError` |
    | 529 | `OverloadedError` |
    | Every 5xx, such as 500, 504, and 529 | `InternalServerError` |
    | Every error response | `APIStatusError` |
    | An error event in a stream | `APIStatusError` |
    | A client timeout (the SDK stopped waiting) | `APITimeoutError` |
    | Every connection failure (including a client timeout and a connection that drops in mid-stream) | `APIConnectionError` |
    | Every error in this table | `APIError` |

    For a status that has no row, such as 402, catch `APIStatusError` and compare its `status`.

    The error’s `error_code` and `type` are symbols.

    To reach the underlying exception, see [Handling errors in Ruby](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby#handling-errors).
  </Tab>
</Tabs>

The table goes by HTTP status and error code, not by `error.type`:

* A 503 with `overloaded_error` counts as a 5xx, not as a 529.
* An error event in a stream never matches a status row or a code’s class. Its HTTP status is the stream’s 200 or is missing.

To go by `error.type` instead, check the error’s `type` (csharp: `Type`; go: `Type()`; java: `type()`; php: `getType()`) as in [Handle an error in a stream](https://platform.claude.com/docs/en/api/handle-errors#handle-an-error-in-a-stream).

## Request ID

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. The same identifier appears as the `request_id` field in [error response bodies](https://platform.claude.com/docs/en/api/errors#error-shapes). When contacting support about a specific request, include this ID to help quickly resolve your issue.

On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.

When the API returns an error response, read the ID from the SDK error in `request_id` (typescript: `requestID`; csharp, go: `RequestID`; java: `requestId()`; php: `getRequestID()`). For a sample, see [Catch errors by kind](https://platform.claude.com/docs/en/api/handle-errors#catch-errors-by-kind). When a request succeeds, read the ID from the response.

The Python and TypeScript SDKs expose the request ID as a `_request_id` property on top-level response objects. The C#, Go, Java, and PHP SDKs expose it through their raw-response accessors, and the Ruby SDK through [middleware](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware). In every SDK except Ruby, use `with_raw_response` (typescript: `.withResponse()`; java: `.withRawResponse()`; csharp: `WithRawResponse`; go: `option.WithResponseInto()`; php: `->raw`) to read any other [response header](https://platform.claude.com/docs/en/api/overview#response-headers), such as `anthropic-organization-id` and [`anthropic-workspace-id`](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response). In Ruby, use the same middleware. On Claude Platform on AWS, use the raw-response accessor to read the AWS request ID (`x-amzn-requestid`) as well:

<CodeGroup>
  ```bash cURL
  # -i prints the response headers, including request-id, before the body
  curl -sS -i https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
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
      Messages = [new UserMessageParam { Content = "Hello, Claude" }]
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
      model="claude-opus-5-5",
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
      model: "claude-opus-5-5",
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

* Some networks might drop idle connections after a variable period of time, which can cause the request to fail or time out without receiving a response from Anthropic.
* Networks differ in reliability. The [Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create) can help you manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

The [Anthropic SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) validates that your non-streaming Messages API requests are not expected to exceed a 10-minute timeout. It also sets a socket option for TCP keep-alive.

If you don’t need to process events incrementally, the SDK can consume the stream for you and return the complete `Message` object, identical to what a non-streaming call returns:

<CodeGroup exclude="shell:cURL">
  <CodeGroupItem language="cURL">
    A curl request prints the raw stream events and can’t combine them into the final message. To get the complete `Message` object from a stream, use the [Anthropic SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
  </CodeGroupItem>

  ```bash CLI
  # The CLI streams events; --format jsonl emits one event on each line
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
      Messages = [new UserMessageParam { Content = "Write a detailed analysis..." }]
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
    model: Anthropic::Model::CLAUDE_SONNET_5,
    max_tokens: 128000,
    messages: [{ role: "user", content: "Write a detailed analysis..." }]
  ).accumulated_message

  puts message.content.find { it.type == :text }.text
  ```
</CodeGroup>

See [Get the final message without handling events](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for more details.

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

Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) on models that support it, system prompt instructions, or [`output_config.format`](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#usage) instead.

### Thinking blocks cannot be modified

If thinking blocks in the request don’t match what the API returned, the request can get a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

```text wrap
`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.
```

With tool use, pass back every `thinking` and `redacted_thinking` block from the assistant turn exactly as received, including blocks whose `thinking` field is empty. If your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. This is a different failure from the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check), whose error says that a block is bound to a different conversation. Setting `prefix_mismatch_behavior` might not clear it. See the [fix for modified thinking blocks](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-blocks-modified) in Troubleshooting thinking.

### Extended thinking not supported

Claude 4.7 and later models don’t support extended thinking. Sending `thinking: {"type": "enabled"}` to any of these models returns a 400 `invalid_request_error`:

```text wrap
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) instead. For the parameter mapping, see [Migrating to adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#migrating-to-adaptive-thinking). To fix the error from its symptom, see [A 400 error says `"thinking.type.enabled"` is not supported](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-enabled).

### Adaptive thinking not supported

Models that support only extended thinking (Claude 4.5 and earlier models) reject `thinking: {"type": "adaptive"}` with a 400 `invalid_request_error`:

```text wrap
adaptive thinking is not supported on this model
```

Use `thinking: {"type": "enabled", "budget_tokens": N}` on these models; see [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for the configuration and the [symptom-first fix for the adaptive thinking error](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-adaptive) in Troubleshooting thinking.

### Thinking cannot be disabled

On Claude Fable 5.2, [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview), Claude Fable 5.1, [Claude Mythos 5.1](https://platform.claude.com/docs/en/models/mythos-5-1/overview), Claude Fable 5, [Claude Mythos 5](https://platform.claude.com/docs/en/models/mythos-5/overview), Claude Opus 5.5, and [Claude Mythos Preview](https://anthropic.com/glasswing), thinking is always on. Sending `thinking: {"type": "disabled"}` to any of these models returns a 400 `invalid_request_error`. On all of these models except Claude Mythos Preview, the message reads:

```text wrap
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

On Claude Mythos Preview, the only one of these models that accepts extended thinking, the message reads:

```text wrap
"thinking.type.disabled" is not supported for this model. Thinking defaults to adaptive mode when not specified; use "thinking.type.enabled" with "budget_tokens" for extended thinking.
```

On Claude Sonnet 5.5, thinking can’t be set to `disabled`. Use `thinking: {"type": "between_tools"}` for the lowest thinking setting, which turns off up-front thinking. Sending `thinking: {"type": "disabled"}` returns a 400 `invalid_request_error` with this message:

```text wrap
To turn thinking off on this model, send "thinking": {"type": "between_tools"} instead of {"type": "disabled"}. The model does not think before responding. The short updates it writes between tool calls come back as thinking blocks.
```

At `xhigh` or `max` [effort](https://platform.claude.com/docs/en/build-with-claude/effort), a request with `between_tools` also returns a 400 `invalid_request_error`. The error message says thinking is disabled because `between_tools` has no up-front thinking:

```text wrap
output_config.effort 'xhigh' is not supported when thinking is disabled on this model. Use effort 'high' or below, or enable thinking.
```

With `between_tools`, effort can’t change mid-conversation: a per-message `output_config.effort` that differs from the level in effect returns a 400 error. The error names the position of the message that set the new level:

```text wrap
messages.N: output_config.effort 'low' differs from the 'high' in effect before it; effort cannot change when thinking is disabled on this model. Use effort 'high', or enable thinking.
```

Claude Haiku 5.5 accepts `thinking: {"type": "disabled"}` and holds it to the same two effort limits that apply to `between_tools`: at `xhigh` or `max` effort, or with a per-message `output_config.effort` that differs from the level in effect, the request returns a 400 `invalid_request_error` with the matching message shown earlier.

In both messages, “enable thinking” means adaptive thinking: omit the `thinking` field or send `thinking: {"type": "adaptive"}`. Claude Sonnet 5.5 and Claude Haiku 5.5 also reject `"enabled"` with a 400 error. To vary effort for each turn, use adaptive thinking.

Sending `thinking: {"type": "between_tools"}` to any model other than Claude Sonnet 5.5 returns a 400 `invalid_request_error`:

```text wrap
"thinking.type.between_tools" is not supported for this model.
```

For the fixes, see the [`between_tools` and effort errors](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-between-tools) in Troubleshooting thinking.

Omit the `thinking` parameter and the request runs with adaptive thinking. To keep thinking content out of responses without turning thinking off, set `display: "omitted"` on the thinking configuration. See the [fix for the disabled thinking error](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-type-disabled) in Troubleshooting thinking.

### Forced tool use not supported

Claude Fable 5.2, [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview), Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1, and [Claude Mythos 5.1](https://platform.claude.com/docs/en/models/mythos-5-1/overview) don’t support forced tool use. Sending `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` to any of these models, including on the [token counting endpoint](https://platform.claude.com/docs/en/build-with-claude/token-counting), returns a 400 `invalid_request_error`:

```text wrap
tool_choice: type "tool" and "any" are not supported for this model.
```

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are accepted. Use `auto` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) to keep tool inputs schema-valid, or [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) when you need the response itself in a fixed JSON shape. See [Forcing tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).

### Computer use tool version not supported

Claude Fable 5.2, Claude Mythos 5.2, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5 return a 400 error for any [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) tool version they don’t accept. On the Claude API, that includes `computer_20251124` with its beta header. They don’t accept `computer_20250124` on any platform. The Claude API’s `invalid_request_error` message names the rejected type and, after `Did you mean one of`, lists the tool types the model accepts. For Claude Opus 5.5, the message begins:

```text wrap
'claude-opus-5-5' does not support tool types: computer_20251124.
```

The Claude API returns the same message for any Anthropic-defined tool type that the requested model doesn’t support. Claude Fable 5.2, Claude Mythos 5.2, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5 support computer use through the `computer_toolset_20260801` toolset. Declare `{"type": "computer_toolset_20260801"}` without the beta header and update your agent loop as described in [Migrate from `computer_20251124`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124). To move from `computer_20250124`, see [Move computer use to the toolset](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#computer-use-toolset) in the Claude Haiku 5.5 migration guide.

On Amazon Bedrock, Claude Fable 5.2, Claude Mythos 5.2, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5 also accept the `computer_20251124` tool with the `computer-use-2025-11-24` beta header. With Amazon Bedrock’s InvokeModel API, send `computer-use-2025-11-24` in the `anthropic_beta` array of the request body instead of in a header. For that API, see [Claude on Amazon Bedrock (`bedrock-runtime`)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy). For the models to use with each earlier version, see [Earlier tool versions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#earlier-tool-versions).

### Thinking block bound to a different conversation

This 400 `invalid_request_error` means a thinking block you sent back failed the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check). Compare `system`, `tools`, and the messages before the block with what you sent when the model produced it. For which changes matter, see [What counts as a change](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#what-counts-as-an-edit). The error message starts with the position of the first failing block:

```text wrap
messages.{i}.content.{j}: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```

Resending the same history fails the same way. Fixing the code that made the edit doesn’t help this conversation if the edit is still in its history. To continue, do one of the following:

* Send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`, on the retry and on every later request in that conversation. On Claude Sonnet 5.5 and Claude Haiku 5.5, `block_binding` works only with `thinking: {"type": "adaptive"}`.
* Strip the block the error names and every `thinking` and `redacted_thinking` block after it, in that message and in every later message. Retry, and leave the stripped blocks out of later requests.

To stop new conversations from failing, [keep the history append-only](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#what-to-check). See the [fix for an invalid thinking block signature](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-block-signature) in Troubleshooting thinking.

Sending `thinking.block_binding` without the `thinking-binding-controls-2026-08-01` [beta header](https://platform.claude.com/docs/en/api/beta-headers) returns a 400 `invalid_request_error` whose message ends in:

```text wrap
block_binding: Extra inputs are not permitted
```

Add the header, turn thinking on, or remove the field.

### Outbound web identity federation disabled (Claude Platform on AWS)

If every request to [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once for each AWS account. See [Enable outbound web identity federation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#enable-outbound-web-identity-federation) for details.

## Next steps

<CardGroup cols={3}>
  <Card title="Troubleshooting thinking" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting">
    Symptom-first fixes for thinking configuration 400 errors, empty thinking blocks, and `max_tokens` stops.
  </Card>

  <Card title="Rate limits" icon="gauge" href="https://platform.claude.com/docs/en/api/rate-limits">
    To mitigate misuse and manage capacity on the API, limits are in place on how much an organization can use the Claude API.
  </Card>

  <Card title="Handle errors" icon="code" href="https://platform.claude.com/docs/en/api/handle-errors">
    Use the SDK to catch Claude API errors by error code, HTTP status, or connection failure and to handle an error that arrives in a stream.
  </Card>
</CardGroup>
