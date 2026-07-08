Title: The Anthropic Economic Index report: New building blocks for understanding AI use

URL Source: https://www.anthropic.com/research/economic-index-primitives

Markdown Content:
Is artificial intelligence really making people faster at work? What sort of tasks does AI support best? And how might it change the nature of people’s occupations?

At Anthropic, we’re measuring real-world AI use on an ongoing basis to answer questions exactly like these. Our privacy-preserving [analysis method](https://www.anthropic.com/research/clio) allows us to learn more about conversations on [Claude.ai](http://claude.ai/redirect/website.v1.8c7827ec-0b04-4b41-b050-c11405d6492b) (capturing uses by consumers) and our first-party API (mostly capturing uses by businesses).1 In past reports, we’ve assessed AI tasks by [occupation and wage level](https://www.anthropic.com/news/the-anthropic-economic-index), looked more closely at [software development](https://www.anthropic.com/research/impact-software-development), and studied AI use [by country and by US state](https://www.anthropic.com/research/economic-index-geography).

We’re now adding a new level of detail to our Economic Index. In our fourth report, we’re introducing what we’ve called **economic primitives**: a set of five simple, foundational measurements to track the economic impacts of Claude over time. Our initial set includes task complexity, skill level, purpose (work, education, or personal use), AI autonomy, and success.2 We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample for this report.

These primitives provide a leading indicator of AI’s potential economic impacts—and allow us to answer far more complex questions about how AI is already changing jobs. Our latest report, which samples conversations from November 2025 (predominantly using Claude Sonnet 4.5), uses our primitives to explore a wide range of questions that we wouldn’t otherwise be able to answer—including how Claude’s task-level success rates change for more complex tasks, and whether the use of Claude to date might portend a net-deskilling effect on many jobs.

You can read the fourth Economic Index report [here](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report). Below, we summarize its results.

## **What we’ve learned from our economic primitives**

We applied our economic primitives to questions about individual tasks, occupations, and then the possible aggregate impacts of the changes we observe. (Our full methodology—including details on how we tested the accuracy of our primitives—is described in chapter two of the [full report](https://www.anthropic.com/research/anthropic.com/research/anthropic-economic-index-january-2026-report).)

### Tasks

#### **Which tasks does AI speed up, and by how much?**

We found that more complex tasks were sped up the most by Claude. We measure this by what Claude estimates as the number of years of schooling required to understand the conversation’s inputs: in Claude.ai, tasks with prompts requiring a high school education (12 years) were sped up by a factor of 9, while those requiring a college degree (16 years) were sped up by a factor of 12. (On the API, the speedup was greater still.) These results imply that AI’s productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the [evidence](https://www.nber.org/papers/w32966) that white collar professionals are more likely to use AI at work.

This same trend holds—albeit in weaker form—when we adjust for tasks’ success rates. Claude successfully completes tasks that require a college degree 66% of the time, compared to 70% for those tasks that require less than a high school education. This reduces, but doesn’t eliminate, the overall effect: Claude’s impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate.

![Image 1](https://www-cdn.anthropic.com/images/4zrzovbb/website/748b522964169a031f15579194d8c8976ba80a79-1920x792.svg)

_**Speedup and success rate vs. human years of schooling.**The chart on the left shows a scatterplot of the relationship between speedup and human years of schooling, measured at the O*NET task level. The dashed lines show the line of best fit. The chart on the right shows the relationship with the success rate._

#### **What are the time horizons over which Claude can support tasks?**

[METR](https://metr.org/)’s measure of AI’s [task horizons](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) shows that longer tasks are harder for AI models to complete. But the length of time over which AI models can work is steadily increasing as models get better: this measure has now become a key indicator of AI progress.

We’re able to complement METR’s analysis using our economic primitives. In the graph below, we show Claude’s task-level success rates relative to the amount of time a human would take to do the same task, both on [Claude.ai](http://claude.ai/redirect/website.v1.8c7827ec-0b04-4b41-b050-c11405d6492b) and on our API:

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fbf18bd0b6c14a07cff03bad97dc720183a0ac507-3840x2800.png&w=3840&q=75)

_**Task success vs. human-only time.**This chart shows the relationship between task success (%) and the time the task would require a human to complete alone, all measured at the O*NET task level and split by platform. The dashed lines show the fit from a linear regression._

METR’s benchmark suggests that Claude Sonnet 4.5 (the model in our own analysis) achieves 50% success rates on tasks of 2 hours. By contrast, our own API data finds that Claude is 50% successful at tasks that take nearly twice as long (around 3.5 hours), and on Claude.ai, the duration is vastly longer still—around 19 hours. But this might not be as discordant as it seems: our methodology is different to METR’s in some important ways. In our sample, users can break down complex tasks into smaller steps, creating a feedback loop that allows Claude to correct course. And rather than a fixed set of tasks, our sample contains a form of selection bias: users bring tasks to Claude that they’re more confident will work.

Our analysis shows how Claude’s _effective_ time horizons might look different to those found in a study with a consistent set of tasks. We’ll track this indicator in further reports.

#### **How does the nature of Claude’s work vary across countries?**

We find that Claude completes very different kinds of tasks in countries at different stages of economic development. In countries with higher GDP per capita, Claude is used much more frequently for work or for personal use—whereas countries at the other end of the spectrum are more likely to use it for educational coursework. This fits a straightforward “adoption curve” story, in which lower-income countries show a large share of AI use on education and on a smaller number of work tasks, while AI use diversifies towards personal purposes as countries become richer.

These results align with recent work [by Microsoft](http://microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf) that associates AI use in education with lower per-capita income, and AI use for leisure with higher incomes. Our [recent partnership](https://www.anthropic.com/news/rwandan-government-partnership-ai-education) with the Rwandan government and ALX, a technology training provider, is designed with this in mind: participants begin by developing AI literacy, and we’re piloting a program for granting some graduates year-long access to Claude Pro, supporting the transition from educational use to a broader range of applications.

![Image 3](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d102cf4365e7743de4413f22dda33035de71038-1072x356.svg)

_**Per capita income predicts how Claude is used across countries.**Each plot shows the relationship between the share of a specific kind of use (work, coursework, or personal) for Claude.ai conversations, and log GDP per capita._

### Occupations

#### **Coverage**

In our [first report](https://www.anthropic.com/news/the-anthropic-economic-index), with data from January 2025, we found that 36% of jobs in our sample saw Claude being used for at least a quarter of their tasks. Pooling data across reports, this has risen to 49%. But once we account for Claude’s _success_ _rate_ (which we weight according to how often workers do that task and how long the task takes), we get a different picture of which jobs are most affected by the use of AI.

On the graph below, we plot that earlier measure of occupations’ task coverage along the _x_ axis, and our new, adjusted measure on the _y_ axis. Although the two are certainly correlated, we now find that some occupations (like data entry keyers and radiologists) are much more heavily affected by AI than task coverage alone would suggest, while others (like teachers and software developers) are relatively less affected.

![Image 4](https://www-cdn.anthropic.com/images/4zrzovbb/website/1fc34cf7333c83157f586f908b8f7ec2dc92afe2-857x712.svg)

_**Effective AI coverage vs. task coverage.**The plot shows the relationship between task effective AI coverage (%) and task coverage, measured at the occupation level. Effective AI coverage tracks the share of a worker’s time-weighted duties that AI could successfully perform, based on Claude.ai data. Task coverage is the share of tasks that appear in Claude.ai usage. The dashed line shows where effective AI coverage share equals task coverage._

That said, even our revised assessment is still limited: we only assess tasks that are performed on Claude.ai, and it’s not always clear how these conversations might map onto changes in the real world. This is an area we plan to dig into further in future.

#### **Task content**

A further question we asked is whether the tasks that AI covers represent the higher- or the lower-skilled components of a given occupation. Using an estimate that we create of the skill level required for each task, we find that Claude is relatively more likely to cover the tasks that require _higher_ education levels—specifically, tasks that require an average of 14.4 years of education (equivalent to a US associate’s degree), relative to the economy’s average of 13.2 (shown below). This aligns with our earlier finding that Claude is used more frequently by white-collar workers.

![Image 5](https://www-cdn.anthropic.com/images/4zrzovbb/website/ee80542ac5b4dc9fd097a391284e628ab5f5d239-713x425.svg)

_**Education level of all tasks vs. Claude-covered tasks.** The blue bars give the distribution of the predicted task-level education required for all tasks in the O*NET database, weighted by employment. The orange bars show the same, restricting to tasks that appear in Claude.ai data._

As an experiment, we estimated how removing these Claude-covered tasks would shift the task composition of people’s jobs. As a first-order effect, this would _deskill_ jobs on average, since it would remove those higher-education tasks. Professions like technical writers, travel agents, and teachers would be affected (as we discuss further in [the report](https://www.anthropic.com/research/anthropic.com/research/anthropic-economic-index-january-2026-report)), though a rarer few (like real estate managers) would see effects going the other way.

We’re not necessarily _predicting_ that this deskilling will occur: it’s possible that _even if_ AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn’t account for. (Of course, as models improve, the composition of tasks that AI covers will change, too.) That said, we think this offers a useful signal as to the most immediate effects that AI might have on occupations in the near future.3

### **Aggregate impact**

In our earlier research, we [estimated](https://www.anthropic.com/research/estimating-productivity-gains) that the widespread adoption of AI could increase US labor productivity growth by 1.8 percentage points per year over the next ten years—around double the trend rate. Our new primitives allow us to revisit this analysis.

Based on our estimates of task speedups alone, we replicated our earlier finding of a 1.8 percentage point increase (even when we added in our API data). But when we account for task _reliability_—that is, when we adjust our estimate of task-level time savings by the probability that the task is _successful_, our estimate falls by about one-third for tasks completed on [Claude.ai](http://claude.ai/redirect/website.v1.8c7827ec-0b04-4b41-b050-c11405d6492b) (to 1.2 percentage points per year), and by slightly more (to 1.0 percentage points) for the typically more challenging tasks completed on our API.

Even a 1 percentage point increase in annual labor productivity growth would still be notable: it would return US productivity growth to the rates of the late 1990s and early 2000s. And, as we mentioned in our [earlier research](https://www.anthropic.com/research/estimating-productivity-gains), this top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher. Indeed, since our survey, Claude has become substantially more powerful, with the release of Claude Opus 4.5.

## **Updates on our previous measures**

In addition to our primitives, we collected a new round of data on the measures we’ve been tracking in our previous reports. This allows us to pick out trends in AI use over the course of 2025, from January to November. Here, we mostly find only small evolutions from the results of previous analyses, which pointed to an uneven distribution of Claude use.

First, we find that the use of Claude has remained highly concentrated among certain tasks: even though our sample includes 3,000 unique work tasks on Claude.ai, the top ten account for 24% of the set, which has steadily increased from 21% in January 2025. More specifically, computer and mathematical tasks continue to dominate Claude use: they’re about a third of all conversations on Claude.ai, and nearly half of our API traffic.

Second, our new report finds that augmentation (52% of conversations) has overtaken automation (45%) as the most popular pattern of interaction with Claude on [Claude.ai](http://claude.ai/redirect/website.v1.8c7827ec-0b04-4b41-b050-c11405d6492b). This is a reversal of what we saw in our August sample (when automation led by 49% to 47%), but, when we assess this question over a longer time-frame, we still see a slow rise in _automation_’s share of tasks: augmentation led by 55% to 41% in January of last year, and by 55% to 42% in March.

Third, our latest analysis shows that the geographic concentration of AI use (as we [discussed last time](https://www.anthropic.com/research/economic-index-geography)) remains evident. The US, India, Japan, the UK, and South Korea still lead in overall Claude.ai use, and adoption remains well-explained by GDP per capita. That said, in the US, we’ve observed greater changes: Claude use has become noticeably more evenly distributed across US states. In fact, if this trend was sustained, our model predicts that Claude use would be equalized across the country within two to five years. We discuss this model in more detail [in the report](https://www.anthropic.com/research/anthropic.com/research/anthropic-economic-index-january-2026-report).

## **Conclusion**

The most immediate conclusion from our latest Economic Index report is that the impact of AI on the global workforce remains a highly uneven one: AI use remains concentrated in specific countries and occupations, and it affects some occupations in a very different way to others, as the evidence on task coverage suggests.

More generally, this report has given us a new baseline against which to compare our future surveys. As Claude improves, we expect it’ll be asked to take on harder tasks, and that it’ll likely find greater success. We also expect that tasks might move from [Claude.ai](http://claude.ai/redirect/website.v1.8c7827ec-0b04-4b41-b050-c11405d6492b) to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it’ll give us another possible indication of coming economic impacts, given the importance of business adoption for AI’s effect on productivity. Through our primitives, we’ll be able to measure how changes like these are beginning to impact real-world outcomes, including the nature of people’s work, and which people (and where) are likely to be most affected during this period of rapid technological transition.

In the meantime, researchers, journalists, and the public can use our data to inform their own research and thinking, and to provide an empirical foundation for the potential policy responses we might need. For much more detail on each of the areas we’ve discussed above, see our [full report](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report).

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
