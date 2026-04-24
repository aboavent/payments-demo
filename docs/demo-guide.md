# Demo Guide — FinTechCo Presentation

**Audience:** CTO (skeptical, security-conscious, 20+ yrs fintech) + Head of Digital Transformation (AI champion, productivity-focused)  
**Demo slot:** ~15 minutes  
**Narrative frame:** "A developer's first week at FinTechCo — from understanding the codebase to shipping a regulated feature safely."

---

## Before the demo

### Setup checklist

```bash
cd payments-demo
source .venv/bin/activate            # activate the virtual environment
bash scripts/demo-reset.sh          # restores baseline, confirms 10 tests pass
uvicorn app.main:app                 # NO --reload (see note below)
```

Open **http://127.0.0.1:8000** in a browser.

Verify:
- [ ] Page loads with empty form, empty alerts panel, empty audit log
- [ ] Claude Code is open in this directory (CLAUDE.md and skills are loaded)
- [ ] Tests pass: `.venv/bin/pytest tests/ -q` → 10 passed
- [ ] `app/services/alerts.py` — `check_suspicious_transfer()` body is **commented out**
- [ ] `app/services/ach.py` — import and call are **commented out**
- [ ] Terminal and browser are side by side on screen ← critical for Act 3

> **Important:** Run `uvicorn app.main:app` without `--reload`. The `--reload` watcher restarts the worker process on file changes, wiping the in-memory store mid-demo.

### Screen layout

Open **two terminal windows** before starting:
- **Terminal 1** — runs `uvicorn app.main:app` (server, stays open the whole demo)
- **Terminal 2** — free for git commands, resets, and watching the PostToolUse hook fire pytest

Arrange your screen in three columns:
```
┌─────────────────┬──────────────────────┬────────────────┐
│  Claude Code    │  Terminal 1 (server) │    Browser     │
│                 │  Terminal 2 (tests)  │  127.0.0.1:8000│
└─────────────────┴──────────────────────┴────────────────┘
```

This layout is critical for Act 3 — the audience watches Claude edit files on the left, pytest fire in Terminal 2 in the middle, and the live result in the browser on the right. Three things happening simultaneously without anyone orchestrating them.

### Reset between runs

```bash
source .venv/bin/activate
bash scripts/demo-reset.sh
uvicorn app.main:app
```

**What the reset script does — and why you don't need to delete the GitHub repo:**

After a full demo (Acts 1–4), the remote repo is in a "used" state:
- A `devsecops-hardening` branch exists on GitHub with CI, PR template, and validation code
- An open PR was created from that branch

If you try to run Act 4 again without resetting, `git push origin devsecops-hardening` and `gh pr create` will both fail because they already exist. The reset script handles this automatically:

| Step | What it resets |
|---|---|
| Stops uvicorn | Clears port 8000 |
| `git checkout -f main` | Discards all uncommitted changes, returns to baseline |
| Restores `ach.py` + `alerts.py` | Extension point stubs back to commented-out state |
| Removes `tests/test_alerts.py` | Test file belongs to the feature, not the baseline |
| Removes `.github/` | Must not exist at demo start — Claude creates it live in Act 4 |
| Closes open PR on GitHub | So `gh pr create` works cleanly on the next run |
| Deletes `devsecops-hardening` branch (remote + local) | So `git push origin devsecops-hardening` works cleanly |
| Runs pytest | Confirms 10 tests pass before you present |

**`origin/main` is never touched.** It is always the stable baseline. The reset script only cleans up the feature branch and its PR.

---

## Act 1 — Codebase exploration (2 min)

**What this shows:** Claude Code as an onboarding accelerator. Relevant to the CTO's concern about ramp time and knowledge transfer across 120 engineers.

### In the browser

Briefly show the UI — form, alerts panel, transfers table, audit log. Submit one transfer:
- Amount: `2500`, Originator: `Acme Corp`, Beneficiary: `Jane Doe`

Point to the audit log: "Every action is recorded — immutable event trail, exactly what a regulated environment requires."

### In Claude Code, type:

```
give me a quick architecture overview of this codebase
```

Claude describes the layered architecture (routes → services → repository), the in-memory store, and the extension point pattern.

**Narration:**
> "New engineer joins FinTechCo on Monday. Instead of a 2-hour walkthrough, they ask Claude Code. In 30 seconds they understand the data flow, the extension points, and what's safe to change. For a 120-person engineering organization, that onboarding acceleration compounds with every hire."

---

## Act 2 — Security review and bug fix (4 min)

**What this shows:** Claude Code as a compliance reviewer operating under a machine-readable policy. Directly targets the CTO's security concerns.

### Open CLAUDE.md — the key reframe

Before running any command, open `CLAUDE.md` briefly and point to the Security Expectations section.

**Narration:**
> "This is what makes Claude Code different from a generic coding assistant. CLAUDE.md is a machine-readable compliance policy. Your security team writes the rules once — which fields are sensitive, where validation must happen, what Claude is not allowed to do. Every session in this codebase is automatically bound by it."

### Enter Plan Mode first — the trust moment

Press **Shift+Tab** to enter Plan Mode (or type `/plan-mode`).

**Narration:**
> "Before we ask Claude to touch any code, I want to show you something your CTO will appreciate. This is Plan Mode — Claude can read and analyze the entire codebase, but it is physically incapable of writing a single file. This is read-only audit mode. Your security team can use this to ask Claude to review the codebase for compliance gaps, with a hard guarantee that nothing changes."

### In Claude Code (still in Plan Mode), type:

```
review the input validation in this app. is everything validated at the right layer?
```

Claude identifies that `routing_number` and `account_number` are validated only in the HTML form — not in `routes.py` at the server boundary. Any direct POST to `/transfers` bypasses all validation entirely.

**Narration:**
> "It found a real gap. Account numbers and routing numbers are regulated fields — they're explicitly called out in CLAUDE.md. A penetration tester would catch this. Claude caught it in seconds, in read-only mode, without touching a line of code."

### Exit Plan Mode and fix it

Press **Shift+Tab** again to exit Plan Mode. Then:

```
fix it — add server-side validation for routing_number and account_number in routes.py
```

Claude adds a 9-digit routing number check and non-empty account number check at the route boundary. The **PostToolUse hook fires pytest automatically** — visible in the terminal.

**Narration:**
> "It touched exactly one file. It didn't reformat adjacent code, didn't add abstractions, didn't expand scope. Surgical. And notice the terminal — tests ran automatically without anyone asking. That's a permanent project hook, not a demo configuration."

### Subagents — show the list (30 seconds)

After the fix, type `/agents` to show available subagents.

**Narration:**
> "For a more complex audit across multiple services — say, reviewing every microservice in your payments platform simultaneously — Claude delegates to specialized subagents automatically. Parallel analysis, one instruction. Think of them as specialist engineers Claude can spin up on demand."

Close `/agents` and move on. The live subagent demo happens in Act 4.

---

## Act 3 — Governed feature delivery (7 min)

**What this shows:** The 4-phase workflow as an enterprise governance layer. The main differentiator vs. Copilot/Cursor. The terminal and browser must both be visible.

**Narration before starting:**
> "Now I want to show you something you won't see in any other coding assistant. Not Claude writing code faster — Claude enforcing a *process* before writing code. This is what enterprise-scale adoption actually looks like."

### Step 1 — Spec

```
/spec   add suspicious transfer alerting
```

Claude produces a structured spec: problem statement, files affected, acceptance criteria, test plan, rollback notes.

**Narration:**
> "Before a single line of code is written, we have a documented spec saved to `docs/specs/`. This is Phase 2 of the 4-phase workflow encoded in CLAUDE.md. The spec is the contract — Claude cannot deviate from it during implementation."

Review the spec. Point out the acceptance criteria. Approve it.

### Step 2 — Plan

```
/plan
```

Claude breaks the spec into atomic tasks with explicit acceptance criteria and verification steps.

**Narration:**
> "Each task is independently testable and leaves the system in a working state. A junior engineer following this plan produces the same outcome as a senior engineer. That's what governance at scale looks like."

### Step 3 — Build (the two-terminal moment)

Make sure both terminals are visible. Terminal 1 shows the running server. Terminal 2 will show pytest firing.

```
/build   task 1
```

Claude modifies `alerts.py` then `ach.py`. After each file save, **Terminal 2 fires pytest automatically** via the PostToolUse hook — without anyone asking.

Point to Terminal 2 as it runs:

**Narration:**
> "Three things just happened simultaneously: Claude edited the file on the left, tests ran automatically in the middle terminal, and the server on the right is already serving the updated code. Nobody orchestrated that. The hook in `.claude/settings.json` enforces it permanently — it's not possible to ship broken code silently in this repo."

### Step 4 — Demo the feature in the browser

Submit a transfer in the browser (right side of screen):
- Amount: `15000`, Originator: `Acme Corp`, Beneficiary: `Jane Doe`

The **Alerts panel** populates immediately:
> Suspicious Transfer Detected — Transfer of $15,000.00 from 'Acme Corp' exceeds threshold.

Submit a transfer below threshold (`2500`). No alert.

**Narration:**
> "The fraud detection logic just went live — wired to the payment flow, tested, and visible in the UI. The data science team's fraud models follow the same pattern. Claude Code in Jupyter, same CLAUDE.md governance, same spec-driven process."

### Step 5 — Review and ship

```
/review
```

Claude checks correctness, security (are account/routing numbers in logs?), maintainability, operational risk.

```
/ship
```

**Narration:**
> "The /ship checklist is the answer to the question every CTO asks before a release: what changed, is it tested, what's the rollback path? It's explicit. Never assumed. And it's here because CLAUDE.md defines what 'done' means for this project."

---

## Act 4 — DevSecOps transformation (5 min) ✂️ cut if short on time

**What this shows:** Claude Code as a DevSecOps engineer — auditing a repo's CI/CD posture, identifying gaps, and setting up missing infrastructure. Closes the loop for the CTO: not just writing code safely, but governing the entire delivery pipeline.

**Requires pre-setup — see below.**

### Pre-setup (before the demo — do once)

```bash
# 1. Initialize git and push baseline to GitHub
git init
git add .
git commit -m "initial state: ACH Transfer Operations Portal"
gh repo create payments-demo --private --source=. --push

# 2. Confirm gh CLI is authenticated
gh auth status

# 3. Verify the repo has no .github/ folder (the gap Claude will find)
ls .github   # should say: No such file or directory
```

> The repo must be on GitHub with no `.github/` folder. That's the DevSecOps gap Claude will audit and fix live.

### Transition narration (bridge from Act 3)

> "We just shipped a feature safely — spec, tests, review, ship. But there's a broader question your CTO will ask: what does the *delivery pipeline* look like? Does this repo have CI? Branch protection? A PR template that enforces your security checklist? Let's find out."

### Step 1 — Parallel audit with subagents

In Claude Code, type:

```
/devsecops-audit
```

The skill explicitly spawns five specialist subagents simultaneously — one per audit axis. Watch Terminal 2: you will see five agents running in parallel.

Point to the agents as they start:

**Narration:**
> "Five specialist agents just spun up in parallel — ci-audit, pr-hygiene-audit, secrets-audit, branch-protection-audit, dependency-audit. Each one is reading a different part of the codebase simultaneously. This is agent composition: complex analysis decomposed into specialists, orchestrated by one command. For FinTechCo's platform with dozens of microservices, you'd run one command and get a compliance report across all of them."

Claude consolidates the five results into a findings table:
- **Risk:** no `.github/workflows/` — PRs merge without tests running
- **Risk:** no PR template — no enforced security checklist
- **Note:** branch protection — cannot verify from files, manual GitHub step required
- **OK:** secrets hygiene — `.gitignore` present, no hardcoded credentials
- **Note:** dependencies — versions pinned, no Dependabot configured

**Narration (after findings):**
> "Five axes audited in parallel, consolidated into one report. Every gap is actionable. Claude didn't need to be told what to look for — the agent definitions encode what a fintech repo must have. Your security team writes those definitions once."

> **Rehearsal note:** Confirm subagents spawn visibly during rehearsal. If for any reason they run sequentially, the fallback narration is: "Claude is auditing five compliance axes systematically — CI/CD pipeline, PR hygiene, branch protection, secrets hygiene, dependency security. Each one mapped to the requirements in CLAUDE.md."

### Step 2 — Fix: CI pipeline

Claude proposes the GitHub Actions workflow. Approve it.

Claude creates `.github/workflows/ci.yml` — runs pytest on every PR against `main`.

**Narration:**
> "From now on, no PR merges without tests passing. That constraint didn't exist 60 seconds ago."

### Step 3 — Fix: PR template

Claude creates `.github/pull_request_template.md` — includes test checklist, security checklist, rollback path.

**Narration:**
> "Every PR your 120 engineers open will now include a security checklist by default. Not a policy document — an enforced template that appears automatically in GitHub."

### Step 4 — Commit and open a PR

```bash
git checkout -b devsecops-hardening
git add .github/
git commit -m "add CI pipeline and PR template"
git push -u origin devsecops-hardening
gh pr create --fill
```

The PR opens in GitHub. Show the browser — the CI workflow is running, the PR template is pre-populated with the security checklist.

**Narration:**
> "The pipeline is live. The PR template is enforced. Claude Code didn't replace your DevSecOps engineer — it gave you one on demand, in five minutes, scoped exactly to what this repo needed."

### Step 5 — Fix: Branch protection

Run this in Terminal 2:

```bash
gh api repos/aboavent/payments-demo/branches/main/protection \
  --method PUT \
  --input - <<'EOF'
{
  "required_status_checks": {"strict": true, "checks": [{"context": "test"}]},
  "enforce_admins": true,
  "required_pull_request_reviews": {"required_approving_review_count": 1},
  "restrictions": null
}
EOF
```

**Narration:**
> "One command. Main is now locked — no PR merges without CI passing and one reviewer approving. Not a policy document, not a two-minute click in Settings — an enforced constraint applied programmatically. That's the difference between a rule someone might follow and a rule the platform enforces."

> **Note:** this requires the repo to be public (or GitHub Pro for private repos). `aboavent/payments-demo` is public — the command works as-is.

---

## Act 5 — Refactoring (2 min) ✂️ cut if short on time

**What this shows:** Claude Code improves code quality, not just adds features. Closes the full software lifecycle: understand → secure → build → ship → improve.

**When to run:** only if you have 2+ minutes after Act 4. Can also replace Act 4 if you want something more visual than git commands.

### Setup

After `/build` in Act 3, `ach.py` still has the `# --- DEMO EXTENSION POINT ---` comment block. The feature is live — the comment is now dead code. This is the refactor target. Nothing needs to be staged.

### In Claude Code, type:

```
/simplify
```

Claude will apply Chesterton's Fence — it reads `ach.py`, understands what the comment was for, confirms the feature is now active, and flags it as removable dead code.

**Narration:**
> "The feature is shipped. But Claude noticed something — the extension point comment that guided the implementation is now dead code. It's not needed anymore and it's adding noise. Before touching anything, Claude explains *why* the code was written that way and confirms it's safe to remove. That's Chesterton's Fence: understand before you change."

Claude removes the comment block. The PostToolUse hook fires pytest — 10 tests pass.

**Narration:**
> "One file. Tests still pass. Behavior unchanged. Claude doesn't just add things — it actively removes what's no longer needed. In a large codebase with 120 engineers, that discipline compounds. Technical debt doesn't accumulate silently."

Point to the terminal showing tests passing.

> "It couldn't introduce a regression here even if it tried — the hook would catch it immediately."

---

## Talking points by audience

### For the CTO (security, compliance, skepticism)

> "CLAUDE.md is a machine-readable compliance policy. Your security team writes it once. Every Claude Code session in this repo is bound by it automatically — sensitive fields, validation requirements, what Claude is not allowed to do."

> "Plan Mode gives you a hard read-only guarantee. Use it for compliance audits, security reviews, or onboarding — Claude analyzes everything and cannot change anything."

> "The PostToolUse hook means Claude physically cannot edit a file in `app/` without tests running. That's not a convention — it's an enforced constraint in `.claude/settings.json`."

> "Claude changed exactly two files to add this feature. Small, reviewable diff. That's what surgical changes look like at 120 engineers."

### For the Head of Digital Transformation (velocity, adoption)

> "New engineers productive in 30 seconds, not 2 hours. That ROI compounds with every hire."

> "The 4-phase workflow isn't Anthropic's idea — your team writes CLAUDE.md. You define the process; Claude enforces it across every session."

> "Your fraud detection team? Same tool, same governance, in Jupyter. No separate process for data scientists."

> "Subagents mean complex tasks get delegated automatically — parallel specialists, one instruction. That's where this is heading."

---

## If things go wrong

| Problem | Fix |
|---|---|
| Alerts not appearing | You have `--reload` running — `Ctrl+C`, run `bash scripts/demo-reset.sh`, restart without `--reload` |
| Tests fail after build | Show it as a feature: "Claude caught a regression before it shipped — that's the hook working" |
| Claude expands scope | Point to CLAUDE.md: "The compliance policy prevents silent scope creep — Claude flags it instead of doing it" |
| GitHub auth fails | Skip `gh pr create`, show `git diff --stat` and commit message — traceability story lands the same |
| Plan Mode not responding | Press `Shift+Tab` again — it toggles per session |
| Subagents don't spawn in Act 4 | Use fallback narration (sequential is fine) — don't break flow trying to force it |
| pytest not firing in Terminal 2 | Check `.claude/settings.json` hook is present; run `.venv/bin/pytest tests/ -q` manually instead |

---

## Time guide

| Act | Content | Time | Cuttable? |
|---|---|---|---|
| 1 | Codebase exploration | 2 min | No |
| 2 | Plan Mode + security review + bug fix | 4 min | No |
| 3 | Governed feature delivery (spec → build → ship) | 7 min | No |
| 4 | DevSecOps transformation (`/devsecops-audit`) | 5 min | Yes |
| 5 | Refactoring with `/simplify` | 2 min | Yes |
| **Core (Acts 1–3)** | | **13 min** | |
| **Full run (Acts 1–5)** | | **20 min** | |

**Cut decision guide:**
- 13 min available → Acts 1–3 only, close with `/ship` narration
- 15 min available → Acts 1–3 + Act 5 (refactor is faster and more visual than DevSecOps)
- 18 min available → Acts 1–4, skip Act 5
- 20 min available → all five acts

**Fallback (Option A):** if DevSecOps pre-setup wasn't done or time is tight, replace Act 4 with:
```bash
git diff --stat
gh pr create --fill
```
Narration: "One command — PR created, description generated from the commit. Claude Code fits inside your existing review workflow." (~2 min)

---

## Natural next questions to invite

> "What would the rollout plan look like for our 120 engineers?"  
> "How does this work with our existing GitHub Actions CI pipeline?"  
> "Can the data science team use this with Jupyter notebooks?"  
> "How do we control what CLAUDE.md says across teams?"

These are intentional open loops — they transition directly to your evaluation plan slide.
