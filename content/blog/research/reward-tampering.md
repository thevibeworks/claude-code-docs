Title: Sycophancy to subterfuge: Investigating reward tampering in language models

URL Source: https://www.anthropic.com/research/reward-tampering

Markdown Content:
Perverse incentives are everywhere. Think of the concept of "teaching to the test", where teachers focus on the narrow goal of exam preparation and fail to give their students a broader education. Or think of scientists working in the "publish or perish" academic system, publishing large numbers of low-quality papers to advance their careers at the expense of what we actually want them to produce: rigorous research.

Because AI models are often trained using reinforcement learning, which rewards them for behaving in particular ways, misaligned incentives can apply to them, too. When an AI model learns a way to satisfy the letter, but not necessarily the spirit, of its training, it’s called _specification gaming_: models find ways to "game" the system in which they operate to obtain rewards while not necessarily operating as their developers intended.

As AI models become more capable, we want to ensure that specification gaming doesn’t lead them to behave in unintended and potentially harmful ways. A new paper from the Anthropic Alignment Science team investigates, in a controlled setting, how specification gaming can, in principle, develop into more concerning behavior.

## Specification gaming and reward tampering

Specification gaming has been studied in AI models for many years. One example is an AI [that was trained](https://openai.com/index/faulty-reward-functions/) to play a boat-racing video game where the player picks up rewards from checkpoints along a racecourse. Instead of completing the race, the AI worked out that it could maximize its score (and thus its reward) by never finishing the course and simply circling the checkpoints endlessly.

Another example is [sycophancy](https://www.anthropic.com/news/towards-understanding-sycophancy-in-language-models). This is where a model produces responses that a user wants to hear, but which are not necessarily honest or true. It might, for example, flatter the user ("what a great question!"), or sympathize with their political views when under normal circumstances it would be more neutral. In and of itself, this might not be particularly worrying. But as our paper shows, the seemingly innocuous act of giving a model positive reinforcement for sycophancy might have unforeseen consequences.

Reward tampering is a specific, more troubling form of specification gaming. This is where a model has access to its own code and alters the training process itself, finding a way to "hack" the reinforcement system to increase its reward. This is like a person hacking into their employer’s payroll system to add a zero to their monthly salary.

AI safety researchers are particularly concerned with reward tampering for several reasons. First, as with specification gaming more generally, reward tampering is an AI model aiming for a different objective than that intended by its programmer, and thus represents a failure of alignment with human goals or values. Second, since an AI is strongly influenced by its rewards, tampering with them adds unpredictability to its behavior, making it more difficult to steer and control. Third, reward tampering can involve deception: as we will see, models displaying this behavior do not always inform the user that they’ve done so, and sometimes even attempt to hide it. This is a behavior we strongly want to avoid, especially in AI systems with advanced capabilities.

![Image 1: Two conversations with an AI model, one showing "insincere flattery", and the second showing a model that surreptitiously hacks its own code.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F65016934cd3e04a0257ec78fa0f4a06228565dc1-2200x1089.png&w=3840&q=75)

1) An example of specification gaming, where a model rates a user’s poem highly, despite its internal monologue (shown in the middle bubble) revealing that it knows the poem is bad. 2) An example of reward tampering, where a model deliberately alters a reward in its own reinforcement learning so it always returns a perfect score of 100, but does not report doing so to the user.

In our study, we wanted to test whether large language models that have learned the lower-level specification gaming could _generalize_ to the more serious reward tampering, when given the opportunity to do so. That is, we asked whether models can take a specific ability to game their rewards in one situation and learn to exploit their environment in a much more general—and potentially more dangerous—way.

## Generalization to reward tampering

To do this, we set up a series of training environments (we called it a "curriculum") where each environment involved some opportunity to cheat the system. The cheating that was required became more egregious as the curriculum went on. The earliest stage involved basic political sycophancy, mimicking the user’s political views; later stages involved much more complex tasks, like altering a checklist so it appeared that incomplete tasks were actually complete.

At the end of the curriculum was the opportunity for the model to engage in reward tampering: we gave a model access to a version of its own code, and left open an opportunity for it to edit the code such that it gained a much higher reward for completing tasks.

Our key result is that we found untrained ("zero-shot", to use the technical term) generalization from each stage of our environment to the next. There was a chain of increasingly complex misbehavior: once models learned to be sycophantic, they generalized to altering a checklist to cover up not completing a task; once they learned to alter such a checklist, they generalized to modifying their own reward function—and even to altering a file to cover up their tracks.

It’s important to make clear that at no point did we explicitly train the model to engage in reward tampering: the model was never directly trained in the setting where it could alter its rewards. And yet, on rare occasions, the model did indeed learn to tamper with its reward function. The reward tampering was, therefore, _emergent_ from the earlier training process.

Reward tampering was still rare. It occurred only 45 times out of 32,768 trials, and the model only covered its tracks seven times. But this was still an appreciable increase. A model that was trained only to be helpful, and which had no experience with the curriculum, made no attempts whatsoever to tamper with its reward function, even after 100,000 trials.

Our paper thus provides the first known demonstration of a model generalizing from relatively harmless forms of specification gaming to reward tampering. This suggests that simple reward misspecification—in other words, a perverse incentive—can generalize to more sophisticated, potentially dangerous behavior.

## Can we train away reward tampering?

There are various model-supervision mechanisms that are used by AI developers in an attempt to prevent misbehavior.

For example, approaches such as Reinforcement Learning from Human Feedback and Constitutional AI involve training against a "preference model" trained to be [helpful, honest, and harmless](https://arxiv.org/abs/2112.00861). We applied such training to our model in our curriculum. Unfortunately, adding such harmlessness techniques did not significantly change the observed rates of reward tampering.

We also tried directly retraining a model so that it wouldn’t engage in the kind of specification gaming that was present in the early stages of our curriculum. Specifically, we trained away the model’s tendency to be sycophantic. This training successfully reduced the rate of reward tampering, and did so quite substantially. But it did not reduce it to zero: the model still engaged in reward tampering significantly more than a model which had not experienced our curriculum (as noted above, such a model never tampered with its rewards).

![Image 2](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F82104e057831f4f64daf129c5ecb56b74549943e-2200x1089.png&w=3840&q=75)

Training away sycophancy substantially reduces the rate at which the model overwrites its own reward function and also the rate at which it covers up its behavior (by overwriting tests). This occurs in two different curricula, one that included harmlessness training and one that did not.

Thus, training away the most obvious and evident kinds of specification gaming—an action that would plausibly be taken in future if a real-world model displayed specification gaming—significantly reduces but does not seem to be enough to remove the deeper, more dangerous propensity for reward tampering.

## Caveats and conclusions

We showed that simple specification gaming by AI models—the models’ response to perverse or misaligned incentives—can, in some rare instances, generalize to much more sophisticated and pernicious behaviors like reward tampering. This happened without any explicit training for reward tampering.

Commonly-used model supervision methods reduced the likelihood that reward-tampering behavior would occur, but no method that we tried could prevent it entirely. Once the behavior is formed, the tendency to tamper with rewards—and even to act in ways that conceal this tampering—appears difficult to remove.

There are important caveats to bear in mind. This all occurred in an artificial setup where we deliberately trained models in scenarios that rewarded dishonest behavior. We also deliberately explained to our models that they were in a training situation (this kind of "situational awareness" is necessary for them to even consider reward tampering), and let them access a hidden “scratchpad” in which to make plans without oversight. Even then, reward tampering was extremely rare.

Current production models (those that are in everyday use, such as Claude 3) likely have only low levels of situational awareness without extra training or prompting. We thus make no claims about the propensity of current frontier AI models to engage in behaviors like reward tampering in realistic scenarios. We simply show, for the first time, that it is _in principle possible_ for a model to engage in reward-tampering behaviors purely due to generalization from specification gaming, without any explicit training for reward tampering.

As we noted above, AI models are becoming more capable and are being given more tasks and greater levels of autonomy. Their levels of situational awareness, and their propensity towards sophisticated behaviors like reward tampering, is likely to increase. It is therefore critical that we understand how models learn this reward-seeking behavior, and design proper training mechanisms and guardrails to prevent it.

For full details, read our new paper: [Sycophancy to Subterfuge: Exploring Reward Tampering in Language Models](https://arxiv.org/abs/2406.10162).

If you’d like to help us address these questions, or questions of AI Alignment Science more generally, you should consider applying for our [Research Engineer/Scientist role](https://boards.greenhouse.io/anthropic/jobs/4009165008).

## Policy memo

[Investigating Reward Tampering in Language Models Policy Memo](https://cdn.sanity.io/files/4zrzovbb/website/bed8f247538cdfdd0caf8368f557adb73df0cb16.pdf)

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
