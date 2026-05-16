"""Legacy import path that re-exports the API app.

Keep this file to preserve existing tooling and Docker/uvicorn commands
that reference `chama_arbitrator.app.main:app` while the package is being
reorganized.
"""

from chama_arbitrator.api.app import app  # re-export

