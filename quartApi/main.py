# [START gae_python37_app]
import datetime

from quart import Quart, websocket, jsonify
from gino.ext.quart import Gino
from marshmallow import Schema, fields

from config import DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD

app = Quart(__name__)
app.config.update(
    DB_HOST=DB_HOST,
    DB_DATABASE=DB_DATABASE,
    DB_USER=DB_USER,
    DB_PASSWORD=DB_PASSWORD
)
db = Gino(app=app)


# MODEL #####

class BazosProduct(db.Model):
    __tablename__ = 'bazos_products'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Unicode(127), unique=True, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    price = db.Column(db.Integer())
    city = db.Column(db.Unicode(32))
    post = db.Column(db.String(10))
    views = db.Column(db.Integer())
    description = db.Column(db.Unicode(255))


# SCHEMA #####

class BazosProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    date = fields.DateTime(required=True)
    price = fields.Int()
    city = fields.Str()
    post = fields.Str()
    views = fields.Int()
    description = fields.Str()


bazos_products_schema = BazosProductSchema(many=True)


@app.route('/products')
async def products():
    products = await BazosProduct.query.where(BazosProduct.city == "Nitra").gino.all()
    serialized_products, errors = bazos_products_schema.dump(products)
    return jsonify(products=serialized_products)


@app.websocket('/ws')
async def ws():
    while True:
        await websocket.send('test')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
