---
name: demo-reset
description: Resets the demo to baseline state. Use before every demo run to restore commented-out stubs, remove .github/, delete the feature branch, and confirm 10 tests pass.
---

# /demo-reset — Reset Demo to Baseline

Run the reset script and confirm the repo is in the correct starting state for the demo.

```bash
bash scripts/demo-reset.sh
```

After the script completes, verify:
- [ ] 10 tests pass
- [ ] `app/services/ach.py` — import and call are commented out
- [ ] `app/services/alerts.py` — function body is commented out
- [ ] `.github/` directory does not exist
- [ ] On `main` branch

Then start the server:

```bash
uvicorn app.main:app
```
