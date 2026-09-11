# Add-on Modules

Add a module only after a real need is identified and the user confirms the proposed creation
or registration. Prefer registering an equivalent existing project practice over introducing a
parallel one.

## Decision Records

Suggest a Decision Record when a confirmed choice is hard to reverse or future work would
naturally ask why another viable option was not chosen. For a new project, first use creates:

```text
docs/decisions/
  INDEX.md
  0001-short-title.md
```

The index lists number, title, status, relationship, and link. A record is a decision-time
snapshot: context, alternatives, conclusion, consequences, and any review condition. It does
not replace current principles or detailed history. Existing projects keep one active decision
location unless a confirmed migration changes it.

## Archive

At the first real archive event, create `docs/archive/README.md`. The index records path,
status, reason, replacement or no-replacement, archive time, and a brief reading cue. Valid
statuses are `deprecated`, `superseded`, `archived`, and `deleted-reference`. Preserve the old
artifact by default; moving, renaming, or deletion requires confirmation.

## Subagent Workflow

Use real subagents when independent perspective or parallel work materially improves the
result. A reviewer should receive raw materials and an acceptance boundary, then look for
counter-evidence rather than repeat the expected conclusion. One-off collaboration can remain
in the reply. Create a durable review artifact only when the user confirms that traceability or
reuse is worthwhile.

## Hooks and Coding Guidance

Hooks are appropriate when a recurring, observable problem can be meaningfully prompted or
guarded by a real tool mechanism. They need a disable or rollback path. Coding guidance is for
project-specific engineering practice; register existing guidance first, and do not make it a
default requirement for non-code projects.
