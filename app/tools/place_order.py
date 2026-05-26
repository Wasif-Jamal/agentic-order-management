from app.repository.order import OrderRepository
from app.tools.check_inventory import CheckInventoryTool
from app.tools.update_inventory import UpdateInventoryTool
from app.tools.create_order_audit import CreateOrderAuditTool
from app.tools.create_inventory_audit import CreateInventoryAuditTool


class PlaceOrderTool:
    def __init__(
        self,
        order_repository: OrderRepository,
        check_inventory_tool: CheckInventoryTool,
        update_inventory_tool: UpdateInventoryTool,
        create_order_audit_tool: (CreateOrderAuditTool),
        create_inventory_audit_tool: (CreateInventoryAuditTool),
    ):

        self.order_repository = order_repository

        self.check_inventory_tool = check_inventory_tool

        self.update_inventory_tool = update_inventory_tool

        self.create_order_audit_tool = create_order_audit_tool

        self.create_inventory_audit_tool = create_inventory_audit_tool

    def execute(self, product_id: int, quantity: int, remarks: str | None = None):

        self.check_inventory_tool.execute(product_id=product_id, quantity=quantity)

        order = self.order_repository.create_order(
            product_id=product_id, quantity=quantity, remarks=remarks
        )

        self.update_inventory_tool.reduce_inventory(
            product_id=product_id, quantity=quantity
        )

        self.create_order_audit_tool.execute(
            order_id=order.order_id,
            previous_status="NONE",
            new_status="PLACED",
            remarks="Order placed successfully.",
        )

        self.create_inventory_audit_tool.execute(
            product_id=product_id,
            change_type="REMOVE",
            quantity_changed=quantity,
            remarks="Inventory deducted after order.",
        )

        return order
