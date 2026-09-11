---
name: agentic-foundation
description: >-
  Initialize, incrementally upgrade, or extend a lightweight project foundation for
  long-running human-agent work. Use when the user wants to 打地基, 初始化项目地基,
  create or maintain AGENTS.md, a project map, docs/foundation, decision records,
  archive, hooks, subagent workflow, or coding guidance. Do not use for writing PRDs,
  Specs, plans, architecture, QA/TDD workflows, or implementation work itself.
metadata:
  short-description: Initialize or evolve a project foundation
  version: v2.1.2
  updated: 2026-09-07
---

# Agentic Foundation

Create a small, living documentation foundation that helps people and agents orient,
continue work, preserve decisions, and evolve project practice without turning every
project into a process system.

## Choose One Mode

- **Initialize** a new project with the default structure.
- **Sync / upgrade** an existing foundation incrementally.
- **Extend** an existing foundation with a confirmed optional module.

For discussion or assessment only, analyze without writing.

## Shared Boundaries

- Confirm the project path, selected mode, and relevant write scope before changing files.
- Preserve existing content and project conventions. Never silently overwrite, move, delete,
  or create a module outside the authorized scope.
- Let the project's entrance, map, and current state establish an initial view. Follow the
  task, risk, and evidence to decide what else to inspect; a map is navigation, not proof.
- Keep claims, completion statements, and modifications proportionate to their evidence and
  scope. Do not weaken validation merely to obtain a pass.
- Prefer the smallest action that addresses the actual issue after understanding its impact.
- Keep the default structure lean. Add files, folders, or automation only when they solve a
  real continuing problem and the user has agreed to their creation.

## Initialize

Read [default structure](references/default-structure.md). Confirm the target is new enough
for initialization, collect only the project purpose plus any material risks or preferences,
then run the initializer in preview first:

```text
python scripts/init_foundation.py <target_dir> --project-name <name> --language zh --dry-run
```

If the preview is conflict-free and initialization is authorized, rerun without `--dry-run`.
Use `--create-target` only when the user explicitly wants the target directory created.

## Sync / Upgrade

Read [migration policy](references/migration-policy.md) and [record routing](references/record-routing.md).
Inspect only the active entrance, project map, current state, and paths naturally relevant to
the requested upgrade. Produce a small incremental-change preview before writing. A request to
check or assess stops at the preview; an explicit sync or upgrade authorizes only the described
incremental scope. Preserve user additions and project-specific rules; migrations, removals,
new modules, conflicts, and scope expansion require explicit confirmation.

## Extend

Read [add-on modules](references/add-on-modules.md). Explain the problem, the proposed
artifact or registration, how it will be used, and its review or stopping condition. Create
or change the module only after the user has authorized that addition.

## Record and Evolve

Use [record routing](references/record-routing.md) when current state, history, long-lived
constraints, decisions, or archived material need different homes. When a correction, drift,
repeat failure, or important boundary crossing could change future collaboration, make a
lightweight judgment: update an already-authorized existing artifact, propose an addition, or
stay quiet when there is no durable conclusion.

## Verify

Read [validation](references/validation.md) after changing templates, scripts, or structure.
Run the local validator and relevant dry-run / generated-artifact checks. For a substantial
change, use independent review or forward testing when it can uncover a meaningful risk; fix
or surface P0/P1 findings before declaring completion.

Finish with what changed, what was verified, and any decision still needed.
