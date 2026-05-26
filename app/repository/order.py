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

    def get_order_by_id(self, order_id: int):

        return self.db.query(Order).filter(Order.order_id == order_id).first()

    def cancel_order(self, order_id: int):

        order = self.get_order_by_id(order_id)

        if not order:
            raise ValueError("Order not found.")

        previous_status = order.status

        order.status = "CANCELLED"

        self.db.commit()

        self.db.refresh(order)

        return {"order": order, "previous_status": previous_status}
