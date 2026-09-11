#!/usr/bin/env python3
"""Check the structural invariants of the Agentic Foundation skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_TEMPLATES = {
    "AGENTS.md",
    "README.md",
    "docs/foundation/README.md",
    "docs/foundation/PRINCIPLES.md",
    "docs/foundation/STATE.md",
    "docs/foundation/LOG.md",
}
REQUIRED_REFERENCES = {
    "default-structure.md",
    "add-on-modules.md",
    "migration-policy.md",
    "record-routing.md",
    "validation.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill = root / "SKILL.md"
    if not skill.is_file():
        fail("SKILL.md is missing")
    content = skill.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "name: agentic-foundation" not in content:
        fail("SKILL.md frontmatter is invalid")
    version = re.search(r"^  version: v(\d+\.\d+\.\d+)$", content, re.MULTILINE)
    if not version:
        fail("SKILL.md metadata.version is missing or invalid")

    templates_root = root / "assets" / "templates"
    found_templates = {path.relative_to(templates_root).as_posix() for path in templates_root.rglob("*.md")}
    if found_templates != EXPECTED_TEMPLATES:
        fail(f"default templates differ: {sorted(found_templates)}")
    if found_templates & {"SUGGESTIONS.md", "CHECKS.md", "docs/README.md"}:
        fail("forbidden default template exists")

    references_root = root / "references"
    found_references = {path.name for path in references_root.glob("*.md")} if references_root.is_dir() else set()
    missing_references = REQUIRED_REFERENCES - found_references
    if missing_references:
        fail(f"required references are missing: {sorted(missing_references)}")

    initializer = (root / "scripts" / "init_foundation.py").read_text(encoding="utf-8")
    if f'FOUNDATION_VERSION = "{version.group(1)}"' not in initializer:
        fail("initializer version does not match SKILL.md")
    if '("docs/README.md", "docs/README.md")' in initializer:
        fail("initializer still creates docs/README.md")
    if '"--dry-run"' not in initializer:
        fail("initializer has no dry-run support")

    ui = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "docs/README.md" in ui:
        fail("UI metadata describes a removed default file")

    package_readme = (root / "README.md").read_text(encoding="utf-8")
    if "docs/\n  README.md\n  foundation/" in package_readme:
        fail("package README describes a removed default file")

    print(f"OK: agentic-foundation v{version.group(1)} structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
