from langchain_core.tools import tool

from app.config.db_config import db_config

from app.repository.order import OrderRepository


@tool
def place_order(product_id: int, quantity: int, remarks: str = "") -> str:
    """
    Place a new order.
    """

    db = db_config.SessionLocal()

    try:
        order_repository = OrderRepository(db)

        order = order_repository.create_order(
            product_id=product_id, quantity=quantity, remarks=remarks
        )

        return f"Order placed successfully. Order ID: {order.order_id}"

    finally:
        db.close()
