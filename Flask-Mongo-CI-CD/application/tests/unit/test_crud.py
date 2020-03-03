from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        # print(app.config['MONGO_URI'])

    def tearDown(self):
        pass

class TestCrud(BaseTest):
    def test_list_0(self):
        with self.app as client:
            request = client.get('/list')

            self.assertEqual(200, request.status_code)
            # self.assertEqual([], request.get_json().get('users'))

    def test_insert(self):
        with self.app as client:
            request = client.get('/insert/?name=aan&npk=1234')
            self.assertEqual(201, request.status_code)

            self.assertEqual('aan', request.get_json().get('user')[0]['name'])
            self.assertEqual('1234', request.get_json().get('user')[0]['npk'])

    def test_list(self):
        with self.app as client:
            insert = client.get('/insert/?name=aan&npk=1234')
            request = client.get('/list')
            self.assertEqual(2, len(request.get_json().get('users')))