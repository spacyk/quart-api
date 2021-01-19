import datetime

from app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Unicode(127), unique=True, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    price = db.Column(db.Integer())
    city = db.Column(db.Unicode(32))
    post = db.Column(db.String(10))
    views = db.Column(db.Integer())
    description = db.Column(db.Unicode(255))
    url = db.Column(db.Unicode(127))
