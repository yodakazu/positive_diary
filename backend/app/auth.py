import jwt
import datetime

SECRET_KEY = 'your_secret_key_here'

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # トークンの有効期限を1日に設定
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token