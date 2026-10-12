---
name: summarize-repo-structure-subagent
description: Run the repository summarizer to produce a concise JSON summary of the workspace layout.
entrypoint: tools/skills/summarize_repo.py
runner: .vscode/skills/run_summarize_repo.sh
outputs:
  - repo_summary.json
invocation:
  manual: bash .vscode/skills/run_summarize_repo.sh
  ci_workflow: .github/workflows/summarize_repo.yml
author: automated by GitHub Copilot assistant
---

This file registers a local "subagent" descriptor for the `summarize-repo-structure` skill.
Tools or automation that look for subagent manifests can use this file to discover the
entrypoint, runner script, and outputs.

Notes
-----
- The runner script is executable and calls the Python entrypoint. It prints pretty JSON when run.
- The GitHub Actions workflow already produces `repo_summary.json` and uploads it as an artifact.
