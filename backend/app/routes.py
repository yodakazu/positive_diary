from flask import Blueprint, request, jsonify
from .models import db, User

test_bp = Blueprint('test', __name__)

@test_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!!")

users_bp = Blueprint('users', __name__, url_prefix='/users')

# ユーザー新規登録
@users_bp.route('/signup', methods=['POST'])
def signup_user():
    data = request.json
    # フィールドの欠損をチェック
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    # usernameの競合をチェック
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 409
    # emailの競合をチェック
    existing_user_by_email = User.query.filter_by(email=data['email']).first()
    if existing_user_by_email:
        return jsonify({'message': 'Email already exists'}), 409
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# ユーザー情報取得
@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    # user_idが存在しない場合の処理
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }
    return jsonify(user_data), 200

# ユーザー情報更新
@users_bp.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    # user_idが存在しない場合の処理
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

# ユーザー削除
@users_bp.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.get(user_id)
    # user_idが存在しない場合の処理
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200