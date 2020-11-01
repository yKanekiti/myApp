from ..model.node import Node, get_learning_targets
import numpy as np
from keras.preprocessing.image import load_img, img_to_array


class Learning:
    def __init__(self, size):
        self.size = (size, size)
        self.train_x, self.train_t = [], []

    # すべて学習
    # 全ノード取得でforeach
    # ノードで学習

    def learn_all(self):
        node_list = get_learning_targets()
        for node in node_list:
            self.learn(node)

    # 個別に学習
    # 学習ノードに対しては、まず子ノードをとって子ノード以下で画像とラベルづけ
    # パスから画像データ取得
    # 画像データを加工、ついでにラベルづけ
    # 画像データをtrain_xに、ラベルをtrain_tに詰める
    # Network呼んでfitしてはいOK
    # モデルの保存はノードのモデルパス取得してそこに

    def learn(self, node):
        self.train_x, self.train_t = [], []
        for child_node in node.get_children():
            image_path_list = child_node.get_images()
            # 1つ1つの画像パスについて、まずnumpyにして加工してく
            label = child_node.id
            for image_path in image_path_list:
                image = load_img(image_path, grayscale=False, target_size=self.size)
                image = img_to_array(image) / 255
                self.edit_image(image, label)

    # 水増しをやりつつそのたびにラベルも入れてく
    def edit_image(self, image, label):
        return True
