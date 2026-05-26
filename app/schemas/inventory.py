from pydantic import BaseModel


class InventoryCreate(BaseModel):
    product_name: str
    quantity_available: int
    price: float
