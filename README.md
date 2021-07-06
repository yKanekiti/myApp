## ディレクトリはこんな感じで作ろう

myApp/  
├ README.md  
├ Dockerfile  
├ docker-compose.yml  
├ .gitignore  
└ src/  
&emsp; ├ web/   
&emsp;&ensp;|&emsp; ├ Dockerfile  
&emsp;&ensp;|&emsp; └ frontend/  
&emsp; ├ backend/  
&emsp;&ensp;|&emsp; ├ api/  
&emsp;&ensp;|&emsp; ├ common/  
&emsp;&ensp;|&emsp; ├ model/  
&emsp;&ensp;|&emsp; └ learning/  
&emsp; ├ train/  
&emsp;&ensp;|&emsp; ├ images/  
&emsp;&ensp;|&emsp; └ Model/  
&emsp; ├ mobile/  
&emsp; └ mysql/  
&emsp;&ensp; &emsp; ├ Dockerfile  
&emsp;&ensp; &emsp; ├ my.cnf  
&emsp;&ensp; &emsp; ├ init/  
&emsp;&ensp; &emsp; └ data/  

## 起動方法

### 1. ビルドするためにdocker-compose.ymlと同じディレクトリで実行
`$ docker-compose up -d`

### 2. ビルドができたらコンテナに接続
`$ docker exec -it flask bash`

### 3. Flaskサーバー起動
`$ flask run -h 0.0.0.0`

## 準備

myApp/src/train/Modelには学習モデルを置くこと

※諸々の理由でGitにはあげれないため適当な方法で共有
