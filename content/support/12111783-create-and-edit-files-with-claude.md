Title: Create and edit files with Claude

URL Source: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude

Markdown Content:
Claude can execute code to create and work with files directly in your conversations. Prompt Claude using natural language to generate Excel spreadsheets, PowerPoint presentations, Word documents, and PDF files that you can download and use immediately.

These capabilities make it easy to produce professional documents by simply chatting with Claude. You can create financial models in Excel with working formulas, perform advanced analyses on uploaded data, produce reports with charts and visualizations, and generate presentations from your documents—all without specialized software skills.

## Availability

**Free, Pro, and Max plans:**

**Team plan:**

**Enterprise plan:**

## How to get started

### Enabling on web and desktop

**Enterprise plans:**This capability is enabled by default at the organization level with **Allow network egress** toggled off for new Enterprise organizations. Owners can adjust this in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)** using the **Code execution and file creation** toggle.

**Team plans:**This capability is enabled by default at the organization level with **Allow network egress** toggled on with access to package managers only. An organization owner can manually disable this for the organization in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)** if needed.

**Free, Pro, and Max plans:**Enable file creation from **[Settings > Capabilities](http://claude.ai/settings/capabilities)** by toggling **Code execution and file creation** on.

To give Claude access to external data sources, toggle **Allow network egress** on:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2054774005/25bcfffba6c249cd128d6c3f6d52/CleanShot+2026-02-11+at+16_34_47%402x.png?expires=1779963300&signature=74cdf9fa8a08ec27763f602bdac881a547c628d1a834a403c576bc723c189f99&req=diAiEs55mYFfXPMW1HO4zYFJxARMCprNPQVowIiib2n0lHkagorgWjKwKskO%0Ay2ah9h5kvdIMw9nJ%2Fuw%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2054774005/25bcfffba6c249cd128d6c3f6d52/CleanShot+2026-02-11+at+16_34_47%402x.png?expires=1779963300&signature=74cdf9fa8a08ec27763f602bdac881a547c628d1a834a403c576bc723c189f99&req=diAiEs55mYFfXPMW1HO4zYFJxARMCprNPQVowIiib2n0lHkagorgWjKwKskO%0Ay2ah9h5kvdIMw9nJ%2Fuw%3D%0A)

### Enabling on Claude Mobile

To enable or disable this feature on Claude for iOS or Android, tap your initials or name in the left sidebar to open Settings. Select "Capabilities" and toggle **Code execution and file creation** on or off.

## Configuring network access (Team and Enterprise plans)

Team and Enterprise organization owners can control network access settings in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)**. After enabling code execution and file creation, choose from the following options to configure network access for your team:

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945362/ad72504d5429960f369b8b91b43c/86f06c0e-6eaa-4574-a4cb-2c38b273613a?expires=1779963300&signature=1f53c4076bce4caa51204a4a8ccd3bed6cab8f971166aaaba5104d4d3d5e8d46&req=dScvH8B6mIJZW%2FMW1HO4zXJcCWRKkypIpMW6Iph6YZfKrjRV9IEbTsHvSwKg%0As6wcCrg67m9%2FpGXhqvY%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945362/ad72504d5429960f369b8b91b43c/86f06c0e-6eaa-4574-a4cb-2c38b273613a?expires=1779963300&signature=1f53c4076bce4caa51204a4a8ccd3bed6cab8f971166aaaba5104d4d3d5e8d46&req=dScvH8B6mIJZW%2FMW1HO4zXJcCWRKkypIpMW6Iph6YZfKrjRV9IEbTsHvSwKg%0As6wcCrg67m9%2FpGXhqvY%3D%0A)

**All domains:** Claude has full internet access except for domains on Anthropic's legal blocklist. While this provides maximum flexibility for file creation and analysis tasks, it’s also the riskiest option. Please review the **[security considerations below](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1)** before enabling “All domains”:

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945361/e3188cb8edb9ca7c303615da6378/f1c99a7d-5956-48d5-9ec7-b7ae6c8c3d28?expires=1779963300&signature=5f42226c622980ebb2dc17fe48b06fbef28ee3b353e27a7655f0b4de47722243&req=dScvH8B6mIJZWPMW1HO4zdnsdx2b6DyhqgKIA6CM1tpx%2BCk0HGYyusyeEWrO%0AU7UB5J4aiSuFx5%2Fg7UI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945361/e3188cb8edb9ca7c303615da6378/f1c99a7d-5956-48d5-9ec7-b7ae6c8c3d28?expires=1779963300&signature=5f42226c622980ebb2dc17fe48b06fbef28ee3b353e27a7655f0b4de47722243&req=dScvH8B6mIJZWPMW1HO4zdnsdx2b6DyhqgKIA6CM1tpx%2BCk0HGYyusyeEWrO%0AU7UB5J4aiSuFx5%2Fg7UI%3D%0A)

## How does disabling network access address security concerns with code execution and file creation?

**Short answer:** Disabling network access prevents data from leaving Claude's sandboxed environment - even if something goes wrong.

### How it works

When Claude executes code or creates files, it operates within an isolated, sandboxed container. This means the work happens in a controlled environment separate from your systems. However, if network access is enabled, there's a potential risk: through prompt injection or other attacks, Claude could theoretically be tricked into sending data to external servers.

Disabling network access eliminates this risk entirely. Your team still gets Claude's full code execution and file creation capabilities - building Excel models, creating presentations, analyzing data - but with the assurance that nothing can be transmitted outside the sandbox.

### A phased approach to network access

Claude is most powerful with network access enabled - it can install new packages and dependencies, pull in real-time data, and interact with web services. For organizations comfortable with that risk profile, enabling access to vetted, trusted domains unlocks the full potential of code execution and file creation.

For those taking a more cautious approach, we recommend starting with network access disabled and adjusting as your team builds confidence:

This approach gives you defense in depth - even if there were vulnerabilities in the sandbox or a successful prompt injection, disabled network access acts as a final barrier preventing data from leaving Anthropic's infrastructure.

## Using code execution and file creation

When enabled, simply describe what you need in your message. For example, you might say "Create an Excel spreadsheet to track monthly expenses" or "Convert this document into a PowerPoint presentation." Claude will generate the file, which you can then download directly from the conversation.

Start with simple tasks to familiarize yourself with Claude's capabilities, then progress to more complex workflows. Be specific in your requests—describe the structure, content, and formatting you want. You may need to review and refine Claude's outputs to meet your exact requirements.

### Supported file types

Claude can create Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization.

The maximum file size is 30MB per file for both uploads and downloads.

## Key capabilities

### Direct file creation and editing

Claude creates Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

The maximum file size is 30MB per file for both uploads and downloads. For PDFs larger than 30MB, Claude can process them through its computing environment without loading them into the context window.

### Advanced data analysis

Claude can perform sophisticated data analysis and data science work, including:

### Project files integration

Files in your projects are now accessible through Claude's computing environment while remaining in context. This enables seamless reference and workflow integration across your project files.

### Extended context window

The context window has been expanded to support more complex multi-step workflows, particularly for conversations that use code execution and file creation extensively.

### Language support

Claude provides full support for multiple languages in both the user interface and generated files, with proper formatting and regional standards.

## Security and network access

### How it works

Code execution and file creation gives Claude a sandboxed computing environment. Claude’s internet access will vary based on your network egress settings.

**Network access allows Claude to:**

## Security considerations

It is possible for a bad actor to inconspicuously add instructions via external files or websites that trick Claude into:

This means Claude can be tricked into sending information from its context (for example, prompts, projects, data via MCP, Google integrations) to malicious third parties. To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly. You can report issues to us using the thumbs down function directly in Claude.

We have performed red-teaming and security testing on this feature. We have a continuous process for ongoing security testing and red-teaming. We encourage organizations to evaluate these protections against their specific security requirements when deciding whether to enable this feature.

### For Team and Enterprise owners

Team and Enterprise owners have full control over this feature, including:

## Approved network domains

When network access is enabled, Claude can access the following approved domains:

## Common workflows

### Build a financial model in Excel

Generate spreadsheets with working formulas and calculations by describing your needs. Try:

Claude will produce an Excel file with proper formulas, formatting, and even charts to visualize your data.

### Generate a professional report

Combine data analysis with document creation by providing your information and requirements. Try:

Claude will analyze your data and produce a formatted Word document or PDF with charts, insights, and professional formatting.

### Convert between file formats

Change any document from one format to another while preserving or enhancing the content. Try:

or

Claude can even support workflows requiring multiple file format conversions. For instance, you could upload a CSV file and prompt Claude to create a financial model, write a memo summarizing it, and generate a PowerPoint to share the results.

### Extract and analyze PDF data

Upload a PDF containing tables or forms and ask Claude to extract the information. Try:

Claude will pull the data, organize it in spreadsheet format, and add visualizations for quick insights.

### Perform complex analyses

Upload a CSV with data and ask Claude to build a machine learning model to predict a particular outcome. Have Claude output a report summarizing what it did and the results. Claude will use python to train a model on your data, and provide an explanation of what it did, including the quality of the model, and the results.

## Frequently asked questions

### How does file creation work?

We have given Claude a private computing environment directly in claude.ai. This allows Claude to write and run code (for example Python or Javascript). It uses common code packages to create documents, spreadsheets, and slides. Users can also have Claude use its computing environment for other things like data analysis, debugging code snippets, and fun tasks like gif-creation.

### How do Claude’s file creation capabilities impact usage limits?

Use of this capability draws from the same usage limits offered by your plan. Note that creating files will use more of your limit compared to normal chats with Claude.

### Can Claude work with more than one file at a time?

Claude can handle multiple files in a single chat, allowing you to create comprehensive multi-file reports and analyses. Files remain available for download throughout your conversation.

### Is file creation supported on Claude for iOS or Android?

File creation is supported on Claude for iOS and Android. Note that when you tap "Download" on Claude Mobile, the file will open in either the system preview or a separate app (for example, the Word app for .docx files).

### Do artifacts work with file creation?

Yes you are still able to create artifacts (e.g., HTML or react apps, markdown documents, mermaid diagrams, SVGs) with file creation on. Claude now uses the computing environment to create artifacts so the user experience may look slightly different than users are used to. Please report any issues or feedback using the thumbs up/down functionality when chatting with Claude.

* * *

Related Articles

[Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Claude Cowork desktop architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview)
