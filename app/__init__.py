from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from app.auth.admin import AuthUserView, MyAdminIndexView


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()
admin = Admin(name='Large app admin', index_view=MyAdminIndexView(), template_mode='bootstrap4')


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    bcrypt.init_app(app)
    admin.init_app(app)

    from app.core.views import core
    from app.auth.views import auth

    from app.models import User

    admin.add_view(AuthUserView(User, db.session))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    db.create_all(app=app)

    return app
