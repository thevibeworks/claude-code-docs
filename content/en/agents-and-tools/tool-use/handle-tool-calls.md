---
title: Handle tool calls
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
description: Parse tool_use blocks, format tool_result responses, and handle errors with is_error.
---

When Claude’s response contains `tool_use` blocks, your code runs each tool and sends back `tool_result` blocks, including any errors. Write this code yourself when you need custom control over tool execution. Otherwise, use the SDK’s [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner), which runs the tools and sends the results for you.

Claude’s response differs based on whether it uses a [client or server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#how-tool-use-works).

## Handling results from client tools

The response has a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:

* `id`: A unique identifier for this particular tool use block. This is used to match up the tool results later.
* `name`: The name of the tool being used.
* `input`: An object containing the input being passed to the tool, conforming to the tool’s `input_schema`.

A `tool_use` block for a member of the [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) or [browser use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool) toolset also carries a `toolset_name` field (`"computer"` or `"browser"`). Its `name` is the member tool Claude is calling, such as `screenshot` or `navigate`, so dispatch those blocks on both fields.

<Accordion title="Example API response with a `tool_use` content block">
  ```json JSON
  {
    "id": "msg_01Aq9w938a90dw8q",
    "model": "claude-opus-5-5",
    "stop_reason": "tool_use",
    "role": "assistant",
    "content": [
      {
        "type": "text",
        "text": "I'll check the current weather in San Francisco for you."
      },
      {
        "type": "tool_use",
        "id": "toolu_01A09q90qw90lq917835lq9",
        "name": "get_weather",
        "input": { "location": "San Francisco, CA", "unit": "celsius" }
      }
    ]
  }
  ```
</Accordion>

When you receive a tool use response for a client tool, follow these steps:

1. For each `tool_use` block, run the tool that the block names, passing in its `input`.
2. In a new request, keep the earlier messages and add the response’s `content` unchanged as an `assistant` message.
3. Add a `user` message with one `tool_result` block for each `tool_use` block in that content, even if the tool failed.
4. Send the request with the same `tools` as the first request. Claude uses the tool results to continue its response.
5. If the next response’s `stop_reason` is also `tool_use`, repeat these steps. For other values, see the [stop reason quick reference](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#quick-reference).

For these steps as complete programs, see [Tutorial: Build a tool-using agent](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent).

Each `tool_result` block has `type` set to `tool_result`, plus these fields:

* `tool_use_id`: The `id` of the `tool_use` block that this result answers.
* `content` (optional): The result of the tool as a string or a list of content blocks. These content blocks can use the `text`, `image`, `document`, or [`search_result`](https://platform.claude.com/docs/en/build-with-claude/search-results) types.
* `is_error` (optional): Set to `true` if the tool failed or the call was invalid.

For example, a successful tool result looks like this:

```json JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
    }
  ]
}
```

A `tool_result` that answers a computer use or browser use member block must also echo the same `toolset_name` value as the `tool_use` block; a member result that omits it is rejected. Its `content` is also narrower: a member result may contain only `text` and `image` blocks, and a browser use result may add one [`browser_state`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#track-tabs-and-page-state) block (the [tab-management members](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-management-results) return only that block).

<Note>
  **Important formatting requirements:**

  * Tool result blocks must immediately follow their corresponding tool use blocks in the message history. You cannot include any messages between the assistant’s tool use message and the user’s tool result message.
  * In the user message containing tool results, the `tool_result` blocks must come FIRST in the content array. Any text must come AFTER all tool results.
  * If the assistant turn also called a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) that has no result block yet, the user message must contain only `tool_result` blocks. Text after the results ends the turn early; for a server tool Claude called directly, the request then fails with a 400 error that names the unresolved server tool. See [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#tool-use).

  If you receive an error such as “tool\_use ids were found without tool\_result blocks immediately after”, check that your tool results are formatted correctly.
</Note>

<Warning>
  Tool results often carry content from sources outside your control: webpages, inbound email, user uploads, third-party APIs. Treat that content as untrusted: an attacker who can influence it might embed instructions that try to redirect Claude (indirect prompt injection). Keep untrusted content inside `tool_result` blocks rather than `system` prompts or plain user `text` blocks, and see [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection) for further hardening.
</Warning>

<AccordionGroup>
  <Accordion title="Example of tool result with images">
    ```json JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            { "type": "text", "text": "15 degrees" },
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "/9j/4AAQSkZJRg..."
              }
            }
          ]
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of empty tool result">
    ```json JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9"
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of tool result with documents">
    ```json JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            { "type": "text", "text": "The weather is" },
            {
              "type": "document",
              "source": {
                "type": "text",
                "media_type": "text/plain",
                "data": "15 degrees"
              }
            }
          ]
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Example of text before and after a tool result">
    For example, this causes a 400 error:

    ```json
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "Here are the results:" }, // ❌ Text before tool_result
        { "type": "tool_result", "tool_use_id": "toolu_01" /* ... */ }
      ]
    }
    ```

    This is correct when the assistant turn calls only client tools:

    ```json
    {
      "role": "user",
      "content": [
        { "type": "tool_result", "tool_use_id": "toolu_01" /* ... */ },
        { "type": "text", "text": "What should I do next?" } // ✅ Text after tool_result
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

## Handling results from server tools

Claude runs the tool internally and incorporates the results directly into its response without requiring additional user interaction.

<Note>
  A response can contain both a client `tool_use` block and a `server_tool_use` block that has no result block. That server tool call is not complete yet, and its result block arrives in a later response. Reply with a user message that contains only the `tool_result` blocks for the client tools and keep the same `tools` array; for a server tool Claude called directly, the API runs it on that request and the next response starts with its result block. See [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#tool-use).
</Note>

<Tip>
  **Differences from other APIs**

  Unlike APIs that separate tool use or use special roles like `tool` or `function`, the Claude API integrates tools directly into the `user` and `assistant` message structure.

  Messages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client content and `tool_result`, whereas `assistant` messages contain AI-generated content and `tool_use`.
</Tip>

## Handling errors with is\_error

When a client tool fails or a call is invalid, send a `tool_result` block with `is_error` set to `true`. Claude might then call the tool again with a new `tool_use` block, so limit how many retries your loop allows.

<AccordionGroup>
  <Accordion title="Tool execution error">
    If the tool itself throws an error during execution (for example, a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:

    ```json JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "ConnectionError: the weather service API is not available (HTTP 500)",
          "is_error": true
        }
      ]
    }
    ```

    Claude can then call the tool again or tell the user what happened. For example, Claude might say “I’m sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later.”

    <Tip>
      Write instructive error messages. Instead of generic errors such as `"failed"`, include what went wrong and what Claude should try next (for example, `"Rate limit exceeded. Retry after 60 seconds."`). This gives Claude the context it needs to recover or adapt without guessing.
    </Tip>
  </Accordion>

  <Accordion title="Invalid tool call">
    If Claude’s attempted use of a tool is invalid (for example, missing required parameters), it usually means that there wasn’t enough information for Claude to use the tool correctly. The best approach during development is to try the request again with more-detailed `description` values in your tool definitions.

    However, you can also continue the conversation with a `tool_result` that indicates the error:

    ```json JSON
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Missing required 'location' parameter",
          "is_error": true
        }
      ]
    }
    ```

    Claude can then call the tool again with the missing information filled in.

    <Tip>
      To eliminate invalid tool calls entirely, use [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) with `strict: true` on your tool definitions. This guarantees that tool inputs always match your schema exactly, preventing missing parameters and type mismatches.
    </Tip>
  </Accordion>

  <Accordion title="Server tool errors">
    Unlike with client tools, you don’t send `is_error` results for server tools. When a server tool hits an error, such as a network issue during web search, the API returns the error inside the tool’s result block. In most cases, Claude then continues with another approach or an explanation for the user.

    For web search error codes, see [Web search tool errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#errors).
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Parallel tool use" icon="grid" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use">
    Handle responses where Claude calls several tools in a single turn.
  </Card>

  <Card title="Tool runner (SDK)" icon="wrench" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner">
    Let the SDK manage the `tool_use` loop, result formatting, and retries for you.
  </Card>

  <Card title="Define tools" icon="hammer" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools">
    Write schemas and descriptions that steer Claude toward the right tool.
  </Card>
</CardGroup>
