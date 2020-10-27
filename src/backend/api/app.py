from flask import Flask, make_response, jsonify, render_template
from controller.node_list import node_router

app = Flask(__name__, static_folder='../../web/static/', template_folder='../../web/templates/')
app.register_blueprint(node_router)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
