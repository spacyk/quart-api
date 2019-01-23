#!/usr/bin/python

import psycopg2
from config import PG_DBNAME, PG_PASSWORD, PG_USER, PG_HOST


def create_table():
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


if __name__ == '__main__':
    pass
    # create_table()
