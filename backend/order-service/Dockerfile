FROM python:3.12-slim
WORKDIR order-service
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir "fastapi[standard]" sqlalchemy pydantic dynaconf asyncpg alembic
COPY ./order-service /order-service
COPY ./order-service/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "run.py"]