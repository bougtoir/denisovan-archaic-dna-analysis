# JHG QC failure analysis

The package's limits were correct, but the controls behind them could not have caught a wrong value. Table of control gaps (before this pass) and their fixes:

| Expected safeguard | Actual behaviour | Why it failed / was weak | Consequence | Required remediation (done) |
|---|---|---|---|---|
| Audit checked independently of the generator | The audit and the generator limits came from one reading of the GTA in one session | One source and one reader; no second check | A wrong reading would have reached both unchanged | Guard re-parses the GTA row on every build (`parse_guide_row`) |
| Build checks compare against the journal source | `validate()` compared against literals (250, 5000, 6, 50) | Literals carried no provenance | Any copied or stale literal would PASS | Limits are read from the manifest, and the build fails unless the manifest equals the parsed GTA row |
| Second official source | Live author page archived but not checked by the build | Not machine-checked | A newer guide could have gone unnoticed | Guard requires two sources (guide + live page); the live page must link the pinned guide, otherwise "Sources conflict" FAIL |
| Journal name asserted when requirements are loaded | No identity assertion | Limits were journal-agnostic numbers | A requirements file for another journal would be accepted | Guard asserts slug, full name, the canonical `/jhg/` URL family and a `JHG_GTA*` guide name |
| PDF title / journal identity checked | Not checked | — | An HGV guide renamed as JHG would be accepted | Guard requires "The Journal of Human Genetics is" in the guide's About section and the JHG `<title>` on the live page |
| Cached-source date checked | Ledger recorded dates but nothing read them | — | A stale cached copy could silently win | Sources are pinned by SHA-256; a ledger entry for the same URL that is newer and has a different hash FAILS |
| Article type tied to the limits | `ARTICLE_TYPE` and the limits were independent | — | Brief Communication limits could be labelled Article | Manifest article type must equal `jhg_content.ARTICLE_TYPE`; limits are parsed from that type's row only (regression test: Brief Communication values labelled Article → FAIL) |
| Premise in user instructions verified | Done manually in this pass (stop and ask) | Manual only | — | Recorded here; the guard makes the check reproducible |
