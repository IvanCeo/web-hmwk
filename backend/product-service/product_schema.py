from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from uuid import UUID

class ProductCreateSchema(BaseModel):
    product_name: str
    in_stock: int
    price: Decimal
    description: str


class ProductSchema(BaseModel):
    product_id: UUID
    product_name: str
    in_stock: int
    price: Decimal
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True