import sys
sys.path.append("src/backend/")

from common.database import db, ma, desc
from common.config import Config


class Relation(db.Model):
    id = db.Column(db.Integer, nullable=False)
    child_id = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)


