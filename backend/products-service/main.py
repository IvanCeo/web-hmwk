from fastapi import FastAPI
import aiohttp
import asyncio


app = FastAPI()


@app.get("/product/{product_id}")
async def get_product_by_id(product_id):
    return 