Title: Introducing Claude 3.5 Sonnet

URL Source: https://www.anthropic.com/news/claude-3-5-sonnet

Markdown Content:
![Image 1: Claude head illustration](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4e78f69ef8d4186fb5691714abe36224483d91b0-2880x1620.png&w=3840&q=75)

*   Update

Consumer Terms and Privacy Policy

Aug 28, 2025 

Today, we’re launching Claude 3.5 Sonnet—our first release in the forthcoming Claude 3.5 model family. Claude 3.5 Sonnet raises the industry bar for intelligence, outperforming competitor models and Claude 3 Opus on a wide range of evaluations, with the speed and cost of our mid-tier model, Claude 3 Sonnet.

Claude 3.5 Sonnet is now available for free on Claude.ai and the Claude iOS app, while Claude Pro and Team plan subscribers can access it with significantly higher rate limits. It is also available via the Anthropic [API](https://docs.anthropic.com/en/home), [Amazon Bedrock](https://aws.amazon.com/blogs/aws/anthropics-claude-3-5-sonnet-model-now-available-in-amazon-bedrock-the-most-intelligent-claude-model-yet/), and [Google Cloud’s Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/announcing-anthropics-claude-3-5-sonnet-on-vertex-ai-providing-more-choice-for-enterprises). The model costs $3 per million input tokens and $15 per million output tokens, with a 200K token context window.

![Image 2: Claude model family](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1f044104447e9db6b22db3a06e45d114f50f274e-2200x1174.png&w=3840&q=75)

## Frontier intelligence at 2x the speed

Claude 3.5 Sonnet sets new industry benchmarks for graduate-level reasoning (GPQA), undergraduate-level knowledge (MMLU), and coding proficiency (HumanEval). It shows marked improvement in grasping nuance, humor, and complex instructions, and is exceptional at writing high-quality content with a natural, relatable tone.

Claude 3.5 Sonnet operates at twice the speed of Claude 3 Opus. This performance boost, combined with cost-effective pricing, makes Claude 3.5 Sonnet ideal for complex tasks such as context-sensitive customer support and orchestrating multi-step workflows.

In an [internal agentic coding evaluation](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf), Claude 3.5 Sonnet solved 64% of problems, outperforming Claude 3 Opus which solved 38%. Our evaluation tests the model’s ability to fix a bug or add functionality to an open source codebase, given a natural language description of the desired improvement. When instructed and [provided with the relevant tools](https://www.anthropic.com/news/tool-use-ga), Claude 3.5 Sonnet can independently write, edit, and execute code with sophisticated reasoning and troubleshooting capabilities. It handles code translations with ease, making it particularly effective for updating legacy applications and migrating codebases.

![Image 3: Claude 3.5 Sonnet benchmarks](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcf2c754458e9102b7334731fb18a965bfeb7ad08-2200x1894.png&w=3840&q=75)

## State-of-the-art vision

Claude 3.5 Sonnet is our strongest vision model yet, surpassing Claude 3 Opus on standard vision benchmarks. These step-change improvements are most noticeable for tasks that require visual reasoning, like interpreting charts and graphs. Claude 3.5 Sonnet can also accurately transcribe text from imperfect images—a core capability for retail, logistics, and financial services, where AI may glean more insights from an image, graphic or illustration than from text alone.

[Video 5](https://www.youtube.com/watch?v=dhxrHvgXpSM)

![Image 4: Claude 3.5 Sonnet vision evals](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcaff3d60763b27b59fe33e4ae984530f0dba4ddb-2200x1110.png&w=3840&q=75)

## Artifacts—a new way to use Claude

Today, we’re also introducing Artifacts on Claude.ai, a new feature that expands how users can interact with Claude. When a user asks Claude to generate content like code snippets, text documents, or website designs, these Artifacts appear in a dedicated window alongside their conversation. This creates a dynamic workspace where they can see, edit, and build upon Claude’s creations in real-time, seamlessly integrating AI-generated content into their projects and workflows.

This preview feature marks Claude’s evolution from a conversational AI to a collaborative work environment. It’s just the beginning of a broader vision for Claude.ai, which will soon expand to support team collaboration. In the near future, teams—and eventually entire organizations—will be able to securely centralize their knowledge, documents, and ongoing work in one shared space, with Claude serving as an on-demand teammate.

[Video 6](https://www.youtube.com/watch?v=rHqk0ZGb6qo)

## Commitment to safety and privacy

Our models are subjected to rigorous testing and have been trained to reduce misuse. Despite Claude 3.5 Sonnet’s leap in intelligence, our red teaming assessments have concluded that Claude 3.5 Sonnet remains at [ASL-2](https://www.anthropic.com/news/anthropics-responsible-scaling-policy). More details can be found in the [model card addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf).

As part of our commitment to safety and transparency, we’ve engaged with external experts to test and refine the safety mechanisms within this latest model. We recently provided Claude 3.5 Sonnet to the UK’s Artificial Intelligence Safety Institute (UK AISI) for pre-deployment safety evaluation. The UK AISI completed tests of 3.5 Sonnet and shared their results with the US AI Safety Institute (US AISI) as part of a Memorandum of Understanding, made possible by the partnership between the US and UK AISIs [announced earlier this year](https://www.commerce.gov/news/press-releases/2024/04/us-and-uk-announce-partnership-science-ai-safety).

We have integrated policy feedback from outside subject matter experts to ensure that our evaluations are robust and take into account new trends in abuse. This engagement has helped our teams scale up our ability to evaluate 3.5 Sonnet against various types of misuse. For example, we used feedback from child safety experts at [Thorn](https://www.thorn.org/) to update our classifiers and fine-tune our models.

One of the core constitutional principles that guides our AI model development is privacy. We do not train our generative models on user-submitted data unless a user gives us explicit permission to do so.

## Coming soon

Our aim is to substantially improve the tradeoff curve between intelligence, speed, and cost every few months. To complete the Claude 3.5 model family, we’ll be releasing Claude 3.5 Haiku and Claude 3.5 Opus later this year.

In addition to working on our next-generation model family, we are developing new modalities and features to support more use cases for businesses, including integrations with enterprise applications. Our team is also exploring features like Memory, which will enable Claude to remember a user’s preferences and interaction history as specified, making their experience even more personalized and efficient.

We’re constantly working to improve Claude and love hearing from our users. You can submit feedback on Claude 3.5 Sonnet directly in-product to inform our development roadmap and help our teams to improve your experience. As always, we look forward to seeing what you build, create, and discover with Claude.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
