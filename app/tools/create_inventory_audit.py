from app.repository.inventory_audit import InventoryAuditRepository


class CreateInventoryAuditTool:
    def __init__(self, inventory_audit_repository: (InventoryAuditRepository)):

        self.inventory_audit_repository = inventory_audit_repository

    def execute(
        self,
        product_id: int,
        change_type: str,
        quantity_changed: int,
        remarks: str | None = None,
    ):

        return self.inventory_audit_repository.create_inventory_audit(
            product_id=product_id,
            change_type=change_type,
            quantity_changed=quantity_changed,
            remarks=remarks,
        )
