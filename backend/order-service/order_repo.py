from sqlalchemy import select
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID
from decimal import Decimal

from order_schema import OrderSchema, OrderCreateSchema
from order_model import Order, OrdersItems
from order_model import OrderStatusEnum


class OrderRepo:
    async def get_by_id(self, order_id: UUID, session: AsyncSession):
        result = await session.execute(select(Order).filter_by(order_id=order_id))
        order = result.scalars().first()
        if not order:
            return None
        return OrderSchema.model_validate(order)

    async def create_order(self, order_data: OrderCreateSchema, session: AsyncSession):
        try:
            total_price = sum([p.price * p.in_stock for p in order_data.products])
            order = Order(total_price=total_price, status=order_data.status)
            session.add(order)
            await session.flush()  # получаем order_id

            for product in order_data.products:
                item = OrdersItems(
                    order_id=order.order_id,
                    product_id=product.product_id,
                    quantity=product.in_stock,
                    price_at_order_time=product.price,
                )
                session.add(item)

            await session.commit()
            return OrderSchema.model_validate(order)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def add_product_to_order(
        self,
        order_id: UUID,
        product_id: UUID,
        quantity: int,
        price: Decimal,
        session: AsyncSession,
    ):
        try:
            item = OrdersItems(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                price_at_order_time=price,
            )
            session.add(item)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def remove_product_from_order(
        self, order_id: UUID, product_id: UUID, session: AsyncSession
    ):
        try:
            stmt = sql_delete(OrdersItems).where(
                OrdersItems.order_id == order_id, OrdersItems.product_id == product_id
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def delete_order(self, order_id: UUID, session: AsyncSession):
        try:
            stmt = sql_delete(Order).where(Order.order_id == order_id)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0
        except SQLAlchemyError as e:
            await session.rollback()
            raise e


order_repo = OrderRepo()
