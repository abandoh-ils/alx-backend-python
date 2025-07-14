# generate dummy data

import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Sample dummy user data
dummy_users = [
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Charlie Brown', 'charlie@example.com'),
    ('Diana Prince', 'diana@example.com'),
    ('Ethan Hunt', 'ethan@example.com'),
    ('Fiona Gallagher', 'fiona@example.com'),
    ('George Orwell', 'george@example.com'),
    ('Hannah Baker', 'hannah@example.com'),
    ('Ian Malcolm', 'ian@example.com'),
    ('Jane Eyre', 'jane@example.com')
]

# Insert users if table is empty
cursor.execute('SELECT COUNT(*) FROM users')
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO users (name, email)
        VALUES (?, ?)
    ''', dummy_users)
    print("Inserted dummy user data.")
else:
    print("User table already contains data. Skipping insert.")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and table setup complete.")
