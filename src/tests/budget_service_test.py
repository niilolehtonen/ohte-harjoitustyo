import unittest
from unittest.mock import MagicMock
from entities.user import User
import os,sys
dir = os.path.dirname("budget_service.py")
sys.path.append(dir)
from src.services.budget_service import BudgetService, InvalidCredentialsError

class BudgetServiceTest(unittest.TestCase):
    def setUp(self):
        self.user_repository = MagicMock()
        self.transaction_repository = MagicMock()
        self.budget_service = BudgetService(self.user_repository)

    def test_create_user(self):
        user_repository_mock = MagicMock()
        self.budget_service = BudgetService(user_repository_mock)
        user = User('niilo', 'niilo10')
        user_repository_mock.create_user.return_value = user

    def test_login_with_valid_credentials(self):
        username = "niilo"
        password = "niilo00"
        user = MagicMock(password=password)
        self.user_repository.search_username.return_value = user

        result = self.budget_service.login(username, password)

        self.assertEqual(result, user)
        self.user_repository.search_username.assert_called_once_with(username)
        self.assertEqual(self.budget_service._user, user)

    def test_login_with_invalid_credentials(self):
        username = "niilo"
        password = "niilo00"
        self.user_repository.search_username.return_value = None

        with self.assertRaises(InvalidCredentialsError):
            self.budget_service.login(username, password)

        self.user_repository.search_username.assert_called_once_with(username)

        self.user_repository.search_username.reset_mock()

        user = MagicMock(password="wrongpassword")
        self.user_repository.search_username.return_value = user

        with self.assertRaises(InvalidCredentialsError):
            self.budget_service.login(username, password)

        self.user_repository.search_username.assert_called_once_with(username)

    def test_new_income(self):
        name = 'paycheck'
        amount = 500
        self.budget_service.new_income()