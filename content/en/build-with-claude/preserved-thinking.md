---
title: Preserved thinking
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking
description: Modifying a conversation now results in an error or a dropped block; how to check whether your integration does that and how to migrate.
---

On Claude Fable 5.1, changing prior turns in the conversation (the `system` prompt, the `tools`, or any earlier message) affects the API response. By default, it makes the API reject the request with an error, unless you opt to have the affected thinking blocks dropped from what the model sees instead (`prefix_mismatch_behavior: "drop_block"`). The check is enforced by default for new accounts created on or after August 31, 2026, 00:00 UTC. There are more details in *[How it works](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#how-it-works)* and *[Who is affected](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#who-is-affected).*

When you send a block back, the API uses its `signature` to check that the prior conversation is unchanged and that the current model can read the block. The check exists so that reasoning produced under one set of instructions can't be replayed under another, potentially adversarial set of instructions.

The API provides first-class alternatives to modify a conversation as it progresses, covering most use cases for transcript edits: [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) for new instructions, [turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#per-turn-reminders) for per-turn reminders, [mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) for adding and removing tools, and [per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) to adjust depth of thinking per turn. The rest of this page covers how to tell whether your integration is affected and how to migrate common harness patterns to these features. As an added benefit, keeping everything before each thinking block byte-for-byte unchanged also keeps the prefix stable for [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

Whether you need to do anything depends on what manages your conversation history:

* **You use an official Claude product or SDK:** Claude Code, claude.ai, [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), or the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview). These keep the prefix intact for you.

* **You call the Messages API directly**, from your own agent loop or any other setting. You should check your code and ensure that the `messages` array is treated as append-only. These common patterns edit the prefix and invalidate the thinking after the edit:

  * Trimming or dropping older turns
  * Summarizing older turns on the client and keeping recent ones
  * Injecting a reminder into an earlier turn and removing it on the next request
  * Rebuilding the `system` prompt each request (current time, token budget, mode flags)
  * Adding or removing entries in `tools` mid-session

## How it works

For new requests the API checks:

* **The model is the same or newer.** A block is readable by the model that produced it and by later models, not by earlier ones. A conversation that moves to a newer model keeps its reasoning. A conversation that moves to an older model fails the model check for those blocks, and the API drops them for that request. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-for-model) for the exact per-model list.
* **Nothing before the block has changed.** The top-level `system` prompt, the set of tools in `tools`, and every message before the block. With server-side compaction the checked prefix starts at the most recent [compaction block](https://platform.claude.com/docs/en/build-with-claude/compaction).
* **The chain of earlier thinking blocks is unbroken.** Earlier `thinking` and `redacted_thinking` blocks aren't part of the prefix, but each thinking block records the one before it, across turns. You can remove thinking blocks from the front of the history. Removing one from the middle invalidates every thinking block after it.

A block that fails the model check is always dropped. For a prefix mismatch you choose what happens with `thinking.block_binding.prefix_mismatch_behavior`, which requires the `thinking-binding-controls-2026-08-01` [beta header](https://platform.claude.com/docs/en/api/beta-headers):

* `"drop_block"`: the API removes the block and every thinking block after it in the conversation, and the request succeeds. Dropped blocks aren't billed. The response lists them in a top-level `input_transformations` array (on the `message_start` event when streaming).
* `"error"`: the API rejects the request with a 400 `invalid_request_error` that names the first failing block.

The default is `"error"`. The header lets you set the field and adds `input_transformations` to responses.

## Who is affected

Claude Fable 5.1. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-thinking) for the model list.

On Claude Fable 5.1, the API enforces the check for new accounts. A new account is one created on or after August 31, 2026, 00:00 UTC. The same definition applies on the Claude API and on cloud platforms. Later models will enforce the check for all users.

A request that sets `prefix_mismatch_behavior` opts into enforcement regardless of account age, which is how you test from an older account. To check whether your account is enforced by default, send a request that edits history without the beta header: a 400 that names the header means enforced.

<Note>
  If you maintain a tool or framework that people run with their own API key, your users on new accounts hit the check before you do: your own key is likely on an older account. Test with `prefix_mismatch_behavior` set so you see what they'll see.
</Note>

## How to tell whether your integration is impacted

Capture the exact request bodies your integration sends over a few normal turns, including a compaction or a tool change if your product does those. For each pair of consecutive requests, compare `system`, `tools`, and the shared part of `messages`. They should be byte-identical up to the newly appended turns.

Then confirm against the API. With the `thinking-binding-controls-2026-08-01` [beta header](https://platform.claude.com/docs/en/api/beta-headers) and `claude-fable-5-1`, set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"` and run a normal multi-turn session through your integration. This request is the second turn of such a session, sending back the first response's assistant turn exactly as received:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: thinking-binding-controls-2026-08-01" \
  -d '{
    "model": "claude-fable-5-1",
    "max_tokens": 16000,
    "thinking": {
      "type": "adaptive",
      "block_binding": { "prefix_mismatch_behavior": "drop_block" }
    },
    "system": "You are a coding agent.",
    "messages": [
      { "role": "user", "content": "Fix the failing test." },
      {
        "role": "assistant",
        "content": [
          { "type": "thinking", "thinking": "", "signature": "EqQBCkYIBxgCKkD..." },
          { "type": "text", "text": "I need to see the test first. Which file is it in?" }
        ]
      },
      { "role": "user", "content": "tests/test_auth.py" }
    ]
  }'
```

Every response then carries a top-level `input_transformations` array. Log it on each turn:

```json
{
  "input_transformations": [
    {
      "type": "thinking_dropped",
      "path": "messages.1.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```

* **Empty on every turn:** your integration keeps history intact.
* **`reason: "prefix_binding_mismatch"`:** something before the block at `path` changed between this request and the previous one. Diff `system`, `tools`, and `messages` up to that turn to find it.
* **`reason: "model_binding_mismatch"`:** the conversation moved to a model that can't read the earlier model's blocks (a router, a fallback). Not a bug in your integration. Keep sending the blocks and let the API drop what the current model can't read.

This works from any account, because setting the field opts the request into enforcement. To fail loudly in CI instead, set `"error"`. The 400 begins:

```text wrap
messages.1.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```

Without the beta header on the request, the message continues: ``That setting requires the `thinking-binding-controls-2026-08-01` value in the `anthropic-beta` header.`` The message usually ends with a sentence naming what changed, for example that the `system` prompt or the `tools` list differs from when the block was created.

See [Troubleshooting thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-block-signature) for every variant of this error.

## What counts as an edit

Between two consecutive requests:

| Change between requests                                                                                                                           | Later thinking blocks                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Append messages at the end                                                                                                                        | Valid                                                                  |
| Add a tool with `defer_loading: true` that nothing has referenced yet                                                                             | Valid                                                                  |
| Remove `thinking` blocks from the start of the history (every thinking block before some point)                                                   | Valid                                                                  |
| Change any request parameter outside `system`, `tools`, and `messages` (`max_tokens`, `output_config`, `tool_choice`, `metadata`, and so on)      | Valid                                                                  |
| Add, move, or remove `cache_control` markers                                                                                                      | Valid                                                                  |
| A rotating signed URL that returns the same bytes                                                                                                 | Valid                                                                  |
| Server-side compaction or context editing removes or replaces content                                                                             | Valid (the check compares what you sent, not the server's edited copy) |
| A cleared [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#per-turn-reminders) left in place | Valid                                                                  |
| Edit, reorder, or delete any earlier `user`, `assistant`, or `system` message                                                                     | Invalid                                                                |
| Add a text block to an earlier user turn, or remove one you added last time                                                                       | Invalid                                                                |
| Change the top-level `system` string or blocks                                                                                                    | Invalid                                                                |
| Add, remove, rename, or edit a tool in `tools`                                                                                                    | Invalid                                                                |
| Remove a `thinking` block from the middle of the history and keep later ones                                                                      | Invalid for every later thinking block                                 |
| An image or document URL that returns different bytes on the next request                                                                         | Invalid                                                                |
| The same turn-scoped message deleted or reworded on a later request                                                                               | Invalid                                                                |

## Update your integration

Each pattern replaces one kind of history edit with an API feature that has the same effect on the model without changing earlier bytes.

### Append assistant turns exactly as returned

Store the `content` array from each response and send it back unchanged as the assistant turn, every block type in the order received, including `thinking` blocks whose `thinking` field is empty. Don't reserialize through an intermediate type that drops unknown block types or empty fields.

### Add instructions with a mid-conversation system message, not by editing `system`

If your code rebuilds the top-level `system` prompt each request (current time, token budget, mode flag, newly discovered project context), every thinking block in the conversation fails the check. Freeze `system` at session start, and when something changes append a [`role: "system"` message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) at the point in `messages` where it becomes true:

```json
{
  "role": "system",
  "content": "The user switched the workspace to read-only mode. Do not write files until told otherwise."
}
```

The model treats it with system-prompt authority, and everything before it is unchanged. No beta header is needed on Claude Fable 5.1. In a tool loop, place it after the `tool_result` user message, never between an assistant `tool_use` and its `tool_result` (see [Limitations](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)).

### Send per-turn reminders as turn-scoped system messages

The most common history edit is the per-turn nudge: a line appended after each batch of tool results ("request independent reads together", "you haven't updated the user in a while") and removed on the next request so reminders don't pile up. Removing it is the edit.

Instead, send the nudge as a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) with `clear_at: "next_user_message"` after the `tool_result` user message (beta header `mid-conversation-system-clear-at-2026-08-21`). This `messages` array is the request after two tool rounds. `messages[3]` is the previous request's nudge, left in place, and `messages[6]` is this request's copy:

```json
[
  { "role": "user", "content": "Fix the failing test." },
  {
    "role": "assistant",
    "content": [
      { "type": "thinking", "thinking": "", "signature": "..." },
      {
        "type": "tool_use",
        "id": "toolu_01",
        "name": "read_file",
        "input": { "path": "tests/test_auth.py" }
      }
    ]
  },
  {
    "role": "user",
    "content": [{ "type": "tool_result", "tool_use_id": "toolu_01", "content": "..." }]
  },
  {
    "role": "system",
    "clear_at": "next_user_message",
    "content": "Request every independent read in one turn."
  },
  {
    "role": "assistant",
    "content": [
      { "type": "thinking", "thinking": "", "signature": "..." },
      {
        "type": "tool_use",
        "id": "toolu_02",
        "name": "read_file",
        "input": { "path": "src/auth.py" }
      }
    ]
  },
  {
    "role": "user",
    "content": [{ "type": "tool_result", "tool_use_id": "toolu_02", "content": "..." }]
  },
  {
    "role": "system",
    "clear_at": "next_user_message",
    "content": "Request every independent read in one turn."
  }
]
```

A `tool_result`-only user message counts as the "next user message", so `messages[3]` is already cleared: it renders nothing and costs no input tokens, but it's still in the array, so the thinking in `messages[4]` stays valid. `messages[6]` is what the model sees this turn. On later requests keep both where they are and append the next copy after the next `tool_result` message. Turn-scoped messages carry `text` only and take no `cache_control`. Put the cache breakpoint on the preceding user turn. See [Turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages).

Without the beta, append the nudge as a `text` block after the `tool_result` blocks in the same user message, and leave earlier copies in place. The model acts on the newest one.

### Change tools with `tool_addition` and `tool_removal`, not by editing `tools`

If the set of tools changes mid-session (a tool unlocks after authentication, a dangerous tool is withdrawn after a mode switch), don't edit `tools`. Declare the full set at session start and use [mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) to offer or withdraw a tool from that point on (beta header `mid-conversation-tool-changes-2026-07-01`). A tool that isn't available yet gets `defer_loading: true` and a later `tool_addition` block, same shape as this `tool_removal`:

```json
{
  "role": "system",
  "content": [
    { "type": "tool_removal", "tool": { "type": "tool_reference", "name": "delete_branch" } },
    { "type": "text", "text": "Branch deletion is disabled for the rest of this session." }
  ]
}
```

A tool whose schema you learn mid-session (an MCP server discovered at runtime) can be appended to `tools` with `defer_loading: true` and offered with `tool_addition`. An unreferenced deferred tool isn't part of the prefix, so appending it is safe. Appending a regular tool isn't.

### Trim context on the server where you can

Client-side truncation and summarization are the second most common edit: drop or summarize the oldest turns and keep the recent ones verbatim. The recent turns' thinking blocks were produced while the history you removed was still in place, so they fail the check. The server-side equivalents don't count as edits, because the check compares the conversation as you sent it:

* [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) summarizes older turns into a compaction block when the context approaches a threshold you set, and the checked prefix restarts from that block. Its [`instructions` parameter](https://platform.claude.com/docs/en/build-with-claude/compaction#custom-summarization-instructions) takes your own summarization prompt ("preserve every ticker, position size, and stated assumption").
* [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) clears old tool results (`clear_tool_uses_20250919`) or old thinking blocks oldest-first (`clear_thinking_20251015`) by rule.

### Custom compaction on the client

This check doesn't prohibit client-side compaction. The rule is narrower: **don't keep a thinking block behind a prefix you've rewritten.**

**Simple compaction** is the recommended shape and needs no changes. When the conversation grows too long, summarize it into one message and start the next request with that summary plus the new user turn, replaying no earlier turns or thinking blocks: `messages` becomes `[{"role": "user", "content": "<summary of the session so far>\n\n<the next instruction>"}]`. No earlier thinking remains, so nothing fails, and the model thinks afresh on the compacted conversation. Claude models are trained on long-horizon tasks with this scheme, and it performs comparably to more elaborate ones for most workloads. It resets the prompt cache at the compaction point, as any compaction does.

Two other common shapes fail as written and need one change each:

* **Keep-tail compaction** summarizes older turns and keeps the most recent turns verbatim. The kept turns' thinking blocks were produced against the full history, so they fail behind the summary. Fix: strip `thinking` and `redacted_thinking` from every assistant turn you carry across, keeping `text` and `tool_use`, or send `prefix_mismatch_behavior: "drop_block"` and let the API strip them.
* **Background compaction** builds the summary off the critical path and swaps it in while the conversation continues, so every turn produced in the meantime has thinking that predates the swap. Fix: send `"drop_block"` on every request that still carries thinking blocks produced before the swap (or strip those blocks yourself; `input_transformations` on the first response after the swap lists exactly which ones), or compact synchronously.

Snipping individual turns out of the middle of the transcript invalidates everything after them, and no client-side shape avoids that. Use a mid-conversation system message for the instruction change you were making, or server-side [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) for selective removal.

Don't compact in the middle of a tool round: an assistant turn whose `tool_use` is still waiting on a `tool_result` should go back with its thinking intact, so the model finishes the round with its reasoning (see [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#preserving-thinking-blocks)).

### Reference files by ID, not by URL that changes content

For an `image` or `document` block with a `url` source, the fetched bytes are part of the checked prefix and the URL string isn't. A "latest screenshot" endpoint or an edited document invalidates later thinking. A rotating signed URL for the same file doesn't. For content you reference across turns, upload it once with the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) and use the `file_id`, or send base64.

### Decide what happens on a mismatch

Once your integration is append-only, choose a `prefix_mismatch_behavior` for production. It governs only prefix mismatches. A block the current model can't read (after a router switch or [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback)) is always dropped, and reported in `input_transformations` when the beta header is sent.

* **`"error"`** (the default) if a prefix mismatch can only mean a bug in your code. You find out from a 400 in testing rather than from silently dropped blocks. In the Message Batches API, the unset default drops failing blocks instead of failing the batch item; set `"error"` explicitly if you want items to error.
* **`"drop_block"`** if you'd rather drop the affected blocks than fail. Log `input_transformations`.

If you catch the 400 in production, retrying the same request won't clear it. Retry with `prefix_mismatch_behavior: "drop_block"` (and the beta header), which removes exactly the blocks that fail, including any in an assistant turn whose `tool_use` is still waiting on its `tool_result`. The drop applies to that request only, so keep sending `"drop_block"` (and the beta header) for the rest of the session. Without the beta, strip every `thinking` and `redacted_thinking` block from the history, leaving each turn's `text` and `tool_use` blocks in place, and retry once. Then fix the edit that caused it.

## API features used on this page

| Feature                                                                                                                                                                                                              | What it replaces                                                                                                      | Status | Header                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------ | --------------------------------------------- |
| [Controls for blocks that aren't preserved](https://platform.claude.com/docs/en/build-with-claude/thinking#preserved-thinking-controls) (`thinking.block_binding.prefix_mismatch_behavior`, `input_transformations`) | Choose reject or drop on a prefix mismatch, and see what was dropped                                                  | Beta   | `thinking-binding-controls-2026-08-01`        |
| [Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) (`role: "system"` in `messages`)                                                          | Rebuilding the top-level `system` prompt                                                                              | Stable | None                                          |
| [Turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#per-turn-reminders) (`clear_at: "next_user_message"`)                                                         | Injecting a reminder and deleting it next request                                                                     | Beta   | `mid-conversation-system-clear-at-2026-08-21` |
| [Mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) (`tool_addition`, `tool_removal`)                              | Editing the `tools` array                                                                                             | Beta   | `mid-conversation-tool-changes-2026-07-01`    |
| [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) (`instructions` for a custom summary prompt)                                                                                          | Client-side summarization of old turns                                                                                | Beta   | `compact-2026-01-12`                          |
| [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) (`clear_tool_uses_20250919`, `clear_thinking_20251015`)                                                                     | Client-side deletion of old tool results or thinking                                                                  | Beta   | `context-management-2025-06-27`               |
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files) (`file_id` sources)                                                                                                                         | URLs whose content changes between requests                                                                           | Stable | None                                          |
| [Per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) (`output_config.effort` on a `role: "system"` message)                                        | Changing top-level effort between requests (protects the prompt cache, not thinking: effort isn't part of the prefix) | Beta   | `mid-conversation-output-config-2026-07-01`   |

To combine headers in one request:

```text wrap
anthropic-beta: thinking-binding-controls-2026-08-01,mid-conversation-system-clear-at-2026-08-21,mid-conversation-tool-changes-2026-07-01
```

The same beta names apply on Amazon Bedrock and Google Cloud. See [Beta headers](https://platform.claude.com/docs/en/api/beta-headers) for how to send them with each SDK.

## Checklist

* If an official Claude product or SDK (Claude Code, claude.ai, Claude Managed Agents, the Claude Agent SDK) manages your conversation history, stop here.
* Consecutive request bodies are byte-identical in `system`, `tools`, and the shared `messages` prefix.
* A full session under `prefix_mismatch_behavior: "drop_block"` logs no `prefix_binding_mismatch` entries.
* Assistant turns go back byte-for-byte as returned, all block types included.
* Top-level `system` and `tools` are fixed for the session. Changes go in `role: "system"` messages and `tool_addition` / `tool_removal` blocks.
* Per-turn reminders are turn-scoped system messages (or trailing text blocks) that are appended fresh and never removed.
* Context is trimmed by compaction or context editing, or by a client-side compaction that leaves no thinking blocks behind the rewritten prefix and never splits a tool round.
* Cross-turn files are `file_id` or base64, not mutable URLs.
* A production `prefix_mismatch_behavior` is set and its 400s or dropped entries are monitored.

## Next steps

<CardGroup cols={2}>
  <Card title="Troubleshooting thinking" icon="hammer" href="https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting">
    Diagnose and fix the most common thinking failures: configuration 400 errors, empty or missing thinking blocks, max\_tokens stops, and cache misses.
  </Card>

  <Card title="Mid-conversation system messages and tool changes" icon="messages" href="https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages">
    Change system instructions or tool availability partway through a conversation without invalidating the cached prefix that came before them.
  </Card>

  <Card title="Compaction" icon="stack" href="https://platform.claude.com/docs/en/build-with-claude/compaction">
    Server-side context compaction for managing long conversations that approach context window limits.
  </Card>

  <Card title="Prompt caching" icon="database" href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">
    Cache prompt prefixes with `cache_control` to cut costs and latency, using automatic caching or explicit breakpoints with 5-minute or 1-hour TTLs.
  </Card>
</CardGroup>
