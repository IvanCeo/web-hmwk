from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from starlette.responses import Response

from product_schema import ProductSchema
from product_services import product_service
from db import get_session


app = FastAPI()

# @app.get("/product/{product_id}")
# async def get_product_by_id(product_id):
#     """
#     Энпоинт получения товара по id 
#     """
#     product = await product_service.
#     return 

@app.get("/healthcheck")
async def healthcheck():
    return Response(status_code=HTTP_200_OK)

@app.post("/product/")
async def create_product(
    request: ProductSchema,
    session: AsyncSession = Depends(get_session)
):
    """
    Энпоинт создания товаров
    """
    try:
        await product_service.add_product(request=request, session=session)
    except Exception as e:
        return Response(content=e, status_code=HTTP_400_BAD_REQUEST)
    return Response(status_code=HTTP_201_CREATED)

@app.get("/product/list")
async def get_product_list(session: AsyncSession = Depends(get_session)):
    """
    Энпоинт получения списка товаров
    """
    all_products = await product_service.get_all_products(session=session)
    if not all_products:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return all_products

# @app.post("/product/{product_id}")
# async def update_product(product_id):
#     """
#     Энпоинт изменения товара
#     """
#     pass

# @app.delete("/product/{product_id}")
# async def delete_product(product_id):
#     """
#     Энпоинт удаления товара
#     """
#     pass