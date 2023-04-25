from src.transaction import Transaction
from src.user import User
from src.database_connection import get_database_connection

class TransactionRepository:

    def __init__(self,connection):
        self._connection = connection

    def new_transaction(self, transaction):
        
        cursor = self._connection.cursor()
        
        cursor.execute('INSERT INTO TRANSACTIONS (username, type, name, amount) VALUES (?, ?, ?, ?)', 
                    (transaction.username, transaction.type, transaction.name, transaction.amount))
        
        self._connection.commit()

    def get_transactions(self, user):
        username = user.username
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM TRANSACTIONS WHERE username = ?', (username,))
        rows = cursor.fetchall()
        return [Transaction(*row) for row in rows]


transaction_repository = TransactionRepository(get_database_connection())