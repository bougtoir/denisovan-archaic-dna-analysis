# JHG requirements propagation trace

## Chain for the values actually used in the package (Article 250 / 5,000 / 6 / 50)

`JHG_GTA_v10.pdf (official, SHA-256 6b920a00…)` → `JHG_REQUIREMENTS_AUDIT.md` rows 3–6 (commit 5eddb19ad, 2026-11-08 03:52 UTC) → `scripts/create_jhg_submission.py` validate() literals 250 / 5000 / 6 / 50 (same commit) → `JHG_BUILD_CHECKS.md`, `JHG_SUBMISSION_FORMAT_AUDIT.md`, `SUBMISSION_CHECKLIST_JHG.md`, `FINAL_HANDOFF_JHG.md` (same commit) → single-author versions (commit 4d9514c20, 2026-11-08 04:30 UTC) → this pass: `data/journal_requirements/jhg_requirements.json`, verified against the GTA and the live page on every build.

At every step the values equal the official JHG Article row, so **no incorrect limit entered or propagated through the project**.

## Chain for the disputed premise (Article = 150 / 1,000 / 3 / 20)

1. First appearance: user instruction 3 (`DEVIN_JHG_COMPACT_WITH_ROOT_CAUSE_PROMPT.txt`, received in this session after commit 4d9514c20). It calls 5,000 / 6 / 50 incorrect and states that "the current JHG Guide to Authors appears to specify a much shorter Article format". It cites no URL, version or page.
2. Before that, no repository file, git revision (`git log --all -S`), generated DOCX or earlier instruction contains these numbers as JHG Article limits.
3. It went no further: Devin checked it against the official guide before any compression, found it matched the Brief Communication row, and stopped to ask the user, who chose to keep the Article. No generator, checklist or handoff took up the compact values.

## Why the later QC did not reject the original values

Nothing needed rejecting, because the values were correct. The QC weakness was structural. The builder compared against hard-coded literals copied from an audit written by the same process, so it would have accepted wrong values just as readily. See JHG_QC_FAILURE_ANALYSIS.md.
