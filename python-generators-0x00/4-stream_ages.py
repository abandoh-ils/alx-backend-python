import seed  # assumes seed.py contains connect_to_prodev()

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    conn = seed.connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # 🔁 1st loop
        yield float(age)

    cursor.close()
    conn.close()

def compute_average_age():
    """Compute average age of users using a generator."""
    total_age = 0
    count = 0

    for age in stream_user_ages():  # 🔁 2nd loop
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")

# Run the script
if __name__ == "__main__":
    compute_average_age()
