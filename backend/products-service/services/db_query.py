import psycopg2
import time


def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host='postgres',
                port='5432',
                user='postgres',
                password='root',
                database='postgres'
            )
            conn.close()
            print("PostgreSQL готов к работе!")
            return
        except psycopg2.OperationalError:
            print("Ожидание PostgreSQL...")
            time.sleep(2)

def create_table():
    conn = psycopg2.connect(
        host='postgres',
        port='5432',
        user='postgres',
        password='root',
        database='postgres'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(50) not null,
            in_stock INT default 0,
            price DECIMAL(10, 2),
            description TEXT,
            created_at timestamp CURRENT_TIMESTAMP,
            updated_at timestamp CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()    

def get_product(product_id):
    wait_for_postgres()
    create_table()

    conn = psycopg2.connect(
        host='postgres',
        port='5432',
        user='postgres',
        password='root',
        database='postgres'
    )
    cursor = conn.cursor()
    cursor.execute(f'select * from products p where p.product_id = {product_id}')
    conn.commit()
    cursor.close()
    conn.close()
