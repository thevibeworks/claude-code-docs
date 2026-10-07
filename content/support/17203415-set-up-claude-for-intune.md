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

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

If you want to use Conditional Access with Claude for Intune, the app has to be registered in your Microsoft Entra tenant first. Until it is, Claude for Intune doesn't appear in the list of apps you can select in a Conditional Access policy.

Claude for Intune is registered the first time someone who is authorized to consent on behalf of the organization signs in with Microsoft. Choose one of these options:

- **Have a user sign in.** Go to claude.ai and select “Continue with Microsoft.” One successful sign-in is enough.

- **Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

After either option, Claude for Intune appears in Microsoft Entra and your Conditional Access admin can target it in a policy.

To require app protection at sign-in, target the Conditional Access rule at “All resources” with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Add Claude for Intune to your managed apps and make it available to BYOD devices.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791396000&amp;signature=bae990b7b7396d37fcae780ce1ad642408e87d7a31782c994154b3e93b4e27c4&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjDS621gAMLV2Uu0R4UPNpoHPiNrPDzINm8v%0A%2B5iH%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791396000&amp;signature=e164d2ef1150e8e5773d5bd0ab35b220e765fe9ab1b625cfde45c264d702fcbd&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzkuHWUQ7hR7Wh%2Bi70IZdaU6zX1i1nHAJWp%0AyTzj%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791396000&amp;signature=e6cc72ceef1c0320a136cb9dc5c58003825442161208f3795f2525c86462452a&amp;req=dicnFsh3mIZWWPMW1HO4zTni3ccqa5gs2SRx6amjj9EKz%2B1vpzkvaiF04yp5%0AZv4K%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791396000&amp;signature=ac2719c1cc64eb65e5f9e7b674fd27090358584443d69e0a1dbd2d49ac8dc8a5&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YlUfjQuDNNSLAHCCFpctJSPotTyxWol5b1K%0A%2BKDH%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791396000&amp;signature=06486f61bd2a4e7df4f6e2ed5dbb9021b3b90195e957f6526ca0f85a80681959&amp;req=dicnFsh3moZeXPMW1HO4zeVx8DQa6CqNoVYQxJ7ndH5lbQ7MOmuibWo88c1k%0AL7Ns%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791396000&amp;signature=6a80957c2b061b4698eed42813f79360aab2517840bc8c0ea08ca1bb022df7b6&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZIsBWtQ8LtTCoSp4D6o5mw05A43Ki%2FVEdzwT%0AZFMt%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791396000&amp;signature=8c35206006965db0486aedea90d3d15b4a0046bd05de32f8fce9c1981ae71bb0&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXB4%2B%2FPvtnJWY0xu8hzLh45aRPghkMo5zRR9R%0A6khd%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791396000&amp;signature=22009408cb24c76d3c7443a42d06d75cfec2dd21c0881073d849f4a045cbbaf4&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y0pVC3xOV2VWh%2B9zzErWZ%2F8q6cpQLs5JPJF%2F%0A1swT%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791396000&amp;signature=ab83b71fbb27918d34c4367bd431786008f810af2ff1932f6f1ef7776a52dbdb&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJAXWjsIKETwku7gMsuzQ2acG2L4PQnkoZyJ%0AyVzh%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791396000&amp;signature=fc88dfa3f2c3d097a4c4c4995608855fb1c480592273de52782da564ae3ea9f6&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIrwax312LT9vQL0W4Fxv9IiNbsCK%2FzW1XY%0AZyXo%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791396000&amp;signature=dfff1dd51107307635ea0a2bfa3dc20ecc86add04ce36e115702934ff66d8ce8&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NSJ0s7f8F6Cfy2R7u%2FBGQwioHaHg1o9p8HI%0AWSjI%0A)

7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.

8. In the **Assignments** tab, add a user group to assign the policy to them.

9. Review and create.

10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**

2. When you select apps, choose “Select custom apps” and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using “Select custom apps.”