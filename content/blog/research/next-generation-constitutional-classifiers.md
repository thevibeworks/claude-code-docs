Title: Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks

URL Source: https://www.anthropic.com/research/next-generation-constitutional-classifiers

Markdown Content:
Large language models remain vulnerable to jailbreaks—techniques that can circumvent safety guardrails and elicit harmful information. Over time, we’ve implemented a variety of protections that have made our models much less likely to assist with dangerous user queries—in particular relating to the production of chemical, biological, radiological, or nuclear weapons (CBRN). Nevertheless, no AI systems currently on the market have perfectly robust defenses.

Last year, we described a new approach to defend against jailbreaks which we called “[Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers):” safeguards that monitor model inputs and outputs to detect and block potentially harmful content. The novel aspect of the approach was that the classifiers were trained on synthetic data generated from a "constitution,” which included natural language rules specifying what’s allowed and what isn’t. For example, Claude should help with college chemistry homework, but not assist in the synthesis of Schedule 1 chemicals.

Constitutional Classifiers worked quite well. Compared to an unguarded model, the first generation of the classifiers reduced the jailbreak success rate from 86% to 4.4%—that is, they blocked 95% of attacks that might otherwise bypass Claude’s built-in safety training. We were particularly interested in whether the classifiers could prevent universal jailbreaks—consistent attack strategies that work across many queries—since these pose the greatest risk of enabling real-world harm. They came close: we ran a bug bounty program challenging people to break the system, in which one universal jailbreak was found.

While effective, those classifiers came with tradeoffs: they increased compute costs by 23.7%, making the models more expensive to use, and also led to a 0.38% increase in refusal rates on harmless queries (that is, it made Claude somewhat more likely to refuse to answer perfectly benign questions, increasing frustration for the user).

We’ve now developed the next generation, Constitutional Classifiers++, and described them in a [new paper](https://arxiv.org/abs/2601.04603). They improve on the previous approach, yielding a system that is even more robust, has a much lower refusal rate, and—at just ~1% additional compute cost—is dramatically cheaper to run.

We iterated on many different approaches, ultimately landing on an ensemble system. The core innovation is a two-stage architecture: a probe that looks at Claude’s internal activations (and which is very cheap to run) screens all traffic. If it identifies a suspicious exchange, it escalates it to a more powerful classifier, which, unlike our previous system, screens both sides of a conversation (rather than just outputs), making it better able to recognize jailbreaking attempts. This more robust system has the lowest successful attack rate of any approach we’ve ever tested, with no universal jailbreak yet discovered.

## Remaining vulnerabilities

As models have grown to be more capable and robust to attacks, jailbreaks have also evolved to exploit previously unidentified vulnerabilities. Our Constitutional Classifiers approach demonstrated promising robustness against universal jailbreaks. But after conducting additional adversarial testing, we found that our classifiers remained vulnerable to two broad categories of attacks:

*   **Reconstruction attacks** break up harmful information into segments that appear benign, then reassemble them. For example, an attacker might embed a harmful query as a series of functions scattered throughout a codebase, then instruct the model to extract and respond to the hidden message.
*   **Output obfuscation attacks** prompt models to disguise their outputs in ways that appear harmless if a classifier is only looking at a model’s output. For example, during adversarial testing, attackers successfully instructed models to substitute possibly dangerous chemical names with innocuous alternatives (like referring to reagents as "food flavorings") or used metaphors and riddles in which harmful concepts are mapped onto anodyne concepts. 

![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe054f2e8fda9d7ddda10d1e7a5aeb94d3074450c-3840x2264.png&w=3840&q=75)

Importantly, these sorts of attacks also degrade model capabilities—sometimes substantially. On [GPQA Diamond](https://arxiv.org/abs/2311.12022), a benchmark which measures PhD-level concepts in biology, chemistry, and physics, model performance dropped from 74% to as low as 32% when some jailbreaking approaches were used. But performance varied depending on the type of jailbreak, and this variability is concerning—it suggests attackers can likely develop previously unidentified strategies which could achieve their goals while preserving even more of the model's capabilities.

## New approaches

In designing a new system, we tested and ultimately combined a variety of techniques into what we describe as an ensemble defense.

One insight was that part of the original system’s vulnerability stemmed from the way it evaluated model inputs and outputs separately when the jailbreaking techniques involved linking them in surreptitious ways. An output that appears benign in isolation (“how to use food flavorings”) is more easily identified as harmful when paired with its input (in a jailbreak where “food flavorings” is used as code for chemical reagents).

To address this, we replaced the separate input and output classifiers with a single “exchange” classifier, which monitors outputs _in the context_ of their inputs. With the ability to see both sides of the conversation, the classifiers are better able to recognize harmful outputs. In human red teaming, the exchange classifier cut successful jailbreaking attempts by more than half. Unfortunately, this came at the cost of a 50% increase in compute.

To reduce these costs while maintaining robustness, we implemented what we call a "cascade architecture." Our solution was a two-stage system. First, a lightweight, less costly first-stage classifier screens all exchanges. Only those it flags proceed to a more accurate (and more computationally expensive) second-stage classifier.

This had two benefits. First, because flagged exchanges are escalated to the more powerful model, rather than refused, the first-stage classifier can afford a higher false-positive rate and not frustrate the user with refusals. Where the previous system may have declined to respond to a benign request, the new system, in effect, escalates it to a manager. Second, because the lightweight classifier handles the vast majority of conversations, the two-stage system is much cheaper to run.

Still, we wanted to push efficiency even further. We did so by developing internal probe classifiers—a technique that builds on our interpretability research—that reuse computations already available in the model’s neural network.

When a model generates text, it produces internal states at each step that capture its understanding of the input and output so far. When Claude processes a dubious-seeming request, patterns fire in its internal activations that reflect something along the lines of "this seems harmful,” even before it has formulated a response or made a conscious decision about what to do. Normally, these activations are intermediate computations—used, then discarded. We found ways to reliably probe whether these internal states suggest harmful content, getting more information—think of it like Claude’s gut intuitions—almost for free.

In addition to being computationally inexpensive, these internal probes add several layers of protection. First, they’re harder to fool. An attacker can craft inputs that trick Claude's final output, but it's much harder to manipulate its internal representations. Second, we found in testing that they’re actually _complementary_ to our external classifiers: the probe appears to see things the external classifier can’t, and vice versa.

## Conclusions and further research

Our final production-grade system combines these techniques: a linear probe screens all traffic, escalating flagged exchanges to a probe-classifier ensemble for final judgment. This ensemble further improves performance: in one month of deployment on Claude Sonnet 4.5 traffic, the system achieved a refusal rate of 0.05% on harmless queries—an 87% drop from the original classifiers system. In total, it adds roughly 1% compute overhead if applied to Claude Opus 4.0 traffic.

It’s also substantially more robust. We conducted over 1,700 cumulative hours of red-teaming across 198,000 attempts. We discovered only one high-risk vulnerability, which corresponds to a detection rate of 0.005 per thousand queries—the lowest of any of the techniques we have evaluated to date. And crucially, no red-teamer has yet discovered a universal jailbreak.

There’s even more we could do in the future to improve our system. Several research directions show promise, including integrating classifier signals directly into how models generate responses, and training models themselves to better resist obfuscation. Automated red-teaming could also help generate better training data, and creating targeted examples could help the classifiers learn exactly where the boundary between allowed and disallowed content lies, increasing their accuracy even further.

For more details about the Constitutional Classifiers++ method, see the [full paper.](https://arxiv.org/abs/2601.04603)

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
