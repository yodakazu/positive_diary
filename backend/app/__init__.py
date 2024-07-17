from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .models import db

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # login_manager.login_view = 'users.signin_user'
    login_manager.login_message = "Please log in to access this page."

    with app.app_context():
        db.create_all()

    from .routes import test_bp, users_bp, diaries_bp
    app.register_blueprint(test_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(diaries_bp)


    return app
