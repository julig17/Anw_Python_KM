
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

def entferne_whitespaces(inhalt):
    for i in range(len(inhalt)):
        inhalt[i] = inhalt[i].strip()   
    return inhalt


def verarbeite_artikel(inhalt):
    for i in range(len(inhalt)):
        inhalt[i] = inhalt[i].split(';')   
    return inhalt



datei_name = "./wiederholung/artikel.txt"
inhalt = lese_aus_datei(datei_name)

if len(inhalt) > 0:
    inhalt = entferne_whitespaces(inhalt)
    inhalt = verarbeite_artikel(inhalt)
    print(inhalt)
else:
    print("Datei ist leer")