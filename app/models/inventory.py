from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.config.db_config import db_config


class Inventory(db_config.Base):
    __tablename__ = "inventory"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity_available = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)
