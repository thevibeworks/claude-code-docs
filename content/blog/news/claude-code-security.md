Title: Making frontier cybersecurity capabilities available to defenders

URL Source: https://www.anthropic.com/news/claude-code-security

Markdown Content:
**Claude Code Security**, a new capability built into Claude Code on the web, is now available in a limited research preview. It scans codebases for security vulnerabilities and suggests targeted software patches for human review, allowing teams to find and fix security issues that traditional methods often miss.

Security teams face a common challenge: too many software vulnerabilities and not enough people to address them. Existing analysis tools help, but only to a point, as they usually look for known patterns. Finding the subtle, context-dependent vulnerabilities that are often exploited by attackers requires skilled human researchers, who are dealing with ever-expanding backlogs.

AI is beginning to change that calculus. We’ve recently shown that [Claude can detect novel, high-severity vulnerabilities](https://red.anthropic.com/2026/zero-days/). But the same capabilities that help defenders find and fix vulnerabilities could help attackers exploit them.

Claude Code Security is intended to put this power squarely in the hands of defenders and protect code against this new category of AI-enabled attack. We’re releasing it as a limited research preview to Enterprise and Team customers, with expedited access for maintainers of open-source repositories, so we can work together to refine its capabilities and ensure it is deployed responsibly.

**How Claude Code Security works**
----------------------------------

Static analysis—a widely deployed form of automated security testing—is typically rule-based, meaning it matches code against known vulnerability patterns. That catches common issues, like exposed passwords or outdated encryption, but often misses more complex vulnerabilities, like flaws in business logic or broken access control.

Rather than scanning for known patterns, Claude Code Security reads and reasons about your code the way a human security researcher would: understanding how components interact, tracing how data moves through your application, and catching complex vulnerabilities that rule-based tools miss.

Every finding goes through a multi-stage verification process before it reaches an analyst. Claude re-examines each result, attempting to prove or disprove its own findings and filter out false positives. Findings are also assigned severity ratings so teams can focus on the most important fixes first.

Validated findings appear in the Claude Code Security dashboard, where teams can review them, inspect the suggested patches, and approve fixes. Because these issues often involve nuances that are difficult to assess from source code alone, Claude also provides a confidence rating for each finding. Nothing is applied without human approval: Claude Code Security identifies problems and suggests solutions, but developers always make the call.

**Using Claude for cybersecurity**
----------------------------------

Claude Code Security builds on more than a year of research into Claude’s cybersecurity capabilities. Our Frontier Red Team has been stress-testing these abilities systematically: entering Claude in [competitive Capture-the-Flag events](https://red.anthropic.com/2025/ai-for-cyber-defenders/), partnering with Pacific Northwest National Laboratory to [experiment with using AI to defend critical infrastructure](https://red.anthropic.com/2026/critical-infrastructure-defense/), and refining Claude’s ability to find and patch real vulnerabilities in code.

Claude’s cyberdefensive abilities have improved substantially as a result. Using [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6), released earlier this month, our team [found over 500 vulnerabilities](https://red.anthropic.com/2026/zero-days/) in production open-source codebases—bugs that had gone undetected for decades, despite years of expert review. We’re working through triage and responsible disclosure with maintainers now, and we plan to expand our security work with the open-source community.

We also use Claude to review our own code, and we’ve found it to be extremely effective at securing Anthropic’s systems. We built Claude Code Security to make those same defensive capabilities more widely available. And since it’s built on Claude Code, teams can review findings and iterate on fixes within the tools they already use.

**The road ahead**
------------------

This is a pivotal time for cybersecurity. We expect that a significant share of the world’s code will be scanned by AI in the near future, given how effective models have become at finding long-hidden bugs and security issues.

Attackers will use AI to find exploitable weaknesses faster than ever. But defenders who move quickly can find those same weaknesses, patch them, and reduce the risk of an attack. Claude Code Security is one step towards our goal of more secure codebases and a higher security baseline across the industry.

**Getting started**
-------------------

We’re opening a limited research preview of Claude Code Security to Enterprise and Team customers today. Participants will get early access and collaborate directly with our team to hone the tool’s capabilities. We also encourage open-source maintainers to apply for free, expedited access.

[Apply for access here](https://claude.com/contact-sales/security).

To learn more, visit [claude.com/solutions/claude-code-security](http://claude.com/solutions/claude-code-security).

Related content
---------------

### Anthropic’s Responsible Scaling Policy: Version 3.0

[Read more](https://www.anthropic.com/news/responsible-scaling-policy-v3)

### Detecting and preventing distillation attacks

[Read more](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

### Anthropic and the Government of Rwanda sign MOU for AI in health and education

[Read more](https://www.anthropic.com/news/anthropic-rwanda-mou)
