from app.repository.inventory import InventoryRepository


class UpdateInventoryTool:
    def __init__(self, inventory_repository: InventoryRepository):

        self.inventory_repository = inventory_repository

    def reduce_inventory(self, product_id: int, quantity: int):

        return self.inventory_repository.reduce_inventory(
            product_id=product_id, quantity=quantity
        )

    def restore_inventory(self, product_id: int, quantity: int):

        return self.inventory_repository.restore_inventory(
            product_id=product_id, quantity=quantity
        )
