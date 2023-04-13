import unittest
from user import User
import os, sys
from src.initialize_database import initialize_database

dir = os.path.dirname("user_repository.py")
sys.path.append(dir)
from src.repositories.user_repository import user_repository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        initialize_database()
        user_repository.delete_all_users()
        self.user_niilo = User('niilo', 'niilo10')
        self.user_timo = User('timo', 'timo11')
    
    def test_create_user(self):
        user_repository.create_user(self.user_niilo)
        all_users = user_repository.get_all()
        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, self.user_niilo.username)
        self.assertEqual(all_users[0].password, self.user_niilo.password)
