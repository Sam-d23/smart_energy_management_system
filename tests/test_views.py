import unittest
from app import create_app, db


class TestViews(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)


    def test_add_energy_data(self):
        response = self.client.post('/api/energy_data', json={
            'user_id': 1,
            'timestamp': '2024-08-11T00:00:00',
            'energy_consumed': 45.5
        })
        self.assertEqual(response.status_code, 200)
