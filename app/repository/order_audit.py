from sqlalchemy.orm import Session

from app.models.order_audit import OrderAudit

class OrderAuditRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_order_audit(
        self,
        order_id,
        previous_status,
        new_status,
        remarks=None
    ):

        audit = OrderAudit(
            order_id=order_id,
            previous_status=previous_status,
            new_status=new_status,
            remarks=remarks
        )

        self.db.add(audit)

        self.db.commit()

        self.db.refresh(audit)

        return audit