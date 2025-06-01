from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from starlette.responses import Response
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from db import get_session
from order_schema import OrderCreateSchema
from order_services import order_service


app = FastAPI()


@app.get("/")
async def healthcheck():
    return Response(status_code=HTTP_200_OK)


@app.post("/order/")
async def create_order(
    request: OrderCreateSchema, session: AsyncSession = Depends(get_session)
):
    """
    Эндпоинт создания заказа
    """
    try:
        order = await order_service.create_order(request=request, session=session)
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)}, status_code=HTTP_400_BAD_REQUEST
        )
    return order


@app.get("/order/{order_id}")
async def get_order_by_id(order_id: UUID, session: AsyncSession = Depends(get_session)):
    """
    Эндпоинт получения заказа по ID
    """
    try:
        order = await order_service.get_order_by_id(order_id=order_id, session=session)
    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=HTTP_404_NOT_FOUND)
    return order


@app.delete("/order/{order_id}")
async def delete_order(order_id: UUID, session: AsyncSession = Depends(get_session)):
    """
    Эндпоинт удаления заказа по ID
    """
    await order_service.delete_order(order_id=order_id, session=session)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.post("/order/{order_id}/product/{product_id}")
async def add_product_to_order(
    order_id: UUID,
    product_id: UUID,
    quantity: int,
    price: float,
    session: AsyncSession = Depends(get_session),
):
    """
    Эндпоинт добавления товара в заказ
    """
    await order_service.add_product_to_order(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price,
        session=session,
    )
    return Response(status_code=HTTP_201_CREATED)


@app.delete("/order/{order_id}/product/{product_id}")
async def remove_product_from_order(
    order_id: UUID, product_id: UUID, session: AsyncSession = Depends(get_session)
):
    """
    Эндпоинт удаления товара из заказа
    """
    await order_service.remove_product_from_order(
        order_id=order_id, product_id=product_id, session=session
    )
    return Response(status_code=HTTP_204_NO_CONTENT)
