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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1789279200&amp;signature=69f24b2dd20b9aa0bea69a47ddda57dc967f51b13c56b233022ac5141ca8f09e&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymECFEwClktHcEoeKC4fLaB4JSEEgv7BO97Vx%0ASQyY%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1789279200&amp;signature=b8471b94434dad3972171c606143c08483c7fcc2029b65460df95d6947f573ec&amp;req=diYjFM56mIRZW%2FMW1HO4zc116gdqR1mzMCr%2B42fbmkZyXtEQAgVywsyqVXSJ%0AN6DX%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1789279200&amp;signature=1bd6c88b8067265bc2df570463cd6ccb123b300357706e6bf53cc98a6155e71c&amp;req=diYjFM56m4VZX%2FMW1HO4zaveae9gkXTCVPpeIJbmktTzMGJO8yjLBf1xQJJV%0ApB5u%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1789279200&amp;signature=7ea57eb20e491613f06da2bfb78f1b499d50b1fa66041a12ee630af8c2202bc8&amp;req=diYjFM54lYBeXvMW1HO4zTU0lNKSLE9F9BWcjfiNKI1i0FunG0lNV3fMAtcl%0AiBt%2F%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1789279200&amp;signature=41c18afec5e607bc85171e44937517cff20e54c782c3c95f9d5094094e5a203f&amp;req=diYjFM56m4hWXPMW1HO4zQfcHTKs6Hcp9apHi%2BiM8oiQyLN%2FUiSqZVuVFJWQ%0ATXhQ%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1789279200&amp;signature=4431d68fbab8b8a0510d5f402806ddcc0571008501a0992d02543954dfcab9a9&amp;req=diYjFM56moNfWfMW1HO4zaUR8q9l8fc6fTukdAE3MWsPjT49KXm%2B7GvcTD9Q%0A%2F8kr%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.