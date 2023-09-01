from tests.base_test import BaseTest
from models.user import UserModel


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('bulat', 'qwerty')
            self.assertIsNone(user.find_by_username('bulat'))
            user.save_to_db()
            self.assertIsNotNone(user.find_by_username('bulat'))

    def test_find_by_username(self):
        with self.app_context():
            user = UserModel('bulat', 'qwerty')
            user.save_to_db()
            u = user.find_by_username('bulat')
            self.assertIsNotNone(u)
            self.assertEqual(u.username, 'bulat')

    def test_find_by_id(self):
        with self.app_context():
            user = UserModel('bulat', 'qwerty')
            user.save_to_db()
            u = user.find_by_id(1)
            self.assertIsNotNone(u)
            self.assertEqual(u.id, 1)
