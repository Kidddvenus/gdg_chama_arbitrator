Recommended source layout for `src/chama_arbitrator`
===============================================

Goal
----
Provide a clear, maintainable package layout for production services and agents.

Suggested layout
----------------
- `chama_arbitrator/`
  - `api/` - HTTP API controllers and FastAPI app factory (entrypoint for uvicorn)
  - `agents/` - AI agents and agent orchestration code
    - `tools/` - small utility tools (financial analyst, vector search wrappers)
  - `services/` - core business logic and long-running services
  - `components/` - reusable components like retrievers and rerankers
  - `prompts/` - prompt registry and templates
  - `security/` - input/output/content filters
  - `frontend/` - streamlit or other frontend code
  - `observability/` - tracing, metrics, feedback collectors
  - `models.py` - Pydantic models and schemas (or `models/` package for many schemas)

Practical steps to adopt this layout
-----------------------------------
1. Create an `api` package and move `app/main.py` into `api` as the app factory.
2. Keep `agents/`, `services/`, and `components/` as separate packages; add `__init__.py` files
   that expose minimal public APIs to reduce long relative imports across the codebase.
3. Use absolute imports within the `chama_arbitrator` package (e.g. `from chama_arbitrator.services.query_router import QueryRouter`).
4. Add a lightweight `cli.py` at package root to run dev servers and convenience scripts.
5. Add automated tests under `tests/` that import the package the same way production code will.

Coding conventions
------------------
- Use type hints on public methods and docstrings for every public method.
- Keep service methods `async` where they represent IO-bound work.
- Place reusable small utilities under `tools` and keep them lightweight.

Next actions
------------
- I can: (A) create an `api` package and move the FastAPI app into it, (B) add `__init__.py` exports to reduce import churn,
  and (C) run tests and fix import errors. Which would you like me to start with?
