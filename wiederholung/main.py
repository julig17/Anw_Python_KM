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

datei_name = "./wiederholung/artikel.txt"
inhalt = lese_aus_datei(datei_name)

if len(inhalt) > 0:
    inhalt = entferne_whitespaces_und_verarbeite_artikel(inhalt)
    artikel_liste_als_dict = dump_in_dictionary(inhalt)
    print(artikel_liste_als_dict)
else:
    print("Datei ist leer")

