---
name: agentic-foundation
description: >-
  Initialize, review, incrementally sync, or extend an agentic project foundation.
  Use when the user wants to 打地基, 初始化项目地基, 建立 agent 工作入口, create AGENTS.md,
  create a project/document map, create docs/foundation governance files, sync or upgrade an
  existing .foundation or docs/foundation structure, or add foundation modules such as ADR,
  archive, open questions, hooks, subagent review workflow, or coding guidance. Do not use for
  PRD writing, Specs generation, project planning, task breakdown, architecture design, QA,
  release checks, or direct implementation unless the user is asking only to register their
  entry points in the foundation. If the user is only discussing whether a foundation is useful,
  analyze only and do not write files.
metadata:
  short-description: Initialize or sync project foundation
  version: v2.0.1
  updated: 2026-07-14
---

# Agentic Foundation

Use this skill to create or maintain a lightweight foundation for projects where agents need a stable entrance, current handoff state, long-lived principles, important history, and optional governance modules.

## Default Output

For a new project, create only:

```text
AGENTS.md
README.md
docs/
  README.md
  foundation/
    README.md
    PRINCIPLES.md
    STATE.md
    LOG.md
```

Do not create ADR, archive, review, hook, coding-guidance, open-questions, QA, TDD, handoff, notes, or suggestion files by default. Add them only through the add-on module workflow.

## File Contract

| File | Responsibility |
|---|---|
| `AGENTS.md` | Short agent entrance: what to read first, hard rules, and when to use the foundation. |
| `README.md` | Project front door: one-line project description and pointer to `docs/README.md`. |
| `docs/README.md` | Project map: active document entrances, minimum read set, enabled modules, and archive index if present. |
| `docs/foundation/README.md` | Foundation routing authority: where information belongs, when to read or write, and how modules are added. |
| `docs/foundation/PRINCIPLES.md` | Current long-lived rules, forbidden zones, stable preferences, and tradeoffs. |
| `docs/foundation/STATE.md` | Current handoff snapshot, revised to stay current; not a historical log. |
| `docs/foundation/LOG.md` | Important history ledger: initialization, upgrades, decisions, incidents, reviews, archive events, and artifact references. |

Keep details in the smallest appropriate artifact. Prefer paths and short summaries over copying long PRDs, Specs, logs, reviews, issues, or handoff text into foundation files.

Preserve validation integrity: failed tests, checks, reviews, or acceptance criteria are evidence. Do not weaken, skip, delete, or rewrite validation just to make it pass. Change validation only when the requirement, interface, or validation itself is demonstrably outdated or wrong, and explain what protection remains.

## Workflow Selection

Choose exactly one entry:

1. **Initialize**: user asks to create a foundation in a project folder.
2. **Sync / Upgrade**: user asks to update an existing foundation to the current capability.
3. **Add Module**: user asks for or agrees to add ADR, archive, open questions, hooks, subagent workflow, coding guidance, or another optional foundation module.

If the user is only asking for analysis, design discussion, or whether a foundation is useful, do not write files.

## Initialize

1. Confirm the target project directory. If the current directory is clearly the target, use it and say so.
2. Confirm write authorization. Words like 初始化, 创建, 生成, 应用, 打地基, 建立, 同步, 升级, 追加 mean write authorization for the relevant workflow.
3. Check for conflicts before writing:
   - `AGENTS.md`
   - `README.md`
   - `docs/README.md`
   - `docs/foundation/`
   - legacy `.foundation/`
   - any output file with the same path
4. If any conflict exists, stop and ask the user how to proceed. Do not overwrite, merge, delete, or migrate silently.
5. Collect only minimal dynamic content:
   - project purpose in one short paragraph
   - main risks
   - user work preferences
6. Run:

```text
python scripts/init_foundation.py <target_dir> --project-name <name> --language zh
```

Optional:

```text
--purpose "<project purpose>"
--risks "<main risks>"
--preferences "<work preferences>"
--create-target
```

Use `--create-target` only when the user explicitly wants the target directory created.

## Sync / Upgrade

Sync is incremental alignment, not re-initialization.

1. Identify the current structure: `AGENTS.md`, root `README.md`, `docs/README.md`, `docs/foundation/`, legacy `.foundation/`, old `SUGGESTIONS.md`, old `CHECKS.md`, ADR, archive, reviews, context docs, and project-specific entrances.
2. Read only files relevant to the current foundation entrance, project map, minimum read path, or naturally encountered archive candidates.
3. Preserve user-added content, project-specific rules, history, and artifact paths.
4. Do not whole-file overwrite, auto-delete, auto-move, or bulk-promote old suggestions into ADR.
5. For legacy `.foundation/`, actively suggest migration to `docs/foundation/` when it would reduce entrance confusion, but wait for confirmation.
6. If old archive / backup / deprecated areas pollute the active map, scatter history, or break the reading path, propose migration to `docs/archive/` and wait for confirmation.
7. Record the handling conclusion for each default file. Only mark the project synced when every default file is updated or has a clear keep-as-is reason.

If the user only asked for an update check, report the diff and recommendations without changing files.

## Add Module

Optional modules are actively suggested when they would prevent recurring confusion or improve long-term maintainability, but never created automatically.

Before creating or modifying module files, state:

- what problem the module solves
- what will be created or registered
- when agents should read it
- how it stops being useful or should be reviewed
- whether it affects the foundation core

Then wait for user confirmation.

Common module defaults:

| Module | Create or register after confirmation |
|---|---|
| ADR | `docs/adr/README.md` and the first ADR, or an existing decision-record location. |
| Open Questions | `docs/foundation/OPEN_QUESTIONS.md` or an existing questions artifact. |
| Subagent Workflow | A reply-only summary, or `docs/reviews/YYYY-MM-DD-topic.md` when traceability is needed. |
| Hooks | Real hook configuration plus disable / rollback notes, or an existing hook location. |
| Coding Guidance | `docs/foundation/CODING_GUIDANCE.md` or an existing coding / QA / TDD convention path. |
| Archive | `docs/archive/README.md` when the first real archive event happens. |

Do not create empty module directories, placeholder READMEs, fixed role libraries, or unused process files.

## Self-Evolution Rules

Agents should actively notice foundation update opportunities at natural lifecycle points:

- user says remember, later, do not repeat, why again, sync, upgrade, review, decision, archive, ADR, hook, subagent
- before modifying stable entrances, project maps, foundation files, templates, scripts, migrations, archive areas, or optional modules
- while seeing conflicts, outdated paths, missing evidence, repeated errors, unverifiable results, scope creep, or document/repo drift
- when tests, checks, reviews, acceptance criteria, or validation rules fail unexpectedly
- after important work, verification, migration, archive, sync, subagent review, or module addition
- when context is getting long, a handoff is needed, or a phase is starting or ending

Most triggers are internal checks. Show them only when they require a write, user decision, risk explanation, module suggestion, or explicit "no action" reason.

Self-evolution does not expand write authorization. It allows the agent to propose, route, update already-authorized files, or ask for confirmation.

## Validation

After any initialization or template/script change:

1. Run the skill validator.
2. Run the init script in a temporary empty directory.
3. Confirm the generated structure matches the default output.
4. Confirm no legacy `.foundation/`, `SUGGESTIONS.md`, or `CHECKS.md` is generated.
5. Confirm conflict protection still stops on existing `AGENTS.md`, `README.md`, `docs/foundation/`, or legacy `.foundation/`.

When the change is substantial, use independent subagents for review or forward-testing if available. Review P0/P1 first; do not keep iterating on low-priority polish if the core behavior is sound.

## Completion

Finish with a concise status:

- what changed
- what was verified
- any limitation or user decision still pending

Do not generate PRD, Specs, project plans, task breakdowns, architecture designs, or QA matrices as part of foundation initialization.
