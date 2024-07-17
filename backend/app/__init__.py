from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    from .routes import test_bp, users_bp, diaries_bp
    app.register_blueprint(test_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(diaries_bp)


    return app
