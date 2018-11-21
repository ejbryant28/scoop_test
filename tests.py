import unittest

from server import app

from model import connect_to_db, db

from seed import load_tests

from datetime import datetime


class Tests(unittest.TestCase):
    """"""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        #connect to db
        connect_to_db(app, 'postgres:///testcalculator')
        db.create_all()

        load_tests()

    def tearDown(self):
        """close session at end"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()