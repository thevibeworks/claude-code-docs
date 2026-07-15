# What are customer-managed encryption keys \(CMEK\)?

Customer-managed encryption keys are available to eligible organizations on Enterprise plans and the Claude Platform.

A customer-managed encryption key (CMEK) lets your organization provision an encryption key in your own AWS KMS, Google Cloud KMS, or Azure Key Vault and have Anthropic use it to encrypt certain data in Claude, such as your team's chats, projects, and files. You keep full control of the key, and every operation Anthropic performs with your key is recorded in your cloud provider's audit logs. CMEK is optional, and your organization can choose to enable it in place of the default encryption Anthropic provides.

For complete details, including what's encrypted, what's disabled or changed, limitations, and setup guides for each cloud provider, see **[Customer-managed encryption keys on Claude API Docs](https://platform.claude.com/docs/en/manage-claude/cmek)**.