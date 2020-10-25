from ..common.database import db, ma


class Node(db.Model):
    __tableName__ = 'node'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

