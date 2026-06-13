Title: Frontier Model Security

URL Source: https://www.anthropic.com/news/frontier-model-security

Markdown Content:
![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F10d2b2627656111aae62a8ab7b299b4b73ee86a4-2880x1620.png&w=3840&q=75)

As the capabilities of frontier artificial intelligence models continue to increase rapidly, ensuring the security of these systems has become a critical priority. In our previous posts, we’ve focused on Anthropic’s [approach to safety](https://www.anthropic.com/news/core-views-on-ai-safety), and Claude’s capabilities and applications. In this post, we are sharing some of the steps we are taking to ensure our models are developed securely. We hope to advance public discussion about how all labs can deploy top models securely, as well as share recommendations for government regulatory approaches that encourage adoption of strong cybersecurity practices. Below we discuss some of our recommendations for cybersecurity best practices, which Anthropic itself is in the process of implementing.

## Summary

Future advanced AI models have the potential to upend economic and national security affairs within and among nation-states. Given the strategic nature of this technology, frontier AI research and models must be secured to levels far exceeding standard practices for other commercial technologies in order to protect them from theft or misuse.

In the near term, governments and frontier AI labs must be ready to protect advanced models and model weights, and the research that feeds into them. This should include measures such as the development of robust best practices widely diffused among industry, as well as treating the advanced AI sector as something akin to “critical infrastructure” in terms of the level of public-private partnership in securing these models and the companies developing them.

Many of these measures can begin as voluntary arrangements, but in time it may be appropriate to use government procurement or regulatory powers to mandate compliance.

## Cybersecurity Best Practices

We believe “two-party control” is necessary to secure advanced AI systems. Two-party control is already used in a range of domains; for example, two people with two keys are needed to open the most secure vaults, and multi-party review patterns have been applied in manufacturing ([GMP](https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/gmp#:~:text=GMP%20defines%20quality%20measures%20for,the%20production%20of%20pharmaceuticals%20and), [ISO 9001](https://www.iso.org/iso-9001-quality-management.html)), food ([FSMA PCQI](https://www.sqfi.com/wp-content/uploads/2018/08/FSMA-FAQs-for-website-.pdf), [ISO 22000](https://www.iso.org/iso-22000-food-safety-management.html)), medical ([ISO 13485](https://www.iso.org/standard/59752.html)) and finance tech ([SOX](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act)).

*   This pattern should be applied to all systems involved in the development, training, hosting, and deployment of frontier AI models.
*   This pattern is already in widespread use within major tech companies to defend against the most advanced threat actors and mitigate insider risk.
*   It is manifested as a system design where no person has persistent access to production-critical environments, and they must ask a coworker for time-limited access with a business justification for that request.
*   Even emerging AI labs, without large enterprise resources, can implement these controls.

We call this **multi-party authorization to AI-critical infrastructure design**. This is a leading security requirement that depends on the gamut of cybersecurity best practices to implement correctly.

In addition, secure software development practices should pervade the frontier AI model environment. The gold-standard for these practices are the NIST [Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf) (SSDF) and the [Supply Chain Levels for Software Artifacts](https://slsa.dev/) (SLSA). Executive Orders have been leveraged successfully to encourage major tech companies to adopt higher development standards: in 2021,[EO 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) directed OMB to set Federal Procurement guidelines. This motivated action: the software industry has invested heavily to meet the SSDF’s requirements to retain federal contracts.

While frontier AI research is already benefiting from the implementation of some of these standards by dint of cloud providers hosting their models, applying these existing standards can step-change the security of these AI systems:

SSDF and SLSA are largely translatable into the development of models and their coupled software; producing a model and then deploying it is almost identical to building software and then deploying it.

SSDF and SLSA coupled together mean that any AI system deployed has a chain of custody. By this, we mean that when applied correctly these practices make it so you are able to tie back a deployed model to the company that developed it, which helps provide provenance.

We call this a **secure model development framework**. We encourage extending SSDF to encompass model development inside of NIST’s standard-setting process.

In the near term, these two best practices could be established as procurement requirements applying to AI companies and cloud providers contracting with governments – alongside standard cybersecurity practices that also apply to these companies. As U.S. cloud providers provide the infrastructure that many current frontier model companies use,procurement requirements will have an effect similar to broad market regulation and can work in advance of regulatory requirements.

Anthropic is implementing two-party controls, SSDF, SLSA, and other cybersecurity best practices. As model capabilities scale, we will need to further enhance security protections, moving beyond the above recommendations. This will necessarily be an iterative process in consultation with government and industry.

## Public-Private Cooperation

Frontier AI research labs should participate in public-private cooperation in the same way as companies in critical infrastructure sectors like financial services. This sector could be designated as a special sub-sector of the existing IT sector, for example. Such a designation would be a vehicle for enhanced cooperation and information sharing between and among industry labs and government agencies, helping all labs better guard against highly resourced malicious cyber actors.

## Conclusion

It can be tempting to deprioritize security: when everything is going well, it can feel like it isn’t necessary or that it is in tension with other company goals. But this technology is becoming more powerful and will require enhanced precautions. We also believe that while security can sometimes interfere with productivity, that there are creative ways to ensure that its effects are limited and that research and other work can proceed effectively.

The development of artificial intelligence has incredible potential to benefit humanity, but it also comes with risks if not pursued thoughtfully. As an AI company working on the frontier of this technology, we take our responsibility seriously to build and deploy Claude in a way that is safe, secure and aligned with human values. We will continue sharing our perspectives on the responsible development of AI.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
