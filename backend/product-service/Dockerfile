FROM python:3.9-slim
WORKDIR /product-service
RUN pip install --no-cache-dir "fastapi[standard]" sqlalchemy pydantic dynaconf
COPY ./product-service /product-service
COPY ./settings.toml /product-service/settings.toml
CMD ["uvicorn", "run:app"]