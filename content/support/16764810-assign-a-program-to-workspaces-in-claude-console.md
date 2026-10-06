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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1791271800&amp;signature=6123b60936fe7140d6b6c3a304bac2637e9aaffa77a548494a7825fb1b544c49&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymUiFEwivktHcEoeKC4eE6hzpsIkg4ZvDmsfb%0AGP9w%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1791271800&amp;signature=1f74d08f39c7935962fcce470f417d209981509fb6d2f7abbe65ba74acd4ed8b&amp;req=diYjFM56mIRZW%2FMW1HO4zc116w9qR1G5MCr%2B42fbmkbShbhUHmx8V3uglk6V%0A4QZ5%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1791271800&amp;signature=e683dc02d1ce01b69371e4a198631bb36845483d2f8edfc3ef5ca099526fe68b&amp;req=diYjFM56m4VZX%2FMW1HO4zaveaOdgkXzIVPpeIJbmktQUo2Z33SfNfqvr0h%2F6%0A4NvG%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1791271800&amp;signature=2f531fc037d823d09a39f1e159590674c48d1bc2234ec3d468947a7888940ab0&amp;req=diYjFM54lYBeXvMW1HO4zTU0ldqSLEdP9BWcjfiNKI0smu%2BLa6%2BBm7JZ9QNg%0AbSmj%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1791271800&amp;signature=9a28a4af5e98cfacc0bf5c60d98790374d59c77cffab536eade52897f266fe6d&amp;req=diYjFM56m4hWXPMW1HO4zQfcHDqs6H8j9apHi%2BiM8ogIt8%2BYY6RBwoB%2BkJrQ%0A960f%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1791271800&amp;signature=c9fcb54e555443bc5453a3494e1f5d82042acf3cd08050036d5cab46fa113233&amp;req=diYjFM56moNfWfMW1HO4zaUR86dl8f8wfTukdAE3MWsGE1s8nWJg6Qj5Z9OI%0AzeCD%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.