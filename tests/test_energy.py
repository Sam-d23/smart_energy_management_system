import unittest
from datetime import datetime

from app import create_app, db
from app.models.energy_models import EnergyData
from app.analysis.energy_analysis import (
    total_energy_consumption,
    average_daily_consumption,
    peak_usage_times,
)


class EnergyManagementTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_energy_usage(self):
        response = self.client.post('/add_usage', json={
            'device_id': 'device_1',
            'usage_kwh': 10.5
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Energy usage added successfully', response.data)

    def test_get_energy_usage(self):
        with self.app.app_context():
            usage = EnergyUsage(device_id='device_1', usage_kwh=10.5,
                                timestamp=datetime.utcnow())
            db.session.add(usage)
            db.session.commit()

        response = self.client.get('/get_usage')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'device_1', response.data)

    def test_total_energy_consumption(self):
        with self.app.app_context():
            total = total_energy_consumption('device_1')
            self.assertEqual(total, 0)  # No data, should return 0

    def test_average_daily_consumption(self):
        with self.app.app_context():
            avg = average_daily_consumption('device_1')
            self.assertEqual(avg, 0)  # No data, should return 0

    def test_peak_usage_times(self):
        with self.app.app_context():
            peaks = peak_usage_times('device_1')
            self.assertEqual(peaks, [])  # No data, should return empty list


if __name__ == '__main__':
    unittest.main()
