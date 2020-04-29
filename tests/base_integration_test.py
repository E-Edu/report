from unittest import TestCase
from app import app
from report import db

class BaseTest(TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()

        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()