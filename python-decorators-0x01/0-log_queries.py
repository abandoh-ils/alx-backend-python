from datetime import datetime
import sqlite3
import functools

# Decorator to log SQL queries with timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        if query:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Executing SQL Query: {query}")
        else:
            print("[LOG] No SQL query found to log.")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Run the function
users = fetch_all_users(query="SELECT * FROM users")
for user in users:
    print(user)
