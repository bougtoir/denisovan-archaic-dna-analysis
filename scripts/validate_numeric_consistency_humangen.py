#!/usr/bin/env python3
"""Spot-check numeric consistency between the Human Genetics manuscript and data files."""

import validate_numeric_consistency as base

base.DOCX = base.ROOT / "docs" / "humangen_submission" / "HUMAN_GENETICS_MAIN_MANUSCRIPT.docx"
base.OUT = base.ROOT / "docs" / "humangen_submission" / "numeric_consistency_check.txt"

if __name__ == "__main__":
    base.main()
