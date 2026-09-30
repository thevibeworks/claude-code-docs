# Why Claude switched models in your conversation with Sonnet 5.5

This article explains why a request might fall back to another model or be blocked on Claude Sonnet 5.5, what happens when your chat switches models, and how to manage automatic switching.

## Why some requests get blocked

Because its cybersecurity capabilities are a substantial step up from Claude Sonnet 5's, Claude Sonnet 5.5 is the first Sonnet model with cyber fallbacks like those we’ve developed for our most capable models. Its biology safeguards are the same as Sonnet 5’s. Both safeguards target a narrow set of high-risk requests; routine software development and most life sciences work are unaffected.

Most requests sent to Sonnet 5.5 won't encounter these safeguards. A narrow set of higher-risk requests either fall back to Sonnet 5 or are blocked directly, so we can keep supporting everyday work while limiting the risk of misuse. We continue to refine these safeguards so they block fewer legitimate requests, including fine-tuning our classifiers to reduce false positives. Your feedback helps guide this work.

## What requests may fall back or get blocked

Sonnet 5.5 runs automated safety checks, or classifiers, on every request. The checks also review everything the model reads, not just your latest message. This includes memory, content from connectors, web search results, and files, so a fallback or block can be triggered by content you didn't type.

Fallbacks and blocks work differently depending on the type of classifier triggered: cybersecurity, biology, LLM development, or distillation.

## Cybersecurity

Sonnet 5.5 may fall back to Claude Sonnet 5 when our cyber classifiers flag potentially higher-risk offensive cybersecurity requests, such as:

- Exploit generation

- Binary-based vulnerability scanning

- Penetration testing

You can still use Sonnet 5.5 for secure coding use cases, such as scanning source code for vulnerabilities.

## Biology

Sonnet 5.5 blocks requests that could help someone cause serious biological harm. Biology blocks don't fall back to another model, and the request is blocked outright.

Sonnet 5.5 uses the same set of biology safeguards as Sonnet 5. These target harmful requests; most research, education, and clinical work is unaffected, though some microbiology and virology requests may be flagged in error. Organizations can apply to our Life Sciences Verification Program for access to safeguards designed for the full breadth of biology-related work.

## Frontier LLM development

Sonnet 5.5 has classifiers for a small set of capabilities related to developing the most advanced LLMs, such as kernel development for certain ML accelerators. They shouldn't affect the vast majority of traditional AI or ML development, research, or general coding. When these classifiers flag a request, Claude falls back from Sonnet 5.5 to Sonnet 5.

## Distillation

Sonnet 5.5 has classifiers that detect and directly block attempts to extract the model's internal reasoning. Distillation blocks don't fall back to another model, and the request is blocked outright.

Examples of blocked requests include prompts that ask Claude to repeat its reasoning verbatim or write its full chain of thought to an external output. You can still ask Claude to explain its reasoning, teach you a concept, or walk through a code review. Conversational requests like "why did you do that?" aren't affected.

## What happens after a fallback

Automatic model switching is active by default. When your request falls back, Claude re-runs it on Sonnet 5 in the same conversation. All fallbacks are transparent, meaning you'll see a notice explaining that the model switched, and the response is labeled with the model that answered.

After the switch, the model picker stays on Sonnet 5 for the rest of the chat. You can switch back to Sonnet 5.5 anytime from the model picker.

**Note:** If you switch back to Sonnet 5.5 after an automatic model switch, the same safeguards may cause Claude to fall back again if your original request is still part of the conversation. Editing your previous message before retrying often helps.

## If the fallback request is also blocked

Sonnet 5 has its own safety systems. If your request is also blocked on Sonnet 5, you can edit your message and retry.

For biology, if your organization does legitimate life sciences research and is affected by these safeguards, you can apply for the Life Sciences Verification Program (LSVP) for expanded capabilities. On Sonnet 5.5, LSVP relaxes biology safeguards only through the High-risk Use add-on. Learn more in our blog: **[Introducing the Life Sciences Verification Program](https://support.claude.com/en/articles/16975617)**.

Sonnet 5.5 isn't available in the Cyber Verification Program at launch. Soon, cyberdefenders will be able to apply to our expanded Cyber Verification Program for tiered access to more advanced capabilities on Sonnet 5.5.

**Note:** Claude Sonnet 5.5 is compatible with Zero Data Retention (ZDR).

## Manage automatic model switching

Automatic switching is enabled by default for Sonnet 5.5, and you can turn it off anytime:

1. Go to **Settings > Capabilities** (or **Config > MODEL & OUTPUT** in Claude Code).

2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a request that falls back pauses the chat instead of switching models. You can then:

- Edit your message and retry on Sonnet 5.5

- Send the same message to a different model manually

## Usage and billing

How a request that falls back or is blocked is billed depends on when the block happens and which classifier triggered it:

- **Blocked before Claude responds:** To disrupt coordinated attacks on our safeguards, refusals that arrive before any output are billed when they stop or fall back due to biology, distillation, or LLM development safety classifiers. Requests blocked before any output in other categories aren't charged.

- **Blocked after Claude starts responding:** If a request is blocked midstream, the input tokens and those streamed before the block are charged at the rates of the model that produced them.

- **Fallback requests:** If you're opted into automatic model switching and the chat switches to Sonnet 5 after a block, the Sonnet 5 response is charged separately, at Sonnet 5's rates. We provide a credit to compensate for the cache miss of the fallback request.

Learn more about **[refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed)**.

## Give feedback

If your request is blocked but seems unrelated to one of the classifiers listed above, or if your legitimate work keeps falling back, let us know. Use "Send feedback" to report it. Reports of incorrectly blocked requests help us narrow and improve these safeguards.

## Where automatic model switching applies

Automatic model switching works the same way everywhere you can use Claude Sonnet 5.5:

- Claude on the web

- Claude Mobile

- Claude Desktop

- Claude Cowork

- Claude Code

- Claude Design

- Claude for Microsoft 365

- Claude Tag

- Claude Science

**Important:** If you're using the Claude API, model switching works differently. Automatic switching isn't active by default, and API customers must opt into and configure fallbacks. Until fallbacks are configured, the model returns a 200 response with a stop reason on the API. See the **[developer documentation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)** for details.

Read our blog to learn more about **[Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)**.

Our safeguards are built to match the capabilities of a model.

For how safeguards work on Claude Opus 5.5, see **[Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681)**. For Claude Fable 5.1, see **[Why Claude switched models in your conversation with Fable 5 or Fable 5.1](https://support.claude.com/en/articles/15363606)**.