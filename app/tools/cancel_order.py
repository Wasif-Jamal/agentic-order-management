from langchain_core.tools import tool

from app.config.db_config import db_config

from app.repository.order import OrderRepository


@tool
def cancel_order(order_id: int) -> str:
    """
    Cancel an existing order.
    """

    db = db_config.SessionLocal()

    try:
        order_repository = OrderRepository(db)

        order_repository.cancel_order(order_id)

        return "Order cancelled successfully."

    finally:
        db.close()
