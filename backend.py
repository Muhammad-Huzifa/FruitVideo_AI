"""Backward-compatible entry point for the FruitVideo AI API.

New deployments should run ``uvicorn app.main:app``. Keeping this module means
the original ``uvicorn backend:app`` command continues to work.
"""

from app.main import app

__all__ = ["app"]
