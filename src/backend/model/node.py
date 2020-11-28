import sys, os

sys.path.append("src/backend/")

from common.database import db, ma, desc, Config
from glob import glob
from .relation import Relation


def get_learning_targets():
    node_list = []
    # ここ絶対もっとスーッといけるはず
    data_list = db.session.query(Node).all()
    for node in data_list:
        if not node.is_leaf():
            node_list.append(node)
    return node_list


def get_node(node_id):
    return db.session.query(Node).filter(id == node_id).one()


class Node(db.Model):
    __tablename__ = "node"
    __table_args__ = ({"mysql_engine": "InnoDB"})
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    dir_name = db.Column(db.String(30), nullable=False)

    # ノードの子供リスト取得
    def get_children(self):
        id_list = db.session.query(Relation.child_id). \
            filter(Relation.id == self.id, Relation.distance == 1).all()
        children_node = db.session.query(Node). \
            filter(Node.id.in_(id_list)).all()
        return children_node

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
        file_path = '/src/train/Images/' + self.get_file_path() + '/**'
        # glob関数でパスを全て取得。このままではフォルダも含まれてしまう（/src/train/Images/root/ みたいな）
        file_path_list = glob(file_path, recursive=True)
        # ファイルのみに絞るフィルターをかける
        return filter(lambda path: os.path.isfile(path), file_path_list)

    # 学習モデルの保存先
    def get_learning_model_path(self):
        return '/src/train/Model/' + self.get_file_path()

    # ノードが葉かどうか判定
    def is_leaf(self):
        return db.session.query(Relation).filter(Relation.id == self.id).count() == 1


"""
# EntityをJsonに変換
class NodeSchema(ma.ModelSchema):
    class Meta:
        model = Node
        fields = ('id', 'name')
"""
