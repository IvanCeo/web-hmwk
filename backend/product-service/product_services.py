from sqlalchemy.ext.asyncio import AsyncSession

from product_schema import ProductSchema
from product_model import Product
from product_repo import product_repo

class ProductService:
    def __init__(self):
        self.repo = product_repo

    async def get_all_products(self, session: AsyncSession) -> list[ProductSchema]:
        products = await self.repo.get_all(session=session)
        return products
    
    async def add_product(self, request: ProductSchema, session: AsyncSession) -> None:
        product = Product(
            product_name=request.product_name,
            in_stock = request.in_stock,
            price = request.price,
            description = request.description
        )
        try:
            await self.repo.add(product=product, session=AsyncSession)
        except Exception as e:
            raise e

product_service = ProductService()