myApp（仮名）
├── dockerfile
├── docker-compose.yml
├── README.txt
└── src
		├── web
		│		├─── static						# ここにjsやcssのファイルを置く
		│		└─── templates					# ここにはhtmlを置く
		│					└─── index.html		# SPAだとhtmlはこいつだけになる？
		├── backend
		│		├─── api						# FlaskAPI
		│		└─── learning					# 学習関係
		├── train								# とりあえず画像と学習済モデルはここに置いておこう
		├── mobile								# Android(余力があるならiOSつくってええよ)
		└── mysql	
				├─── init						# DDLとかだったかな
				└─── data						# ここ触ることはないはず（DBの中身がマウントされる）
