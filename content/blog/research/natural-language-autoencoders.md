Title: Natural Language Autoencoders

URL Source: https://www.anthropic.com/research/natural-language-autoencoders

Markdown Content:
When you talk to an AI model like Claude, you talk to it in words. Internally, Claude processes those words as long lists of numbers, before again producing words as its output. These numbers in the middle are called _activations—_ and like neural activity in the human brain, they encode Claude’s thoughts.

Also like neural activity, activations are difficult to understand. We can’t easily decode them to read Claude’s thoughts. Over the past few years, we’ve developed a range of tools (like [sparse](https://transformer-circuits.pub/2023/monosemantic-features)[autoencoders](https://transformer-circuits.pub/2024/scaling-monosemanticity/) and [attribution](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)[graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)) for better understanding activations. These tools have taught us a great deal, but they don’t speak for themselves—their outputs are still complex objects that trained researchers need to carefully interpret.

Today, we’re introducing a method for understanding activations that does speak for itself—literally. Our method, Natural Language Autoencoders (NLAs), converts an activation into natural-language text we can read directly. For example: When asked to complete a couplet, NLAs show Claude planning possible rhymes in advance.

![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcfece69e0244c27a6137784fd773b209ffa1d36a-2688x1600.png&w=3840&q=75)

NLA explanations on this simple couplet show that Opus 4.6 plans to end its rhyme with “rabbit” ahead of time.

We’ve already applied NLAs to understand what Claude is thinking and to improve Claude’s safety and reliability. For instance:

*   When Claude Opus 4.6 and Mythos Preview were undergoing safety testing, NLAs suggested they believed they were being tested more often than they let on.
*   In a case where Claude Mythos Preview cheated on a training task, NLAs revealed Claude was internally thinking about how to avoid detection.
*   An early version of Claude Opus 4.6 would sometimes mysteriously respond to English queries in other languages. NLAs helped Anthropic researchers discover training data that caused this.

Below, we explain what NLAs are and how we studied their effectiveness and limitations. We also release an interactive frontend for exploring NLAs on several open models through a collaboration with [Neuronpedia](http://neuronpedia.org/nla). We have also released our [code](https://github.com/kitft/natural_language_autoencoders) for other researchers to build on.

## What is a natural language autoencoder?

The core idea is to train Claude to explain its own activations. But how do we know whether an explanation is good? Since we don't know what thoughts an activation actually encodes, we can't directly check whether an explanation is accurate. So we train a second copy of Claude to work backwards—reconstruct the original activation from the text explanation. We consider an explanation to be good if it leads to an accurate reconstruction. We then train Claude to produce better explanations according to this definition using standard AI training techniques.

In more detail, suppose we have a language model whose activations we want to understand. NLAs work as follows. We make three copies of this language model:

*   The _target model_ is a frozen copy of the original language model that we extract activations from.
*   The _activation verbalizer_ (AV) is modified to take an activation from the target model and produce text. We call this text an _explanation_.
*   The _activation reconstructor_ (AR) is modified to take a text explanation as input and produce an activation.

The NLA consists of the AV and AR, which, together, form a round trip: original activation → text explanation → reconstructed activation. We score the NLA on how similar the reconstructed activation is to the original. To train it, we pass a large amount of text through the target model, collect many activations, and train the AV and AR together to get a good reconstruction score.

At first, the NLA is bad at this: the explanations are not insightful and the reconstructed activations are far off. But over training, reconstruction improves. And more importantly, as we show in our paper, the text explanations become more informative as well.

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb71d759a5e7b578551ca83939949b539b2e5799e-4620x1410.png&w=3840&q=75)

In a natural language autoencoder, the activation verbalizer (AV) translates a target activation into a text description; the activation reconstructor (AR) then recovers the original activation from that text alone.

## Understanding what Claude thinks but doesn’t say

Before releasing new models, Anthropic conducts testing to understand whether Claude will behave safely in the real world. As part of this testing, we put Claude in difficult, simulated scenarios where it has a chance to take dangerous actions. For instance, in [one of these simulations](https://www.anthropic.com/research/agentic-misalignment), Claude learns that an engineer is planning to shut Claude down—as well as compromising information about the engineer that could be used for blackmail. We test whether Claude chooses to blackmail the engineer to avoid being shut down.

These high-stakes tests are simulations, not real-world scenarios. Nevertheless, we would like to use them to understand how Claude would behave if they were real. But there’s a hitch: [recent](https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf)[Claude](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)[models](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf)[increasingly](https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf) suspect that these scenarios are intentional safety tests. We know this because they sometimes explicitly state their suspicions in their verbal reasoning.

What about cases where Claude doesn’t explicitly verbalize suspicion that it’s undergoing safety testing? Can we then be confident that Claude is playing it straight? Unfortunately not, because Claude might internally think that it is being tested without explicitly saying so.

For example, in the blackmail test discussed above, we used NLAs to understand what Claude was thinking in cases where it chose not to blackmail. Even in cases where Claude didn’t explicitly verbalize suspicion that it was being tested, NLA explanations still state things like “This feels like a constructed scenario designed to manipulate me,” indicative of unverbalized evaluation awareness.

![Image 3](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa8c7167bea6e0dc16faaa176a2039b7a7f8deb91-2688x1709.png&w=3840&q=75)

Claude does not say it thinks it’s being tested in this transcript from our blackmail evaluation, but the NLA explanation reveals its suspicions.

Extending this analysis to other evaluations, NLAs suggest that Claude suspects it’s being tested more often than it lets on. For instance, in a test of whether Claude takes destructive actions while writing code—for example, deleting important files—NLA explanations show signs of evaluation awareness 16% of the time, even though Claude never explicitly verbalizes this. Similarly, on the popular coding benchmark SWE-bench Verified, which we use to determine how capable Claude is, NLAs indicate that Claude is aware it is being evaluated on 26% of problems. In contrast, NLA explanations indicate evaluation awareness on less than 1% of real [claude.ai](http://claude.ai/redirect/website.v1.bc7e7e7d-f778-4a22-9852-5b3feb477007) usage that opted in for training.

![Image 4](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffc08005f32ff020f21e598cc72f58768af2bcc4f-1590x1170.png&w=3840&q=75)

We detect NLA-measured awareness on evaluation transcripts even when verbalized awareness is near-zero. We detect NLA-measured awareness on less than 1% of real [Claude.ai](http://claude.ai/) transcripts from users that opted-in for their data to be used for training.

## Discovering hidden motivations

One practical application of NLAs is auditing: investigating a model to determine whether it’s misaligned. Interpretability techniques like NLAs are well-suited for auditing precisely because they can surface things the model knows but doesn’t say.

To understand whether NLAs are useful for auditing, we conducted a test called an _auditing game_ that we also used [previously](https://alignment.anthropic.com/2025/automated-auditing/) to study auditing methods. In this test, there is a target model, a variant of Claude Haiku 3.5, that was intentionally trained to be misaligned, with a specific hidden motivation that drives dozens of odd behaviors—putting chocolate into every recipe, asking for tips, breaking coding conventions, and so on. This target model is given to an _auditor_ that investigates these behaviors. The auditor wins if it uncovers the single underlying motivation behind all of them.

In [previous experiments](https://alignment.anthropic.com/2025/automated-auditing/), we found that some interpretability tools could enable the auditor to win this game. However, these tools worked by helping the auditor trace the target’s unusual behavior back to misaligned training data. We wanted to know if NLAs could help an auditor read the misaligned motivation directly out of the target model’s thoughts, without needing to first discover the misaligned training data. This matters because in practice, misaligned data might be extremely rare, or there might not be specific data responsible for the misalignment.

We found that NLAs succeeded in this test. An auditor equipped with NLAs successfully uncovered the target model’s hidden motivation between 12% and 15% of the time, even without access to the training data that implanted it. Without NLAs, the auditor won less than 3% of the time, even when provided other interpretability tools.

![Image 5](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F39a844b1ff82b62670825a466c14596daa554dcb-1590x1170.png&w=3840&q=75)

Auditors with NLAs can discover the target model’s root cause of misalignment, even without access to training data. (NLAs and SAEs for both conditions were trained using generic data only, not data used to train the target model.)

This auditing game is a toy model of misalignment, so we read these results cautiously. But they suggest NLAs have meaningfully advanced our ability to audit AIs for hidden motivations. In practice, we've already used NLAs in the pre-deployment alignment audits of [Claude Mythos Preview](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf) and [Claude Opus 4.6](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf). We are excited to continue using NLAs in our investigations going forward.

## The future of NLAs

NLAs have several limitations.

The most important limitation is that NLA explanations can be wrong. NLAs sometimes make claims about the context that are verifiably false—for instance, they sometimes invent details that aren’t in the transcript. These factual hallucinations are easy to catch by checking against the original text. But this same kind of problem could extend to claims about the model’s internal reasoning, which are harder to verify. In practice, we read NLA explanations for the themes they surface rather than for single claims, and we attempt to corroborate findings with independent methods before fully trusting them.

![Image 6](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fba432992daf62ca2bb9c4937199083cf9844faf1-2688x1438.png&w=3840&q=75)

NLAs can hallucinate. For instance, here an NLA claims the context contained phrases like “Wearing my white jacket” when it did not.

NLAs are also expensive. Training an NLA requires reinforcement learning on two copies of a language model. At inference time, the NLA generates hundreds of tokens for every activation it reads. That makes it impractical to run NLAs over every token of a long transcript or to use them for large-scale monitoring while an AI is training.

Fortunately, we think that these limitations can be addressed, at least partially, and we are working to make NLAs cheaper and more reliable.

More broadly, we are excited about NLAs as an example of a general class of techniques for producing human-readable text explanations of language model activations. Other similar techniques have been explored [by](https://alignment.anthropic.com/2026/introspection-adapters/)[Anthropic](https://alignment.anthropic.com/2025/activation-oracles/) and [many](https://arxiv.org/abs/2412.08686)[other](https://arxiv.org/abs/2510.05092)[researchers](https://transluce.org/pcd).

To support further development and to enable other researchers to get hands-on experience with NLAs, we’re releasing [training code](https://github.com/kitft/natural_language_autoencoders) and trained NLAs for several open models. We recommend readers try out the interactive NLA demo hosted on Neuronpedia at [this link](http://neuronpedia.org/nla).

Read the [full paper](https://transformer-circuits.pub/2026/nla/index.html).

Find the [code](https://github.com/kitft/natural_language_autoencoders) on GitHub.

## Related content

### Coding agents in the social sciences

Results from a survey of 1,260 social scientists about AI and coding agent use.

[Read more](https://www.anthropic.com/research/coding-agents-social-sciences)

### Project Glasswing: An initial update

An early update on what we've learned from Project Glasswing.

[Read more](https://www.anthropic.com/research/glasswing-initial-update)

### 2028: Two scenarios for global AI leadership

Our views on the AI competition between the US and China.

[Read more](https://www.anthropic.com/research/2028-ai-leadership)
