from ..common.database import db
from ..common.config import Config
from glob import glob


class Relation(db.Model):
    id = db.Column(db.Integer, nullable=False)
    child_id = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)


