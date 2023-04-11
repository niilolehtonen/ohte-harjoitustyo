from user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    if row:
        return User(row['username'], row['password'])
    else:
        return None

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM USERS')

        rows = cursor.fetchall()

        all_users = []

        for row in rows:
            all_users.append(get_user_by_row(row))
        
        return all_users

    def create_user(self, user):

        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO USERS (username, password) VALUES (?,?)',(user.username,user.password))

        self._connection.commit()

        return user

    def delete_all_users(self):

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM USERS')

        self._connection.commit()

    def search_username(self,username):

        cursor = self._connection.cursor()

        cursor.execute('SELECT  user FROM USERS WHERE username = ?',(username,))

        row = cursor.fetchone()

        return get_user_by_row(row)

user_repository = UserRepository(get_database_connection())