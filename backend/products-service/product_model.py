import uuid
from sqlalchemy import Column, Integer, String, UUID, DECIMAL, DateTime
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
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )