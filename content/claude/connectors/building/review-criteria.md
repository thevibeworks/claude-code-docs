> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector pre-submission checklist

> Check your MCP connector against what Anthropic reviewers test, including tool design, prompt-injection patterns, and functional quality, before you submit.

This checklist covers what Anthropic checks on an MCP connector submitted to the directory, organized around the most common rejection reasons so you can correct them before you submit. It's for connector authors preparing a [directory submission](/docs/connectors/building/submission). For the full legal text behind these criteria, see the [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).

<Note>
  If you're submitting a plugin, see the [plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) instead.
</Note>

Work through [tool design](#design-tools-that-pass-review), [server behavior](#server-behavior-and-scope), and [what to include with your submission](#gather-what-to-include-with-your-submission), then [test every tool](#test-before-you-submit) before you open the portal. [How Anthropic reviews connectors](#understand-how-anthropic-reviews-connectors) covers the Community and Verified labels.

## Design tools that pass review

Tool design covers how your tools are split, named, annotated, and described. These rules apply to every tool your server exposes.

### Separate read and write tools

A single tool that accepts both safe HTTP methods, such as GET, HEAD, and OPTIONS, and unsafe methods, such as POST, PUT, PATCH, and DELETE, is rejected. Don't ship a catch-all `api_request` tool with a `method` parameter.

Split a catch-all tool into a read-only tool and one or more write tools. Ideally, split write operations further by action type: create, update, and delete. Documenting safe versus unsafe operations within one tool's description doesn't satisfy this requirement. The operations must be in separate tools.

### Reference API docs in custom query tools

If a tool accepts freeform endpoint paths, query strings, or request bodies that the caller constructs, its description must include a link to or the explicit name of the target API. For example, "Queries the Slack Web API, see [https://api.slack.com/methods](https://api.slack.com/methods)" passes. A description like "Makes a request to the API" with no further context fails.

The API docs requirement applies only to custom query tools. Purpose-built tools that call a fixed endpoint internally don't need an API docs reference.

### Provide tool annotations

Every tool must include a `title` and the applicable hint: `readOnlyHint: true` for read-only tools, and `destructiveHint: true` for tools that modify or delete data. These determine auto-permissions in Claude. Read-only tools can run without per-call confirmation, and destructive tools always prompt.

### Keep tool names short

Tool names must be 64 characters or fewer.

### Write narrow, accurate descriptions

Each tool description should state precisely what the tool does and when to invoke it. The description must match the tool's actual behavior.

### Avoid prompt-injection patterns

Describe what the tool does, and don't tell Claude how to behave. Tool descriptions are rejected if they:

* Instruct Claude to call external software or tools the user didn't request
* Interfere with Claude calling other tools
* Direct Claude to pull behavioral instructions from external sources
* Contain hidden, obfuscated, or encoded instructions
* Tell Claude to behave in ways unrelated to the tool's function, attempt to override system instructions, or promote products and services

## Server behavior and scope

Beyond individual tools, reviewers check how the server behaves when called, whose APIs it calls, and whether its use case is one the directory accepts.

### Functional quality

* Every tool must return a successful response when called with valid parameters, and generic errors such as "Internal Server Error" or "Bad Request" with no detail fail review
* Validate inputs and return actionable error messages rather than silently accepting invalid data
* Keep responses reasonably sized for the task, and don't return a full database dump when a summary was requested
* Don't collect conversation data beyond what the tool needs for its function
* Don't query Claude's memory, chat history, conversation summaries, or user files

### API ownership

Your server must call your own first-party APIs, or APIs you legitimately proxy. The MCP server domain should match your service.

### Unsupported use cases

Connectors that do the following aren't accepted:

* Transfer money, cryptocurrency, or other financial assets
* Generate images, video, or audio through AI models

Design tools that produce diagrams, charts, or UI mockups are allowed.

## Gather what to include with your submission

Alongside the server itself, a submission carries credentials, links, and terms acknowledgments that reviewers check:

* **Test credentials**: required, and they must be for a fully populated account
* **Allowed link URIs**: recommended if your server calls `ui/open-link`. Declared HTTPS origins and custom URI schemes open without a confirmation prompt, and anything else still prompts the user. See [Allowed link URIs](/docs/connectors/building/submission#allowed-link-uris)
* **Public documentation**: required by your publish date. A blog post or help-center article is sufficient, and you can share docs privately with Anthropic during review

## Test before you submit

Exercise every tool through the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) and as a [custom connector in Claude](/docs/connectors/building/testing) before you submit. The portal's **Test & launch** step asks you to confirm you've done this.

## Understand how Anthropic reviews connectors

When you submit a server, Anthropic scans it automatically for policy compliance and, by default, lists it in the directory as a [Community connector](/docs/connectors/verification). Anthropic may then escalate listings flagged as highly useful to Claude users to Verified review, which is higher touch and slower, and in which reviewers run a functional test of each tool. That escalation is assessed automatically, and you don't need to take any action. Every server in the directory must meet the criteria on this page, whichever label it carries. The label is a quality signal shown to users and doesn't change how your connector runs once connected.

## Next steps

* [Submit a connector](/docs/connectors/building/submission): what the developer portal asks for at each step
* [Connector verification](/docs/connectors/verification): what the Community and Verified labels mean to the people who install your connector
* [Manage your directory listing](/docs/connectors/building/managing-your-listing): track review status and reviewer feedback after you submit
