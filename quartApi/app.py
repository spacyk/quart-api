from quart import Quart
from gino.ext.quart import Gino

from config import DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD

app = Quart(__name__)
app.config.update(
    DB_HOST=DB_HOST,
    DB_DATABASE=DB_DATABASE,
    DB_USER=DB_USER,
    DB_PASSWORD=DB_PASSWORD
)

db = Gino(app=app)
