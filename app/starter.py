from fastapi import FastAPI

from app.config.env_config import settings


def start_application() -> FastAPI:
    app = FastAPI(
        title="Agentic Order Management",
        version="1.0.0"
    )

    print("Starting Agentic Order Management System...")
    print(f"Database URL: {settings.DATABASE_URL}")

    return app