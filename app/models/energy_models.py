from app.models.base_model import BaseModel
from app import db


class EnergyData(BaseModel):
    __tablename__ = 'energy_data'

    timestamp = db.Column(db.DateTime, nullable=False)
    energy_consumed = db.Column(db.Float, nullable=False)
    energy_generated = db.Column(db.Float, nullable=False)
