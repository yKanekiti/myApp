from flask import Flask, make_response, jsonify
from .controller.node_list import node_router

app = Flask(__name__)
app.register_blueprint(node_router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
