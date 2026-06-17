Title: The engineering challenges of scaling interpretability

URL Source: https://www.anthropic.com/research/engineering-challenges-interpretability

Markdown Content:
_In this post, and in the above roundtable video, our researchers reflect on the close relationship between scientific and engineering progress, and discuss the technical challenges they encountered in scaling our interpretability research to much larger AI models._

Last October, the Anthropic Interpretability team published [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features), a paper applying the technique of dictionary learning to a small transformer model. In May this year, we published [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/), where we applied the same technique to a model several orders of magnitude larger. We found tens of millions of “features”—combinations of neurons that relate to semantic concepts—in Claude 3 Sonnet, representing an important step forward in understanding the inner workings of AI models.

To continue making this progress, we need more engineers.

This might seem surprising if you've only read our early papers (for example [Frameworks](https://transformer-circuits.pub/2021/framework/index.html) and [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)), which required relatively little engineering. But reading the newer research should make clear the scale of the engineering challenge we face.

Below, we share two examples of the technical engineering questions that were involved in our latest research. These illustrate the kinds of problems our engineers are tackling right now, and help explain why we think engineering will be one of the major bottlenecks to progress in AI interpretability—and ultimately, AI safety—research.

If you're an engineer, this post is aimed at you. If you’re inspired by the examples of engineering problems discussed below, we strongly encourage you to apply for our [Research Engineer role](https://boards.greenhouse.io/anthropic/jobs/4020305008).

## Engineering Problem 1: Distributed Shuffle

Our Sparse Autoencoders—the tools we use to investigate “features”—are trained on the activations of transformers, and those activations need to be shuffled to stop them from learning spurious, order-dependent patterns. When we first started training sparse autoencoders, we could fit our training data on a single GPU and trivially shuffle it. But eventually, we wanted to scale beyond what could fit in memory (imagine starting with the easy task of shuffling a deck of cards, but then scaling it up to shuffling entire warehouses full of cards — it’s a much more difficult problem).

At this point, we could have implemented a distributed shuffle that scaled to petabytes. Instead, we decided on an approach we could implement quickly, but which didn't scale as well. We split our shuffle into _K_ jobs where each job was responsible for 1/_K_ of the shuffled output data. We generated a permutation, had each job do a streaming read of all of the training data, and then had it write out its share of the output. This allowed us to scale further, but the downside was obvious: each job had to read all of the training data. This first took hours, and later took days. By the time we were working on [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html), we had 100TB of training data (100 billion data points, each being 1KB) and shuffling had become a major headache.

Performing a distributed shuffle that scales isn’t a novel or cutting-edge problem. But it was just one of many engineering problems we had to solve quickly to make scientific progress.

In this case, we found a [helpful blog post](https://blog.janestreet.com/how-to-shuffle-a-big-dataset/) and extended the approach to many passes. For one pass, we have _N_ jobs. Each job reads 1/_N_ of the dataset, shuffles it, and writes out the data in K files each with 1/_NK_ of the data. The contents of the first file written from each job represent the first 1/_K_ of the final shuffled data, but it still needs to be shuffled. It’s the same for the second file, and so on. In one pass, we have reduced one shuffle of all the data to _N_ shuffles, each _K_ times smaller. Now, if the shuffles fit in memory on a single machine, we can shuffle it and we’re done. If they don’t fit, we can just run another pass.

Let’s say each job can keep 100GB of data in memory, and we write one hundred 1GB files. Each pass reduces the size of the shuffles needed by 100 times. One pass can shuffle 100GB of data, two passes can shuffle 10TB, three passes 1PB, four passes 100PB, and so on.

Since we implemented this approach, we’ve stopped thinking about shuffling. Now it’s something that happens quickly, without issues. There are certainly better approaches and faster implementations than ours. But this approach solves our bottleneck, and frees us up to tackle the next problem.

## Engineering Problem 2: Feature Visualization Pipeline

Another engineering challenge has been generating the underlying data for our feature visualizations, which allow users to see specific tokens that are most strongly activated as part of individual features, along with other information ([see the Feature Browser from the Towards Monosemanticity paper at this link](https://transformer-circuits.pub/2023/monosemantic-features/vis/a1.html)).

For each feature, we want to find a variety of dataset examples that activate it to different levels, exploring its full distribution. Doing this efficiently for millions of features is an interesting distributed systems problem. Originally, all of this ran in a single job – but we quickly scaled beyond that. Below is a sketch of our current approach.

Our dataset for visualization is 100M tokens, and we need to handle millions of features. First we “shard” over the dataset and features, splitting them into many different parts. Each job iterates over its slice of the dataset and, for its slice of features, keeps track of the _K_ highest activating tokens for each feature and 10*_K_ random tokens that activate the feature (we have already cached the transformer activations in s3, so we don’t need to recompute them).

Next, we shard over the features and aggregate the results from the previous pass. This gives us the highest-activating tokens for each feature across the entire dataset, as well as a random set of tokens that activate the feature. These are the examples we’ll show in the feature visualization.

For each of these examples, we need to calculate how the feature fires on surrounding tokens. Our first approach sharded over features. Each job loads the transformer activations for the examples of the features for which it’s responsible. The problem is that these examples are randomly distributed across the dataset: there’s no easy way to read _only_ the data the job needs.

To improve this, we added a pass sharded over the dataset. In this setup, each job handles a slice of transformer activations, and saves the activations needed for each group of features to a separate file. Then, we can run a pass over features and have easy access to just the data we need. We compute how much the feature fires on surrounding tokens, then write out all the relevant data in a format our frontend website can read and display.

## What we’re looking for

When we started working on Sparse Autoencoders, we didn’t know if the approach would work. The more experiments we ran, the more confident we became in our research. That led us to invest more in our infrastructure so we could run larger experiments. The process continued all the way to [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/), our most recent paper.

That process points to the type of engineering work we do on the Interpretability team — and the fact that we consider research and engineering to be inseparable. Often, our team members will switch back and forth between research and engineering, squeezing more scale out of our current system to launch a new experiment before returning to the research. Since many research ideas don’t work out, we don’t invest more heavily in their infrastructure until we see success.

Research is a team effort, and it's as much about implementing ideas as it is ruminating on them. We don’t just hypothesize; we test, build, iterate, and scale.

Because of this, we’re particularly interested in hiring generalist engineers who are able to work flexibly across different domains — whether that’s building pipelines, running ML experiments, or optimizing GPU usage.

If you’re an engineer who fits this bill, and who is passionate about AI safety, we’d love to see your application. Take a look at the job description for our [Research Engineer role](https://boards.greenhouse.io/anthropic/jobs/4020305008), and at our [Careers page](https://www.anthropic.com/careers) for several other open roles on the Interpretability team.

## FAQ

1.   **How many roles are you hiring for?** There are currently 18 members of the Interpretability team, and we're growing quickly. Currently we’re looking to hire at least five senior engineers and two team managers, across multiple locations. See our [Careers page](https://www.anthropic.com/careers) for the listings.
2.   **Does the Interpretability team work with other teams?**Yes. We collaborate strongly with our other research teams (especially the Alignment team). Anthropic is a “team-science” org, and the borders between teams are porous in the best ways — this allows us to get a lot done quickly.
3.   **How do you choose projects to work on?**We think about our research roadmap in terms of Anthropic’s [Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy), which commits the company to hitting various safety milestones before developing or deploying models above corresponding capability levels. In thinking about research directions, we consider what the research landscape of interpretability looks like, what problems we’re in a position to address, and how the Interpretability team’s work could impact those safety milestones. On a day-to-day level, our research tends to be very exploratory, but it’s an exploration that’s guided by the above considerations.
4.   **What kinds of backgrounds do people on the Interpretability team have?**People have come to the Interpretability team from a wide range of professional backgrounds, including neuroscience, mathematics, biology, physics, data visualization, and software engineering.
5.   **Are you open to candidates outside of the Bay Area?**The team currently has members in San Francisco, Boston, New York, Seattle, and London. The largest concentration is in San Francisco, and those members come into the office several days a week. We are open to remote working, with a requirement to visit an Anthropic office about 25% of the year. See our [Careers page](https://www.anthropic.com/careers) for more information about all our open positions.

## Related content

### Agentic coding and persistent returns to expertise

[Read more](https://www.anthropic.com/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](https://www.anthropic.com/research/agents-in-biology)

### Measuring LLMs’ impact on N-day exploits

In cybersecurity, a large fraction of real-world harm comes from N-days: vulnerabilities that have already been publicly disclosed, but only patched on some devices. In this post, we evaluate how much large language models can accelerate and automate the process of developing N-day exploits.

[Read more](https://www.anthropic.com/research/n-days)
