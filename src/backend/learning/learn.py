from model.node import get_learning_targets
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from learning.Network import Network
from sklearn.model_selection import train_test_split
from pprint import pprint
from keras.utils import to_categorical

INPUT_SIZE = 200
BATCH_SIZE = 128
EPOCH = 256


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
    children_node_list = node.get_children()

    pprint("==.==.==.==.==.==.==.==.==.==.==.==.==.==.==")
    print("親ノード：", node.name)
    pprint("==.==.==.==.==.==.==.==.==.==.==.==.==.==.==")
    label = 0
    for child_node in children_node_list:
        pprint("==.==.==.==.==.==.==.==.==.==")
        print("子ノード：", child_node.name)
        pprint("==.==.==.==.==.==.==.==.==.==")
        image_path_list = child_node.get_images()
        # 1つ1つの画像パスについて、まずnumpyにして加工してく

        for image_path in image_path_list:
            image = load_img(image_path, grayscale=False, target_size=(INPUT_SIZE, INPUT_SIZE))
            image = img_to_array(image) / 255
            train_images.append(image)
            train_labels.append(label)
        label += 1

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    return train_images, train_labels, label


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
        train_images, train_labels, output_size = get_images(node)
        train_labels = to_categorical(train_labels)

        # 水増し設定
        data_generator = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.15,
            height_shift_range=0.10,
            zoom_range=[0.8, 1.2],
            channel_shift_range=15,
            shear_range=3,
            fill_mode="nearest",
            validation_split=0.15)
        network = Network(INPUT_SIZE, output_size)
        model = network.create_model()
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        print("- 学習開始（各ノード） -")
        print("train_images.shape =", train_images.shape)
        print("train_labels.shape =", train_labels.shape)

        model.fit(data_generator.flow(train_images, train_labels, batch_size=BATCH_SIZE), shuffle=True,
                  steps_per_epoch=len(train_images) / BATCH_SIZE, epochs=EPOCH)

        model.save(node.get_learning_model_path())

        print("- 学習終了（各ノード） -")
