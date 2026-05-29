import mysql.connector
from mysql.connector import Error

""" diese Funktion ist für Verbindung zur MySQL-Datenbank herstellen"""
def connect_to_db(host, user, password, database):
    
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Verbindung erfolgreich hergestellt!")
            return connection

    except Error as e:
        print(f"Fehler bei der Verbindung: {e}")
        return None
