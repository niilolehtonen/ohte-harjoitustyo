from src.user import User # pylint: disable=import-error
from src.database_connection import get_database_connection # pylint: disable=import-error

def get_user_by_row(row):
    if row:
        return User(row['username'], row['password'])
    return None

class UserRepository:
    """Class responsible for database operations regarding users

    Attributes:
        connection: Database connection.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        """Method to fetch all the users from the database.

        Returns:
            list: Returns a list of user-objects.
        """
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM USERS')

        rows = cursor.fetchall()

        all_users = []

        for row in rows:
            all_users.append(get_user_by_row(row))

        return all_users

    def create_user(self, user):
        """Method for inserting a new user into the database.

        Args:
            user: User-object that will be inserted into the database.

        Returns:
            user: User-object
        """
        cursor = self._connection.cursor()

        cursor.execute('INSERT INTO USERS (username, password) VALUES (?,?)',
                        (user.username,user.password))

        self._connection.commit()

        return user

    def delete_all_users(self):
        """Method for deleting users from the database
        """

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM USERS')

        self._connection.commit()

    def search_username(self,username):
        """Method for searching a user by username

        Args:
            username (str): Username to be searched

        Returns:
            user: Returns the matching user-object for the username.
        """
        cursor = self._connection.cursor()

        cursor.execute('SELECT username, password FROM USERS WHERE username = ?',(username,))

        row = cursor.fetchone()

        return get_user_by_row(row)

user_repository = UserRepository(get_database_connection())
