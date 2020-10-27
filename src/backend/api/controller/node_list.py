from flask import Blueprint, request, make_response, jsonify

# ルーティング設定
node_router = Blueprint('node_router', __name__)


# パスとHTTPメソッドを指定
@node_router.route('/node', methods=['GET'])
def get_node_list():
    """
    判定リクエストのインターフェース部分
    :return: Jsonデータ
    """
    print('**** request get_node_list ****')
    result = [
        {
            'id': 1,
            'name': 'MobileSuit'
        }, {
            'id': 2,
            'name': 'Sanrio'
        }
    ]
    json_data = jsonify({
        'is_leaf': True,
        'winner_node_id': 1,
        'result': result
    })
    print(json_data)
    return json_data
