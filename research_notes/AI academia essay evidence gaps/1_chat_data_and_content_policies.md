# Chat data and scholarly content as AI training inputs (2022–2026): testing the "convergence on harvesting user knowledge" claim

All URLs accessed 2026-10-15. **Primary** = company policy, help-centre or blog page; court filing or court-approved notice; regulator decision. **Secondary** = press, law-firm or aggregator. **[search extract]** = the page could not be fetched directly (HTTP 403 or paywall), so the content comes from the search engine's extract of that page. Treat these as less certain than pages that were read in full.

Access limits that affected the evidence:
- web.archive.org is blocked by this environment's egress policy. Wayback snapshot URLs were located with the archive.org availability API, but their contents could **not** be read (listed under Gaps in Q1).
- For Anthropic's history I used Anthropic's own dated legal archive (anthropic.com/legal/archive/…), which is primary and could be read.
- openai.com, help.openai.com, x.ai and the Microsoft Copilot blog returned 403. Reuters, Wired and The Verge cannot be searched with the search tool. The Verge could be fetched directly and was.

Disclosure, at the caller's request: these notes were compiled by a Claude model (made by Anthropic). Evidence unfavourable to Anthropic is reported in the same way as everything else.

---

## Q1. Cross-company comparison: consumer-chat training defaults, opt-outs, retention, human review, exclusions (status at 2026-10-15)

### Takeaway
As of October 2026, every major US general-purpose assistant examined uses consumer conversations for training by default, with an opt-out at most: OpenAI, Google, Meta, Microsoft, xAI and (since October 2025) Anthropic. So do the EU's Mistral and the Chinese assistants DeepSeek, Kimi, Doubao and Qwen. Meta goes furthest: since December 2025 it has used AI chats for ad and content personalisation with no opt-out. Paid business, API, government and education tiers are excluded by default everywhere. The clear counter-examples are Apple (opt-in only) and Proton's Lumo (no training).

### Cited Findings

**Summary table.** Sources are in the last column. Each fact is repeated with an inline citation in the per-company sections (Q2–Q9).

| Company / product | Consumer chats used for training by default? | How to opt out | Documented since | Retention | Human review | Business / API / Edu exclusions | Sources |
|---|---|---|---|---|---|---|---|
| **OpenAI ChatGPT** (Free/Plus/Pro) | Yes | Settings > Data Controls > "Improve the model for everyone" off; Temporary Chat; Privacy Portal "Do not train on my content" | At least early 2023. Opt-out form and then a "chat history off" toggle (Apr 2023). Separate training toggle from about Apr–May 2024 | Deleted chats and Temporary Chats are removed within 30 days, except during the NYT preservation order (13 May – 26 Sep 2025) | Temporary chats "may be reviewed only to monitor for abuse"; other review practices not verified | Team/Business, Enterprise, Edu and API not trained by default (API since 1 Mar 2023) | [help 5722486](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) [search extract]; [help 8983082](https://help.openai.com/en/articles/8983082-how-do-i-turn-off-chat-history-and-model-training) [search extract]; [NYT-demands page](https://openai.com/index/response-to-nyt-data-demands/) [search extract] |
| **Google Gemini Apps** | Yes for users 18+ ("Keep Activity is on by default") | Turn off Keep Activity; Temporary Chats | Bard (2023), per secondary sources; uploads sampled for training from 2 Sep 2025 | Auto-delete after 18 months by default (3, 36 months or never selectable); 72 h when activity is off; human-reviewed chats kept up to 3 years | Yes: a subset of chats, reviewed by Google and service providers, disconnected from the account | Workspace for Education chats are not human-reviewed or used for training; work/school accounts are under different terms | [Privacy Hub](https://support.google.com/gemini/answer/13594961); [Activity help](https://support.google.com/gemini/answer/13278892); [blog 13 Aug 2025](https://blog.google/products/gemini/temporary-chats-privacy-controls/) |
| **Meta AI** (FB/IG/WA/Meta AI app) | Yes ("use the information people share when interacting with our generative AI features… to improve our products") | EU: objection form. No consumer training opt-out found for US users (gap). No opt-out from ad/content personalisation using AI chats (from 16 Dec 2025) | Sep 2023 (Meta AI launch post). EU training on public posts and AI interactions from 27 May 2025 | Not found | Not found | Not applicable / not found | [Meta 27 Sep 2023](https://about.fb.com/news/2023/09/privacy-matters-metas-generative-ai-features/); [Meta 14 Apr 2025](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/); [Reuters via TradingView](https://de.tradingview.com/news/reuters.com,2025:newsml_L6N3VH1DX:0-meta-to-use-ai-chats-to-personalize-content-and-ads-from-december) |
| **Meta Muse** (agent, Sep 2026) | Yes: "This setting is on when you first use Muse" | Toggle; turning it off also applies to previous interactions | Sep 2026 | Not stated | Not stated | – | [Meta help](https://www.meta.com/help/artificial-intelligence/1047255454427887/) |
| **Microsoft Copilot** (consumer) | Yes, unless excluded | "Training on conversation activity" and "Training on voice conversations" toggles | Announced 16 Aug 2024; opt-out controls Oct 2024 | Conversation activity stored 18 months by default | Yes, automated and human; "an opt-out of human review is not available" | Entra ID (organisational) accounts, Microsoft 365 Copilot, under-18s and signed-out users excluded. Countries excluded: Brazil, China (excl. HK), Israel, Nigeria, South Korea, Vietnam | [Copilot privacy FAQ](https://support.microsoft.com/en-us/topic/privacy-faq-for-microsoft-copilot-27b3a435-8dc9-4b55-9a4b-58eeb9647a7f); [controls](https://support.microsoft.com/en-us/topic/microsoft-copilot-privacy-controls-8e479f27-6eb6-48c5-8d6a-c134062e2be6); [The Decoder 17 Aug 2024](https://the-decoder.com/microsoft-will-start-training-ai-models-with-user-data-from-copilot-bing-and-msn-in-october) |
| **xAI Grok** | Yes | "Improve the model" toggle in the app and on the web; on X: Privacy & safety > Grok & Third-party Collaborators; Private Chat excluded | X posts opted in by default by July 2024; EU posts processed from 7 May 2024 | Not verified | "A limited number of authorized personnel may review your conversations" | API: no training without explicit permission | [x.ai FAQ](https://x.ai/legal/faq) [search extract]; [DPC 8 Aug 2024](https://www.dataprotection.ie/en/news-media/press-releases/dpc-welcomes-xs-agreement-suspend-its-processing-personal-data-purpose-training-ai-tool-grok); [EFF](https://x.com/EFF/status/1816895089245061262) [search extract] |
| **Anthropic Claude** (Free/Pro/Max, including Claude Code) | **Before 8 Oct 2025: No** (unless opt-in, feedback or safety flag). **After: Yes**, with the toggle pre-set "On" in the pop-up | Privacy Settings > "Help improve Claude" / "Model Improvement"; Incognito chats | Announced 28 Aug 2025; terms effective 8 Oct 2025 (originally 28 Sep) | Up to 5 years (de-identified, in training pipelines) if allowed; deleted chats removed within 30 days; safety-flagged content 2 years (scores 7 years); feedback 5 years | Not described for training. Safety review of flagged content exists | Claude for Work, Gov, Education and API (including Bedrock and Vertex) excluded | [Anthropic 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms); [The Verge](https://www.theverge.com/anthropic/767507/anthropic-user-data-consumers-ai-models-training-privacy); [terms](https://www.anthropic.com/legal/consumer-terms); [privacy centre](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data) |
| **Mistral Le Chat** (help centre now says "Vibe") | Yes ("not opted out by default") | Web toggle "Allow your interactions to be used to train our models"; mobile "Enable data sharing" | Start date not found | Not found | Not found | Enterprise opted out by default; Teams admins can opt out the organisation; API/Studio has a separate toggle | [Mistral 347617](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models); [Mistral 455207](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) |
| **DeepSeek** | Policy permits it ("User Input… to train and improve"). But the EU training summary for DeepSeek-V4 ticks **No** for user-interaction data | A "right to opt-out of using your Personal Data for training"; no in-app path described | Policy last updated 10 Feb 2026 | "As long as you have an account" | Not stated | Not stated | [DeepSeek policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html); [V4 summary](https://cdn.deepseek.com/policies/DeepSeek_Template_for_the_Public_Summary_of_Training_Content_for_GeneralPurpose_AI_model.pdf) |
| **Moonshot Kimi** | Yes (de-identified) | Email customer service; registered within 5–7 working days; account-level only | Policy effective 31 Aug 2026 | Stored in PRC | Not stated | – | [Kimi help](https://www.kimi.com/zh-hans/help/others/data-usage); [Kimi policy](https://www.kimi.com/user/agreement/userPrivacy?version=v2) |
| **ByteDance Doubao** | Yes, personal edition (de-identified) | In-app: Settings > Privacy & Permissions > "Help improve model effectiveness" | Policy effective 17 Sep 2026 | Stored in PRC | Not stated | Enterprise edition handled differently | [Doubao policy](https://www.doubao.com/legal/privacy) |
| **Alibaba Qwen / 千问 app** | Yes: samples a small share of de-identified inputs for "model evaluation and feature optimization" | Text: contact the company. Voice: toggle "改进语音服务" | Policy effective 14 Nov 2025 | Stored in PRC | Not stated | Knowledge-base content not used without separate consent | [Qwen policy (third-party mirror)](https://www.elawcn.com/agreement/2025/1127/1676.html) |
| **Apple Intelligence** (counter-example) | **No.** "never used to train our foundation models unless you explicitly choose to help improve them" | Opt-in | Since Jun 2024 | – | – | – | [Apple ML](https://machinelearning.apple.com/research/introducing-apple-foundation-models) |
| **Proton Lumo** (counter-example) | **No.** "doesn't use your conversations or inputs to train" | n/a | Since Jul 2025 | "No logs" server-side | – | – | [Proton 23 Jul 2025](https://proton.me/blog/lumo-ai) |

**Historical archive URLs.** These were located with the archive.org availability API. Their **content was not read**, because web.archive.org is blocked here; a later reader should check them.
- OpenAI Data Controls FAQ, snapshots of 2 May 2023, 28 Feb 2024 and 3 Jun 2025: [2023](http://web.archive.org/web/20230502190723/https://help.openai.com/en/articles/7730893-data-controls-faq), [2024](http://web.archive.org/web/20240228113259/https://help.openai.com/en/articles/7730893-data-controls-faq), [2025](http://web.archive.org/web/20250603183456/https://help.openai.com/en/articles/7730893-data-controls-faq)
- OpenAI "New ways to manage your data in ChatGPT", 27 Apr 2023: [snapshot](http://web.archive.org/web/20230427003907/https://openai.com/blog/new-ways-to-manage-your-data-in-chatgpt)
- OpenAI "How your data is used to improve model performance", 4 Apr 2023: [snapshot](http://web.archive.org/web/20230404114932/https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
- Bard Privacy Hub, 23 Jul 2023: [snapshot](http://web.archive.org/web/20230723003818/https://support.google.com/bard/answer/13594961)
- Gemini Privacy Hub, 1 Mar 2024: [snapshot](http://web.archive.org/web/20240301195020/https://support.google.com/gemini/answer/13594961)
- Anthropic "Is my data used for model training?", 5 Aug 2025 (pre-change): [snapshot](http://web.archive.org/web/20250805144037/https://privacy.anthropic.com/en/articles/10023580-is-my-data-used-for-model-training)
- Anthropic 28 Aug 2025 post, as of 29 Aug 2025: [snapshot](http://web.archive.org/web/20250829184959/https://www.anthropic.com/news/updates-to-our-consumer-terms)
- Microsoft Copilot blog, 19 Aug 2024: [snapshot](http://web.archive.org/web/20240819102321/https://www.microsoft.com/en-us/microsoft-copilot/blog/2024/08/16/transparency-and-control-in-consumer-data-use/)
- xAI FAQ, 14 Jun 2025: [snapshot](http://web.archive.org/web/20250614022714/https://x.ai/legal/faq)
- Mistral help, 1 Jul 2025: [snapshot](http://web.archive.org/web/20250701211602/https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)

**Cross-cutting regulatory facts**
- China's TC260-003 standard (29 Feb 2024) requires an **opt-out**, not an opt-in, for user inputs used in training: "Users shall be provided with a way to turn off the use of their entered information for training purposes… no more than 4 clicks shall be required for the user to reach the option from the main interface" — [CSET translation of TC260-003](https://cset.georgetown.edu/wp-content/uploads/t0588_generative_AI_safety_EN.pdf)
- The EU AI Act training-content template now asks every general-purpose AI provider, under Section 2.4 "User data": "Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? ☐ Yes ☐ No". The template was published 24 Jul 2025; the version read is Commission document C(2025) 8311 final of 5 Dec 2025 — [European Commission page](https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models); [template PDF](https://ec.europa.eu/newsroom/dae/redirection/document/118480)

### Inferences
- The industry norm by 2026 is a **two-tier model**. Consumers' conversations are a default training input; institutions that pay (enterprise, API, government, education) contract out of it. For academia this matters directly: a researcher using a university-licensed Claude for Education, ChatGPT Edu or Workspace-for-Education Gemini is excluded from training by default. The same researcher on a personal Free/Plus/Pro account is included unless they opt out.
- "Opt-out" covers very different things in practice. Some firms offer an in-app toggle (OpenAI, Google, Microsoft, Anthropic, Mistral, xAI, Doubao). Others require email or a contact form (Kimi, DeepSeek, Qwen text) or an objection form (Meta in the EU). Meta's ad personalisation from AI chats has none.

### Gaps
- Wayback snapshots were not readable here, so the exact pre-2024 wording of OpenAI and Google pages is not verified from primary text.
- Meta's training opt-out for non-EU (e.g. US) Meta AI users was not found; neither were retention periods for Meta AI, xAI or Mistral consumer chats.
- No OpenAI document reviewed states a default auto-delete period for saved chats.
- Microsoft's status for EEA/UK training is unclear. EEA was excluded "until further notice" in 2024, but it is not in the current exclusion list, and that FAQ section is marked as applying only to the "older version" of the Copilot app, with a new app available from 18 Aug 2026.

---

## Q2. OpenAI (ChatGPT): "Improve the model for everyone", Temporary Chat, and policy history since 2023

### Takeaway
OpenAI is the earliest documented case of training on consumer chats by default (from at least early 2023). Its controls were built around an opt-out from the start, and under regulatory pressure from Italy. API data has been excluded by default since March 2023, and business/education tiers since they launched. In 2026 OpenAI added advertising matched to conversation context on Free and Go tiers.

### Cited Findings
- **Current default (consumer).** "When you use our services for individuals (Free, Plus, Pro), we may use your content to train our models", and users can turn this off in settings — [OpenAI help, "How your data is used to improve model performance"](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) [search extract; direct fetch 403]
- **Business exclusion.** "By default, we do not train on any inputs or outputs from our products for business users, including ChatGPT Team, ChatGPT Enterprise, and the API." Edu is processed under a Student Data Privacy Agreement — [same page](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) [search extract]; [OpenAI Enterprise privacy](https://openai.com/enterprise-privacy/) [search extract]
- **Feedback exception.** Even after opting out, "If you choose to provide feedback, the entire conversation associated with that feedback may be used to train our models" — [OpenAI help 5722486](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) [search extract]
- **The toggle.** "When Improve the model for everyone is off, new conversations won't be used to train OpenAI models. They can still appear in your chat history." Signed-out users can also turn it off — [OpenAI help 8983082](https://help.openai.com/en/articles/8983082-how-do-i-turn-off-chat-history-and-model-training) [search extract]
- **Temporary Chat.** Not shown in history, does not update memory, not used to improve models, "may be retained for up to 30 days for safety purposes" — [OpenAI Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq) [search extract]. Introduced in the post "Memory and new controls for ChatGPT", dated 13 Feb 2024 — [OpenAI](https://openai.com/index/memory-and-new-controls-for-chatgpt/) [search extract]; [Simon Willison, 14 Feb 2024](https://simonwillison.net/2024/Feb/14/memory-and-new-controls-for-chatgpt/) (secondary) [search extract]
- **April 2023 control.** "Conversations that are started when chat history is disabled won't be used to train and improve our models"; such conversations are retained 30 days and reviewed "only when needed to monitor for abuse" — [OpenAI, "New ways to manage your data in ChatGPT"](https://openai.com/index/new-ways-to-manage-your-data-in-chatgpt/) [search extract; 403]. Training and history were bundled in a single "Chat history & training" switch until about late April–May 2024. A user thread of 29 Apr 2024 quotes the old FAQ text; on 13 May 2024 a user reports the FAQ updated to the new "Improve the model for everyone" UI — [OpenAI Developer Community thread](https://community.openai.com/t/chat-history-training-option-missing-from-web-ui/731626) (secondary, user forum)
- **API (1 Mar 2023).** API data is "not used to train or improve OpenAI models (unless you explicitly opt in)"; abuse-monitoring logs are kept up to 30 days — [OpenAI developer docs, "Your data"](https://developers.openai.com/api/docs/guides/your-data) [search extract]
- **Regulatory origin of the opt-out (Italy, 2023).**
  - On 30 Mar 2023 the Garante imposed an immediate temporary limitation on OpenAI's processing of Italian users' data. It found no legal basis for mass collection of personal data to "train" the algorithms — [Garante press release](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847) [search extract]
  - The order of 11 Apr 2023 required a tool to object to the use of data for training, including for non-users — [Garante provvedimento 11 Apr 2023](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9874702) [search extract]
  - On 28 Apr 2023 ChatGPT reopened in Italy. OpenAI had given everyone in Europe a right to object via an online form, and training on users' data was based on legitimate interest unless they objected — [Garante 28 Apr 2023](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9881490) [search extract]
- **Retention after the NYT litigation.** OpenAI's update of 22 Oct 2025: "we are no longer under a legal order to retain consumer ChatGPT and API content indefinitely. Our obligations under the earlier order ended on September 26, 2025." It says deleted conversations and Temporary Chats are again deleted within 30 days. It keeps "limited historical April–September 2025 user data" — [OpenAI, response to NYT data demands](https://openai.com/index/response-to-nyt-data-demands/) (party statement) [search extract]
- **Advertising (2026).**
  - OpenAI's post of 16 Jan 2026 announced ad tests for logged-in adult US users on Free and Go. It lists "Conversation privacy" as a principle (no conversations shared with or sold to advertisers) and excludes under-18s and sensitive topics (health, mental health, politics) — [OpenAI, "Our approach to advertising and expanding access to ChatGPT"](https://openai.com/index/our-approach-to-advertising-and-expanding-access/) [search extract]
  - The US test began 9 Feb 2026. Ad targeting uses context kept inside ChatGPT; advertisers receive only aggregate data — [OpenAI help, "Ads in ChatGPT"](https://help.openai.com/en/articles/20001047) [search extract]
  - Reporting says ads are matched to conversation topic, previous chats and past ad interactions — [The Decoder](https://the-decoder.com/chatgpt-now-shows-ads-to-free-and-go-users-with-opt-out-cutting-daily-message-limits/) (secondary) [search extract]
  - On 18 Aug 2026 OpenAI announced expansion to 31 European markets — [OpenAI, "ChatGPT Ads expands across Europe"](https://openai.com/index/chatgpt-ads-expands-across-europe/) [search extract]

### Inferences
- In OpenAI's case the opt-out was a response to regulators, not something offered from the start. The first control came within weeks of the Garante's March 2023 ban. That is evidence that default training was the initial position.
- With ads from 2026, chat context becomes both a training input and an ad-matching input. OpenAI says advertisers do not receive conversations.

### Gaps
- No primary text from November 2022 to February 2023 was read; OpenAI's 2022 terms and the original opt-out Google Form are not verified.
- OpenAI pages were reached only through search extracts (403). The exact date of the "Improve the model for everyone" UI change rests on a user forum thread.

---

## Q3. Google (Gemini Apps): Keep Activity / Gemini Apps Activity, human reviewers, 2025 changes

### Takeaway
Gemini trains on adult users' chats by default ("Keep Activity" on for users 18+), with human review of a sample. Reviewed chats are kept up to three years even if the user deletes their activity. In 2025 Google renamed the control, added Temporary Chats, and extended training to a sample of uploaded files and photos from 2 Sep 2025. Education and Workspace accounts are excluded.

### Cited Findings
- "If you're 18 or over, Keep Activity is on by default." When it is off, conversations are still saved for up to 72 hours. Activity older than 18 months is auto-deleted by default; the user can choose 3 or 36 months or turn auto-delete off — [Gemini Apps Help, Manage & delete your activity](https://support.google.com/gemini/answer/13278892)
- With Keep Activity on, "Google uses your activity to provide, develop, and improve its services (including training generative AI models)" — [Gemini Apps Privacy Hub, last updated 13 Oct 2026](https://support.google.com/gemini/answer/13594961)
- **Human review.** A subset of chats is reviewed by human reviewers, including trained service providers. "Chats are disconnected from your account before being sent to service providers." "Reviewed chats are retained for up to three years", and deleting activity does not delete them — [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961)
- **Temporary chats.** "Temporary chats are not used to train Google's AI models"; they are retained 72 hours. Audio and Gemini Live recordings are not used by default — [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961)
- **2025 changes (blog of 13 Aug 2025, Michael Siliski).** "Gemini Apps Activity" was renamed "Keep Activity". "When this setting is on, a sample of your future uploads will be used to help improve Google services for everyone", applying to "uploads submitted starting September 2, 2025". Temporary Chats "won't be used to personalize your Gemini experience or train Google's AI models" — [Google blog](https://blog.google/products/gemini/temporary-chats-privacy-controls/)
- **2023 (Bard).** Bard activity was kept 18 months by default. A random sample of conversations was reviewed without a link to the account, and reviewed conversations were kept up to three years — [Techzine](https://www.techzine.eu/news/applications/108995/eu-users-can-keep-conversations-with-google-bard-out-of-training-set/) (secondary) [search extract]; [TechStartups, 23 Oct 2023](https://techstartups.com/2023/10/23/google-bard-now-includes-human-reviewers-who-may-read-your-conversations-dont-enter-sensitive-info-google-says/) (secondary) [search extract]
- **Education and work exclusions.** "All Google Workspace for Education users have added data protection in the Gemini app, meaning their chats with Gemini are not human reviewed or used to train AI models" — [Google blog (education)](https://blog.google/products-and-platforms/products/education/gemini-enterprise-grade-data-protection/) [search extract]. Work and school accounts "may be subject to different data handling terms" — [Privacy Hub](https://support.google.com/gemini/answer/13594961)
- **Region.** Gemini Apps are provided by Google Ireland Ltd in the EEA and Switzerland. The EU/UK section lists consent as the legal basis for some features (e.g. sharing audio and Live recordings) — [Privacy Hub](https://support.google.com/gemini/answer/13594961)

### Inferences
- Google's model has been default-on with human review since Bard. The 2025 change widened the scope to uploads rather than changing the default.
- Reviewed chats are kept up to three years regardless of user deletion. That is a longer survival of user content against user action than Anthropic's practice, where deleted chats are excluded from training.

### Gaps
- No teen-specific default for consumer Gemini was confirmed.
- The original 2023 Bard Privacy Notice was not read (Wayback blocked).

---

## Q4. Meta (Meta AI): chat use for ads and content personalisation (2025); EU training on public posts; DPA responses

### Takeaway
Meta has used AI-chat interactions "to improve our products" since 2023. It resumed EU training on adults' public posts and Meta AI interactions on 27 May 2025, after regulator-negotiated changes. From 16 Dec 2025 it began using AI chats to personalise content and ads with **no opt-out**, outside the EU, UK and South Korea. Meta is the clearest case of chat data being monetised directly.

### Cited Findings
- **2023.** "We use the information people share when interacting with our generative AI features, such as Meta AI or businesses who use generative AI, to improve our products and for other purposes." Public FB/IG posts were part of the training data; private messages and private posts were not — [Meta Newsroom, 27 Sep 2023](https://about.fb.com/news/2023/09/privacy-matters-metas-generative-ai-features/)
- **EU, April 2025.** Meta would "train AI at Meta using public content —like public posts and comments— shared by adults on our products in the EU", and "People's interactions with Meta AI – like questions and queries – will also be used to train and improve our models." Users get "a link to a form where people can object." Under-18 accounts are excluded. Meta says it is "following the example set by others including Google and OpenAI" — [Meta Newsroom, 14 Apr 2025](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/)
- **Irish DPC, 21 May 2025.** Meta planned to train "using public content shared by adults on Facebook and Instagram across the EU/EEA" from 27 May 2025. The DPC required:
  - updated transparency notices;
  - an easier objection form;
  - a longer notice period;
  - de-identification and filtering.

  It also required an efficacy report "expected in October 2025". It recalls that Meta paused in June 2024, and that the EDPB Opinion of December 2024 gave general criteria — [DPC statement](https://www.dataprotection.ie/news-media/latest-news/dpc-statement-meta-ai)
- **noyb.**
  - Eleven complaints in June 2024 "resulting in a pause" of Meta's plans.
  - A cease-and-desist letter dated 14 May 2025, threatening a European class action.
  - Verbraucherzentrale NRW's separate injunction attempt was not granted by a German court at the interim stage.
  - Source: [noyb](https://noyb.eu/en/noyb-sends-meta-cease-and-desist-letter-over-ai-training-european-class-action-potential-next-step) (advocacy group) [search extract]
- **Ads and content from AI chats.**
  - Meta: "Whether it's a voice chat or a text exchange with our AI features, this update will help us improve the recommendations." Notifications from 7 Oct 2025; "it goes into effect on December 16, 2025." Conversations about religious views, sexual orientation, political views, health, racial or ethnic origin, philosophical beliefs or trade-union membership are not used for ads — [Meta Newsroom, 1 Oct 2025](https://about.fb.com/news/2025/10/improving-your-recommendations-apps-ai-meta/)
  - Reuters: "they will not have an option to opt out… though the update applies only to those who use Meta AI"; rollout "excluding the UK, the European Union and South Korea" — [Reuters via TradingView, 1 Oct 2025](https://de.tradingview.com/news/reuters.com,2025:newsml_L6N3VH1DX:0-meta-to-use-ai-chats-to-personalize-content-and-ads-from-december) (secondary)
- **Muse (agent, announced 8 Sep 2026).** "You decide whether we can use your interactions with Muse to develop and improve our AI models. This setting is on when you first use Muse." "Changes to this setting also apply to previous interactions." "Muse doesn't share your conversations or the data in your virtual machine with Meta ad systems" — [Meta help](https://www.meta.com/help/artificial-intelligence/1047255454427887/); [Meta Newsroom, Muse launch](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)

### Inferences
- Meta shows two moves beyond the training default: chat-to-ads use without opt-out, and EU regulators pushing it to an objection model rather than stopping it.
- The fact that Muse comes with a toggle (default on) suggests consumer expectations or regulation are pushing even Meta toward visible controls, though not toward opt-in.

### Gaps
- No US opt-out for Meta AI chat training was found.
- The DPC's October 2025 efficacy report was not found.
- Retention and human review for Meta AI chats were not found.

---

## Q5. Microsoft: consumer Copilot training policy and opt-out

### Takeaway
Microsoft announced default training on consumer Copilot, Bing and MSN data in August 2024, with an opt-out from October 2024. It excluded the EEA at launch and still excludes several countries. Human review cannot be opted out of. Microsoft was a late adopter of the default, before Anthropic.

### Cited Findings
- **Announcement (16 Aug 2024).** Microsoft would offer opt-out controls in October and would not train until at least 15 days after notifying users. It would not offer the setting or train on consumer data from the EEA "until further notice" — [Microsoft Copilot blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/2024/08/16/transparency-and-control-in-consumer-data-use/) [search extract; 403]; confirmed by [The Decoder, 17 Aug 2024](https://the-decoder.com/microsoft-will-start-training-ai-models-with-user-data-from-copilot-bing-and-msn-in-october) (secondary), which calls it "opt-out rather than… opt in".
- **Current policy (FAQ; the section applies to the older app).**
  - "Except for certain categories of users or users who have opted out, Microsoft uses data from Bing, MSN, Copilot, and interactions with ads on Microsoft for AI training… including the images or files you upload."
  - Excluded: organisational Entra ID users, signed-in under-18s, signed-out users, users who opted out, and "Users in Brazil, China (excluding Hong Kong), Israel, Nigeria, South Korea, and Vietnam".
  - "By default, we store conversation activity for 18 months."
  - "Some Copilot conversations are subject to both automated and human review… an opt-out of human review is not available."
  - Microsoft 365 Copilot conversations "are not used to train."
  - A new app has been available since 18 Aug 2026.
  - Source: [Privacy FAQ for Microsoft Copilot](https://support.microsoft.com/en-us/topic/privacy-faq-for-microsoft-copilot-27b3a435-8dc9-4b55-9a4b-58eeb9647a7f)
- **Controls.** Privacy > "Training on conversation activity" and "Training on voice conversations". Opting out affects future conversations — [Microsoft Copilot privacy controls](https://support.microsoft.com/en-us/topic/microsoft-copilot-privacy-controls-8e479f27-6eb6-48c5-8d6a-c134062e2be6)

### Inferences
- The EEA is absent from the current exclusion list, which suggests EEA consumers may now be included. No Microsoft statement confirming this was found.

### Gaps
- When and whether EEA/UK training began is not verified.
- Data-handling terms of the new Copilot app (from 18 Aug 2026) were not reviewed.

---

## Q6. xAI (Grok): X posts used for training; Irish DPC inquiry

### Takeaway
X opted users' posts and Grok interactions into training by default in mid-2024. The Irish DPC took X to the High Court in August 2024, which led to a suspension for EU data. It opened a formal GDPR inquiry on 11 April 2025, which was still ongoing at the 2025 annual report. Grok's own app uses an opt-out toggle.

### Cited Findings
- **Default opt-in on X.** The EFF wrote: "Without notice, X has opted all users into training its 'Grok' AI Model". The setting covered "posts, interactions, inputs, and results" — [EFF on X, July 2024](https://x.com/EFF/status/1816895089245061262) [search extract]
- **DPC, 8 Aug 2024.** X agreed "to suspend its processing of the personal data contained in the public posts of X's EU/EEA users which it processed between 7 May 2024 and 1 August 2024, for the purpose of training its AI 'Grok'". This came after an urgent Section 134 High Court application — [DPC press release](https://www.dataprotection.ie/en/news-media/press-releases/dpc-welcomes-xs-agreement-suspend-its-processing-personal-data-purpose-training-ai-tool-grok). The proceedings were later struck out, with X undertaking to keep to the suspension — [DPC](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-welcomes-conclusion-proceedings-relating-xs-ai-tool-grok) [search extract]
- **DPC inquiry, 11 Apr 2025.** The inquiry concerns "the processing of personal data comprised in publicly-accessible posts posted on the 'X' social media platform by EU/EEA users, for the purposes of training generative artificial intelligence models, in particular the Grok Large Language Models". It examines "lawfulness and transparency" and was opened under Section 110 of the Data Protection Act 2018 against X Internet Unlimited Company — [DPC](https://www.dataprotection.ie/en/news-media/latest-news/data-protection-commission-announces-commencement-inquiry-x-internet-unlimited-company-xiuc). The DPC's 2025 annual report adds purpose limitation to its scope — [DPC Annual Report 2025](https://www.dataprotection.ie/sites/default/files/uploads/2026-06/DPC-Annual-Report-2025-Digital-AW.pdf) [search extract]
- **noyb (Aug 2024).** GDPR complaints in nine countries over Grok training — [noyb](https://noyb.eu/en/twitters-ai-plans-hit-9-more-gdpr-complaints) [search extract]
- **Grok app.**
  - Opt-out via Settings > Data Controls > "Improve the model" (app) or Settings > Data (web).
  - Private Chat is excluded.
  - In some regions outside the EU/UK, logged-out users cannot opt out.
  - Feedback may be used even after opt-out.
  - "a limited number of authorized personnel may review your conversations with Grok… including improving model performance".
  - Source: [xAI Consumer FAQ](https://x.ai/legal/faq) [search extract; 403]
  - The API is not trained on "without your explicit permission" — [xAI API FAQ](https://docs.x.ai/developers/faq/security) [search extract]

### Inferences
- Like Meta, X's EU retreat was forced by a regulator (a High Court application). The underlying consumer default elsewhere stayed opt-out.

### Gaps
- No final DPC decision on Grok training was found.
- xAI's consumer retention period is not verified.
- A claim, made in a Grok reply on X, that the 15 Jan 2026 X terms remove the opt-out is unverified and not used.
- xAI's 2026 legal pages appear under a SpaceX-related corporate name in search results; this was not verified.

---

## Q7. Anthropic: the exact policy before and after the Aug–Oct 2025 change; toggle default; retention; deadlines

### Takeaway
Until 7 October 2025, Anthropic's consumer documents committed not to train on consumer chats unless the user opted in, gave feedback, or was flagged by safety review. From 8 October 2025 it trains unless users opt out. Existing users met the choice in a pop-up whose training toggle was pre-set to "On". Retention for opted-in data rose from 30 days to up to 5 years. On the record, Anthropic was the **last major US lab to converge on the industry default, not a leader**.

### Cited Findings
- **Before (privacy policy, effective 19 Feb 2025).** "We will not use your Inputs or Outputs to train our models, unless: (1) your conversations are flagged for Trust & Safety review (in which case we may use or analyze them to improve our ability to detect and enforce our Usage Policy, including training models for use by our Trust and Safety team, consistent with Anthropic's safety mission), or (2) you've explicitly reported the materials to us (for example via our feedback mechanisms), or (3) you've otherwise explicitly opted in to the use of your Inputs and Outputs for training purposes." — [Anthropic Privacy Policy, effective 19 Feb 2025 (Anthropic legal archive)](https://www.anthropic.com/legal/archive/a2eecf43-807a-4a53-89dd-04c44c351138)
  - The same "will not use your Inputs or Outputs to train our models, unless…" commitment appears in versions effective 4 Mar 2024, 1 May 2024, 13 May 2024, 5 Jun 2024 and 17 Dec 2024 — e.g. [effective 4 Mar 2024](https://www.anthropic.com/legal/archive/cf9213dc-642f-43ff-bb0b-f07e10eb0d9f); [effective 17 Dec 2024](https://www.anthropic.com/legal/archive/fb6e63a8-fdd2-46fa-baf1-0fba326971a0)
  - Consumer Terms effective 1 May 2025: "We will not train our models on any Materials that are not publicly available, except in two circumstances" (feedback; trust-and-safety flags) — [Anthropic Consumer Terms, effective 1 May 2025 (archive)](https://www.anthropic.com/legal/archive/80e847ae-5c9e-4a7b-b2cb-88895aa972d5)
- **Announcement (28 Aug 2025).**
  - Framed as: "We're now giving users the choice to allow their data to be used to improve Claude."
  - Covers Claude Free, Pro and Max, including Claude Code from those accounts.
  - Does **not** apply to Claude for Work, Claude Gov, Claude for Education or API use, including Amazon Bedrock and Google Cloud Vertex AI.
  - "We are also extending data retention to five years, if you allow us to use your data for model training"; otherwise the 30-day retention continues.
  - "These updates will apply only to new or resumed chats and coding sessions."
  - "If you delete a conversation with Claude it will not be used for future model training."
  - Uses "a combination of tools and automated processes to filter or obfuscate sensitive data."
  - The current text says existing users "have until October 8, 2025" to choose.
  - Source: [Anthropic, "Updates to Consumer Terms and Privacy Policy"](https://www.anthropic.com/news/updates-to-our-consumer-terms)
- **Default state of the toggle (third-party).**
  - The pop-up reads "Updates to Consumer Terms and Policies" with "a big black 'Accept' button".
  - "In smaller print below that… 'Allow the use of your chats and coding sessions to train and improve Anthropic AI models,' with a toggle on / off switch next to it. It's automatically set to 'On.'"
  - "For users that click 'Accept' now, Anthropic will immediately begin training its models on their data and keeping said data for up to five years."
  - Users could defer with "Not now" until the deadline.
  - Source: [The Verge, Hayden Field, 28 Aug 2025](https://www.theverge.com/anthropic/767507/anthropic-user-data-consumers-ai-models-training-privacy) (secondary). Anthropic's own post does not state the default.
- **Deadline (one extension found).** The original pop-up said the update "will take effect on September 28, 2025" — [The Verge](https://www.theverge.com/anthropic/767507/anthropic-user-data-consumers-ai-models-training-privacy). The live Consumer Terms read "Effective October 8, 2025" — [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms) — and the announcement now cites 8 Oct 2025 — [Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms). Many outlets reported the 28 Sep deadline, e.g. [Slashdot quoting The Verge](https://tech.slashdot.org/story/25/08/28/1643241) (secondary).
- **After (operative text).**
  - Consumer Terms effective 8 Oct 2025: "We may use Materials to… develop other products and services, including training our models, unless you opt out of training through your account settings. Even if you opt out, we will use Materials for model training when: (1) you provide Feedback… or (2) your Materials are flagged for safety review" — [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
  - Privacy Policy effective 10 Sep 2026: "We may use your Inputs and Outputs to train and improve Anthropic AI models, unless you opt out through your account settings" — [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
- **Retention and scope now (privacy centre).**
  - With Model Improvement on: "we may retain your data in a de-identified format for up to 5 years in our model training pipelines."
  - Deleted conversations: "Deleted from our back-end storage systems within 30 days."
  - Safety-flagged content: "We retain inputs and outputs for up to 2 years and trust and safety classification scores for up to 7 years."
  - Feedback: kept 5 years.
  - Source: [Anthropic Privacy Center, "How long do you store my data?" (updated 1 Jul 2026)](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)
  - "Your Incognito chats are not used to improve Claude, even if you have enabled Model Improvement." Training data "includes the entire related conversation" but excludes "raw content from connectors (e.g. Google Drive)" — [Anthropic Privacy Center, "Is my data used for model training?" (updated 16 Mar 2026)](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- **Advertising (favourable to Anthropic).** "Claude will remain ad-free. Our users won't see 'sponsored' links adjacent to their conversations with Claude; nor will Claude's responses be influenced by advertisers" — [Anthropic, "Claude is a space to think", 4 Feb 2026](https://www.anthropic.com/news/claude-is-a-space-to-think)
- **Books (unfavourable).** Anthropic downloaded works from the pirate libraries LibGen and PiLiMi and settled for $1.5 billion (see Q10) — [court-approved settlement notice](https://assets-us-01.kc-usercontent.com:443/1eeb16db-4934-006e-40a6-38fa91285ebb/ce109a57-390c-4d76-ad65-5807d4830fe5/ANT%20-%20Long-Form%20Notice_Updated%20Deadline%201.8.2026.pdf)

### Inferences
- **Late convergence, not leadership.** OpenAI (2023), Google (2023), Meta (2023), X/xAI (2024) and Microsoft (2024) all trained on consumer chats by default first. Anthropic's change in October 2025 brought it to the existing industry default.
  - Some details are more protective than peers': deleted chats are excluded, there are Incognito chats, its documentation does not describe human review of chats for training (absence of evidence, not evidence of absence), and it has pledged no ads.
  - Others are less protective, and should be stated plainly: the pre-checked toggle in a pop-up with a dominant "Accept" button, retention extended from 30 days to five years, and Claude Code sessions included.
- **Anthropic's framing versus its terms.** The announcement calls the change "giving users the choice", but its own terms describe an opt-out ("unless you opt out"). The Verge documented a default of "On".
- **The five-year period is a cap.** It applies to de-identified training-pipeline copies, not to visible chat history. It is therefore not directly comparable with Google's 18-month auto-delete or with OpenAI's chats, which persist until deleted (no default auto-delete period was found).

### Gaps
- No official Anthropic notice explaining the move from 28 Sep to 8 Oct 2025 was found. Only one extension is evidenced; the caller's "extensions" (plural) is not confirmed.
- The opt-out or opt-in rates for consumers are not public.
- Whether Anthropic's EU AI Act training-content summaries tick "Yes" for user data was not found.
- Whether any regional (e.g. EU) default differed was not found.

---

## Q8. Mistral (Le Chat / "Vibe")

### Takeaway
Mistral, an EU company, also trains on individual consumers' chats by default with an opt-out, and excludes enterprise customers by default. Default-on training is therefore not only a US or Chinese practice.

### Cited Findings
- "Input and output data are used by default to train our artificial intelligence models, unless you opt out of training"; "Enterprise customers are opted out of training by default." Thumbs-up/down ratings with a comment "authorize[s] us to use your rating, your input and output" — [Mistral help, page dated 31 Aug 2026](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)
- Individual users are "not opted out by default".
  - Web: toggle "Allow your interactions to be used to train our models".
  - Mobile: "Enable data sharing".
  - Teams admins can opt out the whole organisation.
  - Studio and API have a separate toggle, "Anonymous improvement data".
  - Source: [Mistral help, page dated 3 Sep 2026](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)
- Memories prompts on Free, Pro and Student plans "may be used to train our models"; Team and Enterprise are opted out of Memories training by default — [search extract summarising Mistral help/docs](https://docs.mistral.ai/vibe/chat-legacy/memories) [search extract]

### Gaps
- The date Le Chat began default training, retention periods, and whether the product rename to "Vibe" is complete were not established.

---

## Q9. Chinese assistants: DeepSeek, Alibaba Qwen, Moonshot Kimi, ByteDance Doubao

### Takeaway
All four privacy policies allow training on (de-identified) user inputs by default with an opt-out, and all store data in the PRC. This matches the national standard TC260-003, which mandates an opt-out (≤4 clicks), not an opt-in. Opt-out paths vary: Doubao has an in-app toggle, while Kimi, DeepSeek and Qwen (for text) require contacting the company. DeepSeek's EU AI Act summary for its V4 model says no user data was used, despite the permissive policy.

### Cited Findings
- **DeepSeek (policy last updated 10 Feb 2026).**
  - "User Input" (prompts, uploaded files, chat history) is used "To improve and develop the Services and to train and improve our technology, such as our machine learning models and algorithms."
  - Users have "the right to opt-out of using your Personal Data for training our models or optimizing our technologies."
  - "we directly collect, process and store your Personal Data in People's Republic of China."
  - Data is retained "for as long as you have an account."
  - Source: [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)
  - The model disclosure says: "If user input is used to construct training data, we apply secure encryption, strict de-identification, and anonymization… Users are also given the right to opt out" — [DeepSeek model/algorithm disclosure](https://cdn.deepseek.com/policies/en-US/model-algorithm-disclosure.html)
  - **However**, DeepSeek's EU AI Act summary for DeepSeek-V4 (placed on the market 24 Apr 2026; summary last updated 4 Aug 2026) ticks **No** for "Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?" — [DeepSeek V4 Public Summary of Training Content](https://cdn.deepseek.com/policies/DeepSeek_Template_for_the_Public_Summary_of_Training_Content_for_GeneralPurpose_AI_model.pdf)
- **Kimi (Beijing Moonshot AI; policy effective 31 Aug 2026).**
  - "在经安全加密技术处理、严格去标识化且无法重新识别特定个人的前提下，平台可能会将用户的输入数据、指令及生成回复用于模型训练" — on condition of encryption and strict de-identification, inputs, instructions and replies may be used for model training.
  - Opt-out: email customer service; registered within 5–7 working days; account-level only; then covers historical and new data.
  - Data is stored "在位于中国境内…的服务器" — on servers in China.
  - Sources: [Kimi Help Centre, data usage](https://www.kimi.com/zh-hans/help/others/data-usage); [Kimi Privacy Policy](https://www.kimi.com/user/agreement/userPrivacy?version=v2), which states "我们将您的个人信息存储于中华人民共和国境内" (we store your personal information within the PRC).
- **Doubao (Beijing Chuntian Zhiyun Technology; policy updated 10 Sep 2026, effective 17 Sep 2026).**
  - For the personal edition, de-identified "内容数据" (inputs, instructions, replies) may be analysed and "用于模型训练" (used for model training).
  - Opt-out: "设置-隐私与权限-帮助模型改进效果" (Settings – Privacy & Permissions – Help improve model effectiveness).
  - Storage within the PRC.
  - Source: [Doubao Privacy Policy](https://www.doubao.com/legal/privacy)
- **Qwen / 千问 (Shanghai Zhixin Puhui Technology; policy updated 7 Nov 2025, effective 14 Nov 2025; read from a third-party mirror).**
  - "随机抽取少部分输入内容、对话上下文进行产品分析、模型评测和功能优化" — randomly samples a small portion of de-identified inputs and conversation context for product analysis, model evaluation and feature optimisation.
  - Text opt-out: contact the company per §9. Voice opt-out: toggle "改进语音服务" (improve voice service).
  - Knowledge-base content is not used for model training without separate consent.
  - Storage within the PRC.
  - Source: [Qwen product privacy policy (mirror on elawcn.com)](https://www.elawcn.com/agreement/2025/1127/1676.html)
- **Standard.** TC260-003 (29 Feb 2024) requires a convenient way to "turn off the use of their entered information for training purposes" (≤4 clicks), and that users be "clearly informed of the status of user input collection" — [CSET translation](https://cset.georgetown.edu/wp-content/uploads/t0588_generative_AI_safety_EN.pdf)

### Inferences
- Chinese regulation normalises the same opt-out-by-default architecture found in the US. Kimi's email-only opt-out arguably falls short of the standard's "convenient" example (≤4 clicks via an in-product option).
- The DeepSeek-V4 "No" shows that a permissive privacy policy is not proof that a given model was trained on chats. The EU template creates a model-level disclosure that can be checked.

### Gaps
- The official Qwen policy URL was not located (a mirror was used).
- Earlier (2023–2024) versions of these policies were not reviewed, so the dates these policies began are not established.

---

## Q10. Order of convergence; is "convergence on opt-out-by-default" fair; counter-examples (Oct 2026)

### Takeaway
"Convergence on opt-out-by-default for consumer chats, with institutional carve-outs" is a fair summary of the main US, EU and Chinese chatbot providers. Approximate order of the documented default:
1. OpenAI (≤ early 2023)
2. Google (Bard, 2023)
3. Meta (Sep 2023)
4. X/xAI (by mid-2024)
5. Microsoft (Oct 2024)
6. Anthropic (Oct 2025)

Apple and Proton's Lumo are genuine exceptions. EU regulators forced pauses and objection mechanisms but did not reverse the default.

### Cited Findings
- **OpenAI.** Default training was in place by March–April 2023: the Garante's training finding, and a history-off control that excluded chats from training — [Garante](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847) [search extract]; [OpenAI April 2023](https://openai.com/index/new-ways-to-manage-your-data-in-chatgpt/) [search extract]
- **Google.** Bard activity on, 18-month default, human review in 2023 — [Techzine](https://www.techzine.eu/news/applications/108995/eu-users-can-keep-conversations-with-google-bard-out-of-training-set/) (secondary) [search extract]. Today: "If you're 18 or over, Keep Activity is on by default" — [Google](https://support.google.com/gemini/answer/13278892)
- **Meta.** AI-feature interactions used "to improve our products" (27 Sep 2023) — [Meta](https://about.fb.com/news/2023/09/privacy-matters-metas-generative-ai-features/)
- **X/xAI.** EU posts processed 7 May – 1 Aug 2024 — [DPC](https://www.dataprotection.ie/en/news-media/press-releases/dpc-welcomes-xs-agreement-suspend-its-processing-personal-data-purpose-training-ai-tool-grok)
- **Microsoft.** Opt-out controls from October 2024; EEA excluded — [The Decoder](https://the-decoder.com/microsoft-will-start-training-ai-models-with-user-data-from-copilot-bing-and-msn-in-october) (secondary)
- **Anthropic.** No consumer training absent opt-in through the Consumer Terms of 1 May 2025 — [archive](https://www.anthropic.com/legal/archive/80e847ae-5c9e-4a7b-b2cb-88895aa972d5). Opt-out from 8 Oct 2025 — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- **Meta's own framing.** Meta presented its EU move as "following the example set by others including Google and OpenAI" — [Meta 14 Apr 2025](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/)
- **Counter-example: Apple.** "Your private personal data and interactions are never used to train our foundation models unless you explicitly choose to help improve them"; "We never use our users' private personal data or user interactions when training our foundation models" — [Apple Machine Learning Research (10 Jun 2024)](https://machinelearning.apple.com/research/introducing-apple-foundation-models)
- **Counter-example: Proton Lumo.** "Lumo doesn't use your conversations or inputs to train the large language model"; "Lumo doesn't keep any logs of your conversations server side" — [Proton, 23 Jul 2025](https://proton.me/blog/lumo-ai)
- **Partial counter-examples.**
  - Microsoft does not train in six named countries — [Microsoft FAQ](https://support.microsoft.com/en-us/topic/privacy-faq-for-microsoft-copilot-27b3a435-8dc9-4b55-9a4b-58eeb9647a7f)
  - Meta's ad use excludes the EU, UK and South Korea — [Reuters via TradingView](https://de.tradingview.com/news/reuters.com,2025:newsml_L6N3VH1DX:0-meta-to-use-ai-chats-to-personalize-content-and-ads-from-december)
  - DeepSeek-V4 declares no user-interaction training data — [DeepSeek V4 summary](https://cdn.deepseek.com/policies/DeepSeek_Template_for_the_Public_Summary_of_Training_Content_for_GeneralPurpose_AI_model.pdf)

### Inferences
- Among the major US labs, **Anthropic held out longest** (to 7 Oct 2025), followed by Microsoft (to Oct 2024). Apple still holds out (opt-in only).
- "Convergence" is accurate for the default, but should be qualified in three ways:
  1. It is two-tier: business, API, government and education customers are excluded everywhere.
  2. It has a regional exception: in the EU, objection rights, pauses and the AI Act user-data disclosure apply.
  3. The more consequential divergence in 2025–26 is **monetisation**. Meta (ads from chats, no opt-out) and OpenAI (contextual ads) go beyond training; Anthropic has publicly refused ads.
- Opt-out defaults are "harvesting" in effect because most users keep defaults. However, I found no company-published opt-out rates; that behavioural claim would need its own citation.

### Gaps
- No opt-out or uptake statistics for any company.
- Perplexity, DuckDuckGo Duck.ai, Character.AI and others were not reviewed.

---

## Q11. Legal and regulatory events treating chat logs or knowledge as an asset

### Takeaway
Courts and regulators have treated chat logs as discoverable evidence and data protection as enforceable, but outcomes in 2026 were mixed. NYT v. OpenAI forced months of indefinite log retention and production of 20 million de-identified chats. Italy's €15m fine on OpenAI was annulled in 2026 on jurisdictional grounds. Anthropic paid $1.5B over pirated books. Several governments restricted DeepSeek over data transfers to China.

### Cited Findings
- **Italy Garante v. OpenAI.**
  - Decision n. 755 of 2 Nov 2024, announced 20 Dec 2024: €15m fine plus a 6-month information campaign on radio, TV, newspapers and the internet (the first use of Art. 166(7) powers). Grounds included processing users' data to train ChatGPT without an adequate legal basis and failing to notify a March 2023 breach — [Garante press release, 20 Dec 2024](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432) [search extract]
  - The fine was overturned by an Italian court; Reuters reported it on 20 Mar 2026. The fine had been suspended in March 2025, and the Garante declined to comment — [Freevacy summarising Reuters](https://www.freevacy.com/news/reuters/italian-court-overturns-eur15m-gdpr-fine-against-openai/7241) (secondary)
  - The Tribunale di Roma judgment of 18 Mar 2026 annulled the decision on the GDPR one-stop-shop ground (Ireland's DPC as lead authority) without reaching the merits — [diritto.it](https://www.diritto.it/?p=249907) (secondary) [search extract]
- **NYT v. OpenAI log preservation.**
  - The 13 May 2025 order required OpenAI to "preserve and segregate all output log data that would otherwise be deleted". Judge Ona T. Wang lifted it by order of 9 Oct 2025, with no obligation for logs past 26 Sep 2025. OpenAI remained "required to retain logs linked to accounts specifically flagged by the New York Times", and logs already saved remain accessible — [Mashable via Yahoo News, 12 Oct 2025](https://www.yahoo.com/news/articles/judge-lifts-order-requiring-openai-151518813.html) (secondary)
  - OpenAI's Rule 72 objection (ECF 935, 10 Dec 2025, *In re OpenAI Copyright Infringement Litigation*, 1:25-md-03143) concerns orders "that required OpenAI to produce 20 million" de-identified consumer ChatGPT logs. The court had found "all 20 million conversations are relevant" — [OpenAI court filing](https://cdn.openai.com/pdf/2025-12-10-memorandum-of-law-dckt-935-0.pdf) (primary; party filing)
  - OpenAI later stated the district judge had ruled and that it had complied (16 Dec 2025 update) — [OpenAI](https://openai.com/index/response-to-nyt-data-demands/) [search extract]
- **Bartz v. Anthropic.**
  - "In June 2025, the district court ruled that using the books to train AI models was fair use… but left for trial the question whether downloading and use of works from LibGen and PiLiMi was fair use."
  - Class certified July 2025; trial set for December 2025.
  - $1.5 billion fund, "approximately $3,000 per work."
  - Anthropic must destroy the LibGen/PiLiMi books and copies.
  - Source: [court-approved Long-Form Notice](https://assets-us-01.kc-usercontent.com:443/1eeb16db-4934-006e-40a6-38fa91285ebb/ce109a57-390c-4d76-ad65-5807d4830fe5/ANT%20-%20Long-Form%20Notice_Updated%20Deadline%201.8.2026.pdf)
  - "On July 20, 2026, the Court granted final approval." First payments are expected "on or before November 15, 2026" — [settlement website](https://www.anthropiccopyrightsettlement.com/)
  - Bloomberg Law reports more than 480,000 works and about $122m for fees and costs — [Bloomberg Law](https://news.bloomberglaw.com/ip-law/anthropic-authors-1-5-billion-deal-receives-final-approval) (secondary) [search extract]
  - Judge Alsup called training "exceedingly transformative" — [Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/district-court-rules-ai-training-can-be-fair-use-in-bartz-v-anthropic) (secondary) [search extract]
- **Kadrey v. Meta (25 Jun 2025, Judge Chhabria).** Partial summary judgment for Meta on training as fair use, for these plaintiffs, for lack of market-harm evidence. The record shows Meta obtained LibGen and Anna's Archive by torrenting. The ruling "does not stand for the proposition that Meta's use… is lawful" — [Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/second-district-court-rules-ai-training-can-be-fair-use) (secondary) [search extract]; [Loeb & Loeb](https://www.loeb.com/en/insights/publications/2025/07/kadrey-v-meta-platforms-inc) (secondary) [search extract]
- **DeepSeek restrictions.**
  - Italy: on 30 Jan 2025 the Garante ordered urgent limitation of processing of Italian users' data by Hangzhou and Beijing DeepSeek. Findings included storage in China, an inadequate privacy policy and no EU representative — [Garante provvedimento 30 Jan 2025](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10098477) [search extract]
  - South Korea: on 24 Apr 2025 the PIPC found that user prompt contents were transferred to Beijing Volcano Engine (a ByteDance subsidiary) without consent. Service resumed on 28 Apr 2025 under a revised policy — [Korea Times](https://www.koreatimes.co.kr/amp/southkorea/globalcommunity/20250424/deepseek-transferred-korean-users-data-abroad-without-permission-govt) (secondary) [search extract]; [Korea Times](https://www.koreatimes.co.kr/amp/business/companies/20250428/deepseek-resumes-service-in-korea-after-disclosing-revised-info-processing-policy) (secondary) [search extract]
  - Australia: ban on federal government devices (Feb 2025) — [The Daily Aus](https://www.thedailyaus.com.au/latest/deepseek-to-be-banned-on-federal-government-devices) (secondary) [search extract]
  - US: Commerce Department bureaus banned it on government devices (Mar 2025) — [Reuters via The Edge Malaysia](https://theedgemalaysia.com/node/748331) (secondary) [search extract]
  - Germany: on 27 Jun 2025 the Berlin data protection commissioner asked Apple and Google to delist the app over unlawful transfers to China — [TechSpot](https://www.techspot.com/news/108512-germany-asks-apple-google-ban-deepseek-over-illegal.html) (secondary) [search extract]
- **noyb.** Meta (11 complaints, June 2024; cease-and-desist, 14 May 2025) and X/Grok (9 complaints, Aug 2024) — [noyb](https://noyb.eu/en/noyb-sends-meta-cease-and-desist-letter-over-ai-training-european-class-action-potential-next-step) [search extract]; [noyb](https://noyb.eu/en/twitters-ai-plans-hit-9-more-gdpr-complaints) [search extract]
- **2026 developments (summary).**
  - Elsevier, Cengage, Hachette, Macmillan, McGraw Hill and Scott Turow sued Meta in federal court in Manhattan (complaint filed 5 May 2026; reported 6 May 2026), alleging copying of "millions of books and journal articles" to train Llama — [Research Information](https://www.researchinformation.info/news/publishers-sue-meta-platforms-over-alleged-ai-training-piracy/) (secondary)
  - OpenAI ads: 16 Jan announcement, 9 Feb US test, 18 Aug Europe — [OpenAI](https://openai.com/index/chatgpt-ads-expands-across-europe/) [search extract]
  - Anthropic no-ads pledge, 4 Feb 2026 — [Anthropic](https://www.anthropic.com/news/claude-is-a-space-to-think)
  - Bartz final approval, 20 Jul 2026 — [settlement site](https://www.anthropiccopyrightsettlement.com/)
  - Rome tribunal annulment, Mar 2026 — [Freevacy/Reuters](https://www.freevacy.com/news/reuters/italian-court-overturns-eur15m-gdpr-fine-against-openai/7241)
  - Meta Muse training toggle default-on, Sep 2026 — [Meta help](https://www.meta.com/help/artificial-intelligence/1047255454427887/)
  - EU AI Act template user-data question (applies to general-purpose AI providers from 2 Aug 2025) — [Commission template](https://ec.europa.eu/newsroom/dae/redirection/document/118480)
  - Third-party grading of providers' summaries — [AIAL / Trinity College Dublin](https://aial.ie/research/gpai-training-transparency/)

### Inferences
- In the NYT case a court treated chat logs as evidence about how content is used. The preservation order overrode users' deletion choices for about four and a half months.
- The European enforcement record is weaker than the 2023–24 headlines implied: the only major GDPR fine on a chatbot (Garante–OpenAI) was annulled on jurisdiction. Leverage has come mainly from pauses and undertakings (Meta, X).

### Gaps
- The Oct 9, 2025 and May 13, 2025 orders were not read on PACER/CourtListener (rate-limited).
- Whether the Garante appealed the Rome ruling was not found.
- The full Bartz fair-use order text was not read; it is described via the court-approved notice and law-firm summaries.

---

## Q12. Scholarly content: publisher–AI licensing deals (2024–2026), author consultation and opt-outs

### Takeaway
From 2024, major scholarly and academic publishers monetised their backlists through AI licensing. Disclosed sums run to tens of millions of dollars: Taylor & Francis–Microsoft $10m+ (initial); Wiley $44m across two deals. Author consent ranged widely:
- none: Taylor & Francis, Wiley ("no opt-out");
- opt-out: Johns Hopkins University Press;
- opt-in: Cambridge University Press & Assessment, HarperCollins, Bloomsbury.

Since 2025 the deals have shifted toward retrieval and "AI search" integrations (Wiley–Anthropic MCP, Springer Nature–OpenEvidence, De Gruyter Brill–Consensus). Elsevier has chosen litigation rather than a disclosed training licence.

### Cited Findings
- **Tracker.** The Ithaka S+R Generative AI Licensing Agreement Tracker (last updated 7 Aug 2026) lists the deals below — [Ithaka S+R tracker](https://sr.ithaka.org/our-work/generative-ai-licensing-agreement-tracker/); [tracker spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
- **Taylor & Francis / Informa – Microsoft.**
  - "$10m+ for 'an initial data access'… with a recurring payment of an undisclosed sum… over the subsequent three years. Nonexclusive"; Ithaka notes it "seems to include books but not journals."
  - A further LLM data-licensing partner was disclosed in Informa's 2025 half-year Q&A. A "$75m" row for an "unnamed big tech firm" is listed without detail.
  - Source: [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
  - Authors "have not been told about the AI deal, were not given the opportunity to opt out and are receiving no extra payment" — [The Bookseller, 19 Jul 2024](https://thebookseller.com/news/academic-authors-shocked-after-taylor--francis-sells-access-to-their-research-to-microsoft-ai) (secondary)
- **Wiley.** "Wiley set to earn $44m from AI rights deals, confirms 'no opt-out' for authors" — [The Bookseller, 30 Aug 2024](https://thebookseller.com/news/wiley-set-to-earn-44m-from-ai-rights-deals-confirms-no-opt-out-for-authors) (secondary).
  - Split: $23m earned plus $21m expected; the deals mostly cover backlist content three years or older — [Books+Publishing](https://www.booksandpublishing.com.au/articles/2024/09/04/258068/wiley-expects-to-make-us44-million-from-ai-partnership-authors-unable-to-opt-out/) (secondary) [search extract]
  - Later Wiley partnerships: Perplexity (May 2025), AWS (May 2025), Anthropic MCP integration within the Claude for Education pilot (July 2025) — [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
- **Oxford University Press.** "We are actively working with companies developing large language models (LLMs) to explore options for both their responsible development and usage" — [Inside Higher Ed, 5 Aug 2024](https://www.insidehighered.com/news/quick-takes/2024/08/05/oxford-university-press-actively-working-ai-companies) (secondary). No deal terms or author opt-out were found.
- **Cambridge University Press & Assessment.** "contacting 20,000 authors to request their permission before licensing their content for the training and development of large language models" — [The Bookseller, 24 Oct 2024](https://www.thebookseller.com/news/cambridge-university-press--assessment-writes-to-20k-authors-for-ai-licensing-opt-in) (secondary). Ithaka records that only a "small minority" declined and that no public deal had yet been announced — [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
- **Johns Hopkins University Press (July 2025).**
  - "Authors have until the end of August to opt out of the licensing agreement. If they do not, their work will be used to help train AI models."
  - Executive director Barbara Kline Pope: "we are increasingly concerned, although not certain, that the major LLM companies already have our books."
  - Authors who opt out must sign an addendum saying their work "may suffer as a result of… the fact that Hopkins Press will not exercise AI Rights."
  - Source: [Baltimore Banner, 25 Jul 2025](https://www.thebanner.com/education/higher-education/johns-hopkins-press-artificial-intelligence-ai-llm-QKOMZUWMNBC4NLF63TNLPQHD2Q/) (secondary)
  - Ithaka records an estimated author royalty of "less than $100 per title per license" (unverified) — [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
- **De Gruyter Brill.** Expects deals with "several AI technology providers". Authors will receive a percentage share per title under existing contracts. Content "may be used for training and testing foundational large language models." Its August 2026 Consensus deal is explicitly not for training — [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml); [Consensus blog](https://consensus.app/home/blog/announcing-our-partnership-with-de-gruyter-brill/) (linked from the Ithaka tracker; not read directly)
- **Sage.** Said licensing would be a "preferable route" to having content illegally "harvested" — [The Bookseller, 19 Sep 2024](https://www.thebookseller.com/news/sage-confirms-it-is-in-talks-to-license-content-to-ai-firms) (secondary). Causaly deal (July 2026) covering 400+ life-science journals — [Research Information](https://www.researchinformation.info/news/sage-partners-with-causaly-to-bring-full-text-journals-into-ai-research-platform/) (secondary, via the Ithaka tracker)
- **Elsevier.** No disclosed LLM-training licence was found. Its library AI clause lets CC-BY open-access content be used for training, and closed content only with non-learning tools — [OST library, Elsevier AI clause](https://www.ost.ch/de/die-ost/services/bibliothek/e-medien/datenbanken-a-bis-z-der-bibliothek-ost/elsevier-ai-clause) [search extract]. It is a plaintiff against Meta (May 2026) — [Research Information](https://www.researchinformation.info/news/publishers-sue-meta-platforms-over-alleged-ai-training-piracy/)
- **Others (Ithaka tracker).**
  - HarperCollins–Microsoft: reported Nov 2024; opt-in; $5,000 per book split 50/50.
  - Bloomsbury: author opt-in with a 20% royalty (Aug 2025); a Google deal (Dec 2025).
  - NEJM–OpenEvidence (Feb 2025).
  - AAAS–ProRata pilot (Jan 2025).
  - Springer Nature–OpenEvidence (reported 5 Aug 2026; retrieval and citation).
  - Source: [Ithaka S+R tracker](https://docs.google.com/spreadsheets/d/e/2PACX-1vRJ8ZPFRAY6GKX_026vvtQk6ExJSbiI7X_xSrGDEdqdX1BPzAMZccRFe5mhdxck5YRwOlXg4pFY7LWm/pubhtml)
- **Context.** Nature news: "Has your paper been used to train an AI model? Almost certainly" (Elizabeth Gibney, 14 Aug 2024; title verified, body paywalled) — [Nature](https://www.nature.com/articles/d41586-024-02599-9) (secondary)

### Inferences
- The first wave of deals (2024) sold access to research for model training; academic authors were mostly not consulted, the main exception being CUP's opt-in. The second wave (2025–26) sells AI-integration and retrieval access, which keeps publishers as paid intermediaries. Both waves turn academic labour into a licensable data asset, with the publisher, not the author, holding the AI rights in most contracts.

### Gaps
- Informa and Wiley investor filings were not read directly. The Wiley FY2026 figure ($49m, from a secondary editorial) is unverified and not used.
- Terms of the OUP deals were not disclosed.
- De Gruyter Brill's author opt-out policy page could not be retrieved (404).

---

## Q13. Scholarly corpora documented in training sets (arXiv, PubMed Central, S2ORC, shadow libraries)

### Takeaway
Open scholarly corpora are explicitly documented in public training sets: arXiv in LLaMA and The Pile; PubMed Central, PhilPapers and NIH ExPorter in The Pile; S2ORC-derived peS2o in Dolma. Litigation has shown that frontier labs also used shadow libraries (LibGen, PiLiMi, Books3/Bibliotik, Anna's Archive). Publishers now allege that this included journal articles.

### Cited Findings
- **The Pile (Gao et al.).** PubMed Central 90.27 GiB (14.40% of the epoch-weighted mix); ArXiv 56.21 GiB (8.96%); Books3 100.96 GiB (12.07%), "derived from a copy of the contents of the Bibliotik private tracker"; PhilPapers 2.38 GiB; NIH ExPorter 1.89 GiB — [arXiv:2101.00027](https://arxiv.org/abs/2101.00027)
- **LLaMA (Touvron et al., Feb 2023).** ArXiv 2.5% of pre-training data (92 GB). "Gutenberg and Books3 [4.5%]… the Books3 section of ThePile" — [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)
- **Dolma (AI2, OLMo).** Semantic Scholar papers: 38.8M documents, about 70B tokens. peS2o is "a collection of approximately 40 million open-access academic papers… derived from the Semantic Scholar Open Research Corpus (S2ORC)" — [arXiv:2402.00159](https://arxiv.org/abs/2402.00159)
- **Anthropic.** Downloaded works from Library Genesis and Pirate Library Mirror "for purposes of training large language models". The class covers works with an ISBN or ASIN in those datasets — [Bartz settlement notice](https://assets-us-01.kc-usercontent.com:443/1eeb16db-4934-006e-40a6-38fa91285ebb/ce109a57-390c-4d76-ad65-5807d4830fe5/ANT%20-%20Long-Form%20Notice_Updated%20Deadline%201.8.2026.pdf)
- **Meta.** Obtained LibGen and Anna's Archive by torrenting (Kadrey record) — [Loeb & Loeb](https://www.loeb.com/en/insights/publications/2025/07/kadrey-v-meta-platforms-inc) (secondary) [search extract]. The 2026 publishers' complaint alleges Meta copied "millions of books and journal articles" — [Research Information](https://www.researchinformation.info/news/publishers-sue-meta-platforms-over-alleged-ai-training-piracy/) (secondary). Coverage says this was done via Anna's Archive, which indexes LibGen and Sci-Hub — [Bloomberg Law](https://news.bloomberglaw.com/litigation/meta-faces-new-ai-copyright-class-action-from-book-publishers) (secondary) [search extract]
- **LibGen size.** The Atlantic's LibGen search tool (March 2025) is reported to cover about 7.5 million books and 81 million research papers — [Publishers Lunch](https://lunch.publishersmarketplace.com/?p=94383) (secondary) [search extract]. The Atlantic article itself could not be read (403/paywall): [The Atlantic](https://www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093/). The settlement notice confirms authors can check "The Atlantic's list of LibGen files" — [Bartz notice](https://assets-us-01.kc-usercontent.com:443/1eeb16db-4934-006e-40a6-38fa91285ebb/ce109a57-390c-4d76-ad65-5807d4830fe5/ANT%20-%20Long-Form%20Notice_Updated%20Deadline%201.8.2026.pdf)

### Inferences
- Scholarly output entered models by three routes: open-access corpora (arXiv, PMC, S2ORC, used openly), licensed backlists (2024 deals), and shadow libraries (revealed in litigation). Licensing came after the scraping, which is consistent with JHUP's stated fear that "the major LLM companies already have our books".

### Gaps
- Whether LibGen's journal-article collection (scimag, which mirrors Sci-Hub) was ingested by any lab is alleged (Elsevier v. Meta) but not established in a ruling.
- OpenAI's "Books1/Books2" composition is undisclosed.

---

## Implications for the paper

### Takeaway
The convergence claim holds, but Anthropic is the **endpoint**, not the vanguard. It was the last major US lab to adopt default training on consumer chats (October 2025), years after OpenAI, Google, Meta, X and Microsoft. OpenAI is the better single illustration of the trajectory; Meta is the better illustration of chat data as an advertising asset. Anthropic is best used as "even the holdout converged".

### Cited Findings
- Anthropic committed not to train on consumer chats absent opt-in until its 1 May 2025 terms — [archive](https://www.anthropic.com/legal/archive/80e847ae-5c9e-4a7b-b2cb-88895aa972d5). Opt-out from 8 Oct 2025, with the toggle pre-set "On" — [Consumer Terms](https://www.anthropic.com/legal/consumer-terms); [The Verge](https://www.theverge.com/anthropic/767507/anthropic-user-data-consumers-ai-models-training-privacy)
- OpenAI had default training plus opt-out by 2023 — [Garante 28 Apr 2023](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9881490) [search extract]. Conversation-matched ads from 2026 — [OpenAI](https://openai.com/index/our-approach-to-advertising-and-expanding-access/) [search extract]. 20 million chat logs ordered produced in litigation — [OpenAI ECF 935](https://cdn.openai.com/pdf/2025-12-10-memorandum-of-law-dckt-935-0.pdf)
- Meta uses AI chats for ad personalisation with no opt-out from 16 Dec 2025 — [Meta](https://about.fb.com/news/2025/10/improving-your-recommendations-apps-ai-meta/); [Reuters via TradingView](https://de.tradingview.com/news/reuters.com,2025:newsml_L6N3VH1DX:0-meta-to-use-ai-chats-to-personalize-content-and-ads-from-december)
- Business, API, government and education exclusions are universal — e.g. [OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) [search extract]; [Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms); [Google Education](https://blog.google/products-and-platforms/products/education/gemini-enterprise-grade-data-protection/) [search extract]
- China's standard codifies opt-out — [TC260-003](https://cset.georgetown.edu/wp-content/uploads/t0588_generative_AI_safety_EN.pdf)

### Inferences
- **Most defensible one-paragraph wording:**
  > "Between 2023 and 2025 the leading consumer AI assistants converged on a common data regime: conversations from individual users are training data by default, subject at most to an opt-out, while paying institutional customers (enterprise, API, government and education) are contractually excluded. OpenAI and Google adopted this default in 2023, Meta and X followed, Microsoft joined in late 2024, and Anthropic — the last major US developer to promise not to train on consumer chats — switched to an opt-out default in October 2025, extending retention for consenting users to five years. China's national cybersecurity standards committee (TC260) prescribes the same opt-out architecture in its 2024 technical document on generative-AI security, and the French firm Mistral operates it too. Some firms now go further and treat conversations as commercial signal: Meta has used AI chats to personalise ads since December 2025 without an opt-out, and OpenAI began matching ads to conversation context in 2026. Exceptions exist (Apple's opt-in model, Proton's no-training Lumo, EU objection rights won by regulators) but they are marginal in market share. The result is a two-tier knowledge economy: institutions can buy their way out, while individual scholars on personal accounts become, by default, unpaid contributors to proprietary models — alongside the published literature that publishers have licensed to the same firms and that litigation shows was also taken from shadow libraries."
- **Which example to use.**
  - Anthropic is apt for the narrow claim that even the most privacy-differentiated US lab converged. It is inaccurate as an example of a company leading the trend.
  - Anthropic is also apt for the "knowledge as asset" point via Bartz ($1.5B over LibGen/PiLiMi books).
  - It cuts against the monetisation point: it pledged no ads in February 2026.
  - If the paper keeps Anthropic as the lead example, it should say "late convergence" explicitly. The default-on pop-up toggle and the five-year retention are fair criticisms.
  - For the broader "trajectory" claim, OpenAI (first mover, scale, ads, court-ordered log retention) is the stronger primary example. Meta is the strongest example of chats turned directly into ad inputs.

### Gaps
- The claim that most users never change defaults needs a separate empirical citation; no company publishes opt-out rates.
- Market-share figures to support "marginal" exceptions were not researched here.
