import mysql.connector

# Define the custom context manager class
class DatabaseConnection:
    def __init__(self, host, user, password, database):
        # Save database connection details
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None  # Will store the connection object
        self.cursor = None  # Will store the cursor object

    def __enter__(self):
        # Open the connection and return the cursor
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self.cursor  # This gets assigned to the variable in the `with` block

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the cursor and connection when the block ends
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()