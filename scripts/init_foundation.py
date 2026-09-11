#!/usr/bin/env python3
"""Initialize the default Agentic Foundation structure without overwriting a project."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from uuid import uuid4
from pathlib import Path
from zoneinfo import ZoneInfo


FOUNDATION_VERSION = "2.1.2"

FILES = [
    ("AGENTS.md", "AGENTS.md"),
    ("README.md", "README.md"),
    ("docs/foundation/README.md", "docs/foundation/README.md"),
    ("docs/foundation/PRINCIPLES.md", "docs/foundation/PRINCIPLES.md"),
    ("docs/foundation/STATE.md", "docs/foundation/STATE.md"),
    ("docs/foundation/LOG.md", "docs/foundation/LOG.md"),
]

CONFLICT_PATHS = ["AGENTS.md", "README.md", "docs/README.md", "docs/foundation", ".foundation"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create AGENTS.md, README.md, and docs/foundation files."
    )
    parser.add_argument("target_dir", help="Project directory to initialize.")
    parser.add_argument("--project-name", default=None, help="Project display name.")
    parser.add_argument("--language", default="zh", choices=["zh"], help="Template language. Currently only zh.")
    parser.add_argument("--create-target", action="store_true", help="Create target_dir if it does not exist.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned writes without creating or changing files.")
    parser.add_argument("--purpose", default="待补充：请在首次项目澄清后更新。", help="What the project is trying to do.")
    parser.add_argument("--risks", default="待补充：请记录本项目最不能接受的误解、误改或损失。", help="Main risks.")
    parser.add_argument("--preferences", default="待补充：请记录用户希望 agent 如何思考、汇报、确认和记录。", help="Work preferences.")
    return parser.parse_args()


def template_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "templates"


def detect_conflicts(target: Path) -> list[Path]:
    conflicts: list[Path] = []
    docs_path = target / "docs"
    if docs_path.exists() and not docs_path.is_dir():
        conflicts.append(docs_path)
    for rel in CONFLICT_PATHS:
        path = target / rel
        if path.exists() and path not in conflicts:
            conflicts.append(path)
    for _, output_rel in FILES:
        path = target / output_rel
        if path.exists() and path not in conflicts:
            conflicts.append(path)
    return conflicts


def render(template: str, values: dict[str, str]) -> str:
    result = template
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def load_outputs(values: dict[str, str]) -> list[tuple[Path, str]]:
    templates = template_dir()
    outputs: list[tuple[Path, str]] = []
    for template_rel, output_rel in FILES:
        template_path = templates / template_rel
        outputs.append((Path(output_rel), render(template_path.read_text(encoding="utf-8"), values)))
    return outputs


def print_plan(target: Path, create_target: bool) -> None:
    print("FOUNDATION_INIT_DRY_RUN")
    print(f"Target: {target}")
    if create_target:
        print(f"- create directory: {target}")
    for _, output_rel in FILES:
        print(f"- create: {output_rel}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    target = Path(args.target_dir).resolve()
    target_missing = not target.exists()
    if target_missing and not args.create_target:
        print("FOUNDATION_INIT_TARGET_MISSING")
        print("The target directory does not exist. No files were written.")
        print("Pass --create-target only when the user explicitly wants this script to create it.")
        print(f"- {target}")
        return 3

    if not target_missing and not target.is_dir():
        print("FOUNDATION_INIT_TARGET_NOT_DIRECTORY")
        print("The target path exists but is not a directory. No files were written.")
        print(f"- {target}")
        return 4

    conflicts = [] if target_missing else detect_conflicts(target)
    if conflicts:
        print("FOUNDATION_INIT_CONFLICT")
        print("The target directory already contains foundation or entrance files. No files were written.")
        for path in conflicts:
            print(f"- {path}")
        return 2

    name = args.project_name or target.name
    now = dt.datetime.now(ZoneInfo("Asia/Shanghai"))
    values = {
        "PROJECT_NAME": name,
        "FOUNDATION_VERSION": FOUNDATION_VERSION,
        "INIT_DATE": now.date().isoformat(),
        "INIT_TIME": now.strftime("%Y-%m-%d %H:%M CST"),
        "PROJECT_PURPOSE": args.purpose,
        "MAIN_RISKS": args.risks,
        "WORK_PREFERENCES": args.preferences,
    }
    outputs = load_outputs(values)

    if args.dry_run:
        print_plan(target, target_missing)
        return 0

    if target_missing:
        target.mkdir(parents=True, exist_ok=True)

    stage = target / f".agentic-foundation-init-{uuid4().hex}"
    committed: list[Path] = []
    try:
        for output_rel, content in outputs:
            staged_path = stage / output_rel
            staged_path.parent.mkdir(parents=True, exist_ok=True)
            staged_path.write_text(content, encoding="utf-8", newline="\n")
        for output_rel, _ in outputs:
            destination = target / output_rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            (stage / output_rel).replace(destination)
            committed.append(destination)
    except OSError as exc:
        for path in reversed(committed):
            path.unlink(missing_ok=True)
        print("FOUNDATION_INIT_WRITE_FAILED")
        print("Initialization was rolled back. No foundation files were retained.")
        print(f"- {exc}")
        return 5
    finally:
        shutil.rmtree(stage, ignore_errors=True)

    print("FOUNDATION_INIT_OK")
    print(f"Project: {name}")
    print(f"Target: {target}")
    for _, output_rel in FILES:
        print(f"- {output_rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
