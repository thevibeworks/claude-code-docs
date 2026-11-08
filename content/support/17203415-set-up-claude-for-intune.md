# Set up Claude for Intune

Claude for Intune is a managed version of Claude for iOS for organizations that use Microsoft Intune. This article explains how Intune admins add Claude for Intune in the Microsoft Intune admin center and which app to tell employees to install.

## What is Claude for Intune?

Claude for Intune is built for organizations that manage mobile devices with Microsoft Intune, including organizations that let employees work from personal iPhones and iPads.

- Claude for Intune is a separate app from the standard Claude app. Both are listed on the App Store.

- IT teams can apply Intune app-protection policies to Claude for Intune on company-owned and employee-owned iPhones and iPads.

- It signs in with Microsoft only.

- It supports Intune app-protection policies and Microsoft Entra Conditional Access.

## Requirements

Before you set up Claude for Intune, check that you meet these requirements:

- You have an Enterprise plan.

- Your organization uses Microsoft Intune, and you have access to the Microsoft Intune admin center.

- Employees sign in to Claude for Intune with Microsoft. Other sign-in methods aren't available in Claude for Intune.

- You’re using iOS or iPadOS version 18.0 or later.

- Anthropic has enabled Microsoft sign-in for your organization's email domains.

- If you use Conditional Access, Claude for Intune is registered in your Microsoft Entra tenant.

- An admin in your Microsoft Entra tenant has granted admin consent for Claude for Intune. This is required for every organization.

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

Before employees can sign in, an admin in your Microsoft Entra tenant needs to grant admin consent for Claude for Intune. This is required for every organization. It approves the permission Claude for Intune uses to work with Microsoft Intune app protection, and it registers the app in your tenant so you can select it in a Conditional Access policy.

**Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

To confirm it worked, in the Microsoft Entra admin center go to Enterprise applications, open "Claude for Intune (Public)", and select Permissions. "Microsoft Mobile Application Management" should be listed on the "Admin consent" tab. If it isn't, select "Grant admin consent" on that page.

**Note:** Employees signing in to Claude for Intune with "Continue with Microsoft" does not grant this consent; an Entra admin has to grant it.

If employees are signed out within a few seconds of signing in, this step has most likely not been completed. After granting admin consent, ask them to delete Claude for Intune, reinstall it, and sign in again.

To require app protection at sign-in, target the Conditional Access rule at "All resources" with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Install Claude for Intune on employees’ devices

How employees get Claude for Intune depends on how their iPhone or iPad is managed:

- **Personal devices not enrolled in Intune (app protection only):** You don’t need to add or assign the app in Intune. Employees install Claude for Intune from the App Store (it appears there as "**[Claude Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**") and sign in with "Continue with Microsoft." Your app-protection policy (step 2) applies after they sign in.

  - Optional: to also list it in Company Portal, add it as an iOS store app and assign the user group as "Available with or without enrollment."

- **Devices enrolled with Apple User Enrollment:** Employees install Claude for Intune from the App Store themselves. Intune can’t install an app added as an "iOS store app" on these devices, and Company Portal shows "This device needs to be managed before you can install apps."

- **Company-owned devices enrolled in Intune:** Add Claude for Intune as an iOS store app and assign it to a user or device group using the steps below. Employees install it from Company Portal, or you can make the assignment Required to push it to their devices.

To add Claude for Intune for enrolled company-owned devices:

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1794158100&amp;signature=7c807738fd77759cfa559116ac33c83f1f31289fe6cf781974522a6a6114400b&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjXQ52NhAMLV2Uu0R4Vf7LU3I082FLuqmLT9%0AffQf%0A)

2. Under Platforms, select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1794158100&amp;signature=96321e64d970230900e1a527880fa17c2f82d5a8fd982149ba6c99edeb2c6f09&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUnmtHuVQ7hR7Wh%2Bi73i%2FO3%2BoDEfOWFjTyXv%0APwpM%0A)

3. Click "+ Create." For the App type, select the "iOS store app," and click the "Select" button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1794158100&amp;signature=24899798b9e48adc24c9dce70547b08d442f0148da57d0294c2b7917b0475c6c&amp;req=dicnFsh3mIZWWPMW1HO4zTni3cIoZ5Yt2SRx6amjj9HIlEs1raZWrwe4vN0F%0AJ%2B2R%0A)

4. Search "Claude for Intune" and click the "Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the "Next" button:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1794158100&amp;signature=45c4b6225951995a261491ab2c69b7e25d15d853dd6a73214e7b32fee65c1903&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YxWcjovDNNSLAHCCFogQ0cR%2FsXeBSEdWFXk%0AkZa3%0A)

6. For **Assignments**, add the groups that should get the app: under Required to install it automatically, or under Available for enrolled devices so employees can install it from Company Portal. You can use user groups or device groups.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2741107114/8f15b0d179a54c2ca4effaad8577/55bed25a-4b20-47b0-9e89-7f8adc86c04f?expires=1794158100&amp;signature=5f741c55c59c5b71eb898cdfb2a230ddd997eec234ddec1d1500262824c962ae&amp;req=dicjF8h%2BmoBeXfMW1HO4zYaZMey9fPufmN%2B6UXepdg9lnT6h81H7R9DzqvoO%0AlVOz%0A)

7. Click "Next," review and create.

8. If you assigned the app as Required, it installs automatically; if Available, employees install it from Company Portal.

### 2. Apply an app-protection policy to Claude for Intune

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1794158100&amp;signature=9dfc57b82fb764af431d68a5c696a7e9fafa2fc8dd97bb8cb83bb147b2d7f422&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZI4DVto9LtTCoSp4D6qlNcBqggaFofdjNqM6%0AquFE%0A)

2. Under **Manage apps**, select "Protection":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1794158100&amp;signature=246e8c78f183ff3c4bd4596fdac3889351fd64f579746748b3b5e53abf5145dd&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXBs88PXsnJWY0xu8hzL7sTcpbdXsn5fLdiWB%0AJX7f%0A)

3. Click "+ Create" and then select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1794158100&amp;signature=0b38b6b55ce47408a9afb5d41f37a8da1aea7b8b4724c8e87b59c1cf52a61ede&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y09XB3JPV2VWh%2B9zzEo8%2BalFb%2FO6%2FsaRuGbg%0ACked%0A)

4. Enter Name in the **Basics** tab, then click "Next" to **Apps**. Set **Target policy to** "Selected apps." Click "+ Select custom apps":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1794158100&amp;signature=1dde921b31d13af811907d8c0827ba06ba0d239897a422c3d34bbe308ed6b54f&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJUVVjUJKETwku7gMsvYuoKUeoN0l0sArkMA%0ASROG%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking "Select":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1794158100&amp;signature=77e2594764b71e02993e205961fa30e4eb90cab5fe97ef9549c547940805bdb8&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYicpzaJ212LT9vQL0W4N6J0%2BGFMp04d4YNQv%0AnAzw%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking "Next":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1794158100&amp;signature=297c61c2abde2066ef3e65964b5cd5eada2c3442de496a89c2906a2ce2a3734c&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NGL3sDe8F6Cfy2R7u9RtLXT2XpKvds41%2F98%0Af1dN%0A)

7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.

8. In the **Assignments** tab, assign the policy to a user group that includes everyone who will use Claude for Intune—app-protection policies can only target user groups, not device groups. Make sure it also applies to unmanaged devices: don't limit it to Intune-managed devices with the device-type setting or an assignment filter, or employees on personal phones get signed out right after signing in*.*

9. Review and create.

10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**

2. When you select apps, choose "Select custom apps" and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using "Select custom apps."