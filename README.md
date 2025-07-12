# alx-backend-python

## Python script seed.py that does the following:

1. Connects to the MySQL server.
2. Creates the ALX_prodev database if it does not exist.
3. Connects to that specific database.
4. Creates a user_data table with the specified schema.
5. Loads data from a user_data.csv file.

Inserts each record into the table if it doesn’t already exist (based on user_id).

## ✅ Requirements:
1. MySQL server running
2. mysql-connector-python installed (pip install mysql-connector-python)
3. A user_data.csv file with the format: user_id,name,email,age
