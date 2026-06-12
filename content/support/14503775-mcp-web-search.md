Title: MCP: Web Search

URL Source: https://support.claude.com/en/articles/14503775-mcp-web-search

Markdown Content:
The Web Search connector gives Claude the ability to search the public internet for real-time information, including verifying facts, pulling recent news, and researching topics outside its training data.

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256120763/7652c6c669446113eae75f3c5977/9c74d57e-aaa2-4f1c-bfe4-2b9b87fd41ab?expires=1781244000&signature=8612634b1d5813df376364dca578bc78d5ed3a1509641b9c865fa1084ff1e1fe&req=diIiEMh8nYZZWvMW1HO4zQvFLLNRicD4M%2Fw5SJgC29EeSa42Orc0pcvCBimQ%0A5U9%2B5H%2F%2FjUQUlNKJm%2BU%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256120763/7652c6c669446113eae75f3c5977/9c74d57e-aaa2-4f1c-bfe4-2b9b87fd41ab?expires=1781244000&signature=8612634b1d5813df376364dca578bc78d5ed3a1509641b9c865fa1084ff1e1fe&req=diIiEMh8nYZZWvMW1HO4zQvFLLNRicD4M%2Fw5SJgC29EeSa42Orc0pcvCBimQ%0A5U9%2B5H%2F%2FjUQUlNKJm%2BU%3D%0A)

## How Web Search differs for Claude for Government

In commercial Claude, web search is a built-in capability. In Claude for Government, native web search is disabled. The Web Search MCP connector replaces it, providing the same capability with additional transparency and control appropriate for a FedRAMP environment.

## Approve each search before it runs

Every search requires fresh approval. There is no blanket consent and the approval requirement cannot be disabled.

## Set up the Web Search connector

Claude for Government uses the connector flow to enable web search.

### Owners and Primary Owners

No authentication step is required. Once added, Web Search is available in every user's chats immediately—there's no per-user connection, because the per-query approval serves as the consent gate instead.

### For individual users

Once your org admin enables it, Web Search is available in your chats immediately. There's no per-user connection step. You'll be asked to approve individual queries as they come up.

## Example use cases

_"What were the key provisions in the infrastructure bill passed last month?"_

Claude proposes a search query like infrastructure bill key provisions [month year], you approve it, and Claude summarizes results from recent news.

_"Is there a published CVE for [software] version [X]? When was it disclosed?"_

Claude proposes a search targeting CVE databases and vendor advisories, you approve, and Claude returns the CVE details with source links.

## Frequently asked questions

### Does any of my conversation data get sent to Brave?

No. Only the search query string (which Claude shows you for approval) is transmitted. No conversation history, no user identity, no organization identity, no attached files.

### Can I use web search without approving every query?

No. Per-query approval is a required control in Claude for Government and cannot be disabled.

### Did Anthropic need a separate FedRAMP approval for web search?

No. The Remote MCP framework was authorized as a feature, which covers individual connectors including Web Search. Your agency's responsibility is to evaluate whether the specific data-handling characteristics of this connector (queries to a non-FedRAMP third party) are appropriate for your use case.

* * *

Related Articles

[Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)[Public Sector FAQs](https://support.claude.com/en/articles/13756069-public-sector-faqs)[Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)[MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)[MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
