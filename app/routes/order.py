from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.config.db_config import SessionLocal
from app.schemas.order import OrderCreate
from app.repository.order import create_order


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def place_order(order: OrderCreate):

    db: Session = SessionLocal()

    created_order = create_order(
        db=db,
        product_id=order.product_id,
        quantity=order.quantity,
        remarks=order.remarks
    )

    return created_order