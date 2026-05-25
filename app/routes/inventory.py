from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.config.db_config import db_config
from app.schemas.inventory import InventoryCreate
from app.repository.inventory import InventoryRepository


router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/")
def create_inventory(inventory: InventoryCreate):

    db: Session = db_config.SessionLocal()

    created_item = InventoryRepository.create_inventory_item(
        db=db,
        product_name=inventory.product_name,
        quantity_available=inventory.quantity_available,
        price=inventory.price
    )

    return created_item