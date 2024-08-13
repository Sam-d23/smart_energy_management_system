from flask import Blueprint, request, jsonify
from app.models.energy_model import EnergyData
from app import db


bp = Blueprint('energy', __name__, url_prefix='/energy')


@bp.route('/', methods=['POST'])
def create_energy_record():
    data = request.json
    new_record = EnergyData(
        timestamp=data['timestamp'],
        energy_consumed=data['energy_consumed'],
        energy_generated=data['energy_generated']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Record created"}), 201

@bp.route('/', methods=['GET'])
def get_energy_records():
    records = EnergyData.query.all()
    return jsonify([{
        "id": record.id,
        "timestamp": record.timestamp,
        "energy_consumed": record.energy_consumed,
        "energy_generated": record.energy_generated
    } for record in records]), 200
