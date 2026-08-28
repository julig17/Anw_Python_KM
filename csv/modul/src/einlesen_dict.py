import csv
daten = []
datei_name = "./csv/modul/data/artikel.csv"

try:
    with open(datei_name, "r", encoding="UTF-8") as artikel_datei:
        # reader-Objekt zum "CSV-Lesen" der CSV-Datei erstellen
        csv_reader = csv.DictReader(artikel_datei)
        zeilen_liste = list(csv_reader)
        print(zeilen_liste)
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print("sonstiges Dateizugriffsfehler", e)


print(float(zeilen_liste[0]['Preis']))


for zeile in zeilen_liste:
    for spaltenname, wert in zeile.items():
        print(f"{spaltenname:15}: {wert}")
    print("-" * 40)