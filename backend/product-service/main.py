from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from starlette.responses import Response
from uuid import UUID
from product_schema import ProductCreateSchema, ProductUpdateSchema
from product_services import product_service
from db import get_session


app = FastAPI()


@app.get("/product/list")
async def get_product_list(session: AsyncSession = Depends(get_session)):
    """
    Энпоинт получения списка товаров
    """
    all_products = await product_service.get_all_products(session=session)
    if not all_products:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return all_products

@app.get("/")
async def healthcheck():
    return Response(status_code=HTTP_200_OK)

@app.post("/product/")
async def create_product(
    request: ProductCreateSchema,
    session: AsyncSession = Depends(get_session)
):
    """
    Энпоинт создания товаров
    """
    try:
        await product_service.add_product(request=request, session=session)
    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=HTTP_400_BAD_REQUEST)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/product/{product_id}")
async def update_product(
    product_id: UUID,
    request: ProductUpdateSchema,
    session: AsyncSession = Depends(get_session)
):
    """
    Эндпоинт обновления товара
    """
    await product_service.update_product(product_id=product_id, request=request, session=session)
    return Response(status_code=HTTP_200_OK)

@app.delete("/product/{product_id}")
async def delete_product(
    product_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    """
    Эндпоинт удаления товара
    """
    await product_service.delete_product(product_id=product_id, session=session)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.get("/product/{product_id}")
async def get_product_by_id(
    product_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    """
    Энпоинт получения товара по id 
    """
    product = await product_service.get_product_by_id(product_id=product_id, session=session)
    return product