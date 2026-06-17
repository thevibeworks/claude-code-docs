Title: Introducing the next generation of Claude

URL Source: https://www.anthropic.com/news/claude-3-family

Markdown Content:
![Image 1: Claude 3 ](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4e78f69ef8d4186fb5691714abe36224483d91b0-2880x1620.png&w=3840&q=75)

Today, we're announcing the Claude 3 model family, which sets new industry benchmarks across a wide range of cognitive tasks. The family includes three state-of-the-art models in ascending order of capability: Claude 3 Haiku, Claude 3 Sonnet, and Claude 3 Opus. Each successive model offers increasingly powerful performance, allowing users to select the optimal balance of intelligence, speed, and [cost](https://www.anthropic.com/api#pricing) for their specific application.

Opus and Sonnet are now available to use in claude.ai and the Claude API which is now generally available in [159 countries](https://www.anthropic.com/supported-countries). Haiku will be available soon.

### Claude 3 model family

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5d20371eeb8d045465bb22cacfd269b5958b004d-2200x1174.png&w=3840&q=75)

### A new standard for intelligence

Opus, our most intelligent model, outperforms its peers on most of the common evaluation benchmarks for AI systems, including undergraduate level expert knowledge (MMLU), graduate level expert reasoning (GPQA), basic mathematics (GSM8K), and more. It exhibits near-human levels of comprehension and fluency on complex tasks, leading the frontier of general intelligence.

All [Claude 3](https://www.anthropic.com/claude-3-model-card) models show increased capabilities in analysis and forecasting, nuanced content creation, code generation, and conversing in non-English languages like Spanish, Japanese, and French.

Below is a comparison of the Claude 3 models to those of our peers on multiple benchmarks [1] of capability:

![Image 3](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9ad98d612086fe52b3042f9183414669b4d2a3da-2200x1954.png&w=3840&q=75)

### Near-instant results

The Claude 3 models can power live customer chats, auto-completions, and data extraction tasks where responses must be immediate and in real-time.

Haiku is the fastest and most cost-effective model on the market for its intelligence category. It can read an information and data dense research paper on arXiv (~10k tokens) with charts and graphs in less than three seconds. Following launch, we expect to improve performance even further.

For the vast majority of workloads, Sonnet is 2x faster than Claude 2 and Claude 2.1 with higher levels of intelligence. It excels at tasks demanding rapid responses, like knowledge retrieval or sales automation. Opus delivers similar speeds to Claude 2 and 2.1, but with much higher levels of intelligence.

### Strong vision capabilities

The Claude 3 models have sophisticated vision capabilities on par with other leading models. They can process a wide range of visual formats, including photos, charts, graphs and technical diagrams. We’re particularly excited to provide this new modality to our enterprise customers, some of whom have up to 50% of their knowledge bases encoded in various formats such as PDFs, flowcharts, or presentation slides.

![Image 4](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6b66d86ff0c180e95bc6ad2e6e4a1843aa74c80f-2200x960.png&w=3840&q=75)

### Fewer refusals

Previous Claude models often made unnecessary refusals that suggested a lack of contextual understanding. We’ve made meaningful progress in this area: Opus, Sonnet, and Haiku are significantly less likely to refuse to answer prompts that border on the system’s guardrails than previous generations of models. As shown below, the Claude 3 models show a more nuanced understanding of requests, recognize real harm, and refuse to answer harmless prompts much less often.

![Image 5](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd1fbcf3d58ebc2dcd2e98aac995d70bf50cb2e9c-2188x918.png&w=3840&q=75)

### Improved accuracy

Businesses of all sizes rely on our models to serve their customers, making it imperative for our model outputs to maintain high accuracy at scale. To assess this, we use a large set of complex, factual questions that target known weaknesses in current models. We categorize the responses into correct answers, incorrect answers (or hallucinations), and admissions of uncertainty, where the model says it doesn’t know the answer instead of providing incorrect information. Compared to Claude 2.1, Opus demonstrates a twofold improvement in accuracy (or correct answers) on these challenging open-ended questions while also exhibiting reduced levels of incorrect answers.

In addition to producing more trustworthy responses, we will soon enable citations in our Claude 3 models so they can point to precise sentences in reference material to verify their answers.

![Image 6](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7cb598c6a9fa58c12b77f67ee2067feaac4a2de0-2200x896.png&w=3840&q=75)

### Long context and near-perfect recall

The Claude 3 family of models will initially offer a 200K context window upon launch. However, all three models are capable of accepting inputs exceeding 1 million tokens and we may make this available to select customers who need enhanced processing power.

To process long context prompts effectively, models require robust recall capabilities. The 'Needle In A Haystack' (NIAH) evaluation measures a model's ability to accurately recall information from a vast corpus of data. We enhanced the robustness of this benchmark by using one of 30 random needle/question pairs per prompt and testing on a diverse crowdsourced corpus of documents. Claude 3 Opus not only achieved near-perfect recall, surpassing 99% accuracy, but in some cases, it even identified the limitations of the evaluation itself by recognizing that the "needle" sentence appeared to be artificially inserted into the original text by a human.

![Image 7](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd2aa12b60e9c57e7057924bd8878d754c7b3d8e7-2200x1088.png&w=3840&q=75)

### Responsible design

We’ve developed the Claude 3 family of models to be as trustworthy as they are capable. We have several dedicated teams that track and mitigate a broad spectrum of risks, ranging from misinformation and CSAM to biological misuse, election interference, and autonomous replication skills. We continue to develop methods such as [Constitutional AI](https://www.anthropic.com/news/constitutional-ai-harmlessness-from-ai-feedback) that improve the safety and transparency of our models, and have tuned our models to mitigate against privacy issues that could be raised by new modalities.

Addressing biases in increasingly sophisticated models is an ongoing effort and we’ve made strides with this new release. As shown in the model card, Claude 3 shows less biases than our previous models according to the [Bias Benchmark for Question Answering (BBQ)](https://aclanthology.org/2022.findings-acl.165/). We remain committed to advancing techniques that reduce biases and promote greater neutrality in our models, ensuring they are not skewed towards any particular partisan stance.

While the Claude 3 model family has advanced on key measures of biological knowledge, cyber-related knowledge, and autonomy compared to previous models, it remains at AI Safety Level 2 (ASL-2) per our [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy). Our [red teaming](https://www.anthropic.com/news/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) evaluations (performed in line with our [White House commitments](https://www.whitehouse.gov/briefing-room/statements-releases/2023/07/21/fact-sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/) and the [2023 US Executive Order](https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/)) have concluded that the models present negligible potential for catastrophic risk at this time. We will continue to carefully monitor future models to assess their proximity to the ASL-3 threshold. Further safety details are available in the [Claude 3 model card](https://www.anthropic.com/claude-3-model-card).

### Easier to use

The Claude 3 models are better at following complex, multi-step instructions. They are particularly adept at adhering to brand voice and response guidelines, and developing customer-facing experiences our users can trust. In addition, the Claude 3 models are better at producing popular structured output in formats like JSON—making it simpler to instruct Claude for use cases like natural language classification and sentiment analysis.

### Model details

**Claude 3 Opus**is our most intelligent model, with best-in-market performance on highly complex tasks. It can navigate open-ended prompts and sight-unseen scenarios with remarkable fluency and human-like understanding. Opus shows us the outer limits of what’s possible with generative AI.

**Cost**_[Input $/million tokens | Output $/million tokens]_$15 | $75
**Context window**200K*
**Potential uses***   Task automation: plan and execute complex actions across APIs and databases, interactive coding
*   R&D: research review, brainstorming and hypothesis generation, drug discovery
*   Strategy: advanced analysis of charts & graphs, financials and market trends, forecasting
**Differentiator**Higher intelligence than any other model available.

data

_*1M tokens available for specific use cases, please inquire._

![Image 8](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F08376f135c37fe029e2aea16fa55c4c83ec77b6b-1148x56.png&w=3840&q=75)

**Claude 3 Sonnet** strikes the ideal balance between intelligence and speed—particularly for enterprise workloads. It delivers strong performance at a lower cost compared to its peers, and is engineered for high endurance in large-scale AI deployments.

**Cost**_[Input $/million tokens | Output $/million tokens]_$3 | $15
**Context window**200K
**Potential uses***   Data processing: RAG or search & retrieval over vast amounts of knowledge
*   Sales: product recommendations, forecasting, targeted marketing
*   Time-saving tasks: code generation, quality control, parse text from images
**Differentiator**More affordable than other models with similar intelligence; better for scale.

data

**Claude 3 Haiku** is our fastest, most compact model for near-instant responsiveness. It answers simple queries and requests with unmatched speed. Users will be able to build seamless AI experiences that mimic human interactions.

**Cost**_[Input $/million tokens | Output $/million tokens]_$0.25 | $1.25
**Context window**200K
**Potential uses***   Customer interactions: quick and accurate support in live interactions, translations
*   Content moderation: catch risky behavior or customer requests
*   Cost-saving tasks: optimized logistics, inventory management, extract knowledge from unstructured data
**Differentiator**Smarter, faster, and more affordable than other models in its intelligence category.

data

### Model availability

Opus and Sonnet are available to use today in our API, which is now generally available, enabling developers to sign up and start using these models immediately. Haiku will be available soon. Sonnet is powering the free experience on claude.ai, with Opus available for Claude Pro subscribers.

Sonnet is also available today through Amazon Bedrock and in private preview on Google Cloud’s Vertex AI Model Garden—with Opus and Haiku coming soon to both.

### Smarter, faster, safer

We do not believe that model intelligence is anywhere near its limits, and we plan to release frequent updates to the Claude 3 model family over the next few months. We're also excited to release a series of features to enhance our models' capabilities, particularly for enterprise use cases and large-scale deployments. These new features will include Tool Use (aka function calling), interactive coding (aka REPL), and more advanced agentic capabilities.

As we push the boundaries of AI capabilities, we’re equally committed to ensuring that our safety guardrails keep apace with these leaps in performance. Our hypothesis is that being at the frontier of AI development is the most effective way to steer its trajectory towards positive societal outcomes.

We’re excited to see what you create with Claude 3 and hope you will give us feedback to make Claude an even more useful assistant and creative companion. To start building with Claude, visit [anthropic.com/claude](https://www.anthropic.com/claude).

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
