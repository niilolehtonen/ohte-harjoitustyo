from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS USERS;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE USERS (
                        USER_ID TEXT AUTO_INCREMENT PRIMARY KEY,
                        USERNAME TEXT,
                        PASSWORD TEXT
        );
        ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()