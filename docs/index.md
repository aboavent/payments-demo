# ACH Transfer Operations Portal — Documentation

This folder contains all documentation for the project.

## Contents

| File | What it covers |
|---|---|
| [application.md](application.md) | App features, architecture, data models, UI, extension point |
| [demo-guide.md](demo-guide.md) | How to run the live demo, all 6 acts, narration, tips |
| [workflow.md](workflow.md) | 4-phase workflow, decision framework, skills reference |
| [methodologies.md](methodologies.md) | Karpathy guidelines, Addy Osmani agent-skills, how they were adapted |
| [claude-code-setup.md](claude-code-setup.md) | CLAUDE.md, skills, hooks, settings — how the Claude Code layer works |
| [ppt-brief.md](ppt-brief.md) | NotebookLM source document for slide and infographic generation (FinTechCo presentation) |

## Quick reference

```bash
# Run the app (no --reload — wipes in-memory store on file changes)
uvicorn app.main:app
# → http://localhost:8000

# Run tests
.venv/bin/pytest tests/ -q

# Live demo workflow
/spec   [feature description]
/plan
/build  task 1
/review
/ship

# DevSecOps audit (Act 5)
/devsecops-audit

# Reset between runs
bash scripts/demo-reset.sh
```
