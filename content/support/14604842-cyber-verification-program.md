# Cyber Verification Program

This article explains what the Cyber Verification Program (CVP) is, who can join, how to apply, and how to turn on access after you're approved.

The Cyber Verification Program is available on paid Claude plans (Pro, Max, Ultra, Team, and Enterprise), in Claude Console with billing set up, and through linked cloud accounts and third-party platforms. It isn't available on the Free plan.

**Updated October 6, 2026.** The Cyber Verification Program (CVP) previously covered Claude Opus 5, 4.8, and 4.7, and Sonnet 5 with a single level of access. CVP now offers three access tiers for Claude Mythos, Opus, and Sonnet models starting with Claude Mythos 5.1, Claude Opus 5.5, and Claude Sonnet 5.5.

## Program overview

The Cyber Verification Program lets verified security professionals use our most capable models for advanced security work with fewer interruptions from our cyber safeguards.

You don’t need CVP for everyday secure development. You can use our generally available models to review code, patch known issues, and triage security alerts.

You may need CVP if Claude blocks your security work, such as validating exploits or running authorized penetration tests. Organizations can apply for any tier. Individuals, such as independent researchers, open-source maintainers, and bug bounty hunters, can apply for Defense Access.

Every tier includes Claude Mythos, Opus, and Sonnet models starting with Claude Mythos 5.2, Claude Mythos 5.1, Claude Opus 5.5, and Claude Sonnet 5.5. CVP adjusts the safeguards on these models based on your tier. Our **[Usage Policy](https://www.anthropic.com/legal/aup)** still applies in full.

## Access tiers

Below we share an overview of the three access tiers in the Cyber Verification Program: Defense Access, Red Team Access, and Specialized Access.

| **CVP access tier** | **Defense Access**                                                                                                                                                            | **Red Team Access**                                                                                                   | **Specialized Access**                                                                                                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What you can do** | Security operations, incident response, malware analysis, detection engineering, and vulnerability triage and validation                                                      | Authorized penetration testing, red teaming, adversary emulation, offensive tool development, and exploit development | Authorized pen testing and red teaming of critical infrastructure and research into the highest-severity techniques                                                         |
| **Who it’s for**    | Security teams and other employees who regularly do security work, critical infrastructure operators, open-source maintainers, bug bounty hunters, and individual researchers | Penetration testing firms and in-house red teams whose core work is offensive                                         | Teams whose work requires authorized, high-risk offensive testing of critical systems, such as flight operating systems, power grids, and interbank transfer infrastructure |
| **Who can apply**   | Organizations and individuals                                                                                                                                                 | Organizations only                                                                                                    | Organizations only                                                                                                                                                          |
| **Plans**           | Pro, Max, Ultra, Team, Enterprise, and API                                                                                                                                    | Team, Enterprise, and API                                                                                             | Team, Enterprise, and API                                                                                                                                                   |
| **Approved users**  | No default limit. Individual access covers only you                                                                                                                           | Up to 75                                                                                                              | Up to 25                                                                                                                                                                    |

We prohibit some activity in every tier, including:

- Mass destruction of data or devices

- Denial-of-service attacks

- Physical-world damage

- Extortion

- Election interference

- Any request with stated malicious intent

Defense Access suits most critical infrastructure operators. Operating critical infrastructure doesn’t by itself qualify organizations for Specialized Access.

**Note:** You may experience some model refusals and classifier blocks for allowed security work as we continue to refine our safeguards and reduce false positives for approved work across tiers.

## Availability

| **How you access Claude**               | **Tiers available**                | **What to know**                                                                                                        |
| --------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Pro, Max, and Ultra plans               | Defense                            | For individuals                                                                                                         |
| Team plans                              | All                                | Access applies to every user, so Red Team Access is limited to 75 seats, and Specialized Access is limited to 25 seats. |
| Enterprise plans                        | All                                | Your admin assigns access by role                                                                                       |
| Claude Console (API)                    | All                                | Your admin assigns access by workspace                                                                                  |
| Claude Platform on AWS                  | All                                | Link your account before you apply                                                                                      |
| Claude Platform on Google Cloud         | All                                | Link your project before you apply                                                                                      |
| Google Cloud Agent Platform             | All                                | Link your project before you apply                                                                                      |
| Microsoft Foundry                       | All                                | Deploy a Claude model, then link your subscription before you apply                                                     |
| Amazon Bedrock                          | All                                | Requires Enterprise Frontier Safeguards (see **Why is access on Amazon Bedrock limited?**)                              |
| Third-party platforms powered by Claude | Defense Access and Red Team Access | Reach out to your platform to link your account and apply for access                                                    |

## Data retention

Data retention is required for everyone enrolled in the program so that we can help monitor and mitigate cyber misuse. If your organization has a data retention exemption for Claude Fable or Claude Mythos models, you can use CVP with zero data retention (ZDR) on all models in the program for internal use.

Once Enterprise Frontier Safeguards (EFS) is generally available, eligible organizations can store data in cloud infrastructure they control. **[Register your interest in EFS](https://claude.com/form/enterprise-frontier-safeguards)**.

## Prepare your application

By default, CVP is only allowed for internal use. A separate application is required for external use:

- **Internal use:** Security work on your own organization’s code, products, and infrastructure. This also includes bug bounty research and coordinated disclosure that you do independently, within the program’s rules, rather than for a client. Every approved tier covers this.

- **External use:** Security work for your customers, or a product they use. This needs a separate approval after you join CVP and are approved for internal use.

### Internal use: what to prepare

#### All tiers

- **The right account.** Make sure you're applying from the organization where you'll use CVP. Approval doesn't carry over to your other organizations. Your Claude and Claude Console accounts are separate organizations.

- **Your email address.** If you're applying as an organization, use an account with your organization's email domain, if applicable. You can't change your account's email address later, so be sure to use the correct email when creating an account.

- **One application.** Submit one application per organization. An Owner or Primary Owner for Claude accounts, or an Admin for Claude Console accounts must submit your organization’s application. Other users in your organization shouldn’t apply separately.

- **Verification details.** Have information ready about your organization and the person applying. Learn more about **[identity verification on Claude](https://support.claude.com/en/articles/14328960-identity-verification-on-claude)**.

  - If you're verifying as an individual, have these ready:

    - **A valid government-issued photo ID**: the physical document such as a passport, driver's license, state/provincial ID card, or national identity card (not photocopies)

    - **A phone with a camera**: you may be asked to take a live selfie with your phone.

  - If you're verifying on behalf of an organization, you also need:

    - **Identifying information about your organization:** legal name, address, and business registration number

- **Your security work.** Describe what your team does and how you’ll use Claude.

#### Additional items to prepare by tier

**Defense Access**

Ensure your organization can attest it has the following security controls in place: multi-factor authentication (MFA) and API keys replaced at least every seven days.

**Important:** Starting December 15, 2026, Defense Access also requires phishing-resistant MFA and no longer allows static or long-lived API keys. We recommend that you move to **[Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation)** now.

You’ll complete identity verification (business verification for organizations), describe your security work, and accept the terms.

**Red Team Access**

Ensure your organization can attest it has the following security controls in place: phishing-resistant MFA, API keys replaced at least every seven days, company-domain accounts, organization-controlled devices, outbound network controls, and background checks.

Then, find the row that describes your situation, and prepare the relevant information. Matching a row doesn’t guarantee approval.

**Note:** If your organization relies on outside testers, the testing firm should apply to the program.

| **If you’re applying as**                          | **Have this ready**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| An in-house red team                               | All of the following:<br>     Proof of your organization’s security program, including:<br><br>The cybersecurity section of your latest annual report, a current ISO/IEC 27001 certificate or SOC 2 Type II report, or a paid bug bounty program that has run for at least 12 months. Critical infrastructure operators can also use a sector security obligation.<br>The name of your testing team, its lead, and its approximate headcount

<br>Confirmation that each test is authorized in advance by someone with authority over the systems<br>One of the following:<br><br>Team members with offensive security certifications, such as OSCP, GPEN, or CREST Registered Tester<br>Public evidence of the team’s work, such as research or conference talks<br>A redacted internal test report

<br>Critical infrastructure operators also need their sector registry listing |
| A cybersecurity or penetration testing firm        | One of the following, in your firm’s own name:<br>CVE Numbering Authority listing<br>Full membership in the Forum of Incident Response and Security Teams (FIRST)<br>A recent CVE credit<br>A testing accreditation such as CREST, CHECK, or FedRAMP 3PAO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| A smaller testing firm without one of those proofs | All of the following:<br>     Business registration at least one year old<br>Public information about your testing services<br>At least two testers with offensive security certifications<br>A redacted statement of work, test report, or client reference from the last 12 months                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| A government red team                              | All of the following:<br>     The name of your testing team, its lead, and its approximate headcount<br>Confirmation that each test is authorized in advance by someone with authority over the systems<br>One of the following:<br><br>Team members with offensive security certifications, such as OSCP, GPEN, or CREST Registered Tester<br>Public evidence of the team’s work, such as research or conference talks<br>A redacted internal test report                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Specialized Access**

We review every Specialized Access application in depth in collaboration with the US government. This tier is for organizations specifically focusing on red teaming systemically important infrastructure. Most critical infrastructure organizations working on defense do not need Specialized Access. To qualify, you'll need to show that you're authorized to test these types of systems and detail the activities you can't accomplish in the Red Team Access tier.

If you're applying for Specialized Access, ensure your organization can attest it has the following security controls in place: phishing-resistant MFA, API keys replaced at least every seven days, company-domain accounts, organization-controlled devices, outbound network controls, and background checks, plus single sign-on and managed devices with malware protection.

#### Evidence that speeds up your review

- Link to sources we can check independently, such as a public registry, certification directory, or issuer page. Upload the full, dated document if there’s no public link. A LinkedIn profile or a screenshot usually isn’t enough. Your own website works for some items, such as a public trust center page listing your certificate or a page describing your testing services.

- Make sure the name on your evidence matches the organization or person we’re verifying.

- Check that every link works and is publicly visible, including bug bounty profiles.

### External use: what to prepare

Each service or product you offer needs its own approval. You can apply once your organization is approved for a CVP tier.

| **Type**                  | **What it means**                                                                                                                                                                     | **Status**             | **What to have ready**                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Managed service**       | Your staff use Claude to do security work for a customer. The customer receives only finished deliverables reviewed by your staff and never prompts the model or sees its raw output. | Accepting applications | How the service runs, who operates the model, and what customers receive<br>A security contact, plus the name and title of the company officer who signs off |
| **Constrained product**   | Customers use something you built but can’t direct the model or see its raw output.                                                                                                   | Express interest       | N/A                                                                                                                                                          |
| **Unconstrained product** | Any other customer-facing product, such as one where customers can prompt the model.                                                                                                  | Express interest       | N/A                                                                                                                                                          |

**Important:** Serving customers through a service or product without explicit approval is a violation of the CVP terms and grounds for removal from the program.

## How to apply

Apply in the **[Verification Portal](https://portal.anthropic.com/programs)**. The portal walks you through verification, your tier, any evidence your tier needs, and the program terms.

You'll verify as a business or an individual. Choose carefully, because the type of verification affects your application:

- **Business**: You're applying for a company, nonprofit, university, government team, or other organization. For Red Team or Specialized Access, you must apply from an account on a Team, Enterprise, or API plan.

- **Individual**: You're applying for yourself, such as an independent researcher, open-source maintainer, or bug bounty hunter. Individuals can apply only for Defense Access. You can apply for Defense Access with a Pro, Max, Ultra, Team, Enterprise, or API plan.

### Apply with an Anthropic account

If you use Claude, Claude Code, or the Claude API directly through Anthropic, follow these steps:

1. Sign in to the **[Verification Portal](https://portal.anthropic.com/programs)** with your Anthropic account. If you don't have one yet, create a new one and set up billing.

2. Choose “Cyber Verification Program” from the list of programs.

3. Click “Apply” and complete the application.

4. Accept the terms and submit.

### Apply with a cloud account

If you use Claude Platform on AWS, Claude Platform on Google Cloud, Google Cloud Agent Platform, Amazon Bedrock (if eligible for EFS), or Microsoft Foundry, follow these steps:

1. Sign in to the **[Verification Portal](https://portal.anthropic.com/programs)** with your Anthropic account, or sign up if you don't have one.

2. You'll be prompted to link your Cloud Service Provider account with a CLI command, to verify that you are an admin. You can link up to 10 GCP projects or AWS accounts.

3. Open **Programs** and choose “Cyber Verification Program” from the list of programs.

4. Click “Apply” and complete the application.

5. Accept the terms and submit.

Then, follow these steps with your cloud provider account:

1. Sign in to the Verification Portal for **[AWS](https://portal.anthropic.com/link?account_source=aws&program=cvp)**, **[Google Cloud](https://portal.anthropic.com/link?account_source=gcp&program=cvp)**, or **[Azure](https://portal.anthropic.com/programs)**. If you don’t have an Anthropic account, create one. It’s free and doesn’t require billing information, but you can’t apply until you link a cloud account or buy Claude Console credits.

2. Open **[Linked accounts](https://portal.anthropic.com/linked-accounts)**, select “Link account,” and choose your provider.

3. Enter your account details and complete the setup step for your provider:

  1. **AWS:**

    1. **What to enter:** 12-digit account ID

    2. **Setup step:** Create the verification role using the portal’s launch link or command. Link Claude Platform on AWS before Bedrock.

  2. **Google Cloud:**

    1. **What to enter:** Project ID (not the project number)

    2. **Setup step:** Run the `gcloud` command shown.

  3. **Azure:**

    1. **What to enter:** Subscription ID and directory (tenant) ID

    2. **Setup step:** Deploy a Claude model in Foundry first, then run the commands shown.

4. Select “I’ve granted access,” then “Verify.”

5. Choose “Cyber Verification Program,” and click “Apply" from the Programs page.

### Apply through a third-party platform

1. Ask your platform for an Anthropic enrollment link.

2. Open the link, sign in to the Verification Portal or create an account, and confirm that you would like your account linked.

3. Choose “Cyber Verification Program,” and click “Apply” from the Programs page.

### Apply for external use

You must be an Owner or Primary Owner of a Claude account or an Admin of a Claude Console account that’s approved for CVP. Then you can:

1. Open **[Cyber productization](https://portal.anthropic.com/programs/cyber-productization)** in the Verification Portal.

2. Select “Register an offering” and choose your type.

3. For a managed service, complete the form, accept the Anthropic Cyber Defender Partner Addendum, and select “Submit for Review.” For a product, describe it in one line, add a name and email, and select “Express interest.”

**Note:** You can’t edit or withdraw this application after you submit it. Repeat these steps for each additional service or product.

## What to expect after you apply

### When you’ll hear back

We’ll email you with a decision or a request for more information. To check your status, sign in to the Verification Portal, open Programs, and choose "Cyber Verification Program." If your review takes longer than the target, you don't need to reapply or contact support.

| **Application**    | **Target**                                                                                                                                           |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Defense Access     | Two days                                                                                                                                             |
| Red Team Access    | Two weeks. Reviews are currently taking longer because of high demand.                                                                               |
| Specialized Access | No set target. These reviews take longer than Red Team Access because we review every organization in depth in collaboration with the US government. |
| Managed service    | About one week                                                                                                                                       |

If you apply for Red Team Access or Specialized Access and qualify for a lower tier, you will receive access to the lower tier while we review the rest of your application.

### If you’re not approved

You can keep using our generally available models, along with any tier you did get approved for.

You also can reapply after seven days**.** This is the best option if something has changed or you can provide stronger evidence to support your application. Check that you’re applying from the right account and completed the right kind of verification, business or individual.

We may review, narrow, or withdraw program access at any time in our sole discretion if we see activity that violates our policies.

## What to do after you’re approved

### 1. Turn on access

**Important:** On most products, approval doesn’t "turn on" CVP. Your admin needs to assign the program to the proper roles and workspaces first.

| **How you access Claude**                                                      | **What to do**                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pro, Max, Ultra, and Team plans                                                | Nothing. Access turns on automatically, and on Team plans it applies to every user. Red Team Access and Specialized Access stay off on a Team plan that's over the tier’s seat limit.                                                          |
| Enterprise plans                                                               | Assign the program to a custom role (see **Claude Console** below)                                                                                                                                                                             |
| Claude Console (API)                                                           | Assign the program to a workspace (see **Claude Enterprise** below)                                                                                                                                                                            |
| Claude Platform on AWS, Claude Platform on Google Cloud, and Microsoft Foundry | Log into Verification Portal, then open the Cyber Verification program page. Under "Access on linked accounts" turn on the tier. If you want to add additional accounts, link them through the Verification Portal.                            |
| Amazon Bedrock                                                                 | Requires Enterprise Frontier Safeguards (EFS) once it's available. When EFS is available, link your account, then open the Cyber Verification Program page in the Verification Portal. Under **Access on linked accounts**, turn on your tier. |
| Google Cloud Agent Platform                                                    | Link your project, turn on your tier, and set up data sharing.<br>Link your account, then open the Cyber Verification Program page in the Verification Portal. Under **Access on linked accounts**, turn on your tier.                         |
| Third-party platforms                                                          | Open the Cyber Verification Program page in the Verification Portal. Under **Access on linked accounts**, turn on your tier for that platform.                                                                                                 |

**Claude Console**

To turn on access to CVP in Claude Console:

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization admin. You'll have the option to either create a new **[workspace](https://platform.claude.com/settings/workspaces)** or assign CVP access to one you already have. **Note:** You can't assign it to the default workspace.

2. Add only users that should get access to the advanced cyber capabilities to the workspace. For Red Team Access and Specialized Access, the Console shows how many seats you're using. Every organization admin counts as a seat. If you go over your tier’s limit, every workspace loses CVP access until you’re back within it.

3. Open the **[Programs page](https://platform.claude.com/settings/programs)** and select the card for your tier, such as “Defense Access.”

4. In the **Workspaces** table, turn on the **Access** switch for your workspace.

5. If a cell in the workspace’s row says “Not set,” “Not met,” or “Allowed,” select it and follow the fix. Until December 15, 2026, Defense Access allows only API keys that expire within seven days. After that date, it doesn’t allow API keys. Red Team Access and Specialized Access need API keys turned off.

6. Check the page’s count of active workspaces, such as “1 of 2 workspaces active.” A workspace stays inactive until it meets the requirements.

For details, see **[assign a program to workspaces](https://support.claude.com/en/articles/16764810)**.

**Claude Enterprise**

To turn on access to CVP in Claude Enterprise:

1. Sign in as an Owner or Primary Owner.

2. Go to **Organization settings > Roles** and add or edit a custom role.

3. Select the **Details** tab, then choose the groups that need access.

4. Select the **Models** tab, then choose the grant under **Grants** and save.

5. Confirm that your approved users have the **Custom** role type. Built-in roles aren’t covered.

For details, see **[assign a program to a custom role](https://support.claude.com/en/articles/17118092).**

**Google Cloud Agent Platform**

To turn on access to CVP in Google Cloud Agent Platform, repeat these steps for each project:

1. In the Verification Portal, open your linked project. Under **Programs**, turn on your tier.

2. In **Model Garden**, open the Claude model and accept the Advanced AI Safety Addendum.

3. Turn on data sharing for each model and location you use. Set `dataSharingEnabledProvider` to `ANTHROPIC` with Google’s `setPublisherModelConfig` API.

**Claude Mythos on cloud providers**

Access to Mythos on cloud partners starts about five business days after you’re approved for CVP. If you have a committed contract with Anthropic, your account team will send you a short form. Complete it, then accept the private offer in your cloud marketplace. We’ll provision Mythos once both steps are done.

### 2. Give each team the right tier

If you’re approved for more than one tier, treat each grant like any other privileged access. Keep each grant in its own workspace, role, or cloud account.

- **Specialized Access:** The small group whose work is still blocked in Red Team Access

- **Red Team Access:** red teamers, penetration testers, and offensive security researchers

- **Defense Access:** the rest of your security team, plus developers and other employees who do security or security-adjacent work

- **No grant:** everyone else

## Frequently asked questions

### I’m approved. Why am I still blocked?

Ask your admin to confirm they’ve assigned you access. If you use Claude Console, check that you’re in the workspace with the program applied. Then check that the work falls within your tier.

### I have Defense Access. Can I apply for a higher tier?

Yes, if you applied as an organization. You’ll keep Defense Access while we review your application.

### Can different parts of my company have different tiers?

Yes. Each Claude organization needs its own application. Within one organization, you can assign programs by workspace (Console) or role (Enterprise). Team plans can’t split access between users.

### I work at a security firm. Does my tier cover work for clients?

Not by itself. You need a CVP tier and approval for external use, usually as a managed service.

### Can I use CVP internally if another workspace serves customers?

In Claude Console, yes. CVP applies only to the workspaces you assign it to, and it can’t be the Default workspace. Assign it to a workspace used only for internal work, and keep customer traffic in a separate workspace without CVP. To use CVP for customer traffic, you need approval for external use.

On Team plans, access applies to your whole organization, so you can’t limit it to internal work. Don’t serve customers from an organization with CVP access until we’ve approved that service or product for external use.

### Why is access on Amazon Bedrock limited?

Bedrock doesn’t yet support human review of automated safety flags, which CVP requires by default. For now, CVP on Bedrock is available only to organizations with a data retention exemption. Once Enterprise Frontier Safeguards (EFS) is available, Bedrock organization in the EFS program can apply for CVP access. To register your interest in EFS, use this **[Enterprise Frontier Safeguards form](https://claude.com/form/enterprise-frontier-safeguards)**. In the interim, we're working to expand CVP to Bedrock customers. Contact your account team to ask about an exemption.

### How do usage limits work for Claude Mythos models?

Mythos models follow the same usage rules as Claude Fable models.

- **Pro plan:** Mythos models are available only with usage credits.

- **Max and Ultra plans:** Mythos and Fable models share up to 50% of your weekly usage limit. This usage also counts toward your regular usage limits. After that, you can continue with usage credits, if they’re turned on, or switch to another model.

### Can I download a copy of my application?

Yes. You can download your application and terms as a PDF from the program page in the Verification Portal.

### Can I add more people after I’m approved?

Yes. You don’t need to reapply. Your admin adds them to the workspace (Console) or custom role (Enterprise) that has the program, up to your tier’s limit. For Red Team Access and Specialized Access, you can add only people on the team named in your application. Everyone you add must meet your tier’s security requirements.

### Can I add another cloud account after I’m approved?

Yes. Link the new account to the same Anthropic organization in the Verification Portal. You don’t need a new application. On Amazon Bedrock and Google Cloud Agent Platform, you also need to turn on your tier for the new account.

### Does CVP change safeguards outside of cybersecurity?

No. CVP adjusts only our cyber safeguards. Our safeguards from other domains like research biology still apply in every tier. Our **[Usage Policy](https://www.anthropic.com/legal/aup)** still applies in full.

### Can I change or cancel my application after I submit it?

No. You can review and edit your answers until you submit, but you can’t edit or cancel an application after that. If you’re not approved, you can reapply after seven days.

### I was approved on the wrong organization. What should I do?

Apply again from the organization where you’ll use CVP, or ask your account team for help.