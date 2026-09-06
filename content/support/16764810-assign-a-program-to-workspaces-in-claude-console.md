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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1788718500&amp;signature=24d7315a3312b3debc0e627f35992fcf433a9986ca473fe362305203762f8fc2&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymEGAFQGiktHcEoeKC4cXhtTf%2BvKd21eYcjRn%0A1ltE%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1788718500&amp;signature=1d1ae7e583e72df7c5c4daf614da4beee4034de7d440afeb687c3961a7bbbe14&amp;req=diYjFM56mIRZW%2FMW1HO4zc116gZvQVi0MCr%2B42fbmkbcyK2WOcAl2yWTSqyp%0Al0Cg%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1788718500&amp;signature=f33ef3a5dec0639caecb7af1ddf9b089d8c3279f324355f79a4ed2a2450a52dd&amp;req=diYjFM56m4VZX%2FMW1HO4zaveae5ll3XFVPpeIJbmktTRtuYIrXQfTx5gCZxe%0AnPQf%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1788718500&amp;signature=6cbeb294628f7ff5f4556e865f6ec26d3c4b02e2295686d4aa83051d2d865fcd&amp;req=diYjFM54lYBeXvMW1HO4zTU0lNOXKk5C9BWcjfiNKI2iIY%2FLKSnNkKU%2Fv%2BaJ%0AK40x%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1788718500&amp;signature=e62318456e59c7b4a5d235e2258730b53b77bb340123e05056d4fe5270597f81&amp;req=diYjFM56m4hWXPMW1HO4zQfcHTOp7nYu9apHi%2BiM8ohYdpeKAkSYnlctpLOd%0AFfm2%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1788718500&amp;signature=bb45c01a317ff12ad7db29e2421e82d101958c8eaaac5bba564e6e7ae97435f3&amp;req=diYjFM56moNfWfMW1HO4zaUR8q5g9%2FY9fTukdAE3MWsnnDEbdj90yVThzS5k%0AMH0e%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.