from sqlalchemy import Column, Integer, String, UUID, DECIMAL, DateTime
from db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    product_id = Column(UUID, primary_key=True)
    product_name = Column(String, nullable=False)
    in_stock = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )