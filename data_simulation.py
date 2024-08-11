import random
from datetime import datetime, timedelta
from app.models.energy_models import db, EnergyData


def simulate_energy_data(user_id, days=30):
    current_time = datetime.now()
    for day in range(days):
        timestamp = current_time - timedelta(days=day)
        energy_consumed = round(random.uniform(10, 100), 2)
        energy_data = EnergyData(
            user_id=user_id,
            timestamp=timestamp,
            energy_consumed=energy_consumed
        )
        db.session.add(energy_data)
    db.session.commit()
