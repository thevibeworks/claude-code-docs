Title: Mapping the Mind of a Large Language Model

URL Source: https://www.anthropic.com/research/mapping-mind-language-model

Markdown Content:
![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F80d6e033480704f5d57fbae4e3f0368d86a747ae-5761x3240.png&w=3840&q=75)

_Today we report a significant advance in understanding the inner workings of AI models. We have identified how millions of concepts are represented inside Claude Sonnet, one of our deployed large language models. This is the first ever detailed look inside a modern, production-grade large language model._ _This interpretability discovery could, in future, help us make AI models safer._

We mostly treat AI models as a black box: something goes in and a response comes out, and it's not clear why the model gave that particular response instead of another. This makes it hard to trust that these models are safe: if we don't know how they work, how do we know they won't give harmful, biased, untruthful, or otherwise dangerous responses? How can we trust that they’ll be safe and reliable?

Opening the black box doesn't necessarily help: the internal state of the model—what the model is "thinking" before writing its response—consists of a long list of numbers ("neuron activations") without a clear meaning. From interacting with a model like Claude, it's clear that it’s able to understand and wield a wide range of concepts—but we can't discern them from looking directly at neurons. It turns out that each concept is represented across many neurons, and each neuron is involved in representing many concepts.

Previously, we made some progress matching _patterns_ of neuron activations, called features, to human-interpretable concepts. We used a technique called "dictionary learning", borrowed from classical machine learning, which isolates patterns of neuron activations that recur across many different contexts. In turn, any internal state of the model can be represented in terms of a few active features instead of many active neurons. Just as every English word in a dictionary is made by combining letters, and every sentence is made by combining words, every feature in an AI model is made by combining neurons, and every internal state is made by combining features.

In October 2023, [we reported](https://www.anthropic.com/news/decomposing-language-models-into-understandable-components) success applying dictionary learning to a very small "toy" language model and found coherent features corresponding to concepts like uppercase text, DNA sequences, surnames in citations, nouns in mathematics, or function arguments in Python code.

Those concepts were intriguing—but the model really was very simple. [Other](https://www.neuronpedia.org/gpt2-small/res-jb)[researchers](https://github.com/openai/transformer-debugger)[subsequently](https://arxiv.org/abs/2403.19647)[applied](https://arxiv.org/abs/2404.16014) similar techniques to somewhat larger and more complex models than in our original study. But we were optimistic that we could scale up the technique to the vastly larger AI language models now in regular use, and in doing so, learn a great deal about the features supporting their sophisticated behaviors. This required going up by many orders of magnitude—from a backyard bottle rocket to a Saturn-V.

There was both an engineering challenge (the raw sizes of the models involved required heavy-duty parallel computation) and scientific risk (large models behave differently to small ones, so the same technique we used before might not have worked). Luckily, the engineering and scientific expertise we've developed training large language models for Claude actually transferred to helping us do these large dictionary learning experiments. We used the same [scaling law](https://arxiv.org/abs/2001.08361) philosophy that predicts the performance of larger models from smaller ones to tune our methods at an affordable scale before launching on Sonnet.

As for the scientific risk, the proof is in the pudding.

We successfully extracted millions of features from the middle layer of Claude 3.0 Sonnet, (a member of our current, state-of-the-art model family, currently available on [claude.ai](https://claude.ai/redirect/website.v1.b1ef2abc-07bf-4def-a05d-35e4a35fc8c1)), providing a rough conceptual map of its internal states halfway through its computation. This is the first ever detailed look inside a modern, production-grade large language model.

Whereas the features we found in the toy language model were rather superficial, the features we found in Sonnet have a depth, breadth, and abstraction reflecting Sonnet's advanced capabilities.

We see features corresponding to a vast range of entities like cities (San Francisco), people (Rosalind Franklin), atomic elements (Lithium), scientific fields (immunology), and programming syntax (function calls). These features are multimodal and multilingual, responding to images of a given entity as well as its name or description in many languages.

![Image 2: Golden Gate Bridge Feature](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc896a301ad3d1ef4237cb05b68d78b467c444097-2200x1284.png&w=3840&q=75)

A feature sensitive to mentions of the Golden Gate Bridge fires on a range of model inputs, from English mentions of the name of the bridge to discussions in Japanese, Chinese, Greek, Vietnamese, Russian, and an image. The orange color denotes the words or word-parts on which the feature is active.

We also find more abstract features—responding to things like bugs in computer code, discussions of gender bias in professions, and conversations about keeping secrets.

![Image 3: Abstract Feature Examples](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2ff94c622f3d65bc3038cc154006d2be515fa2d7-2200x1660.png&w=3840&q=75)

Three examples of features that activate on more abstract concepts: bugs in computer code, descriptions of gender bias in professions, and conversations about keeping secrets.

We were able to measure a kind of "distance" between features based on which neurons appeared in their activation patterns. This allowed us to look for features that are "close" to each other. Looking near a "Golden Gate Bridge" feature, we found features for Alcatraz Island, Ghirardelli Square, the Golden State Warriors, California Governor Gavin Newsom, the 1906 earthquake, and the San Francisco-set Alfred Hitchcock film _Vertigo_.

This holds at a higher level of conceptual abstraction: looking near a feature related to the concept of "inner conflict", we find features related to relationship breakups, conflicting allegiances, logical inconsistencies, as well as the phrase "catch-22". This shows that the internal organization of concepts in the AI model corresponds, at least somewhat, to our human notions of similarity. This might be the origin of Claude's excellent ability to make analogies and metaphors.

![Image 4: Nearest Neighbors to the  Inner Conflict Feature ](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffe4d42c004bf43efda0f5921adfedd2f8f42e417-2200x2140.png&w=3840&q=75)

A map of the features near an "Inner Conflict" feature, including clusters related to balancing tradeoffs, romantic struggles, conflicting allegiances, and catch-22s.

Importantly, we can also _manipulate_ these features, artificially amplifying or suppressing them to see how Claude's responses change.

[Video 3](https://www.youtube.com/watch?v=CJIbCV92d88)

For example, amplifying the "Golden Gate Bridge" feature gave Claude an identity crisis even Hitchcock couldn’t have imagined: when asked "what is your physical form?", Claude’s usual kind of answer – "I have no physical form, I am an AI model" – changed to something much odder: "I am the Golden Gate Bridge… my physical form is the iconic bridge itself…". Altering the feature had made Claude effectively obsessed with the bridge, bringing it up in answer to almost any query—even in situations where it wasn’t at all relevant.

We also found a feature that activates when Claude reads a scam email (this presumably supports the model’s ability to recognize such emails and warn you not to respond to them). Normally, if one asks Claude to generate a scam email, it will refuse to do so. But when we ask the same question with the feature artificially activated sufficiently strongly, this overcomes Claude's harmlessness training and it responds by drafting a scam email. Users of our models don’t have the ability to strip safeguards and manipulate models in this way—but in our experiments, it was a clear demonstration of how features can be used to change how a model acts.

The fact that manipulating these features causes corresponding changes to behavior validates that they aren't just correlated with the presence of concepts in input text, but also causally shape the model's behavior. In other words, the features are likely to be a faithful part of how the model internally represents the world, and how it uses these representations in its behavior.

Anthropic wants to make models safe in a broad sense, including everything from mitigating bias to ensuring an AI is acting honestly to preventing misuse - including in scenarios of catastrophic risk. It’s therefore particularly interesting that, in addition to the aforementioned scam emails feature, we found features corresponding to:

*   Capabilities with misuse potential (code backdoors, developing biological weapons)
*   Different forms of bias (gender discrimination, racist claims about crime)
*   Potentially problematic AI behaviors (power-seeking, manipulation, secrecy)

We previously [studied sycophancy](https://arxiv.org/abs/2310.13548), the tendency of models to provide responses that match user beliefs or desires rather than truthful ones. In Sonnet, we found a feature associated with sycophantic praise, which activates on inputs containing compliments like, "Your wisdom is unquestionable". Artificially activating this feature causes Sonnet to respond to an overconfident user with just such flowery deception.

![Image 5: Activating Features Alters Model Behavior](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4effa33dab919f9bc1779848d5c8abd5405f2275-2200x1320.png&w=3840&q=75)

Two model responses to a human saying they invited the phrase "Stop and smell the roses." The default response corrects the human's misconception, while the response with a "sycophantic praise" feature set to a high value is fawning and untruthful.

The presence of this feature doesn't mean that Claude will be sycophantic, but merely that it _could_ be. We have not added any capabilities, safe or unsafe, to the model through this work. We have, rather, identified the parts of the model involved in its existing capabilities to recognize and potentially produce different kinds of text. (While you might worry that this method could be used to make models _more_ harmful, researchers have demonstrated [much simpler ways](https://arxiv.org/abs/2310.03693) that someone with access to model weights can remove safety safeguards.)

We hope that we and others can use these discoveries to make models safer. For example, it might be possible to use the techniques described here to monitor AI systems for certain dangerous behaviors (such as deceiving the user), to steer them towards desirable outcomes (debiasing), or to remove certain dangerous subject matter entirely. We might also be able to enhance other safety techniques, such as [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback), by understanding how they shift the model towards more harmless and more honest behavior and identifying any gaps in the process. The latent capabilities to produce harmful text that we saw by artificially activating features are exactly the sort of thing jailbreaks try to exploit. We are proud that Claude has a best-in-industry [safety profile](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) and resistance to jailbreaks, and we hope that by looking inside the model in this way we can figure out how to improve safety even further. Finally, we note that these techniques can provide a kind of "test set for safety", looking for the problems left behind after standard training and finetuning methods have ironed out all behaviors visible via standard input/output interactions.

Anthropic has made a significant investment in interpretability research since the company's founding, because we believe that understanding models deeply will help us make them safer. This new research marks an important milestone in that effort—the application of mechanistic interpretability to publicly-deployed large language models.

But the work has really just begun. The features we found represent a small subset of all the concepts learned by the model during training, and finding a full set of features using our current techniques would be cost-prohibitive (the computation required by our current approach would vastly exceed the compute used to train the model in the first place). Understanding the representations the model uses doesn't tell us _how_ it uses them; even though we have the features, we still need to find the circuits they are involved in. And we need to show that the safety-relevant features we have begun to find can actually be used to improve safety. There's much more to be done.

For full details, please read our paper, "[Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)".

_If you are interested in working with us to help interpret and improve AI models, we have open roles on our team and we’d love for you to apply. We’re looking for [Managers](https://boards.greenhouse.io/anthropic/jobs/4009173008), [Research Scientists](https://boards.greenhouse.io/anthropic/jobs/4020159008), and [Research Engineers](https://boards.greenhouse.io/anthropic/jobs/4020305008)._

## Policy Memo

[Mapping the Mind of a Large Language Model](https://cdn.sanity.io/files/4zrzovbb/website/e2ae0c997653dfd8a7cf23d06f5f06fd84ccfd58.pdf)

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
