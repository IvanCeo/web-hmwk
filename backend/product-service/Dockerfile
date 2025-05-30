FROM python:3.12-slim
WORKDIR /product-service
RUN pip install --no-cache-dir "fastapi[standard]" sqlalchemy pydantic dynaconf asyncpg alembic
COPY ./product-service /product-service
COPY ./product-service/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "run.py"]