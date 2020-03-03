from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass


class Test_Home(BaseTest):
    def test_index(self):
        with self.app as client:
            request = client.get('/', data={})

            self.assertEqual(200, request.status_code)
            self.assertEqual('Hello, welcome to my app', request.get_json().get('message'))