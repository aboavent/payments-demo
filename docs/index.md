# ACH Transfer Operations Portal — Documentation

This folder contains all documentation for the project.

## Contents

| File | What it covers |
|---|---|
| [application.md](application.md) | App features, architecture, data models, UI, extension point |
| [demo-guide.md](demo-guide.md) | How to run the live demo, the feature-add walkthrough, tips |
| [workflow.md](workflow.md) | 4-phase workflow, decision framework, skills reference |
| [methodologies.md](methodologies.md) | Karpathy guidelines, Addy Osmani agent-skills, how they were adapted |
| [claude-code-setup.md](claude-code-setup.md) | CLAUDE.md, skills, hooks, settings — how the Claude Code layer works |

## Quick reference

```bash
# Run the app
uvicorn app.main:app --reload
# → http://localhost:8000

# Run tests
.venv/bin/pytest tests/ -q

# Live demo workflow
/spec   [feature description]
/plan
/build  task 1
/review
/ship
```
