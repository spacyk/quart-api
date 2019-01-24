from gino import Gino

db = Gino()


class BazosProducts(db.Model):
    __tablename__ = 'bazos_products'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Unicode(), unique=True, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Integer())
    city = db.Column(db.Unicode())
    post = db.Column(db.String())
    views = db.Column(db.Integer())
    description = db.Column(db.Unicode())

