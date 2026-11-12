---
title: Prompting Claude Fable 5.2
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
description: "Prompting patterns specific to Claude Fable 5.2 and Claude Mythos 5.2: effort, early stopping, approvals, code ownership, progress updates, subagents, caution that builds up, prompts and harnesses designed for earlier models, final reports, and refusals."
---

This guide covers the prompting patterns specific to Claude Fable 5.2. For the model’s capabilities and API changes, see [What’s new in Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) and the [Claude Fable 5.2 and Claude Mythos 5.2 migration guide](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide). For techniques that apply across all current Claude models, see [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Claude Fable 5.2 behaves differently from earlier models in several ways. Start with the section that matches what you observe:

* Unsure which effort level to run, or easy requests start slowly: [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#calibrate-effort)
* A turn ends before the work is done: [Finish the whole task](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#finish-the-whole-task)
* A coding agent copies existing code, or reports problems and leaves them: [Say who owns the code](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code)
* Long agentic turns look silent: [Keep users informed during long turns](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-users-informed-during-long-turns)
* Agent sessions start more subagents than the task needs: [Set expectations for subagents](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents)
* Agents ask for approvals they don’t need, or hold routine work: [Keep caution from piling up](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-caution-from-piling-up)
* Your system prompt, skills, or harness was written for Claude Fable 5.1 or Claude Opus 5.5: [Review prompts and harnesses designed for earlier models](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#review-instructions-written-for-earlier-models)
* Your users read final reports or handoffs after long tasks: [Make reports easy to follow](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#make-reports-easy-to-follow)
* Requests return `stop_reason: "refusal"`: [Safeguard refusals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#safeguard-refusals)

<Note>
  For the order in which to apply this guidance when you migrate, see [Where to start](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#where-to-start).

  Several sections on this page suggest text to add to your system prompt or changes to a tool description. Some also suggest lines to remove from the system prompt or from the notes and rules your agents carry. Make these changes in new conversations only. On Claude Fable 5.2, a request that fails the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check) gets a [400 error](https://platform.claude.com/docs/en/api/errors#thinking-block-conversation-mismatch). If you resume a stored conversation after you change `system`, `tools`, or an earlier message, the request can fail the prefix check. To change instructions partway through a conversation, [put them in the newest turn](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#changing-context). Where [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) are available, you can instead [append a system message to the conversation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#new-instructions).
</Note>

## Calibrate effort

With Claude Fable 5.2, the [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level sets how much the model thinks, how many tool calls it makes, how long a turn takes, and how many tokens it uses. Tune the effort level alongside your prompt.

Start at `high`, the default for Claude Fable 5.2 on the Claude API. Depending on the use case, you might move effort up or down, testing against your own evals. Effort levels rank the same way across Claude models, but the amount of thinking at each level can differ. So, rerun your effort sweep rather than carrying over a setting you tuned on Claude Fable 5.1 or Claude Opus 5.5.

* `low` suits quick back-and-forth, well-specified tasks, and high-volume workloads (intelligent and fast subagents, for example). On coding evaluations, Claude Fable 5.2 performs better than past models at `low` effort. In Anthropic’s testing, it scored close to what Claude Fable 5.1 did at higher effort.
* `medium` suits interactive coding, chat, and everyday knowledge work.
* `high` suits hard coding, research, agentic work, and long unattended runs. Turns take noticeably longer to finish than at `medium`.
* `xhigh` is for your hardest long-running coding and agentic work where you’ve measured a gain. It raised scores slightly on Anthropic’s internal coding evaluations and used many more tokens.
* `max` is for measuring the model’s ceiling or for the rare task where time and tokens don’t matter. It is most reasonable to use `max` for open-ended problems such as scientific discovery and mathematics. Turns are slow and use many more tokens than at `xhigh`.

You get most of the capability gain when using `high` effort. The step from `medium` to `high` raised scores on most of the coding and knowledge-work evaluations that Anthropic tracks. That step also uses more tokens and more time, so move down to `medium` wherever your evals hold. Above `high`, gains are uneven and task-dependent.

For agentic work at `low` or `medium`, add the text in [Finish the whole task](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#finish-the-whole-task). The model is more likely to stop early at lower effort levels.

At `high` and above, the model thinks before almost every reply, including a reply to a greeting. If you find basic requests taking a while or costing you more, use a lower effort for those turns. In Anthropic’s testing, an instruction to answer directly without deliberating didn’t stop the model from thinking at `medium` and above.

Effort has little effect on the length of assistant turn responses. Use prompting to change the length and tone of replies.

You can also mix levels in one workflow. For example, you might plan and iterate with the model at `medium`, then raise effort for the long, unattended part. To change levels within a conversation and keep the prompt cache, use [Per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort-per-message) (beta, `mid-conversation-output-config-2026-07-01` header). That page lists the platforms where it’s available. A change holds until another one replaces it. Where per-message effort isn’t available, set a new top-level `effort` value on the next request, which can invalidate the cached messages.

## Finish the whole task

On long, multistep tasks, Claude Fable 5.2 sometimes ends a turn before the work is done. It might end the turn by listing what’s left to be done, offering to continue, or stopping at an ordinary obstacle such as a timeout. This happens more often at `low` and `medium` effort.

If you see these stops in your agent, add text like this to your system prompt:

```text wrap
# Finishing work
Please avoid stopping while you still owe work the user asked for. Be persistent and do not stop unless needed.

While status notes are welcome, as is clarifying with the user on open decisions, carry on with work that does not depend on the user's answer without unnecessary stops.

If you notice yourself inviting the user to redirect you or offering to wait, instead proceed on the next part of the task. You may meet ordinary obstacles like errors, timeouts, locked files, empty results or failing tools. Diagnose them first, and when they are not real blockers, work through them with the access you have (wait and retry, fix the request, use another tool or source) rather than stopping unnecessarily.

If someone clearly decided something is a hard blocker, such as a file marked not to be touched, access that was intentionally withheld, or a safety guardrail, leave it alone, say plainly what you found, and look for another safe way to finish the task. Stopping before the task is complete is very rarely merited, as in when the task can't move forward without user input, or where the blocker is deliberate and should not be worked past. This does not override the need for confirmation on risky or destructive actions.
```

This prompt tells Claude that ordinary obstacles, such as errors, timeouts, and failing tools, should be diagnosed and worked through. Deliberate blockers, such as a file marked not to be touched, are to be left alone and reported. Treat this as a starting point and adapt the prompt further for your use case.

In testing, Anthropic replayed recorded sessions from an agentic coding product at `medium`. With a version of this text, about half as many sessions ended with unfinished work that could have been continued. It removed most endings that ask permission or offer to continue, but not endings that list what remains and then stop. Output tokens rose by about 30 percent.

Because the model asks less often with this text, keep your own confirmation step for risky or irreversible actions.

### Approvals

When you ask the model to keep going, say exactly what you want rather than sending a simple “continue.” For example, reply “Yes, run the migration on the staging database” where you might have sent a “go” or a thumbs-up.

If you also write approval rules into your system prompt, be specific about the actions you want double-checked. In Anthropic’s testing on simulated tasks where nobody was there to approve, a rule that listed “sending messages to people outside this conversation” among the steps that need approval led the model to hold back about half of its routine requests to colleagues and other teams.

## Say who owns the code

Claude Fable 5.2 pays close attention to who owns the code it works on. In Anthropic’s testing on small coding tasks, the model tended to add to the existing structure when the prompt said nothing about ownership or presented the code base as someone else’s, even when that duplicated existing code. When the prompt said the code base was the model’s own, it often consolidated duplicated code and sometimes made related fixes without being asked.

If you want the model to improve the structure as it works, say that the code is its own:

```text wrap
You are the owner and long-term maintainer of this codebase, and its design is up to you.
```

The ownership sentence makes the model much more likely to consolidate duplicated code into one shared function. In Anthropic’s testing on small coding tasks, the model consolidated duplicated code in under 10 percent of runs without the sentence and in about 75 percent of runs with it.

With this prompt, output tokens rose by about 70 to 80 percent and the model made changes nobody had asked for, many of them new tests and documentation. In some runs, it also changed how an existing feature behaves. A closing PR summary from Claude Fable 5.2 often left out small changes, so review the reported diff and the summary.

Leave the ownership sentence out where the user owns the code and wants it changed as little as possible. A rule that limits scope doesn’t cancel it. In Anthropic’s testing, the model still consolidated duplicated code in more than half of runs when “No drive-by refactors, renames or cleanups” appeared earlier in the same prompt.

## Keep users informed during long turns

Sometimes Claude Fable 5.2 writes little user-facing text during long runs of tool calls. Additionally, the model might make its first tool call without saying what it’s about to do.

First, check that your client receives the model’s updates. On Claude Fable 5.2, the updates the model writes between tool calls come back as [progress-update `thinking` blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates). These updates say what the model found and what it’s doing next. Their text is empty at the default `thinking.display` of `"omitted"`. So a client that renders only `text` blocks can look silent during a long agentic turn. Set `display: "updates"` (beta, `thinking-display-updates-2026-08-18` header) to receive a short summary of each update, or `"summarized"` to receive the updates along with summarized reasoning. Then render the non-empty `thinking` blocks between tool calls.

Frequent updates matter most in interactive settings. If that is your use case, try the following:

### Modify your harness

An effective way to encourage communication is to count consecutive tool-calling steps that give the user nothing to read: no `text` block and no `thinking` block with text. Count with `display` set to `"updates"` or `"summarized"`, because at `"omitted"` every `thinking` block is empty. This option works where your platform supports [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages). When several pass in a row, you can append this reminder after the latest tool results as a [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) (`clear_at: "next_user_message"`, beta, `mid-conversation-system-clear-at-2026-08-21` header):

```text wrap
The user hasn't heard from you in a while: say in a few words what you're doing, then continue.
```

In Anthropic’s testing on multi-turn coding tasks, the reminder roughly halved the longest silent stretch without a noticeable increase in tokens or time.

Leave each reminder in `messages` on later requests. Removing or rewording one edits an earlier turn, which invalidates the thinking blocks after it. See [Send a reminder for one turn](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#per-turn-reminders).

### Signal intent

To receive an opening line before the first tool call, brief updates, and a closing recap, you can also add this text to your system prompt:

```text wrap
Before you start, say in a line what you're about to do; brief updates while you work help the user follow along. Close with a short recap that stands on its own (what you found, what you did, and what's next), so a reader who only sees the last message has the full picture.
```

With this text, the model wrote a message before its first tool call in every run of the coding tasks. Note that output tokens per task increased by roughly 20 percent as a result.

Use this text where a human is directly in the loop. To increase interactive updates, use this text together with the earlier reminder.

### Update system prompt instructions

If you can’t add the reminder in your harness, or your platform has no mid-conversation system messages, add this sentence to your system prompt instead:

```text wrap
Every few tool calls, give the user a one-line update on where things stand.
```

In Anthropic’s testing, this sentence cut most long silent stretches on workflow automation tasks. Expect runs of several tool calls between updates even when you use the reminder together with the opening and recap text. Claude Fable 5.2 works well on long-running asynchronous tasks, so Anthropic recommends the model for work where nobody needs frequent updates.

## Set expectations for subagents

How much Claude Fable 5.2 delegates depends on your harness and tasks. In Anthropic’s testing on short tasks with a minimal subagent tool, it rarely started a subagent. In an agentic coding product whose prompts invite delegation, it delegated readily.

At higher effort levels such as `xhigh` and `max`, Anthropic saw Claude Fable 5.2 use subagents in an agentic coding product to review its own work, which Claude Fable 5.1 didn’t do on the same tasks.

Early testers had good results with Claude Fable 5.2 as the planner and orchestrator for other models. Delegation can speed up work that runs well in parallel. However, subagents can account for a large part of what a session costs, so check which model your subagents use by default.

Change your subagent tool’s description only if Claude Fable 5.2 starts more subagents than your tasks need. A new description is most useful in a harness that already invites delegation and where subagents make up a large share of your token use. If your subagent tool has a plain description and nothing else in your prompts asks for delegation, you likely don’t need one. If your system prompt, skills, or agent files tell the model to delegate, review those lines first.

In the new tool description, state what a subagent adds to the cost of a session, say when delegation is worth it and when it isn’t, and tell the model how to brief a subagent that it starts.

If the model delegates too much, say more about what a subagent costs in your harness, and test the change. In Anthropic’s testing at `high` effort, a longer description focused on this roughly halved the number of subagents compared to a shorter version.

Adapt your description to your requirements and adjust when it tells the model to delegate.

## Keep caution from piling up

Cautious instructions can build up from past sessions through memory, notes, and instruction files. This can be counterproductive when Claude Fable 5.2 follows the instructions closely and asks for unnecessary approval. In early testing, Anthropic saw this mostly when several agents worked together.

If you see this, remove outdated instructions from your agent’s context:

* **Remove notes you no longer need.** Memory can contain old instructions such as “never retry” that the model keeps following, so delete these instructions once they stop being relevant.
* **Name the steps that need no approval.** Telling the model to act more freely is too vague, so list the routine steps that it can take on its own.
* **Check your validation steps.** A condition such as “stop and review at the first error” can block autonomous work, so remove or narrow the stopping conditions that you don’t need.
* **Be explicit about exceptions.** The model treats an instruction that contains “never” as absolute. For example, write “ask for approval before deleting files” instead of “never delete files” if you want the model to keep responsibility over an action. See [Approvals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#approvals).

Keep your own confirmation step for risky or irreversible actions.

## Review prompts and harnesses designed for earlier models

As you migrate to Claude Fable 5.2, review your prompts and harnesses. In Anthropic’s testing, some instructions and interventions designed for earlier models raised cost, caused side effects, or no longer had an effect. Here are the practices to reconsider:

* **Standing instructions to delegate:** Lines that tell the model to delegate can sit in system prompts, skills, and agent files. Read those files before you migrate and remove the lines you no longer need if the model delegates too much in testing. See [Set expectations for subagents](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents).
* **A token budget shown to the model:** Some harnesses show the model a token budget for the task and how much of it is left. The size of that budget changes how much Claude Fable 5.2 spends. In Anthropic’s testing on coding tasks at `high` and `xhigh` effort, removing a large budget lowered cost, with equivalent performance. Test your tasks without it. This finding is about text in the prompt, not the API’s [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets), a beta feature that the testing didn’t cover.
* **Harness code that edits earlier turns:** Claude Fable 5.2 uses [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking). If your harness changes the system prompt, the tools, or an earlier message between requests, the thinking blocks that follow the changed point in the history become invalid. By default, the Messages API then rejects the request, and the Message Batches API drops those blocks. To shorten the history without this error, use [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing), or [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) that keeps no earlier turns after the summary. To have the Messages API drop the blocks too, set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"` (beta, `thinking-binding-controls-2026-08-01` header). In Anthropic’s testing, when earlier thinking was dropped on every turn, the model thought again and used more output tokens. That is the worst case, and the increase depends on how often your harness edits earlier turns. Apart from compaction and context editing, keep the history append-only. That keeps the cache hit rate high, and no thinking is dropped. Measure output tokens on your own tasks before you rely on `"drop_block"`. See [Set `prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#mismatch-behavior) and [Change tools or instructions without failing the prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions).
* **The “treat that answer as done” lines:** [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#thinking-instructions-in-chat-system-prompts) offers two sentences for chat system prompts. They tell the model to treat an earlier answer as done and to focus its thinking on the new message. In Anthropic’s testing at `high` effort, these instructions reduced Claude Fable 5.2’s thinking on follow-up questions. The model also became far less likely to point out mistakes in its earlier answers. Leave these lines out where you want the model to keep re-examining its earlier answers. Elsewhere, test whether the model still points out its own mistakes before you adopt the lines.
* **Instructions to think less:** Claude Fable 5.1 usually followed a line such as “answer directly without deliberating.” On Claude Fable 5.2, this addition doesn’t stop the model from thinking at `medium` and above. Remove such lines and lower the effort level, as described in [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#calibrate-effort).
* **Style rules for writing:** Claude Fable 5.2 follows them closely, so a hard limit such as “one instruction per sentence, in 20 words or fewer” can make its prose choppy. Remove the rules you no longer need before you add the text in [Make reports easy to follow](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#make-reports-easy-to-follow).
* **Rules, notes, and memories that have built up:** Memory files, notes, and instruction files collect cautions over time, and the model might have written some of them itself. Before you migrate, delete cautions whose reason no longer holds, and rewrite absolute rules with their scope and reason. If a system is already stuck, consider restarting it with its memory and notes trimmed. See [Keep caution from piling up](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-caution-from-piling-up).

## Make reports easy to follow

Early testers rated Claude Fable 5.2’s writing above Claude Fable 5.1’s and similar in clarity to Claude Opus 5.5’s. After long agentic work, however, the people who read Claude Fable 5.2’s final report usually haven’t seen the tool calls or files behind it, so the report needs to make sense on its own.

If you ask Claude Fable 5.2 to write final reports or handoffs, add this text to your system prompt, and adjust it to your readers and your product:

```text wrap
# Communicating clearly
Write for an intelligent but low-context reader. The person reading has not seen your tool calls, your reasoning or the files you opened, and may be switching in from other work. Messages should generally be self-contained: the reader should understand what you mean without having to dig for other context. Put the key points in the first few sentences. Practice progressive disclosure in your sentence order, and do not use undefined references and ideas in line 1 that won't make sense until the reader reaches line 12.

Use plain words, and write in clear, understandable full sentences. Do not use a term or abbreviation that you made up during the work. Say what the thing is in a way any reader would understand. Write mostly in the style of ASD-STE100 Simplified Technical English: short sentences, one idea per sentence, active voice, and consistently using the same word for the same thing. Use a paragraph of flowing prose where ideas connect, and keep bullets for lists of separate items. Leave out unnecessary details unless the reader asks and practice concision, but do ensure that your messages have the key context. Aim to make your user-facing text as human-readable and clear as possible.
```

In Anthropic’s testing on agentic tasks, the text made final reports less dense and reduced the number of semicolons. It also shortened sentences on workflow automation tasks. Depending on your use case, you might want to add instructions about length or ask the model to include specific details.

## Safeguard refusals

Claude Fable 5.2 runs safety classifiers that can decline a request. A declined request returns `stop_reason: "refusal"`, and `stop_details.category` names the [refusal category](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response):

* `cyber`: the request could enable cyber harm, such as malware or exploit development.
* `bio`: the request could enable biological harm, such as dangerous lab methods.
* `frontier_llm`: the request could assist the development of competing AI models.
* `reasoning_extraction`: the request asks the model to reproduce its internal reasoning in the response text.
* `general_harms`: the request falls under another usage-policy area.
* `null`: the refusal doesn’t map to a named category.

Benign cybersecurity and life sciences work can also trigger the `cyber` and `bio` classifiers. If that blocks your organization’s legitimate work, see Anthropic’s [Cyber Verification Program](https://support.claude.com/en/articles/14604842) and [Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program). [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview) offers the same capabilities as Claude Fable 5.2 only to organizations verified through these programs.

If your prompts, skills, or tool descriptions ask the model to write out its reasoning in the response, remove those instructions. To see how the model reasoned, set `display: "summarized"` and read the thinking blocks. See [Keep reasoning in thinking blocks](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#keep-reasoning-in-thinking-blocks).

To retry a declined request on another model, see [Refusals, fallback, and billing](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#refusals-fallback-and-billing).

## Where to start

1. Set `effort` to `high` explicitly, then run your evals at `medium` and `xhigh` as well.
2. Read the system prompts, skills, agent files, memory files, notes, and harness text you carry over, and remove or test what [Review prompts and harnesses designed for earlier models](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#review-instructions-written-for-earlier-models) describes.
3. Run your longest agentic tasks, and note where the model stops early, asks for approvals it doesn’t need, goes quiet, delegates more than the task needs, or adds to existing code where you wanted it restructured.
4. Add the text or follow the advice for each behavior you observed, one at a time, and measure its effect and its token cost on your own tasks.
