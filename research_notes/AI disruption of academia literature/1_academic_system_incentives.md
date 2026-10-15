# Section 1: How the current academic system works, its incentive structure and its known pathologies (annotated bibliography)

Verification method: every DOI below was resolved against the Crossref API (title, authors, venue, year, volume and pages were checked), and the summaries were checked against abstracts from Crossref, Semantic Scholar, Europe PMC or the publisher page where one was available. Where a summary relies on my prior knowledge of the work rather than an abstract I fetched in this session, it is marked **[content from prior knowledge, not re-fetched]**, so the writer knows to spot-check any specific number before quoting it.

Stance codes:
- **S** supports the thesis that the system was already fragile or distorted before AI.
- **N** nuances it.
- **C** challenges it.

---

## Q1. How do publish-or-perish, peer review, journal prestige and quantitative metrics (citations, h-index, JIF, national points systems) shape researcher behaviour?

### Takeaway
There is strong empirical evidence that metric-based evaluation changes what researchers do, and the changes follow the metric's design:
- Australia's publication-count formula raised output volume.
- Italy's citation thresholds in the ASN raised self-citation and national citation "inwardness".
- Chinese cash-per-paper rewards reached up to USD 165,000 per paper.
- Poland's points and publisher lists redirected where people publish.

The literature is not one-sided, though. Polish data show that clear, stable incentives raised output with no measurable drop in quality, and Spanish evidence warns against attributing too much to the evaluation system.

### Cited Findings

**Foundational and seminal works**

1. **Merton, R. K. (1968). The Matthew Effect in Science. *Science*, 159(3810), 56–63.** https://doi.org/10.1126/science.159.3810.56
   - The classic account of cumulative advantage: credit flows disproportionately to scientists who are already eminent. It is the baseline sociological description of how reward and recognition work in science.
   - **S/N**: it shows that status-based distortion is old and structural, not new. — [Crossref/DOI](https://doi.org/10.1126/science.159.3810.56)

2. **de Solla Price, D. J. (1963). *Little Science, Big Science*. New York: Columbia University Press.** https://doi.org/10.7312/pric91844
   - The founding scientometric work. It established the exponential growth of the scientific literature and of the scientific workforce (doubling roughly every 10–15 years) and predicted that this growth must saturate. **[content from prior knowledge, not re-fetched; DOI and title verified]**
   - **S**: it anticipated that growth cannot be sustained. — [DOI](https://doi.org/10.7312/pric91844)

3. **Seglen, P. O. (1997). Why the impact factor of journals should not be used for evaluating research. *BMJ*, 314(7079), 497.** https://doi.org/10.1136/bmj.314.7079.497
   - The canonical critique of the JIF. Citations within a journal are highly skewed, so a journal's impact factor is not representative of its individual articles. **[content from prior knowledge, not re-fetched]**
   - **S**. — [DOI](https://doi.org/10.1136/bmj.314.7079.497)

**National performance-based systems**

4. **Hicks, D. (2012). Performance-based university research funding systems. *Research Policy*, 41(2), 251–261.** https://doi.org/10.1016/j.respol.2011.09.007
   - A comparative review of national performance-based research funding systems (PRFS), such as the UK RAE/REF and systems in Australia and Poland. It argues that PRFS are now widespread, that they work mainly by distributing prestige rather than money, and that they carry costs to equity and diversity. **[content from prior knowledge, not re-fetched]**
   - **S/N**. — [DOI](https://doi.org/10.1016/j.respol.2011.09.007)

5. **Butler, L. (2003). Explaining Australia's increased share of ISI publications—the effects of a funding formula based on publication counts. *Research Policy*, 32(1), 143–155.** https://doi.org/10.1016/S0048-7333(02)00007-0
   - The classic natural experiment. After Australia tied funding to raw publication counts, its share of ISI papers rose, but its relative citation impact fell, with the growth concentrated in lower-impact journals. **[content from prior knowledge, not re-fetched]**
   - **S**: a textbook Goodhart case. — [DOI](https://doi.org/10.1016/S0048-7333(02)00007-0)

6. **Wilsdon, J. et al. (2015). *The Metric Tide: Report of the Independent Review of the Role of Metrics in Research Assessment and Management*. HEFCE.** https://www.ukri.org/publications/review-of-metrics-in-research-assessment-and-management/ (UKRI page verified, HTTP 200). ResearchGate DOI: 10.13140/RG.2.1.4929.1363.
   - The UK government-commissioned review for the REF. It recommended "responsible metrics" and found that metrics cannot replace peer review in the REF. **[content from prior knowledge, not re-fetched]**
   - **N**: it neither defends metrics nor rejects them; it argues for limited, responsible use. — [UKRI](https://www.ukri.org/publications/review-of-metrics-in-research-assessment-and-management/)

7. **Hicks, D., Wouters, P., Waltman, L., de Rijcke, S., & Rafols, I. (2015). Bibliometrics: The Leiden Manifesto for research metrics. *Nature*, 520(7548), 429–431.** https://doi.org/10.1038/520429a
   - Ten principles for responsible use of metrics. It is a response to misuse of the JIF and h-index in evaluation.
   - **S/N**: it concedes that misuse is widespread but defends quantitative evaluation when used properly. — [DOI](https://doi.org/10.1038/520429a)

**Poland (ministerial points)**

8. **Kulczycki, E., Korzeń, M., & Korytkowski, P. (2017). Toward an excellence-based research funding system: Evidence from Poland. *Journal of Informetrics*, 11(1), 282–298.** https://doi.org/10.1016/j.joi.2017.01.001
   - An analysis of the Polish parametric evaluation and its points-based categorisation of institutions. **[content from prior knowledge, not re-fetched]**
   - **N**. — [DOI](https://doi.org/10.1016/j.joi.2017.01.001)

9. **Korytkowski, P., & Kulczycki, E. (2019). Examining how country-level science policy shapes publication patterns: the case of Poland. *Scientometrics*, 119(3), 1519–1543.** https://doi.org/10.1007/s11192-019-03092-1
   - Data: 452,277 publications submitted to Poland's evaluation system, 2009–2016.
   - Evaluation, promotion rules and grants increased the share of articles in impact-factor journals, with no decline in quality as measured by a bibliometric indicator.
   - Only clear and stable incentives changed behaviour. Book publishing, where the rules were unstable, did not respond.
   - **N/C**: incentives work as designed and need not degrade quality. — [Search summary of abstract](https://ideas.repec.org/a/spr/scient/v119y2019i3d10.1007_s11192-019-03092-1.html)

10. **Dzięgiel, G., Kulczycki, E., Maziarczyk, A., & Korytkowski, P. (2024/2025). The impact of a publisher list on publication patterns: evidence from Poland. *Research Evaluation*, 34, rvaf018.** https://doi.org/10.1093/reseval/rvaf018
    - After the Polish Publisher List was introduced in 2019, the number of monographs from non-listed publishers "declined considerably" and authors moved toward international publishers.
    - The authors describe the list as "a powerful policy tool" that produced "a strategic shift in publishing decisions".
    - **S**: researchers re-optimise to whatever list the ministry publishes. — [Crossref abstract](https://doi.org/10.1093/reseval/rvaf018)

**Spain (sexenios, CNEAI/ANECA)**

11. **Jiménez-Contreras, E., de Moya Anegón, F., & López-Cózar, E. D. (2003). The evolution of research activity in Spain: The impact of the National Commission for the Evaluation of Research Activity (CNEAI). *Research Policy*, 32(1), 123–142.** https://doi.org/10.1016/S0048-7333(02)00008-2
    - The core study linking the 1989 sexenio salary-bonus system to growth in Spanish international (ISI) publications. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1016/S0048-7333(02)00008-2)

12. **Osuna, C., Cruz-Castro, L., & Sanz-Menéndez, L. (2011). Overturning some assumptions about the effects of evaluation systems on publication performance. *Scientometrics*, 86(3), 575–592.** https://doi.org/10.1007/s11192-010-0312-7
    - Using a quasi-experimental approach, it challenges the claim that the sexenio system caused Spain's publication growth, and calls for caution in attributing effects to evaluation systems.
    - **C/N**. — [Working paper abstract via IDEAS](https://ideas.repec.org:443/p/ipp/wpaper/1010.html)

**Italy (ASN)**

13. **Seeber, M., Cattaneo, M., Meoli, M., & Malighetti, P. (2019). Self-citations as strategic response to the use of metrics for career decisions. *Research Policy*, 48(2), 478–491.** https://doi.org/10.1016/j.respol.2017.12.004
    - Sample: 886 Italian scientists, 2002–2014.
    - Introducing the ASN, which ties habilitation to publication and citation counts, was associated with "a strong and significant increase in self-citations", especially among those who stood to benefit most.
    - **S**. — [Semantic Scholar abstract](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.respol.2017.12.004)

14. **Baccini, A., De Nicolao, G., & Petrovich, E. (2019). Citation gaming induced by bibliometric evaluation: A country-level comparative analysis. *PLOS ONE*, 14(9), e0221212.** https://doi.org/10.1371/journal.pone.0221212
    - After the 2010–2011 reforms, Italy became the G10 country with "the highest inwardness" (share of citations coming from the same country) and the lowest international collaboration rate.
    - The authors attribute this to "a generalized strategic use of citations". They present this as the most likely explanation, inferred rather than directly observed.
    - **S**. — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0221212)

**China (cash-per-paper and the 2020 reform)**

15. **Quan, W., Chen, B., & Shu, F. (2017). Publish or impoverish: An investigation of the monetary reward system of science in China (1999–2016). *Aslib Journal of Information Management*, 69(5), 486–502.** https://doi.org/10.1108/AJIM-01-2017-0014
    - Based on 168 policy documents from 100 Chinese universities.
    - Cash rewards for Web of Science papers ranged from USD 30 to USD 165,000, and the average reward rose over the decade.
    - **S**. — [Crossref abstract](https://doi.org/10.1108/AJIM-01-2017-0014)

16. **Franzoni, C., Scellato, G., & Stephan, P. (2011). Changing incentives to publish. *Science*, 333(6043), 702–703.** https://doi.org/10.1126/science.1197286
    - Shows that cash-bonus and career incentives across countries (e.g., China, Korea, Turkey) are associated with more submissions to *Science*, while acceptance rates do not rise correspondingly. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1126/science.1197286)

17. **Abritis, A., & McCook, A. (2017). Cash bonuses for peer-reviewed papers go global. *Science* (news), doi:10.1126/science.aan7214.** https://doi.org/10.1126/science.aan7214
    - Journalism (Science/Retraction Watch) documenting that cash-per-paper schemes exist well beyond China. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1126/science.aan7214)

18. **Zhang, L., & Sivertsen, G. (2020). The new research assessment reform in China and its implementation. *Scholarly Assessment Reports*, 2(1), 3.** https://doi.org/10.29024/sar.15
    - Describes China's 2020 policy against "SCI-worship", which ended cash-per-paper rewards and the use of SCI and JIF as the main evaluation criteria. **[content from prior knowledge, not re-fetched]**
    - **S/N**: the state itself acknowledged the distortion and reformed. — [DOI](https://doi.org/10.29024/sar.15)

### Inferences
- Across five national cases (Australia, Spain, Poland, Italy, China), researchers respond quickly and precisely to whatever is counted. This is the empirical core of a "fragile baseline" argument, and it sets up the point that AI lowers the cost of producing exactly what is counted: papers, citations, reviews.
- The strongest counterweight is Korytkowski & Kulczycki (2019) together with Osuna et al. (2011): incentives do not necessarily degrade quality, and their effects can be overstated.

### Gaps
- I did not verify a recent peer-reviewed study specifically on sexenios after the 2023–2024 ANECA/CNEAI criteria reform. This needs a targeted search.
- I did not verify a peer-reviewed study of "REF gaming", such as hiring stars just before the census date or impact case study inflation. The Metric Tide is the policy anchor. Derek Sayer's *Rank Hypocrisies* (2015) could not be verified via Crossref in this session.

---

## Q2. Goodhart's/Campbell's law in science: key theoretical and empirical works

### Takeaway
A coherent literature argues that selection on publication counts and metrics evolves bad methods even without conscious cheating (Smaldino & McElreath) and that every major metric has lost validity through over-optimisation (Fire & Guestrin). The book-length treatments are Muller and Biagioli & Lippman. Fanelli's work is the main empirical counterweight.

### Cited Findings

19. **Smaldino, P. E., & McElreath, R. (2016). The natural selection of bad science. *Royal Society Open Science*, 3(9), 160384.** https://doi.org/10.1098/rsos.160384
    - A 60-year meta-analysis shows statistical power in behavioural science has not improved.
    - An agent-based model shows that when publication drives career advancement, poor methods are selected for. This "requires no conscious strategizing—no deliberate cheating nor loafing".
    - **S**. — [Crossref abstract](https://doi.org/10.1098/rsos.160384)

20. **Higginson, A. D., & Munafò, M. R. (2016). Current incentives for scientists lead to underpowered studies with erroneous conclusions. *PLOS Biology*, 14(11), e2000995.** https://doi.org/10.1371/journal.pbio.2000995
    - An optimality model shows that career-maximising scientists run many small, underpowered studies of novel hypotheses. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1371/journal.pbio.2000995)

21. **Edwards, M. A., & Roy, S. (2017). Academic research in the 21st century: Maintaining scientific integrity in a climate of perverse incentives and hypercompetition. *Environmental Engineering Science*, 34(1), 51–61.** https://doi.org/10.1089/ees.2016.0223
    - Argues that quantitative metrics, hypercompetition for funding and perverse incentives risk a "tipping point" in which unethical behaviour becomes normalised, and explicitly invokes Campbell's law. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1089/ees.2016.0223)

22. **Fire, M., & Guestrin, C. (2019). Over-optimization of academic publishing metrics: observing Goodhart's Law in action. *GigaScience*, 8(6), giz053.** https://doi.org/10.1093/gigascience/giz053
    - Analysis of more than 120 million papers. Paper counts, citations, h-index and JIF have all "ceased to be good" measures, because of longer author lists, shorter papers, self-citation, lengthy reference lists and soaring output in top journals.
    - **S**. — [Crossref abstract](https://doi.org/10.1093/gigascience/giz053)

23. **Biagioli, M., & Lippman, A. (Eds.) (2020). *Gaming the Metrics: Misconduct and Manipulation in Academic Research*. MIT Press.** https://doi.org/10.7551/mitpress/11087.001.0001
    - An edited volume arguing that metric-based evaluation produced new forms of misconduct such as citation rings, fake peer review and predatory venues, so that "post-production misconduct" targets the metrics rather than the data. **[content from prior knowledge, not re-fetched; DOI verified]**
    - **S**. — [DOI](https://doi.org/10.7551/mitpress/11087.001.0001)

24. **Muller, J. Z. (2018). *The Tyranny of Metrics*. Princeton University Press.** https://doi.org/10.23943/9781400889433
    - A general critique of "metric fixation" across sectors, with a chapter on higher education and research. Widely cited as a statement of Campbell's and Goodhart's law. **[content from prior knowledge, not re-fetched; DOI verified]**
    - **S**. — [DOI](https://doi.org/10.23943/9781400889433)

25. **Nosek, B. A., Spies, J. R., & Motyl, M. (2012). Scientific Utopia II: Restructuring incentives and practices to promote truth over publishability. *Perspectives on Psychological Science*, 7(6), 615–631.** https://doi.org/10.1177/1745691612459058
    - The key statement that "what is good for scientists" (publishability) diverges from "what is good for science" (truth). It is foundational to the open science reform movement. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1177/1745691612459058)

26. **Alberts, B., Kirschner, M. W., Tilghman, S., & Varmus, H. (2014). Rescuing US biomedical research from its systemic flaws. *PNAS*, 111(16), 5773–5777.** https://doi.org/10.1073/pnas.1404402111
    - Four eminent leaders argue that the US biomedical system rests on an unsustainable "hypercompetitive" growth model: too many trainees for too few positions, low grant success rates, and conservative science. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1073/pnas.1404402111)

**Counter-evidence**

27. **Fanelli, D., Costas, R., & Larivière, V. (2015). Misconduct policies, academic culture and career stage, not gender or pressures to publish, affect scientific integrity. *PLOS ONE*, 10(6), e0127556.** https://doi.org/10.1371/journal.pone.0127556
    - Retractions were *not* higher among highly productive authors or in countries with high publication pressure.
    - Retractions were higher in countries that reward papers with cash.
    - **C/N**: generic "publish or perish" pressure does not obviously cause misconduct, but cash-per-paper does. — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0127556)

28. **Fanelli, D. (2018). Is science really facing a reproducibility crisis, and do we need it to? *PNAS*, 115(11), 2628–2631.** https://doi.org/10.1073/pnas.1708272114
    - Argues that the "science in crisis" narrative is "mistaken" and that a narrative of "epochal changes and empowerment of scientists" is more accurate.
    - **C**: the strongest direct challenge to the fragility thesis. — [Crossref abstract](https://doi.org/10.1073/pnas.1708272114)

### Inferences
- The Smaldino & McElreath mechanism (selection without intent) is a natural bridge to AI. If AI tools cut the cost of producing a publishable unit, the same selection dynamic predicts more of whatever methods maximise output.
- Fanelli is the main voice the paper must address to be credible. A useful reconciliation is that cash-per-paper and hard thresholds (Fanelli 2015; Seeber 2019; Baccini 2019) cause gaming more clearly than diffuse pressure does.

### Gaps
- I did not fetch the full text of Biagioli & Lippman or Muller, so chapter-level claims should be checked before they are quoted.

---

## Q3. Growth of output and its consequences

### Takeaway
Scientific output grows at roughly 4% a year, a doubling time of about 17 years (Bornmann et al. 2021). Indexed articles grew about 47% between 2016 and 2022, faster than the number of scientists (Hanson et al. 2024). Large fields show ossified canons (Chu & Evans 2021), and disruptiveness has declined (Park et al. 2023). That decline is methodologically contested (Petersen et al.; Holst et al.).

### Cited Findings

29. **Bornmann, L., & Mutz, R. (2015). Growth rates of modern science: A bibliometric analysis based on the number of publications and cited references. *JASIST*, 66(11), 2215–2222.** https://doi.org/10.1002/asi.23329
    - A segmented growth analysis estimating that science has gone through three growth phases, with the current phase growing at about 8–9% a year in cited references. **[growth figure from prior knowledge, not re-fetched; verify before quoting]**
    - **S**. — [DOI](https://doi.org/10.1002/asi.23329)

30. **Bornmann, L., Haunschild, R., & Mutz, R. (2021). Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases. *Humanities and Social Sciences Communications*, 8, 224.** https://doi.org/10.1057/s41599-021-00903-w
    - Uses Dimensions, Microsoft Academic, Web of Science and Scopus. Overall growth rate is 4.10% a year, a doubling time of 17.3 years, and four or five growth segments fit the data best.
    - **S/N**: growth is long-run and structural. — [Crossref abstract](https://doi.org/10.1057/s41599-021-00903-w)

31. **Chu, J. S. G., & Evans, J. A. (2021). Slowed canonical progress in large fields of science. *PNAS*, 118(41), e2021636118.** https://doi.org/10.1073/pnas.2021636118
    - Data: 1.8 billion citations among 90 million papers across 241 subjects.
    - In large fields, a "deluge of papers" leads to "ossification of canon" rather than turnover, and new work struggles to gain attention unless it cites already-canonical papers.
    - **S**. — [Crossref abstract](https://doi.org/10.1073/pnas.2021636118)

32. **Park, M., Leahey, E., & Funk, R. J. (2023). Papers and patents are becoming less disruptive over time. *Nature*, 613(7942), 138–144.** https://doi.org/10.1038/s41586-022-05543-x
    - Data: 45 million papers and 3.9 million patents over six decades.
    - The CD index shows works are "increasingly less likely to break with the past". The trend is universal across fields and is linked to narrowing use of prior knowledge.
    - **S**. — [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41586-022-05543-x&resultType=core&format=json)
    - **Contested by:**
      - **Petersen, A. M., Arroyave, F., & Pammolli, F. (2024).** The disruption index is biased by citation inflation. *Quantitative Science Studies*, 5(4), 936–953. https://doi.org/10.1162/qss_a_00333
      - **Petersen, Arroyave & Pammolli (2025).** The disruption index suffers from citation inflation: Re-analysis of temporal CD trend and relationship with team size reveal discrepancies. *Journal of Informetrics*, 19(1), 101605. https://doi.org/10.1016/j.joi.2024.101605
      - **Holst, V., Algaba, A., Tori, F., Wenmackers, S., & Ginis, V. (2024).** Dataset artefacts are the hidden drivers of the declining disruptiveness in science. arXiv:2402.14583. https://arxiv.org/abs/2402.14583
      - **C/N**: the paper should present the disruption decline as contested. — [Crossref](https://doi.org/10.1162/qss_a_00333); [arXiv](https://arxiv.org/abs/2402.14583)

33. **Hanson, M. A., Gómez Barreiro, P., Crosetto, P., & Brockington, D. (2024). The strain on scientific publishing. *Quantitative Science Studies*, 5(4), 823–843.** https://doi.org/10.1162/qss_a_00327
    - Articles indexed in Scopus and Web of Science were about 47% higher in 2022 than in 2016, outpacing growth in the number of practising scientists.
    - Growth was disproportionately driven by certain publishers using "special issues" with reduced turnaround times. The paper also documents year-over-year JIF inflation and concludes that "Such exponential growth cannot be sustained."
    - **S**: the key pre-AI baseline. — [Crossref abstract](https://doi.org/10.1162/qss_a_00327)

34. **Ioannidis, J. P. A., Klavans, R., & Boyack, K. W. (2018). Thousands of scientists publish a paper every five days. *Nature*, 561, 167–169.** https://doi.org/10.1038/d41586-018-06185-8
    - Identifies "hyperprolific" authors who publish 72 or more papers a year (one every five days), concentrated in certain fields and countries. **[the figure of roughly 9,000 such authors is from prior knowledge; verify]**
    - **S**. — [DOI](https://doi.org/10.1038/d41586-018-06185-8)

35. **Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are ideas getting harder to find? *American Economic Review*, 110(4), 1104–1144.** https://doi.org/10.1257/aer.20180338
    - Research productivity (output per researcher) is declining sharply across domains such as Moore's law and crop yields, so ever-larger research effort is needed to sustain growth. **[content from prior knowledge, not re-fetched]**
    - **S/N**: decline in productivity per researcher.
    - Note: a 2026 NBER working paper titled "Growth is Getting Harder to Find, Not Ideas" (Fort et al., doi:10.3386/w35182) appears to contest this. I only saw its title, so read it before citing. — [DOI](https://doi.org/10.1257/aer.20180338)

36. **Fortunato, S., et al. (2018). Science of science. *Science*, 359(6379), eaao0185.** https://doi.org/10.1126/science.aao0185
    - A review of the quantitative study of science: careers, collaboration, citation dynamics and the Matthew effect. **[content from prior knowledge, not re-fetched]**
    - **N**: neutral framing reference. — [DOI](https://doi.org/10.1126/science.aao0185)

### Inferences
- The baseline before ChatGPT (2022) already showed output growth outpacing reviewers and readers. Hanson et al. (2022 data) and Chu & Evans give the paper a clean "already strained before AI" anchor.
- Because the disruption decline is contested, the paper should present Park et al. with the Petersen and Holst caveats rather than as settled fact.

### Gaps
- Hanson et al. state that growth outpaced the workforce, but I did not re-extract their exact workforce figures (UNESCO-based). Check the full text before quoting.

---

## Q4. Peer review strain, grant competition, APC/open access economics, predatory and mega-journals

### Takeaway
Peer review is an enormous unpaid labour subsidy: more than 100 million reviewer-hours in 2020, with US reviewers' time worth over USD 1.5 billion. Grant writing consumes large amounts of time at low success rates, such as 34 working days per proposal against 21% success at the Australian NHMRC. Winning near the threshold compounds advantage. Publishing is an oligopoly in which five publishers had more than 50% of papers by 2013. The APC model has enabled high-volume and predatory publishing, and MDPI-specific critiques are themselves contested.

### Cited Findings

**Peer review labour**

37. **Aczel, B., Szaszi, B., & Holcombe, A. O. (2021). A billion-dollar donation: estimating the cost of researchers' time spent on peer review. *Research Integrity and Peer Review*, 6, 14.** https://doi.org/10.1186/s41073-021-00118-2
    - More than 100 million reviewer-hours worldwide in 2020, equivalent to over 15,000 years of work.
    - The value of US reviewers' time was over USD 1.5 billion, China over USD 600 million, and the UK close to USD 400 million. The authors say these are likely underestimates.
    - **S**. — [Crossref abstract](https://doi.org/10.1186/s41073-021-00118-2)

38. **Breuning, M., Backstrom, J., Brannon, J., Gross, B. I., & Widmeier, M. (2015). Reviewer fatigue? Why scholars decline to review their peers' work. *PS: Political Science & Politics*, 48(4), 595–600.** https://doi.org/10.1017/S1049096515000827
    - Fatigue is "only one of several reasons" scholars decline to review; most are willing to review but are busy.
    - **N**: an evidence-based nuance on the "reviewer fatigue" narrative. — [Crossref abstract](https://doi.org/10.1017/S1049096515000827)

39. **Bornmann, L. (2011). Scientific peer review. *Annual Review of Information Science and Technology*, 45(1), 197–245.** https://doi.org/10.1002/aris.2011.1440450112
    - A comprehensive review of research on the reliability, fairness and predictive validity of peer review. It finds low inter-reviewer reliability but some predictive validity for later citations. **[content from prior knowledge, not re-fetched]**
    - **N/C**: partly a defence of peer review. — [DOI](https://doi.org/10.1002/aris.2011.1440450112)

**Grant competition**

40. **Herbert, D. L., Barnett, A. G., Clarke, P., & Graves, N. (2013). On the time spent preparing grant proposals: an observational study of Australian researchers. *BMJ Open*, 3(5), e002800.** https://doi.org/10.1136/bmjopen-2013-002800
    - At the NHMRC, 21% of proposals were funded.
    - Each proposal took 34 working days on average, totalling about 550 researcher-years and AU$66 million a year in salary costs.
    - More time spent preparing a proposal did not increase the chance of success.
    - **S**. — [Crossref abstract](https://doi.org/10.1136/bmjopen-2013-002800)

41. **Fang, F. C., & Casadevall, A. (2016). Research funding: the case for a modified lottery. *mBio*, 7(2), e00422-16.** https://doi.org/10.1128/mBio.00422-16
    - Argues that peer review cannot reliably discriminate among the top-scoring proposals at low paylines. It proposes a quality threshold followed by a random draw. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1128/mBio.00422-16)

42. **Bol, T., de Vaan, M., & van de Rijt, A. (2018). The Matthew effect in science funding. *PNAS*, 115(19), 4887–4890.** https://doi.org/10.1073/pnas.1719557115
    - Applicants just above the funding threshold accumulated more than twice as much funding over the next eight years as near-identical applicants just below it. Part of the gap arises because non-winners stop applying.
    - **S**: arbitrary thresholds compound advantage. — [Crossref abstract](https://doi.org/10.1073/pnas.1719557115)

**Publishing business model and predatory/mega-journals**

43. **Larivière, V., Haustein, S., & Mongeon, P. (2015). The oligopoly of academic publishers in the digital era. *PLOS ONE*, 10(6), e0127502.** https://doi.org/10.1371/journal.pone.0127502
    - Data: 45 million Web of Science documents, 1973–2013.
    - The top five publishers had more than 50% of all 2013 papers, and about 70% in the social sciences.
    - **S**. — [Semantic Scholar abstract](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1371/journal.pone.0127502)

44. **Shen, C., & Björk, B.-C. (2015). 'Predatory' open access: a longitudinal study of article volumes and market characteristics. *BMC Medicine*, 13, 230.** https://doi.org/10.1186/s12916-015-0469-2
    - Estimates that predatory OA output grew from about 53,000 articles in 2010 to about 420,000 in 2014, across roughly 8,000 active journals, with authors concentrated in Asia and Africa. **[numbers from prior knowledge, not re-fetched; verify]**
    - **S**. — [DOI](https://doi.org/10.1186/s12916-015-0469-2)

45. **Grudniewicz, A., Moher, D., Cobey, K. D., et al. (2019). Predatory journals: no definition, no defence. *Nature*, 576, 210–212.** https://doi.org/10.1038/d41586-019-03759-y
    - A consensus definition of predatory journals: they prioritise self-interest over scholarship, use false or misleading information, deviate from best editorial practice, lack transparency, and use aggressive solicitation. It has 35 authors. **[content from prior knowledge, not re-fetched]**
    - **S**. — [DOI](https://doi.org/10.1038/d41586-019-03759-y)

46. **Oviedo-García, M. Á. (2021). Journal citation reports and the definition of a predatory journal: The case of the Multidisciplinary Digital Publishing Institute (MDPI). *Research Evaluation*, 30(3), 405–419.** https://doi.org/10.1093/reseval/rvab020
    - Argues that 53 MDPI journals indexed in the JCR show rising self-citation and intra-MDPI citation, consistent with predatory criteria.
    - **Important caveat:** the journal issued an **Expression of Concern** (doi:10.1093/reseval/rvab030, September 2021) and later a **Correction** (doi:10.1093/reseval/rvad014). Both were verified via Crossref "updated-by".
    - Cite it only alongside these notices.
    - **S/contested**. — [Crossref](https://doi.org/10.1093/reseval/rvab020)

### Inferences
- Peer review and grant review already run on an unpaid, overstretched volunteer economy with low discriminative power at the margin (Aczel; Herbert; Fang & Casadevall; Bol et al.). This is where AI-generated submissions and AI-written reviews would hit first.
- The APC model links publisher revenue to volume. This, combined with the special-issue growth documented by Hanson et al., is the structural reason AI-assisted mass production finds a ready outlet.

### Gaps
- I did not verify current (2024–2026) grant success rate statistics from NIH, ERC or UKRI; these should come from agency data portals.
- I did not verify a peer-reviewed empirical study of the Frontiers model. Hanson et al. cover Frontiers and MDPI growth together.
- The Publons *Global State of Peer Review 2018* PDF resolves (HTTP 200 at https://publons.com/static/Publons-Global-State-Of-Peer-Review-2018.pdf), but I did not extract its figures.
- I did not verify Liu et al. on the acceptability of the NZ Health Research Council lottery; Crossref returned an error.

---

## Q5. Counter-arguments: works defending metrics or peer review, or arguing the system works reasonably well

### Takeaway
The credible counter-literature is real but narrower than the critique. It does not claim the system is undistorted. It argues instead that:
- the "crisis" framing is overstated (Fanelli 2018);
- diffuse publish-or-perish pressure is not linked to misconduct (Fanelli et al. 2015);
- well-designed, stable incentives can raise output without lowering quality (Korytkowski & Kulczycki 2019);
- systems with strong ex post evaluation can be more efficient (Sandström & Van den Besselaar 2018);
- citation-indicator science can be done responsibly (Waltman 2016; Leiden Manifesto);
- headline findings such as the disruption decline are methodologically fragile (Petersen et al.; Holst et al.).

### Cited Findings

47. **Sandström, U., & Van den Besselaar, P. (2018). Funding, evaluation, and the performance of national research systems. *Journal of Informetrics*, 12(1), 365–384.** https://doi.org/10.1016/j.joi.2018.01.007
    - Large differences in efficiency exist between national systems. Efficient systems combine well-developed ex post evaluation with high institutional funding and high professional autonomy.
    - Note: a corrigendum was published, doi:10.1016/j.joi.2024.101539.
    - **C/N**: evaluation per se is not the problem. — [Semantic Scholar TLDR](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.joi.2018.01.007)

48. **Waltman, L. (2016). A review of the literature on citation impact indicators. *Journal of Informetrics*, 10(2), 365–391.** https://doi.org/10.1016/j.joi.2016.02.007
    - The authoritative technical review of citation indicators, including field normalisation and the problems of the h-index and JIF. It defends careful, responsible use. **[content from prior knowledge, not re-fetched]**
    - **N/C**. — [DOI](https://doi.org/10.1016/j.joi.2016.02.007)

- **Already listed above:**
  - Fanelli 2018 (entry 28) and Fanelli, Costas & Larivière 2015 (entry 27).
  - Korytkowski & Kulczycki 2019 (entry 9).
  - Osuna et al. 2011 (entry 12).
  - Bornmann 2011 on peer review (entry 39).
  - Breuning et al. 2015 on reviewer fatigue (entry 38).
  - Petersen et al. 2024/2025 and Holst et al. 2024 against the disruption decline (under entry 32).
  - The Metric Tide and the Leiden Manifesto (entries 6–7) as "reform, not abolition" positions.

### Inferences
- The defensible position for the paper is: "the system was already under measurable strain and is demonstrably gameable where incentives are crude (cash-per-paper, hard citation thresholds, volume-linked APC revenue)". A blanket "science was broken" claim would run into Fanelli and the Polish evidence.
- AI arguably matters most because it collapses the cost of producing exactly the metric-visible outputs (papers, citations, reviews, grant text) that these systems reward.

### Gaps
- I found no strong recent (2023–2026) peer-reviewed defence of the JIF or h-index as individual evaluation tools. Defenders mostly argue for responsible use, not for the status quo.
- I did not verify Stephan, P. (2012), *How Economics Shapes Science* (Harvard University Press), in this session. It is a likely useful book on the economics of the academic labour market and funding; verify the publisher page before citing.
