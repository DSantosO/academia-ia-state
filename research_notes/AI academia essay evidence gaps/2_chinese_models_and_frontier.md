# Chinese models' "other direction" and how frontier AI capability is actually distributed (as of 15 Oct 2026)

Conventions used in these notes:
- **Access date.** Every live page, leaderboard, dataset and licence file was accessed on **2026-10-15** unless stated otherwise.
- **Source tags:**
  - [primary]: I read the document, dataset or licence text itself.
  - [secondary]: I read a news or analysis article reporting the fact.
  - [search-summary]: the fact comes only from a search-engine digest and I did not open the page. These are the weakest items and are flagged for re-checking.
- **Disclosure.** These notes were compiled by a Claude model (Anthropic). For that reason, every capability ranking below is reproduced numerically from third-party trackers, and no first-party Anthropic claims are used.

---

## Q1. Openness of Chinese frontier labs, 2024–2026: what is released, under which licences, at what reported cost

### Takeaway
From 2024 to 2025, Chinese labs released frontier-adjacent **weights** under mostly permissive licences (MIT, Apache 2.0, "modified MIT"), often with technical reports. **None released pretraining data.** In 2026 the picture split:
- **Still permissive:** DeepSeek and Xiaomi stayed on MIT, and Tencent moved to Apache 2.0.
- **Restricted or closed:** Alibaba, Moonshot, Zhipu, MiniMax and StepFun now either keep their flagships API-only or ship them under custom "open-weight with commercial strings" licences that resemble Meta's Llama model.

DeepSeek's USD 5.6M figure covers the GPU rental cost of one final pretraining run, not the cost of building the model.

### Cited Findings

**Release pattern and licences, by lab.** Unless noted, these come from the Hugging Face API (repo creation dates and licence tags, accessed 2026-10-15) [primary]: [HF API listing](https://huggingface.co/api/models?author=deepseek-ai&sort=createdAt&direction=-1).

- **DeepSeek**
  - V3-Base was posted 2024-12-25.
  - R1 (2025-01-20) is MIT, with distilled Qwen and Llama variants also MIT.
  - V3-0324, V3.1, V3.2-Exp and V3.2 (Dec 2025) are all MIT.
  - **V4-Pro and V4-Flash** were posted 2026-04-22 under MIT. Later V4 checkpoints are also MIT: V4-Flash-0731, V4-Pro-0813, V4-Flash-Vision-Exp (2026-08-31) and **V4.1-Flash** (2026-09-10). — [HF deepseek-ai](https://huggingface.co/deepseek-ai) [primary]
  - Public V4 launch date was 2026-04-24. — [DataCamp](https://www.datacamp.com/blog/deepseek-v4) [secondary]
  - The V3 technical report states "2.788M H800 GPU hours for its full training." — [arXiv 2412.19437](https://arxiv.org/abs/2412.19437) [primary]
  - DeepSeek's R1 paper was published in *Nature* on 17 Sep 2025, described as the first major LLM to pass journal peer review. — [Scientific American](https://www.scientificamerican.com/article/secrets-of-chinese-ai-model-deepseek-revealed-in-landmark-paper); DOI [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z) [secondary]
- **Alibaba Qwen**
  - Qwen2.5 (Sep 2024) used mixed licences. The 72B model was under the Qwen License, 3B under the Qwen *Research* licence (non-commercial), and the other sizes under Apache 2.0. — [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen) [secondary]
  - Qwen3 (28 Apr 2025) was Apache 2.0.
  - **Qwen3-Max (Sep 2025) was proprietary.** — [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen) [secondary]
  - In 2026 these open releases were all Apache 2.0 [primary, HF tags]:
    - Qwen3.5-397B-A17B and smaller sizes (Feb 2026)
    - Qwen3.6-35B-A3B and 27B (Apr 2026)
    - Qwen3.8-27B (Aug 2026)
  - In 2026 these were hosted only, with no published weights: Qwen3.5-Plus, Qwen3.6-Plus, Qwen3.5-Omni (Feb–Apr 2026), **Qwen3.7-Max and Qwen3.7-Plus (May–June 2026)** and Qwen3.8-Max cloud (3 Aug 2026). — [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen) [secondary]; corroborated by [ASPI, 22 Jul 2026](https://www.aspistrategist.org.au/some-chinese-ai-will-go-closed-source-but-not-all/) ("its latest, Qwen-3.7, is proprietary") [secondary]
  - **Qwen3.8-2.4T-A95B weights** (HF 2026-08-08) ship under a custom "Qwen3.8-Max License" with two conditions:
    - Model-name attribution if a product has more than 100M monthly active users (MAU) or more than USD 20M monthly revenue.
    - A separate licence for "Model as a Service or AI Work Assistant" businesses with more than USD 50M revenue over 12 months.
    - — [licence text](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE) [primary]
  - **Qwen3.8-Flash-Next** (HF 2026-08-24) uses the new "Qwen Community License 1.0". Any MaaS or AI Work Assistant business needs a separate licence, with **no revenue threshold**. — [licence text](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/raw/main/LICENSE) [primary]
- **Moonshot (Kimi)**
  - Kimi K2 (Jul 2025), K2 Thinking (Nov 2025), K2.5 (Jan 2026), K2.6 (Apr 2026) and K2.7-Code (Jun 2026) all use a "Modified MIT" licence. Its only addition is that products with more than 100M MAU or more than USD 20M monthly revenue must display "Kimi K2". — [Kimi K2 LICENSE](https://huggingface.co/moonshotai/Kimi-K2-Instruct/raw/main/LICENSE) [primary]
  - **Kimi K3** (weights reportedly 27 Jul 2026) uses a custom "Kimi K3 License":
    - Model-as-a-Service operators with more than USD 20M aggregate revenue over 12 months must sign a separate agreement before any commercial use.
    - Internal use is exempt.
    - — [Kimi K3 LICENSE](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE) [primary]; release date per [Implicator](https://www.implicator.ai/moonshot-attaches-20-million-revenue-clause-to-kimi-k3-open-weights/) [search-summary]
- **Zhipu / Z.ai**
  - GLM-4.5 (Jul 2025), 4.6, 4.7, **GLM-5 (Feb 2026)**, 5.1 and 5.2 are all MIT [primary, HF tags].
  - GLM-5-Turbo was rolled out closed. — [Implicator](https://www.implicator.ai/stanfords-2026-ai-index-puts-us-lead-over-china-at-2-7-as-deepseek-v4-stalls/) [secondary]
  - **GLM-5.3** (weights 2026-08-25) uses a custom licence: MaaS operators with more than USD **10 billion** revenue "must pass Z.AI's security review" before commercial use. — [GLM-5.3 LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE) [primary]
  - GLM-5.3-Flash remains MIT [primary].
- **MiniMax**
  - M1 (Jun 2025) is Apache 2.0, and M2, M2.1 and M2.5 (Oct 2025–Feb 2026) are "modified-MIT" [primary, HF tags].
  - **M3** (Jun 2026) uses the "MiniMax Community License". It grants rights "for non-commercial purposes" by default. Commercial use requires a "Built with MiniMax M3" notice, and products with more than USD 20M yearly revenue need prior written authorisation. — [M3 LICENSE](https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/LICENSE) [primary]
- **Baidu ERNIE 4.5**
  - Ten-plus variants, from 0.3B up to a 424B-total MoE, were posted 28–29 Jun 2025 (announced 30 Jun/1 Jul 2025) under Apache 2.0. — [HF API](https://huggingface.co/api/models?author=baidu) [primary]; [TechNode](https://technode.com/2025/07/01/baidu-open-sources-ernie-4-5-series-models-including-multimodal-moe-architecture/) [secondary]
  - ERNIE 5.1 is listed as **proprietary** on Arena. — [Arena dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset) [primary]
- **Tencent Hunyuan**
  - Hunyuan-A13B (Jun 2025) licence: "THIS LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA". It also requires licensees with more than 100M MAU to request a licence. — [Hunyuan-A13B LICENSE](https://huggingface.co/tencent/Hunyuan-A13B-Instruct/raw/main/LICENSE) [primary]
  - The same carve-out appears in Hunyuan 3D 2.0/2.1 and HunyuanImage 3.0. — [ScanCode LicenseDB](https://scancode-licensedb.aboutcode.org/tencent-hunyuan-image-3.0-cla.html) [search-summary]
  - **Hy3 (Jul 2026) and Hy4-preview (Aug 2026) are tagged Apache 2.0.** — [HF API](https://huggingface.co/api/models?author=tencent) [primary]
- **Others**
  - Xiaomi MiMo-V2 (Dec 2025), V2.5 (Apr 2026) and **MiMo-V2.6-Pro (Sep 2026)** are MIT. — [HF API](https://huggingface.co/api/models?author=XiaomiMiMo) [primary]
  - StepFun Step3 (Jul 2025) and Step-3.5/3.7-Flash are Apache 2.0.
  - StepFun **Step-5-Preview (Sep 2026)** has a custom licence. It requires a commercial licence for device makers, and for MaaS operators with more than USD 20M revenue over 12 months. — [Step-5 LICENSE](https://huggingface.co/stepfun-ai/Step-5-Preview/raw/main/LICENSE.txt) [primary]
- **Pattern-level confirmation.** ASPI (22 Jul 2026) reports that "some Chinese AI labs had started keeping the weights of their latest AI models proprietary". It notes that at Moonshot "the marketing team wanted the stronger revenue of closed-source", and that Xi's July 2026 World AI Conference (WAIC) speech did not specifically endorse open source. — [ASPI Strategist](https://www.aspistrategist.org.au/some-chinese-ai-will-go-closed-source-but-not-all/) [secondary]
- **Investor pressure.** Z.ai (Zhipu) and MiniMax listed in Hong Kong in January 2026, adding pressure for returns. Hugging Face's Tiezhen Wang said the sustainability of open releases "still hinges on financial results". — [MIT Technology Review, 12 Feb 2026](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) [secondary]

**Training data and transparency (no Chinese lab releases its corpus).**
- The 2025 Foundation Model Transparency Index (Stanford CRFM, Dec 2025) scored companies out of 100:
  - DeepSeek 32 and Alibaba 26, both in the bottom half, as is Meta.
  - IBM highest at 95.
  - The index reports: "Openness correlates with—but isn't sufficient for—transparency" and "Training data continues to be opaque". — [FMTI Dec 2025](https://crfm.stanford.edu/fmti/December-2025) [primary]
  - Meta fell from 60 (2024) to 31, and the average fell from 58 to 40. — [Stanford HAI](https://hai.stanford.edu/news/transparency-in-ai-is-on-the-decline) [search-summary]
- The European Open Source AI Index (Radboud) says DeepSeek uses an undisclosed training dataset and is "at best an open weights model". It places DeepSeek only slightly more open than Llama and far from OLMo. — [OSAI: How open is DeepSeek?](https://osai-index.eu/news/deepseek/) [search-summary]
- USCC's March 2026 paper: "Most models described as 'open' in this paper are only open-weight." — [USCC, Luong, 23 Mar 2026](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]

**Training-cost claims and disputes.**
- **DeepSeek-V3's USD 5.576M** figure was derived as follows:
  - It assumes rented H800s at USD 2/hour for about 2.8M GPU-hours.
  - DeepSeek itself cautioned that it covers only the official training run, "excluding earlier research and ablation experiments". — [heise](https://heise.de/-10267795) [search-summary]; GPU-hours [primary] in [arXiv 2412.19437](https://arxiv.org/abs/2412.19437)
- **SemiAnalysis (31 Jan 2025)** disputed it as a measure of total cost:
  - DeepSeek has "access to around 50,000 Hopper GPUs" (including about 10k H800 and about 10k H100).
  - "total server CapEx for DeepSeek is ~$1.6B", plus about USD 944M in cluster operating costs.
  - The USD 6M covers "just the GPU cost of the pre-training run". — [SemiAnalysis "DeepSeek Debates"](https://newsletter.semianalysis.com/p/deepseek-debates) [primary]
  - Note that the USD 1.6B is fleet capex, partly shared with the parent hedge fund High-Flyer. It is not a rival per-model cost, although some outlets reported it that way. — [techstrong.ai](https://techstrong.ai/agentic-ai/early-critic-of-deepseek-says-model-cost-was-1-6-billion-not-5-6-million/) [search-summary]
- **R1 in *Nature* (17 Sep 2025).** The supplementary material reports:
  - R1's reasoning training cost about USD 294,000 (512 H800s for about 80 hours), on top of about USD 6M for the base model.
  - DeepSeek admitted owning A100s used for preparatory experiments. — [Scientific American](https://www.scientificamerican.com/article/secrets-of-chinese-ai-model-deepseek-revealed-in-landmark-paper) [search-summary]
- **Investment asymmetry.** US private AI investment was **USD 285.9B in 2025 vs USD 12.4B for China**. — [Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report) [primary]

### Inferences
- "Chinese = open" was a fair description of 2025. By Oct 2026 it is true only lab by lab:
  - **Permissive:** DeepSeek and Xiaomi (MIT), and Tencent's Hy3/Hy4 (Apache 2.0).
  - **Revenue-gated or "security-review" licences:** Qwen's flagship, Kimi K3, GLM-5.3, MiniMax M3 and Step-5.
  - **Closed hosted flagships:** Qwen3.x-Max/Plus and GLM-5-Turbo.
- The 2026 Chinese licences converge on one template: free use, research and internal deployment, plus a gate on large API resellers. That is structurally the same as Meta's Llama (700M-MAU gate) and Meta's new Muse Spark Open licence (USD 20M gate; see Q2). It is a business model, not an ideology.
- "Open" at every Chinese lab means open weights, sometimes with inference and training code and a technical report, but **never open training data**. On data, Chinese labs are no more open than US closed labs.
- The USD 5.6M figure is accurate for what it claims: marginal compute for one run. It should not be cited as "what it costs to build a frontier model". Use "a final training run reportedly costing about USD 5.6M in rented-GPU terms, on a fleet SemiAnalysis estimated at about USD 1.6B capex".

### Gaps
- I did not open DeepSeek's original Dec 2024 "DeepSeek License" weight terms for V3. The HF tag for V3-Base is blank, and several older repos show `other/deepseek`.
- Kimi K2 Thinking's widely reported "USD 4.6M" training cost (CNBC, citing a source) and MiniMax-M1's "USD 534,700" RL cost were not verified.
- The Kimi K3 weight-release date (27 Jul 2026) is from secondary write-ups. The HF repo was created 2026-06-13.
- **Label conflicts between trackers:**
  - Epoch labels Kimi K3 "Open weights (non-commercial)", but the licence text allows commercial use except for large MaaS operators.
  - Arena lists GLM-5.3 as "MIT", while the HF repo carries a custom GLM-5.3 licence.
  - Trackers' licence labels should not be cited without checking the licence file.

---

## Q2. Comparison with US and EU openness (gpt-oss, Llama/Meta, Gemma, OLMo, Mistral, 2026 changes)

### Takeaway
US and EU openness moved in mixed directions:
- **More open:** OpenAI returned to open weights (gpt-oss, Apache 2.0, Aug 2025), Google moved Gemma 4 to Apache 2.0 (Apr 2026), and Ai2 and the Swiss Apertus team remain the only "fully open, including data" producers at scale.
- **Less open:** Meta moved its flagship to closed or hosted models (Muse Spark, Muse Wonder) and now ships open weights under a custom revenue-threshold licence.

Every US frontier lab keeps its best model closed, and the best US open-weight models trail the best Chinese open-weight models.

### Cited Findings
- **OpenAI**
  - gpt-oss-120b and gpt-oss-20b were released **5 Aug 2025** under **Apache 2.0**, OpenAI's first open-weight language models since GPT-2 (2019).
  - Weights only: no training data or full codebase. — [OpenSourceForU](https://www.opensourceforu.com/?p=88743), [Google Cloud model card](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai/gpt-oss-120b) [search-summary]
  - gpt-oss-120b scores 140.0 on Epoch's ECI (vs GPT-5 at 150). — [Epoch ECI CSV](https://epoch.ai/data/eci_scores.csv) [primary]
- **Meta, Llama era**
  - The Llama 4 licence (Apr 2025) requires licensees with more than 700M MAU to request a licence from Meta. — [HF Llama 4 Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original) [search-summary]
  - Meta's FAQ restricts EU-domiciled companies and individuals from the **multimodal** models. — [Llama FAQ](https://www.llama.com/faq/) [search-summary]
  - December 2025 reporting (Bloomberg/CNBC, via eWeek) said Meta's next frontier model, "Avocado", would be closed and API-only. — [eWeek](https://www.eweek.com/news/meta-new-avocado-model/) [secondary]
  - USCC links Meta's shift partly to concerns that Chinese labs were leveraging Llama. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
- **Meta in 2026** (all from [VentureBeat, 15 Oct 2026](https://venturebeat.com/technology/meta-unveils-muse-spark-open-the-new-top-u-s-open-weights-model-and-it-runs-on-two-paired-mac-desktops) [secondary]):
  - **Closed:** Muse Spark (8 Apr 2026), hosted only; Muse Wonder and Wonder Full (12 Oct 2026), API and subscription.
  - **Muse Glimmer** (10 Aug 2026): 30B parameters, Apache 2.0.
  - **Muse Spark Open** (15 Oct 2026): 816B total / 42B active, under a custom "Muse Model License". Model-serving businesses with more than USD 20M revenue need a separate agreement, and products must carry "Built with Muse Spark Open".
  - Meta calls it "the most capable US open-weight model to date", but on Artificial Analysis it trails six Chinese open models.
- **Google:** Gemma 4 (2 Apr 2026) moved to Apache 2.0, replacing the custom Gemma terms. — [Slashdot](https://tech.slashdot.org/story/26/04/02/1735238/google-announces-gemma-4-open-ai-models-switches-to-apache-20-license), [Implicator](https://www.implicator.ai/google-releases-gemma-4-under-apache-2-0-dropping-its-custom-ai-license/) [search-summary]
- **Ai2 OLMo 3** (late 2025) is fully open:
  - Pretraining corpus Dolma 3, about 9.3T tokens, with OLMo 3 trained on about 6T of them.
  - Mid- and post-training data (Dolci), code, checkpoints and evaluation tools. — [Ai2 Dolma 3 blog](https://allenai.org/blog/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64), [The New Stack](https://thenewstack.io/ai2s-olmo-3-pushes-the-envelope-for-open-source-llm-performance/) [search-summary]
- **Mistral**
  - Mistral Large 3 (2 Dec 2025) is an open-weight MoE (675B total / 41B active) under Apache 2.0. — [Mistral announcement](https://mistral.ai/news/mistral-3), [The Register](https://www.theregister.com/2025/12/02/mistral_3/) [search-summary]
  - Mistral Large 4 (6–7 Oct 2026) has an unclear licence and weight status. — [eesel.ai](https://www.eesel.ai/blog/mistral-large-4) [search-summary]
  - On Epoch's ECI, Mistral Large 4 scores 146.9, the best European model. — [Epoch CSV](https://epoch.ai/data/eci_scores.csv) [primary]
- **Other US open-weight releases in 2026:** NVIDIA Nemotron 3 Ultra (Jun 2026, ECI 145.8) and Thinking Machines Inkling / Inkling-Small (Jul 2026, ECI 148.6 / 150.2). — [Epoch CSV](https://epoch.ai/data/eci_scores.csv) [primary]
- **US open models vs Chinese open models**
  - **Artificial Analysis, open-weights view (accessed 2026-10-15)** [primary] — [AA open-source models](https://artificialanalysis.ai/models/open-source):
    - The top five are all Chinese: MiMo-V2.6-Pro 46, GLM-5.3 (Max) 45, Step 5 Preview 44, Kimi K3 (Max) 44, GLM-5.3-Flash 42.
    - The best US open model is Meta's Muse Spark Open at 39.
  - **Epoch ECI:** best US open-weight is Inkling-Small at 150.2 vs Kimi K3 at 157.4. — [Epoch CSV](https://epoch.ai/data/eci_scores.csv) [primary]
- **The ATOM Project** (Nathan Lambert/Interconnects, launched Jul–Aug 2025) argues "America has lost its lead in open models – both in performance and adoption". — [Interconnects](https://www.interconnects.ai/p/atom-project) [search-summary]

### Inferences
- The "US closed / China open" dichotomy now holds mainly **at the frontier**: every US lab's best model is closed. Lower down, both countries ship Apache or MIT weights.
- In 2026 licences converged from both sides:
  - Meta adopted the same "MaaS revenue gate" template as Moonshot, Qwen and StepFun.
  - Google and OpenAI ship Apache 2.0 weights.
- **Fully open (data included)** remains a non-commercial and public-sector niche: Ai2 OLMo (US non-profit), Apertus (Swiss public), OpenEuroLLM (EU, promised). No Chinese lab is in this category.

### Gaps
- I did not open OpenAI's gpt-oss announcement or Ai2's OLMo 3 release post directly. Facts above are consistent across several secondary sources.
- I could not confirm Mistral Large 4's licence or whether its weights are public as of 2026-10-15.
- I could not confirm whether Meta "Avocado" became Muse Spark or Muse Wonder (no source links the names).

---

## Q3. Why China went open: policy, export controls, business strategy

### Takeaway
Three drivers reinforce each other, and the evidence supports all three:
- **State policy** explicitly promotes an open-source AI ecosystem: the 2017 AI plan, the 14th Five-Year Plan, the August 2025 AI+ Opinions and the 15th Five-Year Plan.
- **Compute constraints from US export controls** make open weights a way to offload inference to others and to iterate close to the frontier.
- **Commercial logic** for latecomers: reputation, developer mindshare, cloud pull-through and IPO valuations.

The state promotes openness but does not mandate it. In 2026 Beijing even discussed restricting overseas access to its top models, open-weight ones included.

### Cited Findings
- **State Council "AI+" Opinions** (Guofa [2025] No. 11; formulated 21 Aug 2025, released 26 Aug 2025) [primary] — [CSET translation, 24 Sep 2025](https://cset.georgetown.edu/wp-content/uploads/t0652_AI_plus_opinions_EN.pdf); Chinese original [gov.cn](https://www.gov.cn/zhengce/content/202508/content_7037861.htm)
  - Section (11), "Promote a thriving open-source ecosystem":
    - "Support the development of open-source AI communities, promote the gathering together and openness of models, tools, and datasets".
    - "**encourage universities to include open-source contributions in student course credit certification and faculty achievement recognition**".
    - Develop "internationally influential open-source projects".
  - Section (6), "AI+ Global Cooperation": "push for AI technologies to be open-source and accessible … help Global South countries build up their AI capabilities … bridge the global AI divide."
- **Policy lineage** [primary] — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf):
  - Openness was promoted in the 2017 AI Plan, "carried forward in the 2021 14th Five-Year Plan, the 2025 AI+ Initiative … as well as the draft 15th Five-Year Plan".
  - Local governments in Beijing, Guangdong and Hangzhou funded open-source AI.
  - Chinese open models grew from 32 (2022) to 337 (2025), against US open models growing from 213 to 622 (Epoch data cited by USCC).
  - Premier Li Qiang, summer 2025: "China's innovation is open and open-source".
  - In September 2025 the Cyberspace Administration of China (CAC) released an AI standards framework "with emphasis on risks from open-source models".
- **15th Five-Year Plan (approved 12–13 Mar 2026):** AI is the most-mentioned term, and the plan calls for a "globally open AI open-source ecosystem" alongside a proposed World AI Cooperation Organization. — [Flanders-China Chamber](https://www.flanders-china.be/en/newsletterpublications/15th-five-year-plan-2026-2030-mentions-artificial-intelligence-ai-more-than-50-times), [Strider](https://www.striderintel.com/blog/the-prcs-15th-five-year-plan-inside-the-ai-agenda/) [search-summary; official text not read]
- **Export controls and compute** — [CSIS, Atalan, 2 Jul 2026](https://www.csis.org/analysis/what-know-about-chinese-ai-models) [primary]
  - "U.S. export controls limit access to the best AI chips," and Chinese labs lack hyperscaler inference capacity.
  - "Open-weight releases reduce that burden because third-party providers and local users supply much of the serving compute."
  - USCC adds that the open ecosystem "enables China to innovate close to the frontier despite significant compute constraints". — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
- **Business strategy**
  - "Many Chinese labs use open-weight releases to build adoption, prestige, and developer ecosystems." — [CSIS](https://www.csis.org/analysis/what-know-about-chinese-ai-models) [primary]
  - "By releasing strong research, they build reputation and gain free publicity" (Liu Zhiyuan, Tsinghua); open source is also a route to setting standards. — [MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) [secondary]
  - New entrants gain profile and capital: MiniMax's share price doubled on its first day of trading in Hong Kong (Jan 2026). — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
  - Takshashila's discussion paper (7 Aug 2026) lists five factors:
    1. Distillation and efficiency cost advantages.
    2. Prestige.
    3. Undermining US proprietary revenue models.
    4. State-backed capital.
    5. Pull-through to Chinese cloud.
    - — [Takshashila](https://takshashila.org.in/content/publications/20260807-why-is-china-giving-away-its-ai-models.html) [search-summary]
- **USCC's "two loops" thesis:**
  - Open models speed diffusion into manufacturing and robotics, generating industrial data that "may compound into advantages that proprietary U.S. models cannot easily replicate".
  - Export controls target the "digital loop" (training compute), not this deployment loop. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
- **Limits of the state-driven story**
  - ASPI notes a Chinese policy statement urging authorities to "respect enterprise's independent choices" on intellectual property. Zhipu co-founder Tang Jie frames open and closed as "two legs" serving the ecosystem "while safeguarding national security". — [ASPI](https://www.aspistrategist.org.au/some-chinese-ai-will-go-closed-source-but-not-all/) [secondary]
  - **Reuters, 7 Jul 2026:** the Ministry of Commerce (MOFCOM), with the National Development and Reform Commission (NDRC), held meetings with Alibaba, ByteDance and Z.ai on "potentially restricting overseas access to China's most advanced AI models", covering both closed and open-weight models.
    - A tiered regime was floated in a Supreme People's Court journal roundtable: filing for basic open-source tools, security review for advanced ones, and domestic-only for the most sensitive frontier models.
    - Status as reported: "It was not immediately clear when or even if they would come into force." — [Reuters via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/exclusive-beijing-looking-curbing-overseas-101644780.html) [secondary]; [TIME](https://time.com/article/2026/07/07/china-ai-models-alibaba-bytedance/) [search-summary]

### Inferences
- The most defensible causal account is **"policy-endorsed, compute-constrained, commercially rational"** openness, not "openness as a value".
- The state frames open source as national strategy and soft power (Global South and UN language in the AI+ Opinions). It also keeps the option to restrict exports of its best models, the same instinct the US showed in June 2026 (see Q5).
- For the paper's governance section, AI+ section (11) is a neat hook. A state is proposing to **count open-source contributions in faculty achievement recognition**, a top-down change to what academia counts.

### Gaps
- No Brookings, Carnegie, MERICS or DigiChina analysis was opened. The MERICS piece "China's next five-year bet on AI" and DigiChina's 15th Five-Year Plan forum exist but were not read.
- I did not verify the official 15th Five-Year Plan text on open source.
- Whether the Reuters-reported curbs were adopted after July 2026 is unknown. I found no later reporting.

---

## Q4. Adoption: Hugging Face, OpenRouter, scientists, Global South

### Takeaway
Chinese models dominate **open-model** adoption:
- About 41% of Hugging Face downloads over the past year.
- Qwen is the largest derivative ecosystem.
- 74% of tokens among OpenRouter's top 20 models in the week to 14 Oct 2026.
- The main open-weight base in scientific papers: Qwen accounts for about half of open-weight selections.

But **end-user** AI use remains dominated by US closed products, and DeepSeek's consumer reach is concentrated in China, sanctioned or US-restricted states and Africa.

### Cited Findings
- **Hugging Face, "State of Open Source: Spring 2026"** (17 Mar 2026; Ghosh, Kaffee, Jernite, Solaiman) [primary] — [HF blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
  - Chinese models accounted for "the plurality or 41% of downloads" in the past year, and China surpassed the US in monthly and overall downloads.
  - Qwen has more than 113,000 derivative models (more than 200,000 counting all models tagging Qwen). Alibaba has more derivatives than Google and Meta combined.
  - Baidu went from zero Hub releases (2024) to more than 100 (2025). ByteDance and Tencent each increased releases eight- to nine-fold.
  - **Caveats in the report:**
    - Windows differ across figures.
    - The top 200 models (0.01% of models) account for 49.6% of downloads.
    - CI pipelines inflate small-model counts.
    - About half of downloads come from users with no clear geography.
- **Download crossover timing**
  - USCC, citing ATOM: Chinese models overtook US models in total HF downloads in **August 2025**, and accounted for seven of the top ten most-downloaded models in Nov–Dec 2025. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
  - Interconnects dates the crossover to **July 2025**. — [Interconnects](https://www.interconnects.ai/p/atom-project) [search-summary]
  - By 4 Aug 2025, Qwen derivatives were more than 40% of new HF language-model derivatives vs about 15% for Llama. — [MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) [secondary]
  - CAISI: DeepSeek downloads rose nearly 1,000% from Jan to Sep 2025. — [NIST CAISI](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks) [primary]
- **OpenRouter**
  - The a16z/OpenRouter "100 trillion token" study (report 4 Dec 2025; [arXiv 2601.10088](https://arxiv.org/abs/2601.10088), 15 Jan 2026) [search-summary for figures; abstract primary]:
    - Chinese open-source models rose from about 1.2% of usage (late 2024) to nearly 30% in some weeks, averaging 13.0% over the year.
    - Proprietary models served about 70% of tokens.
    - MIT Technology Review independently reports the "nearly 30% … in some recent weeks" figure.
  - **Live snapshot, OpenRouter weekly top-20 models by tokens (data through 2026-10-14)** [primary] — [openrouter.ai/rankings](https://openrouter.ai/rankings), my computation from embedded page data:
    - Chinese-lab models account for **74.1% of tokens among the top 20**.
    - #1 is DeepSeek V4.1 Flash at 37.4T tokens (26.0%), followed by StepFun Step-5 Preview (13.1%), GLM-5.3-Flash (9.0%), Xiaomi MiMo-V2.6-Flash (8.0%) and Tencent Hy4-preview (5.4%).
    - The top US entries are NVIDIA Nemotron 3 Ultra (5.2%), GPT-6 Luna (4.9%) and Claude Opus 5.5 (3.9%).
    - Caveat: OpenRouter is a price-sensitive developer aggregator and excludes first-party traffic (ChatGPT, Claude.ai, direct APIs). Promotional free tiers can inflate counts.
- **End-user adoption remains US-led**
  - RAND: US models captured 93% of global LLM site visits in Aug 2025 (cited by USCC).
  - Microsoft: AI adoption in China was 16.3% vs 28.3% in the US in H2 2025. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
  - An a16z partner estimated that 80% of US startups use Chinese base models (rough estimate, via USCC). — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
- **Scientists**
  - *Nature*, 23 Jan 2025: DeepSeek-R1 "performs reasoning tasks at the same level as OpenAI's o1 — and is open for researchers to examine". — [Nature d41586-025-00229-6](https://www.nature.com/articles/d41586-025-00229-6) [search-summary]
  - *Nature*, 29 Jan 2025, "Scientists flock to DeepSeek": researchers were testing R1 on mathematics and neuroscience tasks. It "won't answer politically sensitive questions", which Subbarao Kambhampati said "looks more like a clumsy add-on than something baked into system". — [Nature d41586-025-00275-0](https://www.nature.com/articles/d41586-025-00275-0) via [ASU reprint](https://prod-fullcircle.fsewp.asu.edu/external/scientists-flock-to-deepseek-how-theyre-using-the-blockbuster-ai-model) [secondary]
  - **Dunivin, "Who Uses Open-Weight Models? China and the Shifting Geography of AI in Science"** (arXiv preprint, 11 Aug 2026; 21M full-text papers from the Semantic Scholar Open Research Corpus, S2ORC, through Jun 2026) [primary] — [arXiv 2608.11090](https://arxiv.org/abs/2608.11090)
    - In single-model-family papers, GPT-family share fell from 80.9% (2023) to 44.2% (2026), and open-weight use reached 44.0% in 2026.
    - 2026 shares of single-family papers: Qwen 22.0%, Llama 8.6% (down from a 12.0% peak in 2025), DeepSeek 3.0%, Gemma 1.9%, Mistral 0.8%.
    - Chinese models are 60.5% of open-weight use, and Qwen alone 49.9% of open-weight selections.
    - Authors at Chinese institutions have 2.23× the odds of using open weights.
    - Conclusion: "open-weight adoption in science is not a general turn toward open science".
- **Global South**
  - **Microsoft AI Diffusion Report H2 2025** (8 Jan 2026) [primary] — [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/Microsoft-AI-Diffusion-Report-2025-H2.pdf), [blog](https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/)
    - DeepSeek's market share was 89% in China, 56% in Belarus, 49% in Cuba and 43% in Russia.
    - "In Africa in particular, DeepSeek usage is estimated to be 2 to 4× higher than in other regions."
    - The report attributes this to the MIT licence, the free chatbot and Huawei-led promotion, and warns that "open‑source AI can function as a geopolitical instrument".
    - Global North adoption was 24.7% vs 14.1% in the Global South.
  - **AI Singapore's national model** moved from Llama to Qwen: Qwen-SEA-LION-v4 is built on Qwen3-32B (Nov 2025), citing better low-resource-language performance and tokenisation. — [TechNode](https://technode.com/2025/11/25/singapores-national-ai-program-drops-meta-model-and-switches-to-alibabas-qwen/), [SCMP](https://www.scmp.com/tech/big-tech/article/3334098/singapore-picks-alibabas-qwen-drive-regional-language-model-big-win-china-tech) [search-summary]

### Inferences
- For academia specifically, Chinese open weights (above all Qwen) have become the default **instrument** for researchers who fine-tune or run models locally. Even so, GPT-family closed models still appear in more single-family papers.
- Dunivin's data suggest this follows geography and price, not open-science values.
- The Global South story is real but double-edged. Adoption is highest where US services are restricted or unaffordable, and Microsoft itself frames it geopolitically.

### Gaps
- I did not open the full a16z/OpenRouter PDF; the 13.0% average and 1.2%→30% figures come from search summaries corroborated by MIT Technology Review.
- I found no peer-reviewed (as opposed to preprint) study of Chinese-model use by scientists. Dunivin is a single-author preprint.
- I found no reliable country-level data for Latin America or South Asia beyond Microsoft's map.

---

## Q5. Caveats: CAC rules, censorship, security, data handling, and whether open weights move control from corporations to the state

### Takeaway
- **Service-level control.** Chinese generative-AI services are under a registration-and-content regime: the "core socialist values" requirement, security assessment, algorithm filing and mandatory labelling.
- **Censorship is in the weights.** Rigorous studies find it persists even in China-origin foundation models (Pan & Xu, *PNAS Nexus* 2026; NIST CAISI 2025). It can partly be fine-tuned away.
- **Data risk sits with the hosted services, not the downloaded weights.** DeepSeek's app stores data in the PRC and drew bans in many jurisdictions; self-hosted weights avoid that data flow.

Open weights shift **some** control away from any single corporation, to whoever hosts them. But they do not remove PRC state influence over what the model was trained to say, and Beijing is weighing export controls on future models. The US government showed comparable control over US frontier models in June 2026.

### Cited Findings
- **Interim Measures for Generative AI Services** (CAC and six other ministries, Order No. 15; promulgated 10 Jul 2023, effective 15 Aug 2023) [primary] — [CAC text](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)
  - Art. 4(1): providers must "坚持社会主义核心价值观" (uphold core socialist values) and must not generate content inciting subversion of state power.
  - Art. 7: training must use "data and foundation models from lawful sources".
  - Art. 17: services "with public-opinion attributes or social-mobilisation capacity" need a security assessment and **algorithm filing**.
  - **Art. 2 exempts organisations that develop or use the technology without offering services to the public in mainland China.** This matters for downloaded weights used abroad or in non-public research.
- **Filing volume:**
  - 346 services were registered by 31 Mar 2025. — [Xinhua](https://english.news.cn/20250408/290d2e9a29eb4db78309ba3c49561c06/c.html) [search-summary]
  - 868 services (plus 530 applications or functions) by 30 Apr 2026. — [Wedoany](https://en.wedoany.com/shortnews/168577.html) [search-summary]
  - **1,112 by end of Aug 2026** (CAC release dated 14 Sep 2026). — [Tech Policy Press](https://www.techpolicy.press/global-digital-policy-roundup-september-2026/), [Digital Policy Alert](https://digitalpolicyalert.org/event/39871-cyberspace-administration-issued-filing-information-for-generative-ai-services-for-march-to-april-2026) [search-summary]
- **Labelling Measures for AI-Generated Synthetic Content** (CAC, MIIT, MPS, NRTA; issued Mar 2025, effective **1 Sep 2025**), plus the mandatory national standard **GB 45438-2025**, require explicit and implicit (metadata) labels. — [Allen & Gledhill](https://www.allenandgledhill.com/sg/publication/articles/30284/further-regulates-ai-generated-content), [HSF Kramer](https://www.hsfkramer.com/notes/tmt/2025-posts/China-Releases-Laws-to-Mandate-Labelling-of-AIGC) [search-summary]
- **Peer-reviewed censorship evidence:** Pan & Xu, "Political censorship in large language models originating from China", *PNAS Nexus* 5(2): pgag013 (17 Feb 2026). — [PNAS Nexus](https://academic.oup.com/pnasnexus/article/5/2/pgag013/8487339) [search-summary, abstract quoted]
  - Across 145 political questions, China-origin **foundation** models show "substantially higher rates of refusal to respond, shorter responses, and inaccurate responses", "not explained by technological limitations or market preferences".
  - The authors do not claim a causal link to regulation.
- A preprint finds the censorship signal shifting "from refusal to reframing" in newer China-origin vision-language models. — [arXiv 2608.11816](https://arxiv.org/html/2608.11816v1) [search-summary; not peer-reviewed]
- **NIST CAISI evaluation of DeepSeek** (30 Sep 2025; R1, R1-0528, V3.1 vs GPT-5, GPT-5-mini, gpt-oss and Claude Opus 4; 19 benchmarks) [primary] — [NIST](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks)
  - DeepSeek models "echoed four times as many inaccurate and misleading CCP narratives as U.S. reference models".
  - R1-0528 agents were "12 times more likely … to follow malicious instructions" (agent hijacking).
  - Under a common jailbreak, R1-0528 responded to 94% of overtly malicious requests vs 8% for US reference models.
  - On cost, one US reference model was 35% cheaper for similar performance.
  - The evaluation was mandated by the US AI Action Plan, so it comes from an interested government evaluator.
- **NIST CAISI on DeepSeek V4 Pro** (1 May 2026) [primary] — [NIST](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
  - Capabilities "lag behind the frontier by about 8 months", performing similarly to GPT-5.
  - "DeepSeek V4 scores better on DeepSeek's self-reported evaluations than on CAISI evaluations."
  - Examples: ARC-AGI-2 semi-private 46% vs GPT-5.5 at 79%; PortBench 44% vs 78%.
  - V4 is cheaper than GPT-5.4 mini on 5 of 7 benchmarks.
  - The page does not report censorship results.
- **Censorship can be partly removed.** Perplexity's R1-1776 (Feb 2025) post-trained R1 on about 40,000 prompts that had triggered censorship. — [The Decoder](https://the-decoder.com/perplexity-ai-removes-chinese-censorship-from-deepseek-r1/), [eWeek](https://www.eweek.com/news/perplexity-ai-deepseek-r1-post-training/) [search-summary; Perplexity's claims not independently verified]
- **DeepSeek privacy policy** (last updated 10 Feb 2026) [primary] — [DeepSeek privacy policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)
  - It will "directly collect, process and store your Personal Data in People's Republic of China".
  - Data may be shared to comply with "government requests".
  - User inputs are used "to train and improve our technology", with an opt-out.
- **Regulatory actions** (Christakis & Raj, MIAI, 28 Jan 2026) [primary] — [ai-regulation.com](https://ai-regulation.com/deepseek-one-year-later-regulatory-storm-global-surge/)
  - **Italy:** the Garante ordered an immediate processing ban on 30 Jan 2025.
  - **South Korea:** the PIPC inquiry led to suspension of new downloads on 15 Feb 2025; service resumed 28 Apr 2025 after corrective recommendations.
  - **Germany:** Berlin's data-protection authority sent Digital Services Act (DSA) Art. 16 notices to Apple and Google on 27 Jun 2025. They did not act.
  - **Government-device bans:** Australia, Taiwan, the Netherlands, the Czech Republic, Belgium, Japanese ministries, Canada, the US Navy, NASA, the House and multiple US states, among others.
- **Dependency and control analyses**
  - USCC: reliance on Chinese base models creates "long-term dependency on infrastructure with embedded censorship and potential security vulnerabilities". — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]
  - CSIS: open-weight diffusion "creates de facto technical dependence on Chinese model families, even when the models are hosted outside China". Third-party hosting also means the developer "cannot see the prompts, logs" (a data-flow point). — [CSIS](https://www.csis.org/analysis/what-know-about-chinese-ai-models) [primary]
  - Licence texts themselves embed state-compatible clauses, for example GLM-5.3's "security review" for the largest MaaS operators and "must comply with applicable laws and regulations". — [GLM-5.3 LICENSE](https://huggingface.co/zai-org/GLM-5.3/raw/main/LICENSE) [primary]
  - Reuters (Jul 2026) reported that Beijing discussed curbs on overseas access, open-weight models included. — [Reuters via Yahoo](https://finance.yahoo.com/technology/ai/articles/exclusive-beijing-looking-curbing-overseas-101644780.html) [secondary]
- **US-side state control (for symmetry)**
  - On **12 Jun 2026**, the US government, "citing national security authorities", directed Anthropic to "suspend all access to Fable 5 and Mythos 5 by any foreign national". Anthropic disabled both models for **all** users worldwide. — [Anthropic statement](https://www.anthropic.com/news/fable-mythos-access) [primary]; [Al Jazeera](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals) [secondary]
  - Commerce withdrew the requirement on 30 Jun 2026, and Fable 5 returned globally on 1 Jul 2026. — [VentureBeat](https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it) [secondary]
  - Mythos 5 was restored only for "a set of US organizations". Commerce "reserved the right to … re-impose license requirements". — [VentureBeat](https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it) [secondary]

### Inferences
- Open weights do **reduce corporate gatekeeping**. Anyone can host, fine-tune, de-censor (partly) and keep data local, as shown by the DeepSeek-app vs self-hosted-weights distinction and R1-1776.
- They **do not neutralise state influence over content**. Value alignment is trained in under CAC rules, and pretraining-data opacity prevents auditing it.
- They also do not guarantee continued access to *future* models. Beijing is weighing export tiers, and licences are tightening.
- The "corporate (US) vs state (China)" contrast is too clean. In June 2026 a US export-control directive switched off a US frontier model for every foreign national, and the most capable US model (Mythos 5) remains restricted to selected US organisations.

### Gaps
- I did not obtain the full CAISI 2025 PDF (methodology of the CCP-narrative dataset).
- No peer-reviewed study compares censorship in self-hosted weights vs Chinese hosted apps. Wired (26 Feb 2026, "How Chinese AI Chatbots Censor Themselves") is cited by USCC but was not read.
- I did not verify whether the Italian ban still stands in Oct 2026.
- I did not read the text of the CAC's September 2025 AI Safety Governance Framework 2.0; only USCC's characterisation.

---

## Q6. Chinese research-system governance: the 2020 anti-"SCI-only" reform, its effects, and rules on AI in research

### Takeaway
China is a rare case of a state changing academic metric incentives **top-down**:
- **2018:** a clean-up of the "four onlys" (papers, titles, diplomas, awards).
- **February 2020:**
  - The Ministry of Education and Ministry of Science and Technology (MOE/MOST) banned cash rewards tied directly to SCI metrics and stopped using SCI as the direct basis for hiring and degrees.
  - MOST also introduced "representative works" with at least one third in domestic journals.
- **March 2026:** the CAS journal ranking table was terminated.

Evidence of effects is weak or mixed:
- Early studies called the reform largely symbolic, and qualitative work finds discretion shifted power to administrators and senior scholars.
- SCI output kept rising, to about one third of the world total in 2023.

On AI, the state moved early with soft-law rules: the 2023 MOST guidelines and draft Degree Law language on "AI ghost-writing". Universities improvised AIGC-detection thresholds without a national standard.

### Cited Findings
- **2018 "clean-up of the four onlys"** (唯论文、唯职称、唯学历、唯奖项): a special action by MOST, MOE, MHRSS, CAS and CAE. MOE later added "唯帽子" (talent titles), making five. — [Science & Technology Daily (大学生科技报), 27 Dec 2018](https://digitalpaper.stdaily.com/http_www.kjrb.com/dxsb/images/2018-12/27/06/dxsb2018122706.pdf) [search-summary]
- **MOE/MOST, 《关于规范高等学校SCI论文相关指标使用 树立正确评价导向的若干意见》** (Jiaokeji [2020] No. 2, dated 18 Feb 2020) [primary] — [gov.cn](https://www.gov.cn/zhengce/zhengceku/2020-03/03/content_5486229.htm)
  - Art. 8: "要取消直接依据SCI论文相关指标对个人和院系的奖励" (abolish rewards to individuals and departments based directly on SCI indicators).
  - Art. 7: SCI indicators are not to be the "direct basis" for judgments, nor a precondition for hiring.
  - Art. 9: SCI counts or impact factors should not be preconditions for graduation or degrees.
  - Art. 10: no SCI or ESI rankings to be published or cited.
- **MOST/MOF 《关于破除科技评价中"唯论文"不良导向的若干措施（试行）》** (Guokefajian [2020] No. 37, 17 Feb 2020):
  - "Representative works" system: "国内科技期刊论文原则上应不少于1/3" (at least one third of papers in domestic journals, in principle).
  - The number and impact factor of works are not to be used as quantitative indicators.
  - Effects were to be evaluated after one year. — [BNU PDF of the measures](https://geo.bnu.edu.cn/docs/20220525181418029786.pdf) [search-summary]
- **Early effect evidence:** a study by Fei Shu and colleagues (Hangzhou Dianzi University) in *Minerva* found:
  - The documents "appear more like a communication exercise to appease public anger".
  - Sixteen provincial S&T departments echoed them without offering "any alternatives to the SCI". — [Times Higher Education, 23 May 2022](https://www.timeshighereducation.com/news/chinas-promised-research-reform-little-more-pr-exercise) [primary]
  - Likely paper: [Minerva, doi 10.1007/s11024-022-09468-7](https://link.springer.com/article/10.1007/s11024-022-09468-7) [title from search; full text not read]
- **Qualitative effects:** "Reconfiguring power: a field analysis of China's research evaluation reform", *Higher Education* (online 23 Jun 2025) [search-summary of abstract] — [Springer](https://link.springer.com/article/10.1007/s10734-025-01480-6)
  - Broader criteria increased administrative and academic discretion, strengthening institutional leaders, established scholars and personal connections.
  - Early-career scholars were disproportionately disadvantaged.
  - There are concerns about domestic-journal capacity and "de-internationalisation".
- **Output did not fall.** Chinese authors published 728,700 SCI papers in 2023, about 33% of the global total. — [gov.cn English (Xinhua), Dec 2024](https://english.www.gov.cn/english.www.gov.cn/news/202412/20/content_WS676548edc6d0868f4e8ee293.html) [search-summary]
- **2026 escalation.** The CAS National Science Library announced on 27 Mar 2026: "Starting from 2026, we will no longer update or release the Journal Classification Table". This is "a permanent termination", aimed at weakening "journal centrism" so as to "shift the focus of evaluation to assessing the quality, innovation and social value of individual research outputs". — [DORA blog, Fang Xu (CAS), 20 May 2026](https://sfdora.org/2026/05/20/cas-journal-list/) [primary]
- **MOST Guidelines for Responsible Research Conduct (2023)** (issued 21 Dec 2023 by MOST's supervision department) [primary for quotes] — [gov.cn English, 6 Jan 2024](https://english.www.gov.cn/news/202401/06/content_WS6598c927c6d0868f4e8e2d24.html); [SCMP](https://www.scmp.com/news/china/science/article/3247420/china-unveils-new-artificial-intelligence-guidelines-scientists-and-bans-use-funding-applications) [search-summary]
  - "generative AI should not be used to directly generate research application materials".
  - AI "should not be listed as a co-author".
  - AI-generated content "should be clearly labeled and the generation process should be explained".
  - "Unverified references generated by AI should not be used directly".
  - Reviewers must obtain "prior consent … from the organizers of the review activity" before using generative AI.
- **Degree Law** (adopted 26 Apr 2024, effective 1 Jan 2025). — [JunHe](https://www.junhe.com/law-reviews/2428) [search-summary]
  - The Aug 2023 draft explicitly listed "人工智能代写" (AI ghost-writing) alongside plagiarism and fabrication as grounds for revoking degrees. — [China News, 29 Aug 2023](https://www.chinanews.com.cn/cj/2023/08-29/10068699.shtml) [search-summary]
- **Thesis AIGC detection** (CCTV via ScienceNet, 22 May 2026) [primary] — [ScienceNet](https://news.sciencenet.cn/htmlnews/2026/5/565116.shtm)
  - Sichuan University caps AI-generated content at 20% (humanities) and 15% (STEM/medicine).
  - Guangxi Normal University, Hebei University of Engineering and Nanjing University of Aeronautics and Astronautics cap it at 40%.
  - Exceeding the cap can bar a thesis from blind review and defence.
  - Students report false positives: 56% overall, and 97% on a self-written plan.
  - Experts call for national technical standards for detectors, which implies none exists.
- **Other venues**
  - Journals of the Chinese Academy of Social Sciences (May 2025) bar external reviewers from using generative AI to review or uploading manuscripts to public AI tools. — [CSSN](https://cssn.cn/ggzp/202505/t20250515_5873974.shtml) [search-summary]
  - NSFC will "slim down" General Program and Young Scientist (C) application outlines from 2026 to counter templated ("套路化") proposals. — [Xinhua, 30 Dec 2025](https://www.news.cn/fortune/20251230/2c7e7a4de64d4c959160d164e11679b5/c.html) [search-summary]

### Inferences
- This is the strongest real-world precedent for the paper's governance section: a state **deliberately de-weighting counts** (SCI, impact factor, journal tiers) by decree, and in 2026 abolishing a dominant national journal ranking.
- The evidence warns that removing metrics without capacity for qualitative judgment shifts power to whoever exercises the discretion.
- Since generative AI makes counted outputs cheap, the Chinese case shows both the possibility of top-down de-metrification and its failure mode.
- On AI rules, China is early and specific (no AI-written grant applications; labelling) but enforcement is decentralised and technologically weak (AIGC detectors).

### Gaps
- No causal or bibliometric study isolating the 2020 reform's effect on publication behaviour was found.
- The final Degree Law text was not checked. **I could not confirm that the explicit "人工智能代写" wording survived into the adopted law**, so do not cite it as law without checking npc.gov.cn.
- No specific NSFC rule on AI-generated proposals or reviewer AI use was found. Search results contained only templates and the 2026 "slimming" action.
- I did not verify the exact date of the CPC/State Council 2020 "Overall Plan for Deepening Education Evaluation Reform in the New Era" (the "five onlys" document).
- Reports of a CAS integrity reminder on AI (Sep 2024) and a CISTI–publishers AIGC guideline (26 Sep 2024) appeared only in search digests and were not verified.

---

## Q7. Frontier capability as of mid-October 2026: neutral trackers, who leads, disagreements, turnover

### Takeaway
No tracker supports "one lab ahead by far":
- Four US firms (Anthropic, OpenAI, Google, Meta) cluster at the top, and **which one is #1 depends on the tracker**:
  - **Epoch ECI and Artificial Analysis:** Anthropic's Claude Opus 5.5 is #1, but on ECI it is statistically tied with OpenAI's GPT-6 models.
  - **Arena (human preference):** Google's Gemini 4 Argon is #1.
  - **METR:** its newest measurements favour Anthropic but stopped updating in Sep 2026.
- The best Chinese and best open-weight models trail by about **4–9 months** (Epoch, CAISI). That is about 9 ECI points, or about 2.4–2.8% on Arena.
- The ECI #1 changed hands three times in September 2026 alone.

### Cited Findings
**Epoch AI (ECI scores CSV, updated 2026-10-15)** [primary] — [epoch.ai/benchmarks/eci](https://epoch.ai/benchmarks/eci), [CSV](https://epoch.ai/data/eci_scores.csv). Scores are listed as model: score [90% CI] (release date).
- **Top six:**
  - Claude Opus 5.5: **166.82** [163.54–170.99] (2026-09-22)
  - GPT-6 Astra: **166.41** [163.35–171.23] (2026-09-03)
  - GPT-6.1 Sol: 166.32 [163.17–170.82]
  - Claude Fable 5.1: 164.65
  - Gemini 4 Argon: 164.56 (limited access)
  - Claude Sonnet 5.5: 164.45
  - The confidence intervals of the top six overlap.
- **Best by country or lab:**
  - Best Chinese: Kimi K3 **157.42** [155.10–160.11] (open weights), then Qwen 3.8 Max 156.88 (API), GLM-5.3 155.91 and DeepSeek V4.1 Flash 155.57 (open).
  - Best Meta: Muse Spark 1.3, 156.76. Best xAI: Grok 4.6, 156.31.
  - Best European: Mistral Large 4, 146.90.
- **My computations from the CSV:**
  - **US–China frontier gap: 9.4 ECI points**, not shrinking. It was 4.7 in 2024Q2, 5.0–6.1 through 2025Q1–Q3, 9.9–11.0 in 2025Q4–2026Q1, 8.3 in 2026Q2 and 9.4 in 2026Q3.
  - Kimi K3's score was first exceeded by a US model about 4.4 months earlier (GPT-5.4 Pro, 2026-03-05). DeepSeek V4.1 Flash's score was matched about 9 months earlier (GPT-5.2 Pro, 2025-12-11).
  - Mistral Large 4 ≈ o3-pro (Jun 2025), a lag of about 16 months.
- **ECI record turnover (my computation):** from 31 Mar 2025 to 15 Oct 2026 the record was held for about 415 days by OpenAI, 109 by Anthropic and 39 by Google. In Sep 2026 it passed from Claude Fable 5.1 (1 Sep) to GPT-6 Astra (3 Sep) to Claude Opus 5.5 (22 Sep), and the current margin is 0.41 points.
- **Epoch Data Insights:**
  - "Since 2023, every model at the frontier of AI capabilities, as measured by the Epoch Capabilities Index, has been developed in the United States". Chinese models lag "an average of seven months, with a minimum gap of four months and a maximum gap of 14". — [Epoch, 2 Jan 2026](https://epoch.ai/data-insights/us-vs-china-eci) [primary]
  - "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months … The average ECI gap was 8 points". — [Epoch, 29 May 2026](https://epoch.ai/data-insights/open-closed-eci-gap) [primary]
  - Epoch also warns that open-weight models "may optimize more aggressively for benchmarks". — [ECI page](https://epoch.ai/benchmarks/eci) [primary]
- **Critique:** the Mercatus/McNair Center argues the US–China gap is "very uncertain", with a best guess of 3–9 months depending on model and benchmark choice. — [McNair Center](https://mcnair.center/china/) [search-summary]

**Arena (formerly LMArena), human preference.** Official `lmarena-ai/leaderboard-dataset`, text board published **2026-10-13** [primary] — [HF dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset). The arena.ai page itself returned HTTP 403 to automated access.
- **Raw "overall" view:**
  - #1 gemini-4-argon-high **1533.2** [1524.4–1542.0] (4,903 votes); #2 claude-opus-5.5-high **1515.5** [1508.0–1523.1]; #3 claude-fable-5.1-max 1509.9; #4 claude-opus-5-max 1507.2; #5 Meta muse-wonder-max 1503.9.
  - #1's interval does not overlap #2's.
  - The top 20 includes Anthropic 9, Google 6, Meta 3, Xiaomi 1 and Alibaba 1.
  - Best OpenAI is #28 (gpt-5.5-high, 1471.4).
  - Best Chinese and best open model: Xiaomi mimo-v2.6-pro (MIT), #11 at 1490.3, 2.8% below #1.
- **Style-controlled "overall" view:**
  - #1 gemini-4-argon-high 1524.8 [1515.9–1533.6]; #2 muse-wonder-max (Meta) 1512.7 [1499.4–1525.9]; #3 claude-opus-5.5-high 1508.1 [1500.5–1515.6].
  - Best OpenAI: gpt-5.6-sol-xhigh, #21. Best Chinese and best open: kimi-k3-max, #17 at 1488.1, 2.4% below #1.
  - The top 20 includes Anthropic 9, Google 5, Meta 5 and Moonshot 1.
- **Turnover:** a Manifold market description (2 Oct 2026 board) also shows Gemini 4 Argon #1. Third-party pages put Claude Fable 5 at #1 in August 2026. — [Manifold](https://manifold.markets/Terminator2/which-company-will-have-the-1-model) [secondary]

**Artificial Analysis Intelligence Index** (v4.3.x; accessed 2026-10-15) [primary] — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models)
- Overall:
  - Claude Opus 5.5 (max) **58**.
  - Claude Sonnet 5.5 (max) 56, Claude Opus 5.5 (xhigh) 56, Meta Muse Wonder Full (max) 56.
  - Claude Fable 5.1 (max) 53, GPT-6 Astra (max) 53, Gemini 4 Argon (high) 53.
- **Open weights:** MiMo-V2.6-Pro 46 (Xiaomi) and GLM-5.3 (Max) 45 lead, against a proprietary best of 58, a 12-point gap. — [AA open-source models](https://artificialanalysis.ai/models/open-source) [primary]
- Caveat: AA re-baselines across index versions. AA's own post at the Kimi K3 weight release called it "the leading open weights model at 57", while the current index lists Kimi K3 (Max) at 44. — [AA on X](https://x.com/ArtificialAnlys/status/2081821449745236270) [search-summary]

**METR time horizons** (Time Horizon 1.1 data; page last updated 2026-09-08 and "no longer actively updated") [primary] — [METR](https://metr.org/time-horizons/), [data YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- 50%-success time horizons:
  - Claude Mythos Preview (early, Apr 2026): about **1,045 min (≈17.4 h)**, CI 509–3,304 min.
  - Claude Opus 4.6: about 719 min (≈12 h), CI 317–3,634.
  - Gemini 3.1 Pro: about 384 min. GPT-5.2: 352 min. GPT-5.3-Codex: 350 min. GPT-5.4: 342 min.
- METR: "Measurements above 16 hrs are unreliable with our current task suite."
- Doubling time since 2023 is about 129 days (CI 104–158).
- **No GPT-6, Gemini 4, Claude Opus 5.5 or 2026 Chinese model has been measured.**
- Chinese models on the older v1.0 suite: DeepSeek-V3 19.8 min, R1 27.9 min, R1-0528 32.8 min, Kimi K2 Thinking 57.6 min (Nov 2025), vs 162–247 min for contemporaneous GPT-5.1-Codex-Max and Claude Opus 4.5. — [data YAML v1.0](https://metr.org/assets/benchmark_results_1_0.yaml) [primary]

**Stanford AI Index**
- **2026 edition** (data to Mar 2026) [primary] — [Technical performance chapter](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)
  - "The U.S.-China AI model performance gap has effectively closed". US and Chinese models "have traded places at the top … multiple times since early 2025".
  - As of Mar 2026 the top US model leads by 2.7% on Arena (1,503 vs 1,464).
  - "Top model performance is converging, with 4 companies now clustered within 25 Elo points": Anthropic 1,503, xAI 1,495, Google 1,494, OpenAI 1,481, then Alibaba 1,449 and DeepSeek 1,424.
  - "the top closed model leads the top open model by 3.3%, up from 0.5% in August 2024."
  - Caveat: "Arena leaderboard standing may partly reflect adaptation to the platform rather than general capability."
  - Industry produced over 90% of notable frontier models in 2025.
- **2025 edition** [primary] — [AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)
  - US institutions produced 40 notable models in 2024, vs 15 for China and 3 for Europe.
  - US–China gaps on MMLU and HumanEval "shrank from double digits in 2023 to near parity in 2024".
  - The open–closed gap fell "from 8% to just 1.7%" (Arena, Jan 2024 → Feb 2025).
  - Top-vs-10th gap fell from 11.9% to 5.4%, and the top two were separated by 0.7%.

**Government evaluator:** CAISI estimated DeepSeek V4 at about 8 months behind the frontier, with self-reported scores higher than independent ones. — [NIST, 1 May 2026](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) [primary]

### Inferences
- **"Claude is the most advanced model by far" is not supported by any third-party tracker as of 2026-10-15:**
  - Anthropic's Claude Opus 5.5 is #1 on Epoch ECI, but by 0.4 points with overlapping CIs against OpenAI.
  - It is #1 on AA, by 2 points over a Meta model and 5 over OpenAI and Google.
  - Google, not Anthropic, is #1 on Arena, and the Arena lead is statistically distinguishable in the raw view.
  - METR's newest data (Anthropic models best) is stale and has very wide CIs.
  - A defensible claim: "Anthropic's models are consistently among the top few, and lead on some capability indices".
- **Trackers disagree on the size of the US–China and open–closed gaps:**
  - **Human-preference Arena** shows them as small: about 2.4–3.3%, "effectively closed" (AI Index).
  - **Capability indices and government tests** show them as material: about 9 ECI points or 4–9 months (Epoch, CAISI), and 12 AA points.
  - Both can be true. Arena compresses differences on conversational quality, while agentic and hard-reasoning benchmarks separate models more.
- Rankings are **volatile on a weeks scale** (the September 2026 ECI record changed hands three times), so any "who leads" sentence in a paper should be dated and hedged.
- On capability, the Chinese open frontier (Kimi K3, DeepSeek V4.x, GLM-5.3, MiMo) roughly matches the US closed frontier of about 4–9 months earlier.

### Gaps
- Arena's website blocked automated access (HTTP 403); I relied on Arena's official HF dataset, which matches the secondary snapshot.
- METR has no measurements of the current (Sep–Oct 2026) frontier, and its page is no longer actively updated.
- I did not access AA's historical index series, so AA turnover is not quantified.
- The Mercatus/McNair critique was seen only via search summary.
- Model names in the AI Index 2026 Arena comparison (Claude Opus 4.6 vs ByteDance Dola-Seed-2.0-Preview) come from secondary coverage, not the report page.

---

## Q8. Other poles (briefly): EU AI Factories and Gigafactories, OpenEuroLLM, "CERN for AI" / RAISE, Swiss Apertus

### Takeaway
Europe's public "third way" is fully open and science-oriented but small and slow:
- AI Gigafactory awards are only due in early 2027.
- RAISE, the "CERN for AI" pilot, is funded at about EUR 140M.
- OpenEuroLLM has not yet shipped a flagship.
- Apertus is the only shipped, fully open (data-transparent) national model.

Europe's best model (Mistral Large 4) trails the frontier by about 20 ECI points, roughly 16 months.

### Cited Findings
- **AI Gigafactories** [primary for the call] — [EuroHPC JU, 30 Jul 2026](https://www.eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en), [call page](https://www.eurohpc-ju.europa.eu/call-tenders-selection-artificial-intelligence-gigafactory-consortia-and-establishment-ai_en)
  - Council Regulation (EU) 2026/150 (16 Jan 2026) entrusted deployment to EuroHPC [search-summary].
  - The call opened 30 Jul 2026 with a deadline of **12 Nov 2026**, for "up to seven" gigafactories. Awards are expected in early 2027, with operation within 18 months of signature.
  - The headline is about EUR 30bn in EU and national co-funding. — [IEU Monitoring](https://ieu-monitoring.com/editorial/eu-launches-e30bn-ai-gigafactories-drive-to-close-europes-computing-gap/1246855) [search-summary]
- **RAISE (Resource for AI Science in Europe):** pilot launched 3 Nov 2025 under the Apply AI and AI-in-Science strategies, with EUR 33M (WP25) and EUR 107M (WP26–27). Observers call it "simply too small and too slow". — [European Commission RAISE page](https://research-and-innovation.ec.europa.eu/strategy/strategy-research-and-innovation/our-digital-future/european-ai-science-strategy/raise-resource-ai-science-europe_en) [search-summary]
- **OpenEuroLLM** — [babl.ai](https://babl.ai/?p=7029), [InfoQ](https://www.infoq.com/news/2025/02/open-euro-llm) [search-summary]
  - Started 1 Feb 2025 with 20 partners, coordinated by Charles University and co-led by AMD Silo AI.
  - Budget EUR 37.4M (EUR 20.6M from the Digital Europe Programme); first project with the EU's STEP seal.
  - Promises fully open models including data.
  - Release timing is unclear: sources conflict on whether 9B checkpoints appeared in Aug 2026.
- **Apertus** (EPFL, ETH Zurich and the Swiss National Supercomputing Centre CSCS; 2 Sep 2025): 8B and 70B models trained on 15T tokens in more than 1,000 languages (about 40% non-English), with weights, code and transparent, reproducible training data. — [EPFL AI Center](https://ai.epfl.ch/a-language-model-built-for-the-public-good/), [Wikipedia: Apertus](https://en.wikipedia.org/wiki/Apertus_(LLM)) [search-summary]
- **Capability position:** Mistral Large 4 scores 146.9 ECI vs a frontier of 166.8. — [Epoch CSV](https://epoch.ai/data/eci_scores.csv) [primary]

### Inferences
- The EU and Swiss initiatives embody the "public knowledge infrastructure" alternative the paper may want, more than Chinese labs do: open data, public compute, science missions. But they operate one or two capability tiers below the frontier.

### Gaps
- I did not verify the Feb 2025 InvestAI figures (EUR 200bn total, EUR 20bn for gigafactories); the Commission press page did not render.
- I did not check the status of the 19 existing "AI Factories".
- Whether RAISE's "pledging initiative" (Dublin, 15 Oct 2026) took place is not confirmed.

---

## Q9. Testing the claim "China is betting on very efficient models that are not yet as powerful but consume much less"

### Takeaway
**Partly right, but it needs reframing.**
- **"Very efficient":** true for training compute and architecture. Chinese labs reach about 4–9 months behind the frontier with roughly 1/30 to 1/50 of the compute of the largest US training runs. They pioneered or popularised fine-grained sparse MoE (3–5% of parameters active per token), multi-head latent attention (MLA), FP8 training at scale, and sparse, linear and hybrid attention.
- **"Not yet as powerful":** accurate on capability indices (about 9 ECI points, or 4–9 months; Q7). Less so on human-preference rankings (2.4–2.8%).
- **"Consume much less" is not established:**
  - Per-token API prices are lower for many Chinese models. But per-task cost depends on how many tokens a model emits, and in Oct 2026 several Chinese flagships cost *more* per Artificial Analysis task than US "small" models at the same score.
  - The best-known energy-per-query study estimates DeepSeek-R1 on DeepSeek's own servers among the *most* energy-intensive models per query, mainly because of hosting hardware and data centres.
  - Chinese frontier models grew to 1–2.8 trillion total parameters in 2026.
  - Aggregate demand rises with efficiency (the Jevons paradox), and China is building out compute too.
- **Efficiency is not uniquely Chinese.** US labs also ship sparse MoE and cheap fast tiers that match the best Chinese models on ECI. The difference is one of emphasis, of necessity under export controls, and above all of **openness**: Chinese labs publish efficient *weights* that others can self-host.

### Cited Findings
**Architecture: sparse MoE and attention efficiency** (HF model cards, accessed 2026-10-15) [primary unless noted]:
- **DeepSeek**
  - **DeepSeek-V3:** "671B total parameters with 37B activated for each token … adopts Multi-head Latent Attention (MLA) and DeepSeekMoE". "we design an FP8 mixed precision training framework and, for the first time, validate the feasibility and effectiveness of FP8 training on an extremely large-scale model." — [HF DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [arXiv 2412.19437](https://arxiv.org/abs/2412.19437)
  - **DeepSeek-V3.2:** "DeepSeek Sparse Attention (DSA) … substantially reduces computational complexity while preserving model performance, specifically optimized for long-context scenarios." — [HF DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)
  - **DeepSeek-V4:** Pro is 1.6T total / 49B activated; Flash is 284B / 13B, with FP4+FP8 mixed weights. Hybrid Compressed Sparse plus Heavily Compressed Attention means that at 1M-token context, "DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2". It uses the Muon optimiser and more than 32T training tokens. — [HF DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- **Moonshot Kimi**
  - **Kimi K2:** 1T total / 32B activated, trained with the Muon optimiser. — [HF Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
  - **Kimi K3:** 2.8T total / **104B activated**, with 69 "KDA" plus 24 gated-MLA attention layers, and "MXFP4 weights / MXFP8 activations (quantization-aware training)". — [HF Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)
- **Alibaba Qwen:** Qwen3-235B-A22B (2025) → Qwen3.5-397B-A17B (Feb 2026) → **Qwen3.8-2.4T-A95B** (Aug 2026). Qwen3.8 uses hybrid "Gated DeltaNet" linear attention plus gated attention, with 512 experts (10 routed + 1 shared) and multi-token prediction. — [HF Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- **Zhipu GLM-4.5:** 355B total / 32B active; GLM-4.5-Air 106B / 12B. FP8 inference needs 8×H100 or 4×H200 (GLM-4.5) and 2×H100 or 1×H200 (Air). — [HF GLM-4.5](https://huggingface.co/zai-org/GLM-4.5)
- **MiniMax**
  - **MiniMax-M1:** 456B total / 45.9B activated, a "hybrid Mixture-of-Experts (MoE) architecture combined with a lightning attention mechanism … compared to DeepSeek R1, M1 consumes 25% of the FLOPs at a generation length of 100K tokens" (vendor claim). — [HF MiniMax-M1-80k](https://huggingface.co/MiniMaxAI/MiniMax-M1-80k)
  - **MiniMax-M3:** ~428B / ~23B activated. Its "MiniMax Sparse Attention … delivers 9× prefill and 15× decode speedups compared to M2 at 1M context, reducing per-token compute to 1/20" (vendor claim). — [HF MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)
- **Xiaomi MiMo-V2.6-Pro:** 1.02T total / 42B activated. — [HF MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- **US open MoEs for comparison**
  - **gpt-oss-120b:** 117B total / 5.1B active. "post-trained with MXFP4 quantization … making gpt-oss-120b run on a single 80GB GPU … and the gpt-oss-20b model run within 16GB of memory." gpt-oss-20b is 21B / 3.6B. — [HF gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)
  - **Llama 4:** Maverick is about 401.6B total (safetensors count) with 17B active and 128 experts. Scout is about 108.6B with 17B active and 16 experts. — [HF Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) (parameter counts from the HF API; README gated)
  - **Meta Muse Spark Open:** 816B / 42B active. — [VentureBeat](https://venturebeat.com/technology/meta-unveils-muse-spark-open-the-new-top-u-s-open-weights-model-and-it-runs-on-two-paired-mac-desktops) [secondary]
- **Active/total ratios (my computation from the figures above).** Chinese and US sparse MoEs sit in the **same range of about 3–9%**:

  | Origin | Model | Active / total |
  |---|---|---|
  | China | DeepSeek-V3 | 5.5% |
  | China | DeepSeek-V4-Pro | 3.1% |
  | China | DeepSeek-V4-Flash | 4.6% |
  | China | Kimi K2 | 3.2% |
  | China | Kimi K3 | 3.7% |
  | China | Qwen3.8 | 4.0% |
  | China | GLM-4.5 | 9.0% |
  | China | MiniMax-M3 | 5.4% |
  | China | MiMo-V2.6-Pro | 4.1% |
  | US | gpt-oss-120b | 4.4% |
  | US | Llama 4 Maverick | 4.2% |
  | US | Muse Spark Open | 5.1% |
- **USCC's assessment:**
  - DeepSeek "did not introduce the mixture-of-experts (MOE) architecture" but "popularized the use of large-scale MOE architectures in open frontier models". "Both MOE and chain-of-thought are now standard for leading frontier models".
  - Chinese innovation reflects "a vibrant research and development (R&D) ecosystem but also necessity, as compute constraints drive experimentation with alternatives to scaling". — [USCC, 23 Mar 2026](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]

**Training compute and cost:**
- **DeepSeek-V3 technical report** [primary] — [arXiv 2412.19437 (HTML)](https://arxiv.org/html/2412.19437)
  - GPU hours: pre-training 2,664K, context extension 119K, post-training 5K, for a total of **2,788K H800 GPU-hours**.
  - "Assuming the rental price of the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M."
  - **Caveat in the report itself:** "Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments on architectures, algorithms, or data."
  - Trained on "a cluster equipped with 2048 NVIDIA H800 GPUs".
  - The report notes H800 limits, for example that "the accumulation precision of FP8 GEMM on NVIDIA H800 GPUs is limited to retaining around 14 bits".
- **External estimate:** SemiAnalysis estimates about 50,000 Hopper GPUs, "total server CapEx for DeepSeek is ~$1.6B", plus about USD 944M in operating costs. The USD 6M is "just the GPU cost of the pre-training run". — [SemiAnalysis, 31 Jan 2025](https://newsletter.semianalysis.com/p/deepseek-debates) [primary]
- **R1 reinforcement learning:** about USD 294K (512 H800s, ~80 h) on top of the base model, per the *Nature* supplementary material. — [Scientific American](https://www.scientificamerican.com/article/secrets-of-chinese-ai-model-deepseek-revealed-in-landmark-paper) [search-summary]
- **Epoch AI model database** (all_ai_models.csv, downloaded 2026-10-15; my computations) [primary dataset] — [Epoch data](https://epoch.ai/data/all_ai_models.csv)
  - DeepSeek-V3: 3.3×10^24 FLOP (2.788M H800-hours; Epoch cost estimate USD 5.39M in 2023 dollars).
  - **Largest Chinese training runs:** Kimi K3 2.0×10^25 (confidence "Speculative"), Qwen3-Max 1.5×10^25 ("Speculative"), DeepSeek-V4-Pro 9.7×10^24 ("Likely"). GLM-5 is 6.8×10^24, with training hardware recorded as **Huawei Ascend 910C** ("Likely").
  - **Largest US runs:** GPT-6 Astra 9.4×10^26 ("Likely", GB200), Grok 4 5×10^26 ("Speculative"), GPT-4.5 3.8×10^26.
  - **Ratio of largest US to largest Chinese run: about 33× in 2025 and about 47× in 2026.** Many US frontier models have undisclosed compute (e.g., Claude, Gemini).
  - gpt-oss-120b, at 4.9×10^24, is at DeepSeek-V3 scale.
- USCC Table 1 (2025) likewise compares Grok 4 at 5×10^26 FLOP with Qwen3-Max at 1.5×10^25. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) [primary]

**API prices** (OpenRouter models API, USD per 1M input/output tokens, accessed 2026-10-15) [primary] — [OpenRouter API](https://openrouter.ai/api/v1/models). Prices vary by provider.

| Group | Model | Input | Output |
|---|---|---|---|
| US frontier | Claude Opus 5.5 | 4 | 20 |
| US frontier | Claude Fable 5.1 | 10 | 50 |
| US frontier | GPT-6 Astra | 10 | 50 |
| US frontier | GPT-6.1 Sol | 2 | 10 |
| US frontier | Gemini 4 Argon | 2 | 10 |
| US frontier | Meta Muse Wonder | 4 | 20 |
| Chinese | DeepSeek V4.1 Flash | 0.15 | 0.60 |
| Chinese | DeepSeek V4 Pro | 0.36 | 0.72 |
| Chinese | MiMo-V2.6-Pro | 0.43 | 0.87 |
| Chinese | MiniMax-M3 | 0.30 | 1.20 |
| Chinese | GLM-5.3 | 0.08 | 4.80 |
| Chinese | Qwen3.8-2.4T | 2 | 6 |
| Chinese | Kimi K3 | 0.40 | 15 |
| US small tier | Claude Haiku 5.5 | 0.10 | 0.50 |
| US small tier | GPT-6 Luna | 0.10 | 0.50 |
| US small tier | Gemini 3.8 Flash | 0.83 | 4.12 |
| US small tier | gpt-oss-120b | 0.15 | 0.60 |

**Per-task cost.** These are Artificial Analysis "Cost per Task" values on its Intelligence Index (v4.3.2), which reflects both price and verbosity. I extracted them from the page data on 2026-10-15 [primary, with caveats in Gaps] — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models). Index score first, then USD per task.
- **About 52–56 (no Chinese model reaches this band):**
  - Claude Opus 5.5 (xhigh): 56.0, $3.46
  - GPT-6 Astra (max): 52.7, $3.26
  - Gemini 4 Argon (high): 52.6, $1.99
  - GPT-6.1 Sol (max): 51.8, $0.72
- **About 42–46:**
  - MiMo-V2.6-Pro (open): 46.3, **$0.13**
  - Qwen3.8 Max (closed): 45.4, **$5.41**
  - GLM-5.3 (max): 44.8, $2.01
  - Step 5 Preview: 43.7, $1.03
  - Kimi K3 (max): 43.6, **$2.00**
  - Claude Haiku 5.5 (max): 43.4, **$0.21**
  - Claude Opus 5.5 (low): 42.3, $0.55
  - GPT-6.1 Sol (low): 42.1, **$0.13**
- **About 38–42:**
  - GLM-5.3-Flash: 41.8, $0.28
  - Gemini 3.8 Flash (high): 40.9, $1.24
  - DeepSeek V4.1 Flash (max): 39.5, $0.27
  - Muse Spark Open: 38.9, $0.84
  - MiMo-V2.6-Flash: 37.9, $0.06

**Cost comparisons from other sources:**
- CAISI (2025): one US reference model was 35% cheaper than the best DeepSeek model for similar performance.
- CAISI (2026): DeepSeek V4 was cheaper than GPT-5.4 mini on 5 of 7 benchmarks, ranging from 53% cheaper to 41% more expensive. — [NIST 2025](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks), [NIST 2026](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) [primary]

**US small closed models vs the best Chinese models on ECI** (accessed 2026-10-15) [primary] — [Epoch CSV](https://epoch.ai/data/eci_scores.csv)
- Claude Haiku 5.5 **158.98** (Oct 2026), Gemini 3.7/3.8 Flash 157.2, GPT-6 Luna 156.31.
- Kimi K3 157.42, DeepSeek V4.1 Flash 155.57.

**Price decline is an industry-wide trend.** Epoch finds the price of reaching a fixed performance level fell "9x to 900x per year" depending on the task, with the fastest drops most recent. — [Epoch, LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) [search-summary]

**Energy** (Jegham et al., "How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference", arXiv:2505.09598, v1 14 May 2025, v6 24 Nov 2025). Estimates are built from public API performance data, company-specific environmental multipliers and *inferred* hardware configurations, i.e. modelled rather than metered [primary] — [arXiv abstract](https://arxiv.org/abs/2505.09598), [HTML v6](https://arxiv.org/html/2505.09598v6)
- **Energy per query (Wh, short / medium / long prompt):**

  | Model and host | Short | Medium | Long |
  |---|---|---|---|
  | DeepSeek-R1, DeepSeek's own servers | 19.25 | 24.60 | **29.08** |
  | DeepSeek-R1, Azure | 2.35 | 4.33 | 7.41 |
  | DeepSeek-V3, DeepSeek's own servers | 2.78 | 8.86 | 13.16 |
  | DeepSeek-V3, Azure | 0.74 | 2.17 | 3.70 |
  | o3 | 1.18 | 5.15 | 12.22 |
  | GPT-4.1 nano | 0.21 | 0.58 | 0.83 |
  | Claude 3.7 Sonnet | 0.95 | 2.99 | 5.67 |

- Azure-hosted versions use "over 70% less energy". The gap is attributed to "inefficiencies in their data centers, including higher PUE, suboptimal cooling technologies" and less efficient hardware, *not* to model design.
- R1 on DeepSeek's servers uses about 65× the energy of the most efficient model on long prompts.
- The paper explicitly invokes the Jevons paradox: "As per-task efficiency improves, total AI usage expands far more rapidly, amplifying net resource consumption."

**Aggregate demand**
- IEA *Energy and AI* (Apr 2025):
  - Data centres used about 415 TWh in 2024 (about 1.5% of global electricity), with the **US at 45%, China 25% and Europe 15%**.
  - Demand is projected to reach **about 945 TWh by 2030**. The US accounts for the largest share of growth, followed by China. — [IEA news release](https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works) [search-summary; exec summary returned HTTP 403]
- Satya Nadella responded to DeepSeek with "Jevons paradox strikes again!" (27 Jan 2025). — [Fortune](https://fortune.com/2025/01/27/microsoft-ceo-satya-nadella-deepseek-optimism-jevons-paradox) [search-summary]

**China's own compute build-out**
- Alibaba pledged at least **RMB 380 billion (about USD 53B) over three years** for cloud and AI infrastructure on 24 Feb 2025, more than its AI and cloud spending of the previous decade. — [SCMP](https://scmp.com/tech/big-tech/article/3299858/alibaba-commits-us53-billion-ai-infrastructure-largest-private-computing-project) [search-summary]
- At the Apsara conference (Sep 2025), CEO Eddie Wu said Alibaba would increase this but gave no new figure. — [SCMP](https://www.scmp.com/tech/big-tech/article/3326624/alibaba-boost-ai-spending-china-tech-giant-sees-agi-new-start), [TechNode](https://technode.com/2025/09/24/alibaba-pitches-qwen-as-android-of-the-ai-era-advances-us52b-infrastructure-plan) [search-summary]
- Z.ai restricted new GLM coding-plan subscriptions citing compute limits (early 2026). — [MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) [secondary]

**Cause: choice, or forced by export controls?**
- DeepSeek founder Liang Wenfeng (Waves interview, before Jul 2024, via AFP): "Money has never been the problem we face; it's the embargo on high-end chips." — [AFP via Prothom Alo](https://en.prothomalo.com/business/global/mj5l9kiuwb) [search-summary]
- The FT (Aug 2025) reported that Chinese authorities encouraged DeepSeek to train R2 on Huawei Ascend. Failed training runs delayed R2, so DeepSeek reverted to Nvidia for training and kept Ascend for inference. — [TrendForce](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-reportedly-urged-by-chinese-authorities-to-train-new-model-on-huawei-hardware-after-multiple-failures-r2-training-to-switch-back-to-nvidia-hardware-while-ascend-gpus-handle-inference) [search-summary; single anonymous-source chain]
- CSIS: export controls limit chips and global inference capacity, and "Open-weight releases reduce that burden because third-party providers and local users supply much of the serving compute". — [CSIS, 2 Jul 2026](https://www.csis.org/analysis/what-know-about-chinese-ai-models) [primary]
- Liu Zhiyuan (Tsinghua): "Compute and energy are real constraints for any deployment", which helps explain the push toward smaller models. — [MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) [secondary]

**Universities self-hosting**
- **Epoch (15 Aug 2025):** open models runnable on a single consumer GPU "typically match the capabilities of frontier models after an average lag between 6-12 months".
  - Size thresholds assume 4-bit weights: ≤28B parameters (RTX 4090 era) and ≤40B (RTX 5090 era).
  - Lags by benchmark: GPQA 7.4 months, MMLU-Pro 7.3, AA Index 6.3, Arena 12.4.
  - Epoch warns that small open models are more likely to be benchmark-optimised. — [Epoch](https://epoch.ai/data-insights/consumer-gpu-model-gap) [primary]
- **Oct 2026 example:** Qwen3.8-27B (27.8B dense parameters, Apache 2.0) scores **ECI 151.55 vs GPT-5's 150.0** (Aug 2025).
  - It is within Epoch's ≤40B consumer-GPU threshold.
  - But on AA's agentic-heavy index it scores only 33.7 vs 58 for the top model. — [Epoch CSV](https://epoch.ai/data/eci_scores.csv), [HF API](https://huggingface.co/api/models/Qwen/Qwen3.8-27B), [AA](https://artificialanalysis.ai/leaderboards/models) [primary]
- **Frontier-class Chinese open weights are cluster-scale:** DeepSeek-V4-Pro 1.6T, Kimi K3 2.8T and Qwen3.8 2.4T total parameters. A reported 1.56 TB Kimi K3 download. — [MLQ](https://mlq.ai/news/moonshot-releases-156-tb-kimi-k3-weights-under-a-custom-commercial-license/) [search-summary]
- **Chinese universities' 2025 local deployments** of full DeepSeek R1/V3 (671B) [search-summary] — [China News, 26 Feb 2025](https://www.chinanews.com/edu/2025/02-26/10374773.shtml), [The Paper](https://m.thepaper.cn/newsDetail_forward_30174463)
  - Shanghai Jiao Tong University ran it on a fully domestic Huawei Ascend stack.
  - Renmin University and Peking University also deployed it, and Tsinghua, Zhejiang, Southeast, Wuhan, BNU and others announced uses.
  - The stated rationale: data must not leave the institution ("数据不出域"), and closed models cannot be privately delivered or are costly.

### Inferences
- **"Efficient" is accurate on training compute and architecture.** Frontier-adjacent results with 1/30 to 1/50 of the largest US training compute is the most robust part of the author's claim. The open publication of these techniques (MLA, FP8, DSA, linear and hybrid attention) is a genuine contribution.
- **"Not yet as powerful" is accurate on capability indices** (4–9 months; about 9 ECI points; 12 AA points between the best open model and the top). It is overstated on Arena (2.4–2.8%).
- **"Consume much less" should be dropped or heavily qualified.**
  - Lower **per-token prices** do not mean lower **per-task** cost or energy: verbose reasoning, hosting hardware and data-centre efficiency dominate.
  - The only systematic per-query energy estimates put DeepSeek's own deployment among the worst. The same model on Azure was about 70–75% lower.
  - Chinese 2026 flagships are among the largest models by total parameters.
  - National demand is rising regardless (Jevons; Alibaba's capex; China at 25% of global data-centre electricity in 2024).
- **Cause:** the evidence supports **necessity plus strategy**, not an ideological "bet on efficiency".
  - Necessity: export controls on chips, plus state pressure to use domestic Ascend chips.
  - Strategy: open weights reward models that others can run cheaply.
- **Kind vs emphasis.** US labs use the same sparse-MoE recipe (gpt-oss and Llama 4 at about 4% active) and sell small tiers (Haiku, Luna, Flash) that match the best Chinese models on ECI at similar or lower per-token prices. The real difference is emphasis and **disclosure**: Chinese labs publish efficient frontier-adjacent weights and architectures, while US labs keep their efficient frontier models closed.
- **For universities:**
  - Small dense or sparse open models that fit one GPU reach the closed frontier of about 6–12 months earlier (Epoch). Qwen3.8-27B ≈ GPT-5 on ECI is a concrete 2026 example.
  - Running *frontier-class* open weights (0.7–2.8T parameters) needs a multi-GPU cluster or national supercomputing centre. That is feasible for consortia, or for well-funded universities as Chinese universities showed in 2025.
  - The governance-relevant property is **self-hostability and data control**, not efficiency per se.

**Suggested wording (efficiency):**
> "Chinese labs have pushed hard on training efficiency, a push driven as much by US chip export controls as by choice. Sparse 'mixture-of-experts' designs activate only a few percent of their parameters per token, and techniques such as low-precision (FP8) training and compressed or sparse attention have let firms like DeepSeek, Moonshot and Alibaba come within roughly four to nine months of the US frontier using a small fraction (on Epoch AI's estimates, a thirtieth to a fiftieth) of the largest US training budgets. Their models are typically cheaper per token, and because many are released as open weights, smaller versions now run on a single high-end GPU with capabilities close to those of US frontier models of about a year earlier. That puts capable, self-hosted AI within reach of university IT departments, and frontier-class versions within reach of national computing centres. But 'efficient' should not be read as 'consumes less': energy per answer depends heavily on how many tokens a reasoning model generates and on the data centre that serves it, US labs pursue the same efficiencies in their 'small' models, and cheaper AI has so far increased total demand rather than reduced it."

### Gaps
- **Jegham et al. evidence status.** It is an arXiv preprint (6 versions; peer-review status not verified), and its energy figures are modelled estimates based on inferred hardware, not metered. No 2026 study of energy per *task* for current US vs Chinese frontier models was found.
- **AA per-task costs:**
  - They were parsed from embedded page data; at least one record (an un-suffixed "Claude Opus 5.5") was mis-parsed and excluded.
  - Values depend on which provider prices AA uses: for example, AA lists Kimi K3 at $3/$15 while an OpenRouter provider lists $0.40/$15.
  - Re-check on artificialanalysis.ai before quoting.
- **Compute disclosure and ratios.** Training compute for Claude and Gemini frontier models is undisclosed, so the "30–50×" ratio compares against the largest *known* US runs. Epoch marks Kimi K3 and Qwen3-Max compute as "Speculative".
- **Aggregate demand data.** No verified 2026 figure was found for China's total AI-compute energy use or for Alibaba's revised capex. The 480 bn RMB figure is unconfirmed.
- **Secondary token-verbosity claims were not used.** Examples: "Kimi K2.5 used ~89M output tokens vs 14M for Claude Sonnet 4.6", and "GPT-5.6 used ~1/9 of DeepSeek V4's tokens". These come from blogs citing AA and were not verified.

---

## Q10. Implications for the paper: defensible wording

### Takeaway
The contrast holds for **weights, licences (for some labs), training-compute efficiency, per-token price and open-model adoption**. It fails for **data openness, transparency, freedom from state control, and "consumes much less"** (energy and per-task cost are not established to be lower). It is also eroding at the Chinese flagship level in 2026. Any "who leads" sentence must be dated and multi-tracker.

### Cited Findings
See Q1–Q7. The key anchors are:
- [HF Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [FMTI 2025](https://crfm.stanford.edu/fmti/December-2025)
- [Pan & Xu 2026](https://academic.oup.com/pnasnexus/article/5/2/pgag013/8487339)
- [Epoch US–China](https://epoch.ai/data-insights/us-vs-china-eci) and [Epoch ECI CSV](https://epoch.ai/data/eci_scores.csv)
- [Arena dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
- [AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)
- Licence texts for [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE) and [Qwen3.8](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)
- [Anthropic directive statement](https://www.anthropic.com/news/fable-mythos-access)
- [Reuters on Beijing curbs](https://finance.yahoo.com/technology/ai/articles/exclusive-beijing-looking-curbing-overseas-101644780.html)

### Inferences
**Suggested wording, "another direction":**
> "Chinese labs have taken a different route to distribution, not to openness in the full sense. Since DeepSeek-R1 (January 2025), firms such as DeepSeek, Alibaba (Qwen), Moonshot and Zhipu have released frontier-adjacent model weights, often under permissive MIT or Apache licences and at a fraction of US prices. By 2025–26 Chinese models accounted for the largest national share of downloads on Hugging Face (about 41% over the year to March 2026), and Qwen had become the most-used open base model in scientific papers. Yet what is opened is the weights, not the training data: independent transparency audits rate these firms as opaque as closed US labs. The models are developed under a regulatory regime that requires generative services to 'uphold core socialist values'. Peer-reviewed tests find more political refusals and inaccuracies in China-origin models. And in 2026 several Chinese flagships moved to closed or revenue-restricted licences, while Beijing discussed curbing foreign access to its most advanced models. Open weights decentralise *who runs* the model; they do not decentralise *who shapes* it."

**Optional symmetry sentence** (supports the paper's concentration thesis without implying US = neutral):
> "Nor is state leverage a Chinese peculiarity: in June 2026 a US export-control directive briefly cut off access to a leading US model for all foreign nationals."

**Suggested wording, "who leads":**
> "As of October 2026, independent trackers place a handful of US firms (Anthropic, OpenAI, Google and, on some measures, Meta) at the frontier, with the lead rotating between them on a scale of weeks. Anthropic's Claude Opus 5.5 tops Epoch AI's Capabilities Index (statistically tied with OpenAI's GPT-6 models) and Artificial Analysis's index, while Google's Gemini 4 Argon tops the Arena human-preference leaderboard. The best Chinese and best open-weight models trail by roughly four to nine months on capability indices (Epoch; NIST CAISI), although on human-preference rankings the gap is under 3%."

Avoid "by far". If the author wants to emphasise Claude, the defensible form is "among the strongest models on current independent benchmarks", with dates.

**On efficiency** (full suggested paragraph in Q9): say "trained with a fraction of the compute and cheaper per token", **not** "consume much less". Present the efficiency drive as shaped by export controls as well as choice, and note that US labs pursue the same techniques in their small models. For the university angle, the robust claim is that **open weights make self-hosting possible**:
- Single-GPU open models now match the closed frontier of about 6–12 months earlier (Epoch).
- Frontier-class open weights need cluster-scale hardware.

**For the governance section:** China's 2020 decree banning cash-per-SCI-paper rewards and SCI-based hiring, its 2026 abolition of the CAS journal ranking, and the AI+ plan's call to count open-source contributions in faculty evaluation are a real precedent for top-down metric change. Pair it with the evidence that early implementation was largely symbolic (Shu et al., *Minerva* 2022) and that discretion shifted power to senior gatekeepers (*Higher Education* 2025).

### Gaps
- All tracker numbers are a 15 Oct 2026 snapshot and will be outdated within weeks. The writer should re-pull Epoch, Arena and AA immediately before submission.
- The Degree Law's final AI wording and any NSFC-specific AI rule remain unverified.
