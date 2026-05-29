from configparser import ConfigParser

import connect as cn
import query as qr
import insert as insert

"""
Das ist unsere Haupfunktion, ab hier startet quasi die Ausführung
Die Methode liest aus der Konfig Datei settings.ini die Konfi-Parameter
die wir zur Herstellung der Verbindung mit der DB benötigen
Die VErbindung selbst wird in dem Skript connect.py hegestellt, von hier nur aufgerufen
Die QUERYS werden in dem Skript query.py gemacht
DIE INSERTS ind dem Script insert.py
"""
def main():
    filename = "db_query - buch\settings.ini"

    config = ConfigParser()
    try:
        config.read(filename)
    except:
        print("settings.ini file errror")
        raise SystemExit()
    settings = config["DBSettings"]

    # Verbindungsparameter für die DB Session
    host = settings["host"]
    user = settings["user"]
    password = settings["password"]
    database = settings["database"]
    
    
    # Verbindung herstellen
    connection = cn.connect_to_db(host, user, password, database)

    if connection:
        # query über das skript query
        qr.query_tables(connection)
        # insert über das skript insert
        insert.insert_data_table(connection)
        connection.close()
        print("Verbindung geschlossen.")

if __name__ == "__main__":
    main()