from app.models.energy_models import db, EnergyData


def calculate_total_energy_consumed(user_id):
    total_energy = db.session.query(db.func.sum(EnergyData.energy_consumed))\
        .filter(EnergyData.user_id == user_id).scalar()
    return total_energy or 0
