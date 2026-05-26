from app.config.db_config import db_config
from app.models.inventory import Inventory


class InventorySeeder:
    def __init__(self):
        self.db = db_config.SessionLocal()

    def seed_inventory(self):

        products = [
            # Smart TVs
            Inventory(
                product_name="Samsung Neo QLED TV",
                quantity_available=15,
                price=189999.0,
            ),
            Inventory(
                product_name="LG OLED Evo TV", quantity_available=10, price=209999.0
            ),
            # Refrigerators
            Inventory(
                product_name="Whirlpool IntelliFresh Refrigerator",
                quantity_available=20,
                price=45999.0,
            ),
            Inventory(
                product_name="Samsung Family Hub Refrigerator",
                quantity_available=8,
                price=125999.0,
            ),
            # Washing Machines
            Inventory(
                product_name="Bosch Front Load Washing Machine",
                quantity_available=18,
                price=52999.0,
            ),
            Inventory(
                product_name="LG AI Direct Drive Washing Machine",
                quantity_available=14,
                price=48999.0,
            ),
            # Air Conditioners
            Inventory(
                product_name="Daikin Inverter AC", quantity_available=12, price=67999.0
            ),
            Inventory(
                product_name="Voltas Adjustable Inverter AC",
                quantity_available=16,
                price=58999.0,
            ),
            # Microwave Ovens
            Inventory(
                product_name="IFB Convection Microwave Oven",
                quantity_available=25,
                price=17999.0,
            ),
            Inventory(
                product_name="Samsung Grill Microwave Oven",
                quantity_available=22,
                price=14999.0,
            ),
        ]

        self.db.add_all(products)

        self.db.commit()

        print("Inventory seeded successfully.")

        self.db.close()


if __name__ == "__main__":
    seeder = InventorySeeder()

    seeder.seed_inventory()
