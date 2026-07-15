# Restrict access to Claude with IP allowlisting

IP allowlisting is available for Enterprise plans only.

IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization. This feature ensures that requests can only be made from approved network locations, providing an additional layer of security.

When enabled, we validate the source IP address of every authenticated request against your organization's configured allowlist. Requests from IP addresses not added to the allowlist will be blocked.

IP allowlisting supports CIDR ranges. For example: `10.0.0.0/8, 2001:db8::/32`.

## How to configure IP allowlisting

If your Enterprise organization is interested in enabling an IP allowlist, please compile a list of all necessary CIDR ranges for your organization, including office locations, VPN exit points, and any other approved access points. Omitting required CIDR ranges could result in users getting locked out of Claude. Then, reach out to your Anthropic Contact or our [Sales team](https://claude.com/contact-sales) to share your list of CIDR ranges. They can add these to your account’s allowlist to enable the feature.

When a request originates from an IP address that’s not in your allowlist, access is denied. Users should contact their IT administrator if they believe they're being blocked in error.