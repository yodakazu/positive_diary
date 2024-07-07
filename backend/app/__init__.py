from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import test_bp, users_bp
    app.register_blueprint(test_bp)
    app.register_blueprint(users_bp)

    return app
