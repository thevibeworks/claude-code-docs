Title: Public Sector FAQs

URL Source: https://support.claude.com/en/articles/13756069-public-sector-faqs

Markdown Content:
## 1. Products and features

### What products are available to Public Sector customers?

Select your product based on both your technical/functional requirements, and also your compliance/security/deployment environment requirements. Here is a list of options:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2197717161/79965a24090029e9e58c727c3c24/pubsec-product-matrix_png+%281%29.jpg?expires=1781626500&signature=e006e49389dc3ca1d08f193df8b63f6126213623f7ec4afd856a80e46f69e7e2&req=diEuEc5%2FmoBZWPMW1HO4zU94LlgjH9s12WxtU42UVC2rbkW%2Fwz1QNKsAnvuM%0A%2B0pcAKixHorLYeiudks%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2197717161/79965a24090029e9e58c727c3c24/pubsec-product-matrix_png+%281%29.jpg?expires=1781626500&signature=e006e49389dc3ca1d08f193df8b63f6126213623f7ec4afd856a80e46f69e7e2&req=diEuEc5%2FmoBZWPMW1HO4zU94LlgjH9s12WxtU42UVC2rbkW%2Fwz1QNKsAnvuM%0A%2B0pcAKixHorLYeiudks%3D%0A)

### What is Claude for Government (C4G)?

Claude for Government is Anthropic's FedRAMP-High authorized product, which is available to both government customers and contractors.

### How do I access Claude for Government?

### What is the difference between Claude Enterprise and Claude for Government?

Claude Enterprise (CE) has robust enterprise-level security features that meet many standards of highly regulated industry and is appropriate for the majority of State and Local government uses. Claude for Government (C4G) is our standalone application that is FedRAMP-High authorized. C4G does not yet include Claude Code or Cowork (though they are on the roadmap to be released this year).

### Does Claude for Government include Claude Code?

Not yet; though it’s coming this year. Until then, customers can use Claude Code through Bedrock or Vertex if they need a FedRAMP authorized environment.

### Can I use Claude API in government environments?

Yes. Claude API is available via Amazon Bedrock (in AWS GovCloud - FedRAMP High, and in IL5+) and Google Vertex with Assured Workloads (FedRAMP-High).

### What models are available in Claude for Government?

Our Claude for Government application is updated with our latest commercial model releases.

## 2. FedRAMP, Impact Levels, and compliance

### What types of data can be used in Claude?

CUl and FIPS 199 High Impact data are authorized in Claude for Government, which is FedRAMP High authorized. Additionally, per our third-party NIST attestation, Claude Enterprise meets compliance requirements for CUl as well. The third-party NIST attestation is available under NDA here: **[[Anthropic] 2026 NIST 800-171r3 Attestation Letter](https://trust.anthropic.com/resources?s=zfucqt7j6yandbrsvlk2&name=[anthropic]-2026-nist-800-171-r-3-attestation-letter)**

ITAR data can only be processed in Claude via AWS Bedrock, which is IL5 accredited.

For most other government agencies like State and Local handling PHI or PII:, Anthropic offers a HIPAA-ready configuration for Enterprise and API customers, including the ability to sign a Business Associate Agreement (BAA). A couple of key points:

You can learn more here:

### What is Claude's FedRAMP authorization level?

Claude for Government (C4G), and Claude via Amazon Bedrock in AWS GovCloud and Google Vertex with Assured Workloads are all FedRAMP-High.

### Are Claude's models themselves FedRAMP authorized?

FedRAMP and DoD Impact Levels are certifications for cloud services (IaaS, PaaS, SaaS). AI models are software components, not cloud services. Claude models deploy within authorized environments, and customers maintain their compliance posture through the hosting platform.

### How can I get access to your FedRAMP authorization information and other associated documentation?

### Can I use Claude for CUI (Controlled Unclassified Information)?

Yes. Claude Enterprise has received a third-party NIST attestation for use of CUI data. Alternatively, CUI data can be processed in a FedRAMP High environment via Claude for Government, Bedrock, or Vertex. The third-party NIST attestation is available under NDA here: **[[Anthropic] 2026 NIST 800-171r3 Attestation Letter](https://trust.anthropic.com/resources?s=zfucqt7j6yandbrsvlk2&name=[anthropic]-2026-nist-800-171-r-3-attestation-letter)**

### Can I use Claude in IL6/Secret environments?

Yes. Claude is available in the AWS Secret region (IL6) via Amazon Bedrock.

### If a customer purchases Claude Enterprise via AWS Marketplace, is that FedRAMP?

No. At present, our only product offering on AWS Marketplace is Claude Enterprise which is not FedRAMP authorized. Customers requiring FedRAMP compliance must use Claude for Government (C4G) or access Claude models through FedRAMP-authorized CSPs (Bedrock GovCloud or Vertex Assured Workloads).

## 3. Cloud service providers and deployment

### How do I deploy Claude in Amazon Bedrock on AWS GovCloud / GCP Vertex in Assured Workloads?

Work with your AWS / GCP account teams. Claude is available as a managed service through Bedrock/Vertex. These links can help to get you started:

### What is the pricing and commitment information for Claude on Vertex/Bedrock?

Contact AWS directly for pricing and commitment requirements. Usage is typically pay-per-token through standard Bedrock pricing.

## 4. Pricing and procurement

### What is the $1/month government offer and who qualifies?

The $1/month offer is specifically for federal, judicial, and legislative agencies for C4G only. It does not extend to defense contractors, FFRDCs, or state/local governments, which receive standard pricing.

### Can we purchase directly from Anthropic or only through Carahsoft?

Both options are available. Anthropic can sell directly, and/or resell / distribute via Carahsoft to specific government customers.

### How much does Claude cost?

C4G is $60/seat/month with usage limits and no additional consumption charges.

Claude Enterprise is $20/seat/month with additional charges for token consumption (PAYG).

* * *

Related Articles

[What is Amazon Bedrock?](https://support.claude.com/en/articles/7996918-what-is-amazon-bedrock)[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)[Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
