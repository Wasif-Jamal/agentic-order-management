from app.repository.inventory import InventoryRepository


class CheckInventoryTool:
    def __init__(self, inventory_repository: InventoryRepository):

        self.inventory_repository = inventory_repository

    def execute(self, product_id: int, quantity: int):

        available = self.inventory_repository.check_inventory_availability(
            product_id=product_id, quantity=quantity
        )

        if not available:
            raise ValueError("Requested quantity is not available.")

        return True
