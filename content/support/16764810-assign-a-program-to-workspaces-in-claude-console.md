# Assign a program to workspaces in Claude Console

Anthropic offers several verification programs, such as the Cyber Verification Program, or access to models that might not be generally available. In order to gain access to these programs, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available to you, and apply.

Once you’ve applied and been approved for a program, Anthropic issues a “program” to your organization. In order for it to be used, you must assign it to a group of people within the organization. In the Claude Console, a program applies to workspaces, either automatically (for programs like the Cyber Verification Program) or by assignment.

This article covers how to enable programs for the Console.

## Before you start

- Your organization must already have a grant. Grants appear only after Anthropic issues one to your organization. To apply to a specific program, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available.

- In the Console, you need to be an organization Admin. Other roles cannot view or manage grants.

## Give a Console workspace access

In the Console, programs are issued to your organization and apply to workspaces. Some programs, such as the Cyber Verification Program, apply automatically to every workspace that meets their requirements. Others need workspaces assigned. A program only applies to API traffic from workspaces that meet its requirements.

**Follow these steps:**

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization Admin. Go to **[Organization settings > Programs](https://platform.claude.com/settings/organization/programs)**. The program card shows whether it applies automatically or needs workspaces assigned.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1789991100&amp;signature=4238916283279c5eca863bc7992154f77d197a2ce62054d94bec47970fb9b9ba&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymECOHQimktHcEoeKC4cM1nwgEhH7t32aY6VB%0AMcjn%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1789991100&amp;signature=36c4bad9bc6249af8d8ac9f86d79eab0d0020143692cb8210693541c5fc67447&amp;req=diYjFM56mIRZW%2FMW1HO4zc116gdhSVGwMCr%2B42fbmkZOcinOyIZZUMWgotHg%0Alv3E%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1789991100&amp;signature=252c8cc9302a9dc35abe98ca02cd46947ffdfd1b580f806b129dead4cfd18eec&amp;req=diYjFM56m4VZX%2FMW1HO4zaveae9rn3zBVPpeIJbmktS2ri%2BDHdk8ZnZQEj%2BX%0AOp0v%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1789991100&amp;signature=204f713ee323756c5affeaca5d23faf09a4c2a5ae3bd7ca1cc59fdda1ef96e39&amp;req=diYjFM54lYBeXvMW1HO4zTU0lNKZIkdG9BWcjfiNKI0RUJVKiF9g%2Fgy0O8cg%0A%2B2ee%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1789991100&amp;signature=ad42422af0c4c236b14b3d31a1b4c90d7366c08d876c9298ba00b76c2d48ea5b&amp;req=diYjFM56m4hWXPMW1HO4zQfcHTKn5n8q9apHi%2BiM8oghChVaqK6YM4HPlu8H%0ArU9d%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1789991100&amp;signature=ea0b64c9eec0f07b8a47f272fad92d19673d082f3436bc5a39d6d5bb0657db12&amp;req=diYjFM56moNfWfMW1HO4zaUR8q9u%2F%2F85fTukdAE3MWtOfkRZtOW3MBNhivUZ%0Aj7he%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.