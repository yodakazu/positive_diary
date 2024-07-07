from flask import Blueprint, request, jsonify
from .models import db, User

test_bp = Blueprint('test', __name__)

@test_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!!")

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
