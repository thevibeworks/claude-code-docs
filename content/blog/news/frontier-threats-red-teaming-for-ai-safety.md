Title: Frontier Threats Red Teaming for AI Safety

URL Source: https://www.anthropic.com/news/frontier-threats-red-teaming-for-ai-safety

Markdown Content:
![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fefd36fc64fd3b723e596406e5320161276017b57-2880x1620.png&w=3840&q=75)

“Red teaming,” or adversarial testing, is a recognized technique to measure and increase the safety and security of systems. While [previous Anthropic research](https://www.anthropic.com/research/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) reported methods and results for red teaming using crowdworkers, for some time, AI researchers have noted that AI models could eventually obtain capabilities in areas relevant to national security. For example, researchers have [called](https://cdn.openai.com/papers/gpt-4-system-card.pdf) to [measure](https://arxiv.org/abs/2305.15324) and [monitor](https://arxiv.org/abs/2108.12427)[these risks](https://938f895d-7ac1-45ec-bb16-1201cbbc00ae.usrfiles.com/ugd/938f89_74d6e163774a4691ae8aa0d38e98304f.pdf), and have [written](https://arxiv.org/abs/2306.03809)[papers](https://arxiv.org/abs/2304.05332) with evidence of risks. Anthropic CEO Dario Amodei also highlighted this topic in [recent Senate testimony](https://www.judiciary.senate.gov/committee-activity/hearings/oversight-of-ai-principles-for-regulation). With that context, we were pleased to advocate for and join in commitments announced at the White House on July 21 that included “internal and external security testing of [our] AI systems” to guard against “some of the most significant sources of AI risks, such as biosecurity and cybersecurity.” However, red teaming in these specialized areas requires intensive investments of time and subject matter expertise.

In this post, we share our approach to “frontier threats red teaming,” high level findings from a project we conducted on biological risks as a test project, lessons learned, and our future plans in this area.

Our goal in this work is to evaluate a baseline of risk, and to create a repeatable way to perform frontier threats red teaming across many topic areas. With respect to biology, while the details of our findings are highly sensitive, we believe it’s important to share our takeaways from this work. In summary, working with [experts](https://www.gryphonscientific.com/), we found that models might soon present risks to national security, if unmitigated. However, we also found that there are mitigations to substantially reduce these risks.

We are now [scaling up this work](https://jobs.lever.co/Anthropic/8f565d59-8831-443a-b72a-cb9ef8ae06b2) in order to reliably identify risks and build mitigations. We believe that improving frontier threats red teaming will have immediate benefits and contribute to [long-term AI safety](https://www.anthropic.com/news/core-views-on-ai-safety). We have been sharing our findings with government, labs, and other stakeholders, and we’d like to see more independent groups doing this work.

## Conducting frontier threats red teaming

Frontier threats red teaming requires investing significant effort to uncover underlying model capabilities. The most important starting point for us has been working with domain experts with decades of experience. Together, we started by defining threat models: what kind of information is dangerous, how that information is combined to create harm, and what degree of accuracy and frequency is required for it to be dangerous. For example, to create harm, it is often necessary to string together many pieces of accurate information, not just generate a single harmful-sounding output.

Following a well-defined research plan, subject matter and LLM experts will need to collectively spend substantial time (i.e. 100+ hours) working closely with models to probe for and understand their true capabilities in a target domain. For example, domain experts may need to learn the best way to interact with or “jailbreak” models.

An important objective is to build new, automated evaluations based on expert knowledge, and the tooling to run those evaluations to make them repeatable and scalable. However, one challenge is that this information is likely to be sensitive. Therefore, this kind of red teaming requires partnerships with trusted third parties and strong information security protections.

## Findings from red teaming biology

Over the past six months, we spent more than 150 hours with [top biosecurity experts](https://www.gryphonscientific.com/) red teaming and evaluating our model’s ability to output harmful biological information, such as designing and acquiring biological weapons. These experts learned to converse with, jailbreak, and assess our model. We developed quantitative evaluations of model capabilities. The experts used a bespoke, secure interface to our model without the trust and safety monitoring and enforcement tools that are active on our public deployments.

We discovered a few key concerns. The first is that current frontier models can sometimes produce sophisticated, accurate, useful, and detailed knowledge at an expert level. In most areas we studied, this does not happen frequently. In other areas, it does. However, we found indications that the models are more capable as they get larger. We also think that models gaining access to tools could advance their capabilities in biology. Taken together, we think that unmitigated LLMs could accelerate a bad actor’s efforts to misuse biology relative to solely having internet access, and enable them to accomplish tasks they could not without an LLM. These two effects are likely small today, but growing relatively fast. If unmitigated, we worry that these kinds of risks are near-term, meaning that they may be actualized in the next two to three years, rather than five or more.

However, the process of researching these risks also enables the discovery and implementation of mitigations for them. We found, for example, that straightforward changes in the training process meaningfully reduce harmful outputs by enabling the model to better distinguish between harmful and harmless uses of biology (see, for example, our work on [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)). We also found that classifier-based filters can make it harder for a bad actor to get the kind of multiple, chained-together, and expert-level pieces of information needed to do harm. These are now deployed in our public-facing frontier model, and we’ve identified a list of mitigations at every step of the model development and deployment pathway that we will continue to experiment with.

## Future Research

At the end of the project, we now have more experiments and evaluations we’d like to run than we started with. For example, we think a very important experiment to repeatedly run will be to measure the speedup that LLMs might provide towards producing harm compared with, for example, a search engine. And we should do so not just with today’s frontier models, but with future ones – next generation models, tool-using models, and multimodal models, for example.

Given our finding that today’s frontier models provide warning of near future risks, frontier model developers should collectively and urgently do more analysis and develop more and stronger mitigations, sharing this information with responsible industry developers so they can add safeguards to their models, and with select government agencies.

We should also prepare for the potential release of models that have not been subject to frontier threats red teaming. We suspect that absent new approaches to mitigation, bad actors could extract harmful biological capabilities with smaller, fine-tuned, or task-specific models adapted from the weights of openly available models if sufficiently capable base models are released.

## We're scaling up and supporting this work

This empirical work confirms that frontier threats red teaming in areas of national security is important and timely. Current models are only showing the first very early signs of risks of this kind, which makes this our window to evaluate nascent risks and mitigate them before they become acute. It is important to increase efforts before a further generation of models that use new tools. Luckily, there is already a wealth of expertise within national security communities to draw on that can help build threat models, evaluations, and mitigations.

It is also an area that governments are naturally familiar with. This means that national security is a domain where governments, labs, and other stakeholders can collaborate. To start, we are establishing a disclosure process by which labs and other stakeholders can report these risks and their mitigations to other relevant actors. Ultimately, we think it is very important that new third parties be set up to conduct national security evaluations between these stakeholders. These third parties would be impartial and would need to have appropriate safeguards to handle sensitive information.

The frontier threats red teaming research agenda is likely to be useful for other types of risks that appear poised to occur on a longer time scale, such as deception. To identify and mitigate these risks, developers must identify future capabilities that models should not have, measure them, and build mitigations or alignment techniques. As a result, we will learn about alignment, security measures, and “warning shots.”

**Anthropic is building up our frontier threats red teaming research team.** This team will experiment with future capabilities to understand coming risks and build scalable evaluations and mitigations. You can learn more about this work and how to apply to join the team [here](https://jobs.lever.co/Anthropic/8f565d59-8831-443a-b72a-cb9ef8ae06b2). We are looking for particularly mission-driven technical researchers who can rapidly prototype across our infrastructure.

**We are also briefing government and labs on the details of what we have found.** We are open to sharing our present and future findings with appropriate audiences and are piloting a responsible disclosure process between stakeholders in the community to report risks and mitigations. We are particularly interested in supporting other groups – especially labs or new third party evaluation organizations – to do more of this work. If you are one of these stakeholders and are interested, please contact us.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
