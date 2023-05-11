import unittest
from src.entities.transaction import Transaction
from entities.user import User
import os, sys
from initialize_database import initialize_database

dir = os.path.dirname("transaction_repository.py")
sys.path.append(dir)
from src.repositories.transaction_repository import transaction_repository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.test_transaction = Transaction('niilo','income','paycheck',2000)
        self.test_transaction_2 = Transaction('niilo','expense','rent',1000)
        self.user_niilo = User('niilo', 'niilo10')

    def test_new_transaction(self):
        transaction_repository.new_transaction(self.test_transaction)
        transactions = transaction_repository.get_transactions(self.user_niilo)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].username, 'niilo')
        self.assertEqual(transactions[0].type, 'income')
        self.assertEqual(transactions[0].name, 'paycheck')
        self.assertEqual(transactions[0].amount, 2000)

    def test_get_transactions(self):
        transaction_repository.new_transaction(self.test_transaction)
        transaction_repository.new_transaction(self.test_transaction_2)
        transactions = transaction_repository.get_transactions(self.user_niilo)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].type, 'income')
        self.assertEqual(transactions[1].type, 'expense')
        self.assertEqual(transactions[0].name, 'paycheck')
        self.assertEqual(transactions[1].name, 'rent')