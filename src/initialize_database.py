from database_connection import get_database_connection


def drop_tables(connection):
    """Clears all the tables in the database

    Args:
        connection: Connection-object of the database conncetion.
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS USERS;
    ''')

    cursor.execute('''
            DROP TABLE IF EXISTS TRANSACTIONS;
        ''')

    connection.commit()


def create_tables(connection):
    """Creates tables in the database.

    Args:
        connection: Connection-object of the database conncetion.
    """
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE USERS (
                        USER_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
                        USERNAME TEXT,
                        PASSWORD TEXT
        );
        ''')

    cursor.execute('''CREATE TABLE TRANSACTIONS (
                        USERNAME TEXT,
                        TYPE TEXT,
                        NAME TEXT,
                        AMOUNT INTEGER    
    );
    ''')

    connection.commit()


def initialize_database():
    """Initializes tables in the database.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
