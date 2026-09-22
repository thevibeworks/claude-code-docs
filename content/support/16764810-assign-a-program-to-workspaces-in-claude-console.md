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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1790091900&amp;signature=3d3523844a5d9856d45f5e233e0d66efb10b208f32ca667f82dd7b6b5dba62d4&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymUmHHQiuktHcEoeKC4cjJWKlcsZ5G2BZCPiC%0A8TjZ%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1790091900&amp;signature=776e8235ee33e1ca84eece86e47d694793cb42b87263e3b66536cc02712f7699&amp;req=diYjFM56mIRZW%2FMW1HO4zc116w5oSVG4MCr%2B42fbmkYwWwtxQGuQkRu51qyT%0AjjrK%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1790091900&amp;signature=e2736abac021883153ef78ff844781223ab0b64f507db4fb608b458f6e58526f&amp;req=diYjFM56m4VZX%2FMW1HO4zaveaOZin3zJVPpeIJbmktQB0NU3evhli6tAw5Dv%0APAJC%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1790091900&amp;signature=981d64b945fe2951c3f4a9c6ade1bcdecaaedb77317f9436cb97ea4a5edad704&amp;req=diYjFM54lYBeXvMW1HO4zTU0lduQIkdO9BWcjfiNKI2WCtRCVDS5eODlhM8U%0A9oAW%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1790091900&amp;signature=1f80891954d9beeb7779ae9c2f84e56022db9ea1335a3aa69e44f2d9331a5cb8&amp;req=diYjFM56m4hWXPMW1HO4zQfcHDuu5n8i9apHi%2BiM8ojYZ5UhJcu1WU75svGm%0A7Knt%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1790091900&amp;signature=7cc7954782e7dd54b4316c05b4014305af8d25ec58e4cb347166cfbecc9a69c9&amp;req=diYjFM56moNfWfMW1HO4zaUR86Zn%2F%2F8xfTukdAE3MWum5n1y1XQhwKFDw8%2FY%0AnIth%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.