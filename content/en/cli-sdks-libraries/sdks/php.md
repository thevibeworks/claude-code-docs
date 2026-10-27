---
title: PHP SDK
url: https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php
description: Install and configure the Anthropic PHP SDK with value objects and builder patterns
---

The Anthropic PHP library provides convenient access to the Claude API from any PHP 8.1.0+ application.

<Info>
  For API feature documentation with code examples, see the [API reference](https://platform.claude.com/docs/en/api/overview). This page covers PHP-specific SDK features and configuration.
</Info>

## Installation

The SDK uses [PSR-18](https://www.php-fig.org/psr/psr-18/) for HTTP and discovers any installed PSR-18 client automatically. [Guzzle](https://docs.guzzlephp.org/) is recommended because the SDK configures it for streaming with no additional setup:

```bash
composer require "anthropic-ai/sdk" "guzzlehttp/guzzle:^7"
```

## Requirements

PHP 8.1.0 or higher.

## Usage

This library uses named parameters to specify optional arguments. Parameters with a default value must be set by name.

```php
$client = new Client();

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: 'claude-opus-5-5',
);

$textBlock = array_find($message->content, static fn ($block): bool => $block->type === 'text');
echo $textBlock->text;
```

For authentication options including Workload Identity Federation, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication). If your API key is a [personal or service account key](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) that isn’t scoped to a workspace, set the workspace ID in the `anthropic-workspace-id` request header; [Select a workspace](https://platform.claude.com/docs/en/manage-claude/authentication#select-a-workspace) shows the per-request option for this SDK.

## Value objects

The recommended way to initialize value objects is the static `with` constructor `Base64ImageSource::with(data: 'U3RhaW5sZXNzIHJvY2tz', ...)` with named parameters.

However, builders are also provided, for example `(new Base64ImageSource())->withData('U3RhaW5sZXNzIHJvY2tz')`.

## Streaming

The SDK provides support for streaming responses using Server-Sent Events (SSE).

```php
$client = new Client();

$stream = $client->messages->createStream(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: Model::CLAUDE_OPUS_5_5,
);

foreach ($stream as $event) {
    echo $event->type . PHP_EOL;
}
```

Streaming requires an HTTP client that returns the response body incrementally. When Guzzle is the discovered PSR-18 client, the SDK configures it for streaming automatically. With a buffering client, the `foreach` loop yields every event at once when the response completes instead of incrementally; if you observe that symptom, install Guzzle or supply a streaming-capable PSR-18 client through the `streamingTransporter` request option:

```php
$client = new Client(
    requestOptions: RequestOptions::with(streamingTransporter: $myStreamingClient),
);
```

## Error handling

When the library is unable to connect to the API, or if the API returns a non-success status code (that is, a 4xx or 5xx response), a subclass of `Anthropic\Core\Exceptions\APIException` is thrown:

```php
<?php
// ...
use Anthropic\Core\Exceptions\APIConnectionException;
use Anthropic\Core\Exceptions\APIStatusException;
use Anthropic\Core\Exceptions\RateLimitException;
use Anthropic\Messages\Model;
// ...
try {
    $message = $client->messages->create(
        maxTokens: 1024,
        messages: [['role' => 'user', 'content' => 'Hello, Claude']],
        model: Model::CLAUDE_OPUS_5_5,
    );
} catch (APIConnectionException $e) {
    echo 'The server could not be reached', PHP_EOL;
    echo $e->getPrevious()?->getMessage(), PHP_EOL;
} catch (RateLimitException $_) {
    echo 'A 429 status code was received; we should back off a bit.', PHP_EOL;
} catch (APIStatusException $e) {
    echo 'Another non-200-range status code was received', PHP_EOL;
    echo $e->getMessage();
}
```

Error codes are as follows:

| Cause            | Error type                     |
| ---------------- | ------------------------------ |
| HTTP 400         | `BadRequestException`          |
| HTTP 401         | `AuthenticationException`      |
| HTTP 403         | `PermissionDeniedException`    |
| HTTP 404         | `NotFoundException`            |
| HTTP 409         | `ConflictException`            |
| HTTP 422         | `UnprocessableEntityException` |
| HTTP 429         | `RateLimitException`           |
| HTTP >= 500      | `InternalServerException`      |
| Other HTTP error | `APIStatusException`           |
| Timeout          | `APITimeoutException`          |
| Network error    | `APIConnectionException`       |

## Retries

Certain errors are automatically retried two times by default, with a short exponential backoff.

Connection errors (for example, because of a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, >=500 Internal errors, and timeouts are all retried by default.

You can use the `maxRetries` option to configure or disable this:

```php
use Anthropic\Messages\Model;
use Anthropic\RequestOptions;
// ...
// Configure the default for all requests:
$client = new Client(requestOptions: RequestOptions::with(maxRetries: 0));

// Or, configure per-request:
$result = $client->messages->create(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: Model::CLAUDE_OPUS_5_5,
    requestOptions: RequestOptions::with(maxRetries: 5),
);
```

## Pagination

List methods in the Claude API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```php
$client = new Client();

$page = $client->beta->messages->batches->list(limit: 20);

// fetch items from the current page
foreach ($page->getItems() as $item) {
    echo $item->id, PHP_EOL;
}
// make additional network requests to fetch items from all pages, including and after the current page
// ...
foreach ($page->pagingEachItem() as $item) {
    echo $item->id, PHP_EOL;
// ...
}
```

## Advanced usage

### OpenTelemetry tracing

When your application registers an OpenTelemetry tracer provider, the SDK emits a span for each request that it sends. To send the spans to your observability platform, see [Set up OpenTelemetry with the Claude SDK](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk).

### Undocumented properties

You can send undocumented parameters to any endpoint, and read undocumented response properties, as follows:

<Note>
  The `extra*` parameters of the same name override the documented parameters.
</Note>

```php
<?php
// ...
use Anthropic\RequestOptions;
// ...
$message = $client->messages->create(
    maxTokens: 1024,
    messages: [['role' => 'user', 'content' => 'Hello, Claude']],
    model: 'claude-opus-5-5',
    requestOptions: RequestOptions::with(
        extraQueryParams: ['my_query_parameter' => 'value'],
        extraBodyParams: ['my_body_parameter' => 'value'],
        extraHeaders: ['my-header' => 'value'],
    ),
);
```

### Undocumented request parameters

If you want to explicitly send an extra parameter, you can do so with the `extraQueryParams`, `extraBodyParams`, and `extraHeaders` options under `RequestOptions::with()` when making a request, as seen in the preceding example.

### Undocumented endpoints

To make requests to undocumented endpoints while retaining the benefit of authentication, retries, and other client features, you can make requests using `client->request`, as follows:

```php
$client = new Client();

$response = $client->request(
    method: 'post',
    path: '/undocumented/endpoint',
    query: ['dog' => 'woof'],
    headers: ['useful-header' => 'interesting-value'],
    body: ['hello' => 'world']
);
```

### Middleware

Middleware runs your code around every HTTP request the client sends. [SDK middleware](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware) shows how to register a middleware and the order in which several run. This section covers the details that are specific to the PHP SDK.

A middleware is a callable that takes the request and `$next`, or an instance of a class that implements `Anthropic\Middleware`, whose `handle()` method has the same signature. The `middleware` request option accepts both:

```php
use Anthropic\Middleware;
use Psr\Http\Message\RequestInterface;
use Psr\Http\Message\ResponseInterface;

final class TracingMiddleware implements Middleware
{
    public function handle(RequestInterface $request, \Closure $next): ResponseInterface
    {
        return $next($request->withHeader('x-trace-id', bin2hex(random_bytes(8))));
    }
}

$client = new Client(requestOptions: ['middleware' => [new TracingMiddleware()]]);
```

`$next` runs the rest of the chain and sends the request. Call it once to forward the request, skip the call to return your own response (such as a cached one), or call it several times to send follow-up requests (such as a custom retry).

The SDK also passes every middleware a third argument: the request’s `Anthropic\RequestOptions`, which merges the client’s options with the options of the call. To read an option such as `fallbackState`, declare an optional third parameter, `?RequestOptions $options = null`. Treat the object as read-only, because every middleware and every retry of the request shares it. If your callable already has a third parameter with another purpose, rewrite it, because the SDK fills that parameter on every call.

At runtime:

* **Retries:** Middleware runs once for each HTTP attempt, inside the SDK’s retry loop, so it runs again on each retry.
* **Error responses:** `$next` returns a response for every HTTP status. The SDK throws its [typed exceptions](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#error-handling) only after the whole chain returns, so a middleware can inspect or replace a 4xx or 5xx response.
* **Exceptions:** An exception that a middleware throws reaches your code unchanged, except in two cases. The SDK handles a PSR-18 `ClientExceptionInterface` as a connection error, which surfaces as `APIConnectionException`. It retries the attempt after an `Anthropic\Core\Exceptions\RetryableException`, and throws that exception unchanged when no retries are left.
* **Authentication:** The SDK refreshes OAuth tokens, and signs or authorizes Amazon Bedrock and Google Cloud requests, inside the innermost `$next`. A request that your middleware changes is therefore signed after the change, and again each time you call `$next`.
* **Response bodies:** A middleware that reads the response body must rewind it, or return `$response->withBody(...)` with a new body, so that the SDK can still decode it. A streaming body can’t be rewound, so pass it through unread.

## Platform integrations

<Note>
  For detailed platform setup guides with code examples, see:

  * [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
  * [Amazon Bedrock (Opus 4.6 and earlier)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)
  * [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)
  * [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed)
  * [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)

  See also [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed).
</Note>

The PHP SDK supports the following platforms:

* **Claude Models on Google Cloud (Google managed):** `Anthropic\Vertex\Client`. Use `::fromEnvironment()`.
* **Bedrock:** `Anthropic\Bedrock\MantleClient`. Use `new MantleClient(awsRegion: ...)`.
* **Bedrock (legacy):** `Anthropic\Bedrock\Client`. Use `::fromEnvironment()` or `::withCredentials()`.
* **Claude Platform on AWS:** `Anthropic\Aws\Client` (requires `aws/aws-sdk-php` as a soft dependency). Use `new Anthropic\Aws\Client(workspaceId: ...)` or set `ANTHROPIC_AWS_WORKSPACE_ID`. Available in beta.
* **Foundry:** `Anthropic\Foundry\Client`. Use `::withCredentials()`.

Use `MantleClient` for new projects; `Anthropic\Bedrock\Client` remains for existing applications using the Bedrock `InvokeModel` API.

The PHP SDK also supports Claude Models on Google Cloud (Anthropic managed) through `Anthropic\GoogleCloud\Client`. This client is in beta. `Anthropic\GoogleCloud\Client` requires `google/auth` as a soft dependency. Use `new Anthropic\GoogleCloud\Client(workspaceId: ...)` or set the `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` environment variable. See [Project, location, and workspace resolution](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#project-location-and-workspace-resolution).

## Semantic versioning

Each major version of this SDK sends one API version by default, and a new major version comes with each new API version. The first major version that sends `2026-10-21` is 1.0.0; see [Switch to 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21#upgrade).

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions.

This package considers improvements to the (non-runtime) PHPDoc type definitions to be non-breaking changes.

## Additional resources

* [GitHub repository](https://github.com/anthropics/anthropic-sdk-php)
* [Packagist](https://packagist.org/packages/anthropic-ai/sdk)
* [API reference](https://platform.claude.com/docs/en/api/overview)
* [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming)
