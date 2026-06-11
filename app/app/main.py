from fastapi import FastAPI
from app.api.router import api_router
from app.core.logging import setup_logging
from app.core.errors import register_error_handlers

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(
        title="AutoPreLimTitleAPP",
        version="1.0.0",
    )
    app.include_router(api_router, prefix="/api")
    register_error_handlers(app)
    return app

app = create_app()
