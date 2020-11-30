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

      result = model.predict(image, batch_size=1, verbose=0)
      max_index = np.argmax(result)
      node_list = node.get_children()

      # resultの長さとnode_listの長さは同じのはず
      prediction_result_list = []
      i = 0
      is_leaf = False
      max_node_id = 0
      # 理想としては、[{"name": MobileSuit, "value": 65.5}, {"name": Sanrio, "value": 34.5}]みたいなのができる
      for _node in node_list:
         prediction_result_list.append(PredictionResult(name=_node.name, value=result[0][i]))

         if i == max_index:
            # このとき、_nodeが今回の結果のMAXなので、そのノードIDと葉かどうかを確保
            max_node_id = _node.id
            is_leaf = _node.is_leaf()
         i += 1
      json_data = jsonify({'is_leaf': is_leaf, 'max_id': max_node_id},
                          PredictionResultSchema(many=True).dump(prediction_result_list).data)
      return json_data
