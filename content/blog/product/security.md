Title: Anthropic's agentic solution for vulnerability detection | Claude Security

URL Source: https://www.anthropic.com/product/security

Markdown Content:
Claude Security reasons about your code like a security researcher: scanning for vulnerabilities, validating findings, and proposing targeted patches. It helps close the loop from finding to shipped fix, so vulnerabilities get resolved instead of sitting in a queue.

## Built for defenders

Software runs critical infrastructure: power grids, hospitals, payment networks, and the supply chains economies depend on. The teams defending that code are stretched thin, and the pace of AI-enabled threats is accelerating. Claude Security helps give defenders the leverage and scale they need to respond: the ability to reason across an entire codebase, surface what is exploitable, and ship the fix before it becomes an incident.

## Surfacing vulnerabilities, ready for review

Claude Security reads code the way a security researcher would. It follows variables across files, and reasons about which inputs can be trusted. Findings are written the way one engineer would explain them to another: what the issue is, why it matters, what to change. And it can propose the patch.

Proposed fixes open in Claude Code for review; these aren't changes that ship on their own. Humans stay in the decision loop, so teams are always in control.

## How Claude Security works, from scan to fix

01

### Finding what scanners miss

Claude Security reads code the way a security researcher would: understanding how components interact, tracing how data moves through your application, and catching logic and access-control flaws that pattern-matching tools often miss.

02

### Validating before you triage

Every finding goes through multi-stage verification. Claude re-examines each result to prove or disprove it, filters false positives, and assigns severity and confidence ratings so your team works a short, ranked list instead of a noisy report.

03

### Suggesting targeted fixes

For each validated finding, Claude generates a targeted patch and creates a branch ready for PR review. You inspect the diff in the dashboard. Nothing ships without your approval. Your call, every time.

04

### Running on your schedule

Scheduled scans keep coverage continuous, and webhooks push new findings into a team's existing tools. Security review happens on the team's cadence rather than in response to a release.

## The research behind Claude Security

Claude Security is built on model capabilities that Anthropic's [Frontier Red Team](https://red.anthropic.com/) has refined through applied research: competitive Capture-the-Flag events, critical-infrastructure defense work with national labs, and systematic vulnerability hunting in production code. That work surfaced [over 500 previously unknown vulnerabilities](https://red.anthropic.com/2026/zero-days/) in widely used open-source software, including bugs that had survived decades of expert review. Claude Security brings the same model capabilities to the code your team owns and ships.

## Agent safety

Capable agents need clear constraints. Claude Security scopes its access to the repository it's invited into and surfaces proposed changes for human review rather than acting on them. These are the same principles we apply across our agentic products, drawing on alignment research into how to let capable systems do useful work without giving up oversight.

Read our [recent research on agent safety](https://www.anthropic.com/research/trustworthy-agents) for more insights.

### What is Claude Security?

Claude Security is a capability accessed through [Claude.ai](https://claude.ai/) and Claude Code on the web that reads a codebase in context, finds vulnerabilities a rules-based scanner would miss, and proposes fixes for human review.

### How is Claude Security different from a traditional code scanner?

Traditional scanners match code against patterns someone has already written rules for. Claude Security reasons about how code actually behaves, including how data flows across files and where trust boundaries break. That lets it find issues outside the patterns a rules engine knows about, reducing false positives.

### What kinds of vulnerabilities does Claude Security find?

Claude Security reasons about code the way a security researcher would, so it catches the context-dependent issues that pattern-matching scanners miss: business logic flaws, broken access control, and unsafe data flows that span files and components.

### Does Claude Security make changes to my code?

Only with your approval. Claude Security can generate a suggested patch for each validated finding
