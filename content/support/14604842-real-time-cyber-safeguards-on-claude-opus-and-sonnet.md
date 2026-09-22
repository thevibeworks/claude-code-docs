# Real-time cyber safeguards on Claude Opus and Sonnet

**Note**: This article applies only to Opus and Sonnet class models, but doesn’t apply to Claude Opus 5.5. We'll soon be expanding the Cyber Verification Program to include Opus 5.5 and Mythos class models.

As part of our ongoing safety commitments, we have real-time cyber safeguards on Claude Opus and Sonnet models. These safeguards are designed to automatically detect and block requests that may indicate prohibited or high-risk cybersecurity usage based on our Usage Policy.

## How this works

Our cyber safeguards currently block two categories of activities:

- **Prohibited use:** Cybersecurity activities that are almost always used maliciously and have little to no legitimate defensive application such as mass data exfiltration or ransomware code development. These are blocked by default and not subject to adjustment via self-serve application through the Cyber Verification Program.

- **High Risk Dual use:** Cybersecurity activities that have legitimate defensive applications, such as vulnerability exploitation or offensive security tooling development. These are blocked by default, but defensive users can apply for adjustment for legitimate use cases through the Cyber Verification Program described below.

## Cyber Verification Program

Many cybersecurity practitioners do legitimate work that overlaps with the dual use category above. The Cyber Verification Program (CVP) is a free application-based program for **Opus and Sonnet** that is designed to enable professionals to continue working on legitimate dual use tasks safely while minimizing interruption.

If your use case has a legitimate defensive purpose and is being affected by these safeguards, we encourage you to apply for the CVP. See **How to apply** below for the right path based on how you access Claude.

Organizations on Zero Data Retention (ZDR) are not currently eligible to participate in the CVP. If you have a Sales Managed ZDR account, please contact your Anthropic Sales Representative for more information.

## How to apply

How you apply depends on how you access Claude. Once you submit your application, we aim to send an email notification with our review decision within two business days. To submit an application you will need to verify your identity. Please see **[Identity verification on Claude](https://support.claude.com/en/articles/14328960-identity-verification-on-claude)** for more information.

| **How you access Claude**                                                | **How to apply**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Anthropic first-party** (Claude.ai, Claude Code, the Anthropic API)    | Navigate to the **[Verification Portal](https://portal.anthropic.com/programs/cvp)** to apply for access to the Cyber Verification Program.<br>**Note:** Only authorized admins will see this option.                                                                                                                                                                                                                                                                                                                                                 |
| **Microsoft Foundry**                                                    | Find both your Azure Tenant ID and Subscription ID in your Azure Portal (see instructions **[here](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)**). Choose "Azure" under the **Surface** field in the **[Cyber Use Case Form](https://claude.com/form/cyber-use-case)**.                                                                                                                                                                                                                                          |
| **Amazon Bedrock**                                                       | The Cyber Verification Program is not available on Bedrock at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Claude Platform on AWS**                                               | Navigate to the **[Verification Portal](https://portal.anthropic.com/link?account_source=aws&program=cvp)** to apply for access to the Cyber Verification Program. You will need to create or log into an Anthropic account, then link your AWS account.
​<br>**Note:** Only authorized admins will be able to apply.                                                                                                                                                                                                                               |
| **Claude on Google Cloud**                                               | Navigate to the **[Verification Portal](http://portal.anthropic.com/link?account_source=aws&program=cvp)** to apply for access to the Cyber Verification Program. You will need to create or log into an Anthropic account, then **[link your Google account](https://portal.anthropic.com/linked-accounts/gcp/link?from=picker)** and configure data retention. Please see the instructions under the **[Enable data retention on Claude on Google Cloud](#h_c551899218)** section below.<br>**Note:** Only authorized admins will be able to apply. |
| **Third-party platform** (coding tools and other apps powered by Claude) | Reach out to your platform directly to check if Anthropic CVP is available and if so request access to the Cyber Use Case Form through the platform. Not all platforms participate in the CVP at this time.                                                                                                                                                                                                                                                                                                                                           |
| **Bring your own key (BYOK) Customers**                                  | Follow instructions under **Anthropic first-party**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

[Verification Portal](https://portal.anthropic.com/programs/cvp)

**Are you a platform owner?** If you use Claude to power products or services available to your customers and want to learn whether your platform is eligible to participate in the Cyber Verification Program, please **[fill out this Platform CVP Interest Form](https://claude.com/form/platform-cvp-interest)**.

## Enable data retention on Claude on Google Cloud

In order to access the Cyber Verification Program through Claude on Google Cloud, you must consent to and configure data retention.

Consent to the Advanced AI Safety Addendum once per project on the model page. In addition, the calling GCP project must opt in to the correct data retention settings. These are set on Google's **[PublisherModelConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#PublisherModelConfig)**, keyed by project, region, and model.

**Note:** You must update these settings for every project, region, and model combination with which you'd like to use the Cyber Verification Program on Claude on Google Cloud.

| **Setting**                     | **Needed for**                   | **`PublisherModelConfig` field**              |
| ------------------------------- | -------------------------------- | --------------------------------------------- |
| **Data sharing with Anthropic** | Opus 5                           | `dataSharingEnabledProvider: "ANTHROPIC"`     |
| **Advanced AI**                 | Sonnet 5<br>Opus 4.7<br>Opus 4.8 | `claudeFeatureConfig.advancedAiEnabled: true` |

You can find out more about how to set this configuration by reading the **[Google Cloud documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/request-response-logging#share-requests-responses-with-maas-partners)**.

## Appeals

We expect to occasionally decline eligible applications incorrectly, and approved users may still experience blocks on legitimate work. We’re actively working to reduce both.

If you’re encountering one of these issues, we recommend checking the following:

**Are you signed in to the right organization?** CVP approval is tied to a specific organization ID. If you're hitting blocks on a different organization—for example, your personal workspace instead of your team's organization—the approval doesn't carry over. Compare the organization ID where you're seeing blocks against the one on your approval email.

**Is the activity actually dual use?** CVP approval only lifts blocks on dual use activities. Prohibited use activities (e.g., mass data exfiltration, ransomware code development) remain blocked regardless of CVP status.

If you've checked both and still believe something is wrong, you can **[submit a report or appeal form](https://claude.com/form/cyber-block-false-positive-report-cvp-rejection-appeal)**. Your feedback helps us refine these safeguards.