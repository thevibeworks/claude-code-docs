Title: Set up the Claude LTI in Canvas by Instructure

URL Source: https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure

Markdown Content:
# Set up the Claude LTI in Canvas by Instructure | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#main-content)

[![Image 2: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Claude for Education](https://support.claude.com/en/collections/12630177-claude-for-education) 
3.   Set up the Claude LTI in Canvas by Instructure

# Set up the Claude LTI in Canvas by Instructure

March 16, 2026

Table of contents

[Creating Claude LTI Developer Key in Canvas](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_62540b0a37)[Installing Claude LTI as an App](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_6bf481f89d)[Turn on the Claude LTI Integration in Claude for Education organization settings](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_13754a113a)[Questions](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_f3b6c5a53c)

This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

## Creating Claude LTI Developer Key in Canvas

1.   In Canvas, sign in as an administrator and navigate to **Admin -> Developer Keys**. 
2.   Click "+ Developer Key" then "+ LTI Key." 
3.   Enter the following: 

    1.   **Key Name:** Claude LTI 
    2.   **Description:** Enter a short description for the Canva LTI 1.3 app 
    3.   **Redirect URIs:**[https://claude.ai/lti/launch](https://claude.ai/lti/launch) 
    4.   **Title:**Claude LTI 
    5.   **Target Link URI:**[https://claude.ai/lti/launch](https://claude.ai/lti/launch) 
    6.   **OpenID Connect Initiation Url:**[https://claude.ai/api/lti/login](https://claude.ai/api/lti/login) 
    7.   **JWK method:**[https://claude.ai/api/lti/keys](https://claude.ai/api/lti/keys) 

4.   Under **Additional Settings**, toggle Privacy Level to **Public**. 
5.   Under **Placements**, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options. 
6.   Click "Save." 
7.   Toggle the state to **On**.  

## Installing Claude LTI as an App

1.   In Canvas, go to Admin -> Settings -> Apps. 
2.   Click "View App Configurations" then select "+ App." 
3.   Select **Configuration Type** “By Client ID.” 
4.   Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas). 
5.   Click "Install" and refresh the course page. 

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1780230600&signature=9d10208641335333b6a8ee402c5045f5ce87f6bfd45b07be43257e089897eb97&req=dSYmF818n4VcWfMW1HO4zTEDauscmPOHEv2ojHLMylYvooRE78ipdfB0ARVy%0AAbetpZFdoFyWseyiIM4%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1780230600&signature=9d10208641335333b6a8ee402c5045f5ce87f6bfd45b07be43257e089897eb97&req=dSYmF818n4VcWfMW1HO4zTEDauscmPOHEv2ojHLMylYvooRE78ipdfB0ARVy%0AAbetpZFdoFyWseyiIM4%3D%0A)

## Turn on the Claude LTI Integration in Claude for Education organization settings

1.   In Claude for Education, sign in as an administrator. 
2.   Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. 
3.   Find **Canvas** and click "Enable." 
4.   In the settings modal that pops up, input the required information to enable the integration 

    1.   **Canvas Domain** 
    2.   **Client ID** (found in Canvas Admin -> Developer Keys) 
    3.   **Deployment ID** (found in Canvas Admin -> Settings -> Apps -> View App Configurations -> Claude LTI Settings Button -> Deployment ID) 

5.   Click "Save Changes." The integration should now show as enabled. 

## Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).

* * *

Related Articles

[FAQs on Using Claude for Education at Your University](https://support.claude.com/en/articles/11139144-faqs-on-using-claude-for-education-at-your-university)[Log in to your Claude account](https://support.claude.com/en/articles/13189465-log-in-to-your-claude-account)[Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)[Open Claude Desktop with a link](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link)[Open the Claude mobile app with a link](https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link)

Did this answer your question?

😞😐😃

Table of contents

[Creating Claude LTI Developer Key in Canvas](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_62540b0a37)[Installing Claude LTI as an App](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_6bf481f89d)[Turn on the Claude LTI Integration in Claude for Education organization settings](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_13754a113a)[Questions](https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure#h_f3b6c5a53c)

[![Image 4: Claude Help Center](https://downloads.intercomcdn.com/i/o/487548/17213f6a445c8e6e874b1f4b/fad85208982e639d11b9108df895a293.png)](https://support.claude.com/en/)

*   [Product](https://www.anthropic.com/product)
*   [Research](https://www.anthropic.com/research)
*   [Company](https://www.anthropic.com/company)
*   [News](https://www.anthropic.com/news)
*   [Careers](https://www.anthropic.com/careers)

*   [Terms of Service - Consumer](https://www.anthropic.com/terms)
*   [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
*   [Privacy Policy](https://www.anthropic.com/privacy)
*   [Usage Policy](https://www.anthropic.com/aup)
*   [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
*   [Compliance](https://trust.anthropic.com/)
