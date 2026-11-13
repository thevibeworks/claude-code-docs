# Set up Claude for Teachers for your school or district

**[Claude for Teachers](https://claude.com/solutions/teachers)** is free for verified US K-12 educators through July 30, 2028, whether you sign up as an individual teacher or your school or district sets up an organization for everyone.

This guide explains how an authorized administrator sets up a free Claude Enterprise organization for their teachers and what comes with it. It's written for district technology leaders and school IT staff.

## What you get

Your school staff get the full Enterprise product (Claude on web, desktop, and mobile, plus Claude Code, Cowork, and Claude Design), the K-12 teaching plugin, the Learning Commons connector with state standards, underlying learning components and progressions, and high-quality curricula, and the same usage allowance as an individual Claude for Teachers account, at no cost. Admins choose which features, models, and connectors are enabled.

Your organization gets one set of **[K-12 terms and a data processing agreement](https://support.claude.com/en/articles/15926041-claude-for-teachers-your-data-and-our-terms)** accepted once for everyone, standard Enterprise admin controls (verified domains, SSO, automatic account creation, roles, usage, and the Compliance API), and a way to bring existing teacher accounts on your domain into the organization.

**Note:** Claude for Teachers is for educators, not students. Student accounts aren't part of this offering.

## Who can apply

US K-12 schools and districts qualify. The person applying must be authorized to set up technology for the school or district, and must apply with a school or district email address.

**Important:** Only one application can be open per email domain at a time, so coordinate within your district so the right person applies. This should be an administrator who can accept the K-12 terms on behalf of all district staff. If you have any issues with your application, **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

## Set up your organization

You'll need your school or district email, a document showing your role (such as an employee ID), access to your domain's DNS records, and access to your identity provider.

1. **Apply and accept the K-12 terms**. Go to **[claude.ai/k12districts](https://claude.ai/k12districts)**, confirm you're authorized, and accept the **[US K-12 Terms of Service](https://www.anthropic.com/legal/k12-terms)**, **[US K-12 Public Sector Addendum](https://anthropic.com/legal/k12-addendum),** and **[US K-12 Data Processing Agreement](https://www.anthropic.com/legal/k12-dpa)**.

2. **Verify your school or district.** Our partner Goodstack confirms your affiliation. When approved, you'll get an email link to your new organization.

3. **Verify your email domain**. Add your district's email domain, publish the DNS TXT record shown on the page, and click Verify. Seats open and the free Claude for Teachers plan applies automatically.

4. **Set up SSO and automatic account creation.** Connect your identity provider, turn on Require SSO, turn on just-in-time or SCIM provisioning, and turn on Restrict organization creation so district emails can't create personal Claude accounts. Once automatic account creation is on, email invitations are disabled. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

5. **Bring your teachers in.** Before you start the migration, make sure you have enough seats for everyone you expect to migrate. Your organization starts with a limit of 500 seats. To ask for more, go to **[Organization settings > Members](https://claude.ai/admin-settings/members)** and click "Request more seats." Click "Migrate accounts" using your domains to start a 30-day window. Every existing Claude account on your domain, including individual Claude for Teachers accounts, is notified and chooses to bring what they can, start fresh, or do nothing. Not everything can move. If they do nothing, the account closes at the deadline and will be deleted, along with its data, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**. Ask teachers to export and download their data before the deadline, from **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**. If they can't export, they should **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support#h_d6fc679aa4)** before the deadline. Teachers who join later sign in with SSO and land in your organization directly. For more information, see **[Claim and migrate accounts on your domain](https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain)**. Teachers can read **[Respond to an Enterprise domain claim on your Claude account](https://support.claude.com/en/articles/14625626-respond-to-an-enterprise-domain-claim-on-your-claude-account)**.

## Manage your organization

Your organization comes with the standard Enterprise admin controls, all in **Organization settings**. You can manage members and assign roles that control which features, models, and connectors each teacher can use; require district SSO and provision members through SCIM; verify domains and block personal accounts on them; choose which connectors teachers can reach (none are on by default); set a default model and organization-wide instructions; and track usage.

For the full set of admin articles, see the **[Admin management](https://support.claude.com/en/collections/9811449-admin-management)** collection and **[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)**

## Get help

For setup questions, **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support)**. Districts working with an Anthropic account team can also reach out to their contact for procurement paperwork, security reviews, or multi-organization setups.