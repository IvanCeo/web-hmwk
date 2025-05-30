import uuid
from sqlalchemy import (
    Column,
    Integer,
    String,
    UUID,
    DECIMAL,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.sql import func
from db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = Column(String, nullable=False)
    in_stock = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_positive'),
        CheckConstraint('in_stock >= 0', name='check_in_stock_non_negative'),
    )
