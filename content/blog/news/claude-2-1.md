Title: Introducing Claude 2.1

URL Source: https://www.anthropic.com/news/claude-2-1

Markdown Content:
![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa03806b9e2428cb5ac0575110aa0918bfcf417c2-2880x1620.png&w=3840&q=75)

Our latest model, Claude 2.1, is now available over API in our Console and is powering our [claude.ai](https://claude.ai/redirect/website.v1.1c483dd6-555e-4007-98c6-23af50a2b61d) chat experience. Claude 2.1 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and our new beta feature: tool use. We are also updating our [pricing](https://www-cdn.anthropic.com/1b1ea2c43d8dd058f6a331a8097e05ea40d626c6/model_pricing_nov2023.pdf) to improve cost efficiency for our customers across models.

**200K Context Window**

Since our launch earlier this year, Claude has been used by millions of people for a wide range of applications—from translating academic papers to drafting business plans and analyzing complex contracts. In discussions with our users, they’ve asked for larger context windows and more accurate outputs when working with long documents.

In response, we’re doubling the amount of information you can relay to Claude with a limit of 200,000 tokens, translating to roughly 150,000 words, or over 500 pages of material. Our users can now upload technical documentation like entire codebases, financial statements like S-1s, or even long literary works like The Iliad or The Odyssey. By being able to talk to large bodies of content or data, Claude can summarize, perform Q&A, forecast trends, compare and contrast multiple documents, and much more.

Processing a 200K length message is a complex feat and an industry first. While we’re excited to get this powerful new capability into the hands of our users, tasks that would typically require hours of human effort to complete may take Claude a few minutes. We expect the latency to decrease substantially as the technology progresses.

**2x Decrease in Hallucination Rates**

Claude 2.1 has also made significant gains in honesty, with a 2x decrease in false statements compared to our previous Claude 2.0 model. This enables enterprises to build high-performing AI applications that solve concrete business problems and deploy AI across their operations with greater trust and reliability.

We tested Claude 2.1’s honesty by curating a large set of complex, factual questions that probe known weaknesses in current models. Using a rubric that distinguishes incorrect claims (“The fifth most populous city in Bolivia is Montero”) from admissions of uncertainty (“I’m not sure what the fifth most populous city in Bolivia is”), Claude 2.1 was significantly more likely to demur rather than provide incorrect information.

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0fb7f10eb5e10278d38be91f84894425f864f869-1712x1442.png&w=3840&q=75)

Claude 2.1 has also made meaningful improvements in comprehension and summarization, particularly for long, complex documents that demand a high degree of accuracy, such as legal documents, financial reports and technical specifications. In our evaluations, Claude 2.1 demonstrated a 30% reduction in incorrect answers and a 3-4x lower rate of mistakenly concluding a document supports a particular claim.

![Image 3](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9c0b9f8de8432b74bb0a9d4b3e2eac9764c619f3-1597x1203.png&w=3840&q=75)

While we are encouraged by these accuracy improvements, enhancing the precision and dependability of outputs for our users remains a top priority for our product and research teams.

**API Tool Use**

By popular demand, we’ve also added tool use, a new beta feature that allows Claude to integrate with users' existing processes, products, and APIs. This expanded interoperability aims to make Claude more useful across our users’ day-to-day operations.

Claude can now orchestrate across developer-defined functions or APIs, search over web sources, and retrieve information from private knowledge bases. Users can define a set of tools for Claude to use and specify a request. The model will then decide which tool is required to achieve the task and execute an action on their behalf, such as:

*   Using a calculator for complex numerical reasoning
*   Translating natural language requests into structured API calls
*   Answering questions by searching databases or using a web search API
*   Taking simple actions in software via private APIs
*   Connecting to product datasets to make recommendations and help users complete purchases

Tool use is currently in early development—we are building developer features and prompting guidelines for easier integration into your applications. We encourage users to share feedback on tool use to help shape and improve the product.

**Developer Experience**

We’ve been working to simplify our developer Console experience for Claude API users while making it easier to test new prompts for faster learning. Our new Workbench product enables developers to iterate on prompts in a playground-style experience and access new model settings to optimize Claude’s behavior. They can create multiple prompts and navigate between them for different projects, and revisions are saved as they go to retain historical context. Developers can also generate code snippets to use their prompts directly in one of our SDKs.

We’re also introducing [system prompts](https://docs.anthropic.com/claude/docs/how-to-use-system-prompts), which allow users to provide custom instructions to Claude in order to improve performance. System prompts set helpful context that enhances Claude’s ability to take on specified personalities and roles or structure responses in a more customizable, consistent way aligned with user needs.

[Claude 2.1](https://www-cdn.anthropic.com/5c49cc247484cecf107c699baf29250302e5da70/ModelCardClaudev2_with_appendix_v1.pdf)is available now in our API, and is also powering our chat interface at [claude.ai](https://claude.ai/redirect/website.v1.1c483dd6-555e-4007-98c6-23af50a2b61d) for both the free and Pro tiers. Usage of the 200K token context window is reserved for Claude Pro users, who can now upload larger files than ever before. We can't wait to see the use cases these new features inspire as we work to build the safest and most technically sophisticated AI systems in the industry.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
