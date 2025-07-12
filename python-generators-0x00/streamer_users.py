import mysql.connector

def stream_users():
    """Generator that yields user_data rows one by one."""
    connection = mysql.connector.connect(
        host="localhost",
        user="alx_dev",
        password="alx_dev",  # Replace with your MySQL password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:  # Single loop as required
        yield row

    cursor.close()
    connection.close()
