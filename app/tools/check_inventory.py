from langchain_core.tools import tool

from app.config.db_config import db_config
from app.repository.inventory import InventoryRepository


@tool
def check_inventory(product_id: int, quantity: int) -> str:
    """
    Check whether requested inventory
    quantity is available.
    """

    db = db_config.SessionLocal()

    try:
        inventory_repository = InventoryRepository(db)

        available = inventory_repository.check_inventory_availability(
            product_id=product_id, quantity=quantity
        )

        if available:
            return "Inventory is available."

        return "Inventory is not available."

    finally:
        db.close()
