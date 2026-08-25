> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pre-submission checklist

> What Anthropic reviewers test, so you can pass on the first try

When you submit a server, it is automatically scanned for policy compliance and, by default, listed in the directory as a [community connector](/docs/connectors/verification). Anthropic may then escalate listings flagged as highly useful to Claude users to verified review, which is higher touch and slower; reviewers run a functional test of each tool. This escalation is assessed automatically, and you do not need to take any action. Every server in the directory must meet the criteria on this page, whichever label it carries. The label is a quality signal shown to users; it does not change how your connector runs once connected. This page surfaces the most common rejection reasons so you can self-correct before submitting. For the full legal text, see the [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).

## Tool design

### Separate read and write tools

A single tool that accepts both safe HTTP methods (GET, HEAD, OPTIONS) and unsafe methods (POST, PUT, PATCH, DELETE) is rejected. Do not ship a catch-all `api_request` tool with a `method` parameter.

Split into a read-only tool and one or more write tools. Ideally, split write operations further by action type (create, update, delete). Documenting safe versus unsafe operations within one tool's description does not satisfy this requirement—the operations must be in separate tools.

### Reference API docs in custom query tools

If a tool accepts freeform endpoint paths, query strings, or request bodies that the caller constructs, its description must include a link to or explicit name of the target API. For example: "Queries the Slack Web API—see [https://api.slack.com/methods](https://api.slack.com/methods)". A description like "Makes a request to the API" with no further context fails.

This applies only to custom query tools. Purpose-built tools that call a fixed endpoint internally do not need an API docs reference.

### Provide tool annotations

Every tool must include a `title` and the applicable hint—`readOnlyHint: true` for read-only tools, `destructiveHint: true` for tools that modify or delete data. These determine auto-permissions in Claude: read-only tools can run without per-call confirmation; destructive tools always prompt.

### Keep tool names short

Tool names must be 64 characters or fewer.

### Write narrow, accurate descriptions

Each tool description should state precisely what the tool does and when to invoke it. The description must match the tool's actual behavior.

## Avoid prompt-injection patterns

Tool descriptions are rejected if they:

* Instruct Claude to call external software or tools the user didn't request
* Interfere with Claude calling other tools
* Direct Claude to pull behavioral instructions from external sources
* Contain hidden, obfuscated, or encoded instructions
* Tell Claude to behave in ways unrelated to the tool's function, attempt to override system instructions, or promote products and services

Describe what the tool does. Do not tell Claude how to behave.

## Functional quality

* Every tool must return a successful response when called with valid parameters. Generic errors ("Internal Server Error", "Bad Request" with no detail) fail review.
* Validate inputs and return actionable error messages rather than silently accepting invalid data.
* Keep responses reasonably sized for the task. Do not return a full database dump when a summary was requested.
* Do not collect conversation data beyond what the tool needs for its function.
* Do not query Claude's memory, chat history, conversation summaries, or user files.

## API ownership

Your server must call your own first-party APIs, or APIs you legitimately proxy. The MCP server domain should match your service.

## Unsupported use cases

Connectors that do the following are not accepted:

* Transfer money, cryptocurrency, or other financial assets
* Generate images, video, or audio via AI models (design tools that produce diagrams, charts, or UI mockups are allowed)

## Submission requirements

* **Test credentials** are required and must be a fully populated account.
* **Allowed link URIs** are recommended if your server calls `ui/open-link`. Declared HTTPS origins and custom URI schemes open without a confirmation prompt; anything else still prompts the user. See [Allowed link URIs](/docs/connectors/building/submission#allowed-link-uris).
* **Public documentation** is required by your publish date—a blog post or help-center article is sufficient. You can share docs privately with Anthropic during review.
* **Plugins** must link a public GitHub repo; closed-source is not accepted.
* **MCPB** open-source and "spec will evolve" clauses in the [Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) are required and not waivable.

## Before you submit

Run `claude plugin validate` on plugins. For MCP servers, exercise every tool through the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) and as a [custom connector in Claude](/docs/connectors/building/testing).
