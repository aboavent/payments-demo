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
- [ ] `app/services/alerts.py` — `check_suspicious_transfer()` returns `None` (stub, no logic)
- [ ] `app/services/ach.py` — `check_suspicious_transfer` is not imported or called
- [ ] Terminal and browser are side by side on screen ← critical for Act 3

> **Important:** Run `uvicorn app.main:app` without `--reload`. The `--reload` watcher restarts the worker process on file changes, wiping the in-memory store mid-demo.

### Screen layout

Open **two terminal windows** before starting:
- **Terminal 1** — runs `uvicorn app.main:app` (server, stays open the whole demo)
- **Terminal 2** — free for git commands, resets, and manual pytest runs

Arrange your screen in three columns:
```
┌─────────────────┬──────────────────────┬────────────────┐
│  Claude Code    │  Terminal 1 (server) │    Browser     │
│                 │  Terminal 2 (git/    │  127.0.0.1:8000│
│                 │  manual pytest)      │                │
└─────────────────┴──────────────────────┴────────────────┘
```

> **Note on pytest:** The PostToolUse hook fires pytest **inside the Claude Code terminal**, not in Terminal 2. You will see the test output scroll in the Claude Code pane after each file edit. Terminal 2 is for git commands (Act 4) and manual pytest runs — e.g. `.venv/bin/pytest tests/ -q` if you want to show the audience test output in a clean terminal.

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
| Restores `ach.py` + `alerts.py` | Back to stub state — `check_suspicious_transfer` returns `None`, not called from `ach.py` |
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

### Step 0 — Try to skip the workflow (45 seconds)

Try each command in order — each one is blocked until the previous phase is complete:

**Attempt 1:** Type `/build task 1` → refused:
```
⛔ No spec found in docs/specs/.
Run /spec first.
```

**Attempt 2:** Type `/plan` → refused:
```
⛔ No spec found in docs/specs/.
Run /spec first.
```

**Narration after both refusals:**
> "Both refused — build can't run without a plan, and plan can't run without a spec. Not because I set rules in this session — because the workflow is encoded in the skills themselves. And this goes all the way through. `/review` is blocked until `/build` completes. `/ship` is blocked until `/review` passes with no blocking issues. The full chain — spec → plan → build → review → ship — is enforced at every step, on disk, not in memory. A junior engineer joining FinTechCo on day one runs into the same gates as a senior. The governance is structural, not voluntary. That's the difference between a policy document and an enforced process."

### Step 1 — Spec

```
/spec   add suspicious transfer alerting
```

Claude produces a structured spec: problem statement, files affected, acceptance criteria, test plan, rollback notes. It identifies that `check_suspicious_transfer()` is a stub returning `None`, and that `ach.py` never calls it — so no alerting logic runs at all.

**Narration:**
> "Before a single line of code is written, we have a documented spec saved to `docs/specs/`. This is Phase 2 of the 4-phase workflow encoded in CLAUDE.md. The spec is the contract — Claude identified exactly what's missing, proposed the implementation, and cannot deviate from it during build."

Review the spec. Point out the acceptance criteria. Approve it.

### Step 2 — Plan

```
/plan
```

Claude breaks the spec into atomic tasks with explicit acceptance criteria and verification steps.

**Narration:**
> "Each task is independently testable and leaves the system in a working state. A junior engineer following this plan produces the same outcome as a senior engineer. That's what governance at scale looks like."

### Step 3 — Build (the live test moment)

Make sure Terminal 1 (server) and the browser are visible alongside Claude Code.

```
/build   task 1
/build   task 2
```

Run both tasks back-to-back. Task 1 implements the detection logic in `alerts.py` — reads the threshold from config and creates a `WARNING` alert. Task 2 wires the call into `ach.py` so it fires on every submitted transfer. **Both tasks are required before the feature is visible in the browser** — `alerts.py` alone does nothing until `ach.py` calls it.

After each file save, **pytest fires automatically inside the Claude Code terminal** via the PostToolUse hook — without anyone asking.

Point to the Claude Code pane as tests run:

**Narration:**
> "Notice what just happened in this terminal — Claude edited the file, and tests ran automatically without anyone asking. That's the PostToolUse hook in `.claude/settings.json`. It's a permanent constraint on this repo: every file change in `app/` triggers the test suite instantly. It's not possible to silently ship broken code here."

### Step 4 — Demo the feature in the browser

Once both `/build task 1` and `/build task 2` are complete, submit a transfer in the browser (right side of screen):
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

Claude checks correctness, security (are account/routing numbers in logs?), maintainability, operational risk. If review passes with no blocking issues, it writes `docs/plans/review.done` — the gate that unlocks `/ship`.

```
/ship
```

If you try `/ship` before `/review`, it refuses:
```
⛔ No review marker found at docs/plans/review.done.
Run /review first.
```

**Narration:**
> "Notice the sequence — `/ship` refused until `/review` completed cleanly. Not because I told it to wait, but because the chain is enforced on disk. Spec, plan, build, review, ship — every gate verified, every step traceable. The `/ship` checklist is the answer to the question every CTO asks before a release: what changed, is it tested, what's the rollback path? Explicit. Never assumed. Enforced by the process, not by convention."

---

## Act 4 — Data science workflow (3 min) ✂️ cut if short on time

**What this shows:** Claude Code is not a tool for software engineers only. The same governance model — same CLAUDE.md, same workflow discipline — applies to the 40 data scientists on the fraud detection, credit scoring, and customer behavior teams. Directly bridges the suspicious transfer alerting feature from Act 3 to the DS team's world.

**When to run:** After Act 3. No pre-setup required — this is a narrated walkthrough, not a live Jupyter build. Takes 3 minutes; can be shortened to 90 seconds with narration only.

### Transition narration

> "The suspicious transfer alerting feature we just built — threshold-based anomaly detection on ACH transfers — is a simplified version of exactly what your fraud detection data scientists build every day. Let me show you what Claude Code looks like in their environment."

### Step 1 — Show the DS scenario (narrated, no live coding required)

Narrate the following scenario while optionally showing a pre-existing Jupyter notebook (or just speaking to the slides):

**Scenario:** The fraud team asks: "Is our $10,000 alert threshold calibrated correctly against actual transfer patterns? Should it be higher or lower?"

In a typical DS workflow without Claude Code:
- Pull historical transfer data manually (hours of wrangling)
- Write EDA code from scratch
- Build a distribution analysis notebook
- Manually convert findings to a pipeline function
- Submit a PR with no spec, no review gate, no compliance check

**With Claude Code in Jupyter:**

> "The data scientist opens Claude Code in their notebook environment and types: 'analyze the distribution of historical ACH transfer amounts and recommend whether our $10,000 suspicious transfer threshold is well-calibrated.' Claude reads the data, runs the analysis, produces a visualization, and — critically — flags that the routing number column should not appear in the output. That flag comes from CLAUDE.md — the same compliance policy that governed the payments service."

**Narration:**
> "Same tool. Same governance. The data scientist didn't configure anything differently. CLAUDE.md traveled with the operating model. The fraud team gets the EDA done in minutes instead of hours, the compliance rule was enforced automatically, and the output is ready to promote to a production pipeline."

### Step 2 — The pipeline bridge (30 seconds)

> "When the analysis is complete, the DS asks Claude: 'convert this notebook into a production-ready pipeline function.' Claude generates the pipeline code. The DS submits it as a PR — through the same GitHub Actions CI the SE team uses, the same PR template with the security checklist, the same branch protection that requires a reviewer. One operating model. Three teams."

### Step 3 — The 1–2 days statistic

Point to the stat from the Anthropic customer (Intercom VP of AI):

**Narration:**
> "'This process saves 1–2 days of routine work per model.' At 40 data scientists, even recovering one day per week per person is 40 DS-days per week — 2,000 days per year — available for new model development instead of pipeline boilerplate. That's faster fraud detection. Better credit scoring models. More accurate customer behavior analysis. Not because the data scientists are more skilled — because the operating model removed the friction that was wasting their time."

---

## Act 5 — DevSecOps transformation (5 min) ✂️ cut if short on time

> **Note:** Previously Act 4. Renumbered to accommodate the DS workflow act.

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

Claude stops after creating the files — it does not commit. You run these commands in Terminal 2:

```bash
git checkout -b devsecops-hardening
git add .github/ .gitignore requirements.txt
git commit -m "add CI pipeline, PR template, and security hardening"
git push -u origin devsecops-hardening
gh pr create \
  --title "Add CI pipeline, PR template, and security hardening" \
  --body "$(cat <<'EOF'
## Summary
Add CI pipeline, PR template, Dependabot, and secrets hardening.

## Test plan
- [x] Tests pass locally: `pytest tests/ -q`
- [x] New behavior tested manually in the UI
- [x] No account numbers or routing numbers in logs

## Security checklist
- [x] No sensitive fields exposed in error messages or logs
- [x] Input validation at the route boundary (not deep in services)
- [x] No new dependencies added without review

## Rollback
Revert .github/ and requirements.txt. Server restart not required.
EOF
)"
```

`gh pr create` prints the PR URL — keep it handy for Step 6.

> **If `git checkout -b devsecops-hardening` fails** with "branch already exists", the reset script did not run cleanly. Run `bash scripts/demo-reset.sh` to clean up, then retry.

> **Do NOT open the browser yet.** Run Step 5 first — branch protection must be in place before you show the PR, otherwise the blocked merge won't appear and Step 6 falls flat.

**Narration:**
> "The pipeline is live. The PR template is enforced — notice the security checklist is already there, pre-populated. And this is the PR that *introduced* the template. Every PR your 120 engineers open from now on gets this automatically. Claude Code didn't replace your DevSecOps engineer — it gave you one on demand, in five minutes, scoped exactly to what this repo needed."

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

### Step 6 — Show the results in GitHub

Switch to the browser. Walk through three things:

**1. The open PR**
Go to `https://github.com/aboavent/payments-demo/pulls` → open the PR.

Point out:
- The PR description has the security checklist pre-populated from the template — every PR your 120 engineers open gets this automatically
- CI passed (green check) — tests ran automatically on push
- "Review required" badge is red and merging is blocked — point to this directly

**Narration:**
> "Notice merging is blocked — CI passed but there's no reviewer yet. That's the rule working exactly as intended. In a 120-engineer org, a second set of eyes is required before anything touches main. Not optional, not a convention — enforced by the platform. The security checklist in the description? Pre-populated automatically from the template we created five minutes ago."

> **Presenter note:** You're the sole collaborator so you can't approve your own PR — that's by design in GitHub. Don't try to work around it. The blocked state is the demo payoff, not a problem. Leave the PR open and move on.

**2. The CI workflow running**
Go to `https://github.com/aboavent/payments-demo/actions`.

Point out:
- The workflow triggered automatically on push — no one scheduled it
- It's running pytest against the real codebase, not a mock

**Narration:**
> "Automated test gate, live. From now on a broken PR can't reach main — the pipeline catches it first."

**3. Branch protection on main**
Go to `https://github.com/aboavent/payments-demo/settings/branches` → click the edit (pencil) icon next to the `main` rule.

Point out (no changes needed — everything is already set by the `gh api` command):
- Branch name pattern: `main` — applies to exactly 1 branch
- Require a pull request before merging ✓
- Require approvals: 1 ✓
- Require status checks to pass ✓ — `test` (the CI job) is already listed under "Status checks that are required"
- Require branches to be up to date ✓
- Enforce admins ✓ — not visible in the UI but set via the API; even the repo owner can't bypass

**Narration:**
> "Pull request required. One reviewer. CI must pass — and you can see the specific check: `test`, the exact job name from the workflow we just created. Branches must be up to date. Admins included. Every one of these was set by a single `gh api` command 60 seconds ago — no UI clicking, no ticket to your platform team. That's the difference between a policy someone might follow and a constraint the platform enforces."

**Closing narration — merge the PR and bridge to Act 6:**
> "The pipeline is in place. Now merge this PR — once it lands on main, every future PR gets CI, the security checklist, and branch protection automatically. The feature we built in Act 3 is waiting. Let's ship it the right way."

In the browser, merge the `devsecops-hardening` PR using **Merge as admin** (the override button at the bottom of the PR).

> **Presenter note:** Using admin override here is intentional and worth narrating: "I'm merging as admin because I'm the only collaborator — in a real org, a teammate would approve it. The rule is enforced; I'm just the exception the platform allows."

---

## Act 6 — Refactoring + shipping through the pipeline (2 min) ✂️ cut if short on time

**What this shows:** Claude Code cleans up code after a feature ships, then commits the full feature work through the pipeline Act 5 just established. Closes the full software lifecycle: understand → secure → build → ship → improve → merge.

**When to run:** only if you have 2+ minutes after Act 5. Requires the `devsecops-hardening` PR to be merged first (done at the end of Act 5 above).

### Step 1 — Refactor with `/refactor`

After Act 3, `ach.py` has a local import inside the function body (`from app.services.alerts import check_suspicious_transfer`). It was written that way intentionally — keeping each build task isolated. Now that the feature is complete, Claude can propose moving it to the standard top-level location.

In Claude Code, type:

```
/refactor
```

Claude reads `ach.py`, identifies the unconventional local import, explains why it was written that way during the build phase, and proposes moving it to the top of the file alongside the other imports.

**Narration:**
> "The feature works. But Claude noticed something worth cleaning up — the import is inside the function body rather than at the top of the file. It was written that way during build to keep each task self-contained. Now that it's complete, Claude proposes the standard pattern. Before touching anything, it explains *why* the code was written that way and confirms the move is safe. That's the discipline that keeps a 120-engineer codebase clean: understand before you change."

Claude moves the import. The PostToolUse hook fires pytest — 13 tests pass.

**Narration:**
> "One file, one line moved. Tests still pass. Behavior unchanged. Claude doesn't just add things — it actively improves what's already there. Technical debt doesn't accumulate silently."

### Step 2 — Commit the feature through the pipeline

Now ship everything from Act 3 through the process Act 4 just established. Run in Terminal 2:

```bash
git checkout -b feature/suspicious-transfer-alerting
git add app/services/ach.py app/services/alerts.py app/routes.py tests/test_alerts.py
git commit -m "implement suspicious transfer alerting and route validation"
git push -u origin feature/suspicious-transfer-alerting
gh pr create \
  --title "Implement suspicious transfer alerting and route validation" \
  --body "$(cat <<'EOF'
## Summary
Implement threshold-based suspicious transfer alerting and server-side input validation.

## Test plan
- [x] Tests pass locally: `pytest tests/ -q`
- [x] Alerts panel shows WARNING for transfers >= $10,000
- [x] No account numbers or routing numbers in logs

## Security checklist
- [x] No sensitive fields exposed in error messages or logs
- [x] Input validation at the route boundary (not deep in services)
- [x] No new dependencies added without review

## Rollback
Revert app/services/ach.py, app/services/alerts.py, app/routes.py. Server restart resets in-memory store.
EOF
)"
```

Open the PR URL in the browser. CI runs automatically. Merging is blocked until a reviewer approves.

**Narration:**
> "The feature built in Act 3 is now going through the pipeline we set up in Act 4. CI is running, the security checklist is pre-populated, merging is blocked until a reviewer approves. That's the full picture: Claude Code helped us build the right thing, reviewed and tested it, hardened the delivery pipeline, and now the feature ships through that pipeline. Every step governed. Nothing assumed."

---

## Talking points by audience

### For the CTO (security, compliance, skepticism)

> "CLAUDE.md is a machine-readable compliance policy. Your security team writes it once. Every Claude Code session in this repo is bound by it automatically — sensitive fields, validation requirements, what Claude is not allowed to do."

> "Plan Mode gives you a hard read-only guarantee. Use it for compliance audits, security reviews, or onboarding — Claude analyzes everything and cannot change anything."

> "The PostToolUse hook means Claude physically cannot edit a file in `app/` without tests running. That's not a convention — it's an enforced constraint in `.claude/settings.json`."

> "Claude changed exactly two files to add this feature. Small, reviewable diff. That's what surgical changes look like at 120 engineers."

> "The full delivery chain — spec → plan → build → review → ship — is enforced at every step by on-disk markers, not session memory. There is no way to skip review and ship. There is no way to build without a spec. A junior engineer on day one is bound by the same gates as a senior. That's governance that scales."

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
| 4 | Data science workflow (Jupyter / DS team story) | 3 min | Yes |
| 5 | DevSecOps transformation (`/devsecops-audit`) | 5 min | Yes |
| 6 | Refactor + ship feature through the pipeline | 2 min | Yes |
| **Core (Acts 1–3)** | | **13 min** | |
| **Full run (Acts 1–6)** | | **23 min** | |

**Cut decision guide:**
- 13 min available → Acts 1–3 only, close with `/ship` narration
- 16 min available → Acts 1–3 + Act 4 (DS story — adds audience coverage without setup risk)
- 18 min available → Acts 1–3 + Act 5 (DevSecOps — skip Act 4 if skipping DS story)
- 20 min available → Acts 1–5
- 23 min available → all six acts

> **Act 4 (DS):** narrated — no live coding, no pre-setup. Safest optional act to add when you have 3 extra minutes.
> **Act 6 dependency:** requires the `devsecops-hardening` PR from Act 5 to be merged before running. If you skip Act 5, skip Act 6 too.

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
