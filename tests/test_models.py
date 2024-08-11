import unittest
from app import create_app
from app.models.energy_models import db, User, EnergyData
from datetime import datetime


class TestModels(unittest.TestCase):


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


    def test_user_model(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)


    def test_energy_data_model(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()

        energy_data = EnergyData(
                user_id=user.id, timestamp=datetime.now(),
                energy_consumed=50.5)
        db.session.add(energy_data)
        db.session.commit()

        self.assertEqual(EnergyData.query.count(), 1)
