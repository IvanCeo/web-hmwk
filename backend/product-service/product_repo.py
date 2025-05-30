from sqlalchemy import select
from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from product_schema import ProductSchema, ProductUpdateSchema
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
        product = result.scalars().first()
        if not product:
            return None
        return ProductSchema.model_validate(product)

    async def update_by_id(self, product_id, update_data: ProductUpdateSchema, session: AsyncSession) -> bool:
        stmt = (
            sql_update(Product)
            .where(Product.product_id == product_id)
            .values(**update_data)
            .execution_options(synchronize_session="fetch")
        )
        result = await session.execute(stmt)
        if result.rowcount == 0:
            return False
        await session.commit()
        return True
    
    async def delete_by_id(self, product_id, session: AsyncSession) -> bool:
        stmt = sql_delete(Product).where(Product.product_id == product_id)
        result = await session.execute(stmt)
        if result.rowcount == 0:
            return False
        await session.commit()
        return True

product_repo = ProductRepo()