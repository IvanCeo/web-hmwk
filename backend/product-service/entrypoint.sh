#!/bin/bash
set -e

echo "Ждём, пока Postgres будет доступен..."

# Проверка доступности БД
for i in {1..30}; do
  if PGPASSWORD=$POSTGRES_PASSWORD pg_isready -h postgres -p 5432 -U postgres > /dev/null 2>&1; then
    echo "База данных готова"
    break
  fi
  echo "Подключение к базе данных не удалось, повтор через 1с..."
  sleep 1
done

# Проверяем существование папки версий миграций
if [[ ! -d "./migrations/versions" || $(ls ./migrations/versions | wc -l) -eq 0 ]]; then
    echo "Создание первой миграции..."
    alembic revision --autogenerate -m "initial"
else
    echo "Миграции уже существуют."
fi

# Применение существующих миграций
echo "Применение миграций..."
alembic upgrade head

# Запуск приложения
echo "Запуск приложения..."
exec "$@"