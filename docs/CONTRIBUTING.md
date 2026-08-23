# Contributing Workflow Guide

This guide documents the standard local-development and Git/GitHub workflow used in this repository. It's written so any developer (or automated agent) picking this project up can follow the same process without prior context.

## 1. Environment Setup

```bash
# Create and activate a local virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install project + dev/test dependencies
pip install -r requirements.txt
```

`.venv/` is self-ignored (it ships its own `.gitignore`), so it never needs to be added to the repo's ignore rules. Use `.venv/bin/pytest`, `.venv/bin/black`, etc. if the venv isn't activated in your shell.

## 2. Starting Work: Branching

Always branch off an up-to-date `main`. Use a `feature/<phase-or-topic>-<short-description>` naming convention, mirroring the roadmap phase where possible:

```bash
git checkout main
git pull origin main
git checkout -b feature/phase-3-topological-sort
```

## 3. Implementing an Algorithm/Feature

Each new algorithm addition should include, as applicable:
1. **Source file(s)** under `src/<domain>/` (e.g. `src/graphs/`, `src/data_structures/`), with type hints, docstrings, and a complexity analysis comment block.
2. **Tests** under `tests/test_<domain>.py`, covering the happy path, edge cases, and invalid/malicious input handling — targeting **100% coverage**.
3. **An ADR** under `docs/adr/NNNN-title.md` documenting the design decision and trade-offs (see existing ADRs for the format).
4. **README.md** updates: link the new ADR, and add a line under "Security, Stability & Privacy Considerations" if relevant.
5. **ROADMAP.md** updates: mark the item `(Completed)`.

## 4. Formatting & Local Verification

Run these before committing — a pre-commit hook enforces them anyway, but running locally first avoids failed commits:

```bash
.venv/bin/black src/ tests/
.venv/bin/pytest tests/ --cov=src --cov-report=term-missing
```

Confirm the coverage report shows 100% for all modified/added files.

## 5. Committing

Stage only the intended files — avoid committing incidental artifacts like `.coverage` diffs unless they're the actual subject of the change:

```bash
git add <changed files>
git commit -m "feat: <summary> (Phase N)

- Bullet point details of what was added.
- Reference tests, ADRs, and docs updates."
```

The repository's pre-commit hook re-runs `black --check` and the full `pytest` suite; a failure here blocks the commit until fixed.

## 6. Pushing & Opening a Pull Request (CLI)

```bash
git push -u origin feature/phase-3-topological-sort

gh pr create \
  --title "feat: <summary> (Phase N)" \
  --body "<concise description of what changed and why>" \
  --base main \
  --head feature/phase-3-topological-sort
```

> **Note on `gh` accounts:** if `gh` commands return `404 Not Found`, you may be authenticated as the wrong account. Check with `gh auth status` and switch with `gh auth switch --user <repo-owner-username>`.

## 7. Merging (CLI)

Once CI checks pass and the PR is reviewed/approved:

```bash
gh pr merge --squash --delete-branch
```

This squash-merges the PR into `main` and deletes the remote feature branch. (The repository also has **"Automatically delete head branches"** enabled in GitHub settings, so remote branches are cleaned up even if merged via the web UI.)

## 8. Post-Merge Local Cleanup

The remote branch is deleted automatically, but your local branch and remote-tracking refs are not — clean them up manually every time:

```bash
git checkout main
git pull origin main
git branch -d feature/phase-3-topological-sort   # safe delete, only works if merged
git fetch origin --prune                          # clears stale remote-tracking refs
```

## Quick Reference

| Step | Command |
|---|---|
| Sync main | `git checkout main && git pull origin main` |
| New branch | `git checkout -b feature/<name>` |
| Format | `.venv/bin/black src/ tests/` |
| Test + coverage | `.venv/bin/pytest tests/ --cov=src --cov-report=term-missing` |
| Push | `git push -u origin <branch>` |
| Open PR | `gh pr create --title "..." --body "..." --base main --head <branch>` |
| Merge PR | `gh pr merge --squash --delete-branch` |
| Cleanup | `git checkout main && git pull origin main && git branch -d <branch> && git fetch origin --prune` |
