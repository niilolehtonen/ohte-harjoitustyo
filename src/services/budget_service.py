from src.user import User # pylint: disable=import-error
from src.transaction import Transaction # pylint: disable=import-error
from src.repositories.user_repository import (user_repository as default_user_repository) # pylint: disable=import-error
from src.repositories.transaction_repository import (transaction_repository as
                                                    default_transaction_repository) # pylint: disable=import-error

class InvalidCredentialsError(Exception):
    pass

class BudgetService:

    def __init__(self,user_repository=default_user_repository,
                transaction_repository=default_transaction_repository):
        self._user = None
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository

    def create_user(self, username, password):

        user = self._user_repository.create_user(User(username, password))

        return user

    def login(self,username,password):

        user = self._user_repository.search_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def new_expense(self,name,amount):

        username = self._user.username
        type = 'expense'
        expense = Transaction(username,type,name,amount)
        self._transaction_repository.new_transaction(expense)

    def new_income(self,name,amount):

        username = self._user.username
        type = 'income'
        income = Transaction(username,type,name,amount)
        self._transaction_repository.new_transaction(income)

    def show_budget(self):
        expenses = []
        incomes = []
        sum_expenses = 0
        sum_incomes = 0
        transactions = self._transaction_repository.get_transactions(self._user)
        if len(transactions) != 0:
            for i in transactions:
                if i.type == 'expense':
                    expenses.append(i)
                if i.type == 'income':
                    incomes.append(i)

        if len(expenses) > 0:
            for i in expenses:
                sum_expenses += int(i.amount)

        if len(incomes) > 0:
            for i in incomes:
                sum_incomes += int(i.amount)

        budget = sum_incomes - sum_expenses

        return (budget,expenses,incomes)

budget_service = BudgetService()
