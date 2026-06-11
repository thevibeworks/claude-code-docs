Title: Agents for financial services

URL Source: https://www.anthropic.com/news/finance-agents

Markdown Content:
We’re releasing ten ready-to-run agent templates for the most time-consuming work in financial services: building pitchbooks, screening KYC files, and closing the books at month-end. Each one ships as a [plugin](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork) in Claude Cowork and Claude Code, and as a cookbook for [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), so a team can put Claude on real financial work in days rather than months.

Claude also now works across Microsoft Excel, PowerPoint, Word, and Outlook (coming soon) through the Claude add-ins for Microsoft 365. Once the add-ins are installed, context carries automatically between applications, so work that starts in a model can end in a deck without re-explaining anything in between.

Finally, we’re continuing to expand our partner ecosystem with new connectors and an MCP app, so the agents draw on the data financial professionals already use. Connectors give Claude governed, real-time access to a provider’s data, and MCP apps go a step further by embedding the provider’s own tools directly inside Claude.

These updates pair best with Claude Opus 4.7, which is state-of-the-art on financial tasks and leads the industry on [Vals AI's Finance Agent benchmark](https://www.vals.ai/benchmarks/finance_agent), at 64.37%.

## New agent templates for finance work

Each agent template is a reference architecture that packages three things: skills (instructions and domain knowledge for the task), connectors (governed access to the data the task runs on), and subagents (additional Claude models that are called upon by the main agent, for specific sub-tasks such as comparables selection or methodology checks). Firms can adapt any of them to their own modeling conventions, risk policies, and approval flows.

Enable these new agent templates either as plugins within Claude Cowork or Claude Code, or as cookbooks for Claude Managed Agents. Find all the plugins and cookbooks at the [financial services marketplace](https://github.com/anthropics/financial-services).

The full list of new agents is as follows:

**Research and client coverage**

*   **Pitch builder** creates target lists, runs comparables, and drafts pitchbooks for client meetings;
*   **Meeting preparer** assembles client and counterparty briefs ahead of calls;
*   **Earnings reviewer** reads transcripts and filings, updates models, and flags thesis-relevant changes;
*   **Model builder** creates and maintains financial models from filings, data feeds, and analyst inputs;
*   **Market researcher** tracks sector and issuer developments, synthesizes news, filings, and broker research, and flags items for credit and risk review.

**Finance and operations**

*   **Valuation reviewer** checks valuations against comparables, methodology, and the firm's review standards;
*   **General ledger reconciler** reconciles general ledger accounts and runs net asset value calculations against the books of record;
*   **Month-end closer** runs the close checklist, prepares journal entries, and produces close reports;
*   **Statement auditor** reviews financial statements for consistency, completeness, and audit-readiness;
*   **KYC screener** assembles entity files, reviews source documents, and packages escalations for compliance review.

[Video 3](https://www.youtube.com/watch?v=foxeK2AXfHQ)

There are two ways to put these to work.

As a plugin in Claude Cowork or Claude Code, the template runs alongside the analyst, using the software already on their desktop. Hand the Pitch agent a target list, and you can get back a comps model in Excel, a pitchbook drafted in PowerPoint, and a cover note ready in Outlook.

As a [Claude Managed Agent](https://platform.claude.com/docs/en/managed-agents/overview), the same template runs autonomously on the Claude Platform, for work that spans a whole book of deals or a nightly schedule. The cookbooks stand it up with the building blocks a firm would otherwise engineer themselves: long-running sessions that can work throughout a multi-hour deal close, per-tool permissions, managed credential vaults, and a full audit log in the Claude Console where compliance and engineering teams can inspect every tool call and decision.

In both scenarios, users stay firmly in the loop—reviewing, iterating on, and approving Claude’s work before it goes to a client, gets filed, or is acted on.

## Claude across Excel, PowerPoint, Word, and Outlook

Claude can work directly in Microsoft [Excel](https://claude.com/claude-for-excel), [PowerPoint](https://claude.com/claude-for-powerpoint), [Word](https://claude.com/claude-for-word), and Outlook via add-ins.

In Outlook, it can act as a chief of staff that triages your inbox, arranges meetings, and drafts responses in your voice. In Excel, it builds financial models from filings and data feeds, audits formulas across linked workbooks, and runs sensitivity analyses. In PowerPoint, it drafts decks that update automatically when the underlying numbers change. In Word, it edits credit memos against a firm’s own templates. Claude carries its knowledge and context across all four platforms: an analyst who’s started a model in Excel doesn’t need to re-explain it when that work moves to PowerPoint.

In Claude Cowork, users can also assign Claude work tasks from anywhere—by text or by voice—using [Dispatch](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork). Claude can keep working on analysts’ local files while they’re away from their desk, with finished work ready for review by the time they’re back.

## The broadest ecosystem for financial services

AI agents are only as good as the data and context they can access. Claude connects to dozens of market data, research platforms, and financial companies’ internal systems—including FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar, Chronograph, LSEG, and Daloopa—along with firms’ own data warehouses, research repositories, and CRMs, all under governed access controls.

We’re now adding connectors and an MCP app from new partners. The new connectors give direct, real-time access to market and research data, while the MCP app surfaces custom, interactive UI directly within Claude.

The new connectors are:

*   **Dun & Bradstreet**, which provides the global standard for verified business identity and helps enterprises connect systems of record and scale AI-enabled workflows;
*   **Fiscal AI**, which extends real-time fundamentals coverage across public equities for deeper research and benchmarking;
*   **Financial Modeling Prep**, which provides real-time quotes, fundamentals, statements, filings, and transcripts across equities, ETFs, crypto, forex, and commodities;
*   **Guidepoint**, which searches 100,000+ compliance-reviewed expert interview transcripts and provides verbatim excerpts linked to source;
*   **IBISWorld**, which tracks industry-level revenue, financial ratios, risk scores, cost structures, and forecasts across thousands of sectors;
*   **SS&C Intralinks**, which gives Claude access to DealCenter AI data rooms for document search, diligence Q&A, and deal-activity tracking;
*   **Third Bridge**, which gives Claude access to primary-source expert interviews on companies, sectors, and value chains;
*   **Verisk**, which provides property, casualty, and specialty insurance data for underwriting, claims, and risk analysis.

In addition, **Moody's** has launched an MCP app that brings proprietary credit ratings and data on more than 600 million public and private companies for use in compliance, credit analysis, and business development.

## Claude's impact in financial services

Many leading banks, asset managers, and insurers choose Claude. It supports the full range of these organizations' work: front office tasks like research and client experience, middle office work in underwriting, risk, and compliance, and back office work like code modernization and operations.

![Image 1: Citadel logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa46aeeca5f6a18c7e83ff1235049e57d2efe5f47-3840x504.png&w=256&q=75)

> Our investment professionals live in data and analytical models, and Claude for Excel meets them there. Analysts are using it to build and update coverage models, separate signal from noise, and pressure-test their work — all with a step-change in efficiency.

![Image 2: FIS logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3c70dfc4944696f4d3ecb9357d8b760190f7e322-2394x1000.svg)

> FIS sits at the center of how money moves for thousands of financial institutions worldwide. When we began to build AI agents, we knew we needed a provider we could trust. Anthropic was the clear choice. Together we're building an agent that compresses AML investigations from days to minutes, with credit decisioning, fraud prevention, and deposit retention agents to follow. FIS clients won't need to build this infrastructure themselves. It's already here.

![Image 3: BNY logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff4da4be08db2bc43ee243e4545cf9b471d82a5d3-3840x833.png&w=256&q=75)

> With Eliza and Claude, we’re giving processes new digital employees who work the case end to end.

![Image 4: Carlyle logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7b60c286a362ff94c2f09bd076a95d1172a81961-1560x194.png&w=256&q=75)

> Carlyle has adopted Claude as a key part of our AI technology stack because of its strong coding capabilities, agentic reasoning, and continual advances in both the underlying models and key features. Claude is a core tool for delivering value across our firm from investing to operations to portfolio management.

![Image 5: Mizuho logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7e8a9f3b8048c0321b46bf1f0c2b01b93ff4c38e-1280x385.png&w=256&q=75)

> Claude compresses and enhances the work before the meeting so each and every meeting is more impactful — prep time has been transformed into idea time, with faster workflows, richer client insights, and new use cases we didn’t anticipate.

![Image 6: Travelers logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb83d0c8ad42d0baf626410b00027ba497a36da5b-3840x2160.png&w=256&q=75)

> Since we started introducing personalized Claude and Claude Code assistants, we have seen significantly elevated levels of engineering excellence and meaningful improvements in productivity. We are pleased to be delivering value by putting AI to work in advancing the company’s strategic innovation priorities of extending our advantage in risk expertise; providing great experiences for our customers, distribution partners and employees; and optimizing our productivity and efficiency.

![Image 7: Walleye logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e9fe73c429973c6f07001b40d834f3e7b71a88b2-317x83.svg)

> 100% of employees at Walleye Capital use Claude Code. This level of adoption across our 400-person hedge fund reflects our AI-first mindset: we expect everyone to constantly rethink how they work, always asking 'How can AI help me do this?'—whether or not they're in a traditionally technical role.

![Image 8: Hg logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F91e187d85b3367ce7d8e6c547b558669aefb3780-500x242.png&w=256&q=75)

> Claude for Excel powered by Claude Opus 4.6 represents a significant leap forward. From due diligence to financial modeling, it’s proving to be a remarkably powerful tool for our team - taking unstructured data and intelligently working with minimal prompting to meaningfully automate complex analysis. It’s an excellent example of AI augmenting investment professionals’ capabilities in tangible, time-saving ways.

![Image 9: Dun & Bradstreet logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Faf68ac48df26917bc592472d7e0c6b61d49cd654-3840x565.png&w=256&q=75)

> Agents in risk workflows must understand who they’re dealing with. Bringing Dun & Bradstreet's Commercial Graph and D-U-N-S® Number, the global standard for business identity, into Claude ensures AI agents operate on verified data and deliver the deterministic, auditable outcomes financial workflows require.

![Image 10: Morningstar logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F640abf19fdf2d81f67926e60f3dffa4f79fe6562-3840x806.png&w=256&q=75)

> Investors need AI they can trust — and trust starts with the data behind it. Morningstar and PitchBook bring decades of independent, analyst-backed intelligence to Claude, so users aren't just getting faster answers. They're getting better ones. Together, we're building the intelligence layer that powers smarter decisions across public and private markets.

![Image 11: FactSet logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fee54230e131ad008f3897e85e91264478dfc2d25-1491x289.png&w=256&q=75)

> Our clients — institutional investors, asset managers, hedge funds, and banks — increasingly want to run AI-assisted workflows directly against select sets of FactSet data. Partnering with Anthropic lets us bring Claude into a hosted programmatic environment where they can reason over our foundational market data, research, and analytics in the tools they already use. Internally, firm-wide Claude Code adoption across our engineering org is accelerating how quickly we can ship those capabilities.

01 /

11

## Getting started

Our new Claude agents are available today at our [financial services marketplace](https://github.com/anthropics/financial-services). They can be used as plugins in Claude Cowork or Claude Code on all paid plans, or as Managed Agents in the Claude Platform (in public beta) for programmatic use. The new connectors and Moody’s MCP app are also available to joint customers on paid plans.

The Claude for Excel, PowerPoint, and Word add-ins are generally available, and Claude for Outlook is coming soon.

To see these capabilities in action, you can register for our [livestreamed keynote](https://www.anthropic.com/events/the-briefing-financial-services-virtual-event), and [hands-on webinar](https://www.anthropic.com/webinars/claude-for-financial-services-putting-agents-to-work) which will provide deeper practical adoption guidance. For additional support, [contact our sales team](https://claude.com/contact-sales/financial-services), and learn more about [our solutions for financial services](https://claude.com/solutions/financial-services).

## Related content

### Claude Fable 5 and Claude Mythos 5

Our next generation of intelligence for the hardest knowledge work and coding problems.

[Read more](https://www.anthropic.com/news/claude-fable-5-mythos-5)

### Introducing the Services Track and Partner Hub of the Claude Partner Network

[Read more](https://www.anthropic.com/news/services-track-partner-hub)

### What we learned mapping a year’s worth of AI-enabled cyber threats

As AI transforms the nature of and methods behind cyberattacks, how well do the techniques and frameworks used by the security community hold up? In a new report, we seek to answer that question.

[Read more](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack)
