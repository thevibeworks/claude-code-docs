Title: Anthropic Economic Index: Insights from Claude 3.7 Sonnet

URL Source: https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7

Markdown Content:
Last month, we launched the [Anthropic Economic Index](https://www.anthropic.com/economic-index)—a new initiative where we’re regularly releasing data and research aimed at understanding AI's effects on labor markets and the economy over time.

Today, we’re releasing our second research report from the Index, covering usage data on Claude.ai following the launch of [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet)—our newest and most capable model with strengths in agentic coding and a new “extended thinking” mode.

Briefly, our latest results are the following:

*   Since the launch of Claude 3.7 Sonnet, we’ve observed a rise in the share of usage for coding, as well as educational, science, and healthcare applications;
*   People use Claude 3.7 Sonnet’s new “extended thinking” mode predominantly for technical tasks, including those associated with occupations like computer science researchers, software developers, multimedia animators, and video game designers;
*   We're releasing data on augmentation / automation breakdowns on a task- and occupation-level. For example, tasks associated with copywriters and editors show the highest amount of _task iteration_, where the human and model co-write something together. By contrast, tasks associated with translators and interpreters show among the highest amounts of _directive_ behavior—where the model completes the task with minimal human involvement.

In addition, we’re releasing a first-of-its-kind bottom-up taxonomy of usage on Claude.ai. This new dataset covers 630 granular categories ranging from “Help resolve household plumbing, water, and maintenance issues” to “Provide guidance on battery technologies and charging systems.” We hope this bottom-up taxonomy will be useful for researchers, and reveal use-cases that might be missed by top-down approaches which map usage onto a list of predefined tasks.

The datasets for these analyses are [freely available to download](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

Read on for more details on our findings.

## What’s changed since the launch of Claude 3.7 Sonnet?

Last month, we introduced Claude 3.7 Sonnet, our most capable model yet with an “extended thinking mode”. We reran our [previous analysis](https://www.anthropic.com/news/the-anthropic-economic-index) on data from the 11 days following the launch, covering 1 million anonymized Claude.ai Free and Pro conversations. The vast majority of the data we analyzed was from Claude 3.7 Sonnet, as it is set as the default on Claude.ai and our mobile app.

As a reminder, our privacy-preserving analysis tool, [Clio](https://www.anthropic.com/research/clio), maps each conversation to one of 17,000 tasks in the U.S. Department of Labor’s O*NET database. We then look at the overall patterns in the occupations and high-level occupational categories associated with those tasks.

When looking at the breakdown of these 1 million conversations, we see that the proportion of usage in several occupational categories has increased modestly, including coding, education and the sciences. While this increase in coding usage was expected due to Claude 3.7 Sonnet’s improved scores on coding benchmarks, the increase in these other categories could reflect either ongoing diffusion of AI throughout the economy, novel applications of coding to those domains, or unexpected capability improvements in the model.

![Image 1: In the two months since our original data sample, we’ve seen an increase in the share of usage for coding, education, and the sciences. Graph shows share of Claude.ai Free and Pro traffic across top-level occupational categories in O*NET. Grey shows the distribution from our first report covering data from Dec ‘25 - Jan ‘25. Colored bars show an increase (green) and decrease (blue) in the share of usage for our new data from Feb ‘25 - March ‘25. Note that the graph shows the share of usage rather than absolute usage. See Appendix for chart showing change across the full list of occupational categories.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0cb42a56faa661d920d185e0009c36046bfaf481-1650x1245.jpg&w=3840&q=75)

_In the two months since our original data sample, we’ve seen an increase in the share of usage for coding, education, and the sciences. Graph shows share of Claude.ai Free and Pro traffic across top-level occupational categories in O*NET. Grey shows the distribution from our first report covering data from Dec ‘25 - Jan ‘25. Colored bars show an increase (green) and decrease (blue) in the share of usage for our new data from Feb ‘25 - March ‘25. Note that the graph shows the share of usage rather than absolute usage. See Appendix for chart showing change across the full list of occupational categories._

## How are people using extended thinking mode?

Claude 3.7 Sonnet features a new “extended thinking” mode which, when activated by the user, enables the model to think for longer when answering more complex questions.

Our analysis reveals that Claude 3.7 Sonnet's extended thinking mode is predominantly used in technical and creative problem-solving contexts. Tasks associated with computer and information research scientists lead with almost 10% using extended thinking, followed by software developers at around 8%. Tasks associated with digital creative roles like multimedia artists (~7%) and video game designers (~6%) also show substantial usage.

While these early usage patterns reveal insights about when people choose to use extended thinking mode, many important questions remain about this new model capability. To enable further research in this space, we’re releasing a new dataset that maps each O*NET task to its associated thinking mode fraction. This dataset is available on our [Hugging Face page](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

![Image 2: What tasks see the highest associated usage of extended thinking mode? Graph shows the O*NET occupations with highest usage of thinking mode in their associated tasks. Occupations shown are limited to those with at least 0.5% representation in the data.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0dba23183a67a9e7277e27ffb822f36cc8c7a0b1-1650x2118.jpg&w=3840&q=75)

_What tasks see the highest associated usage of extended thinking mode? Graph shows the O*NET occupations with highest usage of thinking mode in their associated tasks. Occupations shown are limited to those with at least 0.5% representation in the data._

## How does augmentation vs. automation vary by task and occupation?

In our last report, we analyzed how AI usage varied between _augmentative_ uses, like learning or iterating on an output, and _automative_ uses, like asking the model to directly complete a task or debug errors. Our analysis shows the balance of augmentation and automation is essentially unchanged in our new data, with augmentation still comprising 57% of usage. However, we did see some change in _types_ of automation and augmentation uses—for example, we saw _learning_ interactions, where the user asks Claude for information or explanation about different topics, rise from ~23% to ~28%.

![Image 3: The balance of augmentation and automation has stayed relatively constant in the two months between our data samples (V1 and V2), though the share of Learning conversations has grown appreciably.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fda559605646728c935d3557b6c30286f14dfc0b8-1650x1364.jpg&w=3840&q=75)

_The balance of augmentation and automation has stayed relatively constant in the two months between our data samples (V1 and V2), though the share of Learning conversations has grown appreciably._

We received a number of requests via our [researcher input form](https://docs.google.com/forms/d/e/1FAIpQLSfDEdY-mT5lcXPaDSv-0Ci1rSXGlbIJierxkUbNB7_07-kddw/viewform) to release automation and augmentation data at the level of tasks and occupations. We do just that in this report, providing this data on our [Hugging Face page](https://huggingface.co/datasets/Anthropic/EconomicIndex/).

When splitting the data by high-level occupational categories, we find some categories are highly augmentative; for example, Community and Social Service tasks, which includes education and guidance counseling, approach 75% augmentation. At the other end of the extreme, tasks associated with production or computer and mathematical occupations, we see the balance skew closer to 50-50%. We don’t see any occupational categories where automation dominates.

![Image 4:  Proportion of different interaction modes across high-level occupational categories. Occupational categories shown are limited to those with at least 0.5% representation in the data.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff7c11a7bc170169839903b4ab5e1ed2c596a8904-1650x1973.jpg&w=3840&q=75)

_Proportion of different interaction modes across high-level occupational categories. Occupational categories shown are limited to those with at least 0.5% representation in the data._

Getting more granular, we can also look at specific occupations within these occupational categories, as well as tasks associated with that occupation. For example, tasks associated with copywriters and editors show the highest amount of _task iteration_, where the user iterates on various writing and editing tasks with the model. By contrast, tasks associated with Translators and Interpreters show among the highest amounts of _directive_ behavior—where the model is used for translating documents with minimal human involvement. Note that the O*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation “fine artists, including painters, sculptors, and illustrators,” Claude is probably used far more for creating digital art than for painting or sculpture.

![Image 5](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3b2fa3226418804af9a16c9d617aab52cf3ce100-1650x1364.jpg&w=3840&q=75)

![Image 6](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5500563fb3975ad224be661ba207598873674b1a-1650x1364.jpg&w=3840&q=75)

_Top occupations by interaction type. For each of the five interaction categories (Learning, Task Iteration, Validation, Directive, and Feedback Loop), we plot the occupations with the highest usage proportion within that category. For example, librarians show the highest proportion of learning interactions at ~56%, while copy writers lead in Task Iteration at ~58%. Each panel includes the O*NET task within the occupation that contributed most strongly to that interaction pattern; this is based on both how frequently the task occurs and how often that interaction mode is used within the task. Figures for the other learning modes are shown in the Appendix._ _Note that the O*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation “fine artists, including painters, sculptors, and illustrators,” usage on Claude.ai probably tilts more towards digital art than sculpture. Only occupations with at least 0.5% representation in the overall dataset are shown._

## A bottom-up taxonomy of usage on Claude.ai

Our research so far has relied on the O*NET dataset of tasks and occupations, which was created and maintained by the US Department of Labor. While O*NET covers a very large number of tasks, O*NET may not be the best taxonomy to describe the capabilities of general purpose models which can be used for tasks which are not present in O*NET—and thus might be missed by our analysis.

To address this gap, we’re releasing a new bottom-up dataset of user activity patterns on Claude.ai. This dataset was also created with Clio, and uses the same dataset of anonymized conversations used for the above analysis, meaning that it enables comparisons between top-down and bottom-up approaches. It consists of 630 granular clusters, with associated descriptions, prevalence metrics, and automation/augmentation breakdowns, organized into three levels of hierarchy.

While we leave detailed analysis of this dataset to future work, we highlight a few particularly interesting clusters:

*   Help with water management systems and infrastructure projects
*   Create physics-based simulations with interactive visualization capabilities
*   Help me with font selection, implementation, and troubleshooting
*   Help me create or improve job application materials
*   Provide guidance on battery technologies and charging systems
*   Help with time zone handling in code and databases

## Conclusion

As models continue to advance, so too must our measurement of their economic impacts. In our second report, covering data since the launch of Claude 3.7 Sonnet, we find relatively modest increases in coding, education, and scientific use cases, and no change in the balance of augmentation and automation. We find that Claude’s new extended thinking mode is used with the highest frequency in technical domains and tasks, and identify patterns in automation / augmentation patterns across tasks and occupations. We release datasets for both of these analyses.

In the coming months, we aim to continue tracking these metrics and developing new ones as capabilities improve and models continue to be applied across the economy.

## Work with us

If you’re interested in [working](https://www.anthropic.com/jobs) at Anthropic to research the effects of AI on the labor market, we encourage you to apply for our Societal Impacts Research Scientist and Research Engineer roles, as well as our Economist role.

## Appendix

We share a few additional results and technical details in this appendix.

### Task Curve

We also recompute the “depth of task usage” plot from our original paper. We find generally a very similar curve to our first analysis. If anything we see slightly less area under the curve for the newer model—perhaps owing to an increase in concentration in our sample of conversations towards coding. That said, while we haven’t seen a dramatic change in this curve over the last two months, we will continue to monitor as model capabilities and product surfaces continue to advance.

![Image 7: The depth of task usage across occupations. For example, the graph shows that about 40% of occupations see AI usage in at least 20% of their tasks (where x=0.2, y≈0.4). There is little change in the curves between our first and second reports.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fbc1822466045491b08581839f6bf8f0c95cd778e-1650x1353.jpg&w=3840&q=75)

_The depth of task usage across occupations. For example, the graph shows that about 40% of occupations see AI usage in at least 20% of their tasks (where x=0.2, y≈0.4). There is little change in the curves between our first and second reports._

### Full change across occupational categories

![Image 8: Percentage share of usage across occupational categories, showing values from our original report (gray bars) with corresponding increases (yellow) and decreases (blue) in the second report. computer and mathematical occupations represent the category with the largest absolute increase (+3%), while several categories like education and the sciences show notable percentage increases.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd0b5ad8a21049019850309fbd5445638d2f4f8a6-1650x1806.jpg&w=3840&q=75)

_Percentage share of usage across occupational categories, showing values from our original report (gray bars) with corresponding increases (yellow) and decreases (blue) in the second report. computer and mathematical occupations represent the category with the largest absolute increase (+3%), while several categories like education and the sciences show notable percentage increases._

### Results for other interaction modes

![Image 9](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F94b286d3ab0cd6e45c561b8117f115e82ddb79fd-1650x1364.jpg&w=3840&q=75)

![Image 10: Top occupations by interaction type. For each of the five interaction categories (Learning, Task Iteration, Validation, Directive, and Feedback Loop), we plot the occupations with the highest usage proportion within that category. For example, librarians show the highest proportion of learning interactions at ~56%, while copy writers lead in Task Iteration at ~58%. Each panel includes the O*NET task within the occupation that contributed most strongly to that interaction pattern; this is based on both how frequently the task occurs and how often that interaction mode is used within the task. Figures for the other learning modes are shown in the main body of the post.    Note that the O*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation “fine artists, including painters, sculptors, and illustrators,” usage on Claude.ai probably tilts more towards digital art than sculpture. Only occupations with at least 0.5% representation in the overall dataset are shown.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F88ce923d09c12321a657070448dbf7d99cf77ec3-1650x1364.jpg&w=3840&q=75)

_Top occupations by interaction type. For each of the five interaction categories (Learning, Task Iteration, Validation, Directive, and Feedback Loop), we plot the occupations with the highest usage proportion within that category. For example, librarians show the highest proportion of learning interactions at ~56%, while copy writers lead in Task Iteration at ~58%. Each panel includes the O*NET task within the occupation that contributed most strongly to that interaction pattern; this is based on both how frequently the task occurs and how often that interaction mode is used within the task. Figures for the other learning modes are shown in the main body of the post._ _Note that the O*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation “fine artists, including painters, sculptors, and illustrators,” usage on Claude.ai probably tilts more towards digital art than sculpture. Only occupations with at least 0.5% representation in the overall dataset are shown._

## Additional methodological details

While we mainly follow the methodology of our original report, we make a few changes which we document here for transparency:

*   In contrast to our last report, we do not filter based on whether conversations are relevant to an occupational category. Instead, we simply filter out conversations that flagged our safety classifiers. We find these approaches lead to similar results as our original analysis, while preserving more data that we can release via our bottom-up taxonomy of usage.
*   We use Claude 3.7 Sonnet in place of all cases where we previously used Claude 3.5 Sonnet. We found that using our newer model increased the accuracy of classifications according to the internal benchmarks we use to assess Clio’s accuracy.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
