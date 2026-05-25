from sqlalchemy.orm import Session

from app.models.inventory import Inventory


class InventoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_inventory_item(
        self,
        product_name: str,
        quantity_available: int,
        price: float
    ):

        item = Inventory(
            product_name=product_name,
            quantity_available=quantity_available,
            price=price
        )

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item