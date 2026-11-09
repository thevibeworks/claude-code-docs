---
title: Prompting Claude Fable 5.2
url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
description: "Prompting patterns specific to Claude Fable 5.2 and Claude Mythos 5.2: effort, early stopping, approvals, code ownership, progress updates, subagents, caution that builds up, instructions written for earlier models, final reports, and refusals."
---

This guide covers the prompting patterns specific to Claude Fable 5.2. For the model’s capabilities and API changes, see [What’s new in Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2). For techniques that apply across all current Claude models, see [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

Claude Fable 5.2 behaves differently from earlier models in a few ways. Start with the section that matches what you observe:

* Unsure which effort level to run, or easy requests take too long: [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#calibrate-effort)
* A turn ends before the work is done: [Finish the whole task](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#finish-the-whole-task)
* You approve steps as the agent works, or your system prompt has approval rules: [Approvals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#approvals)
* A coding agent repeats existing code instead of merging it, or reports nearby problems without fixing them: [Say who owns the code](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code)
* Long agentic turns look silent: [Keep users informed during long turns](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-users-informed-during-long-turns)
* Agent sessions start more subagents than the task needs: [Set expectations for subagents](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents)
* Agents ask for approvals they don’t need, or hold back routine work: [Keep caution from piling up](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-caution-from-piling-up)
* You carry over a system prompt, skills, or a harness written for Claude Fable 5.1 or Claude Opus 5.5: [Review instructions written for earlier models](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#review-instructions-written-for-earlier-models)
* Your users read final reports or handoffs after long tasks: [Make reports easy to follow](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#make-reports-easy-to-follow)
* Requests return `stop_reason: "refusal"`: [Safeguard refusals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#safeguard-refusals)

<Note>
  For the API changes when you migrate from an earlier model, see the [Claude Fable 5.2 and Claude Mythos 5.2 migration guide](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide). For the order in which to apply this guidance when you migrate, see [Where to start](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#where-to-start).

  Several sections on this page suggest text to add to your system prompt, lines to remove from it or from the notes and rules your agents carry, or changes to a tool description. Make these changes in new conversations only. On Claude Fable 5.2, the API enforces the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#prefix-check) for every account. A request that sends thinking blocks back after `system`, `tools`, or an earlier message changed can return a 400 error, so a stored conversation resumed with the new text can fail. To change instructions partway through a conversation, [put them in the newest turn](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#changing-context). Where [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) are available, you can instead [append a system message to the conversation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#new-instructions).
</Note>

## Calibrate effort

Start at `high`, the default on the Claude API. If your use case calls for it, move effort up or down, and test each change against your own evals. The [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level sets how much Claude Fable 5.2 thinks, how long a turn takes, and how many tokens it uses. Tune effort alongside your prompt, because the level also changes the way the model thinks and how many tool calls it makes.

In general, effort levels run in the same order across Claude models, but the amount of thinking behind each level can differ from model to model. So rerun your effort sweep instead of carrying over a setting you tuned on Claude Fable 5.1 or Claude Opus 5.5.

Choose a level by the kind of work:

* `low` suits quick back-and-forth, well-specified tasks, and high-volume workloads, such as fast, intelligent subagents. In Anthropic’s testing, the model’s scores at `low` sat close to Claude Fable 5.1’s scores at higher effort levels.
* `medium` suits interactive coding, chat, and everyday knowledge work.
* `high` suits hard coding, research, agentic work, and long unattended runs. Turns take noticeably longer to finish than at `medium`.
* `xhigh` is for your hardest long-running coding and agentic work, where you’ve measured a gain. On Anthropic’s internal coding evaluations, it raised scores slightly and used many more tokens.
* `max` is for measuring the model’s ceiling, or for the rare task where time and tokens don’t matter. It best suits open-ended problems, such as scientific discovery and mathematics. Turns are slow and use many more tokens than at `xhigh`.

Most of the gain in capability is already present at `high`. The step from `medium` to `high` raised scores on most of the coding and knowledge-work evaluations that Anthropic tracks. That step also uses more tokens and more time, so move down to `medium` wherever your evals show that quality holds. Above `high`, gains are uneven and depend on the task.

When you choose a level, note three behaviors:

* The model is more likely to stop early at lower effort levels. For agentic work at `low` or `medium`, add the text in [Finish the whole task](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#finish-the-whole-task).
* At `high` and above, the model thinks before almost every reply, including a reply to a greeting. If easy requests take too long or cost too much, use a lower effort level for those turns. In Anthropic’s testing, an instruction to answer directly without deliberating didn’t stop the model from thinking at `medium` and above.
* Effort barely changes how long the model’s replies are. To change the length and tone of a reply, use your prompt.

You can also mix levels in one workflow. For example, you might plan and iterate with the model at `medium`, then raise effort for the long, unattended part. To change levels within a conversation and keep the prompt cache, use a [per-message effort change](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) (beta, `mid-conversation-output-config-2026-07-01` header); that section lists the platforms where it’s available. A change holds until another one replaces it. Where per-message effort isn’t available, set a new top-level `effort` value on the next request, which starts the cache over.

## Finish the whole task

On long, multistep tasks, Claude Fable 5.2 sometimes ends a turn before the work is done. The turn closes with a list of what remains, an offer to continue, or a stop at an ordinary obstacle such as a timeout. This occurs more often at `low` and `medium` effort.

If you see these stops in your agent, add text like this to your system prompt:

```text wrap
# Finishing work
Please avoid stopping while you still owe work the user asked for. Be persistent and do not stop unless needed.

While status notes are welcome, as is clarifying with the user on open decisions, carry on with work that does not depend on the user's answer without unnecessary stops.

If you notice yourself inviting the user to redirect you or offering to wait, instead proceed on the next part of the task. You may meet ordinary obstacles like errors, timeouts, locked files, empty results or failing tools. Diagnose them first, and when they are not real blockers, work through them with the access you have (wait and retry, fix the request, use another tool or source) rather than stopping unnecessarily.

If someone clearly decided something is a hard blocker, such as a file marked not to be touched, access that was intentionally withheld, or a safety guardrail, leave it alone, say plainly what you found, and look for another safe way to finish the task. Stopping before the task is complete is very rarely merited, as in when the task can't move forward without user input, or where the blocker is deliberate and should not be worked past. This does not override the need for confirmation on risky or destructive actions.
```

This text separates two kinds of obstacle. It tells the model to diagnose and work through ordinary obstacles, such as errors, timeouts, and failing tools. It tells the model to leave deliberate blockers alone, such as a file marked not to be touched, and to report them. Treat the text as a starting point, and keep that distinction when you adapt it to your application.

Anthropic replayed recorded sessions from an agentic coding product at `medium` effort. With a version of this text, about half as many sessions ended with doable work left. The text removed most endings that ask permission or offer to continue, but not endings that list what remains and then stop. Output tokens rose by about 30 percent.

Because the model asks less often with this text, keep your own confirmation step for risky or irreversible actions.

### Approvals

When you tell the model to keep going, say clearly what you want from it instead of sending a bare “continue.” For example, reply “Yes, run the migration on the staging database” where you might have sent “go” or a thumbs-up.

If your system prompt has approval rules, name the exact actions they cover, because the model applies them as written. In Anthropic’s testing on simulated tasks with nobody there to approve, one rule listed “sending messages to people outside this conversation” among the steps that need approval. With that rule, the model held back roughly half of its routine requests to colleagues and other teams.

## Say who owns the code

Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on. In Anthropic’s testing on small coding tasks, when a prompt said nothing about ownership or presented the code base as someone else’s, the model tended to add to the existing structure, even when that repeated existing code. It also tended to report nearby problems instead of fixing them. When the prompt says the code base is the model’s own, the model often merges repeated code and makes related fixes without being asked.

If you want the model to improve the structure as it works, say that the code is its own:

```text wrap
This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.
```

In Anthropic’s testing on small coding tasks, the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it. The rate varied by task. The result held when the sentence stood inside a long system prompt. The requested feature worked in nearly every try either way.

In the same testing, the model also used about 1.5 times the output tokens with the sentence and made several changes that nobody had asked for, many of them new tests and documentation. Apart from bug fixes, it changed how an existing feature behaves in one try in six to ten, and more often at higher effort. Its closing summary named the larger changes but often left out small ones, so review the diff and not only the summary.

Leave the ownership sentence out where the user owns the code and wants it changed as little as possible. A rule elsewhere in the prompt that limits scope doesn’t cancel the ownership sentence. In Anthropic’s testing, with “No drive-by refactors, renames or cleanups” earlier in the same prompt, the model still merged repeated code in about a third of the tries.

## Keep users informed during long turns

Claude Fable 5.2 sometimes writes little user-facing text during long runs of tool calls. The model might also make its first tool call without saying what it’s about to do.

First, check that your client receives the model’s updates. On Claude Fable 5.2, the updates the model writes between tool calls come back as [progress-update `thinking` blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates). These updates say what the model found and what it’s doing next. Their text is empty at the default `thinking.display` of `"omitted"`. So a client that renders only `text` blocks can look silent during a long agentic turn. Set `display: "updates"` (beta, `thinking-display-updates-2026-08-18` header) to receive a short summary of each update, or `"summarized"` to receive the updates along with summarized reasoning. Then render the non-empty `thinking` blocks between tool calls.

Frequent updates matter most when a user watches the work in real time, as in interactive coding. If your users watch the work and still get too few updates, use one or more of these options.

If you can change your harness, an effective option is to have it count consecutive tool-calling steps that give the user nothing to read: no `text` block and no `thinking` block with text. Count with `display` set to `"updates"` or `"summarized"`, because at `"omitted"` every `thinking` block is empty. This option works where your platform supports [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages). After several such steps in a row, have the harness append this reminder after the latest tool results as a [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) (`clear_at: "next_user_message"`, beta, `mid-conversation-system-clear-at-2026-08-21` header):

```text wrap
The user hasn't heard from you in a while: say in a few words what you're doing, then continue.
```

In Anthropic’s testing on multi-turn coding tasks, the reminder roughly halved the longest silent stretch, with no noticeable increase in tokens or time.

Leave each reminder in `messages` on later requests. Removing or rewording one edits an earlier turn, which invalidates the thinking blocks after it. See [Send per-turn reminders as turn-scoped system messages](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#per-turn-reminders).

To also get an opening line before the first tool call, brief updates, and a closing recap, add this text to your system prompt:

```text wrap
Before you start, say in a line what you're about to do; brief updates while you work help the user follow along. Close with a short recap that stands on its own (what you found, what you did, and what's next), so a reader who only sees the last message has the full picture.
```

In Anthropic’s testing on coding tasks, the model spoke before its first tool call every time with this text. The text also raised output tokens per task by roughly 20 percent. Use this text where a human is directly in the loop. To get the most updates, pair it with the reminder that your harness appends.

If you can’t change the harness, or your platform has no mid-conversation system messages, add this sentence to your system prompt:

```text wrap
Every few tool calls, give the user a one-line update on where things stand.
```

In Anthropic’s testing on workflow automation tasks, this sentence cut most long silent stretches.

Even with the reminder and the opening and recap text together, expect runs of several tool calls between updates. Claude Fable 5.2 works well on long-running asynchronous tasks, where the user comes back for the result instead of watching each step. Gaps between updates matter less there.

## Set expectations for subagents

How much work Claude Fable 5.2 delegates to subagents depends on your harness and tasks. In Anthropic’s testing on short tasks with a minimal tool for starting subagents, it rarely started one. In an agentic coding product whose prompts invite delegation, it delegates readily.

If your system prompt, skills, or agent files tell the model to delegate, review those lines first. Change the description of the tool that starts subagents only if Claude Fable 5.2 still starts more subagents than your tasks need. If the tool has a plain description and nothing else in your prompts asks for delegation, you likely don’t need a new description.

In the new description, state what a subagent adds to the cost of a session, say when delegation is worth it and when it isn’t, and tell the model how to brief a subagent that it starts. The description that Anthropic tested does these three things and puts cost first. A description of this kind is most useful when your harness already invites delegation and subagents make up a large share of your token usage.

In Anthropic’s testing on short tasks, the model delegated about a third less often with the tested description than with one that mostly listed reasons to delegate. Task success was the same.

In the tested description, the opening sentences on cost hold delegation back. Say less about cost if the model delegates too little. If it still delegates too much, say more about what a subagent costs in your harness, and test the change.

Anthropic also observed Claude Fable 5.2 using subagents to review its own work in an agentic coding product at higher effort levels, such as `xhigh` and `max`. Claude Fable 5.1 didn’t do this on the same tasks. Early testers had good results with Claude Fable 5.2 as the planner and orchestrator for other models. Delegation can speed up work that runs well in parallel. However, subagents can account for a large part of what a session costs, so check which model your harness runs subagents on by default.

## Keep caution from piling up

Cautious instructions build up wherever context carries over: memory, notes, instruction files, and messages between agents. Claude Fable 5.2 follows these instructions closely, so it might ask for approvals it doesn’t need or hold back routine work. A few early testers saw this behavior, mostly where several agents work together. Earlier models follow such instructions too, but in one of the setups described here only Claude Fable 5.2 held back.

If you see this behavior, clean up what your agents carry:

* **Remove notes you no longer need.** In Anthropic’s testing on simulated tasks, one of a dozen notes from earlier sessions said never to retry. With those notes in context, and with nothing in the prompt that allowed retries, the model retried after a tool was busy in about four in ten tries, down from nearly all without those notes.
* **Name the steps that need no approval.** In Anthropic’s testing on simulated tasks, the context held “never” rules, notes, and a reviewer’s conditions. A line at the end of the rules that listed retries among the steps that need no approval raised retries from almost none to about half of the tries. In the same setup, a general instruction to act more freely changed nothing. Name retries only for calls that are safe to repeat.
* **Check what reviewer agents attach.** In Anthropic’s testing on simulated tasks, one setup had a line in the prompt that listed retries among the steps that need no approval, and a reviewer’s “stop at the first error” in context. Claude Fable 5.2 didn’t retry in about a third of the tries. Claude Fable 5.1 and Claude Opus 5.5 retried.
* **Write the exception into the rule.** In Anthropic’s testing on simulated tasks, the person in charge had approved a step. Under a “never” rule, the model took that step in about one try in ten. A separate line that said an approved step has its go-ahead didn’t change that rate much. When the rule itself said to get a go-ahead first, the model took the step in about nine tries in ten. See [Approvals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#approvals).

Also keep your own confirmation step for risky or irreversible actions.

## Review instructions written for earlier models

When you migrate to Claude Fable 5.2, review your prompts. In Anthropic’s testing, some instructions written for earlier models raised cost, caused side effects, or no longer had an effect. Reconsider these instructions:

* **Standing instructions to delegate:** Lines that push work to subagents can sit in system prompts, skills, and agent files. Read those files before you migrate. If, in your tests, the model starts more subagents than your tasks need, remove the lines you no longer need. See [Set expectations for subagents](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents).
* **A token budget that your harness writes into the prompt:** Some harnesses tell the model in the prompt how many tokens the task may use and how many are left. The size of that budget changes how much Claude Fable 5.2 spends. In Anthropic’s testing on coding tasks at `high` and `xhigh` effort, removing a large budget lowered cost, with equivalent performance. Test your tasks without the budget. This finding is about text in the prompt, not the API’s [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets), a beta feature that the testing didn’t cover.
* **Harness code that edits earlier turns:** Claude Fable 5.2 uses [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking). If your harness changes the system prompt, the tools, or an earlier message between requests, the thinking blocks that follow the changed point in the history become invalid. By default, the Messages API then rejects the request, and the Message Batches API drops those blocks. To shorten the history without this error, use [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing), or [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) that keeps no earlier turns after the summary. To have the Messages API drop the blocks too, set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"` (beta, `thinking-binding-controls-2026-08-01` header). In Anthropic’s testing, when earlier thinking was dropped on every turn, the model thought again and used more output tokens. That is the worst case, and the increase depends on how often your harness edits earlier turns. Apart from compaction and context editing, keep the history append-only. That keeps the cache hit rate high, and no thinking is dropped. Measure output tokens on your own tasks before you rely on `"drop_block"`. See [What the API does with an invalid block](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) and [Make changes without editing the prefix](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#replace-prefix-edits).
* **The “treat that answer as done” lines:** [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#thinking-instructions-in-chat-system-prompts) offers two sentences for chat system prompts. They tell the model to treat an earlier answer as done and to focus its thinking on the new message. In Anthropic’s testing at `high` effort, these sentences reduced Claude Fable 5.2’s thinking on follow-up questions, but the model also became far less likely to point out mistakes in its earlier answers. Leave these lines out where you want the model to keep re-examining its earlier answers. Elsewhere, test whether the model still points out its own mistakes before you adopt the lines.
* **Instructions to think less:** Claude Fable 5.1 usually follows a line such as “answer directly without deliberating.” In Anthropic’s testing, such a line didn’t stop Claude Fable 5.2 from thinking at `medium` and above. Remove these lines and lower the effort level, as described in [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#calibrate-effort).
* **Style rules for writing:** Claude Fable 5.2 follows style rules closely, so a hard limit such as “one instruction per sentence, in 20 words or fewer” can make its prose choppy. Remove the rules you no longer need before you add the text in [Make reports easy to follow](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#make-reports-easy-to-follow).
* **Rules, notes, and memories that have built up:** Memory files, notes, and instruction files collect cautions over time, and the model might have written some of them itself. Before you migrate, delete the cautions whose reason no longer holds, and rewrite absolute rules so that they state their scope and reason. If a system is already stuck, consider restarting it with its memory and notes trimmed, and keep a copy of the originals. See [Keep caution from piling up](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-caution-from-piling-up).

## Make reports easy to follow

After long agentic work, the people who read Claude Fable 5.2’s final report usually haven’t seen the tool calls or files behind it. The report needs to make sense on its own.

If you ask Claude Fable 5.2 to write final reports or handoffs, add this text to your system prompt, and adjust it to your readers and your product:

```text wrap
# Communicating clearly
Write for an intelligent but low-context reader. The person reading has not seen your tool calls, your reasoning or the files you opened, and may be switching in from other work. Messages should generally be self-contained: the reader should understand what you mean without having to dig for other context. Put the key points in the first few sentences. Practice progressive disclosure in your sentence order, and do not use undefined references and ideas in line 1 that won't make sense until the reader reaches line 12.

Use plain words, and write in clear, understandable full sentences. Do not use a term or abbreviation that you made up during the work. Say what the thing is in a way any reader would understand. Write mostly in the style of ASD-STE100 Simplified Technical English: short sentences, one idea per sentence, active voice, and consistently using the same word for the same thing. Use a paragraph of flowing prose where ideas connect, and keep bullets for lists of separate items. Leave out unnecessary details unless the reader asks and practice concision, but do ensure that your messages have the key context. Aim to make your user-facing text as human-readable and clear as possible.
```

In Anthropic’s testing on agentic tasks, this text made final reports less dense, with fewer semicolons. On workflow automation tasks, it also made sentences shorter. You might also add instructions about length or ask the model to include specific details.

## Safeguard refusals

Claude Fable 5.2 runs safety classifiers that can decline a request. A declined request returns `stop_reason: "refusal"`, and `stop_details.category` names the [refusal category](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response):

* `cyber`: the request could enable cyber harm, such as malware or exploit development.
* `bio`: the request could enable biological harm, such as dangerous lab methods.
* `frontier_llm`: the request could help with the development of competing AI models.
* `reasoning_extraction`: the request asks the model to reproduce its internal reasoning in the response text.
* `general_harms`: the request falls under another usage-policy area.

Benign cybersecurity and life sciences work can also trigger the `cyber` and `bio` classifiers. If they block your organization’s legitimate work, see Anthropic’s [Cyber Verification Program](https://support.claude.com/en/articles/14604842) and [Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program). [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview) offers the same capabilities as Claude Fable 5.2 only to organizations verified through these programs.

If your prompts, skills, or tool descriptions ask the model to write its reasoning in the response, remove those instructions. To see how the model reasoned, set `display: "summarized"` and read the thinking blocks. See [Keep reasoning in thinking blocks](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#keep-reasoning-in-thinking-blocks).

To retry a declined request on another model, see [Refusals, fallback, and billing](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#refusals-fallback-and-billing).

## Where to start

When you migrate, work through these steps in order:

1. Set `effort` to `high` explicitly, then run your evals at `medium` and `xhigh` as well.
2. Read the system prompts, skills, agent files, memory files, notes, and harness text you carry over. Remove or test the instructions listed in [Review instructions written for earlier models](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#review-instructions-written-for-earlier-models).
3. Run your longest agentic tasks. Note where the model stops early, asks for approvals it doesn’t need, goes quiet, delegates more than the task needs, or adds to existing code where you wanted it restructured.
4. Apply the guidance for each behavior you observed, one at a time, and measure its effect and its token cost on your own tasks.
