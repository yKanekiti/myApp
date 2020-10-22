# OSはCentOS
FROM centos:latest

# パッケージをインストール
RUN yum -y update
RUN yum -y groupinstall "Development Tools"
RUN yum -y groupinstall "Base"
RUN yum -y install zip wget tar gcc zlib zlib-devel bzip2 bzip2-devel \
				readline readline-devel sqlite sqlite-devel openssl openssl-devel git gdbm-devel 

# anacondaをインストール
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh && \
	bash Anaconda3-5.0.0.1-Linux-x86_64.sh -b && \
	rm -f Anaconda3-5.0.0.1-Linux-x86_64.sh	

# 環境変数
ENV PATH $PATH:/root/anaconda3/bin

# anacondaをアップデート
RUN conda update --all

# 各フレームワークをインストール
RUN conda install -c anaconda Flask TensorFlow Keras

RUN conda config --append channels conda-forge && \
	conda install -c conda-forge flask-sqlalchemy && \
	conda install -c conda-forge flask-marshmallow

# 作業ディレクトリの指定
WORKDIR /root

# コンテナの実行コマンド
CMD ["/bin/bash"]
