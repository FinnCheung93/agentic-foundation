#!/usr/bin/env python3
"""Initialize an agentic governance foundation in a project directory."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path


FILES = [
    ("AGENTS.md", "AGENTS.md"),
    (".foundation/README.md", ".foundation/README.md"),
    (".foundation/PRINCIPLES.md", ".foundation/PRINCIPLES.md"),
    (".foundation/STATE.md", ".foundation/STATE.md"),
    (".foundation/LOG.md", ".foundation/LOG.md"),
    (".foundation/CHECKS.md", ".foundation/CHECKS.md"),
    (".foundation/SUGGESTIONS.md", ".foundation/SUGGESTIONS.md"),
]

FOUNDATION_VERSION = "1.4.1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create AGENTS.md and .foundation/ governance files for an agentic project."
    )
    parser.add_argument("target_dir", help="Project directory to initialize.")
    parser.add_argument("--project-name", default=None, help="Project display name.")
    parser.add_argument("--language", default="zh", choices=["zh"], help="Template language. Currently only zh.")
    parser.add_argument("--create-target", action="store_true", help="Create target_dir if it does not exist.")
    parser.add_argument("--purpose", default="待补充：请在首次项目澄清后更新。", help="What the project is trying to do.")
    parser.add_argument("--risks", default="待补充：请记录本项目最不能接受的 AI 误改、误解或破坏。", help="Main risks.")
    parser.add_argument("--preferences", default="待补充：请记录用户希望 agent 如何先思考、汇报、确认和记录。", help="Work preferences.")
    return parser.parse_args()


def template_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "templates"


def detect_conflicts(target: Path) -> list[Path]:
    conflicts: list[Path] = []
    if (target / ".foundation").exists():
        conflicts.append(target / ".foundation")
    for _, output_rel in FILES:
        output_path = target / output_rel
        if output_path.exists() and output_path not in conflicts:
            conflicts.append(output_path)
    return conflicts


def render(template: str, values: dict[str, str]) -> str:
    result = template
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    target = Path(args.target_dir).resolve()
    if not target.exists():
        if not args.create_target:
            print("FOUNDATION_INIT_TARGET_MISSING")
            print("The target directory does not exist. No files were written.")
            print("Pass --create-target only when the user explicitly wants this script to create it.")
            print(f"- {target}")
            return 3
        target.mkdir(parents=True, exist_ok=True)

    if not target.is_dir():
        print("FOUNDATION_INIT_TARGET_NOT_DIRECTORY")
        print("The target path exists but is not a directory. No files were written.")
        print(f"- {target}")
        return 4

    conflicts = detect_conflicts(target)
    if conflicts:
        print("FOUNDATION_INIT_CONFLICT")
        print("The target directory already contains foundation files. No files were written.")
        for path in conflicts:
            print(f"- {path}")
        return 2

    name = args.project_name or target.name
    now = dt.datetime.now()
    values = {
        "PROJECT_NAME": name,
        "FOUNDATION_VERSION": FOUNDATION_VERSION,
        "INIT_DATE": now.date().isoformat(),
        "INIT_TIME": now.strftime("%Y-%m-%d %H:%M CST"),
        "PROJECT_PURPOSE": args.purpose,
        "MAIN_RISKS": args.risks,
        "WORK_PREFERENCES": args.preferences,
    }

    templates = template_dir()
    for template_rel, output_rel in FILES:
        template_path = templates / template_rel
        output_path = target / output_rel
        content = template_path.read_text(encoding="utf-8")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(render(content, values), encoding="utf-8", newline="\n")

    print("FOUNDATION_INIT_OK")
    print(f"Project: {name}")
    print(f"Target: {target}")
    for _, output_rel in FILES:
        print(f"- {output_rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
