# Why Claude switched models in your conversation with Fable 5 or Fable 5.1

This article explains why a request might be blocked on Claude Fable 5 or Fable 5.1, what happens when your conversation switches to a different Claude model, and how to manage automatic switching.

## Why some requests get blocked

Claude Fable 5 and Fable 5.1's capabilities far exceed those of every model we've previously made generally available. They are state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, vision, and many other areas.

Releasing a model this capable comes with risks. Without strong safeguards, Claude Fable 5 and Fable 5.1's advanced capabilities in areas like cybersecurity and biology could be misused by users to create large-scale cyberattacks or bioweapons that could result in catastrophic damage. These capabilities are the reason we’ve previously only released Mythos-class models (like Mythos Preview) to a small number of selected and vetted partners.

Recognizing these risks, to allow general users to access the vast majority of Fable 5 and Fable 5.1's capabilities, we've launched these models with safeguards that redirect or block their responses in some specific areas in line with our **[Terms of Service](https://www.anthropic.com/legal/commercial-terms)** and **[Usage Policy](https://www.anthropic.com/legal/aup)**. We’ve also **[been iterating](https://www.anthropic.com/news/redeploying-fable-5)** on safeguards since our first launch of Claude Fable 5.

We're working on making these safeguards more precise to help block only genuinely risky requests, with fewer false positives than there are today. Most user queries blocked by these safeguards on Fable 5 or Fable 5.1 may instead receive a response from our next-most-capable model (i.e., "fallback"), which can respond to these types of queries.

## What requests may fall back

**Claude Fable 5 and Fable 5.1 runs automated safety checks, or classifiers, on every user request. These checks are intended to visibly fall back from Fable 5 and Fable 5.1 to Opus models when users submit requests in:**

- Offensive cybersecurity techniques, such as building exploits, malware, or attack tooling. Claude Fable 5 and Fable 5.1 can assist with routine cybersecurity tasks, but users should expect high fallback rates. The safeguards are designed to block access to Mythos-level capabilities.

- A large fraction of queries we consider dual-use in biology, such as virology, toxicology, drug design, and molecular design—so Fable 5 and Fable 5.1 are not recommended for professional biology research and drug development at this time. (**[Classifier updated](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)**: August 6, 2026 on Claude, Claude apps, and Claude Platform, with Amazon Bedrock, Claude Platform on AWS, Google Cloud Vertex AI, and Microsoft Foundry to follow.)

- Distillation attacks on Fable 5 and Fable 5.1, including attempts to extract the model’s **[summarized thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking).**

- A narrow set of frontier LLM development tasks, such as distributed training infrastructure, ML accelerator design, and kernel development for certain non-standard chips.

These blocking safeguards are intentionally broad, and we work to continuously improve the safeguards to reduce their user-experience impact. When requests are blocked, they may fall back to a non-Mythos model, currently Opus 5 for biology, chemistry, and life sciences requests, and Opus 4.8 for offensive cybersecurity technique requests.

The checks also review everything the model reads, not just your latest message—including memory, content from connectors, web search results, and files, so a block can be triggered by content you didn't type.

## What happens after a fallback

Automatic model switching is active by default. When your request falls back, Claude re-runs your blocked Claude Fable 5 or Fable 5.1 request on an Opus model in the same conversation. You’ll see a notice explaining that the model switched, and the response will be labeled with the model that answered. Opus is a highly capable model with strong safeguards of its own, and for most otherwise legitimate requests blocked on Fable 5 or Fable 5.1, Opus should give you a helpful answer.

After the switch, the model picker stays on Opus for the rest of the conversation. You can switch back to Claude Fable 5 or Fable 5.1 anytime from the model picker.

**Note:** If you switch back to Claude Fable 5 or Fable 5.1 after an automatic model switch, the same Fable 5 or Fable 5.1 safeguards may cause Claude to fallback again if your original request is still part of the conversation. Editing your previous message before retrying often helps.

## If the fallback request is also blocked

Opus has its own safety systems. To learn about fallbacks in Claude Opus 5, see **[Why Claude switched models in your conversation with Opus 5](https://support.claude.com/en/articles/16049681)**.

If your request is also blocked on the less capable model, you can edit your message and retry. For cybersecurity specifically, if your use case has a legitimate defensive purpose and is being affected by these safeguards, you can apply for the Cyber Verification Program (CVP) for Opus. Learn more about **[real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)**.

## Manage automatic model switching

Automatic switching is enabled by default the first time you select Claude Fable 5 or Fable 5.1. It stays on by default, and you can turn it off anytime:

1. Go to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (or **Config > MODEL & OUTPUT** in Claude Code).

2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a blocked request pauses the conversation instead of switching models. You can then:

- Edit your message and retry on  Claude Fable 5 or Fable 5.1

- Send the same message to a less capable model manually
​

## Usage and billing

Blocked requests are billed differently depending on when the block happens:

- **Blocked before Claude responds:** To disrupt coordinated attacks on our safeguards, refusals that arrive before any output are billed when they stop or fall back due to biology, distillation, or frontier LLM development safety classifiers. These are the categories where our false positive rates are lowest as of September 2026. Requests blocked before any output in other categories are not charged.

- **Blocked after Claude starts responding:** If a request is blocked midstream, the input tokens and those streamed before the block are charged at the rates of the model that produced them.

- **Fallback requests:** If you are opted into automatic model switching, and the conversation switches to Opus after a block, the Opus response is charged separately, at the respective model’s rates. We provide a credit to compensate for the cache miss of the fallback request at the time of the request.

Learn more about **[refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed)**.

## Give feedback

If your blocked request seems unrelated to one of the classifiers listed above, or if your legitimate work in these areas keeps getting blocked, let us know. Use "Send feedback" to report it. Reports of incorrectly blocked requests help us narrow and improve these safeguards.

## Stay tuned for updates

Moving forward, we plan to consider ways to open up allocations for dual-use cyberdefense and biology research. As our safety systems mature, we aim to support legitimate biology and defensive cybersecurity work while keeping strong protections against misuse in place.

We'll share more details about the program, including eligibility and how to apply, as they become available. Watch this Help Center for updates, or **[sign up for notifications here](https://claude.com/form/mythos-access-interest)**.

## Where automatic model switching applies

Automatic model switching works the same way everywhere you can use Claude Fable 5 and Fable 5.1:

- Claude on the web

- Claude Mobile

- Claude Desktop

- Claude Cowork

- Claude Code

- Claude Design

- Claude for Microsoft 365

- Claude Tag

**Important:** If you're using the Claude API, model switching works differently. Automatic switching isn't active by default, and API customers must opt into and configure fallbacks. Until fallbacks are configured, the model will return a 200 response with a stop reason on the API. See the **[developer documentation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)** for details.

Read our blog to learn more about **[Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)**.

Our safeguards are built to match the capabilities of a model. For how safeguards work on Claude Opus 5, see **[Why Claude switched models in your conversation with Opus 5](https://support.claude.com/en/articles/16049681)**.