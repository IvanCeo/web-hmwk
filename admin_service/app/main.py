from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.db.base import Base  
from app.db.session import engine, get_db  
from app.api.v1.admin_routes import router as admin_router

import os  
from sqlalchemy.orm import Session  
import logging

from app.schemas.admin_schema import AdminCreate 
from app.services.auth_service import get_admin_count, create_admin 
from app.db.session import DATABASE_URL

print("REAL DATABASE_URL:", DATABASE_URL)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    При старте создаём все таблицы (в том числе таблицу 'admins'),
    а затем проверяем, есть ли в базе хотя бы один администратор.
    Если нет — создаём дефолтного из переменных окружения.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created!")
    except Exception as e:
        print("CREATE TABLES ERROR:", e)


    # Открываем сессию, чтобы проверить наличие админов
    db: Session = next(get_db())  
    try:
        # Если таблица admins пуста, создаём дефолтного админа из .env
        if get_admin_count(db) == 0:
            logging.info("Количество записей в бд = 0")  
            username = os.getenv("ADMIN_DEFAULT_USERNAME")  
            password = os.getenv("ADMIN_DEFAULT_PASSWORD")  
            if username and password:
                logging.info("Логин и пароль админа успешно импортированы из окружения")  
                admin_in = AdminCreate(username=username, password=password)  
                create_admin(db, admin_in) 
                print(f"Default admin '{username}' has been created.")  
            else:  
                print("ADMIN_DEFAULT_USERNAME or ADMIN_DEFAULT_PASSWORD not set; skipping default admin creation.")  
    finally:
        db.close()  

    yield
    # При завершении (если нужно) можно что-то добавить

# Инициализируем FastAPI с блоком lifespan
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Разрешаем обращения с любых источников (можно ограничить при необходимости)
    allow_methods=["*"],      # Разрешаем любые HTTP-методы
    allow_headers=["*"],      # Разрешаем любые заголовки
)

app.include_router(admin_router, prefix="/api/v1/admin", tags=["admin"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/", tags=["root"])
def root():
    return {"message": "Admin service root"}
