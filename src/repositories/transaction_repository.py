from src.transaction import Transaction
from src.user import User
from src.database_connection import get_database_connection

class TransactionRepository:

    def __init__(self,connection):
        self._connection = connection

    def get_user_id(self,user):
        cursor = self._connection.cursor()

        cursor.execute('SELECT user_id FROM USERS WHERE username = ?',(user.username))

        id = cursor.fetchone()

        return id

    def new_transcation(self,transaction):

        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO TRANSACTIONS (user_id,type,name,amount) VALUES (?,?,?,?)',(transaction.user_id,transaction.type,transaction.name,transaction.amount))

        self._connection.commit()

    def get_transactions(self,user):

        user_id = self.get_user_id(user)

        cursor = self._connection.cursor('SELECT * FROM TRANSACTIONS WHERE user_id = ?'(user_id))

        transactions = cursor.fetchall()

        return transactions

transaction_repository = TransactionRepository(get_database_connection())