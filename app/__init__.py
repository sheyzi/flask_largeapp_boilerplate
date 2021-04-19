from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    db.init_app(app)


    from app.core.views import core
    from app.auth.views import auth

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
