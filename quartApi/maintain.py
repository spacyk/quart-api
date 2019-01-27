import asyncio
from os import environ

import psycopg2

from quartApi.config import DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD
from quartApi.main import db


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
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_DATABASE, user=DB_USER, password=DB_PASSWORD)
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
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_DATABASE}')
    await db.gino.create_all()


if __name__ == '__main__':
    # create_table_sync_sql()
    asyncio.get_event_loop().run_until_complete(create_table_async_orm())
