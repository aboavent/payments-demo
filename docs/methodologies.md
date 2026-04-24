# Methodologies

How the Karpathy guidelines, Addy Osmani agent-skills, and the AgentFactory 4-phase workflow were adapted for this project — what was taken, what was left out, and why.

---

## Sources

| Source | What it is |
|---|---|
| Karpathy guidelines | Behavioral rules derived from Andrej Karpathy's observations on common LLM coding mistakes |
| Addy Osmani agent-skills | A production-grade skill library covering the full software development lifecycle |
| AgentFactory 4-phase workflow | Research → Specification → Refinement → Implementation |

None of these were copied verbatim. Each was read, distilled, and adapted for a small fintech demo repo.

---

## Karpathy Guidelines

### What the guidelines say

Andrej Karpathy identified a set of recurring failure modes in LLM-assisted coding:

1. **Not thinking before coding** — jumping to implementation before understanding the problem
2. **Over-complication** — adding abstractions, configurability, and features that weren't asked for
3. **Broad changes instead of surgical ones** — touching adjacent code, reformatting, refactoring things that weren't broken
4. **No verifiable success criteria** — "make it work" is not a goal; "the test passes" is
5. **Guessing instead of asking** — silently picking one interpretation when multiple exist

His prescription maps to four principles:
- Think before coding
- Simplicity first
- Surgical changes
- Goal-driven execution (define success, then loop until verified)

### How they were applied here

Every principle appears verbatim as a rule in `CLAUDE.md`:

| Karpathy principle | How it appears in CLAUDE.md |
|---|---|
| Think before coding | "State assumptions explicitly. If uncertain, ask — don't guess silently." |
| Simplicity first | "Write the minimum code that solves the problem. Three similar lines are better than a premature abstraction." |
| Surgical changes | "Touch only what the task requires. Every changed line must trace directly to the task." |
| Goal-driven execution | "Define what 'done' means before writing a line." + Definition of Done checklist |
| Surface tradeoffs | Explicit format: "Option A is simpler but doesn't handle X. Option B handles X but adds N lines. I'll go with A unless you say otherwise." |

The `/build` skill reinforces surgical changes with a scope creep check:
```
NOTICED BUT NOT TOUCHING: [description]
→ Want me to create a follow-up task?
```

The `/simplify` skill operationalizes the "simplicity first" principle as a post-feature pass, not a during-feature distraction.

### What was left out

Karpathy's guidelines are general-purpose. Several aspects weren't relevant to a small demo repo:
- Multi-step plan format with per-step verifications (useful for large features; overkill here)
- The full "loop until verified" framework (pytest auto-running via the hook handles this)
- Warning about over-testing and mocking (not a risk at this scale)

---

## Addy Osmani Agent-Skills

### What the library is

Addy Osmani's [agent-skills](https://github.com/addyosmani/agent-skills) is a library of 21 production-grade skills covering the full software development lifecycle, organized by phase:

- **Define:** spec-driven-development, idea-refine
- **Plan:** planning-and-task-breakdown
- **Build:** incremental-implementation, test-driven-development, context-engineering, source-driven-development, frontend-ui-engineering, api-and-interface-design
- **Verify:** browser-testing-with-devtools, debugging-and-error-recovery
- **Review:** code-review-and-quality, code-simplification, security-and-hardening, performance-optimization
- **Ship:** git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, shipping-and-launch

Each skill follows a consistent structure:
- YAML frontmatter (`name`, `description`)
- Overview
- When to use / when not to use
- Process (step-by-step)
- Common rationalizations (the excuses people make to skip the skill)
- Red flags (signs the skill is needed)
- Verification checklist

### What was taken

Seven skills were adapted and collapsed into this repo's seven skills:

| Addy skill | This repo's skill | What was kept | What was removed |
|---|---|---|---|
| `spec-driven-development` | `/spec` | Gated workflow, assumption surfacing, lightweight mode for small tasks | Full 6-part spec template (too heavy for a demo repo), living document lifecycle |
| `planning-and-task-breakdown` | `/plan` | Vertical slicing, dependency ordering, task format with acceptance criteria, checkpoints | Parallelization details, multi-agent coordination, XL-size breakdown |
| `incremental-implementation` | `/build` | One slice at a time, scope discipline, scope creep reporting | Feature flag strategy, contract-first slicing, Rule of 500 |
| `test-driven-development` + coverage | `/test` | Run and report, propose missing cases, test naming guidelines | TDD red-green-refactor cycle (tests are already written here) |
| `code-review-and-quality` | `/review` | Five-axis review, verdict format, dead code hygiene | Multi-model review pattern, change sizing/splitting guidance, review speed SLAs |
| `shipping-and-launch` | `/ship` | Pre-ship checklist, rollback plan format, next steps | Staged rollout, feature flags, CDN/infrastructure checks |
| `code-simplification` | `/simplify` | Chesterton's Fence, signal/pattern table, Python examples, behavior preservation rule | Rule of 500, TypeScript/React examples, automated codemod guidance |

### Key ideas preserved

**Chesterton's Fence** (from `/simplify`): Before removing or changing anything, understand why it exists. If you can't explain why the fence is there, don't tear it down.

**Vertical slicing** (from `/plan`): Build one complete working path before building the next. Don't build all the DB, then all the API, then all the UI — build one user-visible flow end to end.

**Scope discipline** (from `/build`): "NOTICED BUT NOT TOUCHING." Scope creep is reported, not acted on silently.

**Lightweight mode** (from `/spec`): The spec-driven-development skill explicitly says small tasks don't need long specs — they need acceptance criteria. This repo operationalizes that as a two-line lightweight spec.

**Context isolation** (from `context-engineering`): Research investigates four independent tracks (architecture, tests, alerts/audit, security) before converging on a spec. Each track asks different questions.

### What was left out

Most of the library is irrelevant for a small demo:
- Frontend skills (browser testing, UI engineering) — the UI is static templates
- CI/CD skills — no pipeline exists
- Git workflow skills — single-branch demo, no PR process
- API design skills — one internal route, no external API
- Performance optimization — not a concern at this scale

The common rationalizations and red flags sections in each skill were condensed or omitted. They're valuable in a large team context; in a demo they add length without adding clarity.

---

## AgentFactory 4-Phase Workflow

### What it is

The AgentFactory workflow structures all non-trivial AI-assisted development into four phases with explicit gates between them:

```
Research → Specification → Refinement → Implementation
```

The core insight: most AI coding mistakes happen in the first five seconds — the moment the model starts typing without understanding the problem. The workflow forces a pause at each gate.

### Phase descriptions

**Phase 1 — Research**  
Read-only investigation. Understand the existing architecture, test coverage, data flow, and risk profile before proposing anything. Parallel investigation tracks allow independent questions to be answered concurrently.

**Phase 2 — Specification**  
Write a structured spec before any code. The spec makes assumptions visible, defines what "done" means, and creates a shared reference point. Code written before spec approval is discarded — the spec is the gate.

**Phase 3 — Refinement**  
Ask the one highest-leverage unanswered question. Not five — one. This constraint forces prioritization and prevents the refinement phase from becoming a waterfall requirements session. Surface assumptions and operational risks. Resolve ambiguities. Then lock the spec.

**Phase 4 — Implementation**  
Execute the approved spec in atomic tasks. Implement one slice, test it, verify it, then move to the next. The phase has its own internal cycle:

```
Plan → Build (one task) → Test → Review → Ship
```

Each step has a corresponding skill. The hook provides automatic test feedback between steps.

### Decision framework

The workflow has two modes to avoid ceremony on small tasks:

| Mode | When to use | What to do |
|---|---|---|
| Full 4-phase | Multi-file, ambiguous requirements, medium/high risk | All four phases with gates |
| Lightweight | Single-file, obvious fix, low risk | Constraints + success criteria, then implement |

The decision framework appears at the top of the Workflow section in `CLAUDE.md` so it's applied at the start of every task, not as an afterthought.

### How it was encoded in this repo

| Phase | Encoding |
|---|---|
| Research | `CLAUDE.md` Phase 1 section with parallel investigation track table |
| Specification | `/spec` skill with full and lightweight modes |
| Refinement | `CLAUDE.md` Phase 3 section: "ask only the one highest-leverage question" |
| Implementation | `/plan` → `/build` → `/test` → `/review` → `/ship` skill chain |

The hook provides automatic backpressure: every file edit triggers pytest, making the test-verify step in Phase 4 happen without requiring a deliberate decision.

---

## Spec-Driven Development principles applied

These six principles from the spec-driven development literature shaped the overall design:

### 1. CLAUDE.md as project constitution
`CLAUDE.md` is not a hint file or a style guide. It defines how work is done: architecture rules, quality standards, security expectations, workflow rules, and definition of done. Everything an AI agent needs to know to work correctly in this repo lives there. It is loaded at the start of every Claude Code session.

### 2. Decision framework
Ceremony should be proportional to risk. The full workflow adds value when requirements are unclear or when a change crosses multiple components. Lightweight mode prevents the workflow from becoming friction on trivial changes. Both modes are explicit in `CLAUDE.md`.

### 3. Review the plan, not just the code
`/review` inspects assumptions, scope control, and operational risk — not just whether the code compiles. A change that implements exactly what was asked but violates an unstated assumption is still a bad change. The review catches that.

### 4. Backpressure via hooks
The PostToolUse hook is the backpressure mechanism. It slows down bad changes (by surfacing test failures immediately) and speeds up reliable delivery (by removing the need to manually trigger tests). Good changes get confirmed fast; bad changes get caught fast.

### 5. Context isolation during research
The four investigation tracks in Phase 1 (architecture, tests, alerts/audit, security) are kept separate deliberately. Mixing them produces muddled research. Architecture questions have different answers than security questions for the same file.

### 6. Lightweight spec mode
A two-line spec — constraints + success criteria — is better than no spec. It takes 30 seconds and eliminates the most common class of implementation mistake: building the right code for the wrong problem.

---

## How these methodologies fit together

They address different layers of the same problem:

| Methodology | Layer it addresses |
|---|---|
| Karpathy guidelines | **Behavioral** — how the model should think and act moment-to-moment |
| Addy Osmani agent-skills | **Operational** — what to do at each phase of the development lifecycle |
| 4-phase workflow | **Structural** — when to do each thing, in what order, with what gates |
| Spec-driven development | **Philosophical** — why written specs before code produces better outcomes |

In practice: the 4-phase workflow provides the structure, the skills operationalize each phase, the Karpathy principles govern behavior within each phase, and the spec-driven philosophy explains why the whole thing is worth doing.
