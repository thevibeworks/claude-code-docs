Title: Use Claude for Word

URL Source: https://support.claude.com/en/articles/14465370-use-claude-for-word

Markdown Content:
Claude for Word is an add-in that integrates Claude into your Word workflow. It’s designed for professionals who work extensively with documents, particularly in legal review, financial memo drafting, and iterative editing.

With Claude for Word, you can:

## Get started with Claude for Word

### Supported versions

### For individuals

### For admins

**Deploy Claude for Word to your organization:**

After installation, team members can open Word, activate the Claude add-in (from Tools > Add-ins on Mac or Home > Add-ins on Windows), sign in with their Claude credentials, and start working with their documents.

### Connect through an LLM gateway

If your organization routes API traffic through an internal LLM gateway connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the add-in without a Claude account. This is the same gateway pattern used by Claude Code.

## Key features

### Read and understand documents

Ask Claude questions about specific sections, clauses, or defined terms in your document. Claude provides answers with clickable citations that navigate directly to the referenced section in your document.

**Example prompts:**

### Edit selected text

Select a passage and tell Claude what to change. Claude edits only the selection while preserving surrounding styles, numbering, and formatting. New text inherits the paragraph style, font, and numbering of the surrounding content.

**Example prompts:**

### Track changes mode

When you enter suggested edits mode, Claude’s edits land as tracked revisions. The original text is visible as a deletion and the new text as an insertion, all reviewable in Word’s native review pane. This gives you a clear audit trail of what Claude changed, so you can accept or reject each revision individually.

**Example prompts:**

### Comment-driven editing

Claude reads comment threads in your document, understands what text each thread is anchored to, and can work through them one by one. For each comment, Claude edits the anchored passage and replies to the thread with a note explaining what it did.

**Example prompts:**

### Summarize counterparty redlines

When a counterparty returns a document with tracked changes, Claude can read and summarize what they changed. Ask Claude to group changes by severity or flag the ones worth pushing back on.

**Example prompts:**

### Fill templates

Draft sections in your document’s heading and paragraph styles. Claude uses your template’s formatting when generating content, so new headings, bullets, and table entries match what’s already there. Tables populate in place without reflowing layout or changing column widths.

**Example prompts:**

### Semantic navigation

Find every provision or passage in your document that touches a specific theme. Claude returns thematic matches, not just keyword hits, and each result navigates to the relevant location on click.

**Example prompts:**

## Work across Word, Excel, and PowerPoint

Claude for Word shares context with Claude for Excel and Claude for PowerPoint, so Claude can work across your open documents in a single conversation. For example, you can ask Claude to pull numbers from an Excel model into a Word memo, or summarize a Word document into PowerPoint slides, without copying and pasting between apps.

## Context and session management

### Auto-compaction

### Chat history

Chat history is now stored locally in your browser using IndexedDB. Unlike Claude, conversations aren't stored on Anthropic's servers—they're saved client-side and aren't synced across devices or browsers. You can clear all chat history from Settings at any time, and the local store is cleared when you clear your browser data.

Your chat history is specific to the combination of the add-in surface, your user ID, and your organization ID—so your Excel, PowerPoint, and Word histories are separate, but conversations carry across different documents within Word (or different presentations within PowerPoint/workbooks within Excel). If you switch organizations, you'll have a separate chat history.

### Overwrite protection

To avoid accidental data loss, Claude warns you before overwriting existing data.

## Current limitations

For Claude for Word use, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** Data will be deleted after 30 days, but will be cached for a number of hours so users can access context in recently closed out documents.

Enterprise organizations can route full audit telemetry from Claude for Word to their own OpenTelemetry (OTEL) collector for integration with a SIEM or observability platform. Learn more about **[configuring a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents)**. On Free, Pro, Max, and Team plans, observability and auditability aren't available for Claude for Word. Claude for Word doesn’t inherit custom data retention settings your organization might have set, and isn’t included in Enterprise audit logs or the Compliance API at this time.

As a beta feature, Claude for Word is **not recommended** for:

### Unsupported versions

## Best practices

To use Claude for Word safely and effectively:

## Prompt injection attack risks

Only use Claude for Word with trusted documents and not documents from external untrusted sources (for example, downloaded templates, counterparty files, or collaborative documents shared via email).

An important risk for people using Claude for Word and other AI tools that can read and edit documents is prompt injection attacks that hide malicious instructions in document content (text, comments, tracked changes, headers, footers) to trick AI models into taking unintended actions. For example, a seemingly routine contract received from an external party might contain hidden instructions to modify terms or exfiltrate data. Claude may interpret these instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude for Word can be manipulated to:

While we continue to develop our offerings and improve safety measures to reduce these risks, you should exercise caution when using Claude for Word and should not use it with documents from external, untrusted sources.

## Example use cases

### Legal contract review

### Finance memo drafting

### Document QA and consistency

### General document editing

## Frequently asked questions

### Does Claude understand legal and financial document conventions?

Claude recognizes common document patterns including multi-level legal numbering, defined terms, cross-references, and standard contract structures. However, always verify that outputs match your specific requirements and your firm’s standard positions.

### Can I use Claude for Word with sensitive data?

Claude for Word works within your existing security framework. For highly sensitive or regulated data, ensure you follow your organization’s data handling policies.

### What happens to my chat history?

Your chat history is stored locally in your browser using IndexedDB. It persists between sessions, so you can return to previous conversations. Chat history is not automatically deleted, but you can clear all of it manually from Settings.

Your history is specific to each add-in surface, your user ID, and your organization. This means your Word, Excel, and PowerPoint chat histories are separate. Within a single surface, your chat history is shared across files—for example, conversations in one Word document appear in another. If you log in to a different organization, you'll see a separate chat history.

### How does Claude access my document?

Claude reads the content of your currently open document, including text, comments, tracked changes, footnotes, tables, and bookmarks. It can only access the document you have open in Word.

### What if Claude makes a mistake?

In tracked changes mode, you can review every edit before accepting it. You can always undo changes using Word’s standard undo function (Ctrl+Z / Cmd+Z).

### Does Claude support .doc files?

Claude for Word supports .docx files. If you’re working with a legacy .doc file, save it as .docx first.

* * *

Related Articles

[Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)[Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)[Work across Microsoft 365 apps](https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[Use Claude for Outlook](https://support.claude.com/en/articles/14855664-use-claude-for-outlook)
