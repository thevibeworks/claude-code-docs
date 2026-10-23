---
title: What CMEK covers on Claude Platform
url: https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform
description: Look up which Claude Platform data your key encrypts, what turns off or changes, and what stays under Anthropic's key.
---

For Claude Enterprise, see [What CMEK covers on Claude Enterprise](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise). Beta and research preview features that aren't listed here might not be covered by customer-managed encryption keys (CMEK).

## Encrypted with your key

* Message content.
* Files and attachments, whether sent inline with a request or uploaded with the Files API.
* MCP and tool configuration.
* [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) (beta) data, including agent configurations, environments, webhooks, sessions and their events, [memory stores](https://platform.claude.com/docs/en/managed-agents/memory) (beta) and their memories and memory versions, and [dreams](https://platform.claude.com/docs/en/managed-agents/dreams) (research preview).
* Batch API and Skills API data stored at rest.
* Tool data stored at rest by web search, web fetch, code execution, bash, text editor, MCP connector (beta), structured outputs, advisor tool (beta), computer use, browser use, and context management.
* Backups and snapshots, which inherit the key.

## Turned off or changed

This list is not exhaustive. Review it with your team before you set up CMEK.

| Feature                                                                                                        | What changes                                                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Playground in the Claude Console                                                                               | Turned off.                                                                                                                                                                                                                            |
| Structured outputs, including `strict: true` on tools, with Claude Fable or Claude Mythos models               | Turned off in CMEK organizations. With other models, data that structured outputs store at rest is [encrypted with your key](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-platform#encrypted-with-your-key). |
| [Organization webhooks](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#errors) (beta) | Turned off for an organization whose default workspace uses a key. Requests return a 400 error.                                                                                                                                        |
| Zero data retention (ZDR)                                                                                      | A workspace with your key retains data. See [CMEK, data retention, and ZDR](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention).                                                                                    |

## Encrypted with Anthropic's key

The features that store this data stay available, but the data isn't encrypted with your key. You can turn off some of these features in **Settings**.

| Data                                                                                                                                                                                          | Details                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing data                                                                                                                                                                                 | Written before [your key takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect).                                       |
| Data that isn't at rest, and data with a TTL shorter than 24 hours                                                                                                                            | For example, cache.                                                                                                                                                           |
| Activity Feed, audit logs, and telemetry network traffic such as OpenTelemetry                                                                                                                | Kept under Anthropic's key so that you can maintain compliance even if your key can't be used.                                                                                |
| Claude Managed Agents [vault credential](https://platform.claude.com/docs/en/managed-agents/vaults) values, such as OAuth tokens and client secrets                                           | Write-only and never returned in API responses.                                                                                                                               |
| [User profiles](https://platform.claude.com/docs/en/manage-claude/user-profiles)                                                                                                              | Profile fields such as `name` and `metadata`. Don't store sensitive personal data in profile `metadata`.                                                                      |
| Claude Console feedback                                                                                                                                                                       | Ratings and comments that members choose to send with the **Feedback** option. No setting turns it off.                                                                       |
| [OpenTelemetry destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#add-a-destination) request headers, such as the API key header of your observability platform | Write-only and never returned in API responses.                                                                                                                               |
| Account data for users in your organization                                                                                                                                                   | Includes names, email addresses, and profile pictures.                                                                                                                        |
| Preserved records                                                                                                                                                                             | Anthropic can preserve specific records [in three narrow cases](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#limited-preservation-outside-your-key). |

## Where CMEK does not apply: Claude Code telemetry

When Claude Code connects through an LLM gateway or proxy (a custom `ANTHROPIC_BASE_URL`), CMEK does not apply to Claude Code's operational telemetry. To turn this telemetry off, set the `DISABLE_TELEMETRY` environment variable to `1`, as described under [Telemetry services](https://code.claude.com/docs/en/data-usage#telemetry-services) in the Claude Code documentation.
