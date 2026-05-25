from fastapi import FastAPI

from app.config.env_config import settings
from app.config.db_config import Base, engine

from app.routes.order import router as order_router
from app.routes.inventory import router as inventory_router

# Import models
from app.models.inventory import Inventory  # noqa: F401
from app.models.inventory_audit import InventoryAudit  # noqa: F401
from app.models.order import Order  # noqa: F401
from app.models.order_audit import OrderAudit  # noqa: F401


def start_application() -> FastAPI:
    app = FastAPI(
        title="Agentic Order Management",
        version="1.0.0"
    )

    print("Starting Agentic Order Management System...")
    print(f"Database URL: {settings.DATABASE_URL}")

    Base.metadata.create_all(bind=engine)

    app.include_router(order_router)
    app.include_router(inventory_router)

    return app