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

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1789901100&amp;signature=b506338f58d4ca96ed1ab1e27b45fe2710b2efefb7588ba8bcc8c88644aa20c3&amp;req=diYjFM56mYRXXvMW1HO4zT%2FymECOFAimktHcEoeKC4flD8b8SgfNIkSVfV2I%0Aew6E%0A)

2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1789901100&amp;signature=c087aba031f9b30e49d6ef254525c025398b950708d1d956f29eafe32bd2346f&amp;req=diYjFM56mIRZW%2FMW1HO4zc116gdhQFGwMCr%2B42fbmkYW7EH22lEtpOYpuQSK%0ABpxY%0A)

Hover over the issue to see which requirement is not met.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1789901100&amp;signature=58e1d7169629c0b525432b139a799f63b65007bf9db9779a9257f194de0c025b&amp;req=diYjFM56m4VZX%2FMW1HO4zaveae9rlnzBVPpeIJbmktQUfxScyFEkcfJGqu3D%0AzgfY%0A)

3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1789901100&amp;signature=d11313ed8932155c3f8c50dc4ad811dc960f75c705246db51e0d9ff29eae7b6b&amp;req=diYjFM54lYBeXvMW1HO4zTU0lNKZK0dG9BWcjfiNKI3M9QlGjJm%2FwdM6ADWN%0AOtnH%0A)

4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1789901100&amp;signature=fceca85437dbaf4d3223fc8a9963a44cbdbb23471af52ccdb53f32d7e35b677d&amp;req=diYjFM56m4hWXPMW1HO4zQfcHTKn738q9apHi%2BiM8ojRIQLAR%2FGpYpNG9AXv%0AUk4K%0A)

5. The program shows **Active** for the workspace.

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1789901100&amp;signature=afea41e440ee542f1fb22ee319d66cb04e5fcd6a1feac9ae2cd742786bac67e3&amp;req=diYjFM56moNfWfMW1HO4zaUR8q9u9v85fTukdAE3MWvwAkGOYo7HMDoMk%2F%2BK%0A9i5r%0A)

## Troubleshooting

- **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.

- **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.

- **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.

- **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.