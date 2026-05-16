"""FastAPI application factory and app instance for the HTTP API.

This module centralizes the API app creation so it can be imported from
`chama_arbitrator.api.app` or the legacy `chama_arbitrator.app.main` path.
"""
from fastapi import FastAPI
from chama_arbitrator.app.config import settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    app = FastAPI(
        title="Chama Arbitrator API",
        description="Arbitration engine for cooperative society disputes",
        version="0.1.0",
    )

    @app.get("/")
    async def root():
        return {"message": "Chama Arbitrator API is online"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app


# Module-level app for simple import paths and for ASGI servers.
app = create_app()
