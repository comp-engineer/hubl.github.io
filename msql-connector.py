import mysql.connector

# Function to establish a database connection
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        print("Connected to the database!")
        return db

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to insert data into the database
def insert_data(db, data):
    cursor = db.cursor()
    
    try:
        insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
        cursor.execute(insert_query, data)
        db.commit()
        print("Data inserted successfully!")

    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error: {err}")

    finally:
        cursor.close()

# Function to retrieve data from the database
def retrieve_data(db):
    cursor = db.cursor()

    try:
        select_query = "SELECT * FROM your_table"
        cursor.execute(select_query)
        result = cursor.fetchall()

        for row in result:
            print(f"Column 1: {row[0]}, Column 2: {row[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

# Function to close the database connection
def close_database(db):
    db.close()
    print("Database connection closed.")

if __name__ == "__main__":
    # Replace with your data
    data_to_insert = ("value1", "value2")
    
    # Connect to the database
    database = connect_to_database()

    if database:
        # Insert data into the database
        insert_data(database, data_to_insert)

        # Retrieve and print data from the database
        retrieve_data(database)

        # Close the database connection
        close_database(database)
