from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import desc

db = SQLAlchemy()
ma = Marshmallow()


# 初期設定
def init_db(app):
    db.init_app(app)
