from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from uuid import UUID

from order_model import OrderStatusEnum


class ProductBaseSchema(BaseModel):
    product_name: str
    in_stock: int
    price: Decimal
    description: str


class ProductSchema(ProductBaseSchema):
    product_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrderBaseSchema(BaseModel):
    status: OrderStatusEnum
    products: list[ProductSchema]


class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderUpdateSchema(OrderBaseSchema):
    pass


class OrderSchema(OrderBaseSchema):
    order_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
