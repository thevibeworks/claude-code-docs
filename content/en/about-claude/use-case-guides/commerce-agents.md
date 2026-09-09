---
title: Commerce agent
url: https://platform.claude.com/docs/en/about-claude/use-case-guides/commerce-agents
description: Build a shopping agent and a merchant agent on Claude using Claude for commerce, an open-source blueprint with working implementations on the Messages API, the Claude Agent SDK, and Claude Managed Agents.
---

This guide shows how to build commerce agents on Claude: a shopping agent that customers use inside your app, and a merchant agent for the people running the store, whether that is the business's own operations staff or the sellers on its platform. It does that through Claude for commerce, an open-source blueprint with a working implementation of each agent on the [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), and [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), runnable examples for retail, travel, telecom, and entertainment, and a Claude Code plugin that scaffolds the same design against your own systems.

The code, setup instructions, and safety documentation are in the [Claude for commerce repository on GitHub](https://github.com/anthropics/commerce-agents). For how the agents are built and why, including the single-agent-with-skills design, UI components as tools, harness-enforced safety, prompt caching, memory, and evals, read the engineering post [A guide to the anatomy of effective commerce agents](https://claude.com/blog/the-anatomy-of-effective-commerce-agents).

<Note>
  The blueprint is a reference implementation to fork and adapt, not a supported product or hosted service.
</Note>

## The shopping agent

The shopping agent lives inside your app and reaches your systems through a single backend interface that you implement over your catalog, cart, preferences, order, policy, and fulfillment services. No method on that interface places an order or moves money. In a conversation the agent can:

* Search the catalog, compare finalists, and turn a described need into a shortlist and a recommendation.
* Plan a coordinated set of items toward a goal such as a trip, an event, or a room, and fit it to a budget.
* Show products, comparisons, plans, order status, and the cart as UI components rendered in the conversation.
* Fill the cart and hand off to your checkout.
* Answer order, delivery, return, and policy questions from your own order and policy systems.
* Remember what a customer asks it to remember and apply it in later sessions.

Five skills load on demand to cover search and discovery, purchase research, planning toward a goal, customer care, and memory and personalization. Rules the agent needs on most turns, such as grounding, cart and checkout semantics, and presentation, live in the system prompt instead.

The agent states products, prices, availability, and store terms only from tool results in the conversation, and cart writes accept only product IDs that a catalog or order tool returned in that session. Checkout stages a summary the customer confirms in your app. If you use a hosted checkout, your back end returns its URL and the host renders it without passing it through the model.

## The merchant agent

The merchant agent supports the people running the store. It reaches your analytics, catalog, inventory, pricing, and campaign systems through its own backend interface, and it can:

* Explain how the business is doing: why a metric moved, which segment drove it, and pace against a comparable period. An optional analysis delegate runs read-only queries under a time and size budget.
* Present a daily digest of what needs attention, including low stock, slow movers, and order exceptions.
* Improve listing content and fix catalog data from material the operator supplies.
* Recommend price changes and promotions within the store's guardrails, with a margin preview.
* Draft marketing campaigns with audiences, placements, and budget.

Its five skills cover performance insights, inventory and operations, catalog and listings, pricing and promotions, and marketing campaigns.

Every write the merchant agent proposes, whether a listing update, a price change, an inventory action, a promotion, or a campaign, is a staged change with a server-generated ID that the operator sees as a preview card. Guardrails such as maximum price move, promotion depth, restock size, campaign budget, and protected fields are checked when the change is staged and again when it is applied. The change applies only after a person approves it outside the conversation: a button in the merchant portal on the Messages API path, a confirmation prompt in the Agent SDK console, or an [always-ask permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies) on the apply tool on Claude Managed Agents. An approval typed in chat approves nothing.

## Vertical examples

Each example includes a customer storefront and a merchant portal over fictional data.

| Vertical      | Storefront                                                                         | Merchant portal                                                                            |
| ------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Retail        | Search, comparison, plans, cart, checkout, and memory over the built-in components | Daily digest, staged restocks and listing fixes, and the analysis delegate over a SQL view |
| Travel        | Date-bound inventory and an itinerary component                                    | Occupancy calendar and date-window rate moves                                              |
| Telecom       | Account context, a plan matrix, and server-authored fee disclosures                | Plan mix, price moves that state the lines affected, and protected regulated fees          |
| Entertainment | Timed holds, waitlists, transfers, a venue map, and all-in fee disclosures         | Event pacing, hold releases that add real capacity, and fee-preserving price moves         |

## Where it runs

The Messages API and Agent SDK runtimes run against the Claude API, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Google Cloud's Agent Platform](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), or [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), or through your own gateway. The Claude Managed Agents path runs on the Claude API. The repository's deployment guide shows where each path selects its platform and which model ID format each expects.

## Build your own with the Claude Code plugin

The blueprint ships with a [Claude Code](https://code.claude.com/docs/en/overview) plugin that reads the cloned repository as its reference and builds an agent against your own systems. Its four commands cover the path from nothing to a tested agent:

| Command                    | What it does                                                                                                                              |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `/scaffold-commerce-agent` | Interviews you about your stack, plays the plan back, and scaffolds a shopping agent, a merchant agent, or both on the reference packages |
| `/add-commerce-flow`       | Adds one flow to an existing agent by copying its skill, wiring the tools it calls, and writing its first eval cases                      |
| `/author-commerce-evals`   | Builds an eval suite with a runner, the first cases against your own catalog, and a replay gate for CI                                    |
| `/review-commerce-agent`   | Maps an agent you already run, compares it with the reference, and converts the parts you pick                                            |

The plugin also carries six skills on the architecture, prompt caching, UI as tools, trust and safety, evals, and merchant operations, which load whenever a Claude Code conversation matches them. Installation instructions are in the repository README.

To adapt the reference by hand instead, implement the shopping or merchant backend interface over your services, switch off the systems you don't have with the configuration flags so their tools and prompt lines drop out, and set your brand name, assistant name, and voice. The repository's backend guide walks through identity and credentials, ordered flows, checkout hand-off, and products with options. A pilot can implement search and product details and stub the rest.

## Get started

<CardGroup cols={2}>
  <Card title="Claude for commerce on GitHub" icon="github-logo" href="https://github.com/anthropics/commerce-agents">
    Clone the blueprint and run both agents locally.
  </Card>

  <Card title="A guide to the anatomy of effective commerce agents" icon="book" href="https://claude.com/blog/the-anatomy-of-effective-commerce-agents">
    Read how the agents are built and why.
  </Card>
</CardGroup>
