from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, render_template
from sqlalchemy import desc


class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': "docker",
        'password': "docker",
        'host': "myMysqlDB:3306",    # localhostでなくmysqlサーバーのhostname
        'db_name': "mysql_database"
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = SystemConfig

db = SQLAlchemy()

# 初期設定
def init_db():
    print("==.==.==.==.init_db.==.==.==.==")
    app = Flask(__name__, static_folder='../../web/static/', template_folder='../../web/templates/')
    db.init_app(app)
    app.app_context().push()
    app.config.from_object(Config)
    return app


ma = Marshmallow(init_db())
