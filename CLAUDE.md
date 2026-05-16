# CLAUDE.md - Development Guide

## Build & Run
- **FastAPI Backend**: `uvicorn app.main:app --reload`
- **Frontend**: `streamlit run frontend/app.py`
- **Docker**: `docker-compose up --build`

## Commands
- **Linting**: `black .`, `isort .`
- **Testing**: `pytest`
- **Migrations**: `python scripts/migrate.py`
- **Seed Data**: `python scripts/seed.py`

## Coding Standards
- Use type hints for all function signatures.
- Follow Pydantic V2 patterns for data modeling.
- All core logic should be in `services/`, orchestrated by `app/main.py` or `agents/`.
- Maintain a neutral, professional tone in all system prompts.
- Use `security/` filters for all user inputs and agent outputs.
