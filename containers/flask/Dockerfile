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

# アプリケーションを実行
CMD ["bash", "run.sh"]
