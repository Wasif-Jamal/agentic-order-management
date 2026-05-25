from sqlalchemy.orm import Session

from app.models.inventory import Inventory


def create_inventory_item(
    db: Session,
    product_name: str,
    quantity_available: int,
    price: float
):
    item = Inventory(
        product_name=product_name,
        quantity_available=quantity_available,
        price=price
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item