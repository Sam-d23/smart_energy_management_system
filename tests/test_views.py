import unittest
from app import create_app, db
from datetime import datetime
from app.models import EnergyData


class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_energy_data(self):
        response = self.client.post('/api/energy_data', json={
            'user_id': 1,
            'timestamp': datetime(2024, 8, 11, 0, 0, 0),
            'energy_consumed': 45.5
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
                response.json['message'], 'Energy data added successfully')

        # Verify that the data was actually added to the database
        with self.app.app_context():
            data = EnergyData.query.filter_by(user_id=1).first()
            self.assertIsNotNone(data)
            self.assertEqual(data.energy_consumed, 45.5)
            self.assertEqual(data.timestamp, datetime(2024, 8, 11, 0, 0, 0))

    def test_get_energy_data(self):
        # Adding some data first
        with self.app.app_context():
            energy_data = EnergyData(
                    user_id=1, timestamp=datetime(2024, 8, 11, 0, 0, 0),
                    energy_consumed=45.5)
            db.session.add(energy_data)
            db.session.commit()

        response = self.client.get('/api/energy_data/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['energy_consumed'], 45.5)
        self.assertEqual(response.json['timestamp'], '2024-08-11T00:00:00')


if __name__ == '__main__':
    unittest.main()
