# Why Claude switched models in your conversation with Opus 5 or Opus 5.5

This article explains why a request might fallback on Claude Opus 5 or Opus 5.5, what happens when your conversation switches to another model, and how to manage automatic switching.

## Why some requests get blocked

Claude Opus 5 and Opus 5.5 improve on Claude Opus 4.8 across the board. We've set its safeguards in line with those capability gains.

Most requests sent to Opus 5 or Opus 5.5 won’t encounter fallback safety interventions. A narrow set of higher-risk requests either fallback to a less capable model or are blocked directly, so we can keep supporting everyday work while limiting the risk of misuse. We continue working to refine these safeguards so they block fewer legitimate requests. That includes fine-tuning our classifiers to reduce false positives and factoring in a range of account trust signals. Your feedback helps guide this work.

## What requests may fallback or get blocked

Claude Opus 5 and Opus 5.5 run automated safety checks, or classifiers, on every user request. The checks also review everything the model reads, not just your latest message. This includes memory, content from connectors, web search results, and files, so a fallback can be triggered by content you didn't type.

Fallbacks and blocks work differently depending on the type of classifier triggered: cybersecurity, biology, frontier LLM development, or distillation.

### Cybersecurity

Opus 5 or Opus 5.5 may fallback to Opus 4.8 when our cyber classifiers flag potentially higher-risk offensive cybersecurity requests, such as:

- Exploit generation

- Binary-based vulnerability scanning

- Penetration testing

You can still use Opus 5 and Opus 5.5 for secure coding, including scanning source code for vulnerabilities, triaging security issues, and building secure code.

### Biology

While Claude Opus 5 improves on Opus 4.8 in biology, it’s not as capable as Fable 5 at real world long-horizon tasks for novel research discoveries that could lead to significant risk. As a result, Opus 5 doesn't fallback on biology, chemistry, or life-sciences questions. It uses similar safeguards for these topics as Opus 4.8.

Opus 5.5 has similar safety classifiers to Claude Fable 5 for biology due to increases in capabilities over Opus 5. These classifiers cause Claude to fall back from Opus 5.5 to Opus 5 when you submit dual-use requests in areas like virology, toxicology, and molecular design. You can still use Opus 5.5 for everyday health and educational questions, including interpreting lab results, understanding symptoms, and learning about biology.

### Frontier LLM development (Opus 5.5 only)

Opus 5.5 has classifiers similar to Fable models for a small set of capabilities related to the development of frontier LLMs, such as kernel development for certain ML accelerators. They shouldn't impact the vast majority of traditional AI or ML development, research, or general coding. These classifiers cause Claude to fall back from Opus 5.5 to Opus 5.

**Note:** These frontier LLM development classifiers apply only to Opus 5.5. Opus 5 doesn’t fall back on frontier LLM development questions.

### Distillation

Opus 5 and Opus 5.5 have classifiers that detect and directly block attempts to extract the model's internal reasoning. Distillation blocks don't fall back to another model, and the request is blocked outright.

Examples of blocked requests include prompts that ask Claude to repeat its reasoning verbatim or write its full chain of thought to an external output. You can still ask Claude to explain its reasoning, teach you a concept, or walk through a code review. Conversational requests like "why did you do that?" aren't affected.

## What happens after a fallback

Automatic model switching is active by default. When your request falls back, Claude re-runs your blocked request on a less capable model in the same conversation. All fallbacks are transparent, meaning you'll see a notice explaining that the model switched, and the response will be labeled with the model that answered.

After the switch, the model picker stays on the less capable model for the rest of the conversation. You can switch back to Opus 5 or Opus 5.5 anytime from the model picker.

**Note:** If you switch back to Opus 5 or Opus 5.5 after an automatic model switch, the same safeguards may cause Claude to fall back again if your original request is still part of the conversation. Editing your previous message before retrying often helps.

## If the fallback request is also blocked

Opus 4.8 has its own safety systems. If your request is also blocked on Opus 4.8, you can edit your message and retry.

For cybersecurity specifically, if your use case has a legitimate defensive purpose and is affected by these safeguards, you can apply for the Cyber Verification Program (CVP). Learn more about **[real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)**.

For biology, if your organization does legitimate life sciences research and is affected by these safeguards, you can apply for the Life Sciences Verification Program (LSVP). The LSVP gives verified life sciences organizations access to Claude's most capable models for internal research and development. Learn more in our blog: **[Introducing the Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program)**.

**Note:** Opus 5.5 isn't currently available in the Cyber Verification Program. If your organization already uses Opus 4.8 through the Cyber Verification Program, access to Opus 5 with fewer cyber restrictions is available now. Opus 5 is also compatible with Zero Data Retention.

## Manage automatic model switching

Automatic switching is enabled by default the first time you select Claude Opus 5 or Opus 5.5. It stays on by default, and you can turn it off anytime:

1. Go to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (or **Config > MODEL & OUTPUT** in Claude Code).

2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a request that falls back pauses the conversation instead of switching models. You can then:

- Edit your message and retry on Opus 5 or Opus 5.5

- Send the same message to a less capable model manually

## Give feedback

If your request is blocked but seems unrelated to cybersecurity, biology, frontier LLM development, or distillation, or if your legitimate security work keeps falling back, let us know. Use "Send feedback" to report it. Reports of incorrectly blocked requests help us narrow and improve these safeguards.

## Where automatic model switching applies

Automatic model switching works the same way everywhere you can use Claude Opus 5 or Opus 5.5:

- Claude on the web

- Claude Mobile

- Claude Desktop

- Claude Cowork

- Claude Code

- Claude Design

- Claude for Microsoft 365

- Claude Tag

- Claude Science

**Important:** If you're using the Claude API, model switching works differently. Automatic switching isn't active by default, and API customers must opt into and configure the fallbacks. Until fallbacks are configured, the model will return a 200 response with a stop reason on the API. See the **[developer documentation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)** for details.

Read our blog to learn more about **[Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)** and **[Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)**.

Our safeguards are built to match the capabilities of a model. For how safeguards work on Claude Fable 5, see **[Why Claude switched models in your conversation with Fable 5](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5).**