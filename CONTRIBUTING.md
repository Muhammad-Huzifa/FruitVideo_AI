# Contributing to FruitVideo AI

Thank you for improving FruitVideo AI. Keep each change focused and verify it before
opening a pull request.

## Local setup

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements-dev.txt
```

On macOS or Linux, activate the environment with `source .venv/bin/activate`.

## Development checks

Run these commands before committing:

```bash
ruff check .
ruff format --check .
pytest
```

## Pull requests

1. Create a branch for one feature or fix.
2. Add or update tests for behavior changes.
3. Update the README when commands or endpoints change.
4. Use a short commit message that explains the change.
