import unittest
from helpers import build_url
from models.user import User
import requests



class TestAPIUsers(unittest.TestCase):
    def setUp(self):
        from uuid import uuid4
        user_data = {
            'name': 'test_name',
            'handle': 'test_handle',
            'email': 'test_email',
            'password': str(uuid4())
        }
        r = requests.post(build_url('api/users'), data=user_data).json()
        self.assertEqual(r.get('status'), 'OK')
        self.user_dict = r.get('user')
        self.assertEqual(user_data.get('name'), self.user_dict.get('name'))
    def test_create_user_type(self):
        user_dict = self.user_dict
        self.assertEqual(type(user_dict), dict)
    """
    def test_get_user_status(self):
        r = requests.get('/api/users/id/333').json()
        self.assertEqual(r.get('status'), 'OK')
    def test_update_user_status(self):
        r = requests.put('/api/users/id/333/attribute/value').json()
        self.assertEqual(r.get('status'), 'OK')
    def test_delete_user_status(self):
        r = requests.delete('/api/users/id/333/attribute/value').json()
        self.assertEqual(r.get('status'), 'OK')
    def test_get_user_type(self):
        r = requests.get('/api/users/id/333').json()
        self.assertEqual(type(r.get('user')), User)
    def test_get_n_users(self):
        r = requests.get('/api/users/3').json()
        self.assertEqual(len(r.get('users')), 3)        
    def test_update_user_type(self):
        r = requests.put('/api/users/id/333/attribute/value').json()
        self.assertEqual(type(r.get('user')), User)
    def test_get_user_id(self):
        r = requests.get('/api/users/id/333').json()
        self.assertEqual(r.get('user').get('id'), '333')
    def test_update_user_attribute_and_value(self):
        r = requests.put('/api/users/id/333/attribute/value').json()
        self.assertEqual(r.get('user').get('attribute'), 'value')
    """


if __name__ == "__main__":
    unittest.main()