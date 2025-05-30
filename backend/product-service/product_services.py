from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from product_schema import ProductSchema, ProductCreateSchema, ProductUpdateSchema
from product_model import Product
from product_repo import product_repo

class ProductService:
    def __init__(self):
        self.repo = product_repo

    async def get_all_products(self, session: AsyncSession) -> list[ProductSchema]:
        products = await self.repo.get_all(session=session)
        return products
    
    async def get_product_by_id(self, product_id, session: AsyncSession) -> ProductSchema:
        product = await self.repo.get_by_id(session=session, product_id=product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    
    async def add_product(self, request: ProductCreateSchema, session: AsyncSession) -> None:
        product = Product(
            product_name=request.product_name,
            in_stock = request.in_stock,
            price = request.price,
            description = request.description
        )
        try:
            await self.repo.add(product=product, session=session)
        except Exception as e:
            raise e
        
    async def update_product(self, product_id: int, request: ProductUpdateSchema, session: AsyncSession) -> None:
        success = await self.repo.update_by_id(product_id, request.model_dump(), session)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")

    async def delete_product(self, product_id: int, session: AsyncSession) -> None:
        success = await self.repo.delete_by_id(product_id, session)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")

product_service = ProductService()