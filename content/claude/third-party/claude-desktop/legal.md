> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Legal and compliance

> Legal agreements, compliance, and security information for Claude Desktop on 3P

## Legal agreements

### License

Your use of the Claude Desktop application, including in Claude Desktop on third-party (3P) mode, is subject to Anthropic's [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).

### Commercial agreements

Claude Desktop on 3P routes model inference through the provider you configure (Google Cloud's Agent Platform, Amazon Bedrock, Microsoft Foundry, a compatible gateway, or the Anthropic API directly). Inference usage is billed by, and subject to your agreement with, that provider. When you configure the Anthropic API as your provider, inference billing and data terms fall under your Anthropic agreement. Your existing commercial agreement with Anthropic continues to apply to your use of the Claude Desktop application, unless we've mutually agreed otherwise.

## Compliance

When using Google Cloud's Agent Platform or Amazon Bedrock, the app sends conversation content only to your configured inference endpoint and stores it on the local device. Data handling at the endpoint is governed by [Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance) and [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) respectively, and the compliance posture of your deployment is determined by your inference provider and the device environment you control.

When using Microsoft Foundry, the app also sends conversation content only to your configured inference endpoint and stores it on the local device.

Microsoft Foundry offers Claude models in two hosting options, Hosted on Azure and Hosted on Anthropic, and you choose one when you configure the model deployment in Microsoft Foundry. Under both options, Anthropic operates the Claude models and handles conversation data as an independent processor for Microsoft. Your use of Claude through Microsoft Foundry is subject to Anthropic's data use terms.

Deployments hosted on Azure run inference in an Anthropic-operated service on Azure infrastructure, not in your Azure tenant, and prompts and completions remain within Azure. The only data the service sends out of Azure to Anthropic is usage metadata and any content that Anthropic's safety systems flag. Deployments hosted on Anthropic send prompts and completions to Anthropic's own infrastructure for inference. See [hosting options for Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options) for details.

See the [Overview](/docs/third-party/claude-desktop/overview) for the architecture and [Data handling by provider](/docs/third-party/claude-desktop/overview#data-handling-by-provider) for each provider's data path.

For Anthropic's certifications and compliance reports, see the [Anthropic Trust Center](https://trust.anthropic.com).

For HIPAA, see [HIPAA](/docs/third-party/claude-desktop/overview#hipaa) on the Overview page. For Google Cloud's Agent Platform and Amazon Bedrock, Anthropic does not interact with PHI; the BAA relationship is between you and your cloud service provider, and any remote MCP servers you connect need your own HIPAA review. For Microsoft Foundry, HIPAA readiness (Anthropic's arrangement of a signed BAA plus safeguards for processing PHI) is not available, as described under [What HIPAA readiness does not cover](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#what-hipaa-readiness-does-not-cover) in the Claude API documentation.

## Usage policy

Use of Claude models, including via Claude Desktop on 3P, is subject to the [Anthropic Usage Policy](https://www.anthropic.com/legal/aup).

## Privacy and telemetry

The Claude Desktop application sends operational telemetry (crash reports and product analytics) to Anthropic by default. This telemetry contains no prompt or response content and can be fully disabled via managed configuration. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for what each category contains and how to disable it.

Anthropic's [Privacy Policy](https://www.anthropic.com/legal/privacy) describes how Anthropic handles data it receives.

## Security and trust

Security architecture, threat-model, and data-flow documentation for Claude Desktop and Claude Desktop on 3P is available on the [Anthropic Trust Center](https://trust.anthropic.com).

### Security vulnerability reporting

Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/4f1f16ba-10d3-4d09-9ecc-c721aad90f24/embedded_submissions/new).

***

© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.
