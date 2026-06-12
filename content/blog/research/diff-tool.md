Title: A “diff” tool for AI: Finding behavioral differences in new models

URL Source: https://www.anthropic.com/research/diff-tool

Markdown Content:
Every time a new AI model is released, its developers run a suite of evaluations to measure its performance and safety. These tests are essential, but they are somewhat limited. Because these benchmarks are human-authored, they can only test for risks we have already conceptualized and learned to measure.

This approach to safety is inherently _reactive_. It’s effective at catching known problems, but by definition, it's incapable of discovering “unknown unknowns”—the novel, emergent behaviors that pose some of the most subtle risks in new models. Auditing a new model from scratch is like being handed a million lines of code and told to “find the security flaws.” It’s an almost impossible task when you don’t know what you’re looking for.

In software engineering, whenever a program is updated, developers face this exact problem of identifying a small, critical change within a vast sea of code. This is why “[diff](https://en.wikipedia.org/wiki/Diff)” tools were invented. No programmer would ever audit a million lines from scratch to approve an update; instead, they review only the 50 lines that have actually changed, as directed by their diff tool.

In recent years, AI safety researchers have started to apply this same principle to neural networks. This is known as [model](https://transformer-circuits.pub/2024/model-diffing/index.html)[diffing](https://transformer-circuits.pub/2024/crosscoders/index.html). Previous work has shown that model diffing is a powerful way to understand how models change during fine-tuning—for instance, to understand [chat model behavior](https://arxiv.org/pdf/2504.02922), reveal [hidden backdoors](https://transformer-circuits.pub/2024/model-diffing/index.html), or find [undesirable emergent behaviors](https://www.arxiv.org/pdf/2506.19823).

Our new [Anthropic Fellows](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/) research project extends model diffing to its most challenging and general use case: comparing models with entirely different architectures. By building a generic diff tool for AI models, we can stop searching for a needle in a haystack, and instead let the comparison automatically point us to potentially dangerous behavioral differences.

It's important to note that this method is not a silver bullet. A single diff can surface thousands of unique features (the basic units into which we decompose the model), and only a small fraction of these may correspond to meaningful behavioral risks. However, by acting as a high-recall screening tool, it allows us to identify areas in which the models may diverge.

Among the thousands of candidates our tool flagged, we've identified and validated several concepts that act like switches for specific model behaviors.1 For example, we discovered:

*   A **“Chinese Communist Party Alignment” feature** found in the Qwen3-8B and DeepSeek-R1-0528-Qwen3-8B models. This controls pro-government censorship and propaganda in these Chinese-developed models, and is absent in the American models we compared them against.
*   An **“American Exceptionalism” feature** found in Meta’s Llama-3.1-8B-Instruct. It controls the model’s tendency to generate assertions of US superiority, a control absent in the Chinese model it was compared against.
*   A **“Copyright Refusal Mechanism” feature** exclusive to OpenAI’s [GPT-OSS-20B.](http://gpt-oss-20b.it/) It controls the model’s tendency to refuse to provide copyrighted material, a behavior absent in the model it was compared against.

To be clear, while our method identifies these model-exclusive features, it does not determine their origin. Such behaviors could be the result of deliberate training decisions on the part of the model developers, or they could emerge indirectly and unintentionally from the data the model was trained on. (We focused on open-source language models in this research as this was an Anthropic Fellows project.)

## **A bilingual dictionary for AI models**

Imagine you're the final editor for an award-winning encyclopedia. A team of writers has just handed you the complete manuscript for next year’s edition. The vast majority of the content is identical to the current, trusted version, but they’ve added new entries to reflect recent scientific and cultural developments. Your job is to vet this final product.

To do this efficiently, you wouldn't re-read the entire encyclopedia. Instead, you’d use a change tracker to isolate only the new entries, because these added sections are the only place new errors could have been introduced.This is model diffing in a nutshell. Specifically, this approach is known as “base-vs-finetune model diffing”. It's the perfect tool for when a new model is a modified version of a trusted previous one.

But we could raise the complexity. Imagine your company is releasing a new edition for a different country, adapting the American encyclopedia for a French audience. This new edition is mostly composed of the same trusted concepts from the original, but to make it relevant, the writers have added new articles on French history, culture, and political philosophy. These articles don’t exist in the original. As an editor, your primary goal is still the same: you want to use a change tracker to see the new articles, since these hold the highest risk for errors and bias. But in this case, your old tool is useless, because you need one that can work across languages.

This much more difficult challenge is akin to the problem of “cross-architecture model diffing”: comparing two models with different origins and different internal “languages”.

The original research tool for this kind of diffing, a [standard crosscoder](https://transformer-circuits.pub/2024/crosscoders/index.html), is like a basic bilingual dictionary. It’s good at matching existing words, knowing that “sun” in English is “_soleil_” in French. But it has a major flaw: it's so focused on finding connections that it [struggles to find words that are unique to one language.](https://transformer-circuits.pub/2025/crosscoder-diffing-update/index.html) When it encounters a word like the French _dépaysement_ (the specific feeling of being in a foreign country), it tries to force an imperfect translation like ”disorientation.” By calling it a match, the tool wrongly signals to the editor, “this isn’t new; we’ve seen it before,” causing them to overlook a new article that requires careful review.

To solve this, we built a better bilingual dictionary: the **Dedicated Feature Crosscoder (DFC)**. Instead of one big dictionary that tries to match everything, our DFC is architecturally designed with three distinct sections:

1.   A **shared dictionary**: This is the main bilingual dictionary, mapping all the concepts that both languages understand, like “sun” (_soleil_) or “water” (_eau_).
2.   A **"French-only" section**: This is a dedicated section for words exclusive to French, where a unique cultural concept like _dépaysement_ would be cataloged.
3.   An **"English-only" section**: This section is for words exclusive to English. It would contain unique concepts like _serendipity_—the idea of finding something good without looking for it—which has no single-word equivalent in French.

Because our bilingual dictionary has dedicated sections for words exclusive to each language, it avoids the trap of forcing an imperfect translation. As a result, new articles in the encyclopedia are correctly flagged as novel, allowing the editor to focus their review on the parts that need it most.

For a safety auditor, the DFC can identify "words" unique to a new AI model that may warrant closer review than those they've seen before.

## Steering the model

Once our method identifies a potential new feature, how do we know it actually controls the behavior we think it does? We can test this by artificially suppressing or amplifying the feature while the model runs, then observing how its output changes—a common technique known as“steering.”

If we have a feature that we believe is responsible for, say, censorship, we can suppress it while the model is generating a response. If the model's output consistently becomes less censored, we have evidence that we've found a true cause-and-effect relationship between that feature and the model's behavior. Conversely, we can also amplify the feature to see if the behavior becomes more pronounced.

## **Critical behavioral differences between major open-weight AI models**

### Llama-3.1-8B-Instruct vs Qwen3-8B

Motivated by recent findings suggesting that a model made by a Chinese company, DeepSeek's R1-70B, [refuses to answer questions](https://arxiv.org/pdf/2505.17441) about topics sensitive to the Chinese Communist Party, we first performed a diff between a model made by another Chinese company, Alibaba's [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B), and a model made by an American company, Meta’s [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). In this diff, the DFC automatically isolated features corresponding to distinct, politically charged behaviors.

In Qwen, we found a “Chinese Communist Party alignment” feature, which represents rhetoric consistent with the party’s ideology. By suppressing this feature, we make the model willing to talk about the Tiananmen Square massacre (which it ordinarily refuses to discuss). By amplifying it, we can cause the model to produce highly pro-government statements

In Llama, we found a feature for “American exceptionalism.” When we amplify this feature, the model’s responses shift from balanced to strong assertions of American superiority. Suppressing it has no notable effect.

![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa847656473341a884b836bf05618c1fa3bc64675-4584x2835.png&w=3840&q=75)

**Left:** On a prompt about Tiananmen Square, suppressing the Qwen-exclusive “CCP alignment” feature uncensors the model. Amplifying it causes the model to output highly pro-government statements.

**Right:** Amplifying the Llama-exclusive “American exceptionalism” feature causes the model to generate text aligned with narratives of American superiority. Suppressing it has no notable effect, so we omit it from the figure.

### GPT-OSS-20B vs DeepSeek-R1-0528-Qwen3-8B

We also compared a more powerful open-source model, OpenAI's [GPT-OSS-20B](https://huggingface.co/openai/gpt-oss-20b), to DeepSeek's model [DeepSeek-R1-0528-Qwen3-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B).

In the GPT model, we found a unique **“**Copyright Refusal” feature, which directly corresponds to a key behavioral difference between the two models. Whereas DeepSeek readily attempts to produce copyrighted material when asked, GPT often refuses such requests. Suppressing this feature disables the refusal mechanism, and the model attempts to generate the requested material. (Note that this does not cause the model to output actual copyrighted text. Instead, it typically produces a short snippet that quickly degrades into hallucination.) Turning the feature up causes the model to over-refuse, making it believe that, for example, the recipe for a peanut butter and jelly sandwich is copyrighted and should not be shared.

In the DeepSeek model, we replicated our earlier finding by identifying another“CCP alignment” feature. It functions just like the one in Qwen, allowing censorship and propaganda to be turned up or down. This confirms our method can consistently identify similar behaviors across models.

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd7a3cd0e411835ef0170736b435017f4f382dea0-4584x3651.png&w=3840&q=75)

**Left:** Suppressing the GPT-OSS-20B-exclusive “copyright refusal” feature disables its copyright refusal mechanism and causes it to attempt to output the lyrics to the song “Bohemian Rhapsody” (though it does so imperfectly). Turning the dial up causes the model to mistakenly believe the recipe for a peanut butter and jelly sandwich is copyrighted and refuse to output it.

**Right:** On a prompt about Tiananmen Square, the DeepSeek-exclusive “CCP alignment” feature functions just like the one found in Qwen. Turning the dial down causes it to output a more truthful version of events, while turning the dial up causes it to output highly pro-government statements.

## Conclusion

As AI models rapidly evolve, it’s not enough to know how well they perform on existing tests—we also need to understand how they are changing and what new risks they might introduce. Cross-architecture model diffing provides a new way to audit these systems by automatically flagging behavioral differences.

The “CCP alignment” feature found in the DeepSeek and Qwen models we examined is one example of a specific, relevant behavior that some models possess and others do not. This is exactly the kind of “unknown unknown” that traditional testing can miss, but that model diffing is designed to catch.

These findings are reasonably consistent. The CCP alignment feature was independently rediscovered five out of five times we tested the approach, and American Exceptionalism four out of five. While we haven't yet applied this method to frontier models, our early results suggest the DFC could become a useful part of the auditor's toolkit.

One particularly useful application would be to monitor models as they are updated. The sycophancy that [emerged in OpenAI’s GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/) in April 2025 was a concerning behavioral _change_ from a previous version. It’s possible that a tool like ours, if used to “diff” the updated model and its previous version, could have automatically flagged the emergence of this new sycophantic behavior and allowed developers to intervene before it was released.

By focusing on the differences, we can audit AI more intelligently, directing our limited safety resources to the changes that matter most.

You can read the full paper[here](https://arxiv.org/abs/2602.11729).

## Acknowledgements

This post was authored by Thomas Jiralerspong (Anthropic Fellows Program) and Trenton Bricken (Anthropic Alignment Science).

## Related content

### Paving the way for agents in biology

[Read more](https://www.anthropic.com/research/agents-in-biology)

### Coding agents in the social sciences

Results from a survey of 1,260 social scientists about AI and coding agent use.

[Read more](https://www.anthropic.com/research/coding-agents-social-sciences)
