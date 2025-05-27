from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from product_schema import ProductSchema
from product_model import Product

class ProductRepo():
    async def get_all(self, session: AsyncSession) -> list[ProductSchema]:
        result = await session.execute(select(Product))
        return [
            ProductSchema.model_validate(product) for product in result.scalars().all()
        ]
    
    async def add(self, product: Product, session: AsyncSession) -> None:
        try:
            session.add(product)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        
    async def get_by_id(self, product_id, session: AsyncSession) -> ProductSchema:
        result = await session.execute(select(Product).filter_by(product_id = product_id))
        return ProductSchema.model_validate(result.scalars().all())

    async def chacge_by_id(self, product_id, session: AsyncSession) -> None:
        pass

    async def get_by_id():
        pass

product_repo = ProductRepo()