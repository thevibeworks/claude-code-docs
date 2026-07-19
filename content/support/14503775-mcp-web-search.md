# MCP: Web Search

The Web Search connector gives Claude the ability to search the public internet for real-time information, including verifying facts, pulling recent news, and researching topics outside its training data.

For questions about web search in commercial Claude, see **[Enabling and using web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)**.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256120763/7652c6c669446113eae75f3c5977/9c74d57e-aaa2-4f1c-bfe4-2b9b87fd41ab?expires=1784436300&amp;signature=94b6179aa60a020e4f42e7fe2c2c7a94db3a65a7142147f05ef0e71df46f77eb&amp;req=diIiEMh8nYZZWvMW1HO4zQvFLLZXjsL7M%2Fw5SJgC29FXtBiOWELmWjIxd9EG%0ATKknIN9zzuCMjMyT0ls%3D%0A)

## How Web Search differs for Claude for Government

In commercial Claude, web search is a built-in capability. In Claude for Government, native web search is disabled. The Web Search MCP connector replaces it, providing the same capability with additional transparency and control appropriate for a FedRAMP environment.

**Important:** The Web Search connector runs inside Claude for Government's FedRAMP High boundary, but it calls the **Brave Search API**, which is outside that boundary. When you approve a search, the query string — and only the query string — is transmitted to Brave. No conversation history, user identity, organization identity, or attached files are sent.

Brave does not persistently store search queries, responses, or other user data. Before transmission, Claude reformulates your request into a generic, de-identified search query with no user or org metadata attached.

Your agency is solely responsible for evaluating whether sending search queries to a non-FedRAMP third party is appropriate for your workloads, data classification levels, and regulatory requirements.

**Tip:** Use Organization Preferences to tell Claude about your agency's specific sensitive-data rules. Claude already avoids obviously sensitive terms in search queries, but org-specific guidance sharpens that.

## Approve each search before it runs

Every search requires fresh approval. There is no blanket consent and the approval requirement cannot be disabled.

1. Claude decides a web search would help answer your question.

2. Claude formulates a de-identified search query and **displays the exact query text to you.**

3. Claude pauses—nothing has been sent yet.

4. Review the query. If it contains anything you don't want transmitted outside the boundary, decline and rephrase your request.

5. If you approve, the query goes to Brave, results come back, and Claude continues.

## Set up the Web Search connector

Claude for Government uses the connector flow to enable web search.

### Owners and Primary Owners

1. Navigate to **[claude.fedstart.com/admin-settings/connectors](https://claude.fedstart.com/admin-settings/connectors)**

2. Click Browse connectors → Web Search.

3. Review the advisory text.

4. Click "Add to your team."

No authentication step is required. Once added, Web Search is available in every user's chats immediately—there's no per-user connection, because the per-query approval serves as the consent gate instead.

### For individual users

Once your org admin enables it, Web Search is available in your chats immediately. There's no per-user connection step. You'll be asked to approve individual queries as they come up.

---

## Example use cases

*"What were the key provisions in the infrastructure bill passed last month?"*

Claude proposes a search query like infrastructure bill key provisions [month year], you approve it, and Claude summarizes results from recent news.

*"Is there a published CVE for [software] version [X]? When was it disclosed?"*

Claude proposes a search targeting CVE databases and vendor advisories, you approve, and Claude returns the CVE details with source links.

---

## Frequently asked questions

### Does any of my conversation data get sent to Brave?

No. Only the search query string (which Claude shows you for approval) is transmitted. No conversation history, no user identity, no organization identity, no attached files.

### Can I use web search without approving every query?

No. Per-query approval is a required control in Claude for Government and cannot be disabled.

### Did Anthropic need a separate FedRAMP approval for web search?

No. The Remote MCP framework was authorized as a feature, which covers individual connectors including Web Search. Your agency's responsibility is to evaluate whether the specific data-handling characteristics of this connector (queries to a non-FedRAMP third party) are appropriate for your use case.