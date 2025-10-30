import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="67.205.178.115",
            user="powerbi",
            password="exotic@Powerbi@2022",
            database="exoticindia"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
