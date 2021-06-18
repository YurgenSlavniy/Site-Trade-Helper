from flask import Flask
from config import DevConf as Config


def connect():
    import pymysql.cursors
    return pymysql.connect(
        host=Config.HOSTNAME,
        user=Config.USERNAME,
        password=Config.PASSWORD,
        database=Config.DBNAME,
        charset=Config.CHARSET,
        cursorclass=pymysql.cursors.DictCursor
    )


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config())

    from . import main
    app.register_blueprint(main.bp)

    return app
