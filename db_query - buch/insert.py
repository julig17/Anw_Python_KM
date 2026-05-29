import csv

"""
Dieses Skript liest Daten aus einer CSV Datei und 
führt für jede ausgelesen Zeile ein INSERT 
"""
def insert_data_table(connection):
    csv_data = ""
    # lese Daten aus der csv Datei 
    try :
       csv_data = csv.reader(open("db_query - buch/buch.csv"), delimiter=';') 
       print(csv_data)
    except OSError as e:
        print(f"Fehler beim Dateilesen: {e}")   
    try:
        cursor = connection.cursor()
        #springe auf die erste Zeiled der Daten
        #next(csv_data)
        #lese Zeile für Zeile aus und führe ein INSERT auf Tabelle aus
        for row in csv_data:
            print(row)
            cursor.execute('INSERT INTO buch(isbn, titel, erscheinungsjahr) VALUES(%s, %s, %s)',row)
    except OSError as e:
        print(f"Fehler beim Insert: {e}")

    finally:
        connection.commit()
        cursor.close()