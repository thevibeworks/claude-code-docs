# Change the model, effort, and thinking settings

The model menu next to the send button controls three settings: which Claude model you're chatting with, how much effort it puts into each response, and whether it uses extended thinking. This article explains how to change each one and when to use them.

---

## Change the model

1. Start chatting with Claude or open an existing chat.

2. The selected model and effort level appear next to the send button.

3. To change the model, click on the model name and choose which Claude model you'd like to chat with instead.

4. Click "More models" to view additional options.

If you're on an Enterprise plan and a model or effort level you expect is missing, your administrator may have turned it off for your role.

**Note:** You can change the model, effort level, or thinking setting at any point in a conversation. Changes apply starting with Claude's next response.

---

## Choose an effort level

The effort level controls how much thinking Claude applies to a response. Higher effort means more thorough responses, but they take longer and use more tokens, so you'll reach your usage limits faster.

The effort selector is available for Opus 5, Sonnet 5, Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6.

To change the effort level:

1. Click the model name next to the send button.

2. Click "Effort."

3. Choose a level.

Each model has a recommended effort level, marked as "Default" in the menu:

- **Low** and **Medium** work well for routine tasks and stretch your usage further.

- **High** offers the best overall balance of quality and speed.

- **Extra high** (xhigh) is designed for long-running coding and agentic tasks, offering deeper reasoning than high without the full token cost of max. Available on Opus 4.7 and newer models.

- **Max** is the most thorough option, best for tasks requiring the deepest possible reasoning and most thorough analysis.

Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**.

---

## Use extended thinking

Extended thinking lets Claude spend more time breaking down problems, planning solutions, and exploring different approaches before responding.

Thinking and effort are separate settings, and you can use any combination of the two. The effort level controls how thorough Claude is with every response. The thinking toggle controls whether Claude works through its reasoning in an expandable section before responding.

Extended thinking cannot be turned off in Claude when using Claude Opus 5. On the Claude API, thinking can be turned off at effort levels high and below, but attempting to disable thinking at xhigh or max effort returns an error.

### Turn extended thinking on or off

For models with effort levels:

1. Click the model name next to the send button.

2. Mouse over "Effort."

3. Switch the "Thinking" toggle on or off.

For other models:

1. Click the model name next to the send button.

2. Switch the "Extended" toggle on or off.

### View Claude's thought process

When extended thinking is enabled, you'll see:

- A "Thinking" indicator with a timer showing how long Claude has been processing.

- An expandable "Thinking" section above Claude's response.

Click the "Thinking" section to view Claude's thought process summary and problem-solving approach. Reviewing it can be valuable for verifying how Claude arrived at its conclusion.

### Incomplete thought processes

Occasionally, you may notice that Claude's thinking stops before it's complete, with a message stating that the rest of Claude's thought process is not available.

This happens when Claude's thinking involves information our safety systems have identified as potentially posing an elevated risk of harm or misuse per our **[Usage Policy](https://www.anthropic.com/legal/aup)**.

If the incomplete thought process affects Claude's ability to help with your request, you can try reframing your prompt to help Claude approach the problem from a different angle.

### Choose the right settings for your task

For everyday tasks, the defaults work well. Simple questions, basic information requests, and general writing don't need extra effort or thinking, and lower effort stretches your usage further.

For complex tasks, raise the effort level, turn on thinking, or both. These settings help most with:

- Mathematical calculations and proofs

- Competition-level coding challenges

- Comprehensive project planning

- Detailed document analysis

- Multi-step technical problems

For complex coding and agentic tasks on Opus 4.7 or newer, try Extra high (xhigh) first. For the most difficult, correctness-critical work, choose Max effort and expect longer response times.

Whichever settings you choose, be specific about your problem or question. Clear prompts help Claude use its effort and thinking time effectively.