import random
from datetime import datetime, timedelta
from app import create_app, db
from app.models.energy_model import EnergyUsage


def simulate_data(device_id, days=7):
    app = create_app()
    with app.app_context():
        for day in range(days):
            for hour in range(24):
                usage = EnergyUsage(
                    device_id=device_id,
                    usage_kwh=round(random.uniform(0.1, 2.0), 2),
                    timestamp=datetime.utcnow() - timedelta(
                        days=day, hours=hour)
                )
                db.session.add(usage)
        db.session.commit()


if __name__ == '__main__':
    simulate_data('device_1')
    simulate_data('device_2')
