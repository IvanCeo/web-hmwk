from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from order_schema import OrderCreateSchema, OrderSchema
from order_model import Order, OrdersItems
from order_repo import OrderRepo

order_repo = OrderRepo()


class OrderService:
    def __init__(self):
        self.repo = order_repo

    async def get_order_by_id(
        self, order_id: UUID, session: AsyncSession
    ) -> OrderSchema:
        order = await self.repo.get_by_id(order_id=order_id, session=session)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    async def create_order(
        self, request: OrderCreateSchema, session: AsyncSession
    ) -> OrderSchema:
        try:
            order = await self.repo.create_order(order_data=request, session=session)
            return order
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def add_product_to_order(
        self,
        order_id: UUID,
        product_id: UUID,
        quantity: int,
        price: float,
        session: AsyncSession,
    ) -> None:
        try:
            await self.repo.add_product_to_order(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                price=price,
                session=session,
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def remove_product_from_order(
        self, order_id: UUID, product_id: UUID, session: AsyncSession
    ) -> None:
        success = await self.repo.remove_product_from_order(
            order_id=order_id, product_id=product_id, session=session
        )
        if not success:
            raise HTTPException(status_code=404, detail="Product not found in order")

    async def delete_order(self, order_id: UUID, session: AsyncSession) -> None:
        success = await self.repo.delete_order(order_id=order_id, session=session)
        if not success:
            raise HTTPException(status_code=404, detail="Order not found")


order_service = OrderService()
