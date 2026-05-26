from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.config.db_config import db_config
from app.schemas.order import OrderCreate
from app.repository.order import OrderRepository


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def place_order(order: OrderCreate):

    db: Session = db_config.SessionLocal()

    order_repository = OrderRepository(db)

    created_order = order_repository.create_order(
        product_id=order.product_id, quantity=order.quantity, remarks=order.remarks
    )

    return created_order
