# ベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY config.py config.py
COPY run.py run.py
COPY app/ app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# 環境変数を設定
ENV FLASK_APP=run.py

# マイグレーションを実行
RUN flask db init  
RUN flask db migrate -m "Initial migration"
RUN flask db upgrade

# アプリケーションを実行
CMD ["python", "run.py"]
