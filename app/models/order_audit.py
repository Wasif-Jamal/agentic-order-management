from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.config.db_config import db_config


class OrderAudit(db_config.Base):
    __tablename__ = "order_audit"

    audit_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    previous_status = Column(String)
    new_status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    remarks = Column(String)
