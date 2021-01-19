import asyncio


from config import DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD
from app import db
from model import Product


async def init_data():
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_DATABASE}')
    await db.gino.create_all()

    await Product.create(title="Golden Necklace", price=120, description="24K flower necklace.")
    await Product.create(title="Silver Ring", price=45, description="Shining bright silver. Not fake.")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(init_data())
