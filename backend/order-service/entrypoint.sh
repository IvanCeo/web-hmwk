#!/bin/bash
set -e

for i in {1..20}; do
  echo "Просто ждем, когда другие ребята заработают"
  sleep 1
done

echo "Ждём, пока Postgres будет доступен..."

# Проверка доступности БД
for i in {1..30}; do
  # if PGPASSWORD=mypassword pg_isready -h postgres -p 5432 -U postgres > /dev/null 2>&1; then
  if PGPASSWORD=mypassword psql -h postgres -U postgres -d postgres -c '\q' > /dev/null 2>&1; then
    echo "База данных готова"
    break
  fi
  echo "Подключение к базе данных не удалось, повтор через 1с..."
  sleep 1
done

# Проверяем существование папки версий миграций
if [[ ! -d "./migrations/versions" || $(ls ./migrations/versions | wc -l) -eq 0 ]]; then
    echo "Создание миграции заказов..."
    alembic revision --autogenerate -m "initial orders"
    alembic stamp head
else
    echo "Миграции уже существуют."
fi

# Применение существующих миграций
echo "Применение миграций..."
alembic upgrade head

# Запуск приложения
echo "Запуск приложения..."
exec "$@"