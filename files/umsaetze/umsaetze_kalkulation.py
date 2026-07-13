import geschaeftsprozesse.kalkulation as ka

dateiname = "./files/umsaetze/umsaetze_dat.txt"
rabatte_dat = "./files/umsaetze/rabatte_dat.txt"
umsaetze = []
try:
    with open(file=dateiname, mode="r", encoding="UTF-8") as datei_objekt:
        for zeile in datei_objekt:
            umsaetze.append(float(zeile.strip()))
        print(umsaetze)
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)

print("Gesamtumsatz:")
print(ka.berechne_gesamtumsatz(umsaetze))

print("Max Umsatz:")
print(ka.max_umsatz(umsaetze))

rabattierte_umsaetze = ka.rabatt_anwenden(umsaetze=umsaetze, rabatt=2)
print(rabattierte_umsaetze)


try:
    with open(file=rabatte_dat, mode="w", encoding="UTF-8") as datei_objekt:
        for umsatz in rabattierte_umsaetze:
            datei_objekt.write(f"{umsatz:.2f}\n")
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)