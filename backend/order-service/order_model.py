import uuid
import enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    UUID,
    DECIMAL,
    DateTime,
    CheckConstraint,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class OrderStatusEnum(str, enum.Enum):
    cancelled = "Отменен"
    in_process = "В работе"
    complited = "Выполнен"


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
    total_price = Column(DECIMAL, nullable=False)
    status = Column(
        SQLEnum(OrderStatusEnum, name="order_status_enum"),
        default=OrderStatusEnum.in_process,
        nullable=False,
    )


class OrdersItems(Base):
    __tablename__ = "orders_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        nullable=False,
    )
    product_id = Column(
        UUID(as_uuid=True), nullable=False
    )  # связь на внешний сервис (без FK, т.к. микросервис разделён)
    quantity = Column(Integer, nullable=False)
    price_at_order_time = Column(DECIMAL, nullable=False)

    order = relationship("Order", backref="order_items")
