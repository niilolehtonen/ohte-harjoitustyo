import unittest
from user import User
from user_repository import user_repository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.user_niilo = User('niilo', 'niilo10')
        self.user_timo = User('timo', 'timo11')
    
    def test_create_user(self):
        user_repository.create(self.user_niilo)
        all_users = user_repository.find_all_users()
        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, self.user_niilo.username)
