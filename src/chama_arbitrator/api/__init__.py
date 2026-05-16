"""API package for Chama Arbitrator.

Expose the FastAPI application from `api.app` so existing import paths
(`chama_arbitrator.app.main:app`) continue to work during migration.
"""

from .app import app  # re-export for backwards compatibility
