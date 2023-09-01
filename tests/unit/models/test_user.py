from unittest import TestCase
from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test_username', 'test_password')
        self.assertEqual('test_username', user.username)
        self.assertEqual('test_password', user.password)
        
