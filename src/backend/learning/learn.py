from model.node import get_learning_targets
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from learning.Network import Network
from sklearn.model_selection import train_test_split

INPUT_SIZE = 200
BATCH_SIZE = 32
EPOCH = 80


def get_images(node):
    """
    ノードの画像データ(numpy)とラベルを取得する。
    子ノードに対してそれぞれ異なるラベルを振る
    それより深い子孫ノードについては、子ノードと同じラベルを振る
    :param node: ノード
    :return train_images, train_labels: 画像とラベル
    """
    train_images = []
    train_labels = []
    for child_node in node.get_children():
        image_path_list = child_node.get_images()
        # 1つ1つの画像パスについて、まずnumpyにして加工してく
        label = child_node.id
        for image_path in image_path_list:
            image = load_img(image_path, grayscale=False, target_size=(INPUT_SIZE, INPUT_SIZE))
            image = img_to_array(image) / 255
            train_images.append(image)
            train_labels.append(child_node.id)
    return train_images, train_labels


class Learning:
    def learn_all(self):
        """
        すべてのノードの学習を行う
        """
        # 全ノード取得
        node_list = get_learning_targets()

        print("学習開始（全ノード）")
        for node in node_list:
            self.learn(node)

        print("学習終了（全ノード）")

    # 個別に学習
    # 学習ノードに対しては、まず子ノードをとって子ノード以下で画像とラベルづけ
    # パスから画像データ取得
    # 画像データを加工、ついでにラベルづけ
    # 画像データをtrain_imagesに、ラベルをtrain_labelsに詰める
    # Network呼んでfitしてはいOK
    # モデルの保存はノードのモデルパス取得してそこに
    def learn(self, node):
        """
        ノードの学習を行う
        :param node: ノード
        """

        # データ取得
        train_images, train_labels = get_images(node)
        train_images, test_images, train_labels, test_labels = train_test_split(train_images, train_labels,
                                                                                train_size=0.2)

        # 水増し設定
        data_generator = ImageDataGenerator(
            rotation_range=30,
            width_shift_range=0.2,
            height_shift_range=0.15,
            zoom_range=[0.7, 1.3],
            channel_shift_range=20,
            shear_range=3,
            fill_mode="nearest")

        network = Network(INPUT_SIZE, len(node.get_children))
        model = network.create_model()
        model.summary()

        print("- 学習開始（各ノード） -")

        model.fit_generator(
            data_generator.flow(train_images, train_labels, batch_size=BATCH_SIZE),
            validation_data=(test_images, test_labels),
            epochs=EPOCH)
        model.save(node.get_learning_model_path())

        print("- 学習終了（各ノード） -")
