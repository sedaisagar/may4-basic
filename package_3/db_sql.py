import sqlite3 as sql

try:
    
    # Create / Connect to a database
    connection = sql.connect("sample.db")

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Create a table
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        address TEXT
    )
    '''
    )

    # CRUD OPERATIONS

    # Create -  INSERT OPERATION
    # cursor.execute(
    #     '''
    #     INSERT INTO users (name, age, address) VALUES (?,?,?)
    #     ''', ("Sagar Thapa", 35, "Kathmandu")
    # )
    # connection.commit() # commit the changes to the database

    # Read - SELECT OPERATION
    
    # Multiple records
    # cursor.execute(
    #     '''
    #     SELECT * FROM users
    #     '''
    # )
    # users = cursor.fetchall() # fetch all the records from the users table
    
    # user_data = []

    # for user in users:
    #     id, name, age, address = user
    #     user_data.append({
    #         "id": id,
    #         "name": name,
    #         "age": age,
    #         "address": address
    #     })

    # print(user_data)

    # Single record
    # cursor.execute(
    #     '''
    #     SELECT * FROM users WHERE id = ?
    #     ''', (1,)
    # )

    # id, full_name, age, address = cursor.fetchone() # fetch one record from the users table

    # print({
    #     "id": id,
    #     "name": full_name,
    #     "age": age,
    #     "address": address
    # })

    # Update - UPDATE OPERATION
    # cursor.execute(
    #     '''
    #     UPDATE users SET age = ?, address = ? WHERE id = ?
    #     ''', (40, 'Hetauda', 1)
    # )
    # connection.commit() # commit the changes to the database

    # Delete - DELETE OPERATION
    # cursor.execute(
    #     '''
    #     DELETE FROM users WHERE id = ?
    #     ''', (2,)
    # )
    # connection.commit() # commit the changes to the database
    
except Exception as e:
    connection.rollback() # rollback the changes in case of an error
    print(e)
finally:
    connection.close()
    print("Database connection closed")


# BEGIN;
# INSERT INTO users (name, age, address) VALUES ("Sagar Sedai", 30, "Kathmandu");

# COMMIT; <- IF OK then commit the changes to the database
# ROLLBACK; <- IF NOT OK then rollback the changes to the database