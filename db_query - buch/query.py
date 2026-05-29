""" QUERY für Tabellen der Datenbank abfragen"""
def query_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")

        print("Tabellen in der Datenbank:")
        for (table_name,) in cursor.fetchall():
            print(f" - {table_name}")

    except Error as e:
        print(f"Fehler bei der Abfrage: {e}")

    finally:
        cursor.close()
