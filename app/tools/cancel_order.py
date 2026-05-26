from app.repository.order import OrderRepository
from app.tools.update_inventory import UpdateInventoryTool
from app.tools.create_order_audit import CreateOrderAuditTool
from app.tools.create_inventory_audit import CreateInventoryAuditTool


class CancelOrderTool:
    def __init__(
        self,
        order_repository: OrderRepository,
        update_inventory_tool: UpdateInventoryTool,
        create_order_audit_tool: (CreateOrderAuditTool),
        create_inventory_audit_tool: (CreateInventoryAuditTool),
    ):

        self.order_repository = order_repository

        self.update_inventory_tool = update_inventory_tool

        self.create_order_audit_tool = create_order_audit_tool

        self.create_inventory_audit_tool = create_inventory_audit_tool

    def execute(self, order_id: int, remarks: str | None = None):

        order = self.order_repository.get_order_by_id(order_id)

        if not order:
            raise ValueError("Order not found.")

        previous_status = order.status

        cancelled_order = self.order_repository.cancel_order(order_id)

        self.update_inventory_tool.restore_inventory(
            product_id=order.product_id, quantity=order.quantity
        )

        self.create_order_audit_tool.execute(
            order_id=order.order_id,
            previous_status=previous_status,
            new_status="CANCELLED",
            remarks="Order cancelled successfully.",
        )

        self.create_inventory_audit_tool.execute(
            product_id=order.product_id,
            change_type="RESTORE",
            quantity_changed=order.quantity,
            remarks="Inventory restored after cancellation.",
        )

        return cancelled_order
