from src.transaction import Transaction # pylint: disable=import-error
from src.database_connection import get_database_connection # pylint: disable=import-error

class TransactionRepository:
    """Class responsible for database operations regarding transactions

    Attributes:
        connection = Database connection.
    """

    def __init__(self,connection):
        self._connection = connection

    def new_transaction(self, transaction):
        """Method for inserting a new transaction into the database. 

        Args:
            transaction: Transaction-object.
        """
        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO TRANSACTIONS (username, type, name, amount) VALUES (?, ?, ?, ?)'
        ,(transaction.username, transaction.type, transaction.name, transaction.amount))

        self._connection.commit()

    def get_transactions(self, user):
        """Method for fetching transactions from the database.

        Args:
            user: User-object.

        Returns:
            list: Returns a list of all the transaction-objects matching the username.
        """
        username = user.username
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM TRANSACTIONS WHERE username = ?', (username,))
        rows = cursor.fetchall()
        return [Transaction(*row) for row in rows]


transaction_repository = TransactionRepository(get_database_connection())
