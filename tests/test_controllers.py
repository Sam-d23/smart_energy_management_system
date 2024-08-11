import unittest
from app import create_app, db
from app.models.energy_models import User, EnergyData
from app.controllers.energy_controller import calculate_total_energy_consumed
from datetime import datetime


class TestControllers(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_calculate_total_energy_consumed(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()

        energy_data1 = EnergyData(
                user_id=user.id, timestamp=datetime.now(),
                energy_consumed=30.0)
        energy_data2 = EnergyData(
                user_id=user.id, timestamp=datetime.now(),
                energy_consumed=70.0)
        db.session.add(energy_data1)
        db.session.add(energy_data2)
        db.session.commit()

        total_energy = calculate_total_energy_consumed(user.id)
        self.assertEqual(total_energy, 100.0)
