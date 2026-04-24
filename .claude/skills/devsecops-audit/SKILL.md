---
name: devsecops-audit
description: Audits the repo's CI/CD and security posture using parallel specialist subagents, identifies gaps, and sets up missing infrastructure. Use when onboarding a repo to GitHub best practices or preparing for a compliance review.
---

# /devsecops-audit — DevSecOps Posture Audit

Audit the repo's CI/CD and security posture against fintech best practices using parallel specialist subagents. Identify gaps, then fix them one at a time.

**Do not create files speculatively.** Only create what is missing and justified by the audit findings.

---

## Phase 1 — Parallel audit

Spawn all five specialist subagents simultaneously:

```
Use the ci-audit, pr-hygiene-audit, secrets-audit, branch-protection-audit, and dependency-audit agents in parallel to audit this repo's DevSecOps posture.
```

Wait for all five results, then consolidate into a single findings table:

```
CI/CD pipeline:       [Risk|Note|OK] — [explanation]
PR hygiene:           [Risk|Note|OK] — [explanation]
Branch protection:    [Risk|Note|OK] — [explanation]
Secrets hygiene:      [Risk|Note|OK] — [explanation]
Dependency security:  [Risk|Note|OK] — [explanation]
```

Then ask: **"Fix all gaps, or select which to address first?"**

Do not proceed to implementation without confirmation.

---

## Phase 2 — Implementation rules

- Fix one gap at a time
- Run `.venv/bin/pytest tests/ -q` after any change to `app/` or `tests/`
- For `.github/` changes: explain what each file does and why
- Never commit secrets or credentials
- Branch protection rules cannot be set via files — provide the exact GitHub UI steps or `gh api` command instead

---

## GitHub Actions CI template (use when no workflow exists)

```yaml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ -q --tb=short
```

---

## PR template (use when no template exists)

```markdown
## Summary
<!-- What changed and why -->

## Test plan
- [ ] Tests pass locally: `pytest tests/ -q`
- [ ] New behavior tested manually in the UI
- [ ] No account numbers or routing numbers in logs

## Security checklist
- [ ] No sensitive fields exposed in error messages or logs
- [ ] Input validation at the route boundary (not deep in services)
- [ ] No new dependencies added without review

## Rollback
<!-- How to undo this change: revert files + server restart / migration rollback -->
```

---

## After each fix

Report:
```
FIXED:   .github/workflows/ci.yml — runs pytest on every PR
NEXT:    .github/pull_request_template.md
PENDING: branch protection (manual step in GitHub settings)
```
