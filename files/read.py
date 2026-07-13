dateiname = "./files/gedichte.txt"
"""
#erste Variante Datei als String komplett 
try: 
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    print(datei_objekt)
    for zeile in datei_objekt:
        print(zeile)
except FileNotFoundError as exception:
    print("Datei nicht gefunden", exception)
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)
finally:
    datei_objekt.close()
"""
#zweite Variante Datei als Liste
try: 
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    liste = datei_objekt.readlines()
    print(liste)
    neue_liste = []
    for zeile in liste:
        if zeile != '\n':
            neue_liste.append(zeile.strip())
    print(neue_liste)
except FileNotFoundError as exception:
    print("Datei nicht gefunden", exception)
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)
finally:
    datei_objekt.close()


"""
try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    for zeile in datei_objekt:
        print(zeile.strip())
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)


try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    zeile = datei_objekt.readline()
    #print(zeile)
    while zeile != "":
        #print(zeile)
        zeile = datei_objekt.readline()
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)

ohne_whitespaces = []
try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    liste  = datei_objekt.readlines()
    for element in liste:
        if element != "\n":
         ohne_whitespaces.append(element.strip())
    print(ohne_whitespaces)
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)

try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    inhalt = datei_objekt.read()
    print(inhalt)
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)


"""