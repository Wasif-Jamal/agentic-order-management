from sqlalchemy.orm import Session

from app.models.inventory import Inventory


class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int):
        return (
            self.db.query(Inventory).filter(Inventory.product_id == product_id).first()
        )

    def create_inventory_item(
        self, product_name: str, quantity_available: int, price: float
    ):

        item = Inventory(
            product_name=product_name,
            quantity_available=quantity_available,
            price=price,
        )

        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item

    def check_inventory_availability(self, product_id: int, quantity: int) -> bool:
        product = self.get_product_by_id(product_id)

        if not product:
            return False

        return product.quantity_available >= quantity

    def reduce_inventory(self, product_id: int, quantity: int):
        product = self.get_product_by_id(product_id)

        if not product:
            raise ValueError("Product not found")

        if product.quantity_available < quantity:
            raise ValueError("Insufficient inventory")

        product.quantity_available -= quantity

        self.db.commit()

        self.db.refresh(product)

        return product

    def restore_inventory(self, product_id: int, quantity: int):
        product = self.get_product_by_id(product_id)

        if not product:
            raise ValueError("Product not found")

        product.quantity_available += quantity

        self.db.commit()

        self.db.refresh(product)

        return product
