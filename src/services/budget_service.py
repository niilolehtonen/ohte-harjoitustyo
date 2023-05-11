from src.entities.user import User # pylint: disable=import-error
from src.entities.transaction import Transaction # pylint: disable=import-error
from src.repositories.user_repository import (user_repository as default_user_repository) # pylint: disable=import-error
from src.repositories.transaction_repository import (transaction_repository as # pylint: disable=import-error
                                                    default_transaction_repository) # pylint: disable=import-error

class InvalidCredentialsError(Exception):
    pass

class BudgetService:
    """Class responsible for logic of the application

    Attributes:
        user_repository: Instance of the user-repository class.
        transaction_repository: Instance of the transaction-repository class.
    """
    def __init__(self,user_repository=default_user_repository,
                transaction_repository=default_transaction_repository):
        self._user = None
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository

    def create_user(self, username, password):
        """Creates a new user (registration).

        Args:
            username (str): Username for the new user.
            password (str): Password for the new user.

        Returns:
            user: Returns the user-object after it has been inserted in the database.
        """
        user = self._user_repository.create_user(User(username, password))

        return user

    def login(self,username,password):
        """Method for checking that the login credentials are matching.

        Args:
            username (str): Username
            password (str): Password

        Raises:
            InvalidCredentialsError: An error that is raised if the credentials don't match.

        Returns:
            user: User-object
        """

        user = self._user_repository.search_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return user

    def new_expense(self,name,amount):
        """Method for adding a new expense

        Args:
            name (str): Name/description of the expense.
            amount (str): Amount of the expense.
        """

        username = self._user.username
        type = 'expense'
        expense = Transaction(username,type,name,amount)
        self._transaction_repository.new_transaction(expense)

    def new_income(self,name,amount):
        """Method for adding a new income.

        Args:
            name (str): Name/description of the income.
            amount (str): Amount of the income.
        """

        username = self._user.username
        type = 'income'
        income = Transaction(username,type,name,amount)
        self._transaction_repository.new_transaction(income)

    def show_budget(self):
        """Method for fetching the incomes, outcomes and budget(incomes-outcomes).

        Returns:
            tuple: Returns budget value and individual lists of incomes and expenses.
        """

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

    def logout(self):
        self._user = None

budget_service = BudgetService()
