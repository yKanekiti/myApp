from flask import Blueprint, request, make_response, jsonify

# ルーティング設定
node_router = Blueprint('node_router', __name__)


# パスとHTTPメソッドを指定
@node_router.route('/users', methods=['GET'])
def get_node_list():
    return ""


