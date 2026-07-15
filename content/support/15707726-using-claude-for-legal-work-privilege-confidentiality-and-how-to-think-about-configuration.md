# Using Claude for Legal Work: Privilege, Confidentiality, and How to Think About Configuration

Lawyers and legal teams increasingly want to use Claude for research, drafting, contract review, and litigation prep. One of the most common questions we hear is some version of: *can I do that without putting privilege or client confidentiality at risk?* We think the answer is yes, with the right configuration and the right practices—and we want to be transparent about both how Claude is built and where the law currently stands.

This is Anthropic's perspective on our own products and the public record; it isn't legal advice, and the right answer for your practice depends on your jurisdiction, your clients, and your matters.

## The legal profession has been here before—mostly.

When email and cloud storage arrived, bar regulators initially worried that routing client confidences through a third party's servers was a confidentiality problem. The consensus that emerged—ABA Formal Op. 99-413 on email, the state cloud opinions of 2010-12, ABA 477R, and the 2012 amendments to Model Rules 1.1 and 1.6—was that lawyers may use these technologies with reasonable care in selecting and supervising the vendor. Generative AI is following the same arc: ABA Formal Op. 512 (2024) and the state and local bar opinions since (Florida, D.C., New York City, Pennsylvania, Texas, Oregon, Alaska, among others) apply the existing duties—competence, confidentiality, supervision, and verification—rather than prohibiting use.

## Where the courts are.

The first widely-discussed decision, *United States v. Heppner* (S.D.N.Y. Feb. 2026), held that a criminal defendant's *own* use of a consumer AI account—without his lawyers' involvement—wasn't privileged work product. The court's reasoning turned on the consumer privacy terms and the absence of attorney direction; it said nothing about lawyers using enterprise tools, and its citations to *United States v. Adlman* and *United States v. Kovel* left open that an enterprise-level AI used at an attorney's direction may be privileged.

While *Heppner* declined to find attorney-client privilege or work product in the absence of attorney involvement, subsequent decisions have gone the other way in the context of both pro se litigants’ and attorneys’ use of AI. *Warner v. Gilbarco* (E.D. Mich.), *Morgan v. V2X* (D. Colo.), *Tate Group Automotive v. Legacy Automotive Capital* (Tex. Bus. Ct.), and *Assini v. Hayward* (N.Y. Sup. Ct.) each held that AI-assisted litigation preparation is protected work product and that disclosing inputs to an AI tool does not, by itself, waive that protection. *Morgan* in particular approved protective-order language permitting parties to upload confidential information into an AI tool where the provider is contractually barred from training on, retaining, or disclosing confidential data beyond what's necessary to render the service. Likewise *Warner* emphasized that work product protection can be waived by disclosure to an adversary, but typically is not waived by disclosure to a third party subject to a duty of confidentiality. We think that's the right line—and it's the line our commercial terms are built around.

Work-product protection is generally tied to litigation, and its scope varies by jurisdiction. For work that isn't litigation-related, the focus would be on attorney-client privilege, where it applies, plus our contractual no-training and confidentiality commitments—neither of which depends on litigation.

This is an area of law that's moving quickly. None of these are appellate decisions, courts in other jurisdictions may see it differently, and we'd encourage anyone making deployment decisions to discuss them with their own counsel.

## How Claude is built, and the choices you have.

There are two questions worth separating: *what does Anthropic see*, and *what protections survive even when a vendor sees something*.

On the first—our **[published security and privacy design](https://trust.anthropic.com)** describes the architecture in detail, but in short:

- **We do not train on your content by default.** Under our commercial terms, **[by default](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)**, customer content from Claude for Work, the Claude Platform, and the API is not used to train our models.

- **Retention is configurable.** **[Claude for Work](https://support.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans)** administrators can set an organization-wide retention period. **[API](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** customers can use our standard 30-day retention or, on eligible endpoints and models, **[Zero Data Retention](https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to)**. For our most **[capable models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)**, where safety monitoring requires it, we retain prompts and outputs for 30 days in a governed store that is automatically deleted, with the serving path itself stateless.

- **Human review is a very narrow exception.** Retained data is processed by automated safety systems for potential harm only. Only content flagged by the automated safety system can be reached by a human reviewer. When content is flagged for potential serious harm, review is performed by a small, designated set of safeguards personnel under contractual confidentiality, with need-to-know scoping and two-person approval for regulated data categories.

- **You can verify this.** Every human read is logged to a tamper-proof entry that customers with **[Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency)** can retrieve.

- **Customer-managed encryption** is available for **[qualifying customers](https://trust.anthropic.com/resources?s=7ksqkied5hn0pocsj206m&name=%5Banthropic%5D-security-and-privacy-design-of-anthropic-data-retention-and-review)**, putting the encryption keys for the retention store in your own key management system (KMS)—though this controls key custody, not the narrow safety review above.

- **In-tenancy options.** Claude is also available via AWS Bedrock and Google Cloud Vertex AI for organizations whose policy is that data stay within their own cloud environment. This changes where your data resides and whom you contract with; it does not by itself switch off the safety monitoring described above.

On the second—what survives even when a vendor sees something—two doctrines do the work: attorney-client privilege protects confidential lawyer-client communications on legal advice, and the work-product doctrine protects material prepared by a lawyer in anticipation of litigation. Neither is waived by disclosure to a non-adversary vendor bound to confidentiality—the same footing on which lawyers use e-discovery platforms, document-review vendors, court reporters, and translators today, and the one the post-Heppner courts have applied to AI. Keeping a lawyer visibly directing the work—so that AI output is the attorney's draft, not a substitute for advice—strengthens it. It's the same line that keeps AI use clear of unauthorized-practice concerns now surfacing where people use these tools in place of a lawyer rather than under one.

## What we'd suggest you consider.

- Whether you're on commercial terms (with a DPA and the no-training commitment), which is the baseline expectation for legal technology.

- Whether the sensitivity of the matter calls for ZDR or an in-tenancy deployment.

- How you'll keep a lawyer in the loop, verify output against primary sources, and document your AI use—the same supervision and competence duties that apply to any tool, and the same posture that keeps the work on the right side of those unauthorized-practice questions.

- Your own client-consent and engagement-letter practices, which several bar opinions (including ABA 512) address.

## Our view.

We believe Claude's commercial offerings can be configured by lawyers in a way that maintains privilege and confidentiality, and that the legal profession's experience with email and cloud—initial caution, then a reasonable-care standard, then mainstream adoption—is the likely arc here too. We also think it matters that it goes that way: technology competence is now part of the duty of competence. Rules that scare lawyers away from capable tools don't protect clients and they make representation slower and more expensive in a system where most people already can't afford a lawyer. We'll keep publishing how our systems work, keep our commercial terms aligned with what professional responsibility guidance requires, and keep engaging in the public conversation as the law develops.

---

*This document describes Anthropic's products and Anthropic's perspective on publicly available legal authorities as of June 2026. It is not legal advice. Whether any particular configuration meets your confidentiality, privilege, or regulatory obligations is a question for your own counsel.*