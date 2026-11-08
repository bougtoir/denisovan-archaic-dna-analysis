#!/usr/bin/env python3
"""Validate Human Genetics manuscript references against Crossref/PubMed."""

import validate_references as base
import humangen_content

base.REFERENCE_RECORDS = humangen_content.REFERENCE_RECORDS
base.OUT_PATH = base.ROOT / "docs" / "humangen_submission" / "reference_validation.csv"

if __name__ == "__main__":
    base.main()
