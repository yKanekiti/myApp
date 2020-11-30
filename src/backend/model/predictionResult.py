import dataclasses
from flask_marshmallow import schema
from common.database import ma


@dataclasses.dataclass
class PredictionResult:
    id: int
    name: str
    value: float


class PredictionResultSchema(ma.Schema):
    class Meta:
        model = PredictionResult
