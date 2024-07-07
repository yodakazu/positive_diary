from flask import Flask, jsonify
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
