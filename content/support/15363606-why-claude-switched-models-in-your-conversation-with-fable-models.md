# Why Claude switched models in your conversation with Fable models

This article explains why a request might be blocked on Claude Fable models, what happens when your conversation switches to a different Claude model, which blocks don’t switch models, and how to manage automatic switching.

## Why some requests get blocked

Claude Fable 5.2, Fable 5.1, and Fable 5 are Mythos-class models, which means they perform at a very high level in areas like software engineering, knowledge work, and vision, as well as in cybersecurity and biology.

Releasing models with these capabilities comes with risks. Without strong safeguards, Fable's advanced capabilities in areas like cybersecurity and biology could be misused by users to create large-scale cyberattacks or bioweapons that could result in catastrophic damage.

Recognizing these risks, to allow general users to access the vast majority of Fable's capabilities, we've launched these models with safeguards that redirect or block their responses in some specific areas in line with our **[Terms of Service](https://www.anthropic.com/legal/commercial-terms)** and **[Usage Policy](https://www.anthropic.com/legal/aup)**. We’ve also **[been iterating](https://www.anthropic.com/news/redeploying-fable-5)** on safeguards since our first launch of Claude Fable 5.

We're working on making these safeguards more precise to help block only genuinely risky requests, with fewer false positives than there are today. Most user queries blocked by these safeguards on Fable models may instead receive a response from a less capable model (i.e., "fallback"), which can respond to these types of queries. Some requests, including those that try to extract the model's reasoning, are blocked with no fallback.

## What requests may fall back

**Claude Fable 5.2, Fable 5.1, and Fable 5 run automated safety checks, or classifiers, on every user request. These checks are intended to visibly fallback from Fable models to Opus models when users submit requests in:**

- Offensive cybersecurity techniques, such as building exploits, malware, or attack tooling. Claude Fable 5.2, Fable 5.1, and Fable 5 can assist with routine cybersecurity tasks, but users should expect high fallback rates. The safeguards are designed to block access to Mythos-level capabilities.

- A large fraction of queries we consider dual-use in biology, such as virology, toxicology, drug design, and molecular design—so Fable models are not recommended for professional biology research and drug development at this time. (**[Classifier updated](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)**: August 6, 2026 on Claude, Claude apps, and Claude Platform, with Amazon Bedrock, Claude Platform on AWS, Google Cloud Vertex AI, and Microsoft Foundry to follow.)

- A narrow set of frontier LLM development tasks, such as distributed training infrastructure, ML accelerator design, and kernel development for certain non-standard chips.

These blocking safeguards are intentionally broad, and we work to continuously improve the safeguards to reduce their user-experience impact. When requests are blocked, they may fall back to a non-Mythos model, currently Opus 5 for biology, chemistry, and life sciences requests, and for frontier LLM development requests, and Opus 4.8 for offensive cybersecurity technique requests.

Requests that attempt to extract the model’s reasoning, such as attempts to expose its **[summarized thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking)**, are blocked outright. They don’t fall back to another model.

The checks also review everything the model reads, not just your latest message—including memory, content from connectors, web search results, and files, so a block can be triggered by content you didn't type.

## What happens after a fallback

Automatic model switching is active by default in Claude apps and must be configured in the API. When your request falls back, Claude re-runs your blocked Fable request on an Opus model in the same conversation. You’ll see a notice explaining that the model switched, and the response will be labeled with the model that answered.

After the switch, the model picker stays on Opus for the rest of the conversation. You can switch back to Fable models anytime from the model picker.

**Note:** If you switch back to Fable models after an automatic model switch, the same Fable safeguards may cause Claude to fall back again if your original request is still part of the conversation. Editing your previous message before retrying often helps.

## If the fallback request is also blocked

Opus has its own safety systems. To learn about fallbacks in Claude Opus 5, see **[Why Claude switched models in your conversation with Opus 5](https://support.claude.com/en/articles/16049681)**.

If your request is also blocked on the less capable model, you can edit your message and retry. For cybersecurity specifically, if your use case has a legitimate defensive purpose and is being affected by these safeguards, you can apply for the Cyber Verification Program (CVP) for Opus. Learn more about the **[Cyber Verification Program](https://support.claude.com/en/articles/14604842)**.

## Manage automatic model switching

Automatic switching is enabled by default the first time you select a Claude Fable model. It stays on by default, with each category’s behavior **[as described above](#h_74dc898410)**, and you can turn it off anytime:

1. Go to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (or **Config > MODEL & OUTPUT** in Claude Code).

2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a blocked request pauses the conversation instead of switching models. You can then:

- Edit your message and retry on  the same Fable model

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

Automatic model switching works the same way everywhere you can use Claude Fable 5.2, Fable 5.1, and Fable 5:

- Claude on the web

- Claude Mobile

- Claude Desktop

- Claude Cowork

- Claude Code

- Claude Design

- Claude for Microsoft 365

- Claude Tag

**Important:** If you're using the Claude API, model switching works differently. Automatic switching isn't active by default, and API customers must opt into and configure fallbacks. Until fallbacks are configured, the model will return a 200 response with a stop reason on the API. See the **[developer documentation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)** for details.

For more information about Fable models, refer to this page: **[Claude Fable](https://www.anthropic.com/claude/fable)**.

Our safeguards are built to match the capabilities of a model. For how safeguards work on Opus models, see **[Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681)**. For more information about safeguards on Sonnet 5.5, see **[Why Claude switched models in your conversation with Sonnet 5.5](https://support.claude.com/en/articles/17161993)**.