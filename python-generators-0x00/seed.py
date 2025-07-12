import mysql.connector
import csv
import uuid

# ---------- Prototypes ----------

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='alx_dev',
        password='alx_dev'  # Replace with your MySQL root password
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host='localhost',
        user='alx_dev',
        password='alx_dev',  # Replace with your MySQL root password
        database='ALX_prodev'
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    connection.commit()
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()

    for row in data:
        user_id, name, email, age = row
        cursor.execute("SELECT COUNT(*) FROM user_data WHERE user_id = %s", (user_id,))
        exists = cursor.fetchone()[0]
        if not exists:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))
    
    connection.commit()
    cursor.close()

def load_csv(filepath):
    with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        return [row for row in reader]

# ---------- Main Execution ----------

if __name__ == "__main__":
    try:
        print("Connecting to MySQL server...")
        conn = connect_db()
        print("Creating database...")
        create_database(conn)
        conn.close()

        print("Connecting to ALX_prodev...")
        prodev_conn = connect_to_prodev()
        print("Creating user_data table...")
        create_table(prodev_conn)

        print("Loading CSV data...")
        data = load_csv("user_data.csv")

        print("Inserting data...")
        insert_data(prodev_conn, data)

        print("✅ Database seeded successfully.")
        prodev_conn.close()
    except Exception as e:
        print("❌ Error occurred:", e)
