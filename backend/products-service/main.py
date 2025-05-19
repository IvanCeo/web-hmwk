from fastapi import FastAPI


app = FastAPI()

@app.get("/product/{product_id}")
async def get_product_by_id(product_id):
    """
    Энпоинт получения товара по id 
    """
    return 

@app.post("/product/")
async def create_product():
    """
    Энпоинт создания товаров
    """
    pass

@app.get("/product/list")
async def get_product_list():
    """
    Энпоинт получения списка товаров
    """
    pass

@app.post("/product/{product_id}")
async def update_product(product_id):
    """
    Энпоинт изменения товара
    """
    pass

@app.post("/product/{product_id}")
async def update_product(product_id):
    """
    Энпоинт изменения товара
    """
    pass