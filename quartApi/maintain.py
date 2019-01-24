import asyncio

import psycopg2

from config import PG_DBNAME, PG_PASSWORD, PG_USER, PG_HOST
from main import db


def create_table_sync_sql():
    """
    Synchronously create bazos_products table with psycopg2
    :return:
    """
    command = """
        CREATE TABLE bazos_products (
            product_id SERIAL PRIMARY KEY,
            title VARCHAR(127) NOT NULL UNIQUE,
            date DATE NOT NULL,
            price INTEGER,
            city VARCHAR(32),
            post VARCHAR(10),
            views INTEGER,
            description VARCHAR(255)
        )
        """
    conn = None
    try:
        conn = psycopg2.connect(host=PG_HOST, dbname=PG_DBNAME, user=PG_USER, password=PG_PASSWORD)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


async def create_table_async_orm():
    await db.set_bind(f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:5432/{PG_DBNAME}')
    await db.gino.create_all()


if __name__ == '__main__':
    # create_table_sync_sql()
    asyncio.get_event_loop().run_until_complete(create_table_async_orm())
