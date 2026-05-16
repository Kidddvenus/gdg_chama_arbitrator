"""Frontend package exports (streamlit app)."""

from .app import st  # streamlit app module exposes `st` at import-time

__all__ = ["st"]
