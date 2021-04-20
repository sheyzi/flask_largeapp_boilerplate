from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app()

    from app.core.views import core
    from app.auth.views import auth

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    db.create_all(app=app)

    return app
