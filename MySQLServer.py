# File: MySQLServer.py
"""Python script to connect to MySQL server and
             create the 'alx_book_store' database."""



import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jonathan@17"
    )
    
    # Create cursor
    cursor = connection.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as error:
    print(f"Error: {error}")
    
finally:
    # Close connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()