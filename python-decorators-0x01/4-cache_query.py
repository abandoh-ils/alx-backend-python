import time
import sqlite3
import functools

# Global in-memory cache for queries
query_cache = {}

"""your code goes here"""

# Decorator to manage database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)

        if query in query_cache:
            cached_result, cached_time = query_cache[query]
            print(f"[CACHE HIT] Returning cached result from {cached_time}")
            return cached_result
        else:
            result = func(conn, *args, **kwargs)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            query_cache[query] = (result, timestamp)
            print(f"[CACHE MISS] Caching result at {timestamp}")
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

# Display result
print(users_again)
