import mysql.connector

class ExecuteQuery:
    def __init__(self, host, user, password, database, query, params=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.query = query
        self.params = params if params else ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        # Open connection
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        print("Database connection opened.")

        # Execute query
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results  # Directly return the query results

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.conn.commit()
            print("Transaction committed.")
        else:
            self.conn.rollback()
            print("Transaction rolled back due to exception:", exc_value)

        # Cleanup
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")


# Example usage
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > %s"
    params = (25,)

    with ExecuteQuery(
        host="localhost",
        user="alx_dev",
        password="alx_dev",
        database="ALX_prodev",
        query=query,
        params=params
    ) as results:
        for row in results:
            print(row)
