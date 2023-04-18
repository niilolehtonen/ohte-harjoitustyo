import unittest
from user import User
import os, sys
from initialize_database import initialize_database

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

    def test_get_all(self):

        user_repository.create_user(self.user_niilo)
        user_repository.create_user(self.user_timo)
        all_users = user_repository.get_all()

        self.assertEqual(len(all_users), 2)

        self.assertEqual(all_users[0].username, self.user_niilo.username)
        self.assertEqual(all_users[0].password, self.user_niilo.password)

        self.assertEqual(all_users[1].username, self.user_timo.username)
        self.assertEqual(all_users[1].password, self.user_timo.password)

    def test_delete_all_users(self):
        user_repository.create_user(self.user_niilo)
        user_repository.create_user(self.user_timo)
        all_users = user_repository.get_all()

        self.assertEqual(len(all_users), 2)

        user_repository.delete_all_users()

        all_users = user_repository.get_all()
        self.assertEqual(len(all_users), 0)

    def test_search_username(self):
        user_repository.create_user(self.user_niilo)
        user_repository.create_user(self.user_timo)

        retrieved_user = user_repository.search_username(self.user_niilo.username)
        self.assertEqual(retrieved_user.username, self.user_niilo.username)
        self.assertEqual(retrieved_user.password, self.user_niilo.password)

        retrieved_user = user_repository.search_username(self.user_timo.username)
        self.assertEqual(retrieved_user.username, self.user_timo.username)
        self.assertEqual(retrieved_user.password, self.user_timo.password)