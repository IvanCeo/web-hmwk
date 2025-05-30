from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from uuid import UUID

class ProductBaseSchema(BaseModel):
    product_name: str
    in_stock: int
    price: Decimal
    description: str

class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductUpdateSchema(ProductBaseSchema):
    pass


class ProductSchema(ProductBaseSchema):
    product_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True