#!/bin/bash

# Flaskアプリケーションの設定
export FLASK_APP=run.py  # アプリケーションのエントリーポイントを指定
export FLASK_ENV=development       # 開発環境で実行する場合（デバッグ情報を表示）

# マイグレーションディレクトリが存在するか確認し、存在する場合は削除
if [ -d "migrations" ]; then
    rm -rf migrations
fi

# マイグレーションの実行
flask db init
flask db migrate -m "Initialize database"  # マイグレーションの作成（変更がある場合）
flask db upgrade                   # マイグレーションの実行

# Flaskアプリケーションの起動
flask run --host=0.0.0.0 --port=8000
