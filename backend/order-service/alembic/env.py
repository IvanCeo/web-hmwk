from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

import asyncio

from db import Base
import order_model  
from config import settings

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Основная метаинформация для Alembic
target_metadata = Base.metadata

# Установка URL БД из настроек
config.set_main_option("sqlalchemy.url", settings.db.db_url)


def run_migrations_offline() -> None:
    """Офлайн-режим: миграции без подключения к БД."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Онлайн-режим: подключение к БД и выполнение миграций."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.begin() as conn:
        await conn.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
