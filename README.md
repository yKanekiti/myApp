### ディレクトリはこんな感じで作ろう

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
