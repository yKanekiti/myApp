import sys
sys.path.append("src/backend/")

from common.database import db, ma, desc
from common.config import Config
from glob import glob
from .relation import Relation


# 学習対象ノードの取得は別にstaticでもいいな
def get_learning_targets():
    node_list = []
    # ここ絶対もっとスーッといけるはず
    for node in db.session.query(Node).all():
        if not node.is_leaf():
            node_list.append(node)
    return node_list


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

    # ノードの子供リスト取得
    def get_children(self):
        children_path = db.session.query(Node).outerjoin(Relation, Node.id == Relation.id). \
            filter(Node.id == self.id, Relation.distance == 1).all()
        return children_path

    # ノードのパス（trainより後ろからの）
    def get_file_path(self):
        node_list = db.session.query(Node).outerjoin(Relation, Node.id == Relation.id). \
            filter(Relation.child_id == self.id). \
            order_by(desc(Relation.distance)).all()
        # たぶんdistanceが..2,1,0 って感じで降順ソートされたノードのリストが手に入る（ディレクトリが浅い順）
        # しかもdistance=0を自分自身にしてるから色々と楽！
        file_path = ''
        for node in node_list:
            file_path += node.dir_name + '/'
        return file_path

    # ノードの下にあるイメージのパスを全取得
    def get_images(self):
        # まず相対パス作っとく
        file_path = '../train/image/' + self.get_file_path() + '/**'
        # glob関数でパスを全部とる\
        return glob(file_path, recursive=True)

    # 学習モデルの保存先
    def get_learning_model_path(self):
        return '../train/model/' + self.get_file_path()

    # ノードが葉かどうか判定
    def is_leaf(self):
        return db.session.query(Relation.id).filter(id != self.id) is None


# EntityをJsonに変換
class NodeSchema(ma.ModelSchema):
    class Meta:
        model = Node
        fields = ('id', 'name')
