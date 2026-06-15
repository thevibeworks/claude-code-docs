Title: Work across Microsoft 365 apps

URL Source: https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps

Markdown Content:
Claude can now work across Microsoft 365 apps to coordinate between the Excel, PowerPoint, Word, and Outlook add-ins. Instead of switching between apps and providing context each time, Claude can read from one app and make changes in another. For example, you can ask Claude to analyze data in an Excel workbook, then create a presentation in PowerPoint using those results, without copying and pasting between apps.

## Requirements

## Let Claude work across apps

### 1. Install the add-ins

Get the add-ins from the Microsoft Marketplace:

Open each app and activate the add-in at least once before using the cross-app features.

### 2. Toggle the setting on

Go to **Settings**in each of the add-ins and toggle **Let Claude work across files** on:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152216540/23e9f22eca1109ec09f2c6138191/2ef697a8-3a60-4193-bbd7-639ed91b20e9?expires=1781505900&signature=5e8906a0a059471edbe3b33c796ef538d6e9e4d32142696633ecd25560d307ef&req=diEiFMt%2Fm4RbWfMW1HO4ze%2BVVHXwUAtWQEr1GSm7Lk2oz%2FJdaT7tPFlffrDw%0AViKBqdKYzcqJ8fn%2FehU%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152216540/23e9f22eca1109ec09f2c6138191/2ef697a8-3a60-4193-bbd7-639ed91b20e9?expires=1781505900&signature=5e8906a0a059471edbe3b33c796ef538d6e9e4d32142696633ecd25560d307ef&req=diEiFMt%2Fm4RbWfMW1HO4ze%2BVVHXwUAtWQEr1GSm7Lk2oz%2FJdaT7tPFlffrDw%0AViKBqdKYzcqJ8fn%2FehU%3D%0A)

You'll see connected file indicators when Excel, PowerPoint, Word, or Outlook files are linked to your session:

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152215013/db0cfd2aa4034975480d82218aad/8f11dc16-2173-4b34-a05a-e31a53b58cc2?expires=1781505900&signature=cb0374a7727fc53d1f848ea9d09ffdfec2222dd104bfbc38c7daf7b0b2a702fe&req=diEiFMt%2FmIFeWvMW1HO4zZtV3myz29doGgi4PNaz7vU3ffS95K7cUt%2BSi8GX%0ADP7mMfpY4xWMi7lN7Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152215013/db0cfd2aa4034975480d82218aad/8f11dc16-2173-4b34-a05a-e31a53b58cc2?expires=1781505900&signature=cb0374a7727fc53d1f848ea9d09ffdfec2222dd104bfbc38c7daf7b0b2a702fe&req=diEiFMt%2FmIFeWvMW1HO4zZtV3myz29doGgi4PNaz7vU3ffS95K7cUt%2BSi8GX%0ADP7mMfpY4xWMi7lN7Bg%3D%0A)

## How it works

When you describe a task that involves multiple files or apps, Claude coordinates behind the scenes:

## What you can do

### Read and write across open files

Claude can read data from an open Excel workbook, PowerPoint presentation, Word document, or Outlook email, and make changes to them directly. For example:

### Pass context between apps

When Claude works across multiple files in Excel, PowerPoint, Word, and Outlook, it carries relevant context forward. If you've been building a financial model in Excel and ask Claude to create a summary deck or draft an investment memo, Claude already understands the model's structure and key outputs, so you don't need to re-explain.

## Skills work across apps too

Skills you've enabled in your Claude settings apply when Claude is working in Excel, PowerPoint, Word, or Outlook during a cross-app task. If you have a Skill that enforces your team's modeling conventions in Excel and another that matches your slide template in PowerPoint, Claude uses each one in the right app as it moves through the workflow.

## Data handling

Inputs and outputs are automatically deleted from Anthropic's backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** The Claude for Excel, Claude for PowerPoint, Claude for Word, and Claude for Outlook add-ins do not inherit custom data retention settings your organization may have set, and activity is not currently included in Enterprise audit logs, the Compliance API, or data exports.

### For admins who want to manage access

Team and Enterprise organization owners can control whether team members can access this capability:

Admins can also manage member access to the Claude for Excel, PowerPoint, Word, and Outlook add-ins through the **[Microsoft 365 Admin Center](https://admin.microsoft.com/)**.

## Current limitations

## Troubleshooting

### Claude doesn't see my open file

Make sure the add-in is activated in the app (**Tools > Add-ins** on Mac or **Home > Add-ins** on Windows) and that working across apps is turned on in Claude Desktop settings.

### Changes aren't appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its current action, then check the target file. You may need to ask Claude to refresh or re-read the file.

* * *

Related Articles

[Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)[Use Claude for Outlook](https://support.claude.com/en/articles/14855664-use-claude-for-outlook)[Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
