from flask import Blueprint, request, jsonify
from .models import db, User, Diary

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
        'user_id': user.user_id,
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

diaries_bp = Blueprint('diaries', __name__, url_prefix='/diaries')

# 日記登録
@diaries_bp.route('/add', methods=['POST'])
def add_diary():
    data = request.json
    new_diary = Diary(
        user_id=data['user_id'],
        content=data['content'],
        date=data['date'],
    )
    db.session.add(new_diary)
    db.session.commit()
    return jsonify({'message': 'Diary created successfully'}), 201

# 日記情報取得
@diaries_bp.route('/<int:diary_id>', methods=['GET'])
def get_diary_by_id(diary_id):
    diary = Diary.query.get(diary_id)
    if not diary:
        return jsonify({'message': 'Diary not found'}), 404
    diary_data = {
        'diary_id': diary.diary_id,
        'content': diary.content,
        'date': diary.date
    }
    return jsonify(diary_data), 200

# 日記更新
@diaries_bp.route('/update/<int:diary_id>', methods=['POST'])
def update_diary(diary_id):
    diary = Diary.query.get(diary_id)
    if not diary:
        return jsonify({'message': 'Diary not found'}), 404
    data = request.json
    diary.content = data.get('content', diary.content)
    diary.date = data.get('date', diary.date)
    db.session.commit()
    return jsonify({'message': 'Diary updated successfully'}), 200

# 日記削除
@diaries_bp.route('/delete/<int:diary_id>', methods=['GET'])
def delete_diary(diary_id):
    diary = Diary.query.get(diary_id)
    if not diary:
        return jsonify({'message': 'Diary not found'}), 404
    db.session.delete(diary)
    db.session.commit()
    return jsonify({'message': 'Diary deleted successfully'}), 200