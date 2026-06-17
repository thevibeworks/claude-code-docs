Title: Advancing Claude for Financial Services

URL Source: https://www.anthropic.com/news/advancing-claude-for-financial-services

Markdown Content:
We're expanding [Claude for Financial Services](https://www.claude.com/solutions/financial-services) with an Excel add-in, additional connectors to real-time market data and portfolio analytics, and new pre-built Agent Skills, like building discounted cash flow models and initiating coverage reports.

These updates build on Sonnet 4.5’s state of the art performance on financial tasks, topping the [Finance Agent benchmark](https://www.vals.ai/benchmarks/finance_agent) from Vals AI at 55.3% accuracy. They augment Claude’s intelligence with solutions for time-consuming but critical financial work, built into preferred industry tools.

## Claude for Excel

We’re releasing [Claude for Excel](https://claude.com/claude-for-excel) in beta as a research preview. This allows users to work directly with Claude in a sidebar in Microsoft Excel, where Claude can read, analyze, modify, and create new Excel workbooks. Claude provides full transparency about the actions it takes: it tracks and explains its changes and lets users navigate directly to the cells it references in its explanations.

![Image 1: This picture depicts Claude for Excel.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F450687b3c7a1189eb1a650ade77588c56ca01461-2560x1440.png&w=3840&q=75)

Claude analyzes a spreadsheet containing Acme Grille, Inc.'s consolidated income statement from 2020-2024, providing real-time guidance on financial modeling. 

This means that Claude can discuss how a spreadsheet works, modify it while preserving its structure and formula dependencies, debug and fix cell formulas, populate templates with new data and assumptions, or build new spreadsheets entirely from scratch.

Claude for Excel adds to our existing integrations with Microsoft’s applications. In the Claude apps, Claude can also create and edit files, including Excel spreadsheets and PowerPoint slides, and connect to Microsoft 365 to search for files, emails, and Teams conversations. Select Claude models are also available in Microsoft Copilot Studio and Researcher agent.

Claude for Excel is now in beta as a research preview for Max, Enterprise, and Teams users. We’ll collect real-world feedback from 1,000 initial users before rolling the feature out more broadly. To join the waitlist, [click here](https://docs.google.com/forms/d/e/1FAIpQLSedsdrIw00BOGbiIhAQvTaC7mOQRW6jOofAt7PJ1lYAGzvfUw/viewform?usp=dialog).

## Connecting Claude to live information

[**Connectors**](https://claude.ai/redirect/website.v1.97cf2ef8-c6b9-4823-ba22-d6a5c3cfb1a8/settings/connectors) provide Claude with direct access to external tools and platforms. [In July](https://www.anthropic.com/news/claude-for-financial-services), we added connectors for S&P Capital IQ, Daloopa, Morningstar, and PitchBook. We’re adding new connectors that give Claude immediate access to more information in real time:

*   **Aiera** provides Claude with real-time earnings call transcripts and summaries of investor events, like shareholder meetings, presentations, and conferences;
*   Aiera’s connector also enables a data feed from **Third Bridge**, which gives Claude access to a library of insights interviews, company intelligence, and industry analysis from experts and former executives;
*   **Chronograph** gives private equity investors operational and financial information for portfolio monitoring and conducting due diligence, including performance metrics, valuations, and fund-level data;
*   **Egnyte** enables Claude to securely search permitted data for internal data rooms, investment documents, and approved financial models, while maintaining governed access controls;
*   **LSEG** connects Claude to live market data, including fixed income pricing, equities, foreign exchange rates, macroeconomic indicators, and analysts’ estimates of other important financial metrics;
*   **Moody’s** provides access to proprietary credit ratings, research, and company data – including ownership, financials and news on more than 600 million public and private companies – supporting work and research in compliance, credit analysis, and business development;
*   **MT Newswires** provides Claude with access to the latest global multi-asset class news on financial markets and economies.

For details on MCP connector setup and prompting guidance to maximize the benefit of each connector, see [our documentation here](https://support.claude.com/en/collections/13972013-claude-for-financial-services).

## New Agent Skills for finance tasks

Earlier this month, we introduced [Agent Skills](https://www.anthropic.com/news/skills). Skills are folders that include instructions, scripts, and resources that Claude can use to perform given tasks. Skills work across all Claude apps, including [Claude.ai](http://claude.ai/redirect/website.v1.97cf2ef8-c6b9-4823-ba22-d6a5c3cfb1a8), Claude Code, and our API. To make Claude better at financial services tasks, we’ve added 6 new skills:

*   **Comparable company analysis**, with valuation multiples and operating metrics, which can be easily refreshed with updated data;
*   **Discounted cash flow models**, including full free cash flow projections, WACC calculations, scenario toggles, and sensitivity tables;
*   **Due diligence data packs**, processing data room documents into Excel spreadsheets with financial information, customer lists, and contract terms;
*   **Company teasers and profiles**, condensed company overviews for pitch books and buyer lists;
*   **Earnings analyses**, which research quarterly transcripts and financials to extract important metrics, guidance changes, and management commentary;
*   **Initiating coverage reports** with industry analysis, company deep-dives, and valuation frameworks.

[Video 5](https://www.youtube.com/watch?v=NcBnxbEC0Ng)

As with Claude for Excel, these new skills are being rolled out in preview for Max, Enterprise, and Teams users. You can sign up on behalf of your team or organization [here](https://docs.google.com/forms/d/e/1FAIpQLSdXOB2bR7r_YhwENL1VplbgWvQ96YhInhHj5Fr9_V_MAOCiNQ/viewform).

## Claude’s impact in financial services

Claude is already widely used by leading banking, asset management, insurance, and financial technology companies. It supports front office tasks like client experience, middle office tasks in underwriting, risk and compliance, and back office tasks like code modernization and legacy processes. With ongoing updates to our models and products specific to financial services, we expect Claude to become even better in roles like these.

![Image 2: Citi logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Feeb5f52efd3e66059da5591e05d323013abef19f-300x195.png&w=256&q=75)

> Citi chose to leverage Claude as part of its AI powered Developer Platform because of its advanced planning and agentic coding capabilities, focus on safety and reliability, and compatibility with our workloads.

![Image 3: RBC Capital Markets logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F547b842bf1173a41ffa2e0ae77422eb17ef1d1ea-3840x2160.png&w=256&q=75)

> Working with Anthropic goes beyond deploying another AI tool—it's about partnering with a company that understands the complexity that financial services requires. Claude excels by seamlessly integrating multiple data sources and automating workflows that previously consumed significant time.

![Image 4: Brex logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9b387fa5e89cd8d5634180b9fa0322d6094fcbd7-4723x1250.png&w=256&q=75)

> What we've valued about Anthropic is not just their powerful models, but how they've positioned them for enterprise needs. When I talk with customers about AI, data privacy is always their first concern—it's the critical foundation we have to address before we can even begin discussing capabilities.

![Image 5: Block logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/b165f3c8782daa1ead93af072ead972e9aa9c5da-2044x447.svg)

> 75% of our engineers now save 8 to 10+ hours every week using our open source AI agent for creating SQL queries (codename goose) — accelerating velocity and cutting down on busywork. For the tasks we care about measuring specifically, the Claude family has performed the best.

![Image 6: Coinbase logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc4529fa0b7ca13f9216b9e9c64004cfe7f487caa-2560x458.png&w=256&q=75)

> Anthropic's multi-cloud solution stands out for its scale, performance and security, aligning with our operational needs and customer expectations. It exceeded our performance benchmarks and met all our security requirements, making it the ideal solution. We think Claude will help Coinbase build solutions for different customer segments and bring a billion customers to the crypto economy.

![Image 7: British Columbia Investment Management Corporation logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F38aea6f7503e7ac5d630b71e75b1ecda6640afbf-1200x565.png&w=256&q=75)

> As one of Canada’s largest institutional investors, BCI is driven to experiment, build, and innovate. Claude has accelerated our ability to get up-to-speed on investments and the underlying portfolio’s progress, making us more effective. As we push boundaries on what’s possible, we’re excited by the opportunities.

![Image 8: Visa logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb601fa689b4c5d1d7c1307be158232ed7238956b-3000x2000.png&w=256&q=75)

> We see AI agents as the next evolution of commerce—autonomous systems that can predict, suggest, and find the products and services consumers need. This is only possible with a secure foundation at the base built on consent, privacy, transparency, and security. Anthropic is a key partner of Visa to make this dream a reality and shares our values and principles around responsible data usage.

![Image 9: Jump Trading logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F355151efeae78d87d66071b46e188b01b5b4dc42-1200x997.png&w=256&q=75)

> Claude serves as a remarkable reasoning-powered companion. Its ability to shift smoothly between quick execution and deep analysis, with fine-grained control over both, is exactly what's been missing in AI systems. Anthropic is a go-to technology & partner for AI workloads that require reliable intelligence at scale.

![Image 10: Francisco Partners logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F637986e5b391013433fbbd3f5c9794200644d8c9-1200x1088.png&w=256&q=75)

> Through our training program with Anthropic, we've seen portfolio companies adopt Claude Code with remarkable results. Development teams are completing complex tasks in hours instead of days, and we're hearing from previously skeptical engineers that they can't imagine working without it.

![Image 11: Chronograph logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3045932147eb3dc40823f1c76a37b4bbe908e9ad-5000x793.png&w=256&q=75)

> Chronograph’s connection to Claude will fundamentally change what is possible for our clients – much like how Claude for Enterprise has transformed our internal operations. The partnership between Chronograph and Claude enables our clients to uncover new insights, save significant time, and achieve superior returns using their private capital portfolio data within Claude’s powerful toolset.

![Image 12: Moody's logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd6f232859f8c2f45a96d4e1bae6ed566ea3750df-2560x548.png&w=256&q=75)

> With our GenAI-ready data offerings, we continue to support our customers in their AI evolution—enriching our data via a semantic layer and delivering it through Model Context Protocol (MCP) servers and Smart APIs. Our partnership with Anthropic makes Moody’s vast data estate accessible directly where our customers are innovating.

![Image 13: London Stock Exchange Group (LSEG) logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc44267e39c06075450ac20b9d44793277387c752-3524x1526.png&w=256&q=75)

> LSEG has a long-established reputation for our open, partnership approach and meeting our customers wherever their workflows are taking place. Secure, enterprise grade AI applications, such as Claude, are expanding the opportunities for LSEG to build deep partnerships with customers.

01 /

12

Below, Alexander Bricken, Applied AI Lead for Financial Services, and Nicholas Lin, Head of Product for Financial Services, discuss Anthropic’s research and product strategy within financial services, as well as customer examples.

[Video 6](https://www.youtube.com/watch?v=a8PmR-fNQ_0)

## Getting started

To learn more about using Claude for Financial Services, [see here](https://claude.com/solutions/financial-services) or [contact](https://claude.com/contact-sales/financial-services) our sales team. And to see the new features in action and hear directly from financial services leaders, you can also [register here](http://website.anthropic.com/webinars/%20claude-for-financial-services) for our launch webinar.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
