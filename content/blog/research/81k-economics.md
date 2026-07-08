Title: What 81,000 people told us about the economics of AI

URL Source: https://www.anthropic.com/research/81k-economics

Markdown Content:
### Key findings:

*   _Our recent survey of 81,000 Claude users shows that people who work in roles that are more exposed to AI have more concerns about AI-driven job displacement. These concerns are also higher among early-career respondents._
*   _Those in the highest- and lowest-paid occupations report the largest productivity gains, most commonly from increases in scope (doing new tasks)._
*   _Respondents experiencing the largest speedups from AI express higher concern about job displacement._

In order to inform the public about the economic changes we’re observing with AI, our [Economic Index](https://www.anthropic.com/research/economic-index-march-2026-report) shares what work Claude is being asked to do, and in which jobs Claude is doing the largest share of tasks. To date, however, we’ve lacked information on how these usage patterns map onto people’s thoughts and impressions of AI.

Our recent [survey study with 81,000 Claude users](https://www.anthropic.com/features/81k-interviews) provides a way to connect people’s economic concerns with what we’ve quantified in Claude traffic.

The survey asked people about their visions and fears around advances in AI. Many of the thoughts that people shared touched on economic topics. We learned that many people fear job displacement—though they also feel more productive and empowered at work. In some cases, AI has enabled them to start businesses, or given them time for more important things; in others, AI feels stifling, or imposed on them by their employers.

The survey’s results provide initial evidence that [observed exposure](https://www.anthropic.com/research/labor-market-impacts) (our measure of AI displacement risk) is correlated with economic concern around AI. People in highly exposed occupations—as defined by the tasks Claude is observed performing—were more nervous about economic displacement. This is consistent with people being broadly aware of AI’s diffusion and potential impacts. We expand on our findings below.

## Who worries about job displacement?

_“Well like anyone who has a white collar job these days I'm 100% concerned, pretty much 24/7 concerned about losing my job eventually to A.I.”—Software engineer.1_

One fifth of the respondents in our survey voiced concern about economic displacement. Some worried about this in the abstract: one software developer cautioned about “the possibility of AI in its current state being used to replace junior positions.” Others lamented that their jobs, or aspects of their jobs, were being automated away. One market researcher said, “In terms of improving my capability, it's no doubt. [B]ut in the future AI may replace my work.” In some jobs, people felt it made their work harder. One software developer observed that “when AI arrived, the project managers started giving harder and harder tickets and bugs to solve.”

Throughout this report, we use Claude-powered classifiers to infer people’s attributes and sentiments from their responses. For example, many participants mention their line of work in passing or give informative details about their work life, which allows us to infer their occupation. Similarly, we quantify concerns about job loss by prompting Claude to identify and interpret direct quotes in which respondents indicate that their own role is at risk of AI-driven displacement. We give example prompts in [the Appendix](https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf).

Respondents’ perceived threat from AI was correlated with our [own measure of observed exposure](https://www.anthropic.com/research/labor-market-impacts), which reflects the percentage of a job’s tasks for which Claude is used. A respondent was more concerned about AI when our observed exposure measure for that respondent was higher. Elementary school teachers were less worried about their own displacement than software engineers, for example, consistent with the fact that Claude usage skews toward coding tasks.

We show this in Figure 1 below. The y-axis is the percentage of respondents in a given occupation who said that AI is already replacing their role or is likely to do so soon. The x-axis is observed exposure. The plot shows that, on average, people in more exposed occupations tended to express more concern about their jobs being automated away. For every 10-percentage-point increase in exposure, perceived job threat increased by 1.3 percentage points. People in the top 25% of exposure mentioned the worry three times as often as those in the bottom 25%.

![Image 1](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3cc91526f31561f390700d113a9091e6ad8c094b-1920x1080.png&w=3840&q=75)

**Figure 1: Perceived job threat from AI and Observed Exposure.**Percentage of respondents indicating some job threat from AI vs. the Observed Exposure measure from [Massenkoff and McCrory (2026)](https://www.anthropic.com/research/labor-market-impacts). A respondent was coded as indicating job threat if they said their role was already being replaced or substantially reduced, or that such changes were likely in the near term (coded using Claude). The green line shows a simple linear fit.

Another important worker characteristic is career stage. In previous research, we reported [tentative signs](https://cdn.sanity.io/files/4zrzovbb/website/a42bc3fc08283562f08fd8bdee8f6f9a3d506e87.pdf) of a slowdown in the hiring of recent graduates and early-career workers in the United States. For about half of respondents in this survey, we were able to infer career stage from their answers.2 We found that early-career respondents were much more likely to express concern about job displacement than senior workers.

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe734cb6470a143e7fafa0ec0e0b1070ea63118db-1920x1080.png&w=3840&q=75)

**Figure 2: Concern about economic displacement by career stage.**Percentage of respondents indicating some job threat from AI, by career stage. Both fields are inferred from free-form responses using Claude-powered classifiers.

## Who benefits from AI?

Using Claude to assess the survey responses, we rated the extent of people’s self-reported productivity gains from AI on a 1–7 scale, where 1 is “less productive,” 2 is “no change,” and each subsequent level denotes a larger gain. Responses that scored 7 included testimonials like, “It used to take months to make the website I [made] in 4-5 days”; Claude gave a 5 to statements like, “What might have taken four hours was accomplished in half the time,” and a 2 to ones like, “Personally, I had AI help me fix code on a website. But it took multiple passes to get the result I was after.”3

Overall, people reported meaningful productivity gains on average. The mean productivity rating was 5.1, corresponding to “substantially more productive.” Our respondents were, of course, active Claude users who were willing to take a survey. This could make them more likely to report productivity benefits than the average user. Some 3% reported negative or neutral impacts, and 42% did not give a clear indication on productivity.

This splits somewhat across income lines. The left panel in Figure 3 shows that people in high-paying jobs, like software developers, conveyed the largest productivity gains from AI. This result is not driven only by coding; it holds when we leave out computer and math occupations. It echoes a previous [Economic Index finding](https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf) that also favored higher-paid workers: in tasks requiring greater levels of education, Claude tended to reduce the time taken to complete a task (relative to doing it without AI) by a higher percentage.

Some of the lowest-paid workers describe high productivity gains as well. This included a customer service representative using “AI to save me a lot of time with creating a response based on another one.” And in some cases, people in low-wage jobs were using AI on technical side projects. One delivery driver, for example, was using Claude to start an e-commerce business, and a landscaper was building a music application.

![Image 3](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F054ba6248545bfe2908345aa00abb7baf0ad0e42-1920x1080.png&w=3840&q=75)

**Figure 3: Inferred productivity gain by occupation.**The left panel shows the mean inferred productivity benefit from AI (inferred using a Claude-powered classifier) by quartile of occupational median wage from the BLS. The right panel shows the same outcome, split by major occupational group. Error bars show 95% confidence intervals.

We look at this in more detail in the right panel of Figure 3, showing the inferred productivity gain by major occupational group. At the top are management occupations. These respondents are mostly entrepreneurs using Claude to build a business.4 The next highest category is computer and math, which includes software developers. The two groups exhibiting the mildest productivity improvements were workers in scientific and legal professions. Some lawyers worried about AI’s ability to follow precise instructions. For example: “I have given very specific rules about what is where, how to read a legal document, what I want it to do… but it diverges every time.”

A key question as AI diffuses through the economy is where the benefits will accrue—to workers, their managers, consumers, or corporations. Respondents indicated the recipient of these gains in about a quarter of interviews. Overall, most of these people cited benefits to themselves, through faster tasks, expanded scope, and freed-up time.5 But 10% of respondents who named a recipient said that employers or clients were asking for and getting more work. A smaller share mentioned benefits to AI companies, and an even smaller share said that AI would be a net negative. This depended on career stage: only 60% of early-career workers indicated that they personally benefited from AI, compared to 80% of senior professionals.

![Image 4](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4c1138907fd70ea69195da8100056a9e4801b030-1920x1080.png&w=3840&q=75)

**Figure 4: Where does the surplus from AI productivity go?** Among respondents who named a beneficiary of their AI productivity gains, the share identifying each destination.

## Scope and speed

Respondents also shared where they experienced gains in productivity. We separate this into scope, speed, quality, and cost. For example, many people using AI for coding tasks said things like, “I’m a non tech guy but now I’m a full stack developer.” This is an expansion of scope; AI unlocks new abilities for them. In contrast, some users sped up tasks they were already doing, like the accountant who said, “I built a tool that helps me finish a financing task in 15 minutes that used to take 2 hours.” Quality gains often came from more thorough checks of code, contracts, and other paperwork. And a small share of respondents mentioned the low cost of using AI: “[I]f I hire a social media manager it’s over my budget.”

We find that the most common productivity enhancement is in scope, which was cited by 48% of users who explicitly mentioned productivity effects. 40% of users who mentioned productivity emphasized speed.

![Image 5](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F197366411f5546a640214b38baaeb1402f950c74-1920x1080.png&w=3840&q=75)

**Figure 5: What kind of productivity gain do users report?**Share of respondents describing each type of productivity benefit.

People’s experience with Claude might also shape their concerns about AI. To assess this, we measured the speedup reported by respondents, by extracting whether their work was now much slower (which we coded as 1), showed no change in speed (4), or had become much faster (7).

We found that the relationship between speedup and perceived job threat is U-shaped (see Figure 6). The leftmost bar shows respondents who reported that AI slowed them down. These respondents were more likely to indicate that AI posed a significant threat to their livelihoods. For example, some creative workers, like fine artists and writers, found AI too stifling and rigid to help them at their own work. At the same time, they feared the diffusion of AI into creative fields would make it harder for them to find work.

![Image 6](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fed7b1b8b258c348ad2127b6de33a3802160fac28-1920x1080.png&w=3840&q=75)

**Figure 6: Job threat from AI and speedup.**Percentage of respondents who said that displacement at their own job was already happening or likely in the near term, by the level of inferred speedup.

For the remaining respondents, perceived job threat increases consistently with the level of speedup implied by their answers. This makes some economic sense: if the time required to do one’s tasks is shrinking quickly, there may be more uncertainty about the future viability of the role.

## Discussion

The Economic Index reveals what people do with AI. But another key input for understanding AI’s economic impact is to hear directly from people about their experience. The responses explored here show that people’s intuitions track the usage data: they worry most about AI’s effect in the jobs where we observe Claude doing the most work. We also find higher levels of economic anxiety among early-career workers, which aligns with past research.

There are also signs that Claude empowers its users. People are most likely to talk about benefits flowing to themselves rather than to employers or AI companies. High-wage workers were the most enthusiastic about the productivity impacts of AI, but people with low-wage jobs and lower levels of education also reported large productivity gains. Most respondents reported that Claude enhanced their capabilities in the form of broadening the scope of their work or speeding it up. But users experiencing the largest speedups were also the most nervous about AI’s job impacts.

There are key caveats to our analysis, owing to the nature of the data. First, our survey is limited to users of personal accounts on Claude.ai who chose to respond. Among other potential biases, these users could be more likely to perceive the benefits as flowing to themselves. Second, the users weren’t asked directly about many of the derived variables here, so our inferences on occupation, career stage, and other variables from contextual clues could be wrong. Relatedly, because the survey is open-ended, our measures are based on what respondents happen to mention; these findings should be confirmed in structured surveys that ask about these topics directly.

Still, the interviews surface real insights about people’s feelings around the economics of AI, showing how qualitative data can surface quantitative hypotheses. And the large share of economic-related concerns is a strong signal in itself.

### Citation

```
@online{massenkoff2026interviewer,
author = {Maxim Massenkoff and Saffron Huang},
title = {What 81,000 people told us about the economics of AI},
date = {2026-04-22},
year = {2026},
url = {anthropic.com/research/81k-economics},
}
```

### Appendix

See the final section of the [linked PDF](https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf).

### Acknowledgements

We thank the 80,508 Claude users who shared their stories.

Maxim Massenkoff led the analysis and wrote the blog post. Saffron Huang led the interview project and provided guidance throughout.

Zoe Hitzig and Eva Lyubich provided critical feedback and methodological guidance. Keir Bradwell and Rebecca Hiscott gave editorial support. Hanah Ho and Kim Withee contributed to design. Grace Yun, AJ Alt, and Thomas Millar implemented Anthropic Interviewer within Claude.ai. Chelsea Larsson, Jane Leibrock, and Matt Gallivan contributed to survey and experience design. Theodore Sumers contributed to the data processing and clustering infrastructure. Peter McCrory, Deep Ganguli, and Jack Clark provided critical feedback, direction and organizational support.

Additionally, we thank Miriam Chaum, Ankur Rathi, Santi Ruiz, and David Saunders for their discussion, feedback, and support.

## Related content

### A global workspace in language models

New interpretability research reveals an emergent mental workspace in Claude that holds internal thoughts that don’t appear in the model’s output.

[Read more](https://www.anthropic.com/research/global-workspace)

### Anthropic Economic Index report: Cadences

In our latest Economic Index report, we sample hourly for the first time to ask: When do people come to Claude? What do they produce with it? And how do they perceive AI's impact on their work?

[Read more](https://www.anthropic.com/research/economic-index-june-2026-report)

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](https://www.anthropic.com/research/project-fetch-phase-two)
