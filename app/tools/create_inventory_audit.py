from langchain_core.tools import tool

from app.config.db_config import db_config

from app.repository.inventory_audit import InventoryAuditRepository


@tool
def create_inventory_audit(
    product_id: int, change_type: str, quantity_changed: int, remarks: str
) -> str:
    """
    Create inventory audit record.
    """

    db = db_config.SessionLocal()

    try:
        inventory_audit_repository = InventoryAuditRepository(db)

        inventory_audit_repository.create_audit(
            product_id=product_id,
            change_type=change_type,
            quantity_changed=quantity_changed,
            remarks=remarks,
        )

        return "Inventory audit created successfully."

    finally:
        db.close()
