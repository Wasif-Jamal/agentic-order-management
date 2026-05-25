from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, product_id: int, quantity: int, remarks: str | None):
        order = Order(
            product_id=product_id, quantity=quantity, status="PLACED", remarks=remarks
        )

        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        return order
