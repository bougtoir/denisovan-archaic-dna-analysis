# JHG requirements root cause

## PRIMARY ROOT CAUSE
Verified: the compact instruction's premise mislabels the JHG **Brief Communication** row (150 / 1,000 / 3 / 20) as the JHG **Article** format. The two rows sit next to each other in the "Article Type Specifications" table of JHG_GTA_v10.pdf, and both word-limit cells start with the label "Article:" (for example "Article: 1,000 words max" in the Brief Communication row). Reading a column without its row header gives exactly this mix-up. This is an inference about the mechanism: the premise cites no source, so how it was produced cannot be confirmed.

The earlier package values (5,000 / 6 / 50) were **not** a misreading. They equal the official JHG Article row.

## CONTRIBUTING FACTORS
- The guide reuses the label "Article:" inside word-limit cells of every row (Article, Brief Communication, Review Article), which makes the rows easy to confuse when read out of context.
- The premise cited no URL, version or page, so it could not be traced directly.
- The HGV Article row has the same 5,000 / 6 / 50 values. A reader who sees the two journals' figures together could take JHG's Article limits for HGV's. The project history shows that HGV played no part in the earlier package (no HGV source before this pass), so this is a possible source of confusion, not an established cause.
- Weak controls in the project (JHG_QC_FAILURE_ANALYSIS.md): literal limits, no identity assertion, no machine cross-check of sources.

## DETECTION FAILURE
None inside the project for the disputed values: the premise was caught at the first step (before any compression) by re-reading the official guide. The latent detection weakness was that the build could not have caught a wrong limit, because it checked against its own literals.

## PROPAGATION MECHANISM
The compact values never entered any project file except the archived instruction (JHG_REQUIREMENTS_PROPAGATION_TRACE.md). The correct Article values went from the guide to the audit, the builder literals, the checklists and the handoffs, copied forward without being re-verified. They now flow through the verified manifest.

## IMPACT
- On the package: none. The Article package was correct as submitted, and its text, numbers, figures, tables and references are unchanged by this pass (DOCX text and figure/SI bytes compared with commit 4d9514c20).
- Avoided: compressing a full research article into the Brief Communication format (about −75% of the text, −3 display items, −11 references), which the guide reserves for studies that "fall short of the criteria for full research papers".
- Added: a requirements manifest, a cross-journal guard and 18 regression tests.
