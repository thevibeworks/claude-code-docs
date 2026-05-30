Title: Automated Security Reviews in Claude Code

URL Source: https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code

Markdown Content:
Claude Code now includes automated security review features to help you identify and fix vulnerabilities in your code. This guide explains how to use the /security-review command and GitHub Actions to improve your code security.

## Overview

Automated security reviews in Claude Code help developers catch vulnerabilities before they reach production. These features check for common security issues including SQL injection risks, cross-site scripting (XSS) vulnerabilities, authentication flaws, insecure data handling, and dependency vulnerabilities.

You can use security reviews in two ways: through the /security-review command for on-demand checks in your terminal, or through GitHub Actions for automatic review of pull requests.

## Availability

These features are available for all Claude Code users, including:

## Using the /security-review command

The /security-review command lets you run security analysis directly from your terminal before committing code.

### Running a Security Review

To check your code for vulnerabilities:

### Implementing Fixes

After Claude identifies vulnerabilities, you can ask it to implement fixes directly. This keeps security reviews integrated into your development workflow, allowing you to address issues when they're easiest to resolve.

### Customizing the Command

You can customize the /security-review command for your specific needs. See the[security review documentation](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command) for configuration options.

## Setting up GitHub Actions for automated PR reviews

After installing and configuring the GitHub action, it will automatically review every pull request for security vulnerabilities when it's opened.

### Installation

To set up automated security reviews for your repository:

### How It Works

Once configured, the GitHub action:

This creates a consistent security review process across your entire team, ensuring code is checked for vulnerabilities before merging.

### Customization Options

You can customize the GitHub action to match your team's security policies, including setting specific rules for your codebase and adjusting sensitivity levels for different vulnerability types.

## What security issues can be detected?

Both the /security-review command and GitHub action check for common vulnerability patterns:

## Getting Started

To start using automated security reviews:

## Best Practices

For optimal results, we recommend running /security-review before committing significant changes and configuring the GitHub action for all repositories containing production code. Consider adjusting the filtering rules based on your team's specific security requirements and codebase characteristics.

* * *

Related Articles

[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[Claude Code on the web](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)[Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)[Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)[Use Claude Security](https://support.claude.com/en/articles/14661296-use-claude-security)
