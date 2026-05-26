from sqlalchemy.orm import Session

from app.models.inventory_audit import InventoryAudit


class InventoryAuditRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_inventory_audit(
        self,
        product_id: int,
        change_type: str,
        quantity_changed: int,
        remarks: str | None = None,
    ):

        audit = InventoryAudit(
            product_id=product_id,
            change_type=change_type,
            quantity_changed=quantity_changed,
            remarks=remarks,
        )

        self.db.add(audit)

        self.db.commit()

        self.db.refresh(audit)

        return audit
