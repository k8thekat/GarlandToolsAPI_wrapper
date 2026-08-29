# Notes
---
- Use UV to handle packages

### Version Bumps
Before tagging a release, update the version string in all of these places:
- `async_garlandtools/__init__.py` — `__version__` (this is the single source; `pyproject.toml` reads it via `version = { attr = "async_garlandtools.__version__" }`)
- `pyproject.toml` — only if using a hardcoded `version` field instead of the dynamic attr

### Commit Message Structure
- SYNC before commiting..

```
# file_name.py
- Change 1
- Change 2
-- Change 2 sub-change 1

$ This commit message will be omitted because of `$`
- Everything below it will be ignored too as long as it has a `-`
```

- One `# file_name.py` block per file touched.
- Sub-changes are flush-left `--` (commit messages are not rendered as markdown).
- The subject line of the commit names the overall change; no separate theme key needed.
