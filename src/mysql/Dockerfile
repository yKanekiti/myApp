# イメージはmysql5.7(Ubuntu)
FROM mysql:5.7

# パッケージをインストール
RUN apt-get update \
&& apt-get install -y locales apt-utils\
&& rm -rf /var/lib/apt/lists/* \
&& echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \
&& locale-gen ja_JP.UTF-8 \
&& apt update \
&& apt install -y --no-install-recommends

ENV LC_ALL ja_JP.UTF-8

# コンテナの実行コマンド
