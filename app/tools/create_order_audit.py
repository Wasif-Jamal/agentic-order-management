from langchain_core.tools import tool

from app.config.db_config import db_config

from app.repository.order_audit import OrderAuditRepository


@tool
def create_order_audit(
    order_id: int, previous_status: str, new_status: str, remarks: str
) -> str:
    """
    Create order audit record.
    """

    db = db_config.SessionLocal()

    try:
        order_audit_repository = OrderAuditRepository(db)

        order_audit_repository.create_audit(
            order_id=order_id,
            previous_status=previous_status,
            new_status=new_status,
            remarks=remarks,
        )

        return "Order audit created successfully."

    finally:
        db.close()
