# Validation

Use verification proportionate to the change and its downside. A passing check proves only what
that check actually covered.

For template or script changes:

1. Run `python scripts/quick_validate.py`.
2. Run initialization in an isolated temporary directory with `--dry-run`, then for real.
3. Inspect the generated structure and the minimum reading path.
4. Exercise a conflict case and a missing-target case.

For material workflow changes, use an independent review or forward test when it can expose a
real failure. Give reviewers the raw artifact and acceptance boundary, not the expected answer.
Resolve or surface P0/P1 findings before declaring success. Do not keep iterating merely to
erase low-priority wording preferences.

When a check fails, investigate the target behavior before changing the check. Change a test,
review rule, or acceptance condition only when its premise is demonstrably outdated or wrong,
and state what protection remains.
