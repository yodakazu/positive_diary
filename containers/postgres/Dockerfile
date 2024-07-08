# ベースイメージを指定
FROM postgres:latest

# 環境変数を設定（オプション）
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# オプション: 初期化スクリプトをコピー
# COPY init.sql /docker-entrypoint-initdb.d/