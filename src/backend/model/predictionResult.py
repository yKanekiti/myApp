import dataclasses
from flask_marshmallow import schema
from common.database import ma, db


@dataclasses.dataclass
class PredictionResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    is_leaf = db.Column(db.Integer)


class PredictionResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PredictionResult
