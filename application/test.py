from flask_testing import TestCase
from application import create_app, db
from models import User


class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class SomeTest(MyTest):
    def test_something(self):
        user = User('test')
        db.session.add(user)
        db.session.commit()

        # this works
        assert user in db.session

        response = self.client.get("/")

        # this raises an AssertionError
        assert user in db.session

import unittest
if __name__ == '__main__':
    unittest.main()
