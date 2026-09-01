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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1788350400&amp;signature=b7d333caa3447a6190eb6616e2414c1c112f68cdcfd33c53ebe7707bf0f7a52b&amp;req=diYjFM56mYRXXvMW3nq%2Bgedb6OKoO%2FmhzIcq3yJnhzTKMxEstvf6s8QhmG1N%0AVZKSfaRU5d1HzeKA62Eua5LVsAw%3D%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1788350400&amp;signature=05bad3d03f2d06b46bd216f40ec10dc20fd34753a1969643aafd8337dde5cf0c&amp;req=diYjFM56mIRZW%2FMW3nq%2BgaqVzoRZCfFw6T229fxpgJhbJ%2Bux%2BdFQ%2BsaXdIPE%0AM90szgClo%2FA1DhcH0JRWMyK2yys%3D%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1788350400&amp;signature=4b40c07b70ed26087c784f72f78b1db76bd77c41a63fdd7e7c3fecfc8ca643ac&amp;req=diYjFM56m4VZX%2FMW3nq%2BgSYi3tJgWR8%2FbvkQyVZH%2FIO1HC6fzsxdt5TxdGtY%0AsCRNGmQkyDTjPZaU02nCW0p7tcU%3D%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1788350400&amp;signature=1eb7a2ad2b8009a57c84d0cab1ef2a61f521483bc4ad74d5d6378e81e2fb1ac4&amp;req=diYjFM54lYBeXvMW3nq%2BgdEmqwAl0FXlU2rbEUS4hjBoVf7ai2zhC7cJmQUQ%0Ak09VXld1J%2BlXtJwb0OmVTuQX8JE%3D%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1788350400&amp;signature=a7064394c00ce709a34d7b154249d1d281e60b1a3cd882067c836cc2ae5770e1&amp;req=diYjFM56m4hWXPMW3nq%2BgUCKK30fDwNq1hkfJ9dkjkEj9Ka2kZsmuk6w7v8v%0AyvYrnwTjnpIKooiIwgLdquyRSxg%3D%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1788350400&amp;signature=df09fa47cdba911687360bcae912d05c145333d65bb5733ad277253f3ce8cb51&amp;req=diYjFM56moNfWfMW3nq%2BgfEmBdsDA%2FmbnC59CTHuW4KiaQVFs%2B04dxfjPm4a%0AJf6hUzCOm%2FUHcUKgn5PaC1EFvPQ%3D%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.