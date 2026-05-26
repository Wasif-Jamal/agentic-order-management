from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.config.db_config import db_config


class InventoryAudit(db_config.Base):
    __tablename__ = "inventory_audit"

    audit_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    change_type = Column(String, nullable=False)
    quantity_changed = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    remarks = Column(String)
