from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.config.db_config import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    order_date = Column(DateTime, default=datetime.utcnow)