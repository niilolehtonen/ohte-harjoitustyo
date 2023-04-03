import unittest
from user import User
from src.repositories import user_repository #This import doesn't work yet


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
