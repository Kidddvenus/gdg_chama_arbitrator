"""Top-level package for the Chama Arbitrator application.

This module re-exports common subpackages to simplify absolute imports
throughout the codebase (e.g. `from chama_arbitrator.services import QueryRouter`).
"""

from __future__ import annotations

# Re-export commonly used subpackages for convenience and clearer imports.
from . import api, agents, services, components, prompts, security, frontend, observability  # noqa: F401

__all__ = [
	"api",
	"agents",
	"services",
	"components",
	"prompts",
	"security",
	"frontend",
	"observability",
]
