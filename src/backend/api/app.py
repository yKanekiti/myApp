import sys

sys.path.append("/src/backend/")

from flask import render_template, request
from node_list import node_router
from common.database import init_db
from main import main
from learning.prediction import Prediction
from keras.preprocessing.image import load_img, save_img, img_to_array

app = init_db()
app.register_blueprint(node_router)

INPUT_SIZE = 200


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # POST送信されたデータを受け取る
    node_id = request.form["id"]
    file_name = request.form["name"]
    # ノードがルートの場合、画像を一時フォルダに保存する
    if node_id == "1":
        image = request.files['image']
        image = load_img(image, target_size=(INPUT_SIZE, INPUT_SIZE))
        save_img("/tmp/image/" + file_name, image)
    # 2回目からはimageはサーバにある前提で行く
    else:
        image = load_img("/tmp/image/" + file_name)

    image = img_to_array(image) / 255
    return Prediction().predict(image, node_id, file_name)


@app.route('/learn', methods=["GET"])
def learn():
    main()
    return "fin"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
