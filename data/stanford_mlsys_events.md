# Stanford MLSys Seminar

**News**:

- WE’RE BACK! With [Francois Chaubard](https://www.linkedin.com/in/francois-chaubard-0a169448/) taking over, we are bringing this podcast back!
- In late 2023, we’re partnering with [CS 229s](https://cs229s.stanford.edu/fall2023/), Systems for Machine Learning, and CS 528 to offer a special **systems for machine learning limited series**! We’ll have talks on Mondays, 10:30-11:30 am PT. Stanford students can sign up for either class!
- In early 2023, we partnered with [CS 324](https://stanford-cs324.github.io/winter2023/), Advances in Foundation Models, to offer a special **foundation models limited series**! We had talks on certain Mondays and Wednesdays, 3:30-4:20 PM PT (see schedule below).
- Join our [email list](https://groups.google.com/forum/#!forum/stanford-mlsys-seminars/join) to get notified of the speaker and livestream link every week!.

## 2025 “Hidden Layer” Series

### Schedule

M 10/20/25

Tim Shi (OpenAI)

[Early Days at OpenAI and founding Cresta.ai](https://youtu.be/N62FTn0sAO0)

Abstract
We discuss the early days of OpenAI, the quest for superintelligence, and the founding of unicorn Cresta.ai.




**Bio:** Tim Shi is the Co-Founder & Board Member of Cresta. He started his PhD at Stanford AI Lab researching natural language processing and reinforcement learning. He was an early member of the OpenAI team in 2016 and made contribution to building safe AGI in digital environments. His work on (world of bits) laid foundation for web-based reinforcement learning agents. He co-founded Cresta in 2017 and Cresta was one of first companies to deploy generative AI in enterprise, including GPT based suggestions product in 2019. Cresta is backed by top investors including Sequoia, a16z, Greylock and helps drive hundreds of millions in ROI across Fortune 500 customers like United Airlines, US Bank and Verizon.





**[Livestream Link](https://youtu.be/N62FTn0sAO0)**

M 10/13/25

Beyang Liu (Sourcegraph)

[Coding Agents](https://youtu.be/hR6zyA-EUPo)

Abstract
Coding Agents as a category is only 5-6 months old yet has completely transformed the way that we code. Sourcegraph has been the market leader for code search which is a key ingredient in coding for large enterprise codebases. We deep dive into how Sourcegraph started and how they think about coding agents in the future specifically in mission critical codebases in large enterprises.




**Bio:** Beyang Liu (CTO Sourcegraph) - As co-founder of Sourcegraph, Beyang built one of the first modern code search engines and the first RAG coding assistant, both of which are now relied upon by engineering organizations like OpenAI, xAI, Tesla, Groq, Uber, Coinbase, Reddit, and CERN. Prior to Sourcegraph, Beyang conducted AI research under Dr. Daphne Koller at Stanford and was one of the early Palantir engineers who introduced the use of Apache Spark. Beyang is currently building Amp, a new multi-model coding agent in research preview that's built for programmers who care about speed, efficiency, and quality.





**[Livestream Link](https://youtu.be/hR6zyA-EUPo)**

## Systems for Machine Learning Limited Series

### Schedule

M 10/09/23

Martin Maas (Google Deepmind)

[A Taxonomy of Machine Learning for Systems Problems](https://www.youtube.com/watch?v=4_UdAR_5jqk)

Abstract
Machine learning has the potential to significantly improve computer systems. While recent research in this area has shown great promise, not all problems are equally well-suited for applying ML techniques, and some remaining challenges have prevented wider adoption of ML in systems. In this talk, I will introduce a taxonomy to classify machine learning for systems approaches, discuss how to identify cases that are a good fit for machine learning, and lay out a longer-term vision of how different systems can be improved using ML techniques, ranging from computer architecture to language runtimes.




**Bio:** Martin Maas is a Staff Research Scientist at Google DeepMind. His research interests are in language runtimes, computer architecture, systems, and machine learning, with a focus on applying machine learning to systems problems. Before joining Google, Martin completed his PhD in Computer Science at the University of California at Berkeley, where he worked on hardware support for managed languages and architectural support for memory-trace obliviousness.





**[Livestream Link](https://www.youtube.com/watch?v=4_UdAR_5jqk)**

M 10/23/23

Tim Dettmers (UW)

[Democratizing Foundation Models via k-bit Quantization](https://www.youtube.com/watch?v=EsMcVkTXZrk)

Abstract
Foundation models are effective tools for many tasks but are challenging to finetune and inference due to their GPU memory requirements. Compressing foundation models with k-bit quantization makes them more accessible with minimal resources, but k-bit quantization can lead to degradation in model quality. In this lecture, I will talk about fundamental insights into how to compress foundation models with quantization while maintaining their predictive performance. We will learn about emergent outliers in large language models (LLMs) and how they affect performance during 8-bit quantization. We will learn how to do effective k-bit compression of pretrained large language models such that we maximize their density of predictive performance per bit. We will also talk about how to do efficient fine-tuning of quantized 4-bit LLMs (QLoRA) and how this helps to build state-of-the-art chatbots.




**Bio:** Tim Dettmers is a graduating PhD student advised by Luke Zettlemoyer at the University of Washington in Seattle. He holds degrees in applied math and computer science and has a background in industrial automation. His primary research goal is to democratize foundation models by making them more efficient and accessible through quantization, sparsification, and building machine learning systems that use consumer-grade hardware. He is the creator of the bitsandbytes library. Tim runs a blog about deep learning, GPUs, and PhD life at timdettmers.com.





**[Livestream Link](https://www.youtube.com/watch?v=EsMcVkTXZrk)**

M 10/30/23

Deepak Narayanan (Nvidia)

[Training Large Language Models at Scale](https://www.youtube.com/watch?v=JA1l96tjrs4)

Abstract
Training LLMs efficiently is challenging for a few reasons: training can require yottaFLOPs of compute, and accelerators have limited memory capacity making it impossible to fit large models on even a multi-GPU server. Consequently, new methods of model parallelism such as tensor and pipeline parallelism have been proposed. Unfortunately, naïve usage of these methods leads to scaling issues at thousands of GPUs. In this talk, I describe various systems innovations incorporated into Megatron-LM (https://github.com/nvidia/megatron-lm) that allow us to run training iterations for models with up to a trillion parameters on thousands of GPUs.




**Bio:** Deepak is a Senior Applied Deep Learning Research Scientist in the ADLR group at NVIDIA, where he builds software systems to more efficiently train and serve LLMs. He graduated from Stanford with a Ph.D. in Computer Science in September 2021, where he was advised by Prof. Matei Zaharia.





**[Livestream Link](https://www.youtube.com/watch?v=JA1l96tjrs4)**

M 11/06/23

Travis Addair (Predibase)

[Serving 100s of Fine-Tuned LLMs on 1 GPU with LoRAX](https://www.youtube.com/watch?v=i6zVvfvIFpc)

Abstract
Smaller, specialized language models such as LLaMA-2-7b can outperform larger general-purpose models like GPT-4 when fine-tuned on proprietary data to perform a single task. But serving many fine-tuned LLMs in production can quickly add up to tens of thousands of dollars per month in cloud costs when each model requires its own dedicated GPU resources. LoRA Exchange (LoRAX) is an LLM inference system built for serving numerous fine-tuned LLMs using a shared set of GPU resources. With LoRAX, users can pack over 100 task-specific models into a single GPU, significantly reducing the expenses associated with serving fine-tuned models by orders of magnitude over dedicated deployments. In this seminar, we'll explore the challenges of serving fine-tuned LLMs in production, and the motivation behind building a system like LoRAX. We'll introduce parameter efficient fine-tuning adapters like Low Rank Adaptation (LoRA), and show how LoRAX dynamically loads and exchanges different adapters at runtime, leveraging a tiered weight cache to speed up this exchange process. Additionally, we'll show how LoRAX achieves high throughput with continuous multi-adapter batching, allowing requests from different fine-tuned adapters to batch together within a single decoding step.




**Bio:** Travis Addair is co-founder and CTO of Predibase, the AI platform for engineers. Within the Linux Foundation, he serves as lead maintainer for the Horovod distributed deep learning framework and is a co-maintainer of the Ludwig automated deep learning framework. In the past, he led Uber's deep learning training team as part of the Michelangelo machine learning platform.





**[Livestream Link](https://www.youtube.com/watch?v=i6zVvfvIFpc)**

Thanksgiving

M 11/27/23

Tianqi Chen (CMU)

[Bringing Foundational Models to Consumer Devices via ML Compilation](https://www.youtube.com/watch?v=InoNMvjs_vo)

Abstract
Deploying deep learning models on various devices has become an important topic. Machine learning compilation is an emerging field that leverages compiler and automatic search techniques to accelerate AI models. ML compilation brings a unique set of challenges: emerging machine learning models; increasing hardware specialization brings a diverse set of acceleration primitives; growing tension between flexibility and performance. In this talk. I then discuss our experience in bringing foundational models to a variety of devices and hardware environments through machine learning compilation.




**Bio:** Tianqi Chen is currently an Assistant Professor at the Machine Learning Department and Computer Science Department of Carnegie Mellon University. He is also the Chief Technologist of OctoML. He received his PhD. from the Paul G. Allen School of Computer Science & Engineering at the University of Washington. He has created many major learning systems that are widely adopted: XGBoost, TVM, and MLC-LLM.





**[Livestream Link](https://www.youtube.com/watch?v=InoNMvjs_vo)**

M 12/04/23

Dan Fu (Stanford, Together)

[Monarch Mixer: Making Foundation Models More Efficient](https://www.youtube.com/watch?v=IS59IwGLvVs)

Abstract
Machine learning models are increasingly being scaled in both sequence length and model dimension to reach longer contexts and better performance. However, existing architectures like Transformers scale quadratically along both these axes. In this talk I'll discuss Monarch Mixer (M2), a new architecture that uses the same sub-quadratic primitive along both sequence length and model dimension. M2 mixes information along the sequence and model dimensions using Monarch matrices, a simple class of expressive structured matrices that captures many linear transforms, achieves high hardware efficiency on GPUs, and scales sub-quadratically.




**Bio:** Dan Fu is a PhD student in the Computer Science Department at Stanford University, where he is co-advised by Christopher Ré and Kayvon Fatahalian. His research is at the intersection of systems and machine learning and focuses on developing algorithms and architectures to make machine learning more efficient.





**[Livestream Link](https://www.youtube.com/watch?v=IS59IwGLvVs)**

## About the MLSys Seminar

Machine learning is driving exciting changes and progress in computing.
What does the ubiquity of machine learning mean for how people build and deploy
systems and applications?
What challenges does industry face when deploying machine learning systems in
the real world, and how can academia rise to meet those challenges?

In this seminar series, we want to take a look at the frontier of machine
learning systems, and how machine learning changes the modern programming
stack.
Our goal is to help curate a curriculum of awesome work in ML systems to help
drive research focus to interesting questions.

We started livestreaming each talk in this seminar series every week on [YouTube](https://www.youtube.com/channel/UCzz6ructab1U44QPI3HpZEQ)
in Fall 2020, and we’ve been going strong ever since!
Every week we take questions from the live chat, and keep videos of the talks
available on YouTube afterwards as well.
Give our channel a follow, and tune in every week for an exciting discussion!

Read about our [motivation for starting this seminar](https://hazyresearch.stanford.edu/blog/2020-10-13-mlsys).

Check out our introductory video:

Stanford MLSys Seminar Episode 0: ML + Systems - YouTube

[Photo image of Stanford MLSys Seminars](https://www.youtube.com/channel/UCzz6ructab1U44QPI3HpZEQ?embeds_referring_euri=https%3A%2F%2Fmlsys.stanford.edu%2F)

Stanford MLSys Seminars

25.4K subscribers

[Stanford MLSys Seminar Episode 0: ML + Systems](https://www.youtube.com/watch?v=OEiNnfdxBRE)

Stanford MLSys Seminars

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=OEiNnfdxBRE&embeds_referring_euri=https%3A%2F%2Fmlsys.stanford.edu%2F)

0:00

0:00 / 11:49

•Live

•

## Foundation Models Limited Series

In early 2023 (Stanford winter quarter), we’re excited to partner with CS 324 to offer a special foundation model limited series!
We have an exciting slate of speakers from OpenAI, Google, Anthropic, Meta and more – the experts who are developing and deploying foundation models in practice.
Tune in and be sure not to miss it!

### Schedule

W 1/11/23

Tri Dao (Stanford, Adept AI)

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://www.youtube.com/watch?v=gMOAud7hZg4)

Abstract
Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms IO-aware -- accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).




**Bio:** Tri Dao is a PhD student in Computer Science at Stanford, co-advised by Christopher Ré and Stefano Ermon. He works at the interface of machine learning and systems, and his research interests include sequence models with long-range memory and structured matrices for compact deep learning models. His work has received the ICML 2022 Outstanding paper runner-up award.





**[Livestream Link](https://www.youtube.com/watch?v=gMOAud7hZg4)**

W 1/18/23

Ce Zhang (ETH, Together Compute)

[Optimizing Communications for Distributed and Decentralized Learning](https://www.youtube.com/watch?v=e7o2C0lPrKg)

Abstract
The rapid progress of machine learning in the last decade has been fueled by the increasing scale of data and compute. Today's training algorithms are often communication heavy, as a result, large-scale models are trained dominantly in a centralized environment such as data centers with fast network connections. This strong dependency on fast interconnections is becoming the limiting factor of further scaling, not only for the data center setting but also for alternative decentralized infrastructures such as spot instances and geo-distributed volunteer computes. In this talk, I will discuss our research in communication-efficient distributed learning and our current effort in training foundation models in a decentralized way.




**Bio:** Ce is an Assistant Professor in Computer Science at ETH Zurich. The mission of his research is to make machine learning techniques widely accessible---while being cost-efficient and trustworthy---to everyone who wants to use them to make our world a better place. He believes in a system approach to enabling this goal, and his current research focuses on building next-generation machine learning platforms and systems that are data-centric, human-centric, and declaratively scalable. Before joining ETH, Ce finished his PhD at the University of Wisconsin-Madison and spent another year as a postdoctoral researcher at Stanford, both advised by Christopher Ré. His work has received recognitions such as the SIGMOD Best Paper Award, SIGMOD Research Highlight Award, Google Focused Research Award, an ERC Starting Grant, and has been featured and reported by Science, Nature, the Communications of the ACM, and a various media outlets such as Atlantic, WIRED, Quanta Magazine, etc.





**[Livestream Link](https://www.youtube.com/watch?v=e7o2C0lPrKg)**

W 1/25/23

Aakanksha Chowdhery (Google Brain)

[Pathways Language Model and Model Scaling](https://www.youtube.com/watch?v=CV_eBVwzOaw)

Abstract
Large language models have been shown to achieve remarkable performance across a variety of natural language tasks using few-shot learning, which drastically reduces the number of task-specific training examples needed to adapt the model to a particular application. To further our understanding of the impact of scale on few-shot learning, we trained a 540-billion parameter, dense Transformer language model at Google, which we refer to as Pathways Language Model (PaLM). In this talk, we discuss the system considerations and model improvements necessary to train the PaLM model across 6144 TPU v4 chips using Pathways at very high efficiency levels. Next we share how scaling the model to 540B parameters results in state-of-the-art few shot learning results across hundreds of language understanding and generation benchmarks. We will also share some of the more recent works built on top of PaLM that push the SOTA in various domains and democratize access to natural language processing.




**Bio:** Aakanksha has led the effort on training large language models at Google Research which led to the 540B PaLM model. Aakanksha has also been a core member of the Pathways project at Google. Prior to joining Google, Aakanksha led interdisciplinary teams at Microsoft Research and Princeton University across machine learning, distributed systems and networking. Aakanksha completed her PhD in Electrical Engineering from Stanford University, and was awarded the Paul Baran Marconi Young Scholar Award for the outstanding scientific contributions in the field of communications and the Internet.





**[Livestream Link](https://www.youtube.com/watch?v=CV_eBVwzOaw)**

M 1/30/23

Stella Biderman (EleutherAI, Booz Allen Hamilton)

[Mechanistic Interpretability - Reverse Engineering Learned Algorithms from Transformers](https://www.youtube.com/watch?v=P7sjVMtb5Sg)

Abstract
Transformers are exceptionally powerful technologies that have quickly gone from smashing NLP benchmarks to being one of, if not the premier ML technology in a wide array of fields. Given their growing role in technological pipelines and society writ large, understanding how and why they work is a pressing issue. In this talk I give an overview of research on Mechanistic Interpretability, a field of work that has had substantial success picking apart transformers and understanding the algorithms that trained models use to reason. Topics covered include: the algorithm that toy LLMs can use to perform arithmetic accurately; how real-world LLMs do object identification; and how AlphaFold learns 2D projections of structures and then inflates them over time. Time permitting, I hope to discuss recent discoveries at EleutherAI currently under review for publication.




**Bio:** Stella Biderman is the head of research at EleutherAI, an online research lab that has revolutionized open access to large language models. She is best known for her work on democratizing LLMs, especially the GPT-Neo-2.7B, GPT-NeoX-20B, and BLOOM-176B models, all of which where the largest publicly available GPT-3-style LLMs in the world at time of release. Her work on publicly available datasets and evaluation frameworks has become an integral part of training foundation models in NLP. Her interest in open sourcing NLP models is primarily driven by her passion for interpretability research, a topic she has increasingly focused on as access to LLMs has increased. She proudly does not possess a PhD.





**[Livestream Link](https://www.youtube.com/watch?v=P7sjVMtb5Sg)**

W 2/01/23

Ludwig Schmidt (University of Washington)

[A data-centric view on reliable generalization](https://www.youtube.com/watch?v=brHeIKX8ayw)

Abstract
Researchers have proposed many methods to make neural networks more reliable under distribution shift, yet there is still large room for improvement. Are better training algorithms or training data the more promising way forward? In this talk, we study this question in the context of computer vision and OpenAI's CLIP model for learning from image-text data. First, we survey the current robustness landscape based on a large-scale experimental study involving more than 200 different models and test conditions. The CLIP models stand out with unprecedented robustness gains on multiple challenging distribution shifts. To further improve CLIP, we then introduce new methods for reliably fine-tuning models by interpolating the weights of multiple models. Finally, we investigate the cause of CLIP's robustness via controlled experiments to disentangle the influence of language supervision and training distribution. While CLIP leveraged large scale language supervision for the first time, its robustness actually comes from the pre-training dataset. Based on our findings, we will conclude with initial experiments to improve the pre-training datasets for image-text models.




**Bio:** Ludwig Schmidt is an assistant professor in the Paul G. Allen School of Computer Science & Engineering at the University of Washington. Ludwig's research interests revolve around the empirical foundations of machine learning, often with a focus on datasets, evaluation, reliable methods, and large models. Ludwig completed his PhD at MIT under the supervision of Piotr Indyk and was a postdoc at UC Berkeley hosted by Benjamin Recht and Moritz Hardt. Recently, Ludwig's research group contributed to multimodal language & vision models by creating OpenCLIP and the LAION-5B dataset. Ludwig's research received a new horizons award at EAAMO, best paper awards at ICML & NeurIPS, a best paper finalist at CVPR, and the Sprowls dissertation award from MIT.





**[Livestream Link](https://www.youtube.com/watch?v=brHeIKX8ayw)**

W 2/8/23

Colin Raffel (UNC, HuggingFace)

[Building Machine Learning Models like Open-Source Software](https://www.youtube.com/watch?v=0oGxT_i7nk8)

Abstract
Pre-trained models have become a cornerstone of modern ML pipelines thanks to the fact that they can provide improved performance with less labeled data on downstream tasks. However, these models are typically created by a resource-rich research group that unilaterally decides how a given model should be built, trained, and released, after which point it is left as-is until a better pre-trained model comes along to completely supplant it. In this talk, I will present a vision for building machine learning models in the way that open-source software is developed - by a distributed community of contributors who iteratively build valuable artifacts through a mature set of tools including version control, continuous integration, merging, and more.




**Bio:** Colin Raffel is an Assistant Professor at UNC Chapel Hill and a Faculty Researcher at Hugging Face. His work aims to make it easy to get computers to do new things. Consequently, he works mainly on machine learning (enabling computers to learn from examples) and natural language processing (enabling computers to communicate in natural language). He received his Ph.D. from Columbia University in 2016 and spent five years as a research scientist at Google Brain.





**[Livestream Link](https://www.youtube.com/watch?v=0oGxT_i7nk8)**

M 2/13/23

Raphael Townshend (Atomic AI)

[Unlocking the RNA Universe](https://www.youtube.com/watch?v=Z3e9fJ0fGs4)

Abstract
In this talk we will discuss how Atomic AI is developing foundation models integrated in a virtuous cycle with purpose-designed, in-house wet-lab assays, to discover and design RNA drugs. By tightly coupling both algorithmic development and large-scale data generation, we will explore how we can build on AI-augmented structural biology tools such as AlphaFold to transform the design of RNA-targeted and RNA-based medicines. Such applications reveal the ability of large language models to unlock novel therapeutics to treat undruggable diseases in cancer, neurodegeneration, infectious disease, and other areas.




**Bio:** Raphael Townshend is the Founder and Chief Executive Officer at Atomic AI, a biotechnology company using artificial intelligence to enable the next generation of RNA drug discovery. Prior to founding Atomic AI, Raphael studied his PhD at Stanford University, where he wrote his thesis on Geometric Learning of Biomolecular Structure and taught in Stanford’s machine learning and computational biology programs. He has been recognized in Forbes 30 Under 30, and his work has been featured on the cover of Science, recognized by a Best Paper award at NeurIPS, and published in other top venues such as Nature, Cell, and ICLR. During his PhD program, Raphael also held positions at DeepMind and Google on their artificial intelligence and software engineering teams, and founded the inaugural workshop on machine learning and structural biology.





**[Livestream Link](https://www.youtube.com/watch?v=Z3e9fJ0fGs4)**

W 2/15/23

Rob Reich (Stanford)

[Accelerating the Development of Professional Norms in Generative AI](https://www.youtube.com/watch?v=6iyeV23d3Ig)

Abstract
The frontier of technology routinely races ahead of the capacity of politicians and regulators to craft wise policy and governance. When advances on the technological frontier carry broader social consequences, shaping technology toward social benefit and away from social harm falls primarily to technologists and commercial actors. In this respect, professional norms of responsible conduct are especially significant. We live now in such a moment with generative AI. With the recent shift from a “research lab” to “product lab” orientation, the commercial pressures to develop, deploy, and monetize will grow, potentially at the expense of safety and social considerations. In this talk, I examine how to accelerate the development of professional norms in generative AI, ranging from benchmarking, ethical review, open access versus closed access models, and independent organizations for auditing.




**Bio:** Professor of Political Science, director of the Center for Ethics in Society, co-director of the Center on Philanthropy and Civil Society, and associate director of the Institute for Human-Centered AI. He is the author of System Error: Where Big Tech Went Wrong and How We Can Reboot (with Mehran Sahami and Jeremy M. Weinstein) and Just Giving: Why Philanthropy is Failing Democracy and How It Can Do Better (2018); Digital Technology and Democratic Theory (edited with Lucy Bernholz and Hélène Landemore, 2021). His teaching and writing these days focuses on ethics, policy, and technology.





**[Livestream Link](https://www.youtube.com/watch?v=6iyeV23d3Ig)**

W 2/22/23

Nicholas Carlini (Google Brain)

[Poisoning Web-Scale Training Datasets is Practical](https://www.youtube.com/watch?v=h9jf1ikcGyk)

Abstract
In this talk I introduce the first practical poisoning attack on large machine learning datasets. With our attack I could have poisoned (but didn't!) the training dataset for anyone who has used LAION-400M in the last six months. While we take steps to mitigate these attacks, they come at a (sometimes significant) cost to utility. Addressing these challenges will require new categories of defenses to simultaneously allow models to train on large datasets while also being robust to adversarial training data.




**Bio:** Nicholas Carlini is a research scientist at Google Brain. He studies the security and privacy of machine learning, for which he has received best paper awards at ICML, USENIX Security and IEEE S&P. He obtained his PhD from the University of California, Berkeley in 2018.





**[Livestream Link](https://www.youtube.com/watch?v=h9jf1ikcGyk)**

M 2/27/23

Jack Rae (OpenAI)

[Compression for AGI](https://www.youtube.com/watch?v=dO4TPJkeaaU)

Abstract
In this talk we discuss how foundation models are beginning to validate a hypothesis formed over 70 years ago: statistical models which better compress their source data resultantly learn more fundamental and general capabilities from it. We start by covering some fundamentals of compression, and then describe how larger language models, spanning into the hundreds of billions of parameters, are actually state-of-the-art lossless compressors. We discuss some of the emergent capabilities and persistent limitations we may expect along the path to optimal compression.




**Bio:** Jack Rae is a team lead at OpenAI with a research focus on large language models and long-range memory. Previously, he worked at DeepMind for 8 years and led the large language model (LLM) research group. This group developed a 280B parameter LLM ‘Gopher’, which halved the gap towards human-level performance on a suite of exams, alongside ‘RETRO’ — a retrieval-augmented LLM, and ‘Chinchilla Scaling Laws’ — a discovery that contemporary LLMs were considerably under-trained, which won best paper at NeurIPS 2022. Jack has a PhD in Computer Science from UCL, and has published in AI venues such as ACL, ICLR, ICML, NeurIPS, and Nature.





**[Livestream Link](https://www.youtube.com/watch?v=dO4TPJkeaaU)**

W 3/1/23

Susan Zhang (Meta)

[Trials of developing OPT-175B](https://www.youtube.com/watch?v=p9IxoSkvZ-M)

Abstract
LLM development at scale is an extraordinarily resource-intensive process, requiring compute resources that many do not have access to. The experimentation process will also appear rather haphazard in comparison, given limited compute-time to fully ablate all architectural / hyperparameter choices. In this talk, we will walk through the development lifecycle of OPT-175B, covering infrastructure and training convergence challenges faced at scale, along with methods of addressing these issues going forward.




**Bio:** Susan Zhang is a research engineer at Meta focused on the development of large-scale language models. Previously, she worked on designing photonic chips at Luminous Computing, scaling reinforcement learning systems at OpenAI, and building large-scale data infrastructure systems at Unity Technologies.





**[Livestream Link](https://www.youtube.com/watch?v=p9IxoSkvZ-M)**

M 3/6/23

Yejin Choi (UW, Allen Institute)

[Common Sense: the Dark Matter of Language and Intelligence](https://www.youtube.com/watch?v=n4HakBqoCVg)

Abstract
Scale appears to be the winning recipe in today's leaderboards. And yet, extreme-scale neural models are (un)surprisingly brittle and make errors that are often nonsensical and even counterintuitive. In this talk, I will argue for the importance of knowledge, especially commonsense knowledge, as well as inference-time reasoning algorithms, and demonstrate how smaller models developed in academia can still have an edge over larger industry-scale models, if powered with knowledge and/or reasoning algorithms.




**Bio:** Yejin Choi is Brett Helsel professor at the Paul G. Allen School of Computer Science & Engineering at the University of Washington and also a senior research director at AI2 overseeing the project Mosaic. Her research investigates a wide variety of problems across NLP and AI including commonsense knowledge and reasoning, neural language (de-)generation, language grounding with vision and experience, and AI for social good. She is a MacArthur Fellow and a co-recipient of the NAACL Best Paper Award in 2022, the ICML Outstanding Paper Award in 2022, the ACL Test of Time award in 2021, the CVPR Longuet-Higgins Prize (test of time award) in 2021, the NeurIPS Outstanding Paper Award in 2021, the AAAI Outstanding Paper Award in 2020, the Borg Early Career Award (BECA) in 2018, the inaugural Alexa Prize Challenge in 2017, IEEE AI's 10 to Watch in 2016, and the ICCV Marr Prize (best paper award) in 2013. She received her Ph.D. in Computer Science at Cornell University and BS in Computer Science and Engineering at Seoul National University in Korea.





**[Livestream Link](https://www.youtube.com/watch?v=n4HakBqoCVg)**

W 3/8/23

Jared Kaplan (Anthropic)

[AI Safety, RLHF, and Self-Supervision](https://www.youtube.com/watch?v=fqC3D-zNJUM)

Abstract
First I will discuss AI progress and safety, and then I will talk about two techniques used to train large language models to be safer -- reinforcement learning from human feedback, and constitutional AI.




**Bio:** Jared Kaplan is a co-founder of Anthropic and a professor at Johns Hopkins University. He spent the first 15 years of his career as a theoretical physicist before moving to work on AI, where his contributions include research on scaling laws in machine learning, GPT-3, Codex, and more recently AI safety work such as RLHF for helpful and harmless language assistants and Constitutional AI.





**[Livestream Link](https://www.youtube.com/watch?v=fqC3D-zNJUM)**

## Previous Talks

5/19/22

Roman Kazinnik

[Machine Learning in Production: Review of Empirical Solutions](https://www.youtube.com/watch?v=eNWeFccrouI)

Abstract
Taking stock of ML Infra problems with potential to benefit from systematic analysis. ML currently requires running large amounts experiments to compensate for the lack of analysis. Modern AI infrastructure (major clouds) is efficient in creating, training, and deploying thousands of model. At the same time, improving production models performance, accurate estimation of models performance in production, web data relevance, risk mitigation - these are ad hoc and experiment-driven processes. Analytical analysis for Production \[distributed, large-scale, rapidly changing environment\] ML can help to direct and hopefully replace the empirical and manual processes.




**Bio:** Roman Kazinnik is working at Meta on the AI Platform team. He is an experienced computer programmer passionate about empirical and theoretical work. He worked on creating models for deep Earth oil exploration and stock trading throughout his career. He is a recipient of the best paper award of the European Assoc. of Computer Graphics, and he did his Master's at Technion and Ph.D. at Tel Aviv University, Israel.





**[Livestream Link](https://www.youtube.com/watch?v=eNWeFccrouI)**

5/12/22

Alkis Polyzotis

[What can Data-Centric AI Learn from Data and ML Engineering?](https://www.youtube.com/watch?v=cqDgxP8DcJA)

Abstract
Data-centric AI is a new and exciting research topic in the AI community, but many organizations already build and maintain various "data-centric" applications whose goal is to produce high quality data. These range from traditional business data processing applications (e.g., "how much should we charge each of our customers this month?") to production ML systems such as recommendation engines. The fields of data and ML engineering have arisen in recent years to manage these applications, and both include many interesting novel tools and processes. In this talk we present lessons from data and ML engineering that could be interesting to apply in data-centric AI, based on our experience developing data and ML platforms that serve thousands of applications at a range of organizations. In particular, we will discuss lessons related to data monitoring and the challenges to apply it effectively in production ML systems.




**Bio:** Neoklis (Alkis) Polyzotis is a software engineer at Databricks, working on the intersection of data management and ML. Prior to that, he was a research scientist at Google and a professor at UC Santa Cruz. He received his PhD from the U of Wisconsin at Madison.





**[Video Link](https://www.youtube.com/watch?v=cqDgxP8DcJA)**

5/5/22

Xinyu Hu and Olcay Cirit

[DeepETA: How Uber Predicts Arrival Times Using Deep Learning](https://www.youtube.com/watch?v=CJTitzj0qBo)

Abstract
Estimated Time of Arrival (ETA) plays an important role in delivery and ride-hailing platforms. For example, Uber uses ETAs to calculate fares, estimate pickup times, match riders to drivers, plan deliveries, and more. Commonly used route planning algorithms predict an ETA conditioned on the best available route, but such ETA estimates can be unreliable when the actual route taken is not known in advance. In this talk, we describe an ETA post-processing system in which a deep residual ETA network (DeepETA) refines naive ETAs produced by a route planning algorithm. Offline experiments and online tests demonstrate that post-processing by DeepETA significantly improves upon the accuracy of naive ETAs as measured by mean and median absolute error. We further show that post-processing by DeepETA attains lower error than competitive baseline regression models.




**Bio:** Xinyu Hu is a Senior Research Scientist at Uber, focusing on large-scale machine learning applications in spatial-temporal problems and causal inference. She currently works on projects in personalized incentives targeting, including user promotion targeting, spatial-temporal paid movement targeting, etc.. Prior to Uber, Xinyu graduated from Columbia University with a Ph.D. in Biostatistics. Olcay Cirit is a Staff Research Scientist at Uber AI focused on ML systems and large-scale deep learning problems. Prior to Uber AI, he worked on ad targeting at Google.





**[Video Link](https://www.youtube.com/watch?v=CJTitzj0qBo)**

4/28/22

Arjun Akula

[Improving Robustness and Interpretability in Vision and Language Grounding Models](https://www.youtube.com/watch?v=zKKSXQvdCyE)

Abstract
Deep neural networks have enabled significant progress on many multi-modal grounding problems such as visual question answering (VQA), referring expression recognition (REF) which has several important applications such as in navigation, medical imaging, robotics and accessibility. In the last few years we have seen a huge improvement in how these models perform, some of them reaching human-level performance on several datasets. However, we find that these models could be exploiting strong biases in these datasets casting doubts on the actual progress.
For example, as a human, do you focus on the same visual object when you hear the sentences “the bus in the middle of the crowd” and “the crowd that the bus is in the middle of”? Neural networks do so. The exciting progress on understanding language in the context of an image is not due to the cleverness of the neural networks, but rather because of the shortcuts present in the evaluation datasets. In this talk, we show that state-of-the-art neural network approaches are easily fooled due to their failure in overcoming biases in the training datasets. We also show that the recent self-supervised BERT based multi-modal architectures (e.g. ViLBERT) are relatively more robust compared to other neural architectures. We propose methods to improve robustness (and generalization) of the current models. We show that while data augmentation is one way to increase robustness, multi-task learning is probably a less tedious route. Finally, we describe a mechanism for producing scalable and nonstationary benchmarks (and out-of-distribution hard splits) for testing the generalization capabilities of existing grounding models.




**Bio:** Arjun Akula is a Research Scientist at Google AI in Mountain View. He got his PhD from UCLA, jointly advised by Prof. Song-Chun Zhu (UCLA) and Prof. Joyce Chai (UMich). His research interests are in computer vision, natural language processing, and deep learning, with the focuses on multi-modal grounding. Specifically, he works on identifying biases in state-of-the-art datasets and models, improving robustness of vision and language grounding models to out-of-distribution and adversarial inputs. He also works on making the underlying reasoning process of deep learning models more transparent and interpretable to human users. During his PhD, he interned at Amazon Alexa AI (Sunnyvale, CA), Google Research (Los Angeles, CA), Amazon AI (Palo Alto, CA) and Mila (Montreal). Prior to his PhD, he worked as a research software engineer at IBM Research AI (India) for 2.5 years. He did his Bachelors and Masters in Computer Science and Engineering from IIIT Hyderabad, India. He is an active member of the academic community serving as a reviewer/program committee member of ACL, CVPR, ARR, EMNLP, ICCV, AAAI, ECCV, NeurIPS and NAACL. Outside of work, he enjoys hiking, traveling, and playing Table Tennis. Here is a link to his personal website: https://www.arjunakula.com/





**[Video Link](https://www.youtube.com/watch?v=zKKSXQvdCyE)**

4/21/22

Dan Fu

[Improving Transfer and Robustness of Supervised Contrastive Learning](https://www.youtube.com/watch?v=G3yLSBSCUUw)

Abstract
An ideal learned representation should display transferability and robustness. Supervised contrastive learning is a promising method for training accurate models, but produces representations that do not capture these properties due to class collapse -- when all points in a class map to the same representation. In this talk, we discuss how to alleviate these problems to improve the geometry of supervised contrastive learning. We identify two key principles: balancing the right amount of geometric "spread" in the embedding space, and inducing an inductive bias towards subclass clustering. We introduce two mechanisms for achieving these aims in supervised contrastive learning, and show that doing so improves transfer learning and worst-group robustness. Next, we show how we can apply these insights to improve entity retrieval in open-domain NLP tasks (e.g., QA, search). We present a new method, TABi, that trains bi-encoders with a type-aware supervised contrastive loss and improves long-tailed entity retrieval.




**Bio:** Dan Fu is a PhD student in the Computer Science Department at Stanford University, where he is co-advised by Christopher Ré and Kayvon Fatahalian. His research focuses on understanding the principles behind why machine learning methods work and using that understanding to build the next generation of ML systems. He is supported by a Department of Defense NDSEG fellowship. Outside of work, he moonlights as a scuba diver and a competitive ballroom dancer.





**[Video Link](https://www.youtube.com/watch?v=G3yLSBSCUUw)**

4/14/22

Kexin Rong

[Learned Indexing and Sampling for Improving Query Performance in Big-Data Analytics](https://www.youtube.com/watch?v=sHmpMoaodng)

Abstract
Traditional data analytics systems improve query efficiency via fine-grained, row-level indexing and sampling techniques. However, to keep up with the data volumes, increasingly many systems store and process datasets in large partitions containing hundreds of thousands of rows. Therefore, these analytics systems must adapt traditional techniques to work with coarse-grained data partitions as a basic unit to process queries efficiently.
In this talk, I will discuss two related ideas that combine learning techniques with partitioning designs to improve the query efficiency in the analytics systems. First, I will describe PS3, the first approximate query processing system that supports non-uniform, partition-level samples. PS3 reduces the number of partitions accessed by 3 to 70x to achieve the same error compared to a uniform sample of the partitions. Next, I will present OLO, an online learning framework that dynamically adapts data organization according to changes in query workload to minimize overall data access and movement. We show that dynamic reorganization outperforms a single, optimized partitioning scheme by up to 30% in end-to-end runtime.
I will conclude by discussing additional open problems in this area.




**Bio:** Kexin Rong is a postdoctoral researcher at Vmware Research Group. Her research focuses on improving the efficiency and usability of large-scale data analytics. She received her Ph.D. in computer science from Stanford, advised by Peter Bailis and Philp Levis. She is joining Georgia Tech in the fall as an assistant professor in the School of Computer Science.





**[Video Link](https://www.youtube.com/watch?v=sHmpMoaodng)**

4/7/22

Igor Markov

[Looper: an end-to-end ML platform for product decisions](https://www.youtube.com/watch?v=UAZHJK9VWPY)

Abstract
Modern software systems and products increasingly rely on machine learning models to make data-driven decisions based on interactions with users, infrastructure and other systems. For broader adoption, this practice must (i) accommodate product engineers without ML backgrounds, (ii) support fine-grain product-metric evaluation and (iii) optimize for product goals. To address shortcomings of prior platforms, we introduce general principles for and the architecture of an ML platform, Looper, with simple APIs for decision-making and feedback collection.
Looper covers the end-to-end ML lifecycle from collecting training data and model training to deployment and inference, and extends support to personalization, causal evaluation with heterogenous treatment effects, and Bayesian tuning for product goals. During the 2021 production deployment Looper simultaneously hosted 440-1,000 ML models that made 4-6 million real-time decisions per second. We sum up experiences of platform adopters and describe their learning curve.




**Bio:** Igor L. Markov is a Research Scientist at Meta, previously an EECS professor at the University of Michigan. He received his Ph.D. in Computer Science from UCLA, is currently an IEEE Fellow and an ACM Distinguished Scientist. Prof. Markov researches computers that make computers. He has co-authored five books, four US patents, and over 200 refereed publications, some of which were honored by the best-paper awards at the Design Automation and Test in Europe Conference (DATE), the Int'l Symposium on Physical Design (ISPD), the Int'l Conference on Computer-Aided Design (ICCAD) and IEEE Trans. on Computer-Aided Design (TCAD). During the 2011 redesign of the ACM Computing Classification System, Prof. Markov led the effort on the Hardware tree. Prof. Markov is the recipient of a DAC Fellowship, an ACM SIGDA Outstanding New Faculty award, an NSF CAREER award, an IBM Partnership Award, a Microsoft A. Richard Newton Breakthrough Research Award, and the inaugural IEEE CEDA Early Career Award. He has served on the Executive Board of ACM SIGDA and Editorial Boards of several ACM and IEEE Transactions, Communications of the ACM and IEEE Design & Test.





**[Video Link](https://www.youtube.com/watch?v=UAZHJK9VWPY)**

3/31/22

Zhuohan Li

[Alpa: Automated Model-Parallel Deep Learning](https://www.youtube.com/watch?v=y1NXHjcl6V0)

Abstract
Alpa (https://github.com/alpa-projects/alpa) automates model-parallel training of large deep learning models by generating execution plans that unify data, operator, and pipeline parallelism. Alpa distributes the training of large deep learning models by viewing parallelisms as two hierarchical levels: inter-operator and intra-operator parallelisms. Based on it, Alpa constructs a new hierarchical space for massive model-parallel execution plans. Alpa designs a number of compilation passes to automatically derive the optimal parallel execution plan in each independent parallelism level and implements an efficient runtime to orchestrate the two-level parallel execution on distributed compute devices. Alpa generates parallelization plans that match or outperform hand-tuned model-parallel training systems even on models they are designed for. Unlike specialized systems, Alpa also generalizes to models with heterogeneous architectures and models without manually-designed plans.




**Bio:** Zhuohan Li is a PhD student in Computer Science at UC Berkeley, advised by Prof. Ion Stoica. His interest lies in the intersection of machine learning and distributed systems in general. His recent research focuses on distributed model parallel training and inference. He completed his BS at Peking University and has interned at Microsoft Research, Anyscale, and Google Brain.





**[Video Link](https://www.youtube.com/watch?v=y1NXHjcl6V0)**

03/10/22

Shruti Bhosale

[Scaling Multilingual Machine Translation to Thousands of Language Directions](https://www.youtube.com/watch?v=9nAiqqUn_3c)

Abstract
Existing work in translation has demonstrated the potential of massively multilingual machine translation by training a single model able to translate between any pair of languages. However, much of this work is English-Centric by training only on data which was translated from or to English. While this is supported by large sources of training data, it does not reflect translation needs worldwide. In this talk, I will describe how we create a true Many-to-Many multilingual translation model that can translate directly between any pair of 100 languages. We build and open source a training dataset that covers thousands of language directions with supervised data, created through large-scale mining. Then, we explore how to effectively increase model capacity through a combination of dense scaling and language-specific sparse parameters to create high quality models. Our focus on non-English-Centric models brings gains of more than 10 BLEU when directly translating between non-English directions while performing competitively to the best single systems of WMT.




**Bio:** Shruti Bhosale is a Research Engineer at Facebook AI Research in Menlo Park, focusing on Natural Language Processing. She currently works on projects in massively multilingual machine translation and natural language understanding/generation. Her recent work includes many-to-many machine translation for 100 languages, BASE Layers and efficient large-scale language models with Mixture of Experts. She graduated with a Master's Degree in Computer Science from University of Texas at Austin. Prior to Facebook, Shruti built models for people recommendation systems at LinkedIn.





**[Video Link](https://www.youtube.com/watch?v=9nAiqqUn_3c)**

03/03/22

Vijay Janapa Reddi

[Tiny Machine Learning](https://www.youtube.com/watch?v=489HEmRXzOE)

Abstract
Tiny machine learning (TinyML) is a fast-growing field at the intersection of ML algorithms and low-cost embedded systems. TinyML enables on-device analysis of sensor data (vision, audio, IMU, etc.) at ultra-low-power consumption (<1mW). Processing data close to the sensor allows for an expansive new variety of always-on ML use-cases that preserve bandwidth, latency, and energy while improving responsiveness and maintaining privacy. This talk introduces the vision behind TinyML and showcases some of the interesting applications that TinyML is enabling in the field, from wildlife conservation to supporting public health initiatives. Yet, there are still numerous technical hardware and software challenges to address. Tight memory and storage constraints, MCU heterogeneity, software fragmentation and a lack of relevant large-scale datasets pose a substantial barrier to developing TinyML applications. To this end, the talk touches upon some of the research opportunities for unlocking the full potential of TinyML.




**Bio:** Vijay Janapa Reddi is an Associate Professor at Harvard University, VP and a founding member of MLCommons (mlcommons.org), a nonprofit organization aiming to accelerate machine learning (ML) innovation for everyone. He also serves on the MLCommons board of directors and is a Co-Chair of the MLCommons Research organization. He co-led the MLPerf Inference ML benchmark for data center, edge, mobile and IoT systems. Dr. Janapa-Reddi is a recipient of multiple honors and awards, including the National Academy of Engineering (NAE), Gilbreth Lecturer Honor and IEEE TCCA Young Computer Architect Award. He is passionate about widening access to applied machine learning for STEM, Diversity, and using AI for social good. He designed the Tiny Machine Learning (TinyML) series on edX, a massive open online course (MOOC) that sits at the intersection of embedded systems and ML that tens of thousands of global learners access and audit free of cost. He received a Ph.D. in CS from Harvard University, an M.S. from the University of Colorado at Boulder and a B.S from Santa Clara University.





**[Video Link](https://www.youtube.com/watch?v=489HEmRXzOE)**

02/24/22

Fait Poms

[A vision for interactive model development: efficient machine learning by bringing domain experts in the loop](https://www.youtube.com/watch?v=-9LbJBzK2HQ)

Abstract
Building computer vision models today is an exercise in patience--days to weeks for human annotators to label data, hours to days to train and evaluate models, weeks to months of iteration to reach a production model. Without tolerance for this timeline or access to the massive compute and human resources required, building an accurate model can be challenging if not impossible. In this talk, we discuss a vision for interactive model development with iteration cycles of minutes, not weeks. We believe the key to this is integrating the domain expert at key points in the model building cycle and leveraging supervision cues above just example-level annotation. We will discuss our recent progress toward aspects of this goal: judiciously choosing when to use the machine and when to use the domain expert for fast, low label budget model training (CVPR 2021, ICCV 2021), building confidence in model performance with low-shot validation (ICCV 2021 Oral), and some initial tools for rapidly defining correctness criteria.




**Bio:** Fait Poms is a Ph.D. student at Stanford advised by Prof. Kayvon Fatahalian and a Senior Applied Research Scientist at Snorkel.AI. Her research concerns designing algorithms and systems that enable domain experts to rapidly define, train, and validate computer vision models for specialized tasks. She has done research internships at Snorkel AI (with Braden Hancock and Alex Ratner), Facebook Reality Labs (with Yaser Sheikh, Chenglei Wu, and Shoou-I Yu), and NVIDIA Research (with Michael Garland and Michael Bauer), and has transferred her research into production at Snorkel AI and Facebook. Her work has appeared at CVPR, ICCV, and SIGGRAPH. Website: https://faitpoms.com/





**[Video Link](https://www.youtube.com/watch?v=-9LbJBzK2HQ)**

02/17/22

Doris Lee

[Always-on Dataframe Visualizations with Lux](https://www.youtube.com/watch?v=yrmSoU8jHnw)

Abstract
Visualizations help data scientists discover trends, patterns, identify outliers, and derive insights from their data. However, existing visualization libraries in Python require users to write a substantial amount of code for plotting even a single visualization, often hindering the flow of data exploration. In this talk, you will learn about Lux, a lightweight visualization tool on top of pandas dataframes. Lux recommends visualizations for free to users as they explore their data within a Jupyter notebook without the need to write additional code. Lux is used by data scientists across a variety of industries and sectors and has nearly 66k total downloads and over 3.3k stars on GitHub. For more information, see: https://github.com/lux-org/lux




**Bio:** Doris Lee is the co-founder and CEO of Ponder. She graduated with her Ph.D. from the RISE Lab and School of Information at UC Berkeley in 2021. During this time, she developed several data science tools aimed at accelerating insight discovery, including Lux, a lightweight visualization tool on top of pandas dataframes. She is the recipient of the Facebook Ph.D. Fellowship in Systems for Machine Learning in 2020. More at: http://dorisjunglinlee.com/





**[Video Link](https://www.youtube.com/watch?v=yrmSoU8jHnw)**

02/10/22

Ellie Pavlick

[Implementing Symbols and Rules with Neural Networks](https://www.youtube.com/watch?v=ZmKmbImRguE)

Abstract
Many aspects of human language and reasoning are well explained in terms of symbols and rules. However, state-of-the-art computational models are based on large neural networks which lack explicit symbolic representations of the type frequently used in cognitive theories. One response has been the development of neuro-symbolic models which introduce explicit representations of symbols into neural network architectures or loss functions. In terms of Marr's levels of analysis, such approaches achieve symbolic reasoning at the computational level ("what the system does and why") by introducing symbols and rules at the implementation and algorithmic levels. In this talk, I will consider an alternative: can neural networks (without any explicit symbolic components) nonetheless implement symbolic reasoning at the computational level? I will describe several diagnostic tests of "symbolic" and "rule-governed" behavior and use these tests to analyze neural models of visual and language processing. Our results show that on many counts, neural models appear to encode symbol-like concepts (e.g., conceptual representations that are abstract, systematic, and modular), but not perfectly so. Analysis of the failure cases reveals that future work is needed on methodological tools for analyzing neural networks, as well as refinement of models of hybrid neuro-symbolic reasoning in humans, in order to determine whether neural networks' deviations from the symbolic paradigm are a feature or a bug.




**Bio:** Ellie Pavlick is an Assistant Professor of Computer Science at Brown University, where she leads the Language Understanding and Representation (LUNAR) Lab, and a Research Scientist at Google. Her research focuses on building computational models of language that are inspired by and/or informative of language processing in humans. Currently, her lab is investigating the inner-workings of neural networks in order to "reverse engineer" the conceptual structures and reasoning strategies that these models use, as well as exploring the role of grounded (non-linguistic) signals for word and concept learning. Ellie's work is supported by DARPA, IARPA, NSF, and Google.





**[Video Link](https://www.youtube.com/watch?v=ZmKmbImRguE)**

02/03/22

Cody Coleman

[Data selection for Data-Centric AI: Data Quality Over Quantity](https://www.youtube.com/watch?v=8bNwn8EHqOU)

Abstract
Data selection methods, such as active learning and core-set selection, improve the data efficiency of machine learning by identifying the most informative data points to label or train on. Across the data selection literature, there are many ways to identify these training examples. However, classical data selection methods are prohibitively expensive to apply in deep learning because of the larger datasets and models. This talk will describe two techniques to make data selection methods more tractable. First, "selection via proxy" (SVP) avoids expensive training and reduces the computation per example by using smaller proxy models to quantify the informativeness of each example. Second, "similarity search for efficient active learning and search" (SEALS) reduces the number of examples processed by restricting the candidate pool for labeling to the nearest neighbors of the currently labeled set instead of scanning over all of the unlabeled data. Both methods lead to order of magnitude performance improvements, making active learning applications on billions of unlabeled images practical for the first time.




**Bio:** Cody Coleman is the Founder and CEO of Coactive AI. He is also a co-creator of DAWNBench and MLPerf and a founding member of MLCommons. His work spans from performance benchmarking of machine learning systems to computationally efficient methods for active learning and core-set selection. He holds a PhD in Computer Science from Stanford University, where Professors Matei Zaharia and Peter Bailis advised him, and an MEng and BS from MIT.





**[Video Link](https://www.youtube.com/watch?v=8bNwn8EHqOU)**

01/27/22

Bilge Acun

[Designing Sustainable Datacenters with and for AI](https://www.youtube.com/watch?v=LPrFL2gWmTY)

Abstract
Machine learning has witnessed exponential growth over the recent years. In this talk, we will first explore the environmental implications of the super-linear growth trend of AI from a holistic perspective, spanning data, algorithms, and system hardware. System efficiency optimizations can significantly help reducing the carbon footprint of AI systems. However, predictions show that the efficiency improvements will not be enough to reduce the overall resource needs of AI as Jevon's Paradox suggests "efficiency increases consumption". Therefore, we need to design our datacenters with sustainability in mind, using renewable energy every hour of every day. Relying on wind and solar energy 24/7 is challenging due to their intermittent nature. To cope with the fluctuations of renewable energy generation, multiple solutions can be applied such as energy storage and carbon aware scheduling for the workloads. In this talk, I will introduce a framework to analyze the multi-dimensional solution space by taking into account the operational and embodided footprint of the solutions and further how AI can be a part of the solution.




**Bio:** Bilge Acun is a Research Scientist at Meta AI (/FAIR). Her research lies in the intersection of energy efficient and sustainable system design and machine learning. Her work at Meta included making large scale machine learning systems more efficient through algorithmic and system optimizations. She received her Ph.D. degree in 2017 at the Department of Computer Science at University of Illinois at Urbana-Champaign. Her dissertation was awarded 2018 ACM SigHPC Dissertation Award Honorable Mention. Before joining FAIR, she worked at the IBM Thomas J. Watson Research Center as a Research Staff Member.





**[Video Link](https://www.youtube.com/watch?v=LPrFL2gWmTY)**

01/20/22

Fred Sala

[Efficiently Constructing Datasets for Diverse Datatypes](https://www.youtube.com/watch?v=XbnAYeSJ3EU)

Abstract
Building large datasets for data-hungry models is a key challenge in modern machine learning. Weak supervision frameworks have become a popular way to bypass this bottleneck. These approaches synthesize multiple noisy but cheaply-acquired estimates of labels into a set of high-quality pseudolabels for downstream training. In this talk, I introduce a technique that fuses weak supervision with structured prediction, enabling WS techniques to be applied to extremely diverse types of data. This approach allows for labels that can be continuous, manifold-valued (including, for example, points in hyperbolic space), rankings, sequences, graphs, and more. I will discuss theoretical guarantees for this universal weak supervision technique, connecting the consistency of weak supervision estimators to low-distortion embeddings of metric spaces. I will show experimental results in a variety of problems, including learning to rank, geodesic regression, and semantic dependency parsing. Finally I will present and discuss future opportunities for automated dataset construction.




**Bio:** Frederic Sala is an Assistant Professor in the Computer Sciences Department at the University of Wisconsin-Madison and a research scientist at Snorkel AI. His research studies the foundations of data-driven systems, with a focus on machine learning systems. Previously, he was a postdoctoral researcher in the Stanford CS department. He received his Ph.D. in Electrical Engineering from UCLA.





**[Video Link](https://www.youtube.com/watch?v=XbnAYeSJ3EU)**

01/13/22

Deepak Narayanan

[Resource-Efficient Execution of Deep Learning Computations](https://www.youtube.com/watch?v=3RKmXhzpZN8)

Abstract
Deep Learning models have enabled state-of-the-art results across a broad range of applications; however, training these models is extremely time- and resource-intensive, taking weeks on clusters with thousands of expensive accelerators in the extreme case. In this talk, I will describe two ideas that help improve the resource efficiency of model training. In the first half of the talk, I will discuss how pipelining can be used to accelerate distributed training. Pipeline parallelism facilitates model training with lower communication overhead than previous methods while still ensuring high compute resource utilization. Pipeline parallelism also enables the efficient training of large models that do not fit on a single worker; for example, we used pipeline parallelism at Nvidia to efficiently scale training to language models with a trillion parameters on 3000+ GPUs. In the second half of this talk, I will describe how resources in a shared cluster with heterogeneous compute resources (e.g., different types of hardware accelerators) should be partitioned among different users to optimize objectives specified over one or more training jobs. Heterogeneity-aware scheduling can improve various scheduling objectives, such as average completion time, makespan, or cloud computing resource cost, by up to 3.5x.




**Bio:** Deepak is a Senior Researcher in the Systems group at Microsoft Research Redmond. His broad research interests are in distributed systems and systems for Machine Learning. He graduated from Stanford with a Ph.D. in Computer Science in September 2021, where he was advised by Prof. Matei Zaharia.





**[Video Link](https://www.youtube.com/watch?v=3RKmXhzpZN8)**

01/06/22

Beidi Chen

[Pixelated Butterfly: Simple and Efficient Sparse Training for Neural Network Models](https://www.youtube.com/watch?v=aGPzuwoxmCs)

Abstract
Overparameterized neural networks generalize well but are expensive to train. Ideally, one would like to reduce their computational cost while retaining their generalization benefits. Sparse model training is a simple and promising approach to achieve this, but there remain challenges as existing methods struggle with accuracy loss, slow training runtime, or difficulty in sparsifying all model components. The core problem is that searching for a sparsity mask over a discrete set of sparse matrices is difficult and expensive. To address this, our main insight is to optimize over a continuous superset of sparse matrices with a fixed structure known as products of butterfly matrices. As butterfly matrices are not hardware efficient, we propose simple variants of butterfly (block and flat) to take advantage of modern hardware. Our method (Pixelated Butterfly) uses a simple fixed sparsity pattern based on flat block butterfly and low-rank matrices to sparsify most network layers (e.g., attention, MLP). We empirically validate that Pixelated Butterfly is 3x faster than butterfly and speeds up training to achieve favorable accuracy--efficiency tradeoffs. On the ImageNet classification and WikiText-103 language modeling tasks, our sparse models train up to 2.5x faster than the dense MLP-Mixer, Vision Transformer, and GPT-2 medium with no drop in accuracy.




**Bio:** Beidi Chen is a Postdoctoral scholar in the Department of Computer Science at Stanford University, working with Dr. Christopher Ré. Her research focuses on large-scale machine learning and deep learning. Specifically, she designs and optimizes randomized algorithms (algorithm-hardware co-design) to accelerate large machine learning systems for real-world problems. Prior to joining Stanford, she received her Ph.D. in the Department of Computer Science at Rice University, advised by Dr. Anshumali Shrivastava. She received a BS in EECS from UC Berkeley in 2015. She has held internships in Microsoft Research, NVIDIA Research, and Amazon AI. Her work has won Best Paper awards at LISA and IISA. She was selected as a Rising Star in EECS by MIT and UIUC.





**[Video Link](https://www.youtube.com/watch?v=aGPzuwoxmCs)**

12/02/21

Mosharaf Chowdhury

[Systems Support for Federated Computation](https://www.youtube.com/watch?v=TcbOMbg4F9g)

Abstract
Although theoretical federated learning research is growing exponentially, we are far from putting those theories into practice. In this talk, I will share our ventures into building practical systems for two extremities of federated learning. Sol is a cross-silo federated learning and analytics system that tackles network latency and bandwidth challenges faced by distributed computation between far-apart data sites. Oort, in contrast, is a cross-device federated learning system that enables training and testing on representative data distributions despite unpredictable device availability. Both deal with systems and network characteristics in the wild that are hard to account for in analytical models. I'll then share the challenges in systematically evaluating federated learning systems that have led to a disconnect between theoretical conclusions and performance in the wild. I'll conclude this talk by introducing FedScale, which is an extensible framework for evaluation and benchmarking in realistic settings to democratize practical federated learning for researchers and practitioners alike. All these systems are open-source and available at https://github.com/symbioticlab.




**Bio:** Mosharaf Chowdhury is a Morris Wellman assistant professor of CSE at the University of Michigan, Ann Arbor, where he leads the SymbioticLab. His recent research is on application-infrastructure co-design for federated learning, resource disaggregation, and systems for AI and Big Data. In the past, Mosharaf invented coflows and was a co-creator of Apache Spark. Artifacts from his research are widely used in cloud datacenters. He has received many individual honors and awards as well as best-of-conference awards thanks to his amazing students and collaborators. He received his Ph.D. from the AMPLab at UC Berkeley in 2015.





**[Video Link](https://www.youtube.com/watch?v=TcbOMbg4F9g)**

11/18/21

Zain Asgar

[Data science for infrastructure using Pixie](https://www.youtube.com/watch?v=Wi8gR43x-6Q)

Abstract
Pixie is a Kubernetes-native observability platform which helps developers explore, monitor, secure and manage their applications. Pixie is a Cloud Native Computing Foundation Sandbox Project. Pixie utilizes eBPF to automatically collect telemetry data which is stored on edge nodes. This data is usable in Pixie via a Pandas like interface allowing construction of complex data workflows, including machine learning. This talk will provide an overview of Pixie, some of the problems that we solved, and future work we are looking into.




**Bio:** Zain Asgar is a GM/GVP – Pixie & Open Source @ New Relic. Prior to this Zain was to co-founder/CEO of Pixie Labs (acquired by New Relic). Zain is also an Adjunct Professor of Computer Science at Stanford University and was an Entrepreneur in Residence at Benchmark before co-founding Pixie. He has a PhD from Stanford and has helped build at-scale data and AI/ML at Google AI, Trifacta and Nvidia.





**[Video Link](https://www.youtube.com/watch?v=Wi8gR43x-6Q)**

11/11/21

Albert Gu

[Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=EvQ3ncuriCM)

Abstract
A central goal of sequence modeling is designing a single principled model that can address sequence data across a range of modalities and tasks, particularly on long-range dependencies. Although conventional models including RNNs, CNNs, and Transformers have specialized variants for capturing long dependencies, they still struggle to scale to very long sequences of 10000 or more steps. We introduce a simple sequence model based on the fundamental state space representation $x'(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t)$ and show that it combines the strengths of several model families. Furthermore, we show that the HiPPO theory of continuous-time memorization can be incorporated into the state matrix $A$, producing a class of structured models that handles long-range dependencies mathematically and can be computed very efficiently. The Structured State Space (S3) model achieves strong empirical results across a diverse range of established benchmarks, including (i) 91% accuracy on sequential CIFAR-10 with no data augmentation or auxiliary losses, on par with a larger 2-D ResNet, (ii) substantially closing the gap to Transformers on image and language modeling tasks, while performing generation 60X faster, (iii) SotA on every task from the Long Range Arena benchmark, including solving the challenging Path-X task of length 16k that all prior work fails on, while being as efficient as all competitors.




**Bio:** Albert Gu is a PhD student in the Stanford CS department, advised by Chris Ré. His research interests include algorithms for structured linear algebra and theoretical principles of deep sequence models.





**[Video Link](https://www.youtube.com/watch?v=EvQ3ncuriCM)**

11/04/21

Baharan Mirzasoleiman

[Data-efficient and Robust Learning from Massive Datasets](https://www.youtube.com/watch?v=Bmn8SNojTlA)

Abstract
Large datasets have been crucial to the success of modern machine learning models. However, training on massive data has two major limitations. First, it is contingent on exceptionally large and expensive computational resources, and incurs a substantial cost due to the significant energy consumption. Second, in many real-world applications such as medical diagnosis, self-driving cars, and fraud detection, big data contains highly imbalanced classes and noisy labels. In such cases, training on the entire data does not result in a high-quality model.
In this talk, I will argue that we can address the above limitations by developing techniques that can identify and extract the representative subsets for learning from massive datasets. Training on representative subsets not only reduces the substantial costs of learning from big data, but also improves their accuracy and robustness against noisy labels. I will discuss how we can develop theoretically rigorous techniques that provide strong guarantees for the quality of the extracted subsets, as well as the learned models’ quality and robustness against noisy labels. I will also show the effectiveness of such methods in practice for data-efficient and robust learning.




**Bio:** Baharan Mirzasoleiman is an Assistant Professor in the Computer Science Department at UCLA. Her research focuses on developing new methods that enable efficient machine learning from massive datasets. Her methods have immediate application to high-impact problems where massive data volumes prohibit efficient learning and inference, such as huge image collections, recommender systems, Web and social services, video and other large data streams. Before joining UCLA, she was a postdoctoral research fellow in Computer Science at Stanford University. She received her Ph.D. in Computer Science from ETH Zurich. She received an ETH medal for Outstanding Doctoral Thesis, and was selected as a Rising Star in EECS by MIT.





**[Video Link](https://www.youtube.com/watch?v=Bmn8SNojTlA)**

10/28/21

Gideon Mendels

[MLOps System Design for Development and Production](https://www.youtube.com/watch?v=7XCsi64HLQ8)

Abstract
While ML model development is a challenging process, the management of these models becomes even more complex once they're in production. Shifting data distributions, upstream pipeline failures, and model predictions impacting the very dataset they’re trained on can create thorny feedback loops between development and production. In this talk, we’ll examine some naive ML workflows that don’t take the development-production feedback loop into account and explore why they break down. Next, we'll showcase some system design principles that will help manage these feedback loops more effectively. Finally, we’ll examine several industry case studies where teams have applied these principles to their production ML systems.






**[Video Link](https://www.youtube.com/watch?v=7XCsi64HLQ8)**

10/21/21

Zhihao Jia

[Automatically Discovering Machine Learning Optimizations](https://www.youtube.com/watch?v=XyXzzjbuXCs)

Abstract
As an increasingly important workload, machine learning (ML) applications require different performance optimization techniques from traditional runtimes and compilers. In particular, to accelerate ML applications, it is generally necessary to perform ML computations on distributed heterogeneous hardware platforms and parallelize computations using multiple data dimensions, neither of which is even expressible in traditional compilers and runtimes. In this talk, I will present our recent work on automated discovery of performance optimizations for ML by leveraging the mathematical and statistical properties of ML computations. Compared to existing ML systems, our approaches enable faster ML training/inference and stronger correctness guarantees while requiring significantly less human effort.




**Bio:** Zhihao Jia is an assistant professor of computer science at Carnegie Mellon University. He obtained his Ph.D. from the computer science department at Stanford working with Alex Aiken and Matei Zaharia. His research interests lie in the intersection of computer systems and machine learning, with a focus on building efficient, scalable, and automated systems for ML computations.





**[Video Link](https://www.youtube.com/watch?v=XyXzzjbuXCs)**

10/14/21

Baishakhi Ray

[Improving Software Reliability using Machine Learning](https://www.youtube.com/watch?v=GTbMN8ULx18)

Abstract
Software bugs cost millions of dollars to the US economy. Improving software reliability has been one of the primary concerns of Software Engineering, Security, Programming Language, and Verification research over decades. Researchers developed numerous automatic bug-finding tools, either based on static code analysis or analyzing dynamic code behavior. However, the adoption of these methods in the real-world is still limited, partly because most of them require a significant amount of manual work from developers and have a steep learning curve. In this talk, I will discuss how machine learning-based approaches can help us to automate and scale up the bug-finding (especially with respect to fuzz-testing) and bug-fixing process for large real-world programs.




**Bio:** Baishakhi Ray is an Associate Professor in the Department of Computer Science, Columbia University, NY, USA. She has received her Ph.D. degree in Electrical & Computer Engineering from the University of Texas, Austin. Baishakhi's research interest is in the intersection of Software Engineering and Machine Learning. Baishakhi has received the NSF CAREER award, IBM Faculty Award, and VMware Early Career Faculty Award, and many best Paper awards including FASE 2020, FSE 2017, MSR 2017, IEEE Symposium on Security and Privacy (Oakland), 2014. Her research has also been published in CACM Research Highlights and has been widely covered in trade media.





**[Video Link](https://www.youtube.com/watch?v=GTbMN8ULx18)**

10/07/21

Mi Zhang

[Empowering the Next Billion Devices with Deep Learning](https://www.youtube.com/watch?v=xy4sbZ4ev2k)

Abstract
The proliferation of edge devices and the gigantic amount of data they generate make it no longer feasible to transmit all the data to the cloud for processing. Such constraints fuel the need to move the intelligence from the cloud to the edge where data reside. In this talk, we will present our works on how we bring the power of deep learning to edge devices to realize the vision of Artificial Intelligence of Things.
First, we will present our work on designing adaptive frameworks that empower AI-embedded edge devices to adapt to the inherently dynamic runtime resources to enable elastic on-device AI. Second, we shift from the single edge device setting to the distributed setting for the task of distributed on-device inference. We will focus on one killer application of edge computing, and present a distributed workload-adaptive framework for low-latency high-throughput large-scale live video analytics. Third, we will present our work on designing a distributed on-device training framework that significantly enhances the on-device training efficiency without compromising the training quality. The results and insights obtained in those works are also useful in designing many other modern machine learning systems.




**Bio:** Mi Zhang is an Associate Professor and the Director of the Machine Learning Systems Lab at Michigan State University. He received his Ph.D. from University of Southern California and B.S. from Peking University. Before joining MSU, he was a postdoctoral scholar at Cornell University. His research lies at the intersection of systems and machine learning, spanning areas including On-Device AI, Automated Machine Learning (AutoML), Federated Learning, Systems for Machine Learning, and Machine Learning for Systems. He is the 4th Place Winner of the 2019 Google MicroNet Challenge, the Third Place Winner of the 2017 NSF Hearables Challenge, and the champion of the 2016 NIH Pill Image Recognition Challenge. He is the recipient of six best paper awards and nominations. He is also the recipient of the Facebook Faculty Research Award, Amazon Machine Learning Research Award, and MSU Innovation of the Year Award.





**[Video Link](https://www.youtube.com/watch?v=xy4sbZ4ev2k)**

9/30/21

Dennis Shasha and Mustafa Anil Kocak

[SafePredict and Friends](https://www.youtube.com/watch?v=W2q-8MiW8no)

Abstract
SafePredict is a meta-algorithm for machine learning applications that strategically refuses to accept the predictions of an underlying machine learning algorithm or algorithms. The goal is to achieve a user-specified correctness rate on the non-refused predictions without refusing too much. We show applications to an on-line learning setting in which the data-to-class mapping is not independent and identically distributed (not iid).
In related work, we look at classification problems where we are willing to guess, on average, k classes in the hopes that one is correct. We compare such an approach in which we always choose the top k most likely classes.
Finally, we consider the problem of selective sampling in settings where evaluating each sample is expensive. We build on and improve the Horvitz-Thompson and Augmented Inverse Probability Weighted sampling methods.




**Bio:** Dennis Shasha is a Julius Silver Professor of computer science at the Courant Institute of New York University and an Associate Director of NYU Wireless. He works on meta-algorithms for machine learning to achieve guaranteed correctness rates, with biologists on pattern discovery for network inference; on automated verification for concurrent algorithms; on a tool for policy planners facing epidemics; on tree and graph matching; on algorithms for time series for finance and migratory patterns; on database tuning; and on computational reproducibility. Because he likes to type, he has written six books of puzzles about a mathematical detective named Dr. Ecco, a biography about great computer scientists, and a book about the future of computing. He has also written eight technical books about database tuning, biological pattern recognition, time series, DNA computing, resampling statistics, causal inference in molecular networks, and the automated verification of concurrent search structures. He has co-authored more than 85 journal papers, 80 conference papers, and 25 patents. Because he loves puzzles, he has written the puzzle column for various publications including Scientific American, Dr. Dobb's Journal, and currently the Communications of the ACM. He is a fellow of the ACM and an INRIA International Chair.





**[Video Link](https://www.youtube.com/watch?v=W2q-8MiW8no)**

9/23/21

Laurel Orr

[Towards Transparent Foundations -- Building Accessible Infrastructure for Training Large-Scale Language Models](https://www.youtube.com/watch?v=g-OjU4uzWqE)

Abstract
“Foundation models” — large-scale self-supervised models that can be adapted to a wide range of downstream tasks - are changing how machine learning systems are constructed and deployed. Due to their extreme resource demands, training and developing a science behind these models has remained difficult. In this talk, I'll introduce and describe the journey behind Mistral, an infrastructure for accessible, easy-to-use foundation model training. I'll describe some of the hurdles we encountered with stable, reproducible training and how we see Mistral as a crucial step to facilitate open foundation model research.




**Bio:** Laurel Orr is currently a PostDoc at Stanford working with Chris Ré in the Hazy Research Lab. In August of 2019, she graduated with a PhD from Paul G Allen School for Computer Science and Engineering at the University of Washington in Seattle. She was part of the Database Group and advised by Dan Suciu and Magdalena Balazinska.
Her research interests are broadly at the intersection of machine learning and data management. She focuses on how to manage the end-to-end lifecycle of self-supervised embedding pipelines. This includes problems of how to better train, maintain, monitor, and patch the embedding models and their use downstream.





**[Video Link](https://www.youtube.com/watch?v=g-OjU4uzWqE)**

8/12/21

Pooyan Jamshidi

[Causal AI for Systems](https://www.youtube.com/watch?v=csB_cF6MA9A)

Abstract
In this talk, I will present the recent progress in employing Causal AI (causal structure learning, causal inference, counterfactual reasoning, causal representation learning, and causal transfer learning) in addressing several significant and outstanding challenges in computer systems. Next, I will present our Causal AI approach for robust performance engineering (performance debugging, performance optimization, and performance predictions) in highly configurable composed systems. In particular, I will present our latest results for identifying and repairing performance faults in on-device ML systems and big data analytics pipelines. Finally, I will conclude by discussing future directions and opportunities of Causal AI in testing autonomous robots and dynamic reconfiguration of serverless systems and microservices.




**Bio:** Pooyan Jamshidi is an assistant professor in the computer science and engineering department at the University of South Carolina and a visiting researcher at Google AdsAI. His primary research interest is at the intersections of machine learning and systems.





**[Video Link](https://www.youtube.com/watch?v=csB_cF6MA9A)**

8/5/21

Chaoyang He

[Distributed ML System for Large-scale Models: Dynamic Distributed Training and Scalable Federated Learning](https://www.youtube.com/watch?v=AY7pCYTC8pQ)

Abstract
In modern AI, large-scale deep learning models have emerged as the core technology behind many important Internet businesses, such as Search/ADs/Recommendation System/CV/NLP. BERT, Vision Transformer, GPT-3, and Switch Transformer models scale up the model size to a billion or even trillion number of parameters, showing non-trivial accuracy improvement for nearly all learning tasks. Distributed training using cloud clusters is key to the successful training of such large-scale models in a timely manner. Developing more advanced distributed training systems and algorithms can either reduce the energy cost or enable us to train even larger models. Furthermore, it is also essential to develop disruptive learning paradigms like federated learning, which can not only protect the privacy of users but also distribute the burden of handling unprecedented big data and models.
This talk will mainly focus on distributed ML systems for large-scale models: dynamic distributed training for the cloud cluster (https://DistML.ai) and scale federated learning for the edge devices (https://FedML.ai). In the first part, I will introduce PipeTransformer, an automated elastic pipelining for distributed training of Transformer models (BERT and ViT). In PipeTransformer, we design an adaptive on the fly freeze algorithm that can identify and freeze some layers gradually during training, and an elastic pipelining system that can dynamically reduce GPU resources to train the remaining active layers, and also forks more pipelines on released GPU resources to enlarge the width of data parallelism. In the second part, I will talk about scalable federated learning towards training large-scale models on resource-constrained edge devices and FedML Ecosystem, which aims at ubiquitously distributed training at the edge for diverse AI applications such as CV NLP, GraphNN, and IoT.




**Bio:** Chaoyang He is a Ph.D. Candidate in the CS department at the University of Southern California, Los Angeles, USA. He is advised by Salman Avestimehr (USC), Professor Mahdi Soltanolkotabi (USC), Professor Murali Annavaram (USC), and Professor Tong Zhang (HKUST). He also works closely with researchers/engineers at Google, Facebook, Amazon, and Tencent. Previously, He was an R&D Team Manager and Staff Software Engineer at Tencent (2014-2018), a Team Leader and Senior Software Engineer at Baidu (2012-2014), and a Software Engineer at Huawei (2011-2012). His research focuses on distributed/federated machine learning algorithms, systems, and applications. Chaoyang He has received a number of awards in academia and industry, including Amazon ML Fellowship (2021-2022), Qualcomm Innovation Fellowship (2021-2022), Tencent Outstanding Staff Award (2015-2016), WeChat Special Award for Innovation (2016), Baidu LBS Group Star Awards (2013), and Huawei Golden Network Award (2012). During his Ph.D. study, he has published papers at ICML, NeurIPS, CVPR, ICLR, MLSys, among others. Besides pure research, he also has R&D experience for Internet products and businesses such as Tencent Cloud, Tencent WeChat Automotive / AI in Car, Tencent Games, Tencent Maps, Baidu Maps, and Huawei Smartphone. He obtained three years of experience in R&D team management at Tencent between 2016-2018. With his advisors, he also co-founds FedML.ai, built based on a paper that won Best Paper Award at NeurIPS 2020 FL workshop. More details are available at his homepage: https://ChaoyangHe.com.





**[Video Link](https://www.youtube.com/watch?v=AY7pCYTC8pQ)**

7/29/21

Suman Jana

[Scalable, Accurate, Robust Binary Analysis with Transfer Learning](https://www.youtube.com/watch?v=HbVVOb7xTdU)

Abstract
Binary program analysis is a fundamental building block for a broad spectrum of security tasks. Essentially, binary analysis encapsulates a diverse set of tasks that aim to understand and analyze behaviors/semantics of binary programs. Existing approaches often tackle each analysis task independently and heavily employ ad-hoc task-specific brittle heuristics. While recent ML-based approaches have shown some early promise, they too tend to learn spurious features and overfit to specific tasks without understanding the underlying program semantics.
In this talk, I will describe two of our recent projects that use transfer learning to learn binary program semantics and transfer the learned knowledge for different binary analysis tasks. Our key observation is that by designing a pretraining task that can learn binary code semantics, we can drastically boost the performance of binary analysis tasks. Our pretraining task is fully self-supervised -- it does not need expensive labeling effort and therefore can easily generalize across different architectures, operating systems, compilers, optimizations, and obfuscations. Extensive experiments show that our approach drastically improves the performance of popular tasks like binary disassembly and matching semantically similar binary functions.




**Bio:** Suman Jana is an associate professor in the department of computer science and the data science institute at Columbia University. His primary research interest is at the intersections of computer security and machine learning. His research has received six best paper awards, a CACM research highlight, a Google faculty fellowship, a JPMorgan Chase Faculty Research Award, an NSF CAREER award, and an ARO young investigator award.





**[Video Link](https://www.youtube.com/watch?v=HbVVOb7xTdU)**

7/22/21

Jacopo Tagliabue

[You don't need a bigger boat: MLOps at reasonable scale](https://www.youtube.com/watch?v=Ndxpo4PeEms)

Abstract
It is indeed a wonderful time to build machine learning systems, as we don’t have much to do anymore! Thanks to a growing ecosystem of tools and shared best practices, even small teams can be incredibly productive at “reasonable scale”. In this talk, we present our philosophy for modern, no-nonsense data pipelines, highlighting the advantages of a PaaS approach, and showing (with open source code) how the entire toolchain works on real-world data with realistic constraints. We conclude discussing our proposal for self-documenting ML DAGs - 'DAG cards' for Metaflow - and sharing unsolicited advice on the future of MLOps for “reasonable” companies.




**Bio:** Educated in several acronyms across the globe (UNISR, SFI, MIT), Jacopo Tagliabue was co-founder and CTO of Tooso, an A.I. company in San Francisco acquired by Coveo in 2019. Jacopo is currently the Lead A.I. Scientist at Coveo, shipping models to hundreds of customers and millions of users. When not busy building products, he is exploring topics at the intersection of language, reasoning and learning: his research and industry work is often featured in the general press and premier A.I. venues. In previous lives, he managed to get a Ph.D., do sciency things for a pro basketball team, and simulate a pre-Columbian civilization.





**[Video Link](https://www.youtube.com/watch?v=Ndxpo4PeEms)**

7/15/21

Chris Kedzie

[Building a Machine Learning Framework for Chatbots](https://www.youtube.com/watch?v=rrzqa1C1aeU)

Abstract
At Rasa, our goal is to make it easy for anyone to build a conversational assistant -- or chatbot. To that end, we develop Rasa Open Source, an open source machine learning framework for building chatbots, along with Rasa X, a closed source but free tool for monitoring and iteratively improving chatbots once they are in production. In addition to these technical offerings, we also strive to promote good data science through our philosophy of conversation-driven development.




**Bio:** Chris Kedzie is a machine learning researcher at Rasa. He has published research at the intersection of natural language processing, natural language generation, and machine learning. His most recent work has focused on making neural network models of language generation faithful with respect to content plans or semantic representations. He holds a PhD in computer science from Columbia University and has received a best paper award from the International Conference on Natural Language Generation (INLG 2019).





**[Video Link](https://www.youtube.com/watch?v=rrzqa1C1aeU)**

7/8/21

Sasha Rush

[Beyond Softmax: Scaling Probabilistic Structure in NLP](https://www.youtube.com/watch?v=8nx4KfK3Y3s)

Abstract
Progress on large autoregressive models for NLP applications has been transformative, but has left many practical questions about how to utilize these approaches in a controllable and efficient manner. This talk explores this challenge of using probabilistic models to impose explicit modeling structure. I show that discrete structured models can now be implemented efficiently on modern hardware with optimizing compilers. These approaches generalize the standard softmax function we all know and love, and in fact are not much harder to use in practice. To show the benefit of this approach, I will describe a factorization of the Transformer into a structured model that lets us learn a fast and accurate parallel translation decoder. The system shows how to take advantage of efficient inference based on basic distributional properties, while maintaining the modeling benefits of a deep model.




**Bio:** Alexander 'Sasha' Rush is an Associate Professor at Cornell Tech in NYC. His group's research is in the intersection of natural language processing, deep learning, and structured prediction with applications in text generation and efficient inference. He contributes to several open-source projects in NLP and works part time on HuggingFace Transformers. He was recently General Chair of ICLR and developed the MiniConf tool used to run ML/NLP virtual conferences. His work has received paper and demo awards at major NLP, visualization, and hardware conferences, an NSF Career Award, and a Sloan Fellowship.





**[Video Link](https://www.youtube.com/watch?v=8nx4KfK3Y3s)**

7/1/21

Willem Pienaar

[Feature stores as the bridge between models and data](https://www.youtube.com/watch?v=6OCUMbEtSLU)

Abstract
Feature stores have emerged as a pivotal component in the modern machine learning stack. They solve some of the toughest challenges in data for machine learning, namely feature computation, storage, validation, serving, and reuse. Ultimately, feature stores act as the bridge between models in production and an organization’s data.
In this talk I will describe the key problems that feature stores solve, I will describe some key use cases and deployment patterns for feature stores that we see in the wild, and finally I will comment on how feature stores are evolving with the rise of modern data platforms.




**Bio:** Willem is a tech lead at Tecton where he currently leads open source development for Feast, the open source feature store. Willem previously started and led the data science platform team at Gojek, the Southeast Asian ride-hailing decacorn, where he built their machine learning platform. His main focus areas are building data and ML tooling, allowing organizations to scale machine learning and developer productivity. In a previous life, Willem also founded and sold a networking startup.





**[Video Link](https://www.youtube.com/watch?v=6OCUMbEtSLU)**

6/24/21

Pete Warden

[Machine Learning Everywhere](https://www.youtube.com/watch?v=FXbhJG470ng)

Abstract
When I first joined Google in 2014, I was amazed to discover they were using 13 kilobyte neural network models to recognize "OK Google" on tiny embedded chips on Android phones. This felt like deep magic, and it made me wonder how many other problems these kinds of miniscule ML models could solve. Over the past few years I've been helping Google ship products using this approach with TensorFlow Lite Micro, and helped external developers create new applications. While it's still early days for "TinyML", we're already seeing interesting impacts on how engineers compose systems, including software-defined sensors, cascades of ML models, air-gapped ambient computing, and ubiquitous on-device voice interfaces. In this talk I'll cover the past, present, and future of embedded ML systems.






**[Video Link](https://www.youtube.com/watch?v=FXbhJG470ng)**

6/17/21

Yaron Singer

[Securing AI systems from operational risk](https://www.youtube.com/watch?v=Qp6i-BehgGI)

Abstract
As organizations adopt AI technologies they inherit operational risk. This risk often manifests itself in AI models that produce erroneous predictions that go undetected. In this talk we will discuss root causes for AI models going haywire, and present a rigorous framework for eliminating risk from AI. We will show how this methodology can be used as building blocks for continuous monitoring and firewall systems for AI.




**Bio:** Yaron Singer is the CEO and co-founder of Robust Intelligence, and the Gordon McKay Professor of Computer Science and Applied Mathematics at Harvard University. Before Harvard he was a researcher at Google and obtained his PhD from UC Berkeley. He is the recipient of the NSF CAREER award, the Sloan fellowship, Facebook faculty award, Google faculty award, 2012 Best Student Paper Award at the ACM conference on Web Search and Data Mining, the 2010 Facebook Graduate Fellowship, the 2009 Microsoft Research PhD Fellowship.





**[Video Link](https://www.youtube.com/watch?v=Qp6i-BehgGI)**

6/10/21

Karan Goel

[Building Malleable ML Systems through Measurement, Monitoring & Maintenance](https://www.youtube.com/watch?v=mNkqAZ54wGo)

Abstract
Machine learning systems are now easier to build than ever, but they still don’t perform as well as we would hope on real applications. I’ll explore a simple idea in this talk: if ML systems were more malleable and could be maintained like software, we might build better systems. I’ll discuss an immediate bottleneck towards building more malleable ML systems: the evaluation pipeline. I’ll describe the need for finer-grained performance measurement and monitoring, the opportunities paying attention to this area could open up in maintaining ML systems, and some of the tools that I’m building (with great collaborators) in the Robustness Gym project to close this gap.




**Bio:** Karan Goel is a 3rd year CS PhD student at Stanford advised by Chris Ré. His main goal is to accelerate the pace at which machine learning can be robustly and safely used in practice across applications, and in industry at large. He leads the Robustness Gym project, where he builds tools to measure, monitor and repair machine learning systems interactively. He is a recipient of the Siebel Foundation Scholarship.





**[Video Link](https://www.youtube.com/watch?v=mNkqAZ54wGo)**

6/3/21

Richard Liaw

[Assorted boring problems in distributed machine learning](https://www.youtube.com/watch?v=R7N3quJcGNQ)

Abstract
Much of the academic focus on “distributing/scaling up machine learning” is synonymous with “training larger supervised ML models like GPT-3 with more and more compute resources”. However, training is only a small part of the ML lifecycle. In this talk, I’ll focus on a couple other machine learning problems that demand a large amount of compute resources, which may be a bit more “boring” but equally (or arguably more!) important. I’ll cover a couple problems that my collaborators and I have previously worked on at UC Berkeley and now at Anyscale: abstractions for scalable reinforcement learning and building RLlib (ICML 18, ICLR 20), distributed hyperparameter tuning and dynamic resource allocation for hyperparameter tuning (SOCC 19, Eurosys 21), and ray as a substrate for the next generation of ML platforms.




**Bio:** Richard Liaw is an engineer at Anyscale, where he leads a team in building open source machine learning libraries on top of Ray. He is on leave from the PhD program at UC Berkeley, where he worked at the RISELab advised by Ion Stoica, Joseph Gonzalez, and Ken Goldberg. In his time in the PhD program, he was part of the Ray team, building scalable ML libraries on top of Ray.





**[Video Link](https://www.youtube.com/watch?v=R7N3quJcGNQ)**

5/27/21

Even Oldridge

[Deep Learning Based Recommender Systems in Production](https://www.youtube.com/watch?v=wPso35VkuCs)

Abstract
Recommender Systems are one of the most complex ML applications to deploy into production. The data is sparse, massive, and constantly increasing, and the models deployed create a feedback loop that requires careful monitoring. What's more, the hardware and software that led to the revolution of deep learning was built during the era of computer vision. Differences in architecture and data between vision and recommenders initially made the HW/SW stack a poor fit for deep learning based recommender systems. In this talk we'll explore what makes recommenders different from a data, architecture, and system perspective, and talk about changes in GPU hardware within the last generation that make it much better suited to the recommendation problem. By focusing on these differences we've also identified improvements on the software side that take advantage of optimizations only possible in the recommendation domain. A new era of faster ETL, Training and Inference is coming to the RecSys space and this talk will walk through some of the patterns of optimization that guide the tools we're building to make recommenders both faster to use and easier to deploy on GPUs.




**Bio:** Even Oldridge is a Sr. Manager at NVIDIA leading the effort to develop the open source libraries of Merlin which provide fast, easy to use and deploy, scalable recommender systems on the GPU. He has a PhD in Computer Vision and a Masters in Programmable Hardware from the University of British Columbia. He’s worked in the recommendation space for the past decade and has developed systems for recommending dates and houses, among other things. He’s an industry co-chair for ACM RecSys Conference 2021, and he’ll talk your ear off about embeddings and deep learning based recommenders if you let him.





**[Video Link](https://www.youtube.com/watch?v=wPso35VkuCs)**

5/20/21

Tim Kraska

[Towards Instance-Optimized Data Systems](https://www.youtube.com/watch?v=oOXen4elWns)

Abstract
Recently, there has been a lot of excitement around ML-enhanced (or learned) algorithm and data structures. For example, there has been work on applying machine learning to improve query optimization, indexing, storage layouts, scheduling, log-structured merge trees, sorting, compression, sketches, among many other things. Arguably, the motivation behind these techniques are similar: machine learning is used to model the data and/or workload in order to derive a more efficient algorithm or data structure. Ultimately, what these techniques will allow us to build are “instance-optimized” systems; systems that self-adjust to a given workload and data distribution to provide unprecedented performance and avoid the need for tuning by an administrator. In this talk, I will provide an overview of the opportunities and limitations of learned index structures, storage layouts, and query optimization techniques we have been developing in my group, and how we are integrating these techniques to build a first instance-optimized database system.




**Bio:** Tim Kraska is an Associate Professor of Electrical Engineering and Computer Science in MIT's Computer Science and Artificial Intelligence Laboratory, co-director of the Data System and AI Lab at MIT (DSAIL@CSAIL), and co-founder of Einblick Analytics. Currently, his research focuses on building systems for machine learning, and using machine learning for systems. Before joining MIT, Tim was an Assistant Professor at Brown, spent time at Google Brain, and was a PostDoc in the AMPLab at UC Berkeley after he got his PhD from ETH Zurich. Tim is a 2017 Alfred P. Sloan Research Fellow in computer science and received several awards including the VLDB Early Career Research Contribution Award, the VMware Systems Research Award, the university-wide Early Career Research Achievement Award at Brown University, an NSF CAREER Award, as well as several best paper and demo awards at VLDB and ICDE.





**[Video Link](https://www.youtube.com/watch?v=oOXen4elWns)**

5/13/21

Guanhua Wang

[Disruptive Research on Distributed ML Systems](https://www.youtube.com/watch?v=gDKRrrfPgng)

Abstract
Deep Neural Networks (DNNs) enable computers to excel across many different applications such as image classification, speech recognition and robotics control. To accelerate DNN training and serving, parallel computing is widely adopted. System efficiency is a big issue when scaling out. In this talk, I will make three arguments towards better system efficiency in distributed DNN training and serving.
First, Ring All-Reduce for model synchronization is not optimal, but Blink is. By packing spanning trees rather than forming rings, Blink achieves higher flexibility in arbitrary networking environments and provides near-optimal network throughput. Blink is filed as a US patent and is being used by Microsoft. Blink gains lots of attention from industry, such as Facebook (distributed PyTorch team), ByteDance (parent company of TikTok app). Blink was also featured on Nvidia GTC China 2019 and news from Baidu, Tencent.
Second, communication can be eliminated via sensAI's class parallelism. sensAI decouples a multi-task model into disconnected subnets, each is responsible for decision making of a single task. sensAI's attribute of low-latency, real-time model serving attracts several Venture Capitals in the Bay Area.
Third, Wavelet is more efficient than gang-scheduling. By intentionally adding task launching latency, Wavelet interleaves peak memory usage across different waves of training tasks on the accelerators, and thus it improves both computation and on-device memory utilization. Multiple companies, including Facebook and Apple, show interests to Wavelet project.




**Bio:** Guanhua Wang is a final year CS PhD in the RISELab at UC Berkeley, advised by Prof. Ion Stoica. His research lies primarily in the ML+Systems area including fast collective communication schemes for model synchronization, efficient in-parallel model training and real-time model serving.





**[Video Link](https://www.youtube.com/watch?v=gDKRrrfPgng)**

5/6/21

Carole-Jean Wu

[Designing AI systems for deep learning recommendation and beyond](https://www.youtube.com/watch?v=5xcd0V9m6Xs)

Abstract
The past decade has witnessed a 300,000 times increase in the amount of compute for AI. The latest natural language processing model is fueled with over trillion parameters while the memory need of neural recommendation and ranking models has grown from hundreds of gigabyte to the terabyte scale. This talk introduces the underinvested deep learning personalization and recommendation systems in the overall research community. The training of state-of-the-art industry-scale personalization and recommendation models consumes the highest number of compute cycles among all deep learning use cases at Facebook. For AI inference, recommendation use cases consume even higher compute cycles of 80%. What are the key system challenges faced by industry-scale neural personalization and recommendation models? This talk will highlight recent advances on AI system development for deep learning recommendation and the implications on infrastructure optimization opportunities across the machine learning system stack. System research for deep learning recommendation and AI at large is at a nascent stage. This talk will conclude with research directions for building and designing responsible AI systems – that is fair, efficient, and environmentally sustainable.




**Bio:** Carole-Jean Wu is a Technical Lead and Manager at Facebook AI Research – SysML. Her work is in the domain of computer system architecture with particular emphasis on energy- and memory-efficient systems. Her research has pivoted into designing systems for machine learning execution at-scale, such as for personalized recommender systems and mobile deployment. In general, she is interested in tackling system challenges to enable efficient, responsible AI execution. Carole-Jean chairs the MLPerf Recommendation Benchmark Advisory Board, co-chaired MLPerf Inference, and serves on the MLCommons Board as a director. Carole-Jean received her M.A. and Ph.D. from Princeton and B.Sc. from Cornell. She is the recipient of the NSF CAREER Award, Facebook AI Infrastructure Mentorship Award, the IEEE Young Engineer of the Year Award, the Science Foundation Arizona Bisgrove Early Career Scholarship, and the Intel PhD Fellowship, among a number of Best Paper awards.





**[Video Link](https://www.youtube.com/watch?v=5xcd0V9m6Xs)**

4/29/21

Erin LeDell

[Scalable Machine Learning with H2O & Systems Approach to Algorithm Development](https://www.youtube.com/watch?v=UELpqMxDB1E)

Abstract
The focus of this presentation is the scalable and distributed machine learning platform, H2O. The multi-node distributed algorithms (GLM, Random Forest, GBM, DNNs, etc) can train on datasets which are larger than RAM (of a single machine), and H2O integrates with other 'big data' systems, Hadoop and Spark. H2O is engineered for production use cases with a focus on fast training and prediction speeds. The second part of the talk will discuss a systems approach to developing novel machine learning algorithms such as H2O AutoML. Unlike well-defined ML algorithms (e.g. GBM), an 'AutoML' algorithm is an automated process which aims to train the best model (or ensemble) in a specified amount of time. I will discuss our methodology for experimentation and validation of new strategies or changes to the algorithm, using a benchmark-driven systems approach.




**Bio:** Erin LeDell is the Chief Machine Learning Scientist at H2O.ai. Her research focuses on automatic machine learning, ensemble machine learning and statistical computing. Before joining H2O.ai, she was the Principal Data Scientist at Wise.io and Marvin Mobile Security, the founder of DataScientific, Inc. She received her Ph.D. in Biostatistics with a Designated Emphasis in Computational Science and Engineering from University of California, Berkeley.





**[Video Link](https://www.youtube.com/watch?v=UELpqMxDB1E)**

4/22/21

Jason Knight

[Reshaping the ML software bedrock with compilers](https://www.youtube.com/watch?v=KN4r_oVpfI0)

Abstract
The rate of change for ML software, hardware, and algorithms improves our lives daily, but how sturdy are the foundations we rely on? From my experience at one of the first ML accelerator startups (Nervana), applying ML to biology and medicine, leading the ML SW product team at Intel, and then co-founding OctoML I'll describe: 1) The pains of developing ML SW stacks for CPUs, GPUs and accelerators, and how these pains radiate outwards to both practitioners and hardware vendors, 2) How that led me to find the Apache TVM project, what it is, and why it matters, 3) Challenges and opportunities ahead ML compilation and TVM specifically, and what it can enable for ML end users everywhere.




**Bio:** Jason Knight is co-founder and CPO at OctoML building the machine learning acceleration platform for deploying ML anywhere. From the founders of the Apache TVM project, OctoML uses machine learning to generate efficient binaries for ML model deployment on any hardware. Before starting OctoML, Jason previously drove Intel’s AI software strategy, built large scale human sequencing data pipelines in the biotech industry, and earned a PhD in machine learning and computational biology.





**[Video Link](https://www.youtube.com/watch?v=KN4r_oVpfI0)**

4/15/21

Rutuja Surve

[Building Decentralized Neural Search Systems in Production](https://www.youtube.com/watch?v=WniuYVHqL80)

Abstract
With the rapid growth of media and meta data in both the enterprise and consumer markets, there is an evolving need for search systems to go beyond simple symbolic retrieval and towards more cognitive-driven understanding. Today, with the ever more long documents and multimedia data, finding the right information is more important and challenging than ever. The rise of deep learning has ushered in a new era of neural search. However, building a neural search system is non-trivial for researchers and engineers. While neural search has long held a significant promise, the advantages of open source combined with recent advances in deep learning now provides us a framework to make the next generation of search technology a reality.
In this talk, I will describe how Jina solves these challenges by providing an open source neural search ecosystem for businesses and developers, allowing anyone to search any kind of data with high availability and scalability - driving the shift from a traditional search system to a state-of-the-art AI-centric search system.




**Bio:** Rutuja is an Artificial Intelligence Engineer at Jina AI, with an interest in open source software and research. Her industry experience includes working with Google and Nutanix as a software engineer. She has been a former core contributor at MariaDB Foundation and has development experience contributing to various open source organisations like Mozilla, Linux Foundation and OWASP.





**[Video Link](https://www.youtube.com/watch?v=WniuYVHqL80)**

4/8/21

Lin Ma

[NoisePage: The Self-Driving Database Management System](https://www.youtube.com/watch?v=sY1c7qqQeuA)

Abstract
Database management systems (DBMSs) are an important part of modern data-driven applications. However, they are notoriously difficult to deploy and administer. There are existing methods that recommend physical design or knob configurations for DBMSs. But most of them require humans to make final decisions and decide when to apply changes. The goal of a self-driving DBMS is to remove the DBMS administration impediments by managing itself autonomously. In this talk, I present the design of a new self-driving DBMS (NoisePage) that enables such automatic system management. I first discuss a forecasting framework that uses unsupervised clustering and ensemble ML models to efficiently predict the query arrival rates under varying database workload patterns. I then describe NoisePage's modeling framework that constructs and maintains ML models to predict the behavior of self-driving DBMS actions: the framework decomposes the DBMS architecture into fine-grained operating units to estimate the system's behavior under unseen configurations. I then introduce our ongoing work for an action planning framework that makes explainable decisions based on the forecasted workload and the modeled behavior. Lastly, I explain how we integrate all the self-driving components into the system.




**Bio:** Lin Ma (https://www.cs.cmu.edu/~malin199/) is a PhD candidate from Carnegie Mellon University Computer Science Department advised by Andy Pavlo. He is interested in database systems and machine learning. His research focus has been on designing the architecture for self-driving databases. Lin was voted the 'most congenial PhD student' in the CMU Database Group in 2017, 2018, and 2020.





**[Livestream Link](https://www.youtube.com/watch?v=sY1c7qqQeuA)**

4/1/21

Ameet Talwalker

[Automating Architecture Transfer on Diverse Tasks](https://www.youtube.com/watch?v=ovpo0BdmNT4)

Abstract
Hand-crafted neural architecture design has played a major role in accelerating progress in computer vision, resulting in effective backbones like ResNet. Unfortunately, these convolutional backbones are not as effective in other domains. Successfully transferring existing architectures to applications such as sequence modeling, learning on graphs, or solving partial differential equations has required the manual design of task-specific neural operations to replace convolutions. In this talk, we will first motivate the problem of 'automating architecture transfer' to enable users to find the right operations given data from their specific domain. We will next present our ongoing work on this problem, by introducing a family of neural operations called 'XD-Operations' that mimic the inductive bias of multichannel convolutions while being much more expressive, provably containing numerous well-known operations. We then demonstrate the effectiveness of XD-operations on a diverse set of applications---in some cases outperforming the latest neural operation designs.




**Bio:** Ameet Talwalkar is an assistant professor in the Machine Learning Department at CMU, and also co-founder and Chief Scientist at Determined AI. His interests are in the field of statistical machine learning. His current work is motivated by the goal of democratizing machine learning, with a focus on topics related to automation, fairness, interpretability, and federated learning. He led the initial development of the MLlib project in Apache Spark, is a co-author of the textbook 'Foundations of Machine Learning' (MIT Press), and created an award-winning edX MOOC on distributed machine learning. He also helped to create the MLSys conference, serving as the inaugural Program Chair in 2018, General Chair in 2019, and currently as President of the MLSys Board.





**[Video Link](https://www.youtube.com/watch?v=ovpo0BdmNT4)**

3/25/21

Theodoros Rekatsinas

[Structure is all you need: Software 2.0 for Data Quality Management](https://www.youtube.com/watch?v=_2upFBZsMN4)

Abstract
Data quality management is a bottleneck in modern analytics as high-effort tasks such as data validation and cleaning are essential to obtain accurate results. In this talk, I will review how Software 2.0 can automate routine data validation tasks such as missing value imputation and detection of corrupted samples. First, I will discuss how one can leverage structured, statistical dependencies in the data to obtain information theoretically optimal data preparation methods, and then I will demonstrate how the widely-used Attention mechanism is key to automated data validation. This talk builds upon experience with projects such as HoloClean, FDX, and Picket and their application to different scientific and industrial use-cases.




**Bio:** Theodoros (Theo) Rekatsinas is an Assistant Professor in the Department of Computer Sciences at the University of Wisconsin-Madison, currently on leave at Apple. Theo is also a co-founder of Inductiv (now part of Apple), which developed technology that uses artificial intelligence to automate processes that involve identifying and correcting errors in data.





**[Video Link](https://www.youtube.com/watch?v=_2upFBZsMN4)**

3/18/21

Savin Goyal

[Taming the Long Tail of Industrial ML Applications](https://www.youtube.com/watch?v=wassHqe_Clg)

Abstract
Data Science usage at Netflix goes much beyond our eponymous recommendation systems. It touches almost all aspects of our business - from optimizing content delivery and informing buying decisions to fighting fraud. Our unique culture affords our data scientists extraordinary freedom of choice in ML tools and libraries, all of which results in an ever-expanding set of interesting problem statements and a diverse set of ML approaches to tackle them. Our data scientists, at the same time, are expected to build, deploy, and operate complex ML workloads autonomously without the need to be significantly experienced with systems or data engineering. In this talk, I will discuss some of the challenges involved in improving the development and deployment experience for ML workloads. I will focus on Metaflow, our ML framework, which offers useful abstractions for managing the model’s lifecycle end-to-end, and how a focus on human-centric design positively affects our data scientists' velocity.




**Bio:** Savin is a software engineer at Netflix responsible for Metaflow, Netflix's ML platform. He focuses on building generalizable infrastructure to accelerate the impact of data science at Netflix and beyond.





**[Video Link](https://www.youtube.com/watch?v=wassHqe_Clg)**

3/11/21

Fabio Petroni

[Assessing Machine Knowledge](https://www.youtube.com/watch?v=0xiqtf0-w3I)

Abstract
In the talk I will review a set of general approaches for representing large scale textual knowledge sources that are useful for multiple downstream tasks. I will present benchmarking tools spanning multiple domains (including Question Answering, Entity Linking and Dialogue) and I will describe the latest knowledge-intensive NLP models with a focus on their efficiency.




**Bio:** Fabio is a Research Engineer in the Facebook Artificial Intelligence Research (FAIR) lab in London. His research focuses on Natural Language Processing, in particular, Information Extraction, Question Answering and Knowledge Representation. Prior to joining Facebook, he was with the R&D department of Thomson Reuters and received a PhD degree from Sapienza University of Rome.





**[Video Link](https://www.youtube.com/watch?v=0xiqtf0-w3I)**

3/4/21

Sara Hooker

[The Hardware Lottery](https://www.youtube.com/watch?v=vMhA-xl3dbA)

Abstract
I will introduce the term Hardware lottery to describe when a research idea wins because it is suited to the available software and hardware and not because the idea is superior to alternative research directions. This talk will motivate attention to hardware lotteries by discussing examples from early computer history which have delayed research progress by casting successful ideas as failures. These lessons are particularly salient given the advent of domain specialized hardware which make it increasingly costly to stray off of the beaten path of research ideas.




**Bio:** Sara Hooker is a researcher at Google Brain working on reliable explanations of model behavior. Her main research interests gravitate towards training models beyond test-set accuracy to be compact, robust, fair and interpretable. In 2014, she founded Delta Analytics, a non-profit dedicated to bringing technical capacity to help non-profits across the world use machine learning for good.





**[Video Link](https://www.youtube.com/watch?v=vMhA-xl3dbA)**

2/25/21

Anna Goldie

[Chip Floorplanning with Deep Reinforcement Learning](https://www.youtube.com/watch?v=Y4fcSwsNqoE)

Abstract
In this talk, I will describe a reinforcement learning (RL) method for chip floorplanning, the engineering problem of designing the physical layout of a computer chip. Chip floorplanning ordinarily requires weeks or months of effort by physical design engineers to produce manufacturable layouts. Our method generates floorplans in under six hours that are superior or comparable to humans in all key metrics, including power consumption, performance, and chip area. To achieve this, we pose chip floorplanning as a reinforcement learning problem, and develop a novel edge-based graph convolutional neural network architecture capable of learning rich and transferrable representations of the chip. Our method was used in the design of the next generation of Google’s artificial intelligence (AI) accelerators (TPU).




**Bio:** Anna Goldie is a Staff Researcher at Google Brain and co-founder/tech-lead of the Machine Learning for Systems Team. She is also a PhD student in the Stanford NLP Group, where she is advised by Prof. Chris Manning. At MIT, she earned a Masters of Computer Science, Bachelors of Computer Science, and Bachelors of Linguistics. She speaks fluent Mandarin, Japanese, and French, as well as conversational Spanish, Italian, German, and Korean. Her work has been covered in various media outlets, including MIT Technology Review and IEEE Spectrum.





**[Livestream Link](https://www.youtube.com/watch?v=Y4fcSwsNqoE)**

2/18/21

Piero Molino

[Ludwig, a Declarative Deep Learning Toolbox](https://www.youtube.com/watch?v=BTkl_qc0Plc)

Abstract
The talk will introduce Ludwig, a deep learning toolbox that allows to train models and to use them for prediction without the need to write code. Thanks to its declarative configuration system and the use of data types to guide piepeline building, it helps make deep learning approachable for non-experts and enable faster model improvement iteration cycles for experienced machine learning engineers and researchers. By using Ludwig, experts and researchers can simplify the development process and focus on experiment comparison and model quality. We will also discuss recent improvements to Ludwig, including AutoML and hyperparameter optimization capabilities, its backstory and its future releases.




**Bio:** Piero Molino is a Staff Research Scientist at Stanford University working on Machine Learning systems and algorithms. Piero completed a PhD on Question Answering at the University of Bari, Italy. Founded QuestionCube, a startup that built a framework for semantic search and QA. Worked for Yahoo Labs in Barcelona on learning to rank, IBM Watson in New York on natural language processing with deep learning and then joined Geometric Intelligence, where he worked on grounded language understanding. After Uber acquired Geometric Intelligence, he became one of the founding members of Uber AI Labs. At Uber he worked on research topics including Dialogue Systems, Language Generation, Graph Representation Learning, Computer Vision, Reinforcement Learning and Meta Learning. He also worked on several deployed systems like COTA, an ML and NLP model for Customer Support, Dialogue Systems for driver hands free dispatch, pickup and communications, and on the Uber Eats Recommender System with graph learning. He is the author of Ludwig, a code-free deep learning toolbox.





**[Video Link](https://www.youtube.com/watch?v=BTkl_qc0Plc)**

2/11/21

Shreya Shankar

[Debugging Machine Learning in Production](https://www.youtube.com/watch?v=aGzu7nI8IRE)

Abstract
Machine learning pipelines can successfully demonstrate high performance on train and evaluation datasets, but what happens after you promote that model to production? What are some of the challenges faced, and how do groups of different stakeholders with different technical abilities collaborate to identify and “fix” bugs? In my talk, I will draw from my experiences to describe a high level overview of modern ML infrastructure, criteria for promoting models, case studies of “bugs” encountered when clients were interacting with the live ML predictions, and the challenges in solving these issues.




**Bio:** Shreya is a computer scientist living in San Francisco interested in making machine learning work in the “real world.” Currently, she is taking a break from work, but previously, she was the first ML engineer at Viaduct, did ML research at Google Brain, and completed her BS and MS in computer science at Stanford.





**[Video Link](https://www.youtube.com/watch?v=aGzu7nI8IRE)**

2/4/21

Josh Tobin

[A missing link in the ML infrastructure stack?](https://www.youtube.com/watch?v=qERW9R3espg)

Abstract
Machine learning is quickly becoming a product engineering discipline. Although several new categories of infrastructure and tools have emerged to help teams turn their models into production systems, doing so is still extremely challenging for most companies. In this talk, we survey the tooling landscape and point out several parts of the machine learning lifecycle that are still underserved. We propose a new category of tool that could help alleviate these challenges and connect the fragmented production ML tooling ecosystem. We conclude by discussing similarities and differences between our proposed system and those of a few top companies.




**Bio:** Josh Tobin is the founder and CEO of a stealth machine learning startup. Previously, Josh worked as a deep learning & robotics researcher at OpenAI and as a management consultant at McKinsey. He is also the creator of Full Stack Deep Learning (fullstackdeeplearning.com), the first course focused on the emerging engineering discipline of production machine learning. Josh did his PhD in Computer Science at UC Berkeley advised by Pieter Abbeel.





**[Video Link](https://www.youtube.com/watch?v=qERW9R3espg)**

1/28/21

Travis Addair

[Horovod and the Evolution of Deep Learning at Scale](https://www.youtube.com/watch?v=DB7oOZ5hyrE)

Abstract
Deep neural networks are pushing the state of the art in numerous machine learning research domains; from computer vision, to natural language processing, and even tabular business data. However, scaling such models to train efficiently on large datasets imposes a unique set of challenges that traditional batch data processing systems were not designed to solve. Horovod is an open source framework that scales models written in TensorFlow, PyTorch, and MXNet to train seamlessly on hundreds of GPUs in parallel. In this talk, we'll explain the concepts and unique constraints that led to the development of Horovod at Uber, and discuss how the latest trends in deep learning research are informing the future direction of the project within the Linux Foundation. We'll explore how Horovod fits into production ML workflows in industry, and how tools like Spark and Ray can combine with Horovod to make productionizing deep learning at scale on remote data centers as simple as running locally on your laptop. Finally, we'll share some thoughts on what's next for large scale deep learning, including new distributed training architectures and how the larger ecosystem of production ML tooling is evolving.




**Bio:** Travis Addair is a software engineer at Uber leading the Deep Learning Training team as part of the Michelangelo machine learning platform. He is the lead maintainer for the Horovod open source project and chairs its Technical Steering Committee within the Linux Foundation. In the past, he’s worked on scaling machine learning systems at Google and Lawrence Livermore National Lab.





**[Video Link](https://www.youtube.com/watch?v=DB7oOZ5hyrE)**

1/21/21

Song Han

[TinyML: Reducing the Carbon Footprint of Artificial Intelligence in the Internet of Things (IoT)](https://www.youtube.com/watch?v=nMiCcZffup8)

Abstract
Deep learning is computation-hungry and data-hungry. We aim to improve the computation efficiency and data efficiency of deep learning. I will first talk about MCUNet that brings deep learning to IoT devices. The technique is tiny neural architecture search (TinyNAS) co-designed with a tiny inference engine (TinyEngine), enabling ImageNet-scale inference on an IoT device with only 1MB of FLASH. Next I will talk about TinyTL that enables on-device training, reducing the memory footprint by 7-13x. Finally, I will describe Differentiable Augmentation that enables data-efficient GAN training, generating photo-realistic images using only 100 images, which used to require tens of thousand of images. We hope such TinyML techniques can make AI greener, faster, and more sustainable.




**Bio:** Song Han is an assistant professor in MIT EECS. He received his PhD degree from Stanford University. His research focuses on efficient deep learning computing. He proposed “deep compression” technique that can reduce neural network size by an order of magnitude without losing accuracy, and the hardware implementation “efficient inference engine” that first exploited pruning and weight sparsity in deep learning accelerators. His recent research on hardware-aware neural architecture search and TinyML was highlighted by MIT News, Wired, and Venture Beat, and received many low-power computer vision (LPCV) contest awards. Song received Best Paper awards at ICLR’16 and FPGA’17, Amazon Machine Learning Research Award, SONY Faculty Award, Facebook Faculty Award. Song was named “35 Innovators Under 35” by MIT Technology Review for his contribution on “deep compression” technique that “lets powerful artificial intelligence (AI) programs run more efficiently on low-power mobile devices.” Song received the NSF CAREER Award for “efficient algorithms and hardware for accelerated machine learning.”





**[Video Link](https://www.youtube.com/watch?v=nMiCcZffup8)**

12/10/20

Kayvon Fatahalian

[From Ideas to Video Analysis Models in Hours, Not Weeks](https://www.youtube.com/watch?v=u62aAtBCxEU)

Abstract
My students and I often find ourselves as "subject matter experts" needing to create video understanding models that serve computer graphics and video analysis applications. Unfortunately, like many, we are frustrated by how a smart grad student, armed with a large \*unlabeled\* video collection, an palette of pre-trained models, and an idea of what novel object or activity they want to detect/segment/classify, requires days-to-weeks to create and validate a model for their task. In this talk I will discuss challenges we've faced in the iterative process of curating data, training models, and validating models for the specific case of rare events and categories in image and video collections. In this regime we've found that conventional wisdom about training on imbalance data sets, and data acquisition via active learning does not lead to the most efficient solutions. I'll discuss these challenges in the context of image and video analysis applications, and elaborate on our ongoing vision of how a grad student, armed with massive amounts of unlabeled video data, pretrained models, and available-in-seconds-supercomputing-scale elastic compute should be able to interactively iterate on cycles of acquiring training data, training models, and validating models.




**Bio:** Kayvon Fatahalian is an Assistant Professor in the Computer Science Department at Stanford University. His lab works on visual computing systems projects, including large-scale video analytics, programming systems for video data mining, compilation techniques for optimizing image processing pipelines. In all these efforts, the goal is to enable more rapid development of applications that involve video processing at scale.





**[Video Link](https://www.youtube.com/watch?v=u62aAtBCxEU)**

12/03/20

Matthias Poloczek

[Scalable Bayesian Optimization for Industrial Applications](https://www.youtube.com/watch?v=gpTxayP4CIU)

Abstract
Bayesian optimization has become a powerful method for the sample-efficient optimization of expensive black-box functions. These functions do not have a closed-form and are evaluated for example by running a complex economic simulation, by an experiment in the lab or in a market, or by a CFD simulation. Use cases arise in machine learning, e.g., when tuning the configuration of an ML model or when optimizing a reinforcement learning policy. Examples in engineering include the design of aerodynamic structures or materials discovery. In this talk I will introduce the key ideas of Bayesian optimization and discuss how they can be applied to tuning ML models. Moreover, I will share some experiences with developing a Bayesian optimization service in industry.




**Bio:** Matthias’ research interests lie at the intersection of machine learning and optimization, with a focus on Bayesian methods for 'exotic' optimization problems arising in business applications and in the natural sciences. He is a Principled Scientist at Amazon. Previously, Matthias was a Senior Manager at Uber AI, where he founded Uber’s Bayesian optimization team and led the cross-org effort that built a company-wide service to tune ML models at scale. Matthias received his PhD in CS from Goethe University in Frankfurt in 2013 and then worked as a postdoc at Cornell with David Williamson and Peter Frazier from 2014 until 2017. He was an Assistant Professor in the Department of Systems and Industrial Engineering at the University of Arizona from 2017 until 2019.





**[Video Link](https://www.youtube.com/watch?v=gpTxayP4CIU)**

11/19/20

Roy Frostig

[JAX: accelerating machine learning research by composing function transformations in Python](https://www.youtube.com/watch?v=mbUwCPiqZBM)

Abstract
JAX is a system for high-performance machine learning research and numerical computing. It offers the familiarity of Python+NumPy together with hardware acceleration, plus a set of composable function transformations: automatic differentiation, automatic batching, end-to-end compilation (via XLA), parallelizing over multiple accelerators, and more. JAX's core strength is its guarantee that these user-wielded transformations can be composed arbitrarily, so that programmers can write math (e.g. a loss function) and transform it into pieces of an ML program (e.g. a vectorized, compiled, batch gradient function for that loss).
JAX had its open-source release in December 2018 (https://github.com/google/jax). It's used by researchers for a wide range of applications, from studying training dynamics of neural networks, to probabilistic programming, to scientific applications in physics and biology.




**Bio:** Roy Frostig is a research scientist at Google. He's interested in forming reliable foundations for machine learning, by making software systems for ML research and by studying the statistical elements of its practice. He received his BS, MS, and PhD from Stanford, advised by Percy Liang.





**[Video Link](https://www.youtube.com/watch?v=mbUwCPiqZBM)**

11/12/20

Chip Huyen

[Principles of Good Machine Learning Systems Design](https://www.youtube.com/watch?v=c_AUuTuPA5k)

Abstract
This talk covers what it means to operationalize ML models. It starts by analyzing the difference between ML in research vs. in production, ML systems vs. traditional software, as well as myths about ML production.
It then goes over the principles of good ML systems design and introduces an iterative framework for ML systems design, from scoping the project, data management, model development, deployment, maintenance, to business analysis. It covers the differences between DataOps, ML Engineering, MLOps, and data science, and where each fits into the framework. It also discusses the main skills each stage requires, which can help companies in structuring their teams.
The talk ends with a survey of the ML production ecosystem, the economics of open source, and open-core businesses.




**Bio:** Chip Huyen is an engineer who develops tools and best practices for machine learning production. She’s currently with Snorkel AI and she’ll be teaching Machine Learning Systems Design at Stanford from January 2021. Previously, she was with Netflix, NVIDIA, Primer. She’s also the author of four bestselling Vietnamese books.





**[Video Link](https://www.youtube.com/watch?v=c_AUuTuPA5k)**

11/05/20

Alex Ratner

[Programmatically Building & Managing Training Data with Snorkel](https://www.youtube.com/watch?v=pDVV4zKNqIE)

Abstract
One of the key bottlenecks in building machine learning systems is creating and managing the massive training datasets that today's models require. In this talk, I will describe our work on Snorkel (snorkel.org), an open-source framework for building and managing training datasets, and describe three key operators for letting users build and manipulate training datasets: labeling functions, for labeling unlabeled data; transformation functions, for expressing data augmentation strategies; and slicing functions, for partitioning and structuring training datasets. These operators allow domain expert users to specify machine learning (ML) models entirely via noisy operators over training data, expressed as simple Python functions---or even via higher level NL or point-and-click interfaces---leading to applications that can be built in hours or days, rather than months or years, and that can be iteratively developed, modified, versioned, and audited. I will describe recent work on modeling the noise and imprecision inherent in these operators, and using these approaches to train ML models that solve real-world problems, including recent state-of-the-art results on benchmark tasks and real-world industry, government, and medical deployments.




**Bio:** Alex Ratner is the co-founder and CEO of Snorkel AI, Inc., which supports the open source Snorkel library and develops Snorkel Flow, an end-to-end system for building machine learning applications, and an Assistant Professor of Computer Science at the University of Washington. Prior to Snorkel AI and UW, he completed his PhD in CS advised by Christopher Ré at Stanford, where his research focused on applying data management and statistical learning techniques to emerging machine learning workflows, such as creating and managing training data, and applying this to real-world problems in medicine, knowledge base construction, and more.





**[Video Link](https://www.youtube.com/watch?v=pDVV4zKNqIE)**

10/29/20

Virginia Smith

[On Heterogeneity in Federated Settings](https://www.youtube.com/watch?v=laCyJICLyWg)

Abstract
A defining characteristic of federated learning is the presence of heterogeneity, i.e., that data and compute may differ significantly across the network. In this talk I show that the challenge of heterogeneity pervades the machine learning process in federated settings, affecting issues such as optimization, modeling, and fairness. In terms of optimization, I discuss FedProx, a distributed optimization method that offers robustness to systems and statistical heterogeneity. I then explore the role that heterogeneity plays in delivering models that are accurate and fair to all users/devices in the network. Our work here extends classical ideas in multi-task learning and alpha-fairness to large-scale heterogeneous networks, enabling flexible, accurate, and fair federated learning.




**Bio:** Virginia Smith is an assistant professor in the Machine Learning Department at Carnegie Mellon University. Her research interests span machine learning, optimization, and distributed systems. Prior to CMU, Virginia was a postdoc at Stanford University, received a Ph.D. in Computer Science from UC Berkeley, and obtained undergraduate degrees in Mathematics and Computer Science from the University of Virginia.





**[Video Link](https://www.youtube.com/watch?v=laCyJICLyWg)**

10/22/20

Matei Zaharia

[Machine Learning at Industrial Scale: Lessons from the MLflow Project](https://www.youtube.com/watch?v=nCQ9WqXPIS4)

Abstract
Although enterprise adoption of machine learning is still early on, many enterprises in all industries already have hundreds of internal ML applications. ML powers business processes with an impact of hundreds of millions of dollars in industrial IoT, finance, healthcare and retail. Building and operating these applications reliably requires infrastructure that is different from traditional software development, which has led to significant investment in the construction of “ML platforms” specifically designed to run ML applications. In this talk, I’ll discuss some of the common challenges in productionizing ML applications based on experience building MLflow, an open source ML platform started at Databricks. MLflow is now the most widely used open source project in this area, with over 2 million downloads a month and integrations with dozens of other products. I’ll also highlight some interesting problems users face that are not covered deeply in current ML systems research, such as the need for “hands-free” ML that can train thousands of independent models without direct tuning from the ML developer for regulatory reasons, and the impact of privacy and interpretability regulations on ML. All my examples will be based on experience at large Databricks / MLflow customers.




**Bio:** Matei Zaharia is an Assistant Professor of Computer Science at Stanford University and Chief Technologist at Databricks. He started the Apache Spark project during his PhD at UC Berkeley in 2009, and has worked broadly on other cluster computing and analytics software, including MLflow and Delta Lake. At Stanford, Matei is a co-PI of the DAWN Lab doing research on infrastructure for machine learning. Matei’s work was recognized through the 2014 ACM Doctoral Dissertation Award, an NSF CAREER Award, and the US Presidential Early Career Award for Scientists and Engineers (PECASE).





**[Video Link](https://www.youtube.com/watch?v=nCQ9WqXPIS4)**

10/15/20

Marco Tulio Ribeiro

[Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://www.youtube.com/watch?v=VqiTtdY58Ts)

Abstract
We will present CheckList, a task-agnostic methodology and tool for testing NLP models inspired by principles of behavioral testing in software engineering.

We will show a lot of fun bugs we discovered with CheckList, both in commercial models (Microsoft, Amazon, Google) and research models (BERT, RoBERTA for sentiment analysis, QQP, SQuAD). We'll also present comparisons between CheckList and the status quo, in a case study at Microsoft and a user study with researchers and engineers. We show that CheckList is a really helpful process and tool for testing and finding bugs in NLP models, both for practitioners and researchers.




**Bio:** Marco Tulio Ribeiro is a Senior Researcher at Microsoft Research. His work is on facilitating the communication between humans and machine learning models, which includes interpretability, trust, debugging, feedback, robustness, testing, etc. He received his PhD from the University of Washington.





**[Video Link](https://www.youtube.com/watch?v=VqiTtdY58Ts)**

**Seminar Hosts:** Simran Arora, Dan Fu.

**Guest Hosts (2023 Foundation Models Limited Series)**: Avanika Narayan, Michael Zhang, Percy Liang, Tatsu Hashimoto.

**Executive Producer:** Chris Ré.

**Alumni:**

- Karan Goel (co-host, 2020-2023)
- Fiodar Kazhamakia (co-host, 2020-2022)
- Piero Molino (co-host, 2020-2022)
- Matei Zaharia (executive producer, 2020-2022)

From Fall 2021-Spring 2022, we ran the MLSys seminar alongside [CS 528](https://mlsys.stanford.edu/cs528).

You can reach us at sysmlstanfordseminar \[at\] gmail.

If you’d like to clone this website for your own talk series, source code can be found [here](https://github.com/stanford-sysml-seminar/stanford-sysml-seminar.github.io).