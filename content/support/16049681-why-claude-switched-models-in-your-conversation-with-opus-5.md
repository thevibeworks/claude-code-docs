# Why Claude switched models in your conversation with Opus 5

This article explains why a request might fallback on Claude Opus 5, what happens when your conversation switches to another model, and how to manage automatic switching.

## Why some requests get blocked

Claude Opus 5 improves on Claude Opus 4.8 across the board, including in software engineering and cybersecurity. We've set its safeguards in line with those capability gains.

Most cyber requests sent to Opus 5 will not encounter fallback safety interventions. A narrow set of higher-risk cybersecurity requests fallback to Opus 4.8, our next-most-capable model, so we can keep supporting everyday security work while limiting the risk of misuse. We're continuing our work to reduce false positives, and your feedback helps inform these improvements.

## What requests may fallback

Claude Opus 5 runs automated safety checks, or classifiers, on every user request. These checks cause Claude to visibly fallback from Opus 5 to Opus 4.8 when you submit higher-risk offensive cybersecurity requests, such as:

- Exploit generation

- Binary-based vulnerability scanning

- Penetration testing

You can still use Opus 5 for security work, including scanning source code for vulnerabilities, triaging security issues, and building secure code.

The checks also review everything the model reads, not just your latest message. This includes memory, content from connectors, web search results, and files, so a fallback can be triggered by content you didn't type.

In early testing, Opus 5 traffic ran into cyber fallbacks 85% less than Fable 5.

**Note:** While Claude Opus 5 improves on Opus 4.8 in biology, it is not as capable as Fable 5 at real world long-horizon tasks for novel research discoveries that could lead to significant risk. As a result, Opus 5 doesn't fallback on biology, chemistry, or life-sciences questions. It uses similar safeguards for these topics as Opus 4.8.

## What happens after a fallback

Automatic model switching is active by default. When your request falls back, Claude re-runs your blocked Opus 5 request on a less capable model in the same conversation. You'll see a notice explaining that the model switched, and the response will be labeled with the model that answered.

After the switch, the model picker stays on the less capable model for the rest of the conversation. You can switch back to Opus 5 anytime from the model picker.

**Note:** If you switch back to Opus 5 after an automatic model switch, the same Opus 5 safeguards may cause Claude to fallback again if your original request is still part of the conversation. Editing your previous message before retrying often helps.

## If the fallback request is also blocked

Opus 4.8 has its own safety systems. If your request is also blocked on Opus 4.8, you can edit your message and retry. For cybersecurity specifically, if your use case has a legitimate defensive purpose and is affected by these safeguards, you can apply for the Cyber Verification Program (CVP). Learn more about **[real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)**.

**Note:** If your organization already uses Opus 4.8 through the Cyber Verification Program, access to Opus 5 with fewer cyber restrictions is available now. Opus 5 is also compatible with Zero Data Retention.

## Manage automatic model switching

Automatic switching is enabled by default the first time you select Claude Opus 5. It stays on by default, and you can turn it off anytime:

1. Go to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** (or **Config > MODEL & OUTPUT** in Claude Code).

2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a request that falls back pauses the conversation instead of switching models. You can then:

- Edit your message and retry on Opus 5

- Send the same message to a less capable model manually

## Give feedback

If your request is blocked but seems unrelated to cybersecurity, or if your legitimate security work keeps falling back, let us know. Use "Send feedback" to report it. Reports of incorrectly blocked requests help us narrow and improve these safeguards.

## Where automatic model switching applies

Automatic model switching works the same way everywhere you can use Claude Opus 5:

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

Read our blog to learn more about**[Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)**.

Our safeguards are built to match the capabilities of a model. For how safeguards work on Claude Fable 5, see **[Why Claude switched models in your conversation with Fable 5](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5).**