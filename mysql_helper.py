import mysql.connector
from mysql.connector import Error

class MySQLHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish connection to MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        """Execute a query (INSERT, UPDATE, DELETE)."""
        if self.connection is None:
            print("No connection to the database.")
            return
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: {e}")

    def fetch_results(self, query, params=None):
        """Execute a SELECT query and return results."""
        if self.connection is None:
            print("No connection to the database.")
            return None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

