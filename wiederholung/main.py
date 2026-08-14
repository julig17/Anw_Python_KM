#Konstanten
NUMMER = "nummer"
BEZEICHNUNG = "bezeichnung"
PREIS = "preis"
BESTAND = "bestand"


def lese_aus_datei(dateiname):
    inhalt = []
    try: 
        with open(file=dateiname, mode="r", encoding="utf-8") as file:
            inhalt = file.readlines()
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except Exception as e:
        print("sonstige Dateifehler", e)  
    return inhalt

def entferne_whitespaces_und_verarbeite_artikel(inhalt):
    for i in range(len(inhalt)):
        inhalt[i] = inhalt[i].strip().split(';') 
        for j in range(len(inhalt[i])):
            inhalt[i][j] = datentyp_konvertieren(inhalt[i][j])
        #inhalt[i][0] = int(inhalt[i][0])  # Artikelnummer
        #inhalt[i][2] = float(inhalt[i][2])  # Preis
        #inhalt[i][3] = int(inhalt[i][3])    # Menge 
    return inhalt

def datentyp_konvertieren(element):
    try:
        return int(element)
    except ValueError:
        try:
            return float(element)
        except ValueError:
            return element

def dump_in_dictionary(artikel_liste):
    artikel_liste_dict = []
    for artikel in artikel_liste:
        artikel_dict = {
            NUMMER: artikel[0],
            BEZEICHNUNG: artikel[1],
            PREIS: artikel[2],
            BESTAND: artikel[3]
        }
        artikel_liste_dict.append(artikel_dict)
    return artikel_liste_dict   


def ausgabe(inhalt_als_dict):
    print("Ausgabe der Daten:")
    for artikel in inhalt_als_dict:
        print(f"{artikel[NUMMER]} -  {artikel[BEZEICHNUNG]} - {artikel[PREIS]:.2f} - {artikel[BESTAND]}")

def ausgabe_gefiltert(inhalt_als_dict, filtere_nach=None, anzahl=None):
    print("\nGefilterte Ausgabe der Daten:")
    for artikel in inhalt_als_dict:
        if filtere_nach == BESTAND and artikel[BESTAND] < anzahl:
            print(f"{artikel[BEZEICHNUNG]}")


def berechne_artikel_wert(inhalt_als_dict):
    print("\nWert pro Artikel:")
    for artikel in inhalt_als_dict:
        wert = artikel[PREIS] * artikel[BESTAND]
        print(f"{artikel[BEZEICHNUNG]} - {wert:.2f}")

def berechne_artikel_gesamtwert(inhalt_als_dict):
    gesamtwert = 0
    for artikel in inhalt_als_dict:
        wert = artikel[PREIS] * artikel[BESTAND]
        gesamtwert += wert
    print(f"\nGesamtwert des Lagers:  - {gesamtwert:.2f}")

datei_name = "./wiederholung/artikel.txt"
inhalt = lese_aus_datei(datei_name)

if len(inhalt) > 0:
    #verarbeiten Daten in Liste
    inhalt = entferne_whitespaces_und_verarbeite_artikel(inhalt)
    #Daten in geeignete Datenstruktur umwandeln
    artikel_liste_als_dict = dump_in_dictionary(inhalt)
    #formatierte Ausgabe
    ausgabe(artikel_liste_als_dict)
    #gefilterte Ausgabe
    ausgabe_gefiltert(artikel_liste_als_dict, filtere_nach=BESTAND, anzahl=5)
    #Lagerwert je Artikel
    berechne_artikel_wert(artikel_liste_als_dict)
    berechne_artikel_gesamtwert(artikel_liste_als_dict)
else:
    print("Datei ist leer")

