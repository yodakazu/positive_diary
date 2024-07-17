#!/bin/bash

# APIエンドポイント
URL="http://localhost:8000/users/login"

# リクエストデータ
DATA=$(cat <<EOF
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}
EOF
)

# curlコマンドを使用してPOSTリクエストを送信
curl -X POST $URL -H "Content-Type: application/json" -d "$DATA"