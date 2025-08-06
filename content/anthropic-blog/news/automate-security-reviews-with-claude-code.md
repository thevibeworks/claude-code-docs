Title: Automate security reviews with Claude Code

URL Source: https://www.anthropic.com/news/automate-security-reviews-with-claude-code

Markdown Content:
Today we're introducing automated security reviews in Claude Code. Using our GitHub Actions integration and a new /security-review command, developers can easily ask Claude to identify security concerns—and then have it fix them.

As developers increasingly rely on AI to ship faster and build more complex systems, ensuring code security becomes even more critical. These new features let you integrate security reviews into your existing workflows, helping you catch vulnerabilities before they reach production.

Review code for vulnerabilities from your terminal
--------------------------------------------------

The new /security-review command lets you run ad-hoc security analyses from your terminal before committing code. Run the command in Claude Code, and Claude will search your codebase for potential vulnerabilities and provide detailed explanations of any issues found.

This command uses a specialized security-focused prompt that checks for common vulnerability patterns including:

*   SQL injection risks
*   Cross-site scripting (XSS) vulnerabilities
*   Authentication and authorization flaws
*   Insecure data handling
*   Dependency vulnerabilities

You can also ask Claude Code to implement fixes for each issue after they’re identified. This keeps security reviews in your inner development loop, catching issues early when they're easiest to fix.

Automate security reviews for new pull requests
-----------------------------------------------

The new GitHub action for Claude Code takes security reviews a step further by automatically analyzing every pull request when it's opened. When configured, the action:

*   Triggers automatically on new pull requests
*   Reviews code changes for security vulnerabilities
*   Applies customizable rules to filter out false-positives and known issues
*   Posts comments inline on the PR with any concerns found, including recommendations for fixes

This creates a consistent security review process across your entire team, ensuring no code reaches production without a baseline security review. The action integrates with your existing CI/CD pipeline and can be customized to match your team's security policies.

![Image 1: 2 screenshots showing vulnerabilities that were caught by Claude Code, leaving comments in GitHub.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F37aa77df52f1a4e8d81f398f48dbb98a5ba1d5ec-1920x1080.png&w=3840&q=75)

Improving product security at Anthropic
---------------------------------------

We're using these features ourselves to help secure the code our team ships to production, including Claude Code itself. Since setting up the GitHub action, this has already caught security vulnerabilities in our own code and prevented them from being shipped.

For example, last week, our team built a new feature for an internal tool that relied on starting a local HTTP server meant to accept local connections. The GitHub action identified a remote code execution vulnerability exploitable through DNS rebinding and it was fixed before the PR was ever merged.

![Image 2: A GitHub comment showing a remote code execution vulnerability](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa370dba2f6e5095cdbcb23ef878dda4befd61d95-1920x1080.png&w=3840&q=75)

In another case, an engineer built a proxy system to enable secure management of internal credentials. The GitHub action automatically flagged that this proxy was vulnerable to SSRF attacks, and we promptly fixed this issue.

![Image 3: A GitHub comment showing a SSRF attack vulnerability](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F23dd3b5404c6f7dc812df83a7de95babab286865-1920x1080.png&w=3840&q=75)

Getting started
---------------

Both features are available now for all Claude Code users. To start using automated security reviews:

*   **For the /security-review command**: Simply update Claude Code to the latest version and run /security-review in your project directory. [See the documentation](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command) to customize your own version of the command
*   **For the GitHub action**: [See the documentation](https://github.com/anthropics/claude-code-security-review) for step-by-step installation and configuration instructions
