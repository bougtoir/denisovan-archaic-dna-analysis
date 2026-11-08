# JHG requirements validation guard

Code: `scripts/journal_requirements.py` (`verify()`); manifest: `data/journal_requirements/jhg_requirements.json`; caller: `scripts/create_jhg_submission.py` (at the start of `main()`, so nothing is generated when it fails, and again in `validate()`, which takes every limit from the verified manifest).

Manifest fields: journal_slug, journal_abbreviation, journal_full, publisher, society, canonical_domain, canonical_url, guide_url, guide_version, guide_revised, access_utc, article_type, guide_row_anchor, guide_next_row_anchor, limits{abstract_words, main_text_words, display_items, references}, sources[{role, file, url, sha256}] (roles: guide, live_page).

Checks (any failure raises `RequirementsError` and stops the build):
1. Every required field and limit is present; integer limits only. Missing → FAIL.
2. journal_slug and journal_full equal the builder's target (`jhg`, `Journal of Human Genetics`).
3. canonical_url is on www.nature.com under `/jhg/`; guide_url is a `JHG_GTA*` document on the same domain; the live page URL is under canonical_url.
4. Exactly two official sources (guide + live page), each present on disk with a matching SHA-256.
5. The guide identifies itself ("The Journal of Human Genetics is …" before the article-type table) and contains the pinned version string ("Revised 22 April 2026").
6. The article-type row is parsed from the guide: exactly one row start, one abstract value, one word limit and two "Max of" values. Anything else → "Ambiguous guide row" FAIL. The parsed values must equal the manifest limits.
7. The live page's `<title>` names Journal of Human Genetics and it links exactly the pinned guide. A different or additional JHG_GTA link → "Sources conflict … resolve manually" FAIL.
8. Staleness: a ledger entry for a pinned URL that is newer than access_utc and has a different SHA-256 → FAIL (re-verify manually), so neither an older nor a newer cache can silently replace the verified source.
9. Builder: manifest article_type must equal `jhg_content.ARTICLE_TYPE` (Article).

Update procedure when JHG revises its guide: archive the new PDF and live page under data/raw/journal (new filenames, ledger entries), update the manifest's sources, version string, access_utc and limits, then rebuild. The guard fails until all of these agree.
