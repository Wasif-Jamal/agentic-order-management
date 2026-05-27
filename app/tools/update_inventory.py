from langchain_core.tools import tool

from app.config.db_config import db_config

from app.repository.inventory import InventoryRepository


@tool
def reduce_inventory(product_id: int, quantity: int) -> str:
    """
    Reduce inventory after order placement.
    """

    db = db_config.SessionLocal()

    try:
        inventory_repository = InventoryRepository(db)

        inventory_repository.reduce_inventory(product_id=product_id, quantity=quantity)

        return "Inventory updated successfully."

    finally:
        db.close()


@tool
def restore_inventory(product_id: int, quantity: int) -> str:
    """
    Restore inventory after cancellation.
    """

    db = db_config.SessionLocal()

    try:
        inventory_repository = InventoryRepository(db)

        inventory_repository.restore_inventory(product_id=product_id, quantity=quantity)

        return "Inventory restored successfully."

    finally:
        db.close()
