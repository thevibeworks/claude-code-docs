> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A first Kaplan–Meier curve: the 1963 leukemia trial of 6-MP

> Compare 6-MP against placebo with Kaplan–Meier curves from 42 remission times typed into the prompt.

![Two Kaplan–Meier plots: 6-MP and placebo remission curves with medians of 23 and 8 weeks (log-rank p = 0.00004), and the 6-MP curve three ways, with medians of 23, 16, and 10 weeks.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/clin-km-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=c4d20dad5701ebceb1d87c476424d2d3)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview.md). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts.md#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
In 1963 Freireich and colleagues published an early randomized, placebo-controlled trial of a chemotherapy drug: 42 patients under 20 with acute leukemia in remission got either 6-mercaptopurine (6-MP) or a placebo, and were followed until they relapsed or the trial was stopped, which happened early, once 6-MP was clearly ahead. These are the weeks each patient stayed in remission. A + means the patient was still in remission when the trial was stopped.

6-MP: 6, 6, 6, 6+, 7, 9+, 10, 10+, 11+, 13, 16, 17+, 19+, 20+, 22, 23, 25+, 32+, 32+, 34+, 35+
Placebo: 1, 1, 2, 2, 3, 4, 4, 5, 5, 8, 8, 8, 8, 11, 11, 12, 12, 15, 17, 22, 23

Draw the Kaplan–Meier curve of each arm, with tick marks for the + patients and the numbers at risk under the plot. Give the median remission time in each arm and compare the arms with a log-rank test. Then show me what happens to the 6-MP median if I count every + as a relapse, or if I leave those patients out. Explain each step as you would to a medical student.
```

## Reference analysis

Median remission 23 weeks on 6-MP against 8 on placebo (log-rank p = 0.00004): Kaplan–Meier curves from 42 remission times typed into the prompt. Mishandling the 12 patients still in remission gives a 6-MP median of 16 or 10 weeks instead. The data are the 42 patients analyzed when the trial Freireich and colleagues published in 1963 was stopped; both medians and χ² = 16.79 match the textbook values.

## Data

This example doesn't download any data.

References:

* Freireich E.J. et al., 'The effect of 6-mercaptopurine on the duration of steroid-induced remissions in acute leukemia: a model for evaluation of other potentially useful therapy', Blood 21(6):699–716 (1963), doi:10.1182/blood.V21.6.699.699
* Kleinbaum D.G. & Klein M., Survival Analysis: A Self-Learning Text, 3rd ed.
