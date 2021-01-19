from quart import jsonify
from marshmallow import Schema, fields

from model import Product
from app import app


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    date = fields.DateTime(required=True)
    price = fields.Int()
    city = fields.Str()
    post = fields.Str()
    views = fields.Int()
    description = fields.Str()
    url = fields.Str()


products_schema = ProductSchema(many=True)


@app.route('/products')
async def products():
    products = await Product.query.gino.all()
    serialized_products = products_schema.dump(products)
    return jsonify(products=serialized_products)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
