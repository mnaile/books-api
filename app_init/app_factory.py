from flask import Flask
from extensions.extensions import db,ma


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///bookdb"
    db.init_app(app)
    ma.init_app(app)
    ctx = app.app_context()
    ctx.push()
    # db.drop_all()
    db.create_all()

    return app
    