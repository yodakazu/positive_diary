# ベースイメージの指定
FROM node:latest

# 作業ディレクトリの設定
WORKDIR /app

# パッケージファイルのコピーと依存関係のインストール
COPY package.json .
COPY package-lock.json .
RUN npm install

COPY public/ ./public
COPY src/ ./src

# アプリケーションのビルド
RUN npm run build

# ポートのエクスポート
EXPOSE 3000

# コンテナ内で実行するコマンド
CMD ["npm", "start"]