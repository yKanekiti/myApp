import sys

sys.path.append("/src/backend/")

from flask import Flask, render_template, request, jsonify
from node_list import node_router
from common.database import init_db, ma
from main import main
from learning.prediction import predict

app = init_db()
app.register_blueprint(node_router)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # POST送信されたデータを受け取る
    node_id = request.form["id"]
    image = request.files['image'].stream
    return predict(image, node_id)


@app.route('/learn', methods=["GET"])
def learn():
    main()
    return "fin"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
