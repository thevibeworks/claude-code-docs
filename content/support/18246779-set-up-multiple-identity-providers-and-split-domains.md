# Set up multiple identity providers and split domains

If your parent organization is enrolled in centralized management, you can connect more than one identity provider and route one domain through several of them. This article explains when to use each option, how to set them up, and what happens when you remove an identity provider.

Multiple identity providers and split domains are available in beta for parent organizations enrolled in centralized management, on Enterprise plans and Claude Platform. Learn more about **[getting started with centralized management](https://support.claude.com/en/articles/18232924)**.

---

## Connect multiple identity providers

You can connect more than one identity provider to the parent organization, each with its own SSO and directory sync. An identity provider is one SSO application in your identity service, with its SCIM provisioning if you use directory sync. For example, this can be an enterprise application in Microsoft Entra ID or an app integration in Okta. Two SSO applications are two identity providers, even in the same tenant.

Each identity provider has at most one directory, which is the users and groups it syncs through SCIM. Users sign in through their email domain’s identity provider, and users who can use more than one choose when they sign in.

Parent owners and admins manage identity providers and domains. Child organization admins keep the group-to-role mappings for their own organization, choose which identity provider each mapping applies to, and see which identity provider each synced group came from.

### When to use multiple identity providers

For example, Northwind Traders, a fictional parent organization, might connect a second identity provider:

- **To test changes:** Okta Preview for northwind-sandbox.com, so admins can try changes without touching sign-in for northwind.com.

- **For an acquired company that keeps its identity provider:** Contoso Partners signs in through Microsoft Entra on contoso-partners.com, while northwind.com signs in through Okta.

- **To move to a new identity provider in stages:** Connect the new one alongside the old one, move each domain when it’s ready, then delete the old one.

### Set up an identity provider

1. On the **Identity providers** tab, select “Add identity provider” and give it a distinct name that your users will recognize, for example “Microsoft Entra” or “SubsidiaryCo Okta”. When users at a domain can choose between two or more identity providers, the sign-in page can show this name to anyone who knows the domain, even without an account.

2. Open the new identity provider and select “Configure SSO”. In the setup portal, connect your SAML or OIDC application.

3. If you use directory sync, select “Set up directory sync” and connect SCIM in the setup portal.

4. On the **Domains** page, verify the domain if needed, then select the pencil icon in the **SSO sign-in at** column.

5. Clear the identity provider the domain uses now, if any, select the new one, and select “Save”. Sign-in changes for everyone on that domain as soon as you save.

6. For each domain, turn on **Require SSO for Claude** and **Require SSO for Console** as needed. A domain that requires SSO but has no identity provider blocks its users from signing in.

7. In each child organization’s admin settings, under **User provisioning**, choose SCIM directory sync or just-in-time (JIT) provisioning, and turn on **Enable group mappings**.

8. Select + on a role, then assign a group and choose its identity provider. Seat-tier mappings, available for Claude Enterprise organizations only, work the same way.

### How identity providers affect users and groups

- Until group availability is available, every Enterprise child organization admin can see every synced group from every identity provider under the parent, including groups from a test identity provider.

- A person is identified by their email address, so the same email address in two directories is one person. That person gets the highest matching role in the mappings table, whichever directory grants it. Removing them from one directory doesn’t remove a role that the other directory still grants.

- With JIT provisioning, a person’s role comes from the mappings of the identity provider they last signed in through.

- To rename an identity provider, open its page and select the pencil icon next to its name.

### Remove or turn off an identity provider

When you delete an identity provider:

- Its domain routing and group-to-role mappings are removed, and its directory is disconnected.

- Its domains keep their Require SSO settings, unless it was the last identity provider with SSO connected. Users on a domain that requires SSO and has no other identity provider with SSO set up can’t sign in until you route that domain to another one.

- Users who were members only through its directory are removed at the next sync of a remaining directory.

When you turn off SSO for an identity provider in the setup portal, Require SSO turns off on the domains that route to it and to no other identity provider with SSO set up. Users on those domains can then sign in without SSO.

When you remove the last connected SSO or the last connected directory, either by deleting its identity provider (when another remains) or by turning it off:

- If it was the last SSO, Require SSO turns off on every domain of the parent organization.

- Child organizations that used directory sync for provisioning switch to invite-only provisioning, where admins add users by invitation. If it was the last SSO, organizations that used JIT provisioning switch too.

- Connecting a directory later doesn’t switch provisioning modes back automatically. A child organization admin must choose SCIM directory sync or JIT again in their organization’s admin settings.

**Note:** You can’t delete the parent organization’s only identity provider. You can turn off its SSO or directory sync instead.

---

## Use split domains

A verified domain can sign in through more than one identity provider, and you can choose who sees each identity provider on the sign-in page. Split domains change sign-in only. They don’t separate data or decide which child organization someone lands in.

### When to use split domains

For example, Northwind Traders might use split domains for:

- **One domain, two regions:** Everyone uses northwind.com. Staff in the US sign in through Okta and staff in Europe through Microsoft Entra. With each identity provider set to “Only people in its SCIM directory”, users see only their own.

- **Testing a new identity provider before rollout:** Add it to northwind.com set to “Hidden at sign-in”, test sign-in from its tile in your identity provider’s app dashboard, then show it and remove the old one.

### Set up split domains

Before you start, make sure every organization under the parent uses SCIM directory sync or invite-only provisioning, not JIT provisioning. A domain can’t get a second identity provider while any organization uses JIT, or while Microsoft Login is turned on for that domain. To turn off Microsoft Login, or to talk about split domains with JIT provisioning, contact your account team.

1. Add each identity provider, and connect its SSO and directory sync, using steps 1 to 3 of **Set up an identity provider**. Give each one a name your users will recognize, such as “Okta (US)”.

2. On the new identity provider’s page, under **Single sign-on**, choose who can sign in with it and whether it’s shown on the sign-in page. Do this before you add it to a domain, so it’s set up the way you want as soon as users at that domain can use it.

3. On the **Domains** page, select the pencil icon in the **SSO sign-in at** column.

4. Select each identity provider the domain should sign in through, clear any it should stop using, and select “Save”.

5. Map its groups to roles in each child organization, using steps 7 and 8 of **Set up an identity provider**.

### What users see at sign-in

When two or more of a domain’s identity providers are offered to someone, they see “Choose your identity provider” after entering their email address on claude.ai, platform.claude.com, or admin.claude.com, with one button for each, labeled with its name. Claude Desktop and Claude Mobile show the same choice. Someone who is offered only one identity provider goes straight to it.

### Choose who sees an identity provider

Two settings on each identity provider’s page, under **Single sign-on**, control this.

**Who can sign in with this identity provider?**

- **Everyone at its domains:** The default.

- **Only people in its SCIM directory:** Only the people its directory lists as active can sign in with it, plus your parent organization owners and the primary owner of each organization under the parent, so owners can’t lock themselves out. Parent organization admins aren’t exempt. This option needs directory sync set up for that identity provider.

A person’s email address in Claude must be the one their directory lists. Letter case doesn’t matter, but another alias for the same mailbox, such as j.doe@ for jane.doe@, doesn’t match.

People the directory doesn’t list don’t see the identity provider when they enter their email address. They can still reach it from its tile in your identity provider’s app dashboard, or from Claude Desktop’s one-click sign-in, which is set with the loginSsoOrgDomain device management (MDM) setting and doesn’t check the directory. Either way, they’re refused after signing in, on a page that says “Access managed by your organization”. To ask for a setting that names one identity provider, contact your account team.

**Show this identity provider on the sign-in page?**

**Hidden at sign-in** removes the identity provider from every sign-in page, as soon as you select it. Users can still sign in from its tile in your identity provider’s app dashboard, if your identity provider shows one. Claude then asks them to confirm their email address.

### Things to keep in mind with split domains

- **Identity provider names are public:** When users at a domain can choose between two or more identity providers at sign-in, anyone who knows the domain can see their names, even without an account. With “Only people in its SCIM directory” on, anyone can also tell whether an email address belongs to that directory by typing it on the sign-in page.

- **Require SSO:** On a domain that requires SSO, someone who is offered no identity provider on the sign-in page can’t sign in with email or Google either. If they should have access, add them to the identity provider’s SCIM directory, or set it back to “Everyone at its domains”. Don’t hide every identity provider on such a domain unless everyone signs in from your identity provider’s app dashboard.

- **JIT provisioning:** While a domain has more than one identity provider, an organization can’t switch to JIT, or join the parent with JIT on.