# Claude Code at FinTechCo — Presentation Brief
## Source document for NotebookLM slide and infographic generation

**Central thesis:** Discipline beats raw intelligence.
The best outcomes from AI-assisted engineering come not from the model's raw capability, but from combining that capability with structured workflows, machine-readable standards, and enforced governance. Claude Code is the platform that makes this combination concrete.

**Core positioning (never say "coding assistant"):**
> Claude Code is an enterprise software delivery platform that helps technical teams ship faster with more control.

**Audience:** CTO (skeptical, security-conscious, 20+ years fintech) + Head of Digital Transformation (AI champion, productivity focus) + technical stakeholders
**Meeting format:** 40-minute mock customer meeting
**Demo app:** ACH Transfer Operations Portal — internal fintech payment processing tool (Python/FastAPI)

---

## Section 0 — The Winning Perception

The goal of this presentation is not to convince the audience that Claude Code writes code. They already know AI can write code. The goal is to convince them of something harder:

> "This person understands not just AI tools, but how to operationalize them in a real enterprise."

That distinction separates a tool evaluation from a strategic conversation. Every slide should advance it.

Three questions every executive in the room is asking:
1. **CTO:** "Will this create risk or reduce it?"
2. **Head of DT:** "Can I actually get 180 engineers to adopt this?"
3. **Both:** "What does the ROI look like and how do I measure it?"

Every section of this deck must answer at least one of these questions.

---

## Section 1 — Market Reality: The Vibe Coding Trap

### What's happening
AI coding tools have proliferated across the industry. GitHub Copilot, Cursor, Codeium, Tabnine, ChatGPT — most engineering organizations are already using at least one. The question is no longer "should we use AI?" It's "are we using it in a way that compounds or creates risk?"

### The vibe coding problem
"Vibe coding" — a term coined by AI researcher Andrej Karpathy — describes the dominant pattern of AI adoption in engineering teams today:

- Developer has a task
- Developer prompts an AI assistant with a natural language description
- AI generates code
- Developer accepts, tweaks, ships

**What vibe coding produces at small scale:** faster first drafts, happy developers, impressive demos.

**What vibe coding produces at enterprise scale:**
- Inconsistent quality — output quality varies by how well each developer prompts
- Accumulated technical debt — AI-generated code without review tends to be verbose, over-engineered, or inconsistently styled
- Security gaps — AI assistants without domain-specific constraints will generate code that violates compliance rules (e.g., logging sensitive fields, client-side-only validation)
- No repeatability — one senior developer gets great results; a junior developer on the same team gets inconsistent ones
- Unmeasurable ROI — when every developer uses AI differently, there's no common baseline to measure against

### The enterprise AI paradox
Most companies evaluating AI coding tools are measuring the wrong thing: "how much code does it write?" The right question is: "how much good code reaches production with fewer defects and faster review cycles?"

Fast code generation + poor governance = faster accumulation of problems.

**Benchmark context (external research):**
- GitHub/Microsoft (2023): developers complete tasks 55% faster with AI assistance — but this measures task completion speed, not production quality
- McKinsey (2023): top-quartile teams see 20–45% productivity improvement from AI-assisted development, but only when paired with structured review practices
- DORA Report (2024): high-performing engineering teams deploy 208x more frequently and have 106x faster lead times than low performers — the differentiator is not tools, it's process maturity
- Accenture (2023, "A new era of generative AI for everyone"): 40% of all working hours across industries could be impacted by large language models — engineering is among the highest-impact functions
- Deloitte (2024, "Now decides next"): organizations that pair AI tools with redesigned workflows see 3–4x the productivity benefit of those that simply layer AI onto existing processes — the operating model is the differentiator
- World Economic Forum (2023): reskilling and workflow redesign, not tool access alone, determine which organizations capture AI productivity gains at scale

### The key insight
AI tools amplify what's already there. In a team with strong engineering practices, AI accelerates delivery. In a team without them, AI accelerates the accumulation of debt. **The operating model is the multiplier, not the model.**

---

**SLIDE CUE — Slide 2: Market Reality**
Title: "AI Coding Is Everywhere. Most Teams Are Using It Wrong."
Visual: Split comparison — "Vibe Coding" (chaotic arrows, random prompts, inconsistent output) vs. "Structured Delivery" (clean pipeline, spec → plan → build → review → ship)
Key stat: 55% faster task completion (GitHub/Microsoft) — but only with structured practices does this translate to production ROI
Speaker note: "The question isn't whether your engineers are using AI. They are. The question is whether they're using it in a way that compounds or creates risk."

---

## Section 2 — The Maturity Arc: From Vibe Coding to Structured Delivery

### Stage 1: Vibe Coding (ad hoc prompting)
**What it looks like:**
- Individual developers use AI assistants independently, each with their own prompting style
- No shared standards, no enforced review, no common output quality
- Results vary dramatically by developer skill and prompting experience
- AI is a productivity tool for individuals, not a capability multiplier for the team

**Observable symptoms:** "It works great for Alice but Bob can't get useful output." High variance in PR quality. Code review catching AI-generated anti-patterns repeatedly.

### Stage 2: Guided Prompting (shared conventions)
**What it looks like:**
- Team establishes informal prompting guidelines ("always ask Claude to write tests")
- Some developers sharing effective prompts via Slack or internal wikis
- Still individual-level, still inconsistent, but beginning to converge

**Observable symptoms:** Tribal knowledge about "how to use AI well" concentrated in a few senior developers. Onboarding still slow. No enforcement mechanism.

### Stage 3: Workflow Integration (tool + process)
**What it looks like:**
- AI assistant integrated into the development workflow, not just used ad hoc
- Standards encoded in configuration files (e.g., CLAUDE.md)
- Hooks enforce automated quality gates (tests run on every file change)
- Skills encode repeatable workflows (spec, plan, build, review, ship)
- Junior engineers follow the same process as seniors — governance is structural

**Observable symptoms:** Consistent PR quality. Onboarding time drops dramatically. Review cycles get faster because code arrives with tests and a spec already attached.

### Stage 4: Operating Model (AI as delivery infrastructure)
**What it looks like:**
- CLAUDE.md is maintained by the engineering leadership team as a living compliance document
- Skills are owned by tech leads and updated as standards evolve
- Metrics are tracked: cycle time, defect escape rate, onboarding time, review turnaround
- AI is not a developer tool — it's a delivery platform the whole engineering organization runs on

**Observable symptoms:** New engineers submit their first meaningful PR in days, not weeks. Feature cycle times are predictable. The CTO can look at a metric dashboard and see AI's impact on delivery outcomes.

### Where most enterprises are today
Stage 1–2. The teams getting real ROI are at Stage 3. Stage 4 is where the compounding returns are.

**The good news for FinTechCo:** the infrastructure to move from Stage 1 to Stage 3 is CLAUDE.md + skills + hooks. It can be set up in a single sprint. The demo will show this live.

---

**SLIDE CUE — Slide 3: The Maturity Arc**
Title: "From Vibe Coding to Structured Engineering"
Visual: Horizontal maturity arc with 4 stages, icons for each. Arrow points right. FinTechCo target highlighted at Stage 3/4.
Comparison table:

| | Vibe Coding | Structured Delivery |
|---|---|---|
| Quality | Varies by developer | Governed by standards |
| Review | Catches AI mistakes | Validates AI outputs |
| Onboarding | Still weeks | Days to first PR |
| ROI | Individual | Organizational |
| Risk | Uncontrolled | Structurally mitigated |

Speaker note: "Most teams buy a model. The teams getting real ROI build an operating model."

---

## Section 3 — Claude Code as Enterprise Delivery Platform

### Why "coding assistant" is the wrong frame
Coding assistants answer questions and autocomplete lines. That's table stakes. Claude Code operates differently:

- It reads and understands your entire codebase — not just the file you have open
- It can execute multi-step tasks autonomously: read code, run tests, fix failures, commit changes
- It enforces your team's standards on every session, not just when you remember to ask
- It spans the full software delivery lifecycle

### The full SDLC coverage
Claude Code creates value at every stage of software delivery — not just the "write code" phase:

| Phase | Claude Code capability | FinTechCo application |
|---|---|---|
| **Discover** | Codebase exploration, dependency mapping, legacy code analysis | New engineer onboards to the ACH system; Claude maps the entire data flow in 30 seconds |
| **Design** | Spec generation, architecture review, tech debt identification | `/spec` produces a structured implementation spec before any code is written |
| **Build** | Incremental implementation, test generation, scope enforcement | `/build` implements one atomic task at a time; PostToolUse hook runs tests after every file change |
| **Deploy** | CI/CD pipeline setup, branch protection, PR template enforcement | `/devsecops-audit` audits and fixes the entire delivery pipeline in one command |
| **Support & Scale** | Incident investigation, runbook generation, large-scale refactoring | Ramp: 80% reduction in incident investigation time |

### What makes Claude Code different from Copilot and Cursor

| Capability | GitHub Copilot | Cursor | Claude Code |
|---|---|---|---|
| Codebase understanding | File-level context | Project-level | Full repo + history |
| Workflow enforcement | None | None | CLAUDE.md + skills + hooks |
| Agentic task execution | Limited | Limited | Multi-step autonomous |
| Compliance policy | None | None | Machine-readable via CLAUDE.md |
| Enterprise controls | Basic | Basic | Bedrock/Vertex, corporate proxy, centralized permissions |
| Subagent orchestration | No | No | Yes — parallel specialist agents |

### Customer validation (from Anthropic)
- **Ramp:** "Engineers would try it on their own and have such a transformative experience that they felt compelled to share with their colleagues." — Austin Ray, Senior SWE. Result: 50% weekly active usage across the engineering team; became the default development tool within 30 days.
- **Intercom:** "Claude Code enables us to build applications we wouldn't have had bandwidth for — from AI labeling tools to ROI calculators for our Sales team." — Fergal Reid, VP of AI
- **Shopify:** "Claude Code is pre-installed on everyone's laptop. It's pre-configured with the rules, the tokens, the authentication. It just works out of the box." — Scott MacVicar, Head of Dev Infra
- **Fortune 500 industrial tech:** 81% of developers satisfied or very satisfied. 79% experienced increased development efficiency. 64% would recommend for large-scale codebase modernization.

---

**SLIDE CUE — Slide 4: Why Claude Code**
Title: "Claude Code: Enterprise Software Delivery Platform"
Visual: SDLC ring (Discover → Design → Build → Deploy → Support) with Claude Code at center. Each phase has 2–3 bullet capabilities.
Customer logos/quotes: Ramp, Intercom, Shopify, Fortune 500 industrial.
Speaker note: "This isn't autocomplete. This is an agent that reads your entire codebase, enforces your standards, runs your tests, sets up your pipeline, and helps every engineer — junior or senior — deliver at the quality bar your compliance team requires."

---

## Section 4 — AI Needs an Operating Model, Not Just a Model

### The operating model concept
A model answers questions. An operating model encodes your organization's judgment, compliance rules, delivery standards, and quality expectations into every session — automatically, without relying on individual developers to remember.

The three artifacts that constitute an operating model in Claude Code:

**1. CLAUDE.md — the machine-readable compliance policy**
A markdown file checked into the repo that Claude reads at the start of every session. It defines:
- Architecture and data flow (so Claude never proposes changes that violate the system design)
- Security expectations (which fields are sensitive, where validation must happen, what Claude must never do)
- Engineering principles (surgical changes only, simplicity first, no speculative abstractions)
- The 4-phase workflow (Claude cannot skip spec → plan → build → review → ship)
- Known extension points (what is intentionally incomplete and not to be touched until asked)

Without CLAUDE.md, Claude Code is a powerful general-purpose agent. With it, it is a team member that already knows your codebase, your standards, and your compliance requirements on day one.

**2. Skills — senior engineer judgment encoded as reusable workflows**
Skills are invocable commands (e.g., `/spec`, `/plan`, `/build`, `/review`, `/ship`, `/devsecops-audit`) that encode the steps, guardrails, and output format for common engineering tasks. They are:
- Owned by tech leads, not individual developers
- Checked into the repo and versioned with the code
- Available to every engineer — junior or senior — in every session
- Enforceable: `/build` refuses to run without a spec. `/ship` refuses to run without a passing review.

This is what it means to turn tribal knowledge into scalable capability. The habits of your best senior engineers — writing specs before coding, reviewing security implications before shipping — become structural constraints, not conventions.

**3. Hooks — automated enforcement at the tool level**
Hooks fire automatically in response to tool events. The PostToolUse hook in this demo fires pytest after every file edit in `app/`. This means:
- It is not possible for Claude to silently break tests — the failure is immediate
- It is not possible for a developer to skip the test step — the hook runs regardless
- The constraint is in `.claude/settings.json`, not in anyone's memory

Together, CLAUDE.md + skills + hooks form an operating model that makes good engineering practices the path of least resistance, not the path of most discipline.

### Why this matters for FinTechCo specifically
FinTechCo operates under regulatory requirements that make ad hoc AI usage particularly risky. Account numbers, routing numbers, transaction amounts — these fields have compliance implications if they appear in logs, error messages, or audit trails. CLAUDE.md is the mechanism that encodes these constraints once and enforces them on every Claude Code session in every repo, for every engineer on the team.

One security team writes the rules. 120 engineers follow them automatically.

---

**SLIDE CUE — Slide 5: AI Needs an Operating Model**
Title: "Most Teams Buy a Model. Winning Teams Build an Operating Model."
Visual: Three-part diagram — CLAUDE.md (compliance policy) + Skills (encoded senior judgment) + Hooks (automated enforcement) = Operating Model. Arrow from Operating Model → Consistent Quality + Measurable ROI.
Key message: "Your security team writes the rules once. Every Claude Code session in every repo is automatically bound by them."
Speaker note: "This is what separates a tool evaluation from a strategic capability. The model is the engine. The operating model is the vehicle."

---

## Section 5 — The 4-Phase Workflow: Governance at Scale

### Why a workflow exists at all
The biggest risk of AI-assisted development is not that the AI writes bad code. It's that the AI writes code confidently, at speed, without the organizational alignment that normally happens before a line is written. A developer who says "build this" without a spec will get working code that solves the wrong problem — or the right problem in a way that creates a compliance gap.

The 4-phase workflow exists to preserve the discipline that makes software delivery predictable, and to enforce it structurally rather than relying on convention.

### The 4 phases and what each one prevents

**Phase 1 — Spec (`/spec`)**
*What it produces:* Problem statement, scope, non-goals, files affected, acceptance criteria, test plan, rollback notes.
*What it prevents:* Building the wrong thing. Misaligned expectations between developer and reviewer. Scope creep that happens silently mid-implementation.
*Key constraint:* Cannot proceed to planning without a spec file saved to `docs/specs/`.

**Phase 2 — Plan (`/plan`)**
*What it produces:* Atomic, independently-testable tasks with explicit acceptance criteria and verification steps. Ordered by dependency.
*What it prevents:* Large, unreviewed diffs. Implementations that touch many files at once and are hard to review. Tasks that leave the system in a broken intermediate state.
*Key constraint:* Cannot proceed to build without a plan file saved to `docs/plans/plan.md`.

**Phase 3 — Build (`/build`)**
*What it produces:* One atomic task implemented at a time. Tests run after every file change. Scope creep reported, not silently executed.
*What it prevents:* Silent regressions. Scope expansion without approval. Shipping code that fails tests.
*Key constraint:* Cannot proceed to review without `build.done` marker written to disk.

**Phase 4 — Review + Ship (`/review`, `/ship`)**
*What `/review` produces:* Five-axis assessment — correctness, security, maintainability, operational risk, assumption scope. Writes `review.done` only if no blocking issues.
*What `/ship` produces:* Pre-ship checklist — tests pass, no debugging artifacts, behavior verified in UI, rollback path confirmed.
*What it prevents:* Shipping without a security review. Shipping without a rollback plan. Shipping without confirming the feature works end-to-end.
*Key constraint:* `/ship` is blocked until `review.done` exists on disk.

### The governance paradox
Most CTOs assume AI coding tools lower the quality floor — that junior engineers using AI will ship worse code faster. The 4-phase workflow inverts this. A junior engineer following spec → plan → build → review → ship produces:
- A written spec before any code exists
- A plan where each task is independently testable
- Tests that run automatically after every change
- A security review before shipping

This is more disciplined than most senior engineers working without AI. **The governance isn't advisory — it's structural. A junior engineer on day one is bound by the same gates as a senior engineer with ten years of experience.**

### On-disk enforcement
The gates are enforced by markers written to and read from disk — not session memory. This means:
- A new Claude Code session cannot claim a build was completed — it checks `docs/plans/build.done`
- The workflow survives context resets, model restarts, and mid-session interruptions
- The audit trail is version-controlled — `docs/plans/` and `docs/specs/` can be committed and reviewed

---

**SLIDE CUE — Slide 6: The 4-Phase Workflow**
Title: "Governance Without Slowing Delivery"
Visual: Four-step horizontal pipeline: Spec → Plan → Build → Review/Ship. Each step has a lock icon showing what's blocked if skipped. Arrow at bottom: "Enforced on disk, not in memory."
Key message: "A junior engineer on day one follows the same gates as a senior engineer. Governance is structural, not voluntary."
Speaker note: "This is the answer to the question every CTO asks: how do we make sure AI doesn't become a liability at scale? You don't manage it. You enforce it."

---

## Section 6 — Real ROI: Faster Throughput + Lower Rework

### The wrong metric
Lines of code generated. Tokens consumed. Code completion acceptance rate. These are vanity metrics that measure AI activity, not engineering outcomes.

### The right equation
**Real ROI = (Throughput gain) − (Rework cost)**

This equation matters because AI without governance produces fast first drafts and expensive corrections. A developer who ships AI-generated code without a spec, without tests, and without a security review will produce:
- Faster initial delivery
- Higher review rejection rate
- More production bugs
- More time spent in retrospective fixes

The net ROI can be negative — and frequently is — for teams at Stage 1 (vibe coding).

The 4-phase workflow shifts the rework cost left, to spec and plan, where it's cheap. Not right, to production, where it's expensive.

### The metrics that matter

| Metric | What it measures | Benchmark |
|---|---|---|
| **Cycle time per feature** | Spec to merged PR | Top-quartile teams: 1–3 days. Industry average: 1–2 weeks. McKinsey: AI-assisted teams 20–45% faster cycle time. |
| **Defect escape rate** | Bugs reaching production | DORA high performers: 15% of changes cause incidents vs. 46% for low performers |
| **Onboarding time to first PR** | Time for new hire to ship meaningful code | Ramp: engineers productive significantly faster with Claude Code pre-configured |
| **Review turnaround** | Time from PR open to merge | Faster when PRs arrive with spec, tests, and review checklist pre-attached |
| **Engineering focus time** | % of time on high-value work vs. boilerplate | McKinsey: AI tools can free 25–40% of developer time currently spent on low-value tasks |
| **Change failure rate** | % of deployments causing production incidents | DORA 2024: elite performers — 0–5% change failure rate vs. 46%+ for low performers |
| **Mean time to restore (MTTR)** | Time to recover from production failure | Ramp: 80% reduction in incident investigation time; DORA elite: <1 hour MTTR |
| **Developer satisfaction / retention** | eNPS, attrition risk | Accenture (2023): organizations with structured AI workflows report significantly higher developer satisfaction scores — talent retention compound benefit |

### Additional benchmark context (advisory and research firms)
- **Accenture Technology Vision 2024:** "AI fluency" — the organizational ability to apply AI strategically — is the single strongest predictor of enterprise AI ROI. Tool access is table stakes; operating model maturity is the differentiator.
- **Deloitte Tech Trends 2024:** Financial services firms that piloted AI coding tools with structured governance saw 2–3x higher sustained adoption rates at 6 months vs. unstructured pilots. Governance does not slow adoption — it sustains it.
- **McKinsey Global Institute (2023, "The economic potential of generative AI"):** Software engineering is the #1 function by potential productivity impact from generative AI — estimated 20–45% acceleration in development speed across the software lifecycle, not just code writing.
- **Gartner (2024):** By 2028, 75% of enterprise software engineers will use AI coding assistants — up from less than 10% in 2023. Organizations that establish governance models now will have a 2–3 year structural advantage.
- **IDC (2024):** Companies that combine AI tools with documented engineering standards (analogous to CLAUDE.md) report 67% higher confidence in AI-generated code quality than those using AI ad hoc.

### FinTechCo-specific ROI model

**Inputs:**
- 120 Software Engineers × ~$180K average loaded cost = ~$21.6M annual engineering spend
- 40 Data Scientists × ~$200K average loaded cost = ~$8M annual DS spend
- 20 SREs × ~$170K average loaded cost = ~$3.4M annual SRE spend
- Total: ~$33M annual technical staff spend

**Conservative scenario (20% productivity improvement, top of realistic range for structured adoption):**
- Equivalent of 24 additional SE-equivalents delivered without additional headcount
- At $180K loaded: ~$4.3M in equivalent engineering capacity unlocked
- Defect escape rate reduction of 20%: fewer production incidents, less SRE toil

**Ramp benchmark (aggressive but documented):**
- 80% reduction in incident investigation time → at 20 SREs spending even 20% of their time on incident work, this is ~16 SRE-hours/week recovered
- 1M+ lines of AI-suggested code implemented in 30 days → at FinTechCo scale, this is new product velocity, not just efficiency

**The DS multiplier:**
- From Anthropic customer research: "saves 1–2 days of routine work per model" for data scientists
- At 40 DSs × 1 day/week recovered × 50 weeks = 2,000 DS-days/year
- At $200K/year loaded ÷ 250 days = $800/day × 2,000 days = **$1.6M in DS capacity recovered annually**

**Important framing:** These are not cost-reduction numbers. FinTechCo is not cutting headcount. These are capacity numbers — the equivalent of 20+ additional engineers, data scientists, and SREs working on new products and higher-value work instead of boilerplate, incidents, and onboarding.

---

**SLIDE CUE — Slide 7: Real ROI**
Title: "Real ROI = Faster Throughput + Lower Rework"
Visual: Two-column contrast — Wrong metrics (lines of code, tokens, acceptance rate) vs. Right metrics (cycle time, defect escape rate, onboarding speed, focus time). Below: ROI equation visualization — throughput gain minus rework cost = net ROI. Rework cost decreases as governance matures.
Key stats: 55% faster task completion (GitHub/Microsoft), 20–45% productivity gain (McKinsey), 80% incident investigation reduction (Ramp), 1–2 days/model saved for DS teams (Anthropic customer).
Speaker note: "The question isn't what does Claude Code cost. It's what does the absence of a structured operating model cost you at 180 engineers."

---

## Section 7 — Business Impact for FinTechCo: All Three Teams

### Software Engineers (120 engineers — Python, TypeScript, Java)

**Primary use cases:**
- **Codebase onboarding:** New hire asks "give me a quick architecture overview" — in 30 seconds they understand data flow, extension points, what's safe to change. For a 120-person org, onboarding acceleration compounds with every hire.
- **Compliance-aware feature development:** CLAUDE.md encodes the security team's rules. Sensitive fields (account numbers, routing numbers) are flagged automatically. Server-side validation is enforced at the route boundary, not left to individual developer judgment.
- **Governed delivery:** The 4-phase workflow means every feature — regardless of which developer builds it — goes through spec, plan, build, review, ship. The quality floor is structural.
- **Large-scale refactoring:** Claude reads the entire codebase, not just the file being edited. Refactors that span 10 files are safe because Claude understands the dependencies before touching anything.

**Key FinTechCo relevance:** Digital payments and banking infrastructure operate under regulatory scrutiny. A developer who accidentally logs a routing number creates a compliance event. CLAUDE.md makes this structurally impossible.

### Data Scientists (40 scientists — Python, Jupyter, pandas, scikit-learn, TensorFlow)

**Primary use cases:**
- **EDA and pipeline automation:** "I can now write EDA code in a notebook — pulling data, training a model, and evaluating it with basic metrics — and then ask Claude to convert that into a production pipeline. This process saves 1–2 days of routine work per model." (Anthropic customer, VP of AI, major tech company)
- **Fraud model development:** The suspicious transfer alerting demo (built live in Act 3) is a simplified version of exactly what the DS team builds — threshold-based anomaly detection. Same tool, same governance, same CLAUDE.md policy, now applied to ML model development.
- **Dashboard and visualization:** "Claude Code can rapidly create sophisticated, client-ready interactive applications that would often require significant time or support from someone with front-end dev skills." (Anthropic) — DS teams at FinTechCo can build internal dashboards without requesting SE support.
- **Jupyter notebook workflow:** Claude Code works natively in Jupyter. DS teams don't need a separate tool or a separate process. The same governance model that applies to the payments codebase applies to the fraud models.

**Key FinTechCo relevance:** 40 data scientists spending 1–2 days/week on boilerplate pipeline work represents 40–80 DS-days/week of recoverable capacity. That's new model development, faster fraud detection iteration, better credit scoring models.

### SREs (20 engineers — Python, shell scripts, Go)

**Primary use cases:**
- **Incident investigation:** Ramp documented an 80% reduction in incident investigation time with AI-powered incident response. For SREs managing complex distributed systems across AWS and GCP, this is significant.
- **Runbook generation:** Claude reads the codebase, understands the deployment architecture, and generates runbooks for new services automatically. No more runbook debt.
- **Shell script and automation review:** Claude Code reviews shell scripts for common failure modes (unquoted variables, missing error handling, TOCTOU patterns) as part of the normal PR workflow.
- **Infrastructure debugging:** "Complex infrastructure debugging" is explicitly called out as a use case in Anthropic's own deployment at scale.

**Key FinTechCo relevance:** 20 SREs managing infrastructure across AWS and GCP for a regulated financial services company. Every hour recovered from incident investigation is an hour available for proactive reliability work.

---

**SLIDE CUE — Slide 8: FinTechCo-Specific Impact**
Title: "Value Across Every Technical Team"
Visual: Three-column card layout — SEs (120), DSs (40), SREs (20). Each card: team size, primary use case, key metric/outcome.
Key numbers: DS: 1–2 days/model saved. SRE: 80% incident investigation reduction (Ramp). SE: onboarding time to first PR drops from weeks to days.
Speaker note: "This is not a tool for one team. It's an operating model for the entire technical organization."

---

## Section 8 — Governance Without Slowing Delivery

### The DevOps analogy
DevOps wasn't about making deployments faster. It was about making deployments safe enough to do more often. Before DevOps, deployment was a risky, manual, low-frequency event — which made it more risky because changes accumulated between deployments.

Claude Code + the 4-phase workflow is the same shift applied to feature development. The goal isn't to write code faster. It's to make the act of shipping a feature safe enough to do with more confidence, more frequency, and more predictability.

### Governance mechanisms in the demo

**Plan Mode — read-only audit guarantee**
Before touching any code, you can enter Plan Mode (Shift+Tab). In Plan Mode, Claude can read and analyze the entire codebase but is physically incapable of writing a file. This is not a soft constraint — it's an architectural enforcement.

Use case for FinTechCo: compliance audits, security reviews, onboarding — Claude analyzes everything, changes nothing. The security team can ask "review all input validation across the payments service" without any risk of unintended modifications.

**PostToolUse hook — automated test enforcement**
A hook in `.claude/settings.json` fires pytest after every file edit in `app/`. This means:
- It is structurally impossible to ship broken code silently
- The constraint is permanent and applies to every session — it cannot be forgotten
- Developers don't choose to run tests; the environment runs them automatically

**CI/CD pipeline — pipeline as policy**
`/devsecops-audit` spawns five specialist subagents in parallel to audit the repo's delivery posture: CI/CD pipeline, PR hygiene, branch protection, secrets hygiene, dependency security. It then fixes each gap — creating GitHub Actions workflows, PR templates with security checklists, and branch protection rules — all programmatically.

The result: main is locked. No PR merges without CI passing and a reviewer approving. Not a policy document — an enforced constraint applied in minutes.

### The key message for the CTO
Speed and control are not in tension. The 4-phase workflow, PostToolUse hooks, and programmatic branch protection make fast delivery safer, not riskier. The teams that ship most confidently are the ones with the most automation around their quality gates.

---

**SLIDE CUE — Slide 9: Governance Without Slowing Delivery**
Title: "Speed and Control Are Not in Tension"
Visual: DevOps analogy — before/after comparison. "Manual, low-frequency, high-risk deployment" → "Automated, high-frequency, low-risk deployment." Same arc applied to AI-assisted feature development.
Three mechanism cards: Plan Mode (read-only audit), PostToolUse Hook (automated test gate), CI/Branch Protection (pipeline as policy).
Speaker note: "The CTO's fear is that AI moves fast and breaks things. The operating model is the answer: governance is structural, not voluntary. Fast and safe are the same thing when the constraints are automated."

---

## Section 9 — Token Cost and Structural Controls

### The token explosion problem
A common concern from engineering leaders evaluating AI coding tools: "won't developers just burn tokens prompting AI for everything, and our bill explodes?"

This is a legitimate concern for organizations without an operating model. It is largely mitigated for organizations with one.

### How unstructured usage drives token waste
- Developers re-exploring the same codebase repeatedly because context is not preserved
- AI regenerating already-completed work because there's no on-disk record of what's done
- Long exploratory sessions that produce no output because there's no workflow gate to stop at
- Broad, unfocused prompts that bring in large amounts of irrelevant context

### How the operating model reduces token cost

| Mechanism | How it reduces token usage |
|---|---|
| **CLAUDE.md** | Scopes Claude's context to what's relevant for this repo. Prevents Claude from exploring irrelevant parts of the codebase on every session. |
| **Plan Mode** | Exploration sessions (architecture review, compliance audit) are read-only. Claude doesn't iterate on code in these sessions — it reads and reports. |
| **On-disk workflow gates** | `build.done` and `review.done` markers mean Claude never re-does work that's already complete. A new session picks up where the last one left off. |
| **Surgical change principle** | CLAUDE.md instructs Claude to touch only what the task requires. No reformatting adjacent files, no speculative improvements, no scope expansion. |
| **Atomic tasks** | `/plan` breaks work into tasks that change one logical thing. Each task is a short, focused session — not a long, sprawling one. |

### The right cost frame
Token cost should be measured per feature delivered, not per session. A feature that takes 4 focused sessions of 30 minutes each — each with a clear input (spec, plan, task, review) and a clear output (implementation, tests, review report) — uses far fewer tokens than an unstructured exploration that runs for hours and produces inconsistent output.

**Benchmark context:** Anthropic provides $25 in API credits for the demo preparation. This covers building, reviewing, and shipping a non-trivial feature (suspicious transfer alerting with tests and a full DevSecOps pipeline) with tokens to spare. At production scale with enterprise pricing and structured usage, cost per feature is predictable and manageable.

### Enterprise pricing and controls
- Claude Code supports Anthropic API, Amazon Bedrock, and Google Vertex AI — FinTechCo's existing AWS/GCP infrastructure means Bedrock and Vertex are natural homes for the API spend
- Centralized permissions and corporate proxy support mean the engineering organization doesn't manage individual API keys
- Usage can be tracked at the team, project, or feature level

---

**SLIDE CUE — Slide 10: Token Cost and Controls**
Title: "Token Cost Is a Symptom of Absent Structure"
Visual: Two scenarios — "Unstructured usage" (sprawling, expensive, unpredictable) vs. "Operating model" (focused, efficient, predictable cost per feature). Arrow pointing from left to right.
Key message: "Cost per feature, not cost per session. The operating model is the cost control mechanism."
Speaker note: "The question isn't how many tokens does Claude Code use. It's how many tokens does it take to ship a governed, tested, reviewed feature. That number is predictable, manageable, and declining as your operating model matures."

---

## Section 10 — Evaluation and Rollout Plan

### The recommendation: Start Small, Scale Intentionally

Do not roll out AI coding tools to 120 engineers overnight. The failure mode is: broad adoption, inconsistent usage, no baseline metrics, impossible-to-measure ROI, adoption fades after initial enthusiasm.

The winning pattern: champion team → high-value workflows → metrics baseline → expand by function.

### 30/60/90 Day Plan for FinTechCo

**Days 1–30: Champion Team**
- Identify a 5–8 person team with a mix of senior and junior engineers — ideally the payments or fraud detection team (already working in the demo's domain)
- Set up CLAUDE.md for one repo (the ACH/payments service is a natural starting point)
- Define 3 initial skills: `/spec`, `/build`, `/review`
- Establish baseline metrics before starting: current average cycle time per feature, current defect escape rate, current onboarding time to first PR
- Goal: team ships 2–3 features through the full 4-phase workflow
- Success signal: junior engineers producing PR-ready specs without senior guidance

**Days 31–60: Validate and Instrument**
- Review metrics against baseline: cycle time delta, PR rejection rate, review turnaround
- Identify the top 3 friction points in the workflow and adjust CLAUDE.md/skills
- Extend to the data science team: add Jupyter notebook workflow, `/spec` for model development
- Add DevSecOps layer: CI pipeline, PR template, branch protection
- Goal: operating model is stable enough for the champion team to train adjacent teams
- Success signal: champion team members can onboard a new engineer using only CLAUDE.md and the skills — no manual walkthrough required

**Days 61–90: Expand by Function**
- Roll out to the second engineering team with the champion team as internal trainers
- Add SRE use cases: runbook generation, incident investigation workflow
- Establish a CLAUDE.md governance model: who owns it, how changes are proposed and approved (it should go through a PR review, like any other policy document)
- Begin tracking ROI metrics formally: cycle time, defect escape rate, onboarding time, DS pipeline automation rate
- Goal: 3 teams on the operating model, metrics dashboard in place
- Success signal: a new engineer submits their first PR within 3 days of joining

**Day 91+: Scale and Standardize**
- Quarterly CLAUDE.md review: update standards as the codebase and compliance requirements evolve
- Skills library: each team contributes skills relevant to their domain (fraud team contributes `/fraud-model-spec`, SRE team contributes `/runbook-generate`)
- Metrics review with leadership: cycle time trend, defect escape rate trend, engineering capacity unlocked
- Expand to Java and TypeScript services with language-specific extensions to CLAUDE.md

### Success Metrics at 90 Days
- Cycle time per feature: target 30% reduction vs. baseline
- Defect escape rate: target 20% reduction vs. baseline
- Onboarding time to first PR: target 50% reduction vs. baseline
- DS pipeline automation rate: target 1–2 days/model recovered
- Team adoption: target 50% weekly active usage across enrolled teams (Ramp benchmark)

---

**SLIDE CUE — Slide 11: Rollout Plan**
Title: "Start Small. Scale Intentionally."
Visual: Three-column 30/60/90 day timeline. Each column: team size, key milestone, success signal. Bottom row: metrics at 90 days.
Key message: "The goal at Day 30 is not widespread adoption. It's a stable operating model on one team with a metrics baseline. Everything after that compounds."
Speaker note: "The rollout plan is the answer to 'how do we evaluate this?' You don't evaluate it with a Proof of Concept. You evaluate it with a champion team, a metrics baseline, and 90 days."

---

## Section 11 — Path to Production: Getting Started by Team and Audience

### Why this section exists
The most common failure mode in enterprise AI tool adoption is not resistance — it's ambiguity. "We're adopting Claude Code" means nothing until someone answers: who starts first, what do they do on day one, what does done look like for their role, and when do they hand off to the next team? This section answers those questions per persona.

### Implementation complexity: honest assessment
Before the path, set expectations correctly. Claude Code setup for a single team takes:
- **Hour 1:** Install Claude Code, connect to existing repo, activate a virtual environment — no infrastructure changes
- **Hour 2–4:** Draft CLAUDE.md for the first repo — architecture overview, security expectations, workflow definition. Template available; the first version is imperfect by design.
- **Day 2–3:** Define 3 starter skills (spec, build, review) — adapt from the template library. First feature goes through the 4-phase workflow.
- **Week 2:** Tune CLAUDE.md based on friction observed in week 1. Add hooks.
- **Week 3–4:** Champion team is self-sufficient. Ready to train team 2.

This is not a multi-quarter implementation. The first value is in days, not months. The operating model matures over weeks. That is the honest implementation complexity answer for the CTO who wants to understand timelines.

**Infrastructure prerequisites for FinTechCo (none blocking):**
- GitHub (already in use for the demo) — required for CI/branch protection integration
- AWS Bedrock or GCP Vertex AI — optional but recommended for enterprise API routing through existing cloud infrastructure; avoids direct Anthropic API key management at developer level
- Existing Python virtualenv or equivalent — required for PostToolUse hook; already standard in FinTechCo's stack

### Path to production — Software Engineers (120 engineers)

**Starting point:** Payments or banking infrastructure team — highest compliance surface, most to gain from CLAUDE.md governance.

**Week 1 — Individual capability:**
- Install Claude Code, connect to payments repo
- First task: "give me a quick architecture overview" — immediate value, no risk
- First governed feature: pick a small, well-scoped ticket. Run `/spec`, get approval, `/plan`, `/build`, `/review`, `/ship`
- Outcome: first feature shipped through full 4-phase workflow

**Week 2–3 — Team integration:**
- CLAUDE.md reviewed and approved by tech lead as a team PR (this is the governance moment — the team owns the policy, not just the tool)
- PostToolUse hook enabled — pytest fires on every file change across the team
- Second and third features shipped through the workflow — identify friction points

**Week 4 — DevSecOps layer:**
- Run `/devsecops-audit` on the payments repo
- CI pipeline, PR template, branch protection applied
- All future PRs on the payments repo now go through the enforced pipeline

**Month 2 — Scale signal:**
- Junior engineers shipping PRs that senior engineers approve without requiring substantial rework
- Onboarding time measurably shorter: new hire submits first meaningful PR within 3 days
- Tech lead reviews CLAUDE.md and makes first update — the policy is alive, not static

**Month 3 — Champion team trains team 2:**
- Champion team members lead a 2-hour onboarding session for the next team
- CLAUDE.md template shared; team 2 customizes for their repo
- No Anthropic involvement required for expansion — the operating model is self-propagating

**Key success metric:** Cycle time per feature, measured from spec creation to merged PR. Target: 30% reduction vs. pre-adoption baseline at 60 days.

---

### Path to production — Data Scientists (40 scientists)

**Starting point:** Fraud detection team — directly connected to the demo's suspicious transfer alerting feature. Natural bridge from Act 3.

**Week 1 — Jupyter workflow:**
- Claude Code installed in the DS Python environment (same `pip install` as the SE team)
- First task: "review this notebook and help me convert the EDA section into a reusable pipeline function" — immediate 1–2 day time savings
- No CLAUDE.md required initially — DS team starts with raw productivity before adding governance

**Week 2–3 — Add governance:**
- DS-specific CLAUDE.md created: data sensitivity rules (PII fields, model output logging), experiment reproducibility standards, pipeline promotion checklist
- `/spec` adapted for ML work: "what is the model trying to predict, what data does it use, what's the evaluation metric, what's the promotion criteria?"
- First model goes through spec → build → review cycle

**Week 4 — Pipeline bridge:**
- Claude converts finalized Jupyter notebook into a production-ready Metaflow/Airflow/Kubeflow pipeline (whichever FinTechCo uses)
- DS team submits pipeline PR through the same GitHub Actions CI the SE team uses — same review process, same branch protection
- Outcome: DS models go through the same governed delivery path as SE features

**Month 2 — DS-specific skills:**
- `/fraud-model-spec` skill created by the fraud team — encodes FinTechCo's model validation requirements
- `/pipeline-promote` skill: checklist for promoting a Jupyter prototype to production pipeline
- These skills represent the DS team's tribal knowledge, now codified and available to every DS who joins

**Key success metric:** Days per model from notebook to production pipeline. Target: 30–40% reduction at 60 days (from DS "1–2 days of routine work saved per model" baseline).

---

### Path to production — SREs (20 engineers)

**Starting point:** Incident response workflow — highest immediate ROI, lowest implementation risk (no code changes to production systems).

**Week 1 — Read-only value:**
- Claude Code in Plan Mode used for incident investigation: "read the payments service, identify what could cause a timeout during high ACH transfer volume"
- No file changes — pure analysis value. Zero risk. Immediately demonstrates the 80% incident investigation time reduction story (Ramp benchmark)
- Runbook drafts: Claude reads the repo and generates a first-draft runbook for the top 3 services. SRE reviews, corrects, commits.

**Week 2–3 — Shell script and automation review:**
- Existing shell scripts reviewed by Claude for common failure modes: unquoted variables, missing `set -e`, TOCTOU patterns, missing error handling
- Claude Code added to the SRE team's GitHub Actions pipeline: shell script linting on every PR
- SREs begin using Claude for Go code review — same CLAUDE.md governance, different language

**Week 4 — Incident response integration:**
- Claude Code added to the incident response runbook: step 1 of any P1 is "ask Claude to analyze the affected service and identify likely failure modes"
- Not autonomous — SRE reviews and acts. But investigation time drops dramatically.

**Month 2 — Proactive reliability:**
- Claude Code used for capacity planning analysis: "read the ACH transfer service and estimate where the bottlenecks will be at 2x current volume"
- Infrastructure-as-code review: Terraform/CloudFormation PRs reviewed by Claude before SRE approval
- SRE team contributes `/runbook-generate` skill to the skills library — available to all teams when new services are deployed

**Key success metric:** Mean time to investigate (MTTI) for P1 incidents. Target: 50% reduction at 60 days (conservative vs. Ramp's 80%).

---

### Cross-team governance model: who owns what

| Artifact | Owner | Review process | Cadence |
|---|---|---|---|
| CLAUDE.md (per repo) | Tech lead of owning team | PR review — any engineer can propose, tech lead approves | Quarterly review minimum; event-driven for compliance changes |
| Skills library | Senior engineers / tech leads | PR review — same process as code | As needed; skills are code |
| Hooks configuration | DevOps / SRE | PR review — change requires approval | On change |
| Metrics baseline | Engineering leadership | Reviewed monthly for first 90 days | Monthly at steady state |
| CLAUDE.md template (org-wide) | Head of Digital Transformation | Broad review — cross-team input | Semi-annual |

This governance model answers the CTO's implicit question: "who is responsible when Claude Code produces something wrong?" Answer: the tech lead who approved the CLAUDE.md that permitted it. Accountability is clear, traceable, and version-controlled.

---

**SLIDE CUE — Slide 12: Path to Production**
Title: "Getting Started: A Path for Every Team"
Visual: Three swim-lane timeline — SEs (top), DSs (middle), SREs (bottom). Each lane shows Week 1 → Week 4 → Month 2 → Month 3 milestones. Convergence arrow at right: "Same operating model, full org."
Key message: "First value in days. Operating model mature in weeks. Full org coverage in 90 days."
Speaker note: "The CTO will ask: how long does this take to set up? The honest answer is: first value in hours, first team operational in 2 weeks, three teams running in 90 days. No infrastructure changes required. No new systems to integrate. It runs in the terminal they already use."

---

## Section 12 — Wrap-Up, Next Steps, and Closing

### The closing structure
The PDF explicitly asks for a wrap-up with clear next steps before ending. This is where many presenters lose the room — they either run long, or they close with a vague "so what do you think?" This section provides a structured close that respects the audience's time and gives them something concrete to leave with.

### Suggested close (last 3–4 minutes of the 40-minute meeting)

**1. Acknowledge time (30 seconds)**
> "We're coming up on time — I want to make sure I leave you with clear next steps rather than run long. Let me close with three things."

**2. What you just saw — the demo in one sentence (30 seconds)**
> "In the last 15 minutes: a new developer understood the codebase in 30 seconds, a compliance gap was found and fixed without changing a policy document, a regulated feature was spec'd, built, tested, and shipped through an enforced workflow, and the entire delivery pipeline was hardened — CI, branch protection, security checklist — in under 5 minutes. That's not a demo script. That's the operating model."

**3. The business case in three numbers (60 seconds)**
- 180 technical staff. $33M in annual engineering capacity.
- Conservative scenario: 20% productivity improvement → equivalent of 36 additional engineers delivered without additional headcount.
- Ramp benchmark: 80% reduction in incident investigation time → 20 SREs freed from reactive work to proactive reliability.
- DS benchmark: 1–2 days/model saved → 2,000 DS-days/year recovered for new model development.

> "The question isn't whether Claude Code creates value. It's whether FinTechCo builds the operating model that captures it."

**4. Proposed next steps — concrete, time-bounded (60 seconds)**

| Step | Owner | Timeline |
|---|---|---|
| Identify champion team (5–8 SEs, payments or fraud) | Head of Digital Transformation | This week |
| Set up Claude Code on one repo, draft CLAUDE.md v1 | Tech lead + Anthropic SA support | Week 1–2 |
| First feature through the 4-phase workflow | Champion team | Week 2–3 |
| Metrics baseline captured (cycle time, defect rate, onboarding) | Engineering leadership | Before week 1 |
| 30-day check-in: metrics vs. baseline, friction review | Head of DT + Anthropic | Day 30 |

> "I'd suggest starting with your payments or fraud detection team — they're closest to the compliance and governance story we covered today, and the demo app maps directly to what they build."

**5. Open question (30 seconds — invite rather than close)**
> "Before we wrap up — what's the one concern that would most affect your decision to move forward? I'd rather surface it now than leave it unaddressed."

This question does two things: it shows confidence (you're not avoiding objections), and it often surfaces the real blocker (budget, security approval, competing priorities) that lets you address it directly or commit to following up.

### Anticipated objections and response framing

**"We're already evaluating GitHub Copilot."**
> "Copilot and Claude Code solve different problems. Copilot is an autocomplete layer — individual productivity at the file level. Claude Code is a delivery platform — organizational capability at the workflow level. The question isn't which one writes code faster. It's which one your 120 engineers can trust to deliver a compliant, tested, reviewed feature without a senior engineer babysitting every session."

**"We have security concerns about AI touching our codebase."**
> "That's exactly why Plan Mode exists — Claude can read and audit everything without writing a single file. And CLAUDE.md is your security team's mechanism: they write the rules once, every session is bound by them. The compliance gap in Act 2 was found in read-only mode. Nothing changed until you approved it."

**"What does implementation complexity look like? We don't have bandwidth for a long rollout."**
> "First value in hours: install Claude Code, ask it to overview the codebase. First governed feature in days. Champion team operational in 2 weeks. No infrastructure changes. No new systems. It runs in the terminal your engineers already have open."

**"How do we measure ROI before committing to a full rollout?"**
> "Capture your baseline before week 1: cycle time per feature, defect escape rate, onboarding time to first PR. Run the champion team for 30 days. Compare. If the numbers don't move, you haven't lost anything. If they do — and the benchmark evidence strongly suggests they will — you have the internal case to expand."

**"What about cost? Token usage could be unpredictable."**
> "Token cost is a symptom of absent structure. With the operating model — scoped CLAUDE.md, atomic tasks, on-disk workflow gates — cost per feature is predictable and declining. And FinTechCo's existing AWS/GCP infrastructure means you route through Bedrock or Vertex, using your existing cloud spend commitments."

### The closing sentence
> "The teams that build operating models now will have a compounding advantage that's very hard to replicate in 18 months. The window is open. Let's start with one team, one repo, and one sprint."

---

**SLIDE CUE — Slide 13: Next Steps**
Title: "Three Steps to Get Started"
Visual: Three large numbered boxes — (1) Identify champion team this week, (2) Draft CLAUDE.md and ship first feature in 2 weeks, (3) 30-day check-in with metrics. Each box: owner label, timeline, success signal.
Speaker note: "Don't end with 'let us know what you think.' End with a concrete ask: who is the champion team? That question alone advances the conversation."

**SLIDE CUE — Slide 14: Closing**
Title: "The Operating Model Is the Moat."
Visual: Single compounding curve. X-axis: time (weeks). Y-axis: engineering capability. Two lines — "Tool only" (flat) vs. "Operating model" (compounding). Labels at 30, 60, 90 days showing the divergence.
Key quote: "The teams that build operating models now will have a compounding advantage that's very hard to replicate in 18 months."
Speaker note: "Leave them with one thought: the model is available to everyone. The operating model is built, not bought. That's the moat."

---

### Updated full slide sequence (14 slides)

| # | Title | Section source |
|---|---|---|
| 1 | Claude Code at FinTechCo (title) | Section 0 |
| 2 | AI Coding Is Everywhere. Most Teams Are Using It Wrong. | Section 1 |
| 3 | From Vibe Coding to Structured Engineering | Section 2 |
| 4 | An Enterprise Software Delivery Platform | Section 3 |
| 5 | Most Teams Buy a Model. Winning Teams Build an Operating Model. | Section 4 |
| 6 | Governance Without Slowing Delivery (4-phase workflow) | Section 5 |
| 7 | Live Demo | — |
| 8 | Real ROI = Faster Throughput + Lower Rework | Section 6 |
| 9 | Value Across Every Technical Team | Section 7 |
| 10 | Speed and Control Are Not in Tension | Section 8 |
| 11 | Token Cost Is a Symptom of Absent Structure | Section 9 |
| 12 | Getting Started: A Path for Every Team | Section 11 |
| 13 | Three Steps to Get Started (next steps) | Section 12 |
| 14 | The Operating Model Is the Moat (closing) | Section 12 |

**Additional infographic prompts:**

8. **Path to production swim-lane:** Three horizontal swim lanes (SEs, DSs, SREs). Each lane: 4 milestone markers (Week 1, Week 4, Month 2, Month 3) with 1-line description. Convergence at right: "Same operating model."

9. **Objection-response cards:** Four cards, each with an objection on top (red) and response framing on bottom (green). Visual: obstacle/answer format.

10. **Compounding capability curve:** Two lines on a time/capability graph. "Tool only" — linear, flat. "Operating model" — exponential curve. Three labeled inflection points: Day 30 (champion team stable), Day 60 (second team trained), Day 90 (metrics confirming ROI).

---

### Complete slide sequence for NotebookLM

**Slide 1 — Title/Executive Summary**
*Title:* "Claude Code at FinTechCo: Accelerating Software Delivery Responsibly"
*Subtitle:* How an AI operating model transforms engineering throughput, governance, and ROI across 180 technical staff
*Visual prompt:* Clean executive title slide. Anthropic brand colors. No bullet points.

**Slide 2 — Market Reality**
*Title:* "AI Coding Is Everywhere. Most Teams Are Using It Wrong."
*Key content:* Vibe coding trap. 55% faster task completion (GitHub/Microsoft) — but only when paired with structured practices. The operating model is the multiplier.
*Visual prompt:* Split diagram — chaotic vibe coding on left (random arrows, inconsistent output), structured delivery pipeline on right (clean spec→ship flow). Single dramatic stat in center.

**Slide 3 — Maturity Arc**
*Title:* "From Vibe Coding to Structured Engineering"
*Key content:* 4-stage maturity arc. Comparison table. FinTechCo's current position and target.
*Visual prompt:* Horizontal progression arc with 4 labeled stages. Color gradient from red (Stage 1) to green (Stage 4). FinTechCo "you are here" marker and target marker. Comparison table below.

**Slide 4 — Claude Code Positioning**
*Title:* "An Enterprise Software Delivery Platform"
*Key content:* Full SDLC coverage. Competitive differentiation vs. Copilot/Cursor. Customer quotes (Ramp, Intercom, Shopify, Fortune 500 industrial).
*Visual prompt:* SDLC ring diagram (Discover→Design→Build→Deploy→Support) with Claude Code at center. Customer quote cards below. Competitive comparison table.

**Slide 5 — Operating Model**
*Title:* "Most Teams Buy a Model. Winning Teams Build an Operating Model."
*Key content:* CLAUDE.md (compliance policy) + Skills (encoded senior judgment) + Hooks (automated enforcement). The three artifacts.
*Visual prompt:* Three-part pyramid or triangle. Each vertex: one artifact with icon and 2-line description. Center: "Operating Model." Arrow pointing to "Consistent Quality + Measurable ROI."

**Slide 6 — The 4-Phase Workflow**
*Title:* "Governance Without Slowing Delivery"
*Key content:* Spec → Plan → Build → Review → Ship. What each phase prevents. Governance paradox (raises the floor for juniors).
*Visual prompt:* Five-step horizontal pipeline with lock icons between each step. Each step: name, what it produces, what it prevents. Bottom quote: "A junior engineer on day one follows the same gates as a senior engineer."

**Slide 7 — Live Demo**
*Title:* "Live Demo: ACH Transfer Operations Portal"
*Key content:* What you'll show — codebase exploration, Plan Mode security review, spec-driven feature delivery, DevSecOps audit.
*Visual prompt:* Demo scenario card. Six-row table mapping each act to its audience and key message:

| Act | Title | Audience | Key message |
|---|---|---|---|
| Act 1 (2 min) | Codebase exploration | CTO + Head of DT | Onboarding in 30 seconds |
| Act 2 (4 min) | Plan Mode + security review | CTO | Read-only compliance audit; surgical fix |
| Act 3 (7 min) | Governed feature delivery | CTO + Head of DT | Spec → plan → build → review → ship enforced |
| Act 4 (3 min) | Data science workflow | Head of DT + DS teams | Same governance in Jupyter; 1–2 days/model saved |
| Act 5 (5 min) | DevSecOps transformation | CTO | CI + branch protection in 5 minutes |
| Act 6 (2 min) | Refactor + ship | Head of DT | Feature ships through the pipeline just established |

Timer indicator at bottom. Acts 4–6 marked as optional/cuttable.

**Slide 8 — Real ROI**
*Title:* "Real ROI = Faster Throughput + Lower Rework"
*Key content:* Wrong metrics vs. right metrics. ROI equation. FinTechCo-specific capacity model. Key benchmarks.
*Visual prompt:* ROI equation visual — two boxes (Throughput Gain, Rework Cost) with minus sign → Net ROI box. Below: two-column table (wrong metrics / right metrics). Stats callout boxes: 55%, 20–45%, 80%, 1–2 days.

**Slide 9 — FinTechCo Teams**
*Title:* "Value Across Every Technical Team"
*Key content:* Three-team breakdown — SEs (120), DSs (40), SREs (20). Use cases, key metrics, FinTechCo-specific relevance.
*Visual prompt:* Three vertical cards side by side. Each: team name, headcount, icon, top 3 use cases, key metric. Color-coded by team type.

**Slide 10 — Governance**
*Title:* "Speed and Control Are Not in Tension"
*Key content:* DevOps analogy. Plan Mode, PostToolUse hook, CI/branch protection. Automated quality gates.
*Visual prompt:* Before/after comparison. Left: "Manual governance (conventions)" — developer decides whether to follow. Right: "Structural governance (enforcement)" — environment enforces automatically. Three mechanism icons below.

**Slide 11 — Token Cost**
*Title:* "Token Cost Is a Symptom of Absent Structure"
*Key content:* Token explosion causes. Operating model mitigations. Cost per feature, not cost per session. Bedrock/Vertex for FinTechCo's existing infra.
*Visual prompt:* Two scenarios visualization — unstructured (sprawling, expensive) vs. operating model (focused, predictable). Cost curve declining as operating model matures.

**Slide 12 — Rollout Plan**
*Title:* "Start Small. Scale Intentionally."
*Key content:* 30/60/90 day plan. Champion team → validate → expand. Success metrics at 90 days.
*Visual prompt:* Three-column timeline. Each column: days range, team size, key milestone, success signal. Metrics scorecard at bottom: cycle time, defect escape rate, onboarding time, adoption rate.

**Slide 12 — Path to Production**
*Title:* "Getting Started: A Path for Every Team"
*Key content:* Three swim-lane timeline — SEs, DSs, SREs. First value in days. Operating model mature in weeks. Full org in 90 days.
*Visual prompt:* Three swim lanes with milestone markers. Convergence arrow at right.

**Slide 13 — Next Steps**
*Title:* "Three Steps to Get Started"
*Key content:* Champion team this week. First feature in 2 weeks. 30-day check-in with metrics.
*Visual prompt:* Three numbered boxes with owner, timeline, success signal.

**Slide 14 — Closing**
*Title:* "The Operating Model Is the Moat."
*Key content:* Compounding curve — tool only (flat) vs. operating model (compounding). The model is available to everyone. The operating model is built, not bought.
*Visual prompt:* Single compounding curve with 30/60/90 day labels. One closing quote.

---

### Infographic prompts for NotebookLM

1. **Maturity arc infographic:** Horizontal progression from Vibe Coding (Stage 1) to Operating Model (Stage 4). Each stage: label, observable symptom, key risk. Color gradient red→green.

2. **ROI equation infographic:** Visual math — Throughput Gain (large green box) minus Rework Cost (shrinking red box, labeled "decreases as governance matures") = Net ROI (growing). Two versions: without operating model vs. with.

3. **Operating model triangle:** Three vertices — CLAUDE.md, Skills, Hooks. Center label: "Operating Model." Each vertex has a 1-line description and an icon.

4. **30/60/90 timeline infographic:** Horizontal timeline. Three phases marked. Each phase: team size bubble, key milestone, success signal. Metrics dashboard preview at 90-day mark.

5. **Team value map:** FinTechCo org chart style — three bubbles (SEs 120, DSs 40, SREs 20). Each bubble: top use case, key metric recovered. Connecting lines labeled "same CLAUDE.md governance."

6. **Governance pipeline:** Five boxes in sequence: Spec → Plan → Build → Review → Ship. Lock icon between each. Red X over "bypass" arrow. Bottom annotation: "Enforced on disk, not in memory."

7. **Competitive comparison:** Four-column table — Capability, Copilot, Cursor, Claude Code. Key differentiators highlighted in Claude Code column: full repo understanding, CLAUDE.md policy, agentic execution, subagent orchestration.

---

## Appendix — Key Quotes for Presenter

For the CTO:
> "CLAUDE.md is a machine-readable compliance policy. Your security team writes it once. Every Claude Code session in this repo is automatically bound by it."

> "Plan Mode gives you a hard read-only guarantee. Claude analyzes everything and cannot change anything. Use it for compliance audits."

> "The full delivery chain — spec, plan, build, review, ship — is enforced at every step by on-disk markers. A junior engineer on day one is bound by the same gates as a senior engineer. That's governance that scales."

For the Head of Digital Transformation:
> "New engineers submit their first PR in days, not weeks. That ROI compounds with every hire."

> "The 4-phase workflow isn't Anthropic's idea — your team writes CLAUDE.md. You define the process; Claude enforces it across every session."

> "Your fraud detection team? Same tool, same governance, in Jupyter. No separate process for data scientists."

From Anthropic customers:
> "Claude Code enables us to build applications we wouldn't have had bandwidth for." — Fergal Reid, VP of AI, Intercom

> "Engineers would try it on their own and have such a transformative experience that they felt compelled to share with their colleagues." — Austin Ray, Senior SWE, Ramp

> "Saves 1–2 days of routine work per model." — Data science team, Anthropic customer

---

*Document version: 1.0 | Prepared for NotebookLM slide and infographic generation | FinTechCo presentation brief*
