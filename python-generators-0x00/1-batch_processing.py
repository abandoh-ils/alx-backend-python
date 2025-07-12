import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of rows from user_data."""
    conn = mysql.connector.connect(
        host="localhost",
        user="alx_dev",
        password="alx_dev",  # Replace with your password
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:  # 🔁 1st loop
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch  # Yield the final smaller batch

    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """Generator that yields users over age 25 from each batch."""
    result = []
    for batch in stream_users_in_batches(batch_size):  # 🔁 2nd loop
        filtered = [user for user in batch if float(user['age']) > 25]  # 🔁 3rd loop (list comprehension)
        result.append(filtered)
        yield filtered

    # return result

if __name__ == "__main__":
    for user in batch_processing(batch_size=5):
        print(user)
