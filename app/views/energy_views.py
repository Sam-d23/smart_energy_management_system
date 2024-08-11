from flask import Blueprint, jsonify, request
from app.models.energy_models import db, User, EnergyData


bp = Blueprint('api', __name__)


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])


@bp.route('/energy_data', methods=['POST'])
def add_energy_data():
    data = request.json
    energy_data = EnergyData(
        user_id=data['user_id'],
        timestamp=data['timestamp'],
        energy_consumed=data['energy_consumed']
    )
    db.session.add(energy_data)
    db.session.commit()
    return jsonify({"message": "Energy data added successfully!"})
