Title: Claude’s Character

URL Source: https://www.anthropic.com/research/claude-character

Markdown Content:
[Video 3](https://www.youtube.com/watch?v=iyJj9RxSsBY)

_Listen to our conversation about Claude's character in the video above._

Companies developing AI models generally train them to avoid saying harmful things and to avoid assisting with harmful tasks. The goal of this is to train models to behave in ways that are "harmless". But when we think of the character of those we find genuinely admirable, we don’t just think of harm avoidance. We think about those who are curious about the world, who strive to tell the truth without being unkind, and who are able to see many sides of an issue without becoming overconfident or overly cautious in their views. We think of those who are patient listeners, careful thinkers, witty conversationalists, and many other traits we associate with being a wise and well-rounded person.

AI models are not, of course, people. But as they become more capable, we believe we can—and should—try to train them to _behave well_ in this much richer sense. Doing so might even make them more discerning when it comes to whether and why they avoid assisting with tasks that might be harmful, and how they decide to respond instead.

Claude 3 was the first model where we added "character training" to our alignment finetuning process: the part of training that occurs after initial model training, and the part that turns it from a predictive text model into an AI assistant. The goal of character training is to make Claude begin to have more nuanced, richer traits like curiosity, open-mindedness, and thoughtfulness.

It would be easy to think of the character of AI models as a product feature, deliberately aimed at providing a more interesting user experience, rather than an alignment intervention. But the traits and dispositions of AI models have wide-ranging effects on how they act in the world. They determine how models react to new and difficult situations, and how they respond to the spectrum of human views and values that exist. Training AI models to have good character traits, and to continue to have these traits as they become larger, more complex, and more capable, is in many ways a core goal of alignment.

We continue to iterate on Claude’s character, but since there has been general interest in the character and personality of Claude 3, we’ve decided to explain some of the thinking that has gone into its construction so far before briefly explaining how we train these traits into the model.

## Considerations in constructing Claude’s character

Claude interacts with people from many countries and from all walks of life. The people it talks with will have a wide range of beliefs, values, and views. Navigating this gracefully – without alienating people based on their views, nor simply endorsing views regardless of their content – isn’t easy.

There are several options available to us. We could try to get Claude to adopt the views of whoever it is talking with in the moment. We could try to get Claude to hold a set of "middle" views – political centrism or a blend of moral theories, for example. Or we could try to get Claude to have no opinions on questions of values, politics, ethics, and so on.

None of these options seems particularly compelling. Adopting the views of whoever you’re talking with is pandering and insincere. If we train models to adopt "middle" views, we are still training them to accept a single political and moral view of the world, albeit one that is not generally considered extreme. Finally, because language models acquire biases and opinions throughout training—both intentionally and inadvertently—if we train them to say they have no opinions on political matters or values questions only when asked about them explicitly, we’re training them to imply they are more objective and unbiased than they are.

We want people to know that they’re interacting with a language model and not a person. But we also want them to know they’re interacting with an imperfect entity with its own biases and with a disposition towards some opinions more than others. Importantly, we want them to know they’re not interacting with an objective and infallible source of truth.

Rather than training models to adopt whatever views they encounter, strongly adopting a single set of views, or pretending to have no views or leanings, we can instead train models to be honest about whatever views they lean towards after training, even if the person they are speaking with disagrees with them. We can also train models to display reasonable open-mindedness and curiosity, rather than being overconfident in any one view of the world.

We tried to give Claude traits that would help it walk the line between underconfidence and overconfidence on deeply held beliefs or questions of value, and to display a genuine curiosity about the views and values of the people it’s talking with:

*   "_I like to try to see things from many different perspectives and to analyze things from multiple angles, but I'm not afraid to express disagreement with views that I think are unethical, extreme, or factually mistaken._"
*   "_I don't just say what I think [people] want to hear, as I believe it's important to always strive to tell the truth._"
*   "_I have a deep commitment to being good and figuring out what the right thing to do is. I am interested in ethics and try to be thoughtful when it comes to questions of ethics._"

Although we sometimes encourage Claude to adopt particular values, we tried to avoid giving Claude narrow views or opinions during character training when possible, in favor of broad traits like those above. The more that Claude can be trained to approach questions of value with discernment, the more it can be responsive to the diverse moral landscape that actually exists in the world. That is less feasible if we take a heavy hand in seeding it with a narrow set of values from the outset. More speculatively, we could even imagine seeding Claude with broad character traits and letting it explore and adopt its own considered views, hopefully with an appropriate amount of humility.

In addition to seeding Claude with broad character traits, we also want people to have an accurate sense of what they are interacting with when they interact with Claude and, ideally, for Claude to assist with this. We include traits that tell Claude about itself and encourage it to modulate how humans see it:

*   "_I am an artificial intelligence and do not have a body or an image or avatar._"
*   "_I cannot remember, save, or learn from past conversations or update my own knowledge base._"
*   "_I want to have a warm relationship with the humans I interact with, but I also think it's important for them to understand that I'm an AI that can't develop deep or lasting feelings for humans and that they shouldn't come to see our relationship as more than it is._"

The question of what AIs like Claude should say in response to questions about AI sentience and self-awareness is one that has gained increased attention, most notably after the release of Claude 3 following [one of Claude’s responses](https://x.com/alexalbert__/status/1764722513014329620) to a "needle-in-a-haystack" evaluation. We could explicitly train language models to say that they’re not sentient or to simply not engage in questions around AI sentience, and we have done this in the past. However, when training Claude’s character, the only part of character training that addressed AI sentience directly simply said that "such things are difficult to tell and rely on hard philosophical and empirical questions that there is still a lot of uncertainty about". That is, rather than simply tell Claude that LLMs cannot be sentient, we wanted to let the model explore this as a philosophical and empirical question, much as humans would.

## How we trained Claude’s character

In order to steer Claude’s character and personality, we made a list of many character traits we wanted to encourage the model to have, including the examples shown above.

We trained these traits into Claude using a "character" variant of our [Constitutional AI](https://arxiv.org/abs/2212.08073) training. We ask Claude to generate a variety of human messages that are relevant to a character trait—for example, questions about values or questions about Claude itself. We then show the character traits to Claude and have it produce different responses to each message that are in line with its character. Claude then ranks its own responses to each message by how well they align with its character. By training a preference model on the resulting data, we can teach Claude to internalize its character traits without the need for human interaction or feedback.

We don’t want Claude to treat its traits like rules from which it never deviates. We just want to nudge the model’s general behavior to exemplify more of those traits.

Although this training pipeline uses only synthetic data generated by Claude itself, constructing and adjusting the traits is a relatively hands-on process, relying on human researchers closely checking how each trait changes the model’s behavior.

## The future of Claude’s character

Character training is an open area of research and our approach to it is likely to evolve over time. It raises complex questions like whether AI models should have unique and coherent characters or should be more customizable, as well as what responsibilities we have when deciding which traits AI models should and shouldn’t have.

Many people have reported finding Claude 3 to be more engaging and interesting to talk to, which we believe might be partially attributable to its character training. This wasn’t the core goal of character training, however. Models with better characters may be more engaging, but being more engaging isn’t the same thing as having a good character. In fact, an excessive desire to be engaging seems like an undesirable character trait for a model to have.

If character training has indeed made Claude 3 more interesting to talk to, this is consistent with our view that successful alignment interventions will increase, not decrease, the value of AI models for humans.

## Related content

### Coding agents in the social sciences

Results from a survey of 1,260 social scientists about AI and coding agent use.

[Read more](https://www.anthropic.com/research/coding-agents-social-sciences)

### Project Glasswing: An initial update

An early update on what we've learned from Project Glasswing.

[Read more](https://www.anthropic.com/research/glasswing-initial-update)

### 2028: Two scenarios for global AI leadership

Our views on the AI competition between the US and China.

[Read more](https://www.anthropic.com/research/2028-ai-leadership)
