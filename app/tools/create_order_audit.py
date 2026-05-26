from app.repository.order_audit import OrderAuditRepository


class CreateOrderAuditTool:
    def __init__(self, order_audit_repository: OrderAuditRepository):

        self.order_audit_repository = order_audit_repository

    def execute(
        self,
        order_id: int,
        previous_status: str,
        new_status: str,
        remarks: str | None = None,
    ):

        return self.order_audit_repository.create_order_audit(
            order_id=order_id,
            previous_status=previous_status,
            new_status=new_status,
            remarks=remarks,
        )
