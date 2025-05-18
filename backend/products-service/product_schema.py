from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class Product(BaseModel):
    product_id: str
    product_name: str
    in_stock: int
    price: Decimal
    description: str
    created_at: datetime