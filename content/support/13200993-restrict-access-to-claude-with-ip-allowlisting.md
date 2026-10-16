# Restrict access to Claude with IP allowlisting

IP allowlisting is available for Enterprise plans only.

IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization. This feature ensures that requests can only be made from approved network locations, providing an additional layer of security.

When enabled, we validate the source IP address of every authenticated request against your organization's configured allowlist. Requests from IP addresses not added to the allowlist will be blocked.

IP allowlisting supports CIDR ranges. For example: `10.0.0.0/8, 2001:db8::/32`.

## What IP allowlisting covers

When IP allowlisting is on, the following are only available from your allowlisted IP addresses:

- Chats and projects

- Artifacts, including Claude Docs and other artifact types

- Artifact links shared within your organization

- Live editing and collaboration in Claude Docs

- Access to Claude Docs from connected tools

If someone in your organization opens an artifact from an IP address that isn't on your allowlist, they see an access-denied message instead of the content.

**Important:** Artifacts shared outside your organization aren't limited by your allowlist. To keep artifacts behind your allowlist, turn off **External sharing** and **Email invitations outside your organization** in **Organization settings > Artifacts**. Artifacts you've allowed for external sharing individually stay available outside your allowlist. Learn more about **[managing sharing outside your organization](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans#h_fd0c095985)**.

## How to configure IP allowlisting

If your Enterprise organization is interested in enabling an IP allowlist, please compile a list of all necessary CIDR ranges for your organization, including office locations, VPN exit points, and any other approved access points. Omitting required CIDR ranges could result in users getting locked out of Claude. Then, reach out to your Anthropic Contact or our **[Support team](https://support.claude.com/en/articles/9015913)** to share your list of CIDR ranges. They can add these to your account’s allowlist to enable the feature.

When a request originates from an IP address that’s not in your allowlist, access is denied. Users should contact their IT administrator if they believe they're being blocked in error.