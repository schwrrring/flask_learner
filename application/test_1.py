from flask_testing import TestCase
from application import create_app, db
from application.models import User, Meldung


class MyTest(TestCase):

    def create_app(self):

        # pass in test configuration
        return create_app('TestingConfig')

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class SomeTest(MyTest):
    def test_something(self):
        user = User(name='tesst')
        db.session.add(user)
        db.session.commit()
        assert user in db.session

    def test_insert_meldung(self):
        meldung = Meldung(name='tesst')
        db.session.add(meldung)
        db.session.commit()
        assert meldung in db.session
    # def test_something_2(self):
    #     user = Meldung(name='tesst')
    #     db.session.add(user)
    #     db.session.commit()
    #     # this works
    #     assert user in db.session
    # #
    # # def test_something_2(self):
    #     user = Meldung(hidden_name='tsdfsdf')
    #     db.session.add(user)
    #     db.session.commit()
    #     # this works
    #     assert user in db.session

import unittest
if __name__ == '__main__':
    unittest.main()
