Title: Set up SCIM in Claude for Government

URL Source: https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government

Markdown Content:
System for Cross-domain Identity Management (SCIM) lets your identity provider automatically manage user accounts in Claude for Government. With SCIM, your IdP controls who has access, what role they hold, and what seat tier they're assigned—without manual intervention in the Claude admin console.

## How SCIM differs for Claude for Government

Claude for Government uses a first-party SCIM implementation hosted within the FedRAMP-authorized environment. The commercial Claude Enterprise plan uses a different SCIM backend.

**Feature****Claude for Government****Claude Enterprise**
SCIM endpoint claude.fedstart.com/v1/scim/v2 Configured via claude.ai
SCIM implementation Anthropic first-party (FedRAMP-authorized)Third-party integration
API key management Self-service via identity settings page Self-service via admin settings
Parent Organization Support Yes — for multi-org identity management Not applicable

## Prerequisites

Before setting up SCIM, you must complete:

## How provisioning works with and without SCIM

Without SCIM, Claude for Government uses just-in-time (JIT) provisioning: any user who authenticates through SSO is automatically assigned a seat, as long as licenses are available. You control who can authenticate by managing membership in the SAML application within your IdP.

With SCIM, login and provisioning are separate. Your IdP tells Anthropic who should have access and at what role/tier. SSO is used only for authentication. This gives you fine-grained control over roles, seat tiers, and offboarding.

### Step 1: Generate a SCIM API key

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040196/c3b045028c4c2edef9172b6fb424/9a71258e-ae73-41e3-83a2-d24a240ac0ae?expires=1781156700&signature=288f83328789862ebe4b9652d9d6e43c54cc51f5f7c2eeaa47047556e8ed4cbc&req=diIiEMl6nYBWX%2FMW1HO4zSrRla0ebDATyIvvU1hav7Nl8glpnso4KenwxeYC%0AliuDAiVCPNW2KcgrfuQ%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040196/c3b045028c4c2edef9172b6fb424/9a71258e-ae73-41e3-83a2-d24a240ac0ae?expires=1781156700&signature=288f83328789862ebe4b9652d9d6e43c54cc51f5f7c2eeaa47047556e8ed4cbc&req=diIiEMl6nYBWX%2FMW1HO4zSrRla0ebDATyIvvU1hav7Nl8glpnso4KenwxeYC%0AliuDAiVCPNW2KcgrfuQ%3D%0A)

### Step 2: Configure SCIM in your Identity Provider

### Step 3: Verify sync status

After enabling the integration in your IdP:

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040198/da9188b8b968d5f900cc08e9ceb2/3814ab37-c3fa-4256-8d16-49c1e1b4c654?expires=1781156700&signature=5fb20c4886122f70d8dd95282c7256ff43b47aaa81e4156794cedc345ad0b351&req=diIiEMl6nYBWUfMW1HO4zeLvMlluT0r9oWupW8zJgMosMK3Liz9z4f1NKOXD%0AzscF7AMU8hJaQniKH4A%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040198/da9188b8b968d5f900cc08e9ceb2/3814ab37-c3fa-4256-8d16-49c1e1b4c654?expires=1781156700&signature=5fb20c4886122f70d8dd95282c7256ff43b47aaa81e4156794cedc345ad0b351&req=diIiEMl6nYBWUfMW1HO4zeLvMlluT0r9oWupW8zJgMosMK3Liz9z4f1NKOXD%0AzscF7AMU8hJaQniKH4A%3D%0A)

### Step 4: Map groups to roles and seat tiers

SCIM provisioning uses IdP groups to assign roles and seat tiers within Claude for Government.

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256056441/f7eb09bba549e9861fc81b961cc7/2760fa5b-87bb-491f-9354-ca3cd2bc4475?expires=1781156700&signature=3e4f19897ad7973e55c1f9bcdaf7551a8d059c7506e0a1488b88a498fb0415aa&req=diIiEMl7m4VbWPMW1HO4zaWhsXIjt0Ech340B79BYGYe%2FBD3UsS4uYmST4CX%0AM%2BFq46GVuTPut4EYvj8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256056441/f7eb09bba549e9861fc81b961cc7/2760fa5b-87bb-491f-9354-ca3cd2bc4475?expires=1781156700&signature=3e4f19897ad7973e55c1f9bcdaf7551a8d059c7506e0a1488b88a498fb0415aa&req=diIiEMl7m4VbWPMW1HO4zaWhsXIjt0Ech340B79BYGYe%2FBD3UsS4uYmST4CX%0AM%2BFq46GVuTPut4EYvj8%3D%0A)

If you manage multiple organizations under a single parent (see below), each organization maintains its own role and seat tier mappings. Switch between organizations using the organization selector in the bottom-left corner of the page.

### Parent organizations (multi-org setups)

Every Claude for Government organization belongs to a **parent organization**. For most customers, this is transparent—a parent is created automatically during provisioning and contains a single child organization.

Parent organizations become relevant when multiple organizations share a login domain. Common scenarios include:

In a multi-org setup:

* * *

Related Articles

[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)[Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
