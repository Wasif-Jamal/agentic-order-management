from sqlalchemy.orm import Session

from app.models.order import Order


def create_order(
    db: Session,
    product_id: int,
    quantity: int,
    remarks: str | None
):
    order = Order(
        product_id=product_id,
        quantity=quantity,
        status="PLACED",
        remarks=remarks
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order