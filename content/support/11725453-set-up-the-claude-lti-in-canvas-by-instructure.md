# Set up the Claude LTI in Canvas by Instructure

This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

## Creating Claude LTI Developer Key in Canvas

1. In Canvas, sign in as an administrator and navigate to **Admin -> Developer Keys**.

2. Click "+ Developer Key" then "+ LTI Key."

3. Enter the following:

  1. **Key Name:** Claude LTI

  2. **Description:** Enter a short description for the Canva LTI 1.3 app

  3. **Redirect URIs:** <https://claude.ai/lti/launch>

  4. **Title:** Claude LTI

  5. **Target Link URI:** <https://claude.ai/lti/launch>

  6. **OpenID Connect Initiation Url:** <https://claude.ai/api/lti/login>

  7. **JWK method:** <https://claude.ai/api/lti/keys>

4. Under **Additional Settings**, toggle Privacy Level to **Public**.

5. Under **Placements**, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options.

6. Click "Save."

7. Toggle the state to **On**.

## Installing Claude LTI as an App

1. In Canvas, go to Admin -> Settings -> Apps.

2. Click "View App Configurations" then select "+ App."

3. Select **Configuration Type** “By Client ID.”

4. Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas).

5. Click "Install" and refresh the course page.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1784897100&amp;signature=6455619918b94cd973713f05cf32b9938427a70b30f716b16f15a2684ffbc625&amp;req=dSYmF818n4VcWfMW1HO4zTEDau8WkvSAEv2ojHLMylaRVicU6CnHBc%2B%2FAhco%0ASZcbwpiQXC3dR3Djn68%3D%0A)

## Turn on the Claude LTI Integration in Claude for Education organization settings

1. In Claude for Education, sign in as an administrator.

2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

3. Find **Canvas** and click "Enable."

4. In the settings modal that pops up, input the required information to enable the integration

  1. **Canvas Domain**

  2. **Client ID** (found in Canvas Admin -> Developer Keys)

  3. **Deployment ID** (found in Canvas Admin -> Settings -> Apps -> View App Configurations -> Claude LTI Settings Button -> Deployment ID)

5. Click "Save Changes." The integration should now show as enabled.

## Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).