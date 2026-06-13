Title: Anthropic Education Report: How University Students Use Claude

URL Source: https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude

Markdown Content:
AI systems are no longer just specialized research tools: they’re everyday academic companions. As AIs integrate more deeply into educational environments, we need to consider important questions about learning, assessment, and skill development. Until now, most discussions have relied on surveys and controlled experiments rather than direct evidence of how students naturally integrate AI into their academic work in real settings.

To address this gap, we’ve conducted one of the first large-scale studies of real-world AI usage patterns in higher education, analyzing one million anonymized student conversations on Claude.ai.

The key findings from our Education Report are:

*   STEM students are early adopters of AI tools like Claude, with Computer Science students particularly overrepresented (accounting for 36.8% of students’ conversations while comprising only 5.4% of U.S. degrees). In contrast, Business, Health, and Humanities students show lower adoption rates relative to their enrollment numbers.
*   We identified four patterns by which students interact with AI, each of which were present in our data at approximately equal rates (each 23-29% of conversations): Direct Problem Solving, Direct Output Creation, Collaborative Problem Solving, and Collaborative Output Creation.
*   Students primarily use AI systems for creating (using information to learn something new) and analyzing (taking apart the known and identifying relationships), such as creating coding projects or analyzing law concepts. This aligns with higher-order cognitive functions on [Bloom’s Taxonomy](https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives). This raises questions about ensuring students don’t offload critical cognitive tasks to AI systems.

## Identifying educational AI usage

When researching how people use AI models, protecting user privacy is paramount. For this project, we used Claude Insights and Observations, or "[Clio](https://www.anthropic.com/research/clio)," our automated analysis tool that provides insights into how people are using Claude. Clio enables bottom-up discovery of AI usage patterns by distilling user conversations into high-level usage summaries, such as “troubleshoot code” or “explain economic concepts.” Clio uses a multi-layered, automated process that removes private user information from conversations. We built this process so it minimizes the information that passes from one layer to the next. We describe Clio’s privacy-first design in this [earlier blog](https://www.anthropic.com/research/clio).

We used Clio to analyze approximately one million anonymized 1 conversations from Claude.ai Free and Pro accounts tied to higher education email addresses.2 We then filtered these conversations for student and academic relevance—such as whether the conversation pertained to coursework or academic research—which yielded 574,740 conversations.3 Clio then grouped these conversations to derive aggregate education-related insights: how different academic subjects were represented; how students-AI interaction differed; and the types of cognitive tasks that students delegate to AI systems.

## What are students using AI for?

We found that students primarily use Claude to create and improve educational content across disciplines (39.3% of conversations). This often entailed designing practice questions, editing essays, or summarizing academic material. Students also frequently used Claude to provide technical explanations or solutions for academic assignments (33.5%)—working with AI to debug and fix errors in coding assignments, implement programming algorithms and data structures, and explain or solve mathematical problems. Some of this usage might also be cheating, which we discuss below. A smaller but still sizable portion of student usage was to analyze and visualize data (11.0%), support research design and tool development (6.5%), create technical diagrams (3.2%), and translate or proofread content between languages (2.4%).

Below is a more detailed breakdown of common requests across subjects.

![Image 1: Common student requests from the top four subject areas, based on the 15 most frequent requests in Clio within each subject.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7d9704a6edee6bb96a7f767621d83beadc039a0c-2400x1586.png&w=3840&q=75)

Common student requests from the top four subject areas, based on the 15 most frequent requests in Clio within each subject.

## AI usage across academic disciplines

We next examined which subjects showed _disproportionate_ use of Claude. We did so by comparing Claude.ai usage patterns with the number of U.S. bachelor's degrees awarded.4 The most disproportionately heavy use of Claude was in Computer Science: despite representing only 5.4% of U.S. bachelor's degrees, Computer Science accounted for 38.6% of conversations on Claude.ai (this might reflect Claude’s particular strengths in computer coding). Natural Sciences and Mathematics also show higher representation in Claude.ai relative to student enrollment (15.2% vs. 9.2%, respectively).

Conversely, Business-related educational conversations accounted for just 8.9% of conversations despite constituting 18.6% of bachelor's degrees, showing a disproportionately low use of Claude. Health Professions (5.5% vs. 13.1%) and Humanities (6.4% vs. 12.5%) were also less represented relative to student enrollment in these disciplines.

These patterns suggest that STEM students, particularly those in Computer Science, may be earlier adopters of Claude for educational purposes, while students in Business, Health, and Humanities disciplines may be integrating these tools more slowly into their academic workflows. This may reflect higher awareness of Claude in Computer Science communities, as well as AI systems’ greater proficiency at tasks performed by STEM students relative to those performed by students in other disciplines.

![Image 2: Comparing the percentage of Claude.ai student conversations that are related to an National Center for Education Statistics (NCES) subject area (gray) to the percentage of U.S. college students with an associated major (orange). Note that percentages don’t sum to 100% as some conversations were classified under the “Other” category from the NCES which we exclude from our analysis.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd22ea4cc33c603b51435e334c4311ffc5b1d7f5a-2400x1818.png&w=3840&q=75)

Comparing the percentage of Claude.ai student conversations that are related to an National Center for Education Statistics ([NCES](https://nces.ed.gov/programs/digest/d23/tables/dt23_318.20.asp?current=yes)) subject area (gray) to the percentage of U.S. college students with an associated major (orange). Note that percentages don’t sum to 100% as some conversations were classified under the “Other” category from the NCES which we exclude from our analysis.

## How students interact with AI

There are many ways of interacting with AI, and they’ll affect the learning process differently. In our analysis of how students interact with AI, we identified four distinct patterns of interaction, which we categorized along two different axes, as shown in the figure below.

The first axis was “mode of interaction”. This could involve:5 (1) **Direct** conversations, where the user is looking to resolve their query as quickly as possible, and (2) **Collaborative** conversations, where the user actively seeks to engage in dialogue with the model to achieve their goals. The second axis was the “desired outcome” of the interaction. This could involve: (1) **Problem Solving**, where the user seeks solutions or explanations to questions, and (2) **Output Creation**, where the user seeks to produce longer outputs like presentations or essays. Combining the two axes gives us the four patterns presented below.

![Image 3: Our taxonomy for student-AI conversations, along with sample conversation topics based on those surfaced by Clio.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5b3d52e53c95e4d3f7a3f5e3592f859c5358fd82-2400x1526.png&w=3840&q=75)

Our taxonomy for student-AI conversations, along with sample conversation topics based on those surfaced by Clio.

These four interaction styles were represented at similar rates (each between 23% and 29% of conversations), showing the range of uses students have for AI. Whereas traditional web search typically only supports direct answers, AI systems enable a much wider variety of interactions, and with them, new educational opportunities. Some selected positive learning examples include:

*   Explain and clarify philosophical concepts and theories
*   Create comprehensive chemistry educational resources and study materials
*   Explain muscle anatomy, physiology, and function concepts for academic assignments

At the same time, AI systems present new challenges. A common question is: “how much are students using AI to cheat?” That’s hard to answer, especially as we don’t know the specific educational context where each of Claude’s responses is being used. For instance, a Direct Problem Solving conversation could be for cheating on a take-home exam… or for a student checking their work on a practice test. A Direct Output Creation conversation could be for creating an essay from scratch… or for creating summaries of knowledge for additional research. Whether a Collaborative conversation constitutes cheating may also depend on specific course policies.

That said, nearly half (~47%) of student-AI conversations were Direct—that is, seeking answers or content with minimal engagement. Whereas many of these serve legitimate learning purposes (like asking conceptual questions or generating study guides), we did find concerning Direct conversation examples including:

*   Provide answers to machine learning multiple-choice questions
*   Provide direct answers to English language test questions
*   Rewrite marketing and business texts to avoid plagiarism detection

These raise important questions about academic integrity, the development of critical thinking skills, and how to best assess student learning. Even Collaborative conversations can have questionable learning outcomes. For example,“solve probability and statistics homework problems with explanations,” might involve multiple conversational turns between AI and student, but still offloads significant thinking to the AI. We will continue to study these interactions and try to better discern which ones contribute to learning and develop critical thinking.

## Subject-specific AI usage patterns

Students across disciplines engage with AI in different manners:

*   **Natural Sciences & Mathematics** conversations tended toward Problem Solving, such as “solve specific probability problems with step-by-step calculations” and “solve academic homework or exam problems with step-by-step explanations.”
*   **Computer Science**, **Engineering**, and **Natural Sciences & Mathematics** leaned towards Collaborative conversations, whereas **Humanities, Business, and Health**were more evenly split stronger between Collaborative and Direct conversations.
*   **Education** showed the strongest preference for Output Creation, covering 74.4% of conversations. However, this usage might stem from imperfections in our filtering methods. Many of these conversations involved “creat[ing] comprehensive teaching materials and educational resources” and “creat[ing] detailed lesson plans,” indicating that teachers are also using Claude for educational support. In total, Education made up 3.8% of all conversations.

This suggests that educational approaches to AI integration would likely benefit from being discipline-specific. Our data are a first step in helping recognize the variations in how students across subjects engage with AI.

![Image 4: Distribution of conversations across interaction styles, for each NCES subject.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F99474f14f372a13fd858e8bceb1e6add170ee1c4-2400x2054.png&w=3840&q=75)

Distribution of conversations across interaction styles for each NCES subject.

## Cognitive tasks students delegate to AI

We also explored how students delegate cognitive responsibilities to AI systems. We used [Bloom's Taxonomy](https://www.researchgate.net/publication/235465787_A_Taxonomy_for_Learning_Teaching_and_Assessing_A_Revision_of_Bloom's_Taxonomy_of_Educational_Objectives),6 a hierarchical framework used in education to classify cognitive processes from simpler to more complex. While the framework was initially intended for student thinking, we adapted it to analyze Claude’s responses when conversing with a student.

We saw an inverted pattern of Bloom's Taxonomy domains exhibited by the AI:

*   Claude was primarily completing higher-order cognitive functions, with Creating (39.8%) and Analyzing (30.2%) being the most common operations from Bloom’s Taxonomy.
*   Lower-order cognitive tasks were less prevalent: Applying (10.9%), Understanding (10.0%), and Remembering (1.8%).

This distribution also varied by interaction style. As expected, Output Creation tasks, such as generating summaries of academic text or feedback on essays, involved more Creating functions. Problem Solving tasks, such as solving calculus problems or explaining programming fundamentals, involved more Analyzing functions.

The fact that AI systems exhibit these skills does not preclude students from also engaging in the skills themselves—for example, co-creating a project together or using AI-generated code to analyze a dataset in another context—but it does point to the potential concerns of students outsourcing cognitive abilities to AI. There are legitimate worries that AI systems may provide a crutch for students, stifling the development of foundational skills needed to support higher-order thinking. An inverted pyramid, after all, can topple over.

## Limitations

Our research is grounded in real-world data. That has many advantages in terms of the validity of our findings and their application to educational contexts. However, it also comes with limitations that might affect the scope of our findings:

*   Our dataset likely captures early adopters, and might not represent the broader student population;
*   It's unclear how representative Claude use is relative to overall AI usage in education—many students use AI tools beyond Claude.ai, meaning that we present only a partial view of their overall AI engagement patterns;
*   There are likely both false positives and false negatives in how conversations were classified. We relied on conversations from accounts tied to higher education email addresses: some of these that were considered to be student-related by our classifier may actually be from staff or faculty members. Furthermore, other student conversations are likely on accounts tied to non-university email addresses;
*   Due to privacy considerations, we only analyze Claude.ai usage within a single 18-day retention window. Students’ usage likely differs across the year as their educational commitments fluctuate;
*   We only study what tasks students delegate to AI, not how they ultimately use AI outputs in their academic work or whether these conversations effectively support learning outcomes;
*   The categorization of student-AI conversations into academic disciplines may not fully capture interdisciplinary work where AI usage patterns may differ significantly;
*   Applying Bloom’s Taxonomy to the cognitive processes of an AI, as opposed to a student, is imperfect. Skills like Remembering are harder to quantify in the context of AI systems.

Institutional policies regarding AI use in education vary widely, and might significantly impact the patterns we observe in ways we cannot measure within this dataset.

## Conclusions and looking ahead

Our analysis provides a bird’s-eye view of where and how students are using AI in the real world. We recognize that we are only at the beginning of understanding AI's impact on education.

We've seen in our discussions with students and educators that AI can empower learning in remarkable ways. For example, AI has been used to support a [student's nuclear fusion reactor project](https://www.businessinsider.com/student-builds-nuclear-fusion-prototype-using-ai-glowing-plasma-orb-2024-9), and to facilitate [better communication between students and teachers in classrooms](https://www.sciencedirect.com/science/article/abs/pii/S0360131524001970?via%3Dihub).

But we are under no illusions that these initial findings entirely address the profound changes happening in education. AI is making educators' lives more challenging in all kinds of ways, and this research doesn't fully capture them. As students delegate higher-order cognitive tasks to AI systems, fundamental questions arise: How do we ensure students still develop foundational cognitive and meta-cognitive skills? How do we redefine assessment and cheating policies in an AI-enabled world? What does meaningful learning look like if AI systems can near-instantly generate polished essays, or rapidly solve complex problems that would take a person many hours of work? As model capabilities grow and AI becomes more integrated into our lives, will everything from homework design to assessment methods fundamentally shift?

These findings contribute to the ongoing discussions amongst educators, administrators, and policymakers about how we can ensure AI deepens, rather than undermines, learning. Further research will help us better understand how both students and teachers use AI, the connections to learning outcomes, and the long-term implications for the future of education.

## Anthropic’s approach to education

In addition to this Education Report, we are [partnering with universities](https://www.anthropic.com/news/introducing-claude-for-education) to better understand the role of AI in education. As an early step, we are experimenting with a Learning Mode that emphasizes the Socratic method and conceptual understanding over direct answers. We look forward to collaborating with universities on future research studies and more directly studying the effects that AI has on learning.

## Bibtex

If you’d like to cite this post, you can use the following Bibtex key:

```
@online{handa2025education,
author = {Kunal Handa and Drew Bent and Alex Tamkin and Miles McCain and Esin Durmus and Michael Stern and Mike Schiraldi and Saffron Huang and Stuart Ritchie and Steven Syverud and Kamya Jagadish and Margaret Vo and Matt Bell and Deep Ganguli},
title = {Anthropic Education Report: How University Students Use Claude},
date = {2025-04-08},
year = {2025},
url = {https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude},
}
```

## Acknowledgements

Kunal Handa* and Drew Bent* designed and executed the experiments, made the figures, and wrote the blog post. Alex Tamkin proposed initial experiments and provided detailed direction and feedback. Miles McCain iterated on the technical infrastructure necessary for all experiments. Esin Durmus, Michael Stern, Mike Schiraldi, Saffron Huang, Stuart Ritchie, Steven Syverud, and Kamya Jagadish provided valuable feedback and discussion. Margaret Vo, Matt Bell, and Deep Ganguli provided detailed guidance, organizational support, and feedback throughout.

Additionally, we appreciate helpful discussion and comments from Rose E. Wang, Laurence Holt, Michael Trucano, Ben Kornell, Patrick Methvin, Alexis Ross, and Joseph Feller.

#### Footnotes

1 These spanned an 18-day period on Claude.ai to continue managing data according to our [privacy and retention policies](https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-personal-data). For more information about how Clio protects privacy, see our [research blog](https://www.anthropic.com/research/clio).

2 In particular, we limit the analysis to accounts with email addresses associated with higher education institutions globally, such as emails with .edu and .ac.uk domains. We recognize that not all educational email addresses may be those of students. For this reason, we then filter the associated conversations to those likely addressing students’ schoolwork.

3 Clio uses Claude to filter conversations in an automated way. For this research, Clio filtered conversations to those “likely to be a student seeking help with academics, school work, studying, learning a new concept, academic research, etc?”. Our [previous paper on Clio](https://arxiv.org/abs/2412.13678) details and validates this filtering mechanism.

4 Via the [National Center for Education Statistics (NCES)](https://nces.ed.gov/programs/digest/d23/tables/dt23_318.20.asp?current=yes).

5 In our experiments, we used the terminology “Transactional” and “Dialogic” to classify conversations as we found those terms to most precisely capture the bottom-up interaction patterns surfaced by Clio. Specifically, we used Clio to classify a conversation as one of: Transactional Problem Solving, Transactional Output Creation, Dialogic Problem Solving, or Dialogic Output Creation; Clio was provided with an associated description for each interaction pattern. For ease of understanding, we use the terminology “Direct” and “Collaborative” in place of “Transactional” and “Dialogic” in this report.

6 In particular, we use [Anderson and Krathwohl's (2001) revision](https://books.google.com/books/about/A_Taxonomy_for_Learning_Teaching_and_Ass.html?id=JPkXAQAAMAAJ&source=kp_book_description) of Bloom's Taxonomy and their taxonomy of cognitive processes.

## Related content

### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

[Read more](https://www.anthropic.com/news/fable-mythos-access)

### Results from the first Anthropic Public Record

[Read more](https://www.anthropic.com/news/anthropic-public-record)

### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

[Read more](https://www.anthropic.com/news/tcs-anthropic-partnership)
