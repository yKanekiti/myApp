import numpy as np
from learning.Network import load_created_model
from model.node import get_node
from model.predictionResult import PredictionResult
from common.database import ma
from flask import jsonify
from model.predictionResult import PredictionResultSchema


class Prediction:

    def predict(self, image, node_id, file_name):
        node = get_node(node_id)
        model = load_created_model(node)
        image = np.array([image])

        result = model.predict(image, batch_size=1, verbose=0)
        max_index = np.argmax(result)
        node_list = node.get_children()

        # resultの長さとnode_listの長さは同じのはず
        prediction_result_list = []
        i = 0
        max_node_id = 0
        for _node in node_list:
            prediction_result_list.append(
                PredictionResult(id=_node.id, name=_node.name, value=result[0][i], is_leaf=_node.is_leaf()))

            if i == max_index:
                # このとき、_nodeが今回の結果のMAXなので、そのノードIDと葉かどうかを確保
                max_node_id = _node.id
            i += 1
        json_data = jsonify({'max_id': max_node_id,
                             'result_list': PredictionResultSchema(many=True).dump(prediction_result_list)})
        return json_data
