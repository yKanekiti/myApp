import sys
sys.path.append("src/backend/")

from common.database import db, ma, desc, Config


class Relation(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    child_id = db.Column(db.Integer, nullable=False, primary_key=True)
    distance = db.Column(db.Integer, nullable=False, primary_key=True)


