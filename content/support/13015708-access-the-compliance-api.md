# Access the Compliance API

The Compliance API lets your organization programmatically pull activity feed events, chat data, and file content across all your Claude deployments. Use it to monitor, audit, and meet compliance requirements with your own tools.

The Compliance API is available to Enterprise plan organizations, excluding Public Sector organizations, and to Claude Platform customers in Claude chats.

Coverage also includes Cowork (via Claude, Claude Desktop, and Claude Mobile) and Claude Code (via CLI and Claude Desktop). Coverage for the Claude for Microsoft 365 add-ins (Excel, Word, PowerPoint, and Outlook) and Claude Science is available in beta. All of these use your organization's existing Compliance Access Key and settings, so no additional integration is required.

Coverage doesn't include Claude Code on the web, Claude Code accessed through the Claude Platform, other Microsoft 365 apps, or sessions run on Amazon Bedrock or Google Vertex AI.

**Important:** For Claude Enterprise organizations, only your organization's Primary Owner can enable the Compliance API, from **[Organization settings > API](https://claude.ai/admin-settings/api-access)**. You can create a key on the same page by clicking "+Create key" under **Keys**: the Primary Owner can create a key covering every linked organization, and Owners can create keys limited to their own organization. Owners see this page but not the **Compliance API** toggle—only the Primary Owner can turn the API on or off. Admins don't see the page at all. If your organization is linked to a parent organization, the parent organization's Primary Owner enables it and the setting applies to every linked organization.

## Compliance API technical documentation

For setup instructions, endpoints, and reference material, including how to enable the API and create access keys to start pulling data, see the **[Compliance API documentation](https://platform.claude.com/docs/en/manage-claude/compliance-api)** on Claude Platform Docs.

## Compliance API security integrations

Security and compliance platforms have built integrations on top of the Claude Compliance API, so your team can monitor Claude activity within the tools you already use. Learn more about **[Compliance API integrations](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations)**.

## Audit log events in the Compliance API

The Compliance API now includes audit log events, giving you a full view across all your Claude deployments. To see which events are recorded via audit logs, see **[How to access audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs#h_41cdad187a)**.