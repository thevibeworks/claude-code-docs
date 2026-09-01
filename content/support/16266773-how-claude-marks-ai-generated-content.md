# How Claude marks AI-generated content

Anthropic has signed the EU AI Act's Article 50(2) Code of Practice on Transparency of AI-Generated Content, as a provider of both generative AI models and generative AI systems. This article describes how we’re planning to put those commitments into practice, how marking works, and what its limitations are. We’ll update this article and publish more detailed technical guidance as it becomes available.

**Anthropic’s commitments under the EU AI Act’s Code of Practice on Transparency of AI-Generated Content**

What our marking commitments mean for Claude:

- **New models will mark AI-generated content from day one.** Claude models launched in the EU on or after August 2, 2026 will support machine-readable marking at launch. Generated text will carry embedded watermarks, and generated files will include digitally signed provenance metadata where supported.

- **Marking works everywhere you use Claude.** Marks will apply to output from supported Claude models across Claude Platform (API), Claude, Claude Code, Claude Cowork, and Claude Tag, and wherever Claude is offered, worldwide. Some platforms or features may not support certain marking types.

- **Existing models are in progress.** The law includes a transition period for Anthropic models launched before August 2, 2026, and we’re working to add marking support for those models as well.

- **Watermark detection is in private preview.** Watermark detection is currently available to eligible organizations as required under EU law (such as regulators, law enforcement, media, fact-checkers, independent researchers, educational organizations, and EU civil society groups). It is also available for enterprises who are similarly obligated to verify watermarking for their own compliance with the Act. We plan to expand access to the detection API over time. You can register interest in access here: **[Claude Watermark Detector Access Request Form](https://forms.gle/9tGA33hPJJwtHsMk9)**.

More details about our marking plans are below.

---

## Machine-readable marks in Claude-generated content

As AI-generated content becomes commonplace, greater transparency and signals about where content comes from can give people useful context about the information they consume. To support transparency and comply with our legal obligations, Anthropic is working to include machine-readable marks in content that Claude generates.

### What’s covered

- **Models.** Claude models launched on or after August 2, 2026 support marking at launch. Models currently supported include Fable 5.1 and Mythos 5.1. We’re working to add marking support to other Claude models released before that date, and we’ll update this article as that becomes available.

- **Products.** Claude markings cover output from supported models everywhere you use Claude, including Claude Platform (API), Claude, Claude Code, Claude Cowork, and Claude Tag. Embedded watermarks will apply to all generated text. Provenance metadata will apply where Claude supports processing files.

- **Cloud partners.** When supported Claude models are accessed through AWS, Google Cloud, or Microsoft Foundry they will carry watermarks. Signed provenance metadata is added when Claude creates a file, so it applies only where a platform offers Claude's file generation features.

- **Regions.** Marking will apply to output from supported models wherever Claude is offered, worldwide.

## How Claude marks content

Claude uses two complementary techniques to mark content generated and processed by Claude: (1) watermarks embedded in text, and (2) signed provenance metadata attached to files.

### 1. Embedded watermarks in text

When a supported Claude model generates text, it weaves an imperceptible watermark directly into the text itself. You won’t see it, and it doesn’t change the meaning, quality, or readability of Claude’s response.

Because the watermark is part of the text, it will travel with the text when it’s copied and pasted elsewhere, and may persist through some editing. Watermarking will be applied at the model level, which means it will be present no matter which Claude product or surface the text comes from.

### 2. Signed provenance metadata

When Claude generates a supported file type, such as a .svg, .png, or .jpg, it will attach signed provenance metadata. This metadata follows the Coalition for Content Provenance and Authenticity (C2PA) open standard, which is used across the industry to record information about content provenance. If a signed metadata label is present, it signals that a file was processed by Claude and lets you detect whether the file has been tampered with.

## Detect Claude’s marks

Detection checks whether a piece of text or a file carries a supported Claude mark. If a supported mark is found, it indicates that the content may have been processed by Claude.

To check whether a file contains a Claude-issued Content Credential, use the free **[Claude Content Checker](https://claude.com/check-content)**. To learn more about how Claude marks files and how to verify Claude-issued Content Credentials, see **[Content Credentials on generated files](https://platform.claude.com/docs/en/build-with-claude/watermark-detection)**.

Watermark detection is currently in private preview, available to eligible organizations as required under EU law (such as regulators, law enforcement, media, fact-checkers, independent researchers, educational organizations, and EU civil society groups). It is also available for enterprises who are similarly obligated to verify watermarking for their own compliance with the Act. We plan to expand access to the detection API over time. You can register interest in access here: **[Claude Watermark Detector Access Request Form](https://forms.gle/9tGA33hPJJwtHsMk9)**.

## Limitations

Machine-readable marks provide important signals about content, but it’s worth understanding their limitations across all content types.

- **A detected mark provides a signal that content was processed by Claude, but is not fully conclusive.** Detecting a Claude mark tells you that the content may have been processed by Claude. It does not, on its own, confirm the full provenance of the content. For example:

  - Claude may not be the original author. People often use Claude to proofread, translate, summarize, or convert files. The output can carry a Claude mark even if the underlying ideas, text, or data originated from another source;

  - The content may have changed after Claude processed it. Marked content may be modified, excerpted, or combined with other material after Claude processed it.

- **Lack of a detected mark doesn’t mean the content wasn’t AI-generated or processed.** Content generated by Claude may not carry a detectable mark if, for example:

  - It was generated by a model released before marking was supported;

  - The text has been heavily edited, paraphrased, translated, or mixed into other writing;

  - The passage is very short, leaving too little text for a reliable signal;

  - A file’s metadata was stripped through format conversion, re-saving, screenshots, or other means;

  - It was produced through a platform, feature, or file type where a particular marking type wasn’t supported.

## If you build with Claude

If you deploy Claude in your own product, you should independently assess what Article 50 requires of your products and services. Consistent with our commitments under the EU Code, our goal is to support you in meeting your own transparency obligations, and we'll share technical guidance on our marking and detection approach as it becomes available.